# Function definition
sub NumWays{
    local ($mess, $memo, $pos) = @_;
    my $fElement = @$mess - $pos;    
    my $result = 0; 
    print @$mess[$fElement + 2];
    if (@$mess == 0){
        return 1;
    }elsif(@$mess[$fElement] == 0){
        return 0;
    }elsif(@$memo[$pos - 1] != "null"){
        return @$memo[$pos - 1];
    }
    result = NumWays(\@mess, \@memo, $pos - 1);
    if($pos >= 2 && )
}
# Function call
@message = (1,5,6,5,5);   #List to analyze
@dynamicProgramMemo = ();
$size = @message;
foreach $element (@message){
    push @dynamicProgramMemo, "null"; 
} 
$result = NumWays(\@message, \@dynamicProgramMemo, $size);
print $result;
