"""SNMP MIB module (XEROX-GENERAL-TC) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-GENERAL-TC
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:06 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(MibIdentifier,
 IpAddress,
 NotificationType,
 Counter32,
 Gauge32,
 TimeTicks,
 ObjectIdentity,
 ModuleIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 iso,
 Bits,
 Counter64,
 Integer32,
 Unsigned32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "MibIdentifier",
    "IpAddress",
    "NotificationType",
    "Counter32",
    "Gauge32",
    "TimeTicks",
    "ObjectIdentity",
    "ModuleIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "iso",
    "Bits",
    "Counter64",
    "Integer32",
    "Unsigned32")

(TextualConvention,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "DisplayString")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmGeneralTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 50)
)
xcmGeneralTC.setLastUpdated("0704040000Z")
if mibBuilder.loadTexts:
    xcmGeneralTC.setOrganization("""\
Xerox Corporation - XCMI Working Group
""")
xcmGeneralTC.setContactInfo("""\
 XCMI Editors E-Mail: coherence@crt.xerox.com -- --
""")
if mibBuilder.loadTexts:
    xcmGeneralTC.setDescription("""\
 Version: 5.601.pub Xerox General Textual Conventions See section 9
'Supplement' of XCMI General TC for implementation and conformance guidance for
this TC module. Copyright (C) 1995-2005 Xerox Corporation. All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class Cardinal16(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )

    if mibBuilder.loadTexts:
        description = """\
 The representation for non-negative integers. Used for indices in small tables
where 0 means not specified. It avoids use of the sign bit.
"""


class Cardinal32(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The representation for non-negative integers. Used for indices in large tables
where 0 means not specified. Same size as ISO 10175 (avoids use of sign bit).
"""


class Cardinal64High(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The high-order 31 bits of a 62-bit non-negative integer (0..2**62-1). A
manager must get or set the high and low parts in the same operation.
"""


class Cardinal64Low(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The low-order 31 bits of a 62-bit non-negative integer (0..2**62-1). A manager
must get or set the high and low parts in the same operation.
"""


class CodedCountry(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )

    if mibBuilder.loadTexts:
        description = """\
 A two character country or territory abbreviation from ISO/IEC 3166:1993 -
Codes for the Representation of Names of Countries. Examples: US, FR, DE A null
string SHALL indicate that the country or territory is not defined.
"""


class CodedLanguage(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )

    if mibBuilder.loadTexts:
        description = """\
 A two character language abbreviation as defined in ISO/IEC 639:1988 - Codes
For the Representation of Names of Languages. Examples EN, GB, CA, FR, DE. An
empty string SHALL indicate that the language is not defined.
"""


class CodeIndexedStringIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The representation of string data which the agent can provide in one or more
character sets (but not further localized). Typically this representation is
used because the string data is relatively dynamic, changing too rapidly for
full localization; or because the data exists inherently in only one or a
limited number of character sets and cannot meaningfully be further localized.
The value is an index into a single global string table,
xcmGenCodeIndexedStringTable. A subsidiary index into the
xcmGenCodeIndexedStringTable is the IANA registered enum (see the CodedCharSet
textual-convention in RFC 1759) for the coded character set desired by the
management station (from among the coded character sets supported by the SNMP
agent). A 0 index value SHALL indicate that there is no associated entry in the
string table. 32 bits are needed because Jobs can use up 10-12 code-indexed
strings per job.
"""


class Counter64High(TextualConvention, Counter32):
    status = "current"
    if mibBuilder.loadTexts:
        description = """\
 The high-order 32 bits of a 63-bit counter (0..2**63-1). A manager must get or
set the high and low parts in the same operation.
"""


class Counter64Low(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The low-order 31 bits of a 63-bit counter (0..2**63-1). A manager must get or
set the high and low parts in the same operation.
"""


class Gauge64High(TextualConvention, Gauge32):
    status = "current"
    if mibBuilder.loadTexts:
        description = """\
 The high-order 32 bits of a 63-bit gauge (0..2**63-1). A manager must get or
set the high and low parts in the same operation.
"""


class Gauge64Low(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The low-order 31 bits of a 63-bit gauge (0..2**63-1). A manager must get or
set the high and low parts in the same operation.
"""


class Integer64High(TextualConvention, Integer32):
    status = "current"
    if mibBuilder.loadTexts:
        description = """\
 The high-order 32 bits of a 63-bit signed integer (-2**62..2**62-1). A manager
must get or set the high and low parts in the same operation.
"""


class Integer64Low(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The low-order 31 bits of a 63-bit signed integer (-2**62..2**62-1). A manager
must get or set the high and low parts in the same operation.
"""


class Ordinal16(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )

    if mibBuilder.loadTexts:
        description = """\
 The representation for positive integers. Used for indices in small tables
where 0 is illegal. It avoids use of the sign bit..
"""


class Ordinal32(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The representation for positive integers. Same size as ISO 10175 (avoids use
of sign bit).
"""


class Ordinal64High(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The high-order 31 bits of a 62-bit positive integer (1..2**62-1). A manager
must get or set the high and low parts in the same operation.
"""


class Ordinal64Low(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The low-order 31 bits of a 62-bit positive integer (1..2**62-1). A manager
must get or set the high and low parts in the same operation.
"""


class XcmFixedLocaleDisplayString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )

    if mibBuilder.loadTexts:
        description = """\
 This data type is used to model textual information in some localization
(language, country, and character set), which is fixed (ie, NOT capable of
being altered by management station request). This textual information SHALL be
represented in the localization which is indicated by the current value of
'xcmGenFixedLocalizationIndex'.
"""


class XcmFixedLocaleUtf8String(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )

    if mibBuilder.loadTexts:
        description = """\
 This data type is used to model textual information in the UTF-8 character set
and some locale (language/country), which is fixed (ie, NOT capable of being
altered by management station request). This textual information SHALL be
represented in UTF-8 and the locale which is indicated by the current value of
'xcmGenFixedLocalizationIndex'.
"""


class XcmNamedLocaleUtf8String(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )

    if mibBuilder.loadTexts:
        description = """\
 This data type is used to model textual information in the UTF-8 character set
and some locale (language/country), which is named (ie, explicitly named by a
parallel column or attribute or by the operation context).
"""


class XcmGenGroupSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI General MIB object groups which are supported by this management
agent implementation (ie, version) on this host system, specified in a bit-
mask. The current set of values (which MAY be extended in the future) is given
below: 1 : xcmGenCurrentLocalizationGroup -- 2**0 2 : xcmGenLocalizationGroup
-- 2**1 4 : xcmGenCodeIndexedStringGroup -- 2**2 8 : xcmGenCodedCharSetGroup --
2**3 16 : xcmGenFixedLocalizationGroup -- 2**4 32 : xcmGenLockGroup -- 2**5 64
: xcmGenReconfGroup -- 2**6 128 : xcmGenOptionGroup -- 2**7 256 :
xcmGenClientDataGroup -- 2**8 512 : xcmGenTrapClientGroup -- 2**9 1024 :
xcmGenTrapViewGroup -- 2**10 2048 : xcmGenBaseGroup -- 2**11 4096 :
xcmGenMessageMapGroup -- 2**12 8192 : xcmGenMessageTextGroup -- 2**13 16384 :
xcmGenNotifyRuleGroup -- 2**14 32768 : xcmGenNotifyDetailGroup -- 2**15 Usage:
Conforming management agents SHALL accurately report their support for XCMI
General MIB object groups.
"""


class XcmGenLogFullPolicy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disableAndPauseService", 4),
          ("disableService", 3),
          ("enableServiceAndFlushLog", 5),
          ("enableServiceAndFlushOldest", 6),
          ("other", 1),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
 The current policy for handling job/request/event log 'full' (in MIBs, in
shared RAM, on disk, etc), on this host system.
"""


class XcmGenMessageMapStringLabel(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )

    if mibBuilder.loadTexts:
        description = """\
 This syntax is used to specify a Xerox standard or experiemental message
string label associated with the current value of the message string pointed to
by 'xcmGenMessageMapStringIndexOID'. Usage: Experimental message string labels
SHOULD NOT be used in shipping versions of Xerox-branded products or services.
They exist solely to facilitate rapid product development cycles. Usage: All
Xerox message string label values SHALL be specified using display (NOT space)
characters from the IANA registered charset 'utf-8' (ie, the UTF-8 octet-stream
encoding of ISO-10646 UCS-4, described in RFC 2279). Usage: All Xerox message
string label values SHALL contain no more than 64 UTF-8 display characters AND
no more than 128 total octets (in some scripts, less than 64 characters in
UTF-8 octet-stream encoding). Usage: All Xerox message string label values
SHALL conform to the syntax specified below. A 'format', 'namespace', 'module',
or 'field' component SHALL NOT contain hyphens. A 'format', 'namespace', or
'module' component SHALL use lowercase. A 'field' or 'qualifier' component MAY
use mixed case (see examples below). A 'field' component MAY be use an
abbreviated MIB object tag or other standardized identifier. ONLY a terminal
'qualifier' component MAY contain hyphens. Each component SHALL be separated by
a hyphen '-' character. -- Xerox message string label general ABNF syntax
msg_label = format '-' namespace '-' module '-' field '-' qualifier -- Xerox
message string label alternatives ABNF syntax msg_label = std_label / exp_label
Usage: All Xerox standard message string label values SHALL conform to the
refined syntax specified below. -- Xerox standard message label refined ABNF
syntax std_label = std_fmt '-' std_ns '-' module '-' field '-' qualifier --
Xerox standard format std_fmt = 'xs' -- Xerox standard format / 'x?' -- Xerox
reserved formats (2 characters) -- Xerox standard namespace std_ns = 'ansi' --
American National Standards Institute / 'dmtf' -- Desktop Management Task Force
/ 'ecma' -- European Computer Manufacturers Assn / 'ieee' -- Institute
Electrical/Electronic Engineers / 'ietf' -- Internet Engineering Task Force /
'iso' -- Int'l Organization for Standardization / 'itu' -- Int'l
Telecommunication Union (aka CCITT) / 'omg' -- Object Management Group / 'pwg'
-- Printer Working Group / 'xcmi' -- Xerox Common Management Interface /
'xopen' -- X/Open (aka Open Group) / 'w3c' -- World Wide Web Consortium --
Xerox message label common components module = -- module identifier w/out
hyphens field = -- field identifier w/out hyphens qualifier = -- qualifer (MAY
contain hyphens) Examples of well-formed standard message string labels: --
Examples of ISO standard media sizes xs-iso-10175-mediaSize-iso-a4 -- 210 mm by
297 mm xs-iso-10175-mediaSize-iso-b4 -- 250 mm by 353 mm -- Examples of ISO
standard media types xs-iso-10175-mediaType-envelope xs-iso-10175-mediaType-
transparency -- Examples of ISO standard media colors xs-iso-10175-mediaColor-
white xs-iso-10175-mediaColor-yellow -- Examples of standard MIB objects xs-
ietf-rfc1759-alertDescription-coverOpen xs-pwg-jobmon-processingMessage-
completed xs-xcmi-11hostx-deviceDescription-dc230ST Usage: All Xerox
experimental message string label values SHALL conform to the refined syntax
specified below. -- Xerox experimental message label refined ABNF syntax
exp_label = exp_fmt '-' exp_ns '-' module '-' field '-' qualifier -- Xerox
experimental format exp_fmt = 'xx' -- Xerox experimental format -- Xerox
experimental namespace exp_ns = std_ns '.' prod_ns std_ns = -- as defined above
for standard labels prod_ns = -- 'official' / 'working' product identifier --
Xerox message label common components module = -- as defined above for standard
labels field = -- as defined above for standard labels qualifier = -- as
defined above for standard labels Examples of well-formed experimental message
string labels: xx-ietf.dcs265-rfc1759-alertDescription-skyIsFalling xx-
xcmi.dc230-11hostx-deviceDescription-dc230ST xx-xcmi.belize-11hostx-
systemFaultString-missingWidgets Note: New or refined message label syntaxes
MAY be defined in future versions of this XCMI General TC.
"""


class XcmGenNotifyDetailType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              20,
              21,
              22,
              23,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("notifyEventDelay", 21),
          ("notifyEventNames", 20),
          ("notifyMessageContentKeys", 32),
          ("notifyMessageContentText", 33),
          ("notifyMessageHeaderKeys", 30),
          ("notifyMessageHeaderText", 31),
          ("notifyRecipientURI", 10),
          ("notifySeverityFilter", 22),
          ("notifyTrainingFilter", 23),
          ("other", 1),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
 The type of notify detail stored in this conceptual row in
'xcmGenNotifyDetailTable'. Usage: Conforming XCMI management stations and
agents SHALL encode notify details as UTF-8 strings (like SLPv2, RFC 2608). -
Integers SHALL be encoded as (signed) decimal strings. - Booleans SHALL be
encoded as 'true' or 'false' strings. - Strings SHALL be encoded as UTF-8
character strings. - Binary data (e.g., 'userCertificate') SHALL be stored in
SLPv2 opaque encoding (leading '\FF' and escaped octets). Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information in
'xcmGenNotifyDetailString'.
"""


class XcmGenNotifySchemeSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The terse conformance statement of ALL notification URI schemes which are
supported by this management agent implementation (ie, version) on this host
system, specified in a bit-mask. The current set of values (which MAY be
extended in the future) is given below: 1 : uriNotifySNMP -- RFC 1215/1906 -
2**0 (SNMP) 2 : uriNotifyMailto -- RFC 1738/2368 - 2**1 (SMTP) 4 :
uriNotifyHTTP -- RFC 1738/2616 - 2**2 (HTTP) 8 : uriNotifyHTTPS -- RFC
1738/2396 - 2**3 (HTTPS) 16 : uriNotifyFTP -- RFC 1738/959 - 2**4 (FTP) Usage:
Conforming management agents SHALL accurately report their support for
notification URI schemes.
"""


class XcmGenNotifySeverityFilter(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 This type is used to specify a notification severity filter supported by this
management agent for notification traffic in ALL domains specified by
'xcmGenBaseSNMPDomainSupport' and 'xcmGenBaseNotifySchemeSupport' (for URI-
based notification), specified in a bit-mask. The current set of values (which
MAY be extended in the future) is given below: 1 : severityReport -- 2**0
(informational) 2 : severityWarning -- 2**1 (eg, low toner) 4 :
severitySoftError -- 2**2 (non-critical) 8 : severityHardError -- 2**3
(critical) 16 : severityTestReport -- 2**4 (product-specific) 32 :
severityTestWarning -- 2**5 (product-specific) 64 : severityTestSoftError --
2**6 (product-specific) 128 : severityTestHardError -- 2**7 (product-specific)
256 : severityInternalError -- 2**8 (product-specific) Usage: The terminology
'report', 'warning', and 'error' is coherent with the IETF IPP event
notification work-in-progress and with the IETF Printer MIB (RFC 1759). Usage:
Individual trap definitions MAY further constrain which notifications are 'in
scope'. Usage: Conforming management agents SHALL accurately report their
support for notification severity filters.
"""


class XcmGenNotifyTrainingFilter(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 This type is used to specify a notification training filter supported by this
management agent for notification traffic in ALL domains specified by
'xcmGenBaseSNMPDomainSupport' and 'xcmGenBaseNotifySchemeSupport' (for URI-
based notification), specified in a bit-mask. The current set of values (which
MAY be extended in the future) is given below: 1 : trainingOther -- 2**0
(extension) 2 : trainingUnknown -- 2**1 (unknown) 4 : trainingNone -- 2**2
(untrained) 8 : trainingTrained -- 2**3 (trained) 16 : trainingFieldService --
2**4 (field service) 32 : trainingManagement -- 2**5 (management) 64 :
trainingNoIntervention -- 2**6 (management) Usage: The terminology used here is
coherent with the IETF Printer MIB (RFC 1759). Usage: Individual trap
definitions MAY further constrain which notifications are 'in scope'. Usage:
Conforming management agents SHALL accurately report their support for
notification training filters.
"""


class XcmGenOptionValueSyntax(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("integerCounter", 4),
          ("integerEnum", 5),
          ("integerGauge", 6),
          ("integerIndex", 7),
          ("integerNumber", 3),
          ("integerTruthValue", 8),
          ("oidAutonomous", 10),
          ("oidObject", 9),
          ("other", 1),
          ("stringBinary", 11),
          ("stringCodedCharSet", 14),
          ("stringDisplay", 12),
          ("stringDynamicLocalization", 15),
          ("stringLocalization", 13),
          ("stringUtf8Localization", 16),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
 A reconfiguration option, device detail, storage detail, service detail, or
security profile detail value syntax, used by system administrators and end
users to specify the correct value syntax for this option or detail. Usage:
This option or detail value syntax is used to select which of the three value
objects SHALL be used to contain the value of this option or detail. * An
option or detail value syntax of 'oidObject' indicates that 'xcm...ValueOID'
SHALL be used to specify an actual object type, defined with 'OBJECT-TYPE'. *
An option or detail value syntax of 'oidAutonomous' indicates that
'xcm...ValueOID' SHALL be used to specify an autonomous object type, defined
with 'OBJECT-IDENTITY' or simply 'OBJECT IDENTIFIER'. * An option or detail
value syntax of 'stringBinary' indicates that 'xcm...ValueString' SHALL be used
to specify a (possibly) 'binary' (or 'non-printing') value string. * An option
or detail value syntax of 'stringDisplay' indicates that 'xcm...ValueString'
SHALL be used to specify a 'displayable' (or 'printing') value string. * An
option or detail value syntax of 'stringLocalization' indicates that
'xcm...ValueLocalization' (for options) or 'xcmGenFixedLocalizationIndex' (for
details) SHALL be used to control the localization of the value string (with an
underlying type of 'XcmGenFixedLocaleDisplayString'). * An option or detail
value syntax of 'stringCodedCharSet' indicates that 'xcm...ValueCodedCharSet'
(for options) or 'xcmGenFixedLocalizationIndex' (for details) SHALL be used to
control the character set ONLY of the value string (with an underlying type of
'CodeIndexedStringIndex'). * An option or detail value syntax of
'stringDynamicLocalization' indicates that 'xcmGenCurrentLocalization' SHALL be
used to control the localization of the value string (with an underlying type
of 'InternationalDisplayString'). * An option or detail value syntax of
'stringUtf8Localization' indicates that 'xcm...ValueLocalization' (for options)
or 'xcmGenFixedLocalizationIndex' (for details) SHALL be used to control the
localization of the value string (with an underlying type of
'XcmGenFixedLocaleUtf8String').
"""


class XcmGenReconfOptionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("activateForImmediateChange", 6),
          ("activateForImmediateReboot", 8),
          ("activateForRebootChange", 7),
          ("activateInProgress", 9),
          ("idle", 1),
          ("validateForImmediateChange", 2),
          ("validateForImmediateReboot", 4),
          ("validateForRebootChange", 3),
          ("validateInProgress", 5))
    )

    if mibBuilder.loadTexts:
        description = """\
 The processing state of ALL pending reconfiguration options of this host
system. A write to this object by an (authorized) management station invokes a
request for validation (or activation) of ALL pending reconfiguration options
of this host system. A read of this object returns 'idle',
'validateInProgress', or 'activateInProgress' to report the processing state of
the last 'validate...' or 'activate...' request. It is mandatory that a
conforming management agent ensure that, at system initialization, this object
SHALL be set to a value of 'idle'. * 'idle' - NO processing is 'in progress'
for either 'validate...' or 'activate...' of any pending reconfiguration
options. * 'validateForImmediateChange' - this management agent (and host
system) SHALL perform ALL possible and appropriate validation of ALL pending
reconfiguration options (reporting the FIRST error encountered during
validation), so that reconfiguration could be performed successfully via
'activateForImmediateChange'. * 'validateForRebootChange' - this management
agent (and host system) SHALL perform ALL possible and appropriate validation
of ALL pending reconfiguration options (reporting the FIRST error encountered
during validation), so that reconfiguration could be performed successfully via
'activateForRebootChange'. * 'validateForImmediateReboot' - this management
agent (and host system) SHALL perform ALL possible and appropriate validation
of ALL pending reconfiguration options (reporting the FIRST error encountered
during validation), so that reconfiguration could be performed successfully via
'activateForImmediateReboot'. * 'validateInProgress' - indicates that this
management agent (and host system) are currently performing validation of ALL
pending reconfiguration options. Note: Conforming implementations NEED NOT
support more than ONE of the above three 'validation...' operations. *
'activateForImmediateChange' - this management agent (and host system) SHALL
perform immediate reconfiguration, NOT reboot, for ALL pending reconfiguration
options (reporting the FIRST error encountered during validation). For all
conforming implementations, this reconfiguration SHALL ALWAYS take effect
immediately, WITHOUT host system reboot! Note: Conforming implementations are
STRONGLY encouraged to consider supporting 'benign' reconfiguration in this
manner. * 'activateForRebootChange' - this management agent (and host system)
SHALL perform delayed reconfiguration, NOT reboot, for ALL pending
reconfiguration options (reporting the FIRST error encountered during
validation). For all conforming implementations, this reconfiguration SHALL
ALWAYS take effect delayed, AFTER subsequent host system reboot! Note:
Conforming implementations NEED NOT support 'caching' of multiple outstanding
'sets of reconfiguration' in this manner. * 'activateForImmediateReboot' - this
management agent (and host system) SHALL perform immediate reconfiguration, AND
reboot, for ALL pending reconfiguration options (reporting the FIRST error
encountered during validation). For all conforming implementations, this
reconfiguration SHALL ALWAYS take effect immediately, WITH host system reboot!
Note: Conforming implementations are STRONGLY encouraged to consider secure
alternatives (eg, Device Mgmt) for system reset. * 'activateInProgress' -
indicates that this management agent (and host system) are currently performing
activation of ALL pending reconfiguration options. Note: Conforming
implementations NEED NOT support more than ONE of the above three
'activation...' operations.
"""


class XcmGenRowPersistence(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nonvolatile", 4),
          ("other", 1),
          ("permanent", 5),
          ("readonly", 6),
          ("unknown", 2),
          ("volatile", 3))
    )

    if mibBuilder.loadTexts:
        description = """\
 This type is used to specify the persistence of this conceptual row in a
table. Usage: Conforming management agents SHALL interpret persistence as
follows: 1) 'volatile' rows NEED NOT be saved across power cycles, MAY contain
one or more 'read-[create|write|only]' objects, and their underlying storage
MAY be removable, and conforming management agents NEED NOT delete such rows
(eg, a block in RAM, PCMCIA card, etc); 2) 'nonvolatile' rows SHALL be saved
across power cycles, MAY contain one or more 'read-[write|only]' objects, and
their underlying storage MAY be removable, and conforming management agents MAY
delete such rows (eg, a sector on CD-ROM, font cartridge, hard disk, etc); 3)
'permanent' rows SHALL be saved across power cycles, MAY contain one or more
'read-[write|only]' objects, and their underlying storage SHALL NOT be
removable, and conforming management agents SHALL NOT delete such rows (eg, a
sector on EEPROM, battery-backed RAM, bubble, etc); 4) 'readonly' rows SHALL be
saved across power cycles, SHALL contain exclusively 'read-only' objects, and
their underlying storage SHALL NOT be removable, and conforming management
agents SHALL NOT delete such rows (eg, a sector on ROM, ASIC, etc). Usage:
Dynamically created rows MAY ONLY be given 'volatile' or 'nonvolatile'
persistence. Note: Equivalent to SNMPv2 'StorageType' textual convention, which
has an unfortunately ambiguous name.
"""


class XcmGenSNMPDomain(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10,
              11,
              20,
              21,
              30)
        )
    )
    namedValues = NamedValues(
        *(("snmpCLNSDomain", 2),
          ("snmpCONSDomain", 3),
          ("snmpDDPDomain", 4),
          ("snmpIPHostNameDomain", 21),
          ("snmpIPXDomain", 5),
          ("snmpNetBEUIDomain", 11),
          ("snmpNetBIOSDomain", 10),
          ("snmpTCPDomain", 20),
          ("snmpUDPDomain", 1),
          ("uriNotifyDomain", 30))
    )

    if mibBuilder.loadTexts:
        description = """\
 This type is used to specify a transport domain (address and name space) which
is supported by this management agent for SNMP protocol traffic (SNMP
responses, SNMP traps, etc), in ALL versions specified by
'xcmGenBaseSNMPVersionSupport'. This type is also used to allow the
'xcmGenTrapClientTable' to be used with any URI scheme (e.g., 'mailto:') for
notifications, by specifying 'uriNotifyDomain'.
"""


class XcmGenSNMPVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("snmpV1Community", 3),
          ("snmpV1Party", 4),
          ("snmpV2Community", 6),
          ("snmpV2Party", 5),
          ("snmpV2Secure", 9),
          ("snmpV2Star", 8),
          ("snmpV2Usec", 7),
          ("snmpV3Secure", 10),
          ("unknown", 1))
    )

    if mibBuilder.loadTexts:
        description = """\
 This type is used to specify an SNMP version (RFC 1157, RFC 1905, etc) which
is supported by this management agent for SNMP protocol traffic (SNMP
responses, SNMP traps, etc), in ALL domains specified by
'xcmGenBaseSNMPDomainSupport'.
"""


class XcmGenSNMPv2ErrorStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("authorizationError", 16),
          ("badValue", 3),
          ("commitFailed", 14),
          ("failedDueToPowerSaverState", 19),
          ("genErr", 5),
          ("inconsistentName", 18),
          ("inconsistentValue", 12),
          ("noAccess", 6),
          ("noCreation", 11),
          ("noError", 0),
          ("noSuchName", 2),
          ("notWritable", 17),
          ("readOnly", 4),
          ("requestTimedOut", 20),
          ("resourceUnavailable", 13),
          ("tooBig", 1),
          ("undoFailed", 15),
          ("wrongEncoding", 9),
          ("wrongLength", 8),
          ("wrongType", 7),
          ("wrongValue", 10))
    )

    if mibBuilder.loadTexts:
        description = """\
 Usage: This type specifies the SMIv2 equivalent of the SMIv1 'ErrorStatus'
textual convention as an enumerated type. Note: The enum of '0' (zero) in this
textual convention is illegal in strict SMIv1 (see section 3.2.1.1 of RFC
1155), so this TC must be converted to an integer range for pure SMIv1.
"""


class XcmGlobalUniqueID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )

    if mibBuilder.loadTexts:
        description = """\
 A management station or management agent specifies an object of type
'GlobalUniqueID' to uniquely label a client job request, a system
administration request, or ANY other managed object (or set of managed objects)
which are required to be unambiguously identified in a distributed network
environment. An object of type 'GlobalUniqueID' SHALL be a textual string
representation in standard 'dotted decimal' form of an OID. An object of type
'GlobalUniqueID' SHALL be composed of three mandatory sections (plus zero or
more optional sections), as follows: nodeID.userID.seqID[[.subID1]...[.subIDn]]
Each of the sections SHALL be separated by a dot ('.'). The three mandatory
sections and any specified optional sections (in left to right order) SHALL be:
1) A globally unambiguous (within at least the network domain of the Requestor
and Responder host systems) dotted decimal 'nodeID' of the Requestor host
system which explicitly or implicitly labelled this managed object, either: a)
A domain specific network layer address (eg, IETF IP address for
'nodeIDTypeIP'); OR b) A domain specific datalink MAC sublayer address (eg, ISO
8802-5 MAC address for 'nodeIDType88025'). 2) A locally unambiguous (within at
least the Requestor and/or Responder host systems) dotted decimal 'userID' (ie,
user identifier) of the user who explicitly or implicitly labelled this managed
object. 3) A locally unambiguous (within at least the Requestor and/or
Responder host systems) dotted decimal 'seqID' (ie, sequence identifier)
assigned by the host system or user who explicitly or implicitly labelled this
managed object. 4) A locally unambiguous (within at least the Requestor and/or
Responder host systems) dotted decimal 'subID' (ie, sequence sub-identifier)
assigned by the host system or user who explicitly or implicitly labelled this
managed object. Usage: Conforming implementations MAY use one or more optional
sections in an 'XcmGlobalUniqueID', for example to assign a sub-job identifier
for job distribution services (e.g., fax to multiple destinations specified in
the PDL of an input 'print' job - using an original 'xcmJobClientId' which is
augmented by the server that splits up the destinations into separate jobs).
Usage: Conforming implementations SHALL NOT specify BOTH the first ('nodeID')
and second ('userID') sections as 'empty', but one OR the other section MAY
take on an 'empty' value (see below). The third ('seqID') section SHALL NOT be
'empty'. Each of the three mandatory sections and any optional sections SHALL
be composed of one mandatory and two optional subsections, as follows:
sectionLength.sectionType.sectionValue Each of the subsections SHALL be
separated by a dot ('.'). The three subsections (in left to right order) SHALL
be: 1) A mandatory 'sectionLength', which specifies the decimal count of dotted
decimal 'components' in the associated 'sectionValue' - this 'sectionLength'
SHALL NOT be self-inclusive and SHALL NOT include the single 'component' of the
'sectionType' - a 'sectionLength' of decimal zero ('0') SHALL indicate an
'empty' section, and the associated two subsections ('sectionType' and
'sectionValue') SHALL be omitted. 2) An optional 'sectionType', selected from
the standard 'sectionType' choices applicable to this section (below). 3) An
optional 'sectionValue', specified as a dotted decimal string of 'components',
each 'component' separated by a dot ('.'). The standard 'sectionType' choices
(one set for each section) SHALL be as follows: 1) 'nodeIDType' -- for
mandatory 'nodeID' section 1 : nodeIDTypeOther -- Other 2 : nodeIDTypeUnknown
-- Unknown 11 : nodeIDTypeIP -- Internet IP 12 : nodeIDTypeCLNS -- OSI CLNS 13
: nodeIDTypeCONS -- OSI CONS 14 : nodeIDTypeDDP -- AppleTalk DDP 15 :
nodeIDTypeIPX -- NetWare IPX 16 : nodeIDTypeNetBIOS -- IBM NetBIOS 31 :
nodeIDType88023 -- ISO 8802-3 (Ethernet LAN) 32 : nodeIDType88024 -- ISO 8802-4
(TokenBus LAN) 33 : nodeIDType88025 -- ISO 8802-5 (TokenRing LAN) 34 :
nodeIDType88026 -- ISO 8802-6 (SlottedRing MAN) 2) 'userIDType' -- for
mandatory 'userID' section 1 : userIDTypeOther -- Other 2 : userIDTypeUnknown
-- Unknown 11 : userIDTypeSystem -- System scope 12 : userIDTypeSubnet --
Subnet scope 13 : userIDTypeNetwork -- Network scope 14 : userIDTypeGlobal --
Global scope 3) 'seqIDType' -- for mandatory 'seqID' section 1 : seqIDTypeOther
-- Other 2 : seqIDTypeUnknown -- Unknown 11 : seqIDTypeSystem -- System
generated 12 : seqIDTypeProcess -- Process generated 13 : seqIDTypeThread --
Thread generated 4) 'subIDType' -- for optional 'subID' sections 1 :
subIDTypeOther -- Other 2 : subIDTypeUnknown -- Unknown 11 : subIDTypeSystem --
System generated 12 : subIDTypeProcess -- Process generated 13 :
subIDTypeThread -- Thread generated Usage: A 'seqID' of any type SHALL be
system-unique. Usage: A 'seqID' of type 'seqIDTypeProcess' SHALL be prefixed
(if necessary) by a system-unique dotted decimal 'processID'. Usage: A 'seqID'
of type 'seqIDTypeThread' SHALL be prefixed (if necessary) by a system-unique
dotted decimal 'threadID' (possibly itself prefixed by a system-unique
'processID'). Example: A request submitted from a client end system running the
IETF Internet Protocol Suite (IPS), with an IP address of '13.240.128.21',
without a specified dotted decimal 'userID', might include an 'xcmJobClientId'
of the following form: '4.11.13.240.128.21.0.1.11.3045.1.11.23'
[GlobalUniqueID] |---------1--------|2|----3----|---4---| [Sections] 1) The
mandatory first section ('nodeID') consists of: a) 'sectionLength' of '4'; b)
'sectionType' of '11' ('nodeIDTypeIP'); and c) 'sectionValue' of
'13.240.128.21' (4 components). 2) The mandatory second section ('userID')
consists of: a) 'sectionLength' of '0' (ie, 'empty' section). 3) The mandatory
third section ('seqID') consists of: a) 'sectionLength' of '1'; b)
'sectionType' of '11' ('seqIDTypeSystem'); and c) 'sectionValue' of '3045' (one
component). 4) The optional fourth section ('subID') consists of: a)
'sectionLength' of '1'; b) 'sectionType' of '11' ('subIDTypeSystem'); and c)
'sectionValue' of '23' (one component).
"""


# MIB Managed Objects in the order of their OIDs

_ZeroDotZero_ObjectIdentity = ObjectIdentity
zeroDotZero = _ZeroDotZero_ObjectIdentity(
    (0, 0)
)
_XcmGenZeroDotZero_ObjectIdentity = ObjectIdentity
xcmGenZeroDotZero = _XcmGenZeroDotZero_ObjectIdentity(
    (0, 0, 0)
)
if mibBuilder.loadTexts:
    xcmGenZeroDotZero.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenZeroDotZero.setDescription("""\
 A value used for null object identifiers prior to XCMI v5.1. Do not use.
Instead use the standard definition in RFC 1902/2578 - 'zeroDotZero' - left
here for compatibility.
""")
_XCmGeneralDummy_ObjectIdentity = ObjectIdentity
xCmGeneralDummy = _XCmGeneralDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999)
)
_XCmGenCardinal16_Type = Cardinal16
_XCmGenCardinal16_Object = MibScalar
xCmGenCardinal16 = _XCmGenCardinal16_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 1),
    _XCmGenCardinal16_Type()
)
xCmGenCardinal16.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCardinal16.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenCardinal16.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenCardinal32_Type = Cardinal32
_XCmGenCardinal32_Object = MibScalar
xCmGenCardinal32 = _XCmGenCardinal32_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 2),
    _XCmGenCardinal32_Type()
)
xCmGenCardinal32.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCardinal32.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenCardinal32.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenCardinal64High_Type = Cardinal64High
_XCmGenCardinal64High_Object = MibScalar
xCmGenCardinal64High = _XCmGenCardinal64High_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 3),
    _XCmGenCardinal64High_Type()
)
xCmGenCardinal64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCardinal64High.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenCardinal64High.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenCardinal64Low_Type = Cardinal64Low
_XCmGenCardinal64Low_Object = MibScalar
xCmGenCardinal64Low = _XCmGenCardinal64Low_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 4),
    _XCmGenCardinal64Low_Type()
)
xCmGenCardinal64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCardinal64Low.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenCardinal64Low.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenCodedCountry_Type = CodedCountry
_XCmGenCodedCountry_Object = MibScalar
xCmGenCodedCountry = _XCmGenCodedCountry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 5),
    _XCmGenCodedCountry_Type()
)
xCmGenCodedCountry.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCodedCountry.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenCodedCountry.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenCodedLanguage_Type = CodedLanguage
_XCmGenCodedLanguage_Object = MibScalar
xCmGenCodedLanguage = _XCmGenCodedLanguage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 6),
    _XCmGenCodedLanguage_Type()
)
xCmGenCodedLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCodedLanguage.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenCodedLanguage.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenCodeIndexedStringIndex_Type = CodeIndexedStringIndex
_XCmGenCodeIndexedStringIndex_Object = MibScalar
xCmGenCodeIndexedStringIndex = _XCmGenCodeIndexedStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 7),
    _XCmGenCodeIndexedStringIndex_Type()
)
xCmGenCodeIndexedStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCodeIndexedStringIndex.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenCodeIndexedStringIndex.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenCounter64High_Type = Counter64High
_XCmGenCounter64High_Object = MibScalar
xCmGenCounter64High = _XCmGenCounter64High_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 8),
    _XCmGenCounter64High_Type()
)
xCmGenCounter64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCounter64High.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenCounter64High.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenCounter64Low_Type = Counter64Low
_XCmGenCounter64Low_Object = MibScalar
xCmGenCounter64Low = _XCmGenCounter64Low_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 9),
    _XCmGenCounter64Low_Type()
)
xCmGenCounter64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCounter64Low.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenCounter64Low.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenGauge64High_Type = Gauge64High
_XCmGenGauge64High_Object = MibScalar
xCmGenGauge64High = _XCmGenGauge64High_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 10),
    _XCmGenGauge64High_Type()
)
xCmGenGauge64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenGauge64High.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenGauge64High.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenGauge64Low_Type = Gauge64Low
_XCmGenGauge64Low_Object = MibScalar
xCmGenGauge64Low = _XCmGenGauge64Low_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 11),
    _XCmGenGauge64Low_Type()
)
xCmGenGauge64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenGauge64Low.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenGauge64Low.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenInteger64High_Type = Integer64High
_XCmGenInteger64High_Object = MibScalar
xCmGenInteger64High = _XCmGenInteger64High_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 12),
    _XCmGenInteger64High_Type()
)
xCmGenInteger64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenInteger64High.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenInteger64High.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenInteger64Low_Type = Integer64Low
_XCmGenInteger64Low_Object = MibScalar
xCmGenInteger64Low = _XCmGenInteger64Low_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 13),
    _XCmGenInteger64Low_Type()
)
xCmGenInteger64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenInteger64Low.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenInteger64Low.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenOrdinal16_Type = Ordinal16
_XCmGenOrdinal16_Object = MibScalar
xCmGenOrdinal16 = _XCmGenOrdinal16_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 14),
    _XCmGenOrdinal16_Type()
)
xCmGenOrdinal16.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenOrdinal16.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenOrdinal16.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenOrdinal32_Type = Ordinal32
_XCmGenOrdinal32_Object = MibScalar
xCmGenOrdinal32 = _XCmGenOrdinal32_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 15),
    _XCmGenOrdinal32_Type()
)
xCmGenOrdinal32.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenOrdinal32.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenOrdinal32.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenOrdinal64High_Type = Ordinal64High
_XCmGenOrdinal64High_Object = MibScalar
xCmGenOrdinal64High = _XCmGenOrdinal64High_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 16),
    _XCmGenOrdinal64High_Type()
)
xCmGenOrdinal64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenOrdinal64High.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenOrdinal64High.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenOrdinal64Low_Type = Ordinal64Low
_XCmGenOrdinal64Low_Object = MibScalar
xCmGenOrdinal64Low = _XCmGenOrdinal64Low_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 17),
    _XCmGenOrdinal64Low_Type()
)
xCmGenOrdinal64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenOrdinal64Low.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenOrdinal64Low.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenFixedLocaleDisplayString_Type = XcmFixedLocaleDisplayString
_XCmGenFixedLocaleDisplayString_Object = MibScalar
xCmGenFixedLocaleDisplayString = _XCmGenFixedLocaleDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 18),
    _XCmGenFixedLocaleDisplayString_Type()
)
xCmGenFixedLocaleDisplayString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenFixedLocaleDisplayString.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenFixedLocaleDisplayString.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenGroupSupport_Type = XcmGenGroupSupport
_XCmGenGroupSupport_Object = MibScalar
xCmGenGroupSupport = _XCmGenGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 19),
    _XCmGenGroupSupport_Type()
)
xCmGenGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenGroupSupport.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenLogFullPolicy_Type = XcmGenLogFullPolicy
_XCmGenLogFullPolicy_Object = MibScalar
xCmGenLogFullPolicy = _XCmGenLogFullPolicy_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 20),
    _XCmGenLogFullPolicy_Type()
)
xCmGenLogFullPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenLogFullPolicy.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenLogFullPolicy.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenOptionValueSyntax_Type = XcmGenOptionValueSyntax
_XCmGenOptionValueSyntax_Object = MibScalar
xCmGenOptionValueSyntax = _XCmGenOptionValueSyntax_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 21),
    _XCmGenOptionValueSyntax_Type()
)
xCmGenOptionValueSyntax.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenOptionValueSyntax.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenOptionValueSyntax.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenReconfOptionState_Type = XcmGenReconfOptionState
_XCmGenReconfOptionState_Object = MibScalar
xCmGenReconfOptionState = _XCmGenReconfOptionState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 22),
    _XCmGenReconfOptionState_Type()
)
xCmGenReconfOptionState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenReconfOptionState.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenReconfOptionState.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenRowPersistence_Type = XcmGenRowPersistence
_XCmGenRowPersistence_Object = MibScalar
xCmGenRowPersistence = _XCmGenRowPersistence_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 23),
    _XCmGenRowPersistence_Type()
)
xCmGenRowPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenRowPersistence.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenRowPersistence.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenSNMPDomain_Type = XcmGenSNMPDomain
_XCmGenSNMPDomain_Object = MibScalar
xCmGenSNMPDomain = _XCmGenSNMPDomain_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 24),
    _XCmGenSNMPDomain_Type()
)
xCmGenSNMPDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenSNMPDomain.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenSNMPDomain.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenSNMPVersion_Type = XcmGenSNMPVersion
_XCmGenSNMPVersion_Object = MibScalar
xCmGenSNMPVersion = _XCmGenSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 25),
    _XCmGenSNMPVersion_Type()
)
xCmGenSNMPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenSNMPVersion.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenSNMPVersion.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenSNMPv2ErrorStatus_Type = XcmGenSNMPv2ErrorStatus
_XCmGenSNMPv2ErrorStatus_Object = MibScalar
xCmGenSNMPv2ErrorStatus = _XCmGenSNMPv2ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 26),
    _XCmGenSNMPv2ErrorStatus_Type()
)
xCmGenSNMPv2ErrorStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenSNMPv2ErrorStatus.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenSNMPv2ErrorStatus.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenGlobalUniqueID_Type = XcmGlobalUniqueID
_XCmGenGlobalUniqueID_Object = MibScalar
xCmGenGlobalUniqueID = _XCmGenGlobalUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 27),
    _XCmGenGlobalUniqueID_Type()
)
xCmGenGlobalUniqueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenGlobalUniqueID.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenGlobalUniqueID.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenFixedLocaleUtf8String_Type = XcmFixedLocaleUtf8String
_XCmGenFixedLocaleUtf8String_Object = MibScalar
xCmGenFixedLocaleUtf8String = _XCmGenFixedLocaleUtf8String_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 28),
    _XCmGenFixedLocaleUtf8String_Type()
)
xCmGenFixedLocaleUtf8String.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenFixedLocaleUtf8String.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenFixedLocaleUtf8String.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenMessageMapStringLabel_Type = XcmGenMessageMapStringLabel
_XCmGenMessageMapStringLabel_Object = MibScalar
xCmGenMessageMapStringLabel = _XCmGenMessageMapStringLabel_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 29),
    _XCmGenMessageMapStringLabel_Type()
)
xCmGenMessageMapStringLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenMessageMapStringLabel.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenMessageMapStringLabel.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenNamedLocaleUtf8String_Type = XcmNamedLocaleUtf8String
_XCmGenNamedLocaleUtf8String_Object = MibScalar
xCmGenNamedLocaleUtf8String = _XCmGenNamedLocaleUtf8String_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 30),
    _XCmGenNamedLocaleUtf8String_Type()
)
xCmGenNamedLocaleUtf8String.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenNamedLocaleUtf8String.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenNamedLocaleUtf8String.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenNotifySchemeSupport_Type = XcmGenNotifySchemeSupport
_XCmGenNotifySchemeSupport_Object = MibScalar
xCmGenNotifySchemeSupport = _XCmGenNotifySchemeSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 31),
    _XCmGenNotifySchemeSupport_Type()
)
xCmGenNotifySchemeSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenNotifySchemeSupport.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenNotifySchemeSupport.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenNotifySeverityFilter_Type = XcmGenNotifySeverityFilter
_XCmGenNotifySeverityFilter_Object = MibScalar
xCmGenNotifySeverityFilter = _XCmGenNotifySeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 32),
    _XCmGenNotifySeverityFilter_Type()
)
xCmGenNotifySeverityFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenNotifySeverityFilter.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenNotifySeverityFilter.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenNotifyTrainingFilter_Type = XcmGenNotifyTrainingFilter
_XCmGenNotifyTrainingFilter_Object = MibScalar
xCmGenNotifyTrainingFilter = _XCmGenNotifyTrainingFilter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 33),
    _XCmGenNotifyTrainingFilter_Type()
)
xCmGenNotifyTrainingFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenNotifyTrainingFilter.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenNotifyTrainingFilter.setDescription("""\
Dummy - DO NOT USE
""")
_XCmGenNotifyDetailType_Type = XcmGenNotifyDetailType
_XCmGenNotifyDetailType_Object = MibScalar
xCmGenNotifyDetailType = _XCmGenNotifyDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 34),
    _XCmGenNotifyDetailType_Type()
)
xCmGenNotifyDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenNotifyDetailType.setStatus("current")
if mibBuilder.loadTexts:
    xCmGenNotifyDetailType.setDescription("""\
Dummy - DO NOT USE
""")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-GENERAL-TC",
    **{"Cardinal16": Cardinal16,
       "Cardinal32": Cardinal32,
       "Cardinal64High": Cardinal64High,
       "Cardinal64Low": Cardinal64Low,
       "CodedCountry": CodedCountry,
       "CodedLanguage": CodedLanguage,
       "CodeIndexedStringIndex": CodeIndexedStringIndex,
       "Counter64High": Counter64High,
       "Counter64Low": Counter64Low,
       "Gauge64High": Gauge64High,
       "Gauge64Low": Gauge64Low,
       "Integer64High": Integer64High,
       "Integer64Low": Integer64Low,
       "Ordinal16": Ordinal16,
       "Ordinal32": Ordinal32,
       "Ordinal64High": Ordinal64High,
       "Ordinal64Low": Ordinal64Low,
       "XcmFixedLocaleDisplayString": XcmFixedLocaleDisplayString,
       "XcmFixedLocaleUtf8String": XcmFixedLocaleUtf8String,
       "XcmNamedLocaleUtf8String": XcmNamedLocaleUtf8String,
       "XcmGenGroupSupport": XcmGenGroupSupport,
       "XcmGenLogFullPolicy": XcmGenLogFullPolicy,
       "XcmGenMessageMapStringLabel": XcmGenMessageMapStringLabel,
       "XcmGenNotifyDetailType": XcmGenNotifyDetailType,
       "XcmGenNotifySchemeSupport": XcmGenNotifySchemeSupport,
       "XcmGenNotifySeverityFilter": XcmGenNotifySeverityFilter,
       "XcmGenNotifyTrainingFilter": XcmGenNotifyTrainingFilter,
       "XcmGenOptionValueSyntax": XcmGenOptionValueSyntax,
       "XcmGenReconfOptionState": XcmGenReconfOptionState,
       "XcmGenRowPersistence": XcmGenRowPersistence,
       "XcmGenSNMPDomain": XcmGenSNMPDomain,
       "XcmGenSNMPVersion": XcmGenSNMPVersion,
       "XcmGenSNMPv2ErrorStatus": XcmGenSNMPv2ErrorStatus,
       "XcmGlobalUniqueID": XcmGlobalUniqueID,
       "zeroDotZero": zeroDotZero,
       "xcmGenZeroDotZero": xcmGenZeroDotZero,
       "xcmGeneralTC": xcmGeneralTC,
       "xCmGeneralDummy": xCmGeneralDummy,
       "xCmGenCardinal16": xCmGenCardinal16,
       "xCmGenCardinal32": xCmGenCardinal32,
       "xCmGenCardinal64High": xCmGenCardinal64High,
       "xCmGenCardinal64Low": xCmGenCardinal64Low,
       "xCmGenCodedCountry": xCmGenCodedCountry,
       "xCmGenCodedLanguage": xCmGenCodedLanguage,
       "xCmGenCodeIndexedStringIndex": xCmGenCodeIndexedStringIndex,
       "xCmGenCounter64High": xCmGenCounter64High,
       "xCmGenCounter64Low": xCmGenCounter64Low,
       "xCmGenGauge64High": xCmGenGauge64High,
       "xCmGenGauge64Low": xCmGenGauge64Low,
       "xCmGenInteger64High": xCmGenInteger64High,
       "xCmGenInteger64Low": xCmGenInteger64Low,
       "xCmGenOrdinal16": xCmGenOrdinal16,
       "xCmGenOrdinal32": xCmGenOrdinal32,
       "xCmGenOrdinal64High": xCmGenOrdinal64High,
       "xCmGenOrdinal64Low": xCmGenOrdinal64Low,
       "xCmGenFixedLocaleDisplayString": xCmGenFixedLocaleDisplayString,
       "xCmGenGroupSupport": xCmGenGroupSupport,
       "xCmGenLogFullPolicy": xCmGenLogFullPolicy,
       "xCmGenOptionValueSyntax": xCmGenOptionValueSyntax,
       "xCmGenReconfOptionState": xCmGenReconfOptionState,
       "xCmGenRowPersistence": xCmGenRowPersistence,
       "xCmGenSNMPDomain": xCmGenSNMPDomain,
       "xCmGenSNMPVersion": xCmGenSNMPVersion,
       "xCmGenSNMPv2ErrorStatus": xCmGenSNMPv2ErrorStatus,
       "xCmGenGlobalUniqueID": xCmGenGlobalUniqueID,
       "xCmGenFixedLocaleUtf8String": xCmGenFixedLocaleUtf8String,
       "xCmGenMessageMapStringLabel": xCmGenMessageMapStringLabel,
       "xCmGenNamedLocaleUtf8String": xCmGenNamedLocaleUtf8String,
       "xCmGenNotifySchemeSupport": xCmGenNotifySchemeSupport,
       "xCmGenNotifySeverityFilter": xCmGenNotifySeverityFilter,
       "xCmGenNotifyTrainingFilter": xCmGenNotifyTrainingFilter,
       "xCmGenNotifyDetailType": xCmGenNotifyDetailType}
)
