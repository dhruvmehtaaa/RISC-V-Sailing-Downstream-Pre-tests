let count_word_occurrences filename =
  let channel = open_in filename in
  let word_counts = Hashtbl.create 100 in
  try
    while true do
      let line = input_line channel in
      let words = String.split_on_char ' ' line in
      List.iter (fun word ->
        let count = try Hashtbl.find word_counts word with Not_found -> 0 in
        Hashtbl.replace word_counts word (count + 1)
      ) words
    done
  with End_of_file ->
    close_in channel;
    Hashtbl.iter (fun word count ->
      Printf.printf "Word: %s, Count: %d\n" word count
    ) word_counts;
    ()

let () =
  let filename = "words.txt" in
  count_word_occurrences filename
