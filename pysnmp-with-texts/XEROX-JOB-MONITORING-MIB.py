"""SNMP MIB module (XEROX-JOB-MONITORING-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-JOB-MONITORING-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:17 2024
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

(ProductID,
 InternationalDisplayString,
 hrDeviceIndex) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "ProductID",
    "InternationalDisplayString",
    "hrDeviceIndex")

(ModuleCompliance,
 ObjectGroup,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "ObjectGroup",
    "NotificationGroup")

(Counter32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Integer32,
 Gauge32,
 Bits,
 MibIdentifier,
 NotificationType,
 TimeTicks,
 ModuleIdentity,
 ObjectIdentity,
 iso,
 Counter64,
 Unsigned32,
 IpAddress) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Integer32",
    "Gauge32",
    "Bits",
    "MibIdentifier",
    "NotificationType",
    "TimeTicks",
    "ModuleIdentity",
    "ObjectIdentity",
    "iso",
    "Counter64",
    "Unsigned32",
    "IpAddress")

(DisplayString,
 RowStatus,
 DateAndTime,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "DateAndTime",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(zeroDotZero,
 Ordinal32,
 Cardinal64High,
 Ordinal16,
 Cardinal16,
 CodeIndexedStringIndex,
 Cardinal64Low,
 Cardinal32) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "zeroDotZero",
    "Ordinal32",
    "Cardinal64High",
    "Ordinal16",
    "Cardinal16",
    "CodeIndexedStringIndex",
    "Cardinal64Low",
    "Cardinal32")

(XcmHrDevInfoXStatus,
 XcmHrDevTrafficUnit) = mibBuilder.importSymbols(
    "XEROX-HOST-RESOURCES-EXT-TC",
    "XcmHrDevInfoXStatus",
    "XcmHrDevTrafficUnit")

(XcmJMJobXStateReasons,
 XcmJMImpsCountType,
 XcmJMDocOutputMethod,
 XcmJMDocType,
 XcmJMJobState,
 XcmJMJobX2StateReasons,
 XcmJMJobStateReasons,
 XcmJMJobServiceTypeOID,
 XcmJMDocState,
 XcmJMMediumType,
 XcmJMGroupSupport,
 XcmJMDocFileNameType) = mibBuilder.importSymbols(
    "XEROX-JOB-MONITORING-TC",
    "XcmJMJobXStateReasons",
    "XcmJMImpsCountType",
    "XcmJMDocOutputMethod",
    "XcmJMDocType",
    "XcmJMJobState",
    "XcmJMJobX2StateReasons",
    "XcmJMJobStateReasons",
    "XcmJMJobServiceTypeOID",
    "XcmJMDocState",
    "XcmJMMediumType",
    "XcmJMGroupSupport",
    "XcmJMDocFileNameType")

(XcmPrtInterpreterLangFamily,
 XcmPrtMediumSize,
 XcmPrtPrintQuality,
 XcmPrtChannelType) = mibBuilder.importSymbols(
    "XEROX-PRINTER-EXT-TC",
    "XcmPrtInterpreterLangFamily",
    "XcmPrtMediumSize",
    "XcmPrtPrintQuality",
    "XcmPrtChannelType")


# MODULE-IDENTITY

xcmJobMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59)
)
xcmJobMonMIB.setLastUpdated("0206060000Z")
if mibBuilder.loadTexts:
    xcmJobMonMIB.setOrganization("""\
Xerox Common Management Interface Working Group
""")
xcmJobMonMIB.setContactInfo("""\
 XCMI Editors E-Mail: coherence@crt.xerox.com -- --
""")
if mibBuilder.loadTexts:
    xcmJobMonMIB.setDescription("""\
 File: 41jobmon.dfm, .mib, .txt, .pdf Version: 4.03.pub This MIB specifies job
and document objects for monitoring print jobs, including accounting, of print
jobs. This MIB does not provide for management and control of print jobs, such
as cancelling or modifying them. If job control is desired, another MIB that
augments this one should be developed. The groups in this MIB are arranged so
that an additional MIB may be developed that supports monitoring of
multifunction jobs (print, scan, FAX, etc.), including scan-only jobs. Such a
MIB is intended to augment this MIB. See the companion Job Monitoring MIB
textual conventions module: XEROX-JOB-MONITORING-TC for the textual conventions
and for an explanation of the use of this MIB (see file 40jobtc.txt). The
specification for many of the objects in this MIB is taken directly from the
ISO 10175 Document Printing Application (DPA) standard, clause 9.2, Job
Attributes and clause 9.3, Document Attributes. Such direct inclusions are
explicitly indicated. However, this MIB is intended to be used with non-DPA
implementations, so only a small set of general DPA attributes have been
included in the Job Monitoring MIB. In addition, a single print-centric group
is included. Finally, some of the ISO DPA specifications have been generalized
so that they may be used with non-print job services. For example, changing the
names and descriptions from 'printer' to 'device'. All such changes to ISO DPA
text are indicated inside square brackets to make it clear how this Job
Monitoring MIB differs from ISO DPA. Copyright 1996-2002 Xerox Corporation. All
Rights Reserved. REFERENCES See 40jobtc.txt for the conformance requirements
and textual conventions for use with this MIB module.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmJobZeroDummy_ObjectIdentity = ObjectIdentity
xcmJobZeroDummy = _XcmJobZeroDummy_ObjectIdentity(
    (0, 0, 59)
)
_XcmJobMonBase_ObjectIdentity = ObjectIdentity
xcmJobMonBase = _XcmJobMonBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1)
)
_XcmJobMonBaseTable_Object = MibTable
xcmJobMonBaseTable = _XcmJobMonBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2)
)
if mibBuilder.loadTexts:
    xcmJobMonBaseTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMonBaseTable.setDescription("""\
A table of general counters and capabilities for ease of use of the XCMI Job
Monitoring MIB on this host system. Usage: The ONLY valid row in the
'xcmJobMonBaseTable' shall ALWAYS have an 'xcmJobMonBaseIndex' of one ('1').
""")
_XcmJobMonBaseEntry_Object = MibTableRow
xcmJobMonBaseEntry = _XcmJobMonBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1)
)
xcmJobMonBaseEntry.setIndexNames(
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseIndex"),
)
if mibBuilder.loadTexts:
    xcmJobMonBaseEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMonBaseEntry.setDescription("""\
An entry of general counters and capabilities for ease of use of the XCMI Job
Monitoring MIB on this host system. Usage: The ONLY valid row in the
'xcmJobMonBaseTable' shall ALWAYS have an 'xcmJobMonBaseIndex' of one ('1').
""")
_XcmJobMonBaseIndex_Type = Ordinal32
_XcmJobMonBaseIndex_Object = MibTableColumn
xcmJobMonBaseIndex = _XcmJobMonBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 1),
    _XcmJobMonBaseIndex_Type()
)
xcmJobMonBaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmJobMonBaseIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMonBaseIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmJobMonBaseTable'. Usage: The ONLY valid row in the 'xcmJobMonBaseTable'
shall ALWAYS have an 'xcmJobMonBaseIndex' of one ('1').
""")
_XcmJobMonBaseRowStatus_Type = RowStatus
_XcmJobMonBaseRowStatus_Object = MibTableColumn
xcmJobMonBaseRowStatus = _XcmJobMonBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 2),
    _XcmJobMonBaseRowStatus_Type()
)
xcmJobMonBaseRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMonBaseRowStatus.setDescription("""\
This object is used to display status of the ONLY valid conceptual row in the
'xcmJobMonBaseTable'. Usage: 'xcmJobMonBaseRowStatus' is 'read-only' because
the ONLY valid conceptual row shall NOT be deleted.
""")


class _XcmJobMonBaseVersionID_Type(ProductID):
    """Custom type xcmJobMonBaseVersionID based on ProductID"""
    defaultValue = "(0, 0)"


_XcmJobMonBaseVersionID_Object = MibTableColumn
xcmJobMonBaseVersionID = _XcmJobMonBaseVersionID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 3),
    _XcmJobMonBaseVersionID_Type()
)
xcmJobMonBaseVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseVersionID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMonBaseVersionID.setReference("""\
See: 'hrSW[Installed|Run]ID' in the Software Installed and Software Running
groups of the IETF HR MIB (RFC 1514).
""")
if mibBuilder.loadTexts:
    xcmJobMonBaseVersionID.setDescription("""\
The software product ID of the SNMP sub-agent which implements the XCMI Job
Monitoring MIB on this host system. Usage: This object shall specify the
software product ID of an SNMP sub-agent (possibly also found in a conceptual
row in the 'hrSWRunTable' and/or 'hrSWInstalledTable' in the IETF HR MIB). This
object shall NOT specify a particular release of the XCMI Job Monitoring MIB,
or the whole host system product. Note: Contrast with 'sysObjectID' for the
whole SNMP agent in the IETF MIB-II (RFC 1213) and 'hrDeviceID' for the whole
device (or whole product, in the case of 'xcmHrDevice...') in the IETF Host
Resources MIB (RFC 1514).
""")


class _XcmJobMonBaseVersionDate_Type(DateAndTime):
    """Custom type xcmJobMonBaseVersionDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobMonBaseVersionDate_Object = MibTableColumn
xcmJobMonBaseVersionDate = _XcmJobMonBaseVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 4),
    _XcmJobMonBaseVersionDate_Type()
)
xcmJobMonBaseVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseVersionDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMonBaseVersionDate.setReference("""\
See: 'hrSW[Installed|Run]ID' in the Software Installed and Software Running
groups of the IETF HR MIB (RFC 1514).
""")
if mibBuilder.loadTexts:
    xcmJobMonBaseVersionDate.setDescription("""\
The software build date of the SNMP sub-agent which implements the XCMI Job
Monitoring MIB on this host system. Usage: This object shall specify the BUILD
date of the SNMP sub-agent software (not available elsewhere in IETF/XCMI
MIBs). This object shall NOT specify the INSTALL date of the SNMP sub-agent
software on this host system, nor the RESET date. Note: Contrast with
'hrSWInstalledDate' in the Software Installed group of the IETF Host Resources
MIB (RFC 1514), and 'xcmHrDevInfoResetDate' in the Device Info group of the
XCMI Host Resources Extensions MIB.
""")


class _XcmJobMonBaseGroupSupport_Type(XcmJMGroupSupport):
    """Custom type xcmJobMonBaseGroupSupport based on XcmJMGroupSupport"""
    defaultValue = 3


_XcmJobMonBaseGroupSupport_Object = MibTableColumn
xcmJobMonBaseGroupSupport = _XcmJobMonBaseGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 5),
    _XcmJobMonBaseGroupSupport_Type()
)
xcmJobMonBaseGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMonBaseGroupSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Job Monitoring MIB groups supported by this management agent
implementation (i.e., version) on this host system, specified in a bit-mask.
Usage: Conforming management agents shall ALWAYS accurately report their
support for XCMI Job Monitoring MIB groups.
""")
_XcmJobMonBaseCreateSupport_Type = XcmJMGroupSupport
_XcmJobMonBaseCreateSupport_Object = MibTableColumn
xcmJobMonBaseCreateSupport = _XcmJobMonBaseCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 6),
    _XcmJobMonBaseCreateSupport_Type()
)
xcmJobMonBaseCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseCreateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMonBaseCreateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Job Monitoring MIB groups supported for dynamic row creation (via
'...RowStatus') by this management agent implementation (i.e., version) on this
host system, specified in a bit-mask. Usage: Conforming management agents shall
ALWAYS accurately report their support for XCMI Job Monitoring MIB groups.
""")
_XcmJobMonBaseUpdateSupport_Type = XcmJMGroupSupport
_XcmJobMonBaseUpdateSupport_Object = MibTableColumn
xcmJobMonBaseUpdateSupport = _XcmJobMonBaseUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 7),
    _XcmJobMonBaseUpdateSupport_Type()
)
xcmJobMonBaseUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseUpdateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMonBaseUpdateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Job Monitoring MIB groups supported for existing row update (via
SNMP Set-Request PDUs) by this management agent implementation (i.e., version)
on this host system, specified in a bit-mask. Usage: Conforming management
agents shall ALWAYS accurately report their support for XCMI Job Monitoring MIB
groups.
""")
_XcmJobMonMIBConformance_ObjectIdentity = ObjectIdentity
xcmJobMonMIBConformance = _XcmJobMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2)
)
_XcmJobMonMIBGroups_ObjectIdentity = ObjectIdentity
xcmJobMonMIBGroups = _XcmJobMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3)
)
_XcmJobGenBasic_ObjectIdentity = ObjectIdentity
xcmJobGenBasic = _XcmJobGenBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6)
)
_XcmJobGenBasicTable_Object = MibTable
xcmJobGenBasicTable = _XcmJobGenBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenBasicTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobGenBasicTable.setDescription("""\
A table of general mandatory job information per (logical or physical) device
that is independent of the type of device (printer, scanner, fax, ...) and that
does not require a spooling implementation (though a spooling implementation
shall also implement this group, in which case spooled jobs shall also appear
in the job table). Job information applies to the job as a whole or to all its
documents. The specification for most objects is taken directly from the ISO
10175 Document Printing Application (DPA) standard clause 9.2, Job Attributes.
However, this MIB is intended to be used with non-DPA implementations, so only
a small set of general DPA attributes have been included here.
""")
_XcmJobGenBasicEntry_Object = MibTableRow
xcmJobGenBasicEntry = _XcmJobGenBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1)
)
xcmJobGenBasicEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
)
if mibBuilder.loadTexts:
    xcmJobGenBasicEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobGenBasicEntry.setDescription("""\
An entry exists in this table for each job in the device, no matter what the
state of the job is. Each device is represented as a separate device entry in
the Host Resources MIB device table as a device of type 'printer', 'scanner',
'fax', .... The management station references each job using the
xcmJobIdentifierOnSystem assigned by the system (printer, server, supervisor,
spooler) that accepted the job submission (by some other protocol).
""")


class _XcmJobIdentifierOnSystem_Type(DisplayString):
    """Custom type xcmJobIdentifierOnSystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmJobIdentifierOnSystem_Type.__name__ = "DisplayString"
_XcmJobIdentifierOnSystem_Object = MibTableColumn
xcmJobIdentifierOnSystem = _XcmJobIdentifierOnSystem_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 1),
    _XcmJobIdentifierOnSystem_Type()
)
xcmJobIdentifierOnSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobIdentifierOnSystem.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobIdentifierOnSystem.setReference("""\
See note on maximum length of trap var bind that xcmJobIdentifierOnSystem
contributes to: 'xcmJobV2AlertPrefixNew' in the Job Alert Group of this MIB.
""")
if mibBuilder.loadTexts:
    xcmJobIdentifierOnSystem.setDescription("""\
The job identifier generated on the system that the agent is instrumenting. The
job identifier is generated by the job service provider when it accepts a
submit job request from a job service requester using whatever job submission
protocol that the job service provider supports. This job identifier is for
each job and sub job submitted. The job service provider promote a simple job
request to a compound job, if the job service needs access to multiple devices,
such as a scanner and a printer or to two printers, or to a printer and a fax.
See the textual conventions for a more complete description of compound jobs.
The xcmJobIdentifierOnSystem is used as one of the indexes into each job and
document table, along with the HrDeviceIndex from the Host Resources MIB which
is an index value for each different job service instance (analogous to each
instance of a logical printer in ISO DPA). NOTE: Different jobs on different
systems may have the same job identifier. Additional information is needed to
make the job identifier unique in the network, such as the server or system
component name. See also xcmJobIdentifierUpstream in this group. ISO DPA: Job-
identifier This attribute provides the job-identifier for this job on the
server. The server shall generate a job-identifier value that is unique on that
server, but need not be unique across the distributed environment. [In other
words, the server's name need not be part of the job-identifier.] The value of
the job-identifier attribute shall be returned by the server as part of the
PrintResult in the first Print operation for the job (see 8.2.1). The client
shall pass its value as part of the PrintArgument in subsequent Print
operations for the same job.
""")


class _XcmJobIdentifierUpstream_Type(DisplayString):
    """Custom type xcmJobIdentifierUpstream based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmJobIdentifierUpstream_Type.__name__ = "DisplayString"
_XcmJobIdentifierUpstream_Object = MibTableColumn
xcmJobIdentifierUpstream = _XcmJobIdentifierUpstream_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 2),
    _XcmJobIdentifierUpstream_Type()
)
xcmJobIdentifierUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobIdentifierUpstream.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobIdentifierUpstream.setDescription("""\
Uniquely identifies the job on the immediately upstream client, server or
device as generated by that client, server or device. The server or device is
specified by hrDeviceIndex. For an agent representing a spooling system, this
object is the identifier generated by the submitting client and hrDeviceIndex
identifies a logical device. NOTE: Since multiple clients may each generate the
same identifier for the job, the xcmJobIdentifierUpstream is not necessarily
unique on the server. Client implementers are encouraged to generate client job
ids that are unique. In some cases, the xcmJobSourceChannelType may help to
disambiguate client job ids. NOTE: This object in this MIB is a generalization
of the corresponding ISO DPA attribute: job-identifier-on-client which is
printer-centric. ISO DPA: Job-identifier-on-client[-upstream] This attribute
provides the job-identifier for this job to uniquely identify the job on the
client submitting the job, and the value shall be assigned by that client. The
client shall supply the value of the job-identifier-on- client[-upstream]
attribute at the time that the client submits the job to the server, if such
client has its own job-identifier for the job. NOTE - This attribute is
intended for jobs submitted from legacy servers which have their own job-
identifier for the job. If a job passes through a chain of servers between the
client initiating the job and the output device, the value of the job attribute
job-identifier-on-client shall be the value of the job's job-identifier on the
immediate upstream server and the value of the job attribute job-identifier-on-
printer[-device] shall be the value of the job's job-identifier on the
immediate downstream server or printer. NOTE - A job has attributes for
identifying itself on the current server, on the immediate upstream server
(where the job came from), and on the immediate downstream server or printer
(where the job went). These attributes are job-identifier [job-identifier-on-
system] job-identifier-on-client [job-identifier-upstream] job-identifier-on-
printer [job-identifier-downstream] respectively.
""")


class _XcmJobClientId_Type(OctetString):
    """Custom type xcmJobClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmJobClientId_Type.__name__ = "OctetString"
_XcmJobClientId_Object = MibTableColumn
xcmJobClientId = _XcmJobClientId_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 3),
    _XcmJobClientId_Type()
)
xcmJobClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobClientId.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobClientId.setReference("""\
See note on maximum length of trap var bind that xcmJobClientId contributes to:
'xcmJobV2AlertPrefixNew' in the Job Alert Group of this MIB.
""")
if mibBuilder.loadTexts:
    xcmJobClientId.setDescription("""\
A client end system supplies the 'xcmJobClientId' attribute to clearly identify
jobs which that client has submitted to the server. This attribute is used as
one of the indices into the ClientIdMap table. There are two types of job-
submitting clients: 1. XCMI-conforming job submitting clients 2. non-XCMI-
conforming job submitting clients For XCMI-conforming job submitting clients,
the 'xcmJobClientId' shall be a globally unique job id. This globally unique
job id shall be a textual string representation in standard dotted decimal form
of an OID (used in traps related to this job generated by this host system).
See XcmGlobalUniqueID in the Xerox General textual conventions in 06gentc.mib
for a description of the contents required for XCMI-conforming job submitting
clients. For non-XCMI-conforming job submitting clients, the job id may be any
textual string and may not necessarily be unique, even if the job submitter is
a strictly conforming ISO DPA client. ISO DPA: Job-client-id This attribute
supplies a human-readable descriptor for the job. This descriptor may be
printed by the server on auxiliary sheets to help identify the user's printed
output, and discriminate between different jobs. Use and treatment of this
attribute is implementation and site specific. If the client specifies the
value of the job attribute job- client-id, no server shall change it. If the
client does not specify the value of the job attribute job-client-id, the first
server shall set it to the value of the job attribute job- identifier, so that
no downstream server shall change it. These rules ensure that if an
implementation prints the value of the job-client-id on an auxiliary sheet, it
has a value that is meaningful to the client originally submitting the job, no
matter how many servers the job passes through. For example, client A submits a
job to server B and does not specify a value for the job attribute job-client-
id. Server B assigns a job-identifier of 123 to the job, and forwards this job
to server C. Server C assigns a job-identifier of 456 to the job and forwards
this job to printer D. Printer D is not a DPA server, but it has its own queue
and assigns a job-id of 789 to the job. The following table shows the value of
the relevant job attributes in the two servers B and C: job- job- job- job-
client-id identifier- identifier identifier- on-client on-printer ---------
----------- ---------- ----------- server B 123 unspecified 123 456 server C
123 123 456 789* * If printer D did not assign a job-id to its jobs, then the
value of the job attribute job-identifier-on-printer for server C would be
unspecified.
""")


class _XcmJobServiceType_Type(XcmJMJobServiceTypeOID):
    """Custom type xcmJobServiceType based on XcmJMJobServiceTypeOID"""
    defaultValue = "(0, 0)"


_XcmJobServiceType_Object = MibTableColumn
xcmJobServiceType = _XcmJobServiceType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 4),
    _XcmJobServiceType_Type()
)
xcmJobServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobServiceType.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceType.setDescription("""\
Job-service-type (ISO DPA extension) This attribute specifies the type of the
service to which this job was submitted. The value of this object is filled in
by the job service provider, not by the job service requester, depending on the
service-name-requested (instance) parameter supplied by the job service
requester in the create-job operation. The value is an OBJECT IDENTIFIER, so
the implementers, third parties, and customers can add their own service types.
Values are scan-to-file, scan-to-print, print, etc. NOTE - the Host Resources
Extension MIB defines OIDs for device types, which are closely related to job-
service-types. However, job-service-types are related to one or more device
types.
""")
_XcmJobName_Type = CodeIndexedStringIndex
_XcmJobName_Object = MibTableColumn
xcmJobName = _XcmJobName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 5),
    _XcmJobName_Type()
)
xcmJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobName.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobName.setDescription("""\
ISO DPA: Job-name This attribute supplies a human readable string for the
print- job. This string is used for naming the print-job in human- readable
'free-form' fashion. This attribute is intended for enabling a user or the
user's application to convey a job name that may be printed on a start sheet,
returned in a ListObjectAttributes result, or used in notification or logging
messages. If this attribute is not specified, no job name is assumed, but
implementation specific defaults are allowed, such as the value of the
document-name attribute of the first document in the job.
""")
_XcmJobOwner_Type = CodeIndexedStringIndex
_XcmJobOwner_Object = MibTableColumn
xcmJobOwner = _XcmJobOwner_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 6),
    _XcmJobOwner_Type()
)
xcmJobOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobOwner.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobOwner.setDescription("""\
ISO DPA: Job-owner This attribute supplies the name of the human owner of the
print-job. The value of job-owner will often be the same as job- originator.
The job-owner will be different from job-originator when the job has been
submitted by the originator on behalf of the owner. This attribute is not to
take the place of the security parameters or the access-and-accounting
attributes. If this attribute is not specified, the value of user-name or job-
originator should be used for any circumstances which require a value for job-
owner.
""")


class _XcmJobSourceChannelType_Type(XcmPrtChannelType):
    """Custom type xcmJobSourceChannelType based on XcmPrtChannelType"""


_XcmJobSourceChannelType_Object = MibTableColumn
xcmJobSourceChannelType = _XcmJobSourceChannelType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 7),
    _XcmJobSourceChannelType_Type()
)
xcmJobSourceChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobSourceChannelType.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobSourceChannelType.setDescription("""\
Job-source-channel-type (ISO DPA extension) This attribute specifies the type
of channel that is receiving the job from the input device. See XCMI Printer
Extensions TC for values defined by the Printer MIB (RFC 1759).
""")
_XcmJobSubmittedLocaleIndex_Type = Cardinal32
_XcmJobSubmittedLocaleIndex_Object = MibTableColumn
xcmJobSubmittedLocaleIndex = _XcmJobSubmittedLocaleIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 8),
    _XcmJobSubmittedLocaleIndex_Type()
)
xcmJobSubmittedLocaleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobSubmittedLocaleIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobSubmittedLocaleIndex.setDescription("""\
Job-submitted-locale (ISO DPA extension) This object is the locale (country,
territory, and language) index into the xcmGenLocalizationTable specifying the
locale of the submitting user. This object permits a management station to
determine the exact coded character set that the submitting client used, in
case the code conversion that the agent might perform to a different coded
character set is not sufficient. This object also allows the system and the
accounting package to determine the language that the submitting user used for
selecting media. NOTE: ISO DPA has an operation-locale attribute which is
passed as common arguments of every ISO DPA operation. ISO DPA should be
amended to indicate that the server may copy the operation-locale attribute to
the job object, so that the server can remember the locale that the client
specified. Then an agent could copy the value of the coded character set from
the job's operation-locale attribute in order to return as the value of
xcmJobSubmittedLocaleIndex.
""")


class _XcmJobCurrentState_Type(XcmJMJobState):
    """Custom type xcmJobCurrentState based on XcmJMJobState"""


_XcmJobCurrentState_Object = MibTableColumn
xcmJobCurrentState = _XcmJobCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 9),
    _XcmJobCurrentState_Type()
)
xcmJobCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobCurrentState.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobCurrentState.setDescription("""\
ISO DPA: Current-job-state This attribute identifies the current state of the
job (pending, processing, held, etc.) Print clients and DP-Servers shall be
prepared to receive all the standard job states. DP-Servers are not required to
generate all job states, only those which are appropriate for the particular
implementation. It is not conformant for an agent to return the unknown value
if the job's state can be determined. If a server implementation or policy is
to start processing documents before the last Print request (with a TRUE value
for the job-submission-complete parameter) and the value of the job's job-
scheduling attribute is not after-complete, the server shall change the job's
current-job-state from pre- processing [building] directly to the processing
state when the server begins processing any of the job's documents.
""")
_XcmJobStateReasons_Type = XcmJMJobStateReasons
_XcmJobStateReasons_Object = MibTableColumn
xcmJobStateReasons = _XcmJobStateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 10),
    _XcmJobStateReasons_Type()
)
xcmJobStateReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobStateReasons.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobStateReasons.setDescription("""\
This object is bit-encoded, so that multiple reasons can occur at once. Each
bit corresponds to an ISO DPA OID for the same reason. See textual conventions.
ISO DPA: Job-state-reasons This attribute identifies the reason or reasons that
the job is in the held, terminating, retained, or completed state. The server
shall indicate the particular reason(s) by setting the value of the job-state-
reasons attribute. When the job is not in any of these states, the server shall
set the value of the job-state-reasons attribute to the empty set.
""")
_XcmJobXStateReasons_Type = XcmJMJobXStateReasons
_XcmJobXStateReasons_Object = MibTableColumn
xcmJobXStateReasons = _XcmJobXStateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 11),
    _XcmJobXStateReasons_Type()
)
xcmJobXStateReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobXStateReasons.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobXStateReasons.setDescription("""\
This object is bit-encoded, so that multiple reasons can occur at once. Each
bit corresponds to a Xerox extension OID for the same reason. See textual
conventions. ISO DPA: Job-state-reasons (extended with Xerox OIDs) This
attribute identifies the reason or reasons that the job is in the held,
[processing,] terminating, retained, or completed state. The server shall
indicate the particular reason(s) by setting the value of the job-state-reasons
attribute. When the job is not in any of these states, the server shall set the
value of the job-state-reasons attribute to the empty set. See the Xerox Job
Model Specification for the specification of which reasons can be used in which
job states.
""")
_XcmJobX2StateReasons_Type = XcmJMJobX2StateReasons
_XcmJobX2StateReasons_Object = MibTableColumn
xcmJobX2StateReasons = _XcmJobX2StateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 12),
    _XcmJobX2StateReasons_Type()
)
xcmJobX2StateReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobX2StateReasons.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobX2StateReasons.setDescription("""\
This object is bit-encoded, so that multiple reasons can occur at once. Each
bit corresponds to a second set of 31 Xerox extension OIDs for the same reason.
See textual conventions. ISO DPA: Job-state-reasons (extended with Xerox OIDs)
This attribute identifies the reason or reasons that the job is in the held,
[processing,] terminating, retained, or completed state. The server shall
indicate the particular reason(s) by setting the value of the job-state-reasons
attribute. When the job is not in any of these states, the server shall set the
value of the job-state-reasons attribute to the empty set. See the Xerox Job
Model Specification for the specification of which reasons can be used in which
job states.
""")
_XcmDevicesAssigned_ObjectIdentity = ObjectIdentity
xcmDevicesAssigned = _XcmDevicesAssigned_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7)
)
_XcmDevicesAssignedTable_Object = MibTable
xcmDevicesAssignedTable = _XcmDevicesAssignedTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7, 1)
)
if mibBuilder.loadTexts:
    xcmDevicesAssignedTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmDevicesAssignedTable.setDescription("""\
This table contains the hrDeviceIndex values and states of the device(s) to
which this job has been assigned, if the job has been assigned to a physical
device by the job service provider. If the job service provider has not (yet)
assigned the job to a device, there shall not be any rows in this table for the
job. Some implementations assign jobs to physical devices when the job is
submitted which is called early binding. Other implementations delay assigning
jobs to physical devices until the physical device is ready to accept another
job which is called late binding. Late binding is used when load balancing
between several physical devices. NOTE: Some systems may assign a job to more
than one device and progress part of the job on each. Therefore, the device
state is represented as a table. For example, print systems that only assign a
job to a single printer, need only implement a single row of this table. As
another example, multifunction devices/systems that scan and print, in order to
implement a copy service may either: 1. assign a simple job to at least two
devices: a scanner and a printer or 2. create a compound job with a single
device assigned to each contained sub-job.
""")
_XcmDevicesAssignedEntry_Object = MibTableRow
xcmDevicesAssignedEntry = _XcmDevicesAssignedEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7, 1, 1)
)
xcmDevicesAssignedEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmDevicesAssignedHrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmDevicesAssignedEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmDevicesAssignedEntry.setDescription("""\
Entries may exist in the table for each device index whose device type is
'printer', 'scanner', etc. and for each job. See Host Resources MIB and the
XCMI Host Resources Extension MIB where OIDs are assigned for device types.
""")
_XcmDevicesAssignedHrDeviceIndex_Type = Ordinal32
_XcmDevicesAssignedHrDeviceIndex_Object = MibTableColumn
xcmDevicesAssignedHrDeviceIndex = _XcmDevicesAssignedHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7, 1, 1, 1),
    _XcmDevicesAssignedHrDeviceIndex_Type()
)
xcmDevicesAssignedHrDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmDevicesAssignedHrDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmDevicesAssignedHrDeviceIndex.setDescription("""\
The hrDeviceIndex of one of the [physical] devices (printers, scanners, FAX,
etc. to which the job has been assigned. For devices and systems that ensure
that jobs are not lost across crashes and power cycles, these index values
shall remain stable across successive device power cycles. However, if a (low-
end) device is not ensuring that job are persistent across crashes and power
cycles, these index values need not remain stable across such crashes or power
cycles. The representation of the assigned device(s)is an index into the Host
Resources MIB device table, rather than being the distinguished name of the
physical printer as in the ISO DPA printers-assigned attribute. NOTE - The name
of the physical printer [or scanner] is contained in the XCMI Host Resources
Extension MIB table for this device. ISO DPA: Printers-assigned This attribute
identifies the physical [devices] printer or printers to which this job has
been assigned, if any. When the job is first submitted and the server has not
yet assigned any printers to the job, the [table] shall be empty. If the server
intends to use a single printer for the job, and the server has assigned a
printer to the job, [each row] shall contain just that [device]. If a server
has split the job into multiple pieces and assigned each piece to a different
printer, the table shall contain n rows, one for each assigned device. A job
with multiple job-result-sets is an example of a job that would be easy to
split into multiple pieces. A table with no elements shall be returned if this
attribute is supported, but this job has not yet been assigned to any physical
printers [or other devices]. The number of rows in the table for this attribute
shall be the same as the number of rows in the table for the associated job
attribute printer-state-of-printers-assigned [number of rows for the
xcmDeviceStateOfDevicesAssigned table]. In addition, the ith element of each of
these associated attributes shall be a value that pertains to the printer named
by the ith element of printers-assigned. The printers-assigned value shall not
be the same as the printer requested by the user if the job's printer-name-
requested attribute specified a logical printer that supports one or more
different physical printers. The printers-assigned value might differ also if
the job has been re-assigned by an operator to ensure successful completion of
the job, allowing the user to find out where a job has been re-assigned (when
necessary). The value of the job's printers-assigned attribute shall remain
after the job has completed, so that users can determine the physical
printer(s) on which the job was printed.
""")
_XcmDeviceStateOfDevicesAssigned_Type = XcmHrDevInfoXStatus
_XcmDeviceStateOfDevicesAssigned_Object = MibTableColumn
xcmDeviceStateOfDevicesAssigned = _XcmDeviceStateOfDevicesAssigned_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7, 1, 1, 2),
    _XcmDeviceStateOfDevicesAssigned_Type()
)
xcmDeviceStateOfDevicesAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDeviceStateOfDevicesAssigned.setStatus("current")
if mibBuilder.loadTexts:
    xcmDeviceStateOfDevicesAssigned.setDescription("""\
For the MIB, the object applies to scanners, Faxes, etc., as well as printers.
For job services that are purely software or that have software document
transforms that the implementation wishes to expose the state of the software
'engine' may also include rows in this table. The purpose of the
xcmDeviceStateOfDevicesAssigned is to give more detailed information about the
state of a job when the job is in the processing state. Consequently, the value
of this object shall reflect the state of the device only when the job is in
the processing state. When the job is in any other state, the value of the
xcmDeviceStateOfDevicesAssigned object shall be 'unknown'. Changes of the
values of xcmDeviceStateOfDevicesAssigned shall generate a trap. Since the
value of this object shall change only when the job is in the processing state,
traps shall only be generated for changes in xcmDeviceStateOfDevicesAssigned
while the job is in the processing state. Therefore, the
xcmDeviceStateOfDevicesAssigned object shall not generate a trap when the job
is not in the processing state. NOTE: the xcmDeviceStateOfDevicesAssigned is a
duplicate of an object in the Host Resources Extension MIB. But since that
object is in an optional group, xcmDeviceStateOfDevicesAssigned is duplicated
in this deprecated table, so that implementers are not forced to implement the
entire optional group in the HRX MIB, such to get this state of the device that
is part of the overall job state. NOTE: This group and table has been
DEPRECATED, because some devices can be processing more than one job at a time.
However, if the device stops, only one of those jobs is actually affected. So
the deviceStopped bit in the PWG Job Monitoring MIB should be used (on a per
job basis) to indicate that the device has a problem. ISO DPA: Printer-state-
of-printers-assigned This attribute identifies the current state of each
assigned [device] printer. This attribute gives the client access to
information within each assigned printer. Because this attribute contains a
value that is updated within the printer, the server may choose to update the
value of this attribute only when a client [or management station] queries its
value. See the [devices-assigned] printers-assigned attribute for the
correspondence between elements of this attribute and those of [devices-
assigned] printers-assigned.
""")


class _XcmJobIdentifierDownstream_Type(DisplayString):
    """Custom type xcmJobIdentifierDownstream based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmJobIdentifierDownstream_Type.__name__ = "DisplayString"
_XcmJobIdentifierDownstream_Object = MibTableColumn
xcmJobIdentifierDownstream = _XcmJobIdentifierDownstream_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7, 1, 1, 3),
    _XcmJobIdentifierDownstream_Type()
)
xcmJobIdentifierDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobIdentifierDownstream.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobIdentifierDownstream.setDescription("""\
Uniquely identifies the job(s) on the immediately downstream server or device
as generated by that server or device that this system has submitted in order
to perform this job. The downstream server or device is specified by its own
value of hrDeviceIndex. For an agent representing a spooling system, this
object is the identifier generated by that spooling system and hrDeviceIndex
identifies a logical device. NOTE: This object in this MIB is a generalization
of the corresponding ISO DPA attribute: job-identifier-on-printer which is
printer-centric. ISO DPA: job-identifier-on-printer This attribute provides the
job-identifier for this job to uniquely identify it on the printer or next
server downstream, and it shall be assigned by that printer or server. The
value of the job-identifier-on-printer attribute shall be the job-identifier
that the printer or the next server downstream generates at the time the server
submits the job to the printer or the next server downstream. If the printer or
the next server downstream does not generate its own job identifier, the server
shall leave the value of this attribute unspecified. NOTE - This attribute is
intended for jobs submitted to other servers, such as a gateway to a legacy
server, or to printers which have their own internal queue and assign their own
job identifiers.
""")
_XcmClientIdMap_ObjectIdentity = ObjectIdentity
xcmClientIdMap = _XcmClientIdMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 8)
)
_XcmClientIdMapTable_Object = MibTable
xcmClientIdMapTable = _XcmClientIdMapTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 8, 1)
)
if mibBuilder.loadTexts:
    xcmClientIdMapTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmClientIdMapTable.setDescription("""\
A table that maps 1) job identifiers generated by the client that submitted the
job to 2) job identifiers generated by the server that accepted the job.
""")
_XcmClientIdMapEntry_Object = MibTableRow
xcmClientIdMapEntry = _XcmClientIdMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 8, 1, 1)
)
xcmClientIdMapEntry.setIndexNames(
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobClientId"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
)
if mibBuilder.loadTexts:
    xcmClientIdMapEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmClientIdMapEntry.setDescription("""\
Entries exist in this table for each device entry in the Host Resources MIB
device table whose type is 'printer', 'scanner', 'fax', etc. Such a device may
represent a logical, a physical, or a logical-and-physical device, as specified
in the xcmHrDevInfoRealiszation object in the Host Resources Extension MIB. The
Host Resources Extension MIB has OIDs added for use in hrDeviceType. NOTE - The
map table is indexed by both the xcmJobClientId (which the submitting job
service requester may, optionally, supply to identify the job or the client or
user that submitted the job) and the xcmJobIdentifierOnSystem (which the
accepting job service provider shall supply to uniquely identifier the job on
the accepting system. Thus the job service provider guarantees that each map
entry has a unique pair of indices.
""")
_XcmClientIdMapHrDeviceIndex_Type = Ordinal32
_XcmClientIdMapHrDeviceIndex_Object = MibTableColumn
xcmClientIdMapHrDeviceIndex = _XcmClientIdMapHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 8, 1, 1, 2),
    _XcmClientIdMapHrDeviceIndex_Type()
)
xcmClientIdMapHrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmClientIdMapHrDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmClientIdMapHrDeviceIndex.setDescription("""\
The device index from the Host Resources MIB, so that the client can determine
to which (logical or physical) device this job has been submitted.
""")
_XcmJobGenExt_ObjectIdentity = ObjectIdentity
xcmJobGenExt = _XcmJobGenExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10)
)
_XcmJobGenExtTable_Object = MibTable
xcmJobGenExtTable = _XcmJobGenExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenExtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobGenExtTable.setDescription("""\
A table of general job information per (logical or physical) device that is
independent of the type of device and that does not require a spooling
implementation (though a spooling implementation shall also implement this
group, in which case spooled jobs shall also appear in the job table). Job
information applies to the job as a whole or to all its documents. The
specification for most objects is taken directly from the ISO 10175 Document
Printing Application (DPA) standard clause 9.2, Job Attributes. However, this
MIB is intended to be used with non-DPA implementations, so only a small set of
general DPA attributes have been included here.
""")
_XcmJobGenExtEntry_Object = MibTableRow
xcmJobGenExtEntry = _XcmJobGenExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1)
)
xcmJobGenBasicEntry.registerAugmentions(
    ("XEROX-JOB-MONITORING-MIB",
     "xcmJobGenExtEntry")
)
xcmJobGenExtEntry.setIndexNames(*xcmJobGenBasicEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmJobGenExtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobGenExtEntry.setDescription("""\
An entry exists in this table for each job in the device, no matter what the
state of the job is. Each device is represented as a separate device entry in
the Host Resources MIB device table as a device of type 'printer', 'scanner',
'fax', etc. The management station references each job using the
xcmJobIdentifierOnSystem assigned by this (logical for spooling or physical for
non-spooling) device that accepted the job submission (by some other protocol).
This table augments the Job General Basic table in this MIB.
""")
_XcmJobOriginator_Type = CodeIndexedStringIndex
_XcmJobOriginator_Object = MibTableColumn
xcmJobOriginator = _XcmJobOriginator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 1),
    _XcmJobOriginator_Type()
)
xcmJobOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobOriginator.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobOriginator.setDescription("""\
ISO DPA: Job-originator This attribute supplies the name of the human or
programmatic originator of the print-job. If this attribute is not specified,
no value for job originator is assumed, but implementation specific defaults
are allowed. NOTE - This attribute may be different from job-owner (1) when a
program submits the print-job on behalf of a user or (2) when an operator must
resubmit a misprinted job on behalf of the original job owner. However, an
operation to resubmit a print- job is outside the scope of this part of ISO/IEC
10175.
""")
_XcmJobSubmittingApplication_Type = CodeIndexedStringIndex
_XcmJobSubmittingApplication_Object = MibTableColumn
xcmJobSubmittingApplication = _XcmJobSubmittingApplication_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 2),
    _XcmJobSubmittingApplication_Type()
)
xcmJobSubmittingApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobSubmittingApplication.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobSubmittingApplication.setDescription("""\
ISO DPA: (ISO DPA extension) This attribute supplies the name of the
programmatic originator of the print-job, i.e., name of the program that
submitted the job on behalf of the end-user. If this attribute is not
specified, no value for job programmatic originator is assumed, but
implementation-specific defaults are allowed.
""")
_XcmJobComment_Type = CodeIndexedStringIndex
_XcmJobComment_Object = MibTableColumn
xcmJobComment = _XcmJobComment_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 3),
    _XcmJobComment_Type()
)
xcmJobComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobComment.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobComment.setDescription("""\
ISO DPA: Job-comment This attribute supplies an arbitrary human-readable text
string associated with the print-job. This attribute is intended for enabling a
user to convey a text string that may be printed on a job start sheet, for
example, in an implementation-dependent manner.
""")


class _XcmJobCopies_Type(Ordinal32):
    """Custom type xcmJobCopies based on Ordinal32"""
    defaultValue = 1


_XcmJobCopies_Object = MibTableColumn
xcmJobCopies = _XcmJobCopies_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 4),
    _XcmJobCopies_Type()
)
xcmJobCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobCopies.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobCopies.setDescription("""\
For the MIB: this object is generalized so that it applies to scanning as well
as printing. ISO DPA: job-copies (an element of results-profile attribute)
Total number of job copies in the job, i.e., number of job copies summed across
the job-result-sets. If a job contains documents A, B, C, a job-copies value of
2 results in: A, B, C, A, B, C. See ISO DPA results-profile attribute
description for the specification of a job result set and the definition of
job-copies. NOTE - In ISO DPA, job-copies is a separate value for each job
result set, not the summation. But it didn't seem worth the effort to make job-
copies a table since not many systems support multiple job results sets for a
single job.
""")
_XcmJobCopiesCompleted_Type = Counter32
_XcmJobCopiesCompleted_Object = MibTableColumn
xcmJobCopiesCompleted = _XcmJobCopiesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 5),
    _XcmJobCopiesCompleted_Type()
)
xcmJobCopiesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobCopiesCompleted.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobCopiesCompleted.setDescription("""\
For the MIB: this object is generalized so that it applies to scanning as well
as printing. ISO DPA: Job-copies-completed This attribute indicates the number
of job-copies of the job that the printer(s) have completed printing. The
server shall not reset its value during the processing of multiple print-job
results that are part of the same job (see the results-profile job attribute).
Since this attribute is intended to measure the progress of a job, the value
shall include repeated job- copies due to multiple print-job results for the
same job. The accuracy of this value is implementation-dependent. It is
expected that the value reported is never greater than the actual value. This
attribute may not be supported for all printers and all page description
languages. The value of this attribute shall be 0 if printing has not started
for this job.
""")
_XcmJobOutputBinIndex_Type = Integer32
_XcmJobOutputBinIndex_Object = MibTableColumn
xcmJobOutputBinIndex = _XcmJobOutputBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 6),
    _XcmJobOutputBinIndex_Type()
)
xcmJobOutputBinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobOutputBinIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobOutputBinIndex.setDescription("""\
ISO DPA: output-bin Special MIB definition: specifies the index of the output
subunit table for the job. NOTE - ISO DPA allows the output-bin to be specified
differently for each job result set in a job. However, it doesn't seem worth
the effort to make output-bin a table, since multiple job-result-sets is an
unlikely feature to be supported and/or used, especially with different output-
bins.
""")
_XcmJobServiceNameRequested_Type = CodeIndexedStringIndex
_XcmJobServiceNameRequested_Object = MibTableColumn
xcmJobServiceNameRequested = _XcmJobServiceNameRequested_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 7),
    _XcmJobServiceNameRequested_Type()
)
xcmJobServiceNameRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobServiceNameRequested.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceNameRequested.setDescription("""\
Specifies the job service name instance on which the job is to be processed as
specified by the job service requester when the job was submitted. NOTE: this
object has been generalized for use in this MIB from ISO DPA where the
attribute is only a logical or physical printer, not a job service instance,
such as a scan-to-file service instance. ISO DPA: Printer-name-requested This
attribute identifies the printer to be used for printing the job. The client
shall specify the value of this attribute with the first invocation of the
Print operation for the print- job as the explicit printer-name component of
the PrintArgument, rather than as an attribute (see 8.2.1.1). NOTES 1. To cause
a server to select a printer according to other attributes, the System
Administrator should define a logical printer that supports ALL of the physical
printers supported by the server. 2. For the server that supports only a single
printer, the logical printer name may be the same as the server name, as long
as they cannot be confused for each other in the name service directory. 3.
Initial-value-job objects should have the value of their printer-name-requested
attribute specified as an empty value in order to indicate that no printer-name
is defaulted.
""")


class _XcmJobPreviousState_Type(XcmJMJobState):
    """Custom type xcmJobPreviousState based on XcmJMJobState"""


_XcmJobPreviousState_Object = MibTableColumn
xcmJobPreviousState = _XcmJobPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 8),
    _XcmJobPreviousState_Type()
)
xcmJobPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobPreviousState.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobPreviousState.setDescription("""\
This object permits the management application to display the previous job
state to the user without having to monitor all job state changes. For example,
when a job completes, the previous state indicates what the job was doing just
before completing. If the job was printing, then the completion was normal. If
the previous state was terminating, then the completion was abnormal. Another
example, is when a job is paused. The xcmJobPreviousState indicates the state
that the job was in when the job was paused. ISO DPA: job-previous-state This
attribute identifies the state of the job (pending, processing, held, etc.)
before the last change of job state. Standard values are defined in the
specification for the current-job-state [xcmJobCurrentState] job-status
attribute. See textual-conventions.
""")


class _XcmJobEstimatedCompletionTime_Type(DateAndTime):
    """Custom type xcmJobEstimatedCompletionTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobEstimatedCompletionTime_Object = MibTableColumn
xcmJobEstimatedCompletionTime = _XcmJobEstimatedCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 9),
    _XcmJobEstimatedCompletionTime_Type()
)
xcmJobEstimatedCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobEstimatedCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobEstimatedCompletionTime.setDescription("""\
Job Monitoring MIB: If the estimated completion time is unknown, the agent
should return the DEFVAL. This object is a 'best efforts' object, so any
estimate based on any data such as the octet-count or the number of pages
(perhaps obtained from the PostScript commenting conventions up front) is far
preferable than returning the DEFVAL. A learning algorithm based on recent job
sizes and their times could be used. ISO DPA: Estimated-completion-time This
attribute indicates the estimated time by which this job will be completed. The
time to complete one job is dependent on the time required to complete all
other jobs that the scheduling algorithm determines must be printed before this
job may be printed. The time to complete each individual job may depend on when
on- request resources are available. The time to print each individual job is
dependent on the characteristics of the document formats in which the
individual documents of the job are encoded and on the complexities and other
characteristics of the documents themselves. This attribute is highly
implementation-dependent. The estimated-completion-time may be easy to
calculate for some combinations of document formats and scheduling algorithms.
It may be impossible to calculate for other combinations. It is recommended
that, where possible, document creators provide system hints to the print
system (perhaps appropriately encoded in document format headers) that help the
print system understand which features of the document formats the document
will be exercising.
""")


class _XcmJobSubmissionTime_Type(DateAndTime):
    """Custom type xcmJobSubmissionTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobSubmissionTime_Object = MibTableColumn
xcmJobSubmissionTime = _XcmJobSubmissionTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 10),
    _XcmJobSubmissionTime_Type()
)
xcmJobSubmissionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobSubmissionTime.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobSubmissionTime.setDescription("""\
ISO DPA: Submission-time This attribute indicates the time at which the latest
Print request for this job was accepted by the server. An implementation that
can tell time shall return a valid value for this object. Only a device that
cannot tell time shall return the DEFVAL.
""")
_XcmJobPagesCompleted_Type = Counter32
_XcmJobPagesCompleted_Object = MibTableColumn
xcmJobPagesCompleted = _XcmJobPagesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 11),
    _XcmJobPagesCompleted_Type()
)
xcmJobPagesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobPagesCompleted.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobPagesCompleted.setDescription("""\
For the MIB: this object is generalized so that it applies to scanning as well
as printing. ISO DPA: Pages-completed This attribute indicates the number of
pages of the job that the printer(s) have completed printing. NOTE - The number
of source pages, impressions and sheets of media may differ. The following
examples illustrate how they may differ when attributes, rather than the
document contents, control the printing. If number-up is 0 or 1, there is one
source page per impression, and if number-up is 2, there are two source pages
per impression. If sides is 1, there is one impression per sheet of media, but
if sides is 2, there are two impressions per sheet of media. By inference, if
number-up is 4 and sides is 2, there are 4 source pages per impression and 8
source pages per sheet of media. The server shall not reset its value during
the processing of multiple copies of documents or the job. Since this attribute
is intended to measure the progress of a job, the value shall include repeated
pages due to multiple copies. When the job completes, this attribute should
contain the value of the total number of source pages that the printer
processed for the print-job. The accuracy of this value is implementation-
dependent. It is expected that the value reported is never greater than the
actual value. This attribute may not be supported for all printers and all page
description languages. The value of this attribute shall be 0 if printing has
not started for this job.
""")
_XcmJobOctetsCompletedHigh_Type = Cardinal64High
_XcmJobOctetsCompletedHigh_Object = MibTableColumn
xcmJobOctetsCompletedHigh = _XcmJobOctetsCompletedHigh_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 12),
    _XcmJobOctetsCompletedHigh_Type()
)
xcmJobOctetsCompletedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobOctetsCompletedHigh.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobOctetsCompletedHigh.setDescription("""\
For the Job Monitoring MIB: two objects are used to represent a full 62-bit
value. The sign bit of each half is not used. This object is generalized for
use with input devices as well. ISO DPA: Octets-completed [high 31 bits] This
attribute indicates the number of octets of the job that the printer(s)
[devices(s)] have completed printing [processing]. The server shall not reset
its value during the processing of multiple copies of documents or the job.
Since this attribute is intended to measure the progress of a job, the value
shall include repeated pages due to multiple copies. The accuracy of this value
is implementation-dependent. It may be approximated by the number of octets
conveyed to the printer [device]. This attribute may not be supported for all
printers and all page description languages. The value of this attribute shall
be 0 if the device has not started this job.
""")
_XcmJobOctetsCompletedLow_Type = Cardinal64Low
_XcmJobOctetsCompletedLow_Object = MibTableColumn
xcmJobOctetsCompletedLow = _XcmJobOctetsCompletedLow_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 13),
    _XcmJobOctetsCompletedLow_Type()
)
xcmJobOctetsCompletedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobOctetsCompletedLow.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobOctetsCompletedLow.setDescription("""\
ISO DPA: Octets-completed [low 31 bits] See explanation of
xcmJobOctetsCompletedHigh.
""")
_XcmJobErrorCount_Type = Counter32
_XcmJobErrorCount_Object = MibTableColumn
xcmJobErrorCount = _XcmJobErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 14),
    _XcmJobErrorCount_Type()
)
xcmJobErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobErrorCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobErrorCount.setDescription("""\
ISO DPA: Error-count This attribute provides the number of error events
occurring while processing the job.
""")
_XcmJobWarningCount_Type = Counter32
_XcmJobWarningCount_Object = MibTableColumn
xcmJobWarningCount = _XcmJobWarningCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 15),
    _XcmJobWarningCount_Type()
)
xcmJobWarningCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobWarningCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobWarningCount.setDescription("""\
ISO DPA: Warning-count This attribute provides the number of warning events
occurring while processing the job.
""")
_XcmJobProcessingTime_Type = Counter32
_XcmJobProcessingTime_Object = MibTableColumn
xcmJobProcessingTime = _XcmJobProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 16),
    _XcmJobProcessingTime_Type()
)
xcmJobProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobProcessingTime.setUnits("seconds")
if mibBuilder.loadTexts:
    xcmJobProcessingTime.setDescription("""\
ISO DPA: Processing-time This attribute indicates how long an individual job
has been processing [in seconds].
""")
_XcmJobNumberOfDocuments_Type = Cardinal32
_XcmJobNumberOfDocuments_Object = MibTableColumn
xcmJobNumberOfDocuments = _XcmJobNumberOfDocuments_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 17),
    _XcmJobNumberOfDocuments_Type()
)
xcmJobNumberOfDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobNumberOfDocuments.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobNumberOfDocuments.setDescription("""\
ISO DPA: Number-of-documents This attribute indicates the number of documents
in the job. The number indicates how many Print operations that specified a
document (of any document-type have been submitted for printing until job
submission has been completed; at that point this attribute shall then indicate
the total number of printable documents, fonts, and resource objects submitted
by the client in the job. If the first Print operation does not contain a
first-document component (see 8.2.1), the value of this attribute shall be 0.
The server shall count fonts and resource objects passed to the server by means
of Print operation invocations, as documents for the purposes of this
attribute.
""")
_XcmJobAuthorizationUserName_Type = CodeIndexedStringIndex
_XcmJobAuthorizationUserName_Object = MibTableColumn
xcmJobAuthorizationUserName = _XcmJobAuthorizationUserName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 18),
    _XcmJobAuthorizationUserName_Type()
)
xcmJobAuthorizationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobAuthorizationUserName.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobAuthorizationUserName.setReference("""\
See XCMI security MIB (62sectc.txt and 63sec.txt).
""")
if mibBuilder.loadTexts:
    xcmJobAuthorizationUserName.setDescription("""\
The user's name for authorization purposes. The value of
xcmJobAuthorizationUserName may be the same or may be different than the value
of the xcmJobAccountingUserName object, depending on the security system and
the accounting system being used. ISO DPA: User-name This attribute specifies
the name of the user requesting access to print [or other] service operations.
The usage of this attribute may be mandatory, depending upon the local security
policy used.
""")
_XcmDocGenBasic_ObjectIdentity = ObjectIdentity
xcmDocGenBasic = _XcmDocGenBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12)
)
_XcmDocGenBasicTable_Object = MibTable
xcmDocGenBasicTable = _XcmDocGenBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1)
)
if mibBuilder.loadTexts:
    xcmDocGenBasicTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocGenBasicTable.setDescription("""\
A table of general mandatory document information that is per document which in
turn is per job and which in turn is per (logical or physical) device and is
independent of the type of device (printer, scanner, fax, ...) and that does
not require a spooling implementation (though a spooling implementations shall
also implement this group, in which case spooled jobs shall also appear in the
job table). Document information applies to an individual document contained in
a job. The specification for most objects is taken directly from the ISO 10175
Document Printing Application (DPA) standard clause 9.3, Document Attributes.
However, this MIB is intended to be used with non-DPA implementations, so only
a small set of general DPA attributes have been included here.
""")
_XcmDocGenBasicEntry_Object = MibTableRow
xcmDocGenBasicEntry = _XcmDocGenBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1)
)
xcmDocGenBasicEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmDocSequenceNumber"),
)
if mibBuilder.loadTexts:
    xcmDocGenBasicEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocGenBasicEntry.setDescription("""\
An entry exists in this table for each document in each job, no matter what the
state of the job is. Each printer is represented as a separate device entry in
the Host Resources MIB device table as a device of type 'printer', 'scanner', o
'fax', etc. The management station references each job using the
xcmJobIdentifierOnSystem assigned by this (logical for spooling or physical for
non-spooling) device that accepted the job submission (by some other protocol).
""")
_XcmDocSequenceNumber_Type = Ordinal32
_XcmDocSequenceNumber_Object = MibTableColumn
xcmDocSequenceNumber = _XcmDocSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 1),
    _XcmDocSequenceNumber_Type()
)
xcmDocSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocSequenceNumber.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocSequenceNumber.setDescription("""\
For the MIB, a row shall not exist in this table if the job does not (yet) have
any documents. A 32-bit index is required, since the ISO DPA has a 2**31-1
maximum-value integer for the document-sequence-number attribute. ISO DPA:
Document-sequence-number This attribute specifies the number of this document
in relation to the set of documents in this job. The first document in the job
is numbered 1. The document-sequence-number is not passed as an input attribute
in the print operation. Documents are assumed to be submitted in order (i.e.,
document number 1 followed by document number 2, etc.). [If the job service
requester does not submit a document on the first create-job call, no document
row shall be added to this table. The rest of this ISO DPA paragraph does not
apply:] A server shall return a value of 0 for this attribute if the first
Print operation has not submitted a document (e.g., the first-document element
is omitted in the create-job element of the Print operation). If a document is
cancelled in a multi-document job, the document-sequence numbers of the other
documents shall not change.
""")
_XcmDocName_Type = CodeIndexedStringIndex
_XcmDocName_Object = MibTableColumn
xcmDocName = _XcmDocName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 2),
    _XcmDocName_Type()
)
xcmDocName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocName.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocName.setDescription("""\
For the MIB, the single xcmDocName object is both the document name for scan-
to-file and the document name for file-to-print. ISO DPA: Document-name This
attribute supplies a human readable string for the document. This string is
used for naming the document in a human-readable 'free-form' fashion. This
attribute is intended for enabling a user or the user's application to convey a
document name that may be printed on a start sheet, returned in a
ListObjectAttributes result, or used in notification or logging messages. If
this attribute is not specified, no document name is assumed, but
implementation specific defaults are allowed, such as the simple-name part of
the value of the document-file-name attribute. It is suggested, however, that
the server not supply additional text for this attribute when printing its
value (e.g. on a start sheet). This string only has meaning to the clients and
can therefore take several forms, e.g. the name of a mail folder, name of a
revisable document, the file specification minus the file path, the title of a
document, etc.
""")
_XcmDocFileName_Type = CodeIndexedStringIndex
_XcmDocFileName_Object = MibTableColumn
xcmDocFileName = _XcmDocFileName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 3),
    _XcmDocFileName_Type()
)
xcmDocFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocFileName.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocFileName.setDescription("""\
For the MIB, the single xcmDocFileName object is both the document file name
for scan-to-file and the document file name for file-to-print. If this
attribute is specified for a scan-to-print job, the result of the scan is also
copied to the file specified by xcmDocFileName as a side-effect of the scan-to-
print operation. ISO DPA: Document-file-name This attribute specifies the file
name of the document, if the document came from a file. The file name may
include the full path to the file, in which case the name-syntax element of the
DistinguishedNameString data type shall specify the syntax of the file name. If
the document did not come from a file, the client should not specify this
attribute.
""")
_XcmDocFileNameType_Type = XcmJMDocFileNameType
_XcmDocFileNameType_Object = MibTableColumn
xcmDocFileNameType = _XcmDocFileNameType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 4),
    _XcmDocFileNameType_Type()
)
xcmDocFileNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocFileNameType.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocFileNameType.setDescription("""\
The type of file name syntax from which a document is obtained for an output
job, such as print, or for which a document is produced for an input job, such
as scan- to-file. The file name syntax types are taken from ISO DPA for the
DistinguishedNameStringSyntax data type. ISO DPA: distinguished-name-syntax
data type, name-syntax element. See textual-conventions.
""")
_XcmDocType_Type = XcmJMDocType
_XcmDocType_Object = MibTableColumn
xcmDocType = _XcmDocType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 5),
    _XcmDocType_Type()
)
xcmDocType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocType.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocType.setDescription("""\
ISO DPA: Document-type This attribute indicates that the document being passed
by the current Print abstract-operation is either a printable document, a font,
or a resource. How resources are managed during the printing process is
necessarily dependent on the characteristics of the server and printer
implementations. These methods are considered implementation-specific, and
shall not be dictated by ISO/IEC 10175. In particular, ISO/IEC 10175 does not
require that resources be passed in advance of the documents that use them;
i.e., resources may be passed to the server in any order within the job,
subject only to the requirement that the resources be present at the server
before processing begins on the documents that use them.
""")
_XcmDocFormat_Type = XcmPrtInterpreterLangFamily
_XcmDocFormat_Object = MibTableColumn
xcmDocFormat = _XcmDocFormat_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 6),
    _XcmDocFormat_Type()
)
xcmDocFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocFormat.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocFormat.setDescription("""\
The interpreter language family enum value registered by IANA is used according
to the Printer MIB (RFC 1759). See prtInterpreterLangFamily. For the Job
Monitoring MIB, an index into the prtInterpreterTable is not used, since the
exact format of the document need not conform exactly to one of the printer's
intepreters and, furthermore, the device need not even be a printer (so that
the Printer MIB need not be used for non-printers). For scan-to-file jobs, the
xcmDocFormat object specifies the document format desired as a result of the
scan. ISO DPA: Document-format This attribute identifies the overall print
document format used for the document. It consists of three elements, a
document-format, a document-format-variants and a document- format-version. The
latter two elements are optional. The document-format element identifies a
particular family of document formats, of which there may exist several
versions or variants. The document-format-variants and document-format- version
elements identify a specific instance of a document format. The variant refers
to a particular functional subset of a format. For example, the format
PostScript has variants of level 1 and level 2, and the format PCL has several
variants, including PCL4 and PCL5. The version distinguishes among successive
releases of the same basic format and variant. For example, successive versions
of Xerox Interpress include versions 2.0, 2.1, 3.0, 3.1, etc.
""")
_XcmDocFormatVariants_Type = CodeIndexedStringIndex
_XcmDocFormatVariants_Object = MibTableColumn
xcmDocFormatVariants = _XcmDocFormatVariants_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 7),
    _XcmDocFormatVariants_Type()
)
xcmDocFormatVariants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocFormatVariants.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocFormatVariants.setDescription("""\
For scan-to-file jobs, the xcmDocFormatVariants object specifies the document
format variant desired as a result of the scan. ISO DPA: Document-format-
variants The document-format-variants and document-format-version elements
identify a specific instance of a document format. The variant refers to a
particular functional subset of a format. For example, the format PostScript
has variants of level 1 and level 2, and the format PCL has several variants,
including PCL4 and PCL5. The document-format-variants element consists of a
single text string. If it is necessary to identify more than one variant, the
respective variant values shall all be contained in the document-format-
variants element, separated from one another by commas. If the client omits the
document-format-variants or document- format-version elements, the server may
supply a format- specific default which will restrict the outcome of the rules
described in the next paragraph. This rule shall not cause a job to fail in
validation if it would have succeeded with the rules of the next paragraph. If
the client omits the document-format-variants element, the server shall print
the document if the requested printer's document-formats-supported attribute
contains a DocFormat which differs from the specified document-format only in
the value of its document-format-variants. If the document-format-variants is
omitted from the printer document-formats-supported attribute, the printer
shall accept documents with any variant of the specified format. Similar rules
apply if the document-format-version element is omitted. If the client omits
the document-format-variants or document- format-version elements, the server
may supply a format- specific default. Such a default shall be one that could
have matched a document-format according to the rules of the preceding
paragraph. Proprietary values for the document-format, document-format-
variants, and document-format-version elements are assigned by the owners of
those formats. Annex F contains a set of document-formats and variants for
various commercially available formats and variants that are currently in
common use.
""")
_XcmDocFormatVersion_Type = CodeIndexedStringIndex
_XcmDocFormatVersion_Object = MibTableColumn
xcmDocFormatVersion = _XcmDocFormatVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 8),
    _XcmDocFormatVersion_Type()
)
xcmDocFormatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocFormatVersion.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocFormatVersion.setDescription("""\
For scan-to-file jobs, the xcmDocFormatVersion object specifies the document
format version desired as a result of the scan. ISO DPA: Document-format-
version The version distinguishes among successive releases of the same basic
format and variant. For example, successive versions of Xerox Interpress
include versions 2.0, 2.1, 3.0, 3.1, etc.
""")
_XcmDocOctetCount_Type = Cardinal32
_XcmDocOctetCount_Object = MibTableColumn
xcmDocOctetCount = _XcmDocOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 9),
    _XcmDocOctetCount_Type()
)
xcmDocOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocOctetCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocOctetCount.setDescription("""\
For the MIB, the value of the xcmDocOctetCount is used for both scan-to-file
and file-to-print jobs. In the case of scan-to-file jobs, the value starts at 0
and counts the number of octets scanned. ISO DPA: Octet-count This attribute
specifies the size of the document in octets.
""")
_XcmDocState_Type = XcmJMDocState
_XcmDocState_Object = MibTableColumn
xcmDocState = _XcmDocState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 10),
    _XcmDocState_Type()
)
xcmDocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocState.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocState.setDescription("""\
For the MIB, if the document is being scanned and printed in the same simple
job, the xcmDocState object represents the state of the document being printed,
since level 1 scan-to-print jobs must scan directly to the printer. ISO DPA:
Document-state This attribute identifies the current state of the document
[whether being scanned or printed.].
""")
_XcmDocPrintExt_ObjectIdentity = ObjectIdentity
xcmDocPrintExt = _XcmDocPrintExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13)
)
_XcmDocPrintExtTable_Object = MibTable
xcmDocPrintExtTable = _XcmDocPrintExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1)
)
if mibBuilder.loadTexts:
    xcmDocPrintExtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocPrintExtTable.setDescription("""\
A table of print-centric document information which is per document which in
turn is per job and which in turn is per (logical or physical) printer.
Document information applies to an individual document contained in the job.
The specification for most objects is taken directly from the ISO 10175
Document Printing Application (DPA) standard clause 9.3, Document Attributes
and is print-centric. However, this MIB is intended to be used with non-DPA
implementations, so only a small set of general DPA attributes have been
included here.
""")
_XcmDocPrintExtEntry_Object = MibTableRow
xcmDocPrintExtEntry = _XcmDocPrintExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1)
)
xcmDocPrintExtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmDocSequenceNumber"),
)
if mibBuilder.loadTexts:
    xcmDocPrintExtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocPrintExtEntry.setDescription("""\
An entry exists in this table for each job in the device, no matter what the
state of the job is. Each printer is represented as a separate device entry in
the Host Resources MIB device table as a device of type 'printer'. The
management station references each job using the xcmJobIdentifierOnSystem
assigned by this (logical for spooling or physical for non-spooling) device
that accepted the job submission (by some other protocol). The management
station accesses each document in the job using the xcmDocSequenceNumber from
the xcmDocGenBasicTable. This table extends (for print jobs only) the Document
General Basic table in this MIB.
""")


class _XcmDocPrintDefaultMediumName_Type(InternationalDisplayString):
    """Custom type xcmDocPrintDefaultMediumName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmDocPrintDefaultMediumName_Type.__name__ = "InternationalDisplayString"
_XcmDocPrintDefaultMediumName_Object = MibTableColumn
xcmDocPrintDefaultMediumName = _XcmDocPrintDefaultMediumName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 1),
    _XcmDocPrintDefaultMediumName_Type()
)
xcmDocPrintDefaultMediumName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintDefaultMediumName.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocPrintDefaultMediumName.setDescription("""\
The value of this object is the name of the medium that is the default medium
for this document. A null string indicates that neither the submitting client,
nor the system, nor the printer has specified a default medium for this
document. NOTE: This attribute that is supplied by the job service requester is
localizable by the job service provider, since the job service provider must
understand and support the specified value. ISO DPA: Default-medium This
attribute identifies a medium that the server shall use as the medium default
for the pages of the document that require a specification. Standard values are
defined in the specification of the medium- identifier medium attribute. If the
page-media-select attribute is specified (either by the client or by a server
default, i.e., the page-media-select attribute of the initial-value-job object
specified by the logical or physical printer), then the server shall use the
page-media-select value to override the default-medium specification on a page
by page basis. The default-medium attribute may contain a value of id-val-
generic-none (see DPA 9.1.2) indicating that the server shall not use a default
medium. Instead, the server shall rely on lower precedence document attributes
(such as default-input- tray) for the media specification. If the document
data, itself, specifies media, such specification shall override the default-
medium attribute on a page by page basis. If the document data specifies media
which are not also values of media-used, then a printer may receive a document
which requires media that are not ready. In such a case, an implementation may
either abort the document or try printing the document on some alternative
medium, such as the default medium. A client has numerous ways to specify the
media to be used when printing a document and different document pages can be
specified in different ways. The client can specify the media in the document
contents or with attributes. Some attributes override the document contents,
and other attributes may be overridden by the document contents. In addition,
the client can specify the media by name or by the input-tray containing it.
Before printing each page of a document, the server determines the medium or
input-tray for that page by finding the first condition in the list of numbered
steps below that is satisfied. For this discussion, either the medium or the
input- tray is sufficient information: a) If page-media-select has a medium
value for the current page, use that medium, regardless of document contents
and other attributes. b) If input-tray-select has a value, use that tray. c) If
the document contents specify a medium, and that medium is the same as the
value of one of the original-medium elements in the media-substitution
attribute, then use the corresponding substitution-medium in the media-
substitution attribute. d) If the document contents specify a medium, use that
medium. e) If the document contents specify an input-tray, use that input-tray.
f) If the default-medium has a value, and the document format interpreter
allows its use, and that medium is the same as the value of one of the
original-medium elements in media- substitution attribute, then use the
corresponding substitution-medium in the media-substitution attribute. g) If
the default-medium has a value and the document format interpreter allows its
use, use the default-medium. h) If the default-input-tray has a value and the
document format interpreter allows its use, use the default-input-tray. i) Use
the medium or input-tray selected by the document format processor in the
printer. This selection is implementation-dependent.
""")
_XcmDocPrintDefaultInputIndex_Type = Cardinal16
_XcmDocPrintDefaultInputIndex_Object = MibTableColumn
xcmDocPrintDefaultInputIndex = _XcmDocPrintDefaultInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 2),
    _XcmDocPrintDefaultInputIndex_Type()
)
xcmDocPrintDefaultInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintDefaultInputIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocPrintDefaultInputIndex.setDescription("""\
The value of this object is the index of the input sub-unit in the
prtInputTable in the printer MIB that is the default input tray for this
document. An index value of 0 indicates that neither the submitting client, the
print server, nor printer has specified a default input tray for this document.
The Printer MIB (RFC 1759) requires that input sub-unit indices remain stable
across successive device power cycles. ISO DPA: Default-input-tray This
attribute identifies an input-tray that the server shall use as the input-tray
default for the pages of the document that require a specification. The
correspondence between the simple-name of an input-tray (alphanumeric or
numeric) and the actual tray in the printer is printer-dependent, and a tray
named by such a simple-name may also have an OBJECT IDENTIFIER that names it as
well. A server may try to convert a simple-name received from a client to one
of the server's OIDs, depending on implementation. However, a server shall
always return an input- tray as an OID to the client if the server identifies
the input-tray using an OID. Examples: The simple-name strings: envelope, top,
2, or 02, or the OID value: id-val-input-tray-top. If the default-medium
attribute is specified (either by the client or by a server default, i.e., the
default-medium attribute of the initial-value-job object specified by the
logical or physical printer), then the server shall use the default-medium
value and shall ignore the default-input-tray attribute, if specified. If the
page-media-select attribute is specified (either by the client or by a server
default, i.e., the page-media-select attribute of the initial-value-job object
specified by the logical or physical printer), then the server shall use the
page-media-select value to override the default- input-tray specification on a
page by page basis. If the document data, itself, specifies media or input
trays, such specification shall override the default-input-tray attribute on a
page by page basis. If the document data specifies media or input-trays which
are not also values of media-used or input-trays-used, respectively, then a
printer may receive a document which requires media or input-trays which are
not ready. In such a case, an implementation may either abort the document or
try printing the document using some alternative input-tray, such as the
default input-tray. The following standard values are defined: top The top
input tray in the printer. (id- val-input-tray-top) middle The middle input
tray in the printer. (id- val-input-tray-middle) bottom The bottom input tray
in the printer. (id- val-input-tray-bottom) envelope The envelope input tray in
the printer. (id-val-input-tray-envelope) manual The manual feed input tray in
the printer. (id-val-input-tray-manual) large-capacity The large capacity input
tray in the printer. (id-val-input-tray-large- capacity) main The main input
tray (id-val-input-tray- main) side The side input tray (id-val-input-tray-
side)
""")


class _XcmDocPrintFinishing_Type(InternationalDisplayString):
    """Custom type xcmDocPrintFinishing based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmDocPrintFinishing_Type.__name__ = "InternationalDisplayString"
_XcmDocPrintFinishing_Object = MibTableColumn
xcmDocPrintFinishing = _XcmDocPrintFinishing_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 3),
    _XcmDocPrintFinishing_Type()
)
xcmDocPrintFinishing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintFinishing.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocPrintFinishing.setDescription("""\
Specifies finishing to be performed on the document. NOTE: This attribute that
is supplied by the job service requester is localizable by the job service
provider, since the job service provider must understand and support the
specified value.
""")
_XcmDocPrintOutputMethod_Type = XcmJMDocOutputMethod
_XcmDocPrintOutputMethod_Object = MibTableColumn
xcmDocPrintOutputMethod = _XcmDocPrintOutputMethod_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 4),
    _XcmDocPrintOutputMethod_Type()
)
xcmDocPrintOutputMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintOutputMethod.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocPrintOutputMethod.setDescription("""\
This object is bit coded, so that multiple document output requests may be made
for the document. Each bit corresponds to one of the ISO DPA output OIDs. See
XcmJMDocOutputMethod textual convention for the algorithm that maps DPA OIDs to
bits. ISO DPA: Output This attribute identifies the output processing for the
media on which the document is to be printed.
""")


class _XcmDocPrintNumberUp_Type(InternationalDisplayString):
    """Custom type xcmDocPrintNumberUp based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmDocPrintNumberUp_Type.__name__ = "InternationalDisplayString"
_XcmDocPrintNumberUp_Object = MibTableColumn
xcmDocPrintNumberUp = _XcmDocPrintNumberUp_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 5),
    _XcmDocPrintNumberUp_Type()
)
xcmDocPrintNumberUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintNumberUp.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocPrintNumberUp.setDescription("""\
For the MIB: this object is specified as a text string which can be a number,
e.g., '2' meaning the number of logical pages per side, or a name, e.g.,
'simple-2-up' meaning an imposition object in the system that specifies 2
logical pages per side. NOTE: This attribute that is supplied by the job
service requester is localizable by the job service provider, since the job
service provider must understand and support the specified value. ISO DPA:
number-up (excerpted) This attribute specifies the number of source page-images
to impose upon a single instance of a selected medium. The attribute can be
specified either by a number directly or by naming an imposition object which
specifies some particular number-up imposition. In general, only certain all-
numeric text values are valid for this attribute, depending upon the server and
printer implementations to which the print-request is directed. A text value of
'0' or 'none' shall suppress any server default number up, if any. This
attribute primarily controls the translation, scaling and rotation of page
images, but a site may choose to add embellishments, such as borders to each
logical page. A site may even choose to add an attribute to control the
presence or characteristics of such embellishments. The following standard text
values are defined: '0' This value suppresses any number-up operation or its
embellishments. '1' This value specifies that 1 logical page is to be imaged on
one surface of the medium, possibly with embellishments. '2' This value
specifies that 2 logical pages are to be imaged on one surface of the medium,
possibly with embellishments. '4' This value specifies that 4 logical pages are
to be imaged on one surface of the medium, possibly with embellishments. NOTE -
The value '0' or 'none' specifies that no convenience imposition functions
shall be performed; '0' or 'none' is needed to suppress any special number-up
operation because a value of '1' or 'simple-1-up' for some sites may cause the
server to alter the placement, or size of the page image, or to add
embellishments, such as borders or to rotate the page depending on content-
orientation. See ISO DPA number-up description for further details on the
semantics of number-up, including figures.
""")


class _XcmDocPrintSides_Type(Integer32):
    """Custom type xcmDocPrintSides based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XcmDocPrintSides_Type.__name__ = "Integer32"
_XcmDocPrintSides_Object = MibTableColumn
xcmDocPrintSides = _XcmDocPrintSides_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 6),
    _XcmDocPrintSides_Type()
)
xcmDocPrintSides.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintSides.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocPrintSides.setDescription("""\
NOTE - The xcmDocPrintSides attribute is for print jobs. A scanner-specific
object, xcmDocScanSides is needed to be added when scanning is supported, so
that input and output sides can be specified independently. ISO DPA: Sides This
attribute specifies the number of printable surfaces of the medium to be
imaged.
""")
_XcmDocPrintCopyCount_Type = Cardinal32
_XcmDocPrintCopyCount_Object = MibTableColumn
xcmDocPrintCopyCount = _XcmDocPrintCopyCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 7),
    _XcmDocPrintCopyCount_Type()
)
xcmDocPrintCopyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintCopyCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocPrintCopyCount.setDescription("""\
ISO DPA: Copy-count This attribute specifies the number of copies of the
documents, or of the selected pages of the document, to be printed. A value of
1 for copy-count shall generate a single human perceptible copy of the
electronic document. If a value of 0 is supplied [by the job service requester
and is supported by the job service provider], the job may be processed
normally, but no print output shall be produced or the server shall return an
unsupported-attribute-value AttributeError [to the job service requester, if a
copy-count of 0 is not supported].
""")
_XcmDocPrintCopiesCompleted_Type = Counter32
_XcmDocPrintCopiesCompleted_Object = MibTableColumn
xcmDocPrintCopiesCompleted = _XcmDocPrintCopiesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 8),
    _XcmDocPrintCopiesCompleted_Type()
)
xcmDocPrintCopiesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintCopiesCompleted.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocPrintCopiesCompleted.setDescription("""\
For the MIB: on job recovery after power failure or a crash, the value of
xcmDocPrintCopiesCompleted may be set to a lower value which would normally
violate the SNMP constraints of a Counter32 type. ISO DPA: Copies-completed
This attribute indicates the number of complete copies of this document that
have been printed. Some printers print multiple copies of each individual page
of a document, completing the printing of all copies at the same time, printing
as many of these pages as necessary to satisfy the copy count. The value of
copies-completed is 0 if printing has not started for this document.
""")
_XcmJobGenSpoolingBasic_ObjectIdentity = ObjectIdentity
xcmJobGenSpoolingBasic = _XcmJobGenSpoolingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14)
)
_XcmJobGenSpoolingBasicTable_Object = MibTable
xcmJobGenSpoolingBasicTable = _XcmJobGenSpoolingBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenSpoolingBasicTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobGenSpoolingBasicTable.setDescription("""\
A table of general job information per (logical or physical) device that is
independent of the type of device (printer, scanner, fax, ...) but does require
spooling of job (and document) instructions, but not necessarily of document-
content data. Job information applies to the job as a whole or to all its
documents. The specification for most objects is taken directly from the ISO
10175 Document Printing Application (DPA) standard clause 9.2, Job Attributes.
However, this MIB is intended to be used with non-DPA implementations, so only
a small set of general DPA attributes have been included here.
""")
_XcmJobGenSpoolingBasicEntry_Object = MibTableRow
xcmJobGenSpoolingBasicEntry = _XcmJobGenSpoolingBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1)
)
xcmJobGenBasicEntry.registerAugmentions(
    ("XEROX-JOB-MONITORING-MIB",
     "xcmJobGenSpoolingBasicEntry")
)
xcmJobGenSpoolingBasicEntry.setIndexNames(*xcmJobGenBasicEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmJobGenSpoolingBasicEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobGenSpoolingBasicEntry.setDescription("""\
An entry exists in this table for each job in the device, no matter what the
state of the job is. Each device is represented as a separate device entry in
the Host Resources MIB device table as a device of type 'printer', 'scanner',
'fax', etc. The management station references each job using the
xcmJobIdentifierOnSystem assigned by this logical (for spooling) device that
accepted the job submission (by some other protocol).
""")


class _XcmJobNumberOfJobResultSets_Type(Ordinal32):
    """Custom type xcmJobNumberOfJobResultSets based on Ordinal32"""
    defaultValue = 1


_XcmJobNumberOfJobResultSets_Object = MibTableColumn
xcmJobNumberOfJobResultSets = _XcmJobNumberOfJobResultSets_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1, 1),
    _XcmJobNumberOfJobResultSets_Type()
)
xcmJobNumberOfJobResultSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobNumberOfJobResultSets.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobNumberOfJobResultSets.setDescription("""\
ISO DPA: number-of-job-result-sets The hardcopy output of a print-job consists
of one or more job sets, each of which may be specified to be delivered to, or
held for, one particular recipient who is not necessarily the job creator. Each
job set may be specified to contain one or more job copies. Each job copy shall
contain one or more copies of each of the documents specified by means of the
Print operations that compose the job. For example, consider the following job
being submitted: results-profile: {delivery-address=Jones, job-copies=1},
{delivery-address=Smith, job-copies=2} documentA with copy-count=1 documentB
with copy-count=2
+-------------------------------------------------------------+ |
+----------------------------+ | | | +-------------+ | | | | | document A | | |
| | +-------------+ | | | | | document B | job copy | job result set #1 for
Jones | | | +-------------+ | | | | | document B | | | | | +-------------+ | |
| +----------------------------+ |
+-------------------------------------------------------------+
+-------------------------------------------------------------+ |
+----------------------------+ | | | +-------------+ | | | | | document A | | |
| | +-------------+ | | | | | document B | job copy | | | | +-------------+ | |
| | | document B | | | | | +-------------+ | | | +----------------------------+
| job result set #2 for Smith | | +----------------------------+ | | |
+-------------+ | | | | | document A | | | | | +-------------+ | | | | |
document B | job copy | | | | +-------------+ | | | | | document B | | | | |
+-------------+ | | | +----------------------------+ |
+-------------------------------------------------------------+
""")


class _XcmJobPriority_Type(Integer32):
    """Custom type xcmJobPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XcmJobPriority_Type.__name__ = "Integer32"
_XcmJobPriority_Object = MibTableColumn
xcmJobPriority = _XcmJobPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1, 2),
    _XcmJobPriority_Type()
)
xcmJobPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobPriority.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobPriority.setDescription("""\
For the MIB: A value of 0 means that the priority was not specified by the job
service requester and the system did not specify a default value. ISO DPA: Job-
priority This attribute specifies a priority for scheduling the print- job. It
is used by servers that employ a priority-based scheduling algorithm. A higher
value specifies a higher priority. The value 1 is defined to indicate the
lowest possible priority (a job which a priority-based scheduling algorithm
shall pass over in favor of higher priority jobs). The value 100 is defined to
indicate the highest possible priority. Priority is expected to be evenly or
'normally' distributed across this range. The mapping of vendor-defined
priority over this range is implementation- specific. [The following DPA
sentence is covered by the value of 0, since the DPA range is 1..100. A value
of 0 returned by an SNMP agent indicates the same semantics as ISO DPA
returning the job object without the job-priority attribute present:] The
omission of this attribute implies that the user places no constraints
concerning priority on the scheduling of the print-job.
""")
_XcmJobTotalOctetsHigh_Type = Cardinal64High
_XcmJobTotalOctetsHigh_Object = MibTableColumn
xcmJobTotalOctetsHigh = _XcmJobTotalOctetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1, 3),
    _XcmJobTotalOctetsHigh_Type()
)
xcmJobTotalOctetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobTotalOctetsHigh.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobTotalOctetsHigh.setDescription("""\
For the Job Monitoring MIB: two objects are used to represent a full 62-bit
value. The sign bit of each half is not used. This object is generalized for
use with input devices as well. ISO DPA: Total-job-octets [high 31 bits] This
attribute indicates the size of the job in octets, including document and job
copies. The server may update the value of this attribute after each document
has been transferred to the server or the server may provide this value after
all documents have been transferred to the server, depending on implementation.
In other words, while the job is in the pre-processing [building] state and
when the job is in the held state with the job-state-reasons containing a
document-needed value, the value of the total-job-octets job status attribute
depends on implementation and may not correctly reflect the size of the job. In
computing this value, the server shall include the multiplicative factors
contributed by the (1) copy-count document attribute, (2) the results-
profile.job-copies job attribute element and (3) multiple values of the
results- profile job attribute, independent of whether the printer can process
multiple copies of the job or document without making multiple passes over the
job or document data and independent of the value of the output document
attribute (page-collate vs. no-page-collate). Thus the server computation is
independent of the printer implementation and shall be: a) Document
contribution: Multiply each copy-count by the size of the document in octets.
b) Add each document contribution together c) Job result contribution: Multiply
the job size by the number job-copies in the result set. d) Add each job result
contribution together e) Multiply the value by the number of values in the
job's result-profile attribute.
""")
_XcmJobTotalOctetsLow_Type = Cardinal64Low
_XcmJobTotalOctetsLow_Object = MibTableColumn
xcmJobTotalOctetsLow = _XcmJobTotalOctetsLow_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1, 4),
    _XcmJobTotalOctetsLow_Type()
)
xcmJobTotalOctetsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobTotalOctetsLow.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobTotalOctetsLow.setDescription("""\
ISO DPA: Total-job-octets [low 31 bits] This attribute indicates the size of
the job in octets, including document and job copies. See xcmJobTotalOctetsHigh
for the specification.
""")


class _XcmJobInterveningJobs_Type(Integer32):
    """Custom type xcmJobInterveningJobs based on Integer32"""
    defaultValue = -2


_XcmJobInterveningJobs_Object = MibTableColumn
xcmJobInterveningJobs = _XcmJobInterveningJobs_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1, 5),
    _XcmJobInterveningJobs_Type()
)
xcmJobInterveningJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobInterveningJobs.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobInterveningJobs.setDescription("""\
The number of jobs that are expected to complete before this job is completed
according to the implementation's queuing and processing algorithm if no other
jobs were to be submitted. In other words, this value is the job's queue
position. The agent SHALL return a value of 0 for this object when there are no
other jobs that are expected to complete before this job. A value of (-2) shall
be used when the number of intervening jobs is unknown. NOTE the ISO DPA
language does not include the case when multiple jobs are in the 'processing'
(or printing) state: ISO DPA: Intervening-jobs This attribute indicates the
number of other jobs to be processed before this job may be scheduled for
processing. The server shall set the value of this attribute to 0 when the job
begins processing.
""")
_XcmJobGenSpoolingExt_ObjectIdentity = ObjectIdentity
xcmJobGenSpoolingExt = _XcmJobGenSpoolingExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15)
)
_XcmJobGenSpoolingExtTable_Object = MibTable
xcmJobGenSpoolingExtTable = _XcmJobGenSpoolingExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenSpoolingExtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobGenSpoolingExtTable.setDescription("""\
A table of general extended job information per device that is independent of
the type of device but that does require a spooling implementation. Job
information applies to the job as a whole or to all its documents. The
specification for each object is taken directly from the ISO 10175 Document
Printing Application (DPA) standard clause 9.2, Job Attributes. However, this
MIB is intended to be used with non-DPA implementations, so only a small set of
general DPA attributes have been included here.
""")
_XcmJobGenSpoolingExtEntry_Object = MibTableRow
xcmJobGenSpoolingExtEntry = _XcmJobGenSpoolingExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1)
)
xcmJobGenBasicEntry.registerAugmentions(
    ("XEROX-JOB-MONITORING-MIB",
     "xcmJobGenSpoolingExtEntry")
)
xcmJobGenSpoolingExtEntry.setIndexNames(*xcmJobGenBasicEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmJobGenSpoolingExtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobGenSpoolingExtEntry.setDescription("""\
An entry exists in this table for each job in the (logical) device, no matter
what the state of the job is. Each device is represented as a separate device
entry in the Host Resources MIB device table as a device of type 'printer',
'scanner', 'fax', etc. The management station references each job using the
xcmJobIdentifierOnSystem assigned by this (logical) device that accepted the
job submission (by some other protocol). This table augments the Job General
Basic table in this MIB.
""")


class _XcmJobProcessAfter_Type(DateAndTime):
    """Custom type xcmJobProcessAfter based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobProcessAfter_Object = MibTableColumn
xcmJobProcessAfter = _XcmJobProcessAfter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 1),
    _XcmJobProcessAfter_Type()
)
xcmJobProcessAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobProcessAfter.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobProcessAfter.setDescription("""\
Specifies the calendar date and time of day after which the server is to
process the job on the specified device. The server shall hold the job in the
held state until the specified date and time. NOTE: In this MIB, this object
applies to any type of job, not just print jobs and so this object is a
generalization of the ISO DPA attribute which is only for print jobs. ISO DPA:
Job-print-after This attribute specifies the calendar date and time of day
after which the print-job shall become a candidate to be scheduled for printing
[processing]. If the value of this attribute is in the future, the server shall
set the value of the job's current-job-state to held and add the job-print-
after-specified value to the job's job-state- reasons attribute and shall not
schedule the print-job for printing until the specified date and time has
passed. When the specified date and time arrives, the server shall remove the
job-print-after-specified value from the job's job-state- reason attribute and,
if no other reasons remain, shall change the job's current-job-state to pending
so that the job becomes a candidate for being scheduled on printer(s). [For
purposes of this MIB, the agent shall return the DEFVAL if the job did not
specify this attribute and disregard the next paragraph.] The server shall
assign an empty value (see DPA 9.1.2) to the job-print-after attribute when no
print after time has been assigned, so that the job shall be a candidate for
scheduling immediately.
""")


class _XcmJobDeadlineTime_Type(DateAndTime):
    """Custom type xcmJobDeadlineTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobDeadlineTime_Object = MibTableColumn
xcmJobDeadlineTime = _XcmJobDeadlineTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 3),
    _XcmJobDeadlineTime_Type()
)
xcmJobDeadlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobDeadlineTime.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobDeadlineTime.setDescription("""\
ISO DPA: job-deadline-time This attribute specifies the calendar date and time
of day by which the user desires the print-job to be completed. This attribute
is treated as a scheduling hint only. If the specified deadline time arrives
before completion of the job, the server shall generate the error-past-deadline
event for the job, but the current-job-state shall not be changed. This
attribute is intended for use by servers that implement some form of deadline
scheduling. [For purposes of this MIB, the agent shall return the DEFVAL if the
job did not specify this attribute and disregard the next paragraph.] The
server shall assign an empty value (see DPA 9.1.2) to the job-deadline-time
attribute when there is no deadline for the job.
""")


class _XcmJobDiscardTime_Type(DateAndTime):
    """Custom type xcmJobDiscardTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobDiscardTime_Object = MibTableColumn
xcmJobDiscardTime = _XcmJobDiscardTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 4),
    _XcmJobDiscardTime_Type()
)
xcmJobDiscardTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobDiscardTime.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobDiscardTime.setDescription("""\
ISO DPA: job-discard-time This attribute specifies the calendar date and time
of day at which the print-job should be discarded, whether or not the job has
printed. If this attribute is supported and the discard time has not arrived,
the server shall retain job and document attributes and status; the server is
not required to retain job document files if the job has completed processing
and has exceeded the job's job-retention-period. When the job-discard-time
arrives, the server shall set the job's job-retention-period to zero and shall
perform a CancelJob operation on the specified job. Whether or not the print-
job is discarded if the error-past-discard event occurs while the job is being
printed is implementation-dependent. [For purposes of this MIB, the agent shall
return the DEFVAL if the job did not specify this attribute and disregard the
next paragraph.] The server shall assign an empty value (see DPA 9.1.2) to the
job-discard-time attribute when there is no discard time for the job.
""")
_XcmJobRetentionPeriod_Type = Cardinal32
_XcmJobRetentionPeriod_Object = MibTableColumn
xcmJobRetentionPeriod = _XcmJobRetentionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 5),
    _XcmJobRetentionPeriod_Type()
)
xcmJobRetentionPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobRetentionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobRetentionPeriod.setUnits("seconds")
if mibBuilder.loadTexts:
    xcmJobRetentionPeriod.setDescription("""\
ISO DPA: job-retention-period This attribute specifies the minimum period [in
seconds] of time following the completion of job processing that the server
shall keep job attributes, document attributes, and document data. The server
may keep these attributes and data longer than the value of the job-retention-
period attribute. Job-retention-period specifies a lower bound on how long job
attributes, document attributes and document data shall be retained by a server
after printing [processing] has completed, whilst job-discard-time sets an
upper bound on retention of the job and document attributes independent of
whether the job is ever scheduled for, starts or completes printing
[processing]. In addition to providing status information to a user after a job
has completed printing [processing, the job-retention-period also provides the
mechanism for retaining job's document data after it has been printed
[processed], so that the job may be printed [processed] again, possibly with
modified attributes, such as the job-copies component of the job-results
attribute. However, the mechanism to reprint the job is outside the scope of
this part of ISO/IEC 10175. [See ResubmitJob in Part 3.]
""")
_XcmJobMessageToOperator_Type = CodeIndexedStringIndex
_XcmJobMessageToOperator_Object = MibTableColumn
xcmJobMessageToOperator = _XcmJobMessageToOperator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 6),
    _XcmJobMessageToOperator_Type()
)
xcmJobMessageToOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMessageToOperator.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMessageToOperator.setDescription("""\
ISO DPA: job-message-to-operator This attribute carries a message from the user
to the operator to indicate something about the processing of this print-job.
This message, unlike the job-start-message, is not necessarily related to other
job-scheduling attributes. The server shall make this message available to the
operator when the job has been accepted.
""")
_XcmJobMessageFromOperator_Type = CodeIndexedStringIndex
_XcmJobMessageFromOperator_Object = MibTableColumn
xcmJobMessageFromOperator = _XcmJobMessageFromOperator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 7),
    _XcmJobMessageFromOperator_Type()
)
xcmJobMessageFromOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMessageFromOperator.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMessageFromOperator.setDescription("""\
Xerox extension to ISO DPA: job-message-from-operator This attribute carries a
message from the operator to the user to indicate something about the
processing of this print-job. What additional notification methods are used, if
any, in addition to providing a value for this job attribute depends on
implementation.
""")
_XcmJobMessageFromAdministrator_Type = CodeIndexedStringIndex
_XcmJobMessageFromAdministrator_Object = MibTableColumn
xcmJobMessageFromAdministrator = _XcmJobMessageFromAdministrator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 8),
    _XcmJobMessageFromAdministrator_Type()
)
xcmJobMessageFromAdministrator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMessageFromAdministrator.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMessageFromAdministrator.setDescription("""\
ISO DPA: Job-message-from-administrator This attribute provides a message from
an operator, system administrator or 'intelligent' process to indicate to the
user the reasons for modification or other management action taken on a job.
""")
_XcmJobPageCount_Type = Cardinal32
_XcmJobPageCount_Object = MibTableColumn
xcmJobPageCount = _XcmJobPageCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 9),
    _XcmJobPageCount_Type()
)
xcmJobPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobPageCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobPageCount.setDescription("""\
ISO DPA: Job-page-count This attribute contains the number of source pages in
the job that the server expects to image. The server shall compute this value
by the following procedure: a) For each document in the job object, multiply
the value of document's page-count attribute by the value of its copy- count
attribute and call the result document-set-page-count. b) Add up all the
document-set-page-counts from the previous step and call this sum the job-copy-
page-count. c) For each job-result-set, multiply the value of job-copy- page-
count from the previous step by the value of job-copies element of the job-
result-set and call the result job-result- set-page-count. d) Add up all the
job-result-set-page-counts from the previous step and set this sum into the
job-page-count attribute. The value of this attribute is a measure of the
amount of computation involved. The accuracy of this value is dependent on the
accuracy of the page-count attribute in each document. If some documents have a
page-count value of 0, the server may set the value of this attribute to 0 and
not use it for scheduling.
""")
_XcmJobGenAccountingBasic_ObjectIdentity = ObjectIdentity
xcmJobGenAccountingBasic = _XcmJobGenAccountingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16)
)
_XcmJobGenAccountingBasicTable_Object = MibTable
xcmJobGenAccountingBasicTable = _XcmJobGenAccountingBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenAccountingBasicTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobGenAccountingBasicTable.setDescription("""\
A table of general job accounting information per (logical if spooling or
physical if not spooling) device that is independent of the type of device
(printer, scanner, fax, ...). Job information applies to the job as a whole or
to all its documents. The specification for most objects is taken directly from
the ISO 10175 Document Printing Application (DPA) standard clause 9.2, Job
Attributes. However, this MIB is intended to be used with non-DPA
implementations, so only a small set of general DPA attributes have been
included here.
""")
_XcmJobGenAccountingBasicEntry_Object = MibTableRow
xcmJobGenAccountingBasicEntry = _XcmJobGenAccountingBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1)
)
xcmJobGenBasicEntry.registerAugmentions(
    ("XEROX-JOB-MONITORING-MIB",
     "xcmJobGenAccountingBasicEntry")
)
xcmJobGenAccountingBasicEntry.setIndexNames(*xcmJobGenBasicEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmJobGenAccountingBasicEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobGenAccountingBasicEntry.setDescription("""\
An entry exists in this table for each job in the device, no matter what the
state of the job is. Each device is represented as a separate device entry in
the Host Resources MIB device table as a device of type 'printer', 'scanner',
'fax', etc. The management station references each job using the
xcmJobIdentifierOnSystem assigned by this logical (for spooling) or physical
(not spooling) device that accepted the job submission (by some other
protocol).
""")
_XcmJobAccountingBasicRowStatus_Type = RowStatus
_XcmJobAccountingBasicRowStatus_Object = MibTableColumn
xcmJobAccountingBasicRowStatus = _XcmJobAccountingBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 1),
    _XcmJobAccountingBasicRowStatus_Type()
)
xcmJobAccountingBasicRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmJobAccountingBasicRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobAccountingBasicRowStatus.setDescription("""\
 Manages the status of this conceptual row in the
xcmJobGenAccountingBasicTable. When an accounting program has copied the data
from this row into an accounting system, the accounting program should set
destroy into this object in order to delete this row and all related xcmJob.,
and xcmXxxConsumed. rows, in order to indicate that this accounting and job
information is no longer needed to be retained by the SNMP agent.
""")
_XcmJobAccountingUserName_Type = CodeIndexedStringIndex
_XcmJobAccountingUserName_Object = MibTableColumn
xcmJobAccountingUserName = _XcmJobAccountingUserName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 2),
    _XcmJobAccountingUserName_Type()
)
xcmJobAccountingUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobAccountingUserName.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobAccountingUserName.setDescription("""\
This attribute specifies the name of the user for accounting purposes. See
xcmJobOriginator, xcmJobOwner, and xcmJobAuthorizationUserName for additional
user names for other purposes (and whose values may be different). An agent may
return the same value for all four attributes, if the printer or service does
not support all four concepts. NOTE: There is no corresponding ISO DPA
attribute (but there should be). Often the xcmJobAuthorizationUserName will be
the same as xcmJobAccountingUserName.
""")


class _XcmJobAccountingInformation_Type(OctetString):
    """Custom type xcmJobAccountingInformation based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmJobAccountingInformation_Type.__name__ = "OctetString"
_XcmJobAccountingInformation_Object = MibTableColumn
xcmJobAccountingInformation = _XcmJobAccountingInformation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 3),
    _XcmJobAccountingInformation_Type()
)
xcmJobAccountingInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobAccountingInformation.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobAccountingInformation.setDescription("""\
This object is intended as an accounting identifier, so that a user can
indicate to which account this job should be charged. A user can have any
number of accounts. For example, a lawyer might charge each customer
separately. The value can be text, binary, or encrypted. ISO DPA: Accounting-
information This attribute specifies information required by accounting
services (e.g. the account to be charged for any services rendered). Accounting
information is intended to be interpreted by an accounting system, and may be
opaque to the print service.
""")


class _XcmJobStartedProcessingTime_Type(DateAndTime):
    """Custom type xcmJobStartedProcessingTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobStartedProcessingTime_Object = MibTableColumn
xcmJobStartedProcessingTime = _XcmJobStartedProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 4),
    _XcmJobStartedProcessingTime_Type()
)
xcmJobStartedProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobStartedProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobStartedProcessingTime.setDescription("""\
The time at which the job started to be processed by the intended device
(printed, scanned, faxed, etc.). NOTE: For use with this MIB, this attribute
has been generalized to be used with any device, whereas the corresponding ISO
DPA attribute is only started printing. A conforming implementation shall
return an actual date and time, rather than the DEFVAL, unless the
implementation cannot tell time. ISO DPA: Started-printing-time This attribute
indicates the time at which this job started printing [processing].
""")
_XcmJobImpressionsCompleted_Type = Counter32
_XcmJobImpressionsCompleted_Object = MibTableColumn
xcmJobImpressionsCompleted = _XcmJobImpressionsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 5),
    _XcmJobImpressionsCompleted_Type()
)
xcmJobImpressionsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobImpressionsCompleted.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobImpressionsCompleted.setDescription("""\
If no impressions are completed, this value shall remain 0. ISO DPA:
Impressions-completed This attribute indicates the number of impressions that
the printer engine(s) have placed on the media for the job. See the note in the
pages-completed attribute for the relationship of the pages-completed,
impressions-completed and media-sheets- completed attributes. The server shall
not reset its value during the processing of multiple copies of documents or
the job. Since this attribute is intended to measure the progress of a job, the
value shall include repeated pages due to multiple copies. When the job
completes, this attribute should contain the value of the total number of
impressions that the printer made for the print-job. The accuracy of this value
is implementation-dependent. It is expected that the value reported is never
greater than the actual value. This attribute may not be supported for all
printers and all page description languages. The value of this attribute shall
be 0 if printing [processing] has not started for this job.
""")
_XcmJobMediaSheetsCompleted_Type = Counter32
_XcmJobMediaSheetsCompleted_Object = MibTableColumn
xcmJobMediaSheetsCompleted = _XcmJobMediaSheetsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 6),
    _XcmJobMediaSheetsCompleted_Type()
)
xcmJobMediaSheetsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMediaSheetsCompleted.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobMediaSheetsCompleted.setDescription("""\
If no media sheets are completed, this value shall remain 0. ISO DPA: Media-
sheets-completed This attribute indicates the number of sheets of media that
the printer(s) have completed printing for the job. See the note in the pages-
completed attribute for the relationship of the pages-completed, impressions-
completed and media-sheets- completed attributes. The server shall not reset
its value during the processing of multiple copies of documents or the job.
Since this attribute is intended to measure the progress of a job, the value
shall include repeated pages due to multiple copies. When the job completes,
this attribute should contain the value of the total number of sheets of media
used for the print-job. The accuracy of this value is implementation-dependent.
It is expected that the value reported is never greater than the actual value.
This attribute may not be supported for all printers and all page description
languages. The value of this attribute shall be 0 if printing has not started
for this job.
""")


class _XcmJobCompletionTime_Type(DateAndTime):
    """Custom type xcmJobCompletionTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobCompletionTime_Object = MibTableColumn
xcmJobCompletionTime = _XcmJobCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 7),
    _XcmJobCompletionTime_Type()
)
xcmJobCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobCompletionTime.setDescription("""\
A conforming implementation shall return an actual date and time, rather than
the DEFVAL, unless the implementation cannot tell time. ISO DPA: Completion-
time This attribute indicates the time at which this job completed. Providing
this time is useful for jobs which are retained after printing.
""")


class _XcmJobWorkUnitType_Type(XcmHrDevTrafficUnit):
    """Custom type xcmJobWorkUnitType based on XcmHrDevTrafficUnit"""


_XcmJobWorkUnitType_Object = MibTableColumn
xcmJobWorkUnitType = _XcmJobWorkUnitType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 8),
    _XcmJobWorkUnitType_Type()
)
xcmJobWorkUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobWorkUnitType.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobWorkUnitType.setDescription("""\
Xerox extension This attribute indicates the type of work that is being
accounted for. It shall be different from pages, sheets, or impressions, which
already have their own objects.
""")
_XcmJobUnitsOfWorkCompleted_Type = Counter32
_XcmJobUnitsOfWorkCompleted_Object = MibTableColumn
xcmJobUnitsOfWorkCompleted = _XcmJobUnitsOfWorkCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 9),
    _XcmJobUnitsOfWorkCompleted_Type()
)
xcmJobUnitsOfWorkCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobUnitsOfWorkCompleted.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobUnitsOfWorkCompleted.setDescription("""\
Xerox extension: The number of work units completed. See xcmJobWorkUnitType to
determine what is being counted.
""")
_XcmMediaConsumed_ObjectIdentity = ObjectIdentity
xcmMediaConsumed = _XcmMediaConsumed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17)
)
_XcmMediaConsumedTable_Object = MibTable
xcmMediaConsumedTable = _XcmMediaConsumedTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1)
)
if mibBuilder.loadTexts:
    xcmMediaConsumedTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmMediaConsumedTable.setDescription("""\
This table contains pairs of media indexes and the number of sheets of that
media consumed by this job.
""")
_XcmMediaConsumedEntry_Object = MibTableRow
xcmMediaConsumedEntry = _XcmMediaConsumedEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1)
)
xcmMediaConsumedEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmMediaConsumedIndex"),
)
if mibBuilder.loadTexts:
    xcmMediaConsumedEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmMediaConsumedEntry.setDescription("""\
Entries may exist in the table for each device index in the Host Resource MIB
whose device type is `printer', 'fax', etc., and for each job.
""")
_XcmMediaConsumedIndex_Type = Ordinal16
_XcmMediaConsumedIndex_Object = MibTableColumn
xcmMediaConsumedIndex = _XcmMediaConsumedIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1, 1),
    _XcmMediaConsumedIndex_Type()
)
xcmMediaConsumedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmMediaConsumedIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmMediaConsumedIndex.setDescription("""\
A unique value used by the device to identify this medium entry in this job.
For devices and systems that ensure that jobs are not lost across crashes and
power cycles, these values shall remain stable across successive device power
cycles. However, if a (low-end) device is not ensuring that job are persistent
across crashes and power cycles, these index values need not remain stable
across such crashes or power cycles.
""")
_XcmMediaConsumedRowStatus_Type = RowStatus
_XcmMediaConsumedRowStatus_Object = MibTableColumn
xcmMediaConsumedRowStatus = _XcmMediaConsumedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1, 2),
    _XcmMediaConsumedRowStatus_Type()
)
xcmMediaConsumedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmMediaConsumedRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmMediaConsumedRowStatus.setDescription("""\
Manages the status of this conceptual row in the xcmMediaConsumedTable. When an
accounting program has copied the data from this row into an accounting system,
the accounting program should delete this row in order to indicate that this
accounting information is no longer needed to be retained by the SNMP agent.
Since the accounting data may be of interest to end-users, the accounting
program may want to wait for some period before deleting the row. If the
accounting table becomes filled up so that the agent is unable to add new
entries, a device may either refuse to accept new jobs, so that the valuable
revenue stream is not lost, or may remove the oldest entry in the display and
add the new job's accounting data.
""")


class _XcmMediaConsumedType_Type(XcmJMMediumType):
    """Custom type xcmMediaConsumedType based on XcmJMMediumType"""


_XcmMediaConsumedType_Object = MibTableColumn
xcmMediaConsumedType = _XcmMediaConsumedType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1, 3),
    _XcmMediaConsumedType_Type()
)
xcmMediaConsumedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmMediaConsumedType.setStatus("current")
if mibBuilder.loadTexts:
    xcmMediaConsumedType.setDescription("""\
This attribute indicates the medium type that has been consumed by the
device(s) for this job, e.g. stationery, envelope, transparency, etc.
""")
_XcmMediaConsumedName_Type = CodeIndexedStringIndex
_XcmMediaConsumedName_Object = MibTableColumn
xcmMediaConsumedName = _XcmMediaConsumedName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1, 4),
    _XcmMediaConsumedName_Type()
)
xcmMediaConsumedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmMediaConsumedName.setStatus("current")
if mibBuilder.loadTexts:
    xcmMediaConsumedName.setDescription("""\
This attribute indicates the name of the medium that has been consumed by the
device(s) for this job, e.g. letter-white, iso-a4-white, iso-a4-blanc, monarch-
envelope, iso-a4-transparent, etc. ISO DPA assigns OIDs to medium names, but
also allows the SA to define new media using text strings. Hence, the object in
this MIB is a text string, so that the SA can define additional medium names as
needed.
""")
_XcmMediaConsumedSheetCount_Type = Counter32
_XcmMediaConsumedSheetCount_Object = MibTableColumn
xcmMediaConsumedSheetCount = _XcmMediaConsumedSheetCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1, 5),
    _XcmMediaConsumedSheetCount_Type()
)
xcmMediaConsumedSheetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmMediaConsumedSheetCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmMediaConsumedSheetCount.setDescription("""\
This attribute indicates the number of sheets of the medium that have been
consumed by the device(s) for this job.
""")
_XcmColorImpsConsumed_ObjectIdentity = ObjectIdentity
xcmColorImpsConsumed = _XcmColorImpsConsumed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18)
)
_XcmColorImpsConsumedTable_Object = MibTable
xcmColorImpsConsumedTable = _XcmColorImpsConsumedTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1)
)
if mibBuilder.loadTexts:
    xcmColorImpsConsumedTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedTable.setDescription("""\
This table contains pairs of colorant indexes and the number of impressions of
that colorant consumed by this job.
""")
_XcmColorImpsConsumedEntry_Object = MibTableRow
xcmColorImpsConsumedEntry = _XcmColorImpsConsumedEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1, 1)
)
xcmColorImpsConsumedEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmColorImpsConsumedIndex"),
)
if mibBuilder.loadTexts:
    xcmColorImpsConsumedEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedEntry.setDescription("""\
Entries may exist in the table for each device index whose device type is
'printer', 'fax', etc. and for each job.
""")
_XcmColorImpsConsumedIndex_Type = Ordinal16
_XcmColorImpsConsumedIndex_Object = MibTableColumn
xcmColorImpsConsumedIndex = _XcmColorImpsConsumedIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1, 1, 1),
    _XcmColorImpsConsumedIndex_Type()
)
xcmColorImpsConsumedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedIndex.setDescription("""\
A unique value used by the printer to identify this colorant entry for this
job. For devices and systems that ensure that jobs are not lost across crashes
and power cycles, these values shall remain stable across successive device
power cycles. However, if a (low-end) device is not ensuring that job are
persistent across crashes and power cycles, these index values need not remain
stable across such crashes or power cycles.
""")
_XcmColorImpsConsumedRowStatus_Type = RowStatus
_XcmColorImpsConsumedRowStatus_Object = MibTableColumn
xcmColorImpsConsumedRowStatus = _XcmColorImpsConsumedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1, 1, 2),
    _XcmColorImpsConsumedRowStatus_Type()
)
xcmColorImpsConsumedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedRowStatus.setDescription("""\
Manages the status of this conceptual row in the xcmColorImpsConsumedTable.
When an accounting program has copied the data from this row into an accounting
system, the accounting program should delete this row in order to indicate that
this accounting information is no longer needed to be retained by the SNMP
agent.
""")
_XcmColorImpsConsumedTypeIndex_Type = Ordinal16
_XcmColorImpsConsumedTypeIndex_Object = MibTableColumn
xcmColorImpsConsumedTypeIndex = _XcmColorImpsConsumedTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1, 1, 3),
    _XcmColorImpsConsumedTypeIndex_Type()
)
xcmColorImpsConsumedTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedTypeIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedTypeIndex.setDescription("""\
This attribute indicates one of the colorant type (index into the
prtColorantsTable in the Printer MIB) that have been consumed by the printer(s)
for this print job.
""")
_XcmColorImpsConsumedCount_Type = Counter32
_XcmColorImpsConsumedCount_Object = MibTableColumn
xcmColorImpsConsumedCount = _XcmColorImpsConsumedCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1, 1, 4),
    _XcmColorImpsConsumedCount_Type()
)
xcmColorImpsConsumedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedCount.setDescription("""\
This attribute indicates the number of impressions that have been consumed by
the printer(s) for this print job and this colorant. For implementations that
make a separate impression for each colorant used shall increment this count
once for each colorant, so that the total number of xcmColorImpsConsumedCount
for the job will be a multiple of the xcmJobImpressionsCompleted value.
""")
_XcmJobAlert_ObjectIdentity = ObjectIdentity
xcmJobAlert = _XcmJobAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 19)
)
_XcmJobV1AlertNew_ObjectIdentity = ObjectIdentity
xcmJobV1AlertNew = _XcmJobV1AlertNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 19, 4)
)
if mibBuilder.loadTexts:
    xcmJobV1AlertNew.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobV1AlertNew.setReference("""\
See SNMPv2 'xcmJobV2AlertNew' trap definitions below for 'special semantics'.
""")
if mibBuilder.loadTexts:
    xcmJobV1AlertNew.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever the
state of a job changes.
""")
_XcmJobV2AlertPrefixNew_ObjectIdentity = ObjectIdentity
xcmJobV2AlertPrefixNew = _XcmJobV2AlertPrefixNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 19, 4, 0)
)
_XcmDocAlert_ObjectIdentity = ObjectIdentity
xcmDocAlert = _XcmDocAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 20)
)
_XcmDocV1AlertNew_ObjectIdentity = ObjectIdentity
xcmDocV1AlertNew = _XcmDocV1AlertNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 20, 4)
)
if mibBuilder.loadTexts:
    xcmDocV1AlertNew.setStatus("current")
if mibBuilder.loadTexts:
    xcmDocV1AlertNew.setReference("""\
See SNMPv2 'xcmDocV2AlertNew' trap definitions below for 'special semantics'.
""")
if mibBuilder.loadTexts:
    xcmDocV1AlertNew.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever the
state of a document changes.
""")
_XcmDocV2AlertPrefixNew_ObjectIdentity = ObjectIdentity
xcmDocV2AlertPrefixNew = _XcmDocV2AlertPrefixNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 20, 4, 0)
)
_XcmJobImpsByMediumSize_ObjectIdentity = ObjectIdentity
xcmJobImpsByMediumSize = _XcmJobImpsByMediumSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21)
)
_XcmJobImpsByMediumSizeTable_Object = MibTable
xcmJobImpsByMediumSizeTable = _XcmJobImpsByMediumSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1)
)
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeTable.setDescription("""\
This table contains tuples of medium size, count-type, and the number of
impressions counted by count-type on that medium consumed by this job.
""")
_XcmJobImpsByMediumSizeEntry_Object = MibTableRow
xcmJobImpsByMediumSizeEntry = _XcmJobImpsByMediumSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1)
)
xcmJobImpsByMediumSizeEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeIndex"),
)
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeEntry.setDescription("""\
This entry has one tuple of medium size, count-type, and the number of
impressions counted by count-type on that medium consumed by this job.
""")
_XcmJobImpsByMediumSizeIndex_Type = Ordinal16
_XcmJobImpsByMediumSizeIndex_Object = MibTableColumn
xcmJobImpsByMediumSizeIndex = _XcmJobImpsByMediumSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 1),
    _XcmJobImpsByMediumSizeIndex_Type()
)
xcmJobImpsByMediumSizeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeIndex.setDescription("""\
A unique value used by the device to identify this impressions-by-medium-size
entry in this job. For devices and systems that ensure that jobs are not lost
across crashes and power cycles, these values shall remain stable across
successive device power cycles. However, if a (low-end) device is not ensuring
that job are persistent across crashes and power cycles, these index values
need not remain stable across such crashes or power cycles.
""")
_XcmJobImpsByMediumSizeRowStatus_Type = RowStatus
_XcmJobImpsByMediumSizeRowStatus_Object = MibTableColumn
xcmJobImpsByMediumSizeRowStatus = _XcmJobImpsByMediumSizeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 2),
    _XcmJobImpsByMediumSizeRowStatus_Type()
)
xcmJobImpsByMediumSizeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeRowStatus.setDescription("""\
Manages the status of this conceptual row in the xcmJobImpsByMediumSizeTable.
When an accounting program has copied the data from this row into an accounting
system, the accounting program should delete this row in order to indicate that
this accounting information is no longer needed to be retained by the SNMP
agent. Since the accounting data may be of interest to end-users, the
accounting program may want to wait for some period before deleting the row. If
the accounting table becomes filled up so that the agent is unable to add new
entries, a device may either refuse to accept new jobs, so that the valuable
revenue stream is not lost, or may remove the oldest entry in the display and
add the new job's accounting data.
""")


class _XcmJobImpsByMediumSizeMediumSize_Type(XcmPrtMediumSize):
    """Custom type xcmJobImpsByMediumSizeMediumSize based on XcmPrtMediumSize"""


_XcmJobImpsByMediumSizeMediumSize_Object = MibTableColumn
xcmJobImpsByMediumSizeMediumSize = _XcmJobImpsByMediumSizeMediumSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 3),
    _XcmJobImpsByMediumSizeMediumSize_Type()
)
xcmJobImpsByMediumSizeMediumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeMediumSize.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeMediumSize.setDescription("""\
This attribute indicates the medium size that has been produced by the
device(s) for this job, e.g. naLetter(1000), isoA4(1024), jisB4(1084), etc.
""")


class _XcmJobImpsByMediumSizeCountType_Type(XcmJMImpsCountType):
    """Custom type xcmJobImpsByMediumSizeCountType based on XcmJMImpsCountType"""


_XcmJobImpsByMediumSizeCountType_Object = MibTableColumn
xcmJobImpsByMediumSizeCountType = _XcmJobImpsByMediumSizeCountType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 4),
    _XcmJobImpsByMediumSizeCountType_Type()
)
xcmJobImpsByMediumSizeCountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeCountType.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeCountType.setDescription("""\
This attribute indicates the count-type that is how to count impressions
produced by the device(s) for this job, e.g. blackAndWhiteCount,
highlightColorCount, fullColorCount, etc.
""")
_XcmJobImpsByMediumSizeCount_Type = Counter32
_XcmJobImpsByMediumSizeCount_Object = MibTableColumn
xcmJobImpsByMediumSizeCount = _XcmJobImpsByMediumSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 5),
    _XcmJobImpsByMediumSizeCount_Type()
)
xcmJobImpsByMediumSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeCount.setDescription("""\
This attribute indicates the number of impressions by medium size, count-type,
and quality-type for the job, which are specified respectively by
xcmJobImpsByMediumSizeMediumSize, xcmJobImpsByMediumSizeCountType, and
xcmJobImpsByMediumSizeCountQuality.
""")


class _XcmJobImpsByMediumSizeCountQuality_Type(XcmPrtPrintQuality):
    """Custom type xcmJobImpsByMediumSizeCountQuality based on XcmPrtPrintQuality"""


_XcmJobImpsByMediumSizeCountQuality_Object = MibTableColumn
xcmJobImpsByMediumSizeCountQuality = _XcmJobImpsByMediumSizeCountQuality_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 6),
    _XcmJobImpsByMediumSizeCountQuality_Type()
)
xcmJobImpsByMediumSizeCountQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeCountQuality.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeCountQuality.setReference("""\
 xcmPrtInterpPrintQuality, from 16prtx.mib
""")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeCountQuality.setDescription("""\
This attribute indicates the quality-type used for counting impressions
produced by the device(s) for this job, e.g., draft, normal, high, etc.
""")

# Managed Objects groups

xcmJMBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 1)
)
xcmJMBaseGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseRowStatus"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseVersionID"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseVersionDate"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseGroupSupport"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseCreateSupport"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmJMBaseGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMBaseGroup.setDescription("""\
The conditionally mandatory Job Monitoring Base group, i.e., SHALL be
implemented if implementing traps and/or SJMM.
""")

xcmJMJobGenBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 6)
)
xcmJMJobGenBasicGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierUpstream"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobClientId"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobServiceType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobOwner"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobSourceChannelType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobSubmittedLocaleIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobCurrentState"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobStateReasons"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobXStateReasons"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobX2StateReasons"))
)
if mibBuilder.loadTexts:
    xcmJMJobGenBasicGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMJobGenBasicGroup.setDescription("""\
The conditionally mandatory Job General Basic group, i.e., SHALL be implemented
if implementing traps and/or SJMM.
""")

xcmJMDevicesAssignedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 7)
)
xcmJMDevicesAssignedGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmDeviceStateOfDevicesAssigned"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierDownstream"))
)
if mibBuilder.loadTexts:
    xcmJMDevicesAssignedGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMDevicesAssignedGroup.setDescription("""\
The deprecated Devices Assigned group.
""")

xcmJMClientIdMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 8)
)
xcmJMClientIdMapGroup.setObjects(
    ("XEROX-JOB-MONITORING-MIB", "xcmClientIdMapHrDeviceIndex")
)
if mibBuilder.loadTexts:
    xcmJMClientIdMapGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMClientIdMapGroup.setDescription("""\
The optional client id map group - applies to all jobs.
""")

xcmJMJobGenExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 10)
)
xcmJMJobGenExtGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobOriginator"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobSubmittingApplication"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobComment"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobCopies"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobCopiesCompleted"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobOutputBinIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobServiceNameRequested"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobPreviousState"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobEstimatedCompletionTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobSubmissionTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobPagesCompleted"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobOctetsCompletedHigh"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobOctetsCompletedLow"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobErrorCount"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobWarningCount"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobProcessingTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobNumberOfDocuments"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobAuthorizationUserName"))
)
if mibBuilder.loadTexts:
    xcmJMJobGenExtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMJobGenExtGroup.setDescription("""\
The Job General Extended group.
""")

xcmJMDocGenBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 12)
)
xcmJMDocGenBasicGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmDocSequenceNumber"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocFileName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocFileNameType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocFormat"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocFormatVariants"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocFormatVersion"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocOctetCount"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocState"))
)
if mibBuilder.loadTexts:
    xcmJMDocGenBasicGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMDocGenBasicGroup.setDescription("""\
The document information group.
""")

xcmJMDocPrintExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 13)
)
xcmJMDocPrintExtGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmDocPrintDefaultMediumName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintDefaultInputIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintFinishing"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintOutputMethod"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintNumberUp"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintSides"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintCopyCount"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintCopiesCompleted"))
)
if mibBuilder.loadTexts:
    xcmJMDocPrintExtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMDocPrintExtGroup.setDescription("""\
The Document Print-centric group.
""")

xcmJMJobGenSpoolingBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 14)
)
xcmJMJobGenSpoolingBasicGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobNumberOfJobResultSets"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobPriority"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobTotalOctetsHigh"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobTotalOctetsLow"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobInterveningJobs"))
)
if mibBuilder.loadTexts:
    xcmJMJobGenSpoolingBasicGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMJobGenSpoolingBasicGroup.setDescription("""\
The Job General Spooling Basic group.
""")

xcmJMJobGenSpoolingExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 15)
)
xcmJMJobGenSpoolingExtGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobProcessAfter"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobDeadlineTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobDiscardTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobRetentionPeriod"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMessageToOperator"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMessageFromOperator"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMessageFromAdministrator"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobPageCount"))
)
if mibBuilder.loadTexts:
    xcmJMJobGenSpoolingExtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMJobGenSpoolingExtGroup.setDescription("""\
The Job General Spooling Extended group.
""")

xcmJMJobGenAccountingBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 16)
)
xcmJMJobGenAccountingBasicGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobAccountingBasicRowStatus"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobAccountingUserName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobAccountingInformation"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobStartedProcessingTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobImpressionsCompleted"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMediaSheetsCompleted"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobCompletionTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobWorkUnitType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobUnitsOfWorkCompleted"))
)
if mibBuilder.loadTexts:
    xcmJMJobGenAccountingBasicGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMJobGenAccountingBasicGroup.setDescription("""\
The Job General Accounting Basic group.
""")

xcmJMMediaConsumedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 17)
)
xcmJMMediaConsumedGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmMediaConsumedRowStatus"),
        ("XEROX-JOB-MONITORING-MIB", "xcmMediaConsumedType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmMediaConsumedName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmMediaConsumedSheetCount"))
)
if mibBuilder.loadTexts:
    xcmJMMediaConsumedGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMMediaConsumedGroup.setDescription("""\
The media consumed group.
""")

xcmJMColorImpsConsumedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 18)
)
xcmJMColorImpsConsumedGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmColorImpsConsumedRowStatus"),
        ("XEROX-JOB-MONITORING-MIB", "xcmColorImpsConsumedTypeIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmColorImpsConsumedCount"))
)
if mibBuilder.loadTexts:
    xcmJMColorImpsConsumedGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMColorImpsConsumedGroup.setDescription("""\
The optional color impressions consumed group.
""")

xcmJMJobImpsByMediumSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 21)
)
xcmJMJobImpsByMediumSizeGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeRowStatus"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeMediumSize"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeCountType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeCount"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeCountQuality"))
)
if mibBuilder.loadTexts:
    xcmJMJobImpsByMediumSizeGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJMJobImpsByMediumSizeGroup.setDescription("""\
The Job Impressions by Medium Size group.
""")


# Notification objects

xcmJobV2AlertNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 19, 4, 0, 1)
)
xcmJobV2AlertNew.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"))
)
if mibBuilder.loadTexts:
    xcmJobV2AlertNew.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmJobV2AlertNew.setDescription("""\
This trap is sent whenever the state of a job changes. The 'state of a job' is
comprised by the aggregate values of the xcmJobCurrentState, xcmJobPriority,
xcmJobStateReasons, xcmJobXStateReasons, xcmJobX2StateReasons,
xcmDevicesAssigned and xcmDeviceStateOfDevicesAssigned fields of the job's
table entries: This notification is sent whenever any of these values changes
with the following exceptions: 1. Changes in xcmDeviceStateOfDevicesAssigned
shall only generate traps when the job is in the processing state (NOTE -
xcmJMDevicesAssignedGroup is deprecated) 2. Changes in xcmJobStateReasons,
xcmJobXStateReasons, and xcmJobX2StateReasons shall only generate traps when
the job is in the processing state (rare). The normal polling cycle will pick
up any changes while the job is not in the processing state. Since most changes
in reasons also accompany a job state change, the chances that a change in a
reason will have to wait for the normal polling cycle is very small. For
example, a requester further modifies a held job adding more reasons for it to
be held will have to wait for the polling cycle, since the job does not change
state (remaining in the held state). NOTE - the hrDeviceIndex is included for
convenience, even though the Printer MIB (RFC 1759) doesn't include
hrDeviceIndex in its traps. Then the management station doesn't have to parse
the received varBind OIDs on a trap in order to discover which device trapped.
NOTE - the addition of an entire row to the job tables corresponds to the
acceptance of another job by the server. The state of the job changes from
unknown to a specific value (usually pending). Therefore, the agent shall
generate a trap when a job is accepted (so that the management station can
display the newly arrived job in a timely fashion). Similarly when the server
removes a job because the job has been in the completed state for a sufficient
time or the job has been deleted by a Delete operation, the SNMP agent shall
reflect that removal by removing the row from the job tables, and shall
generate a trap (since the state of the job has changed to non-existent). The
IETF Printer MIB maintains a table which serves as a sort of 'audit-trail' of
recent alerts. There is no need for such a table here, since the job's tables
will serve virtually the same purpose. As with all SNMP notifications, critical
applications cannot completely rely upon delivery: some amount of polling is
recommended. The variable-bindings of this trap have been chosen to give the
minimum of information: the xcmJobIdentifierOnSystem value and hrDeviceIndex
are provided. With these an application is able to obtain the full job table
entry. An application has to look at the job tables anyway. The time of the
alert is returned as part of any SNMP trap. The hrDeviceIndex maps one-to-one
with the PWG Job Mon jmGeneralJobSetIndex. (The PWG Job Mon does not require
the Host Resources MIB, so the name of the primary index for all PWG Job Mon
tables is not hrDeviceIndex, but serves the same purpose of allowing multiple
instances in a single device or server. The Job Alert's special semantics is
covered by U.S. patent 5778183. This notification has the following special
semantics: o If the job's xcmJobClientId field is not empty, its value will
also be appended to trap object ID. NOTE: If the format of the xcmJobClientId
is dotted decimal representation, then it will be encoded as a BER binary OID
appended to the trap object ID. NOTE: The BER binary OID shall not include the
ASN.1/BER tag of 6 indicating an OID and shall not include the ASN.1/BER length
field in octets of the OID. This trap OID qualifier allows job-submission and
monitoring applications to limit the alerts they receive to ones generated by
jobs which they have submitted. NOTE: The sum of the trap var bind values must
be less than can fit into a PDU on any transport, roughly 540 octets on some
transports. Thus implementers are warned to minimize the length of the
xcmJobClientId and xcmJobIdentifierOnSystem objects.
""")

xcmDocV2AlertNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 20, 4, 0, 1)
)
xcmDocV2AlertNew.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocSequenceNumber"))
)
if mibBuilder.loadTexts:
    xcmDocV2AlertNew.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmDocV2AlertNew.setDescription("""\
This trap is sent whenever the state of one of the documents in a job changes.
The state of a single document is represented in the xcmDocGenBasicTable
column: xcmDocState. The job's xcmJobIdentifierOnSystem and the document's
xcmDocSequenceNumber are included in the trap's variable bindings; these can be
used to reference the document's xcmDocGenBasicTable entry. NOTE - the addition
of an entire row to the document tables corresponds to the acceptance of
another document (in a job) by the server. The state of the document changes
from unknown to a specific value (usually transfer pending). Therefore, the
agent generates a trap when a document (within a job) is accepted (so that the
management station can display the newly arrived document in a timely fashion).
This notification has the following special semantics: 1 The agent shall append
the document's job's xcmJobClientId to the trap object ID, if the document's
job's xcmJobClientId field is not empty. NOTE: If the format of the
xcmJobClientId is dotted decimal representation, then it will be encoded as a
BER binary OID appended to the trap object ID. NOTE: The BER binary OID shall
not include the ASN.1/BER tag of 6 indicating an OID and shall not include the
ASN.1/BER length field in octets of the OID. 2 The agent shall append the value
of the document's xcmDocSequenceNumber field to the trap object ID. These trap
OID qualifiers allow job-submission and monitoring applications to specify
exactly which alerts they are interested in and to limit the alerts they
receive to ones generated by jobs or jobs and documents that they have
submitted. NOTE: The sum of the trap var bind values must be less than can fit
into a PDU on any transport, roughly 540 octets on some transports. Thus
implementers are warned to minimize the length of the xcmJobClientId and
xcmJobIdentifierOnSystem objects.
""")


# Notifications groups


# Agent capabilities


# Module compliance

xcmJobMonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 1)
)
if mibBuilder.loadTexts:
    xcmJobMonCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmJobMonCompliance.setDescription("""\
The mandatory compliance statement for the agents that implement the XCMI Job
Monitoring MIB, i.e., all the mandatory groups. NOTE: These two groups are
CONDITIONALLY MANDATORY as far as XCMI Conformance is concerned. But if the
conditions are satisfied (traps and/or SJMM), then these groups MUST be
implemented, making them effectively MANDATORY.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-JOB-MONITORING-MIB",
    **{"xcmJobZeroDummy": xcmJobZeroDummy,
       "xcmJobMonMIB": xcmJobMonMIB,
       "xcmJobMonBase": xcmJobMonBase,
       "xcmJobMonBaseTable": xcmJobMonBaseTable,
       "xcmJobMonBaseEntry": xcmJobMonBaseEntry,
       "xcmJobMonBaseIndex": xcmJobMonBaseIndex,
       "xcmJobMonBaseRowStatus": xcmJobMonBaseRowStatus,
       "xcmJobMonBaseVersionID": xcmJobMonBaseVersionID,
       "xcmJobMonBaseVersionDate": xcmJobMonBaseVersionDate,
       "xcmJobMonBaseGroupSupport": xcmJobMonBaseGroupSupport,
       "xcmJobMonBaseCreateSupport": xcmJobMonBaseCreateSupport,
       "xcmJobMonBaseUpdateSupport": xcmJobMonBaseUpdateSupport,
       "xcmJobMonMIBConformance": xcmJobMonMIBConformance,
       "xcmJobMonCompliance": xcmJobMonCompliance,
       "xcmJobMonMIBGroups": xcmJobMonMIBGroups,
       "xcmJMBaseGroup": xcmJMBaseGroup,
       "xcmJMJobGenBasicGroup": xcmJMJobGenBasicGroup,
       "xcmJMDevicesAssignedGroup": xcmJMDevicesAssignedGroup,
       "xcmJMClientIdMapGroup": xcmJMClientIdMapGroup,
       "xcmJMJobGenExtGroup": xcmJMJobGenExtGroup,
       "xcmJMDocGenBasicGroup": xcmJMDocGenBasicGroup,
       "xcmJMDocPrintExtGroup": xcmJMDocPrintExtGroup,
       "xcmJMJobGenSpoolingBasicGroup": xcmJMJobGenSpoolingBasicGroup,
       "xcmJMJobGenSpoolingExtGroup": xcmJMJobGenSpoolingExtGroup,
       "xcmJMJobGenAccountingBasicGroup": xcmJMJobGenAccountingBasicGroup,
       "xcmJMMediaConsumedGroup": xcmJMMediaConsumedGroup,
       "xcmJMColorImpsConsumedGroup": xcmJMColorImpsConsumedGroup,
       "xcmJMJobImpsByMediumSizeGroup": xcmJMJobImpsByMediumSizeGroup,
       "xcmJobGenBasic": xcmJobGenBasic,
       "xcmJobGenBasicTable": xcmJobGenBasicTable,
       "xcmJobGenBasicEntry": xcmJobGenBasicEntry,
       "xcmJobIdentifierOnSystem": xcmJobIdentifierOnSystem,
       "xcmJobIdentifierUpstream": xcmJobIdentifierUpstream,
       "xcmJobClientId": xcmJobClientId,
       "xcmJobServiceType": xcmJobServiceType,
       "xcmJobName": xcmJobName,
       "xcmJobOwner": xcmJobOwner,
       "xcmJobSourceChannelType": xcmJobSourceChannelType,
       "xcmJobSubmittedLocaleIndex": xcmJobSubmittedLocaleIndex,
       "xcmJobCurrentState": xcmJobCurrentState,
       "xcmJobStateReasons": xcmJobStateReasons,
       "xcmJobXStateReasons": xcmJobXStateReasons,
       "xcmJobX2StateReasons": xcmJobX2StateReasons,
       "xcmDevicesAssigned": xcmDevicesAssigned,
       "xcmDevicesAssignedTable": xcmDevicesAssignedTable,
       "xcmDevicesAssignedEntry": xcmDevicesAssignedEntry,
       "xcmDevicesAssignedHrDeviceIndex": xcmDevicesAssignedHrDeviceIndex,
       "xcmDeviceStateOfDevicesAssigned": xcmDeviceStateOfDevicesAssigned,
       "xcmJobIdentifierDownstream": xcmJobIdentifierDownstream,
       "xcmClientIdMap": xcmClientIdMap,
       "xcmClientIdMapTable": xcmClientIdMapTable,
       "xcmClientIdMapEntry": xcmClientIdMapEntry,
       "xcmClientIdMapHrDeviceIndex": xcmClientIdMapHrDeviceIndex,
       "xcmJobGenExt": xcmJobGenExt,
       "xcmJobGenExtTable": xcmJobGenExtTable,
       "xcmJobGenExtEntry": xcmJobGenExtEntry,
       "xcmJobOriginator": xcmJobOriginator,
       "xcmJobSubmittingApplication": xcmJobSubmittingApplication,
       "xcmJobComment": xcmJobComment,
       "xcmJobCopies": xcmJobCopies,
       "xcmJobCopiesCompleted": xcmJobCopiesCompleted,
       "xcmJobOutputBinIndex": xcmJobOutputBinIndex,
       "xcmJobServiceNameRequested": xcmJobServiceNameRequested,
       "xcmJobPreviousState": xcmJobPreviousState,
       "xcmJobEstimatedCompletionTime": xcmJobEstimatedCompletionTime,
       "xcmJobSubmissionTime": xcmJobSubmissionTime,
       "xcmJobPagesCompleted": xcmJobPagesCompleted,
       "xcmJobOctetsCompletedHigh": xcmJobOctetsCompletedHigh,
       "xcmJobOctetsCompletedLow": xcmJobOctetsCompletedLow,
       "xcmJobErrorCount": xcmJobErrorCount,
       "xcmJobWarningCount": xcmJobWarningCount,
       "xcmJobProcessingTime": xcmJobProcessingTime,
       "xcmJobNumberOfDocuments": xcmJobNumberOfDocuments,
       "xcmJobAuthorizationUserName": xcmJobAuthorizationUserName,
       "xcmDocGenBasic": xcmDocGenBasic,
       "xcmDocGenBasicTable": xcmDocGenBasicTable,
       "xcmDocGenBasicEntry": xcmDocGenBasicEntry,
       "xcmDocSequenceNumber": xcmDocSequenceNumber,
       "xcmDocName": xcmDocName,
       "xcmDocFileName": xcmDocFileName,
       "xcmDocFileNameType": xcmDocFileNameType,
       "xcmDocType": xcmDocType,
       "xcmDocFormat": xcmDocFormat,
       "xcmDocFormatVariants": xcmDocFormatVariants,
       "xcmDocFormatVersion": xcmDocFormatVersion,
       "xcmDocOctetCount": xcmDocOctetCount,
       "xcmDocState": xcmDocState,
       "xcmDocPrintExt": xcmDocPrintExt,
       "xcmDocPrintExtTable": xcmDocPrintExtTable,
       "xcmDocPrintExtEntry": xcmDocPrintExtEntry,
       "xcmDocPrintDefaultMediumName": xcmDocPrintDefaultMediumName,
       "xcmDocPrintDefaultInputIndex": xcmDocPrintDefaultInputIndex,
       "xcmDocPrintFinishing": xcmDocPrintFinishing,
       "xcmDocPrintOutputMethod": xcmDocPrintOutputMethod,
       "xcmDocPrintNumberUp": xcmDocPrintNumberUp,
       "xcmDocPrintSides": xcmDocPrintSides,
       "xcmDocPrintCopyCount": xcmDocPrintCopyCount,
       "xcmDocPrintCopiesCompleted": xcmDocPrintCopiesCompleted,
       "xcmJobGenSpoolingBasic": xcmJobGenSpoolingBasic,
       "xcmJobGenSpoolingBasicTable": xcmJobGenSpoolingBasicTable,
       "xcmJobGenSpoolingBasicEntry": xcmJobGenSpoolingBasicEntry,
       "xcmJobNumberOfJobResultSets": xcmJobNumberOfJobResultSets,
       "xcmJobPriority": xcmJobPriority,
       "xcmJobTotalOctetsHigh": xcmJobTotalOctetsHigh,
       "xcmJobTotalOctetsLow": xcmJobTotalOctetsLow,
       "xcmJobInterveningJobs": xcmJobInterveningJobs,
       "xcmJobGenSpoolingExt": xcmJobGenSpoolingExt,
       "xcmJobGenSpoolingExtTable": xcmJobGenSpoolingExtTable,
       "xcmJobGenSpoolingExtEntry": xcmJobGenSpoolingExtEntry,
       "xcmJobProcessAfter": xcmJobProcessAfter,
       "xcmJobDeadlineTime": xcmJobDeadlineTime,
       "xcmJobDiscardTime": xcmJobDiscardTime,
       "xcmJobRetentionPeriod": xcmJobRetentionPeriod,
       "xcmJobMessageToOperator": xcmJobMessageToOperator,
       "xcmJobMessageFromOperator": xcmJobMessageFromOperator,
       "xcmJobMessageFromAdministrator": xcmJobMessageFromAdministrator,
       "xcmJobPageCount": xcmJobPageCount,
       "xcmJobGenAccountingBasic": xcmJobGenAccountingBasic,
       "xcmJobGenAccountingBasicTable": xcmJobGenAccountingBasicTable,
       "xcmJobGenAccountingBasicEntry": xcmJobGenAccountingBasicEntry,
       "xcmJobAccountingBasicRowStatus": xcmJobAccountingBasicRowStatus,
       "xcmJobAccountingUserName": xcmJobAccountingUserName,
       "xcmJobAccountingInformation": xcmJobAccountingInformation,
       "xcmJobStartedProcessingTime": xcmJobStartedProcessingTime,
       "xcmJobImpressionsCompleted": xcmJobImpressionsCompleted,
       "xcmJobMediaSheetsCompleted": xcmJobMediaSheetsCompleted,
       "xcmJobCompletionTime": xcmJobCompletionTime,
       "xcmJobWorkUnitType": xcmJobWorkUnitType,
       "xcmJobUnitsOfWorkCompleted": xcmJobUnitsOfWorkCompleted,
       "xcmMediaConsumed": xcmMediaConsumed,
       "xcmMediaConsumedTable": xcmMediaConsumedTable,
       "xcmMediaConsumedEntry": xcmMediaConsumedEntry,
       "xcmMediaConsumedIndex": xcmMediaConsumedIndex,
       "xcmMediaConsumedRowStatus": xcmMediaConsumedRowStatus,
       "xcmMediaConsumedType": xcmMediaConsumedType,
       "xcmMediaConsumedName": xcmMediaConsumedName,
       "xcmMediaConsumedSheetCount": xcmMediaConsumedSheetCount,
       "xcmColorImpsConsumed": xcmColorImpsConsumed,
       "xcmColorImpsConsumedTable": xcmColorImpsConsumedTable,
       "xcmColorImpsConsumedEntry": xcmColorImpsConsumedEntry,
       "xcmColorImpsConsumedIndex": xcmColorImpsConsumedIndex,
       "xcmColorImpsConsumedRowStatus": xcmColorImpsConsumedRowStatus,
       "xcmColorImpsConsumedTypeIndex": xcmColorImpsConsumedTypeIndex,
       "xcmColorImpsConsumedCount": xcmColorImpsConsumedCount,
       "xcmJobAlert": xcmJobAlert,
       "xcmJobV1AlertNew": xcmJobV1AlertNew,
       "xcmJobV2AlertPrefixNew": xcmJobV2AlertPrefixNew,
       "xcmJobV2AlertNew": xcmJobV2AlertNew,
       "xcmDocAlert": xcmDocAlert,
       "xcmDocV1AlertNew": xcmDocV1AlertNew,
       "xcmDocV2AlertPrefixNew": xcmDocV2AlertPrefixNew,
       "xcmDocV2AlertNew": xcmDocV2AlertNew,
       "xcmJobImpsByMediumSize": xcmJobImpsByMediumSize,
       "xcmJobImpsByMediumSizeTable": xcmJobImpsByMediumSizeTable,
       "xcmJobImpsByMediumSizeEntry": xcmJobImpsByMediumSizeEntry,
       "xcmJobImpsByMediumSizeIndex": xcmJobImpsByMediumSizeIndex,
       "xcmJobImpsByMediumSizeRowStatus": xcmJobImpsByMediumSizeRowStatus,
       "xcmJobImpsByMediumSizeMediumSize": xcmJobImpsByMediumSizeMediumSize,
       "xcmJobImpsByMediumSizeCountType": xcmJobImpsByMediumSizeCountType,
       "xcmJobImpsByMediumSizeCount": xcmJobImpsByMediumSizeCount,
       "xcmJobImpsByMediumSizeCountQuality": xcmJobImpsByMediumSizeCountQuality}
)
