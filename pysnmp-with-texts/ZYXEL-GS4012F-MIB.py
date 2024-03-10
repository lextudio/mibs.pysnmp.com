"""SNMP MIB module (ZYXEL-GS4012F-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-GS4012F-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:05:46 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(OperationResponseStatus,) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "OperationResponseStatus")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ospfVirtIfNeighbor,
 ospfVirtIfAreaId,
 ospfNbrIpAddr,
 ospfAddressLessIf,
 ospfAreaId,
 ospfNbrAddressLessIndex,
 ospfIfIpAddress,
 ospfLsdbAreaId,
 ospfLsdbType,
 ospfLsdbLsid,
 ospfLsdbRouterId) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfVirtIfNeighbor",
    "ospfVirtIfAreaId",
    "ospfNbrIpAddr",
    "ospfAddressLessIf",
    "ospfAreaId",
    "ospfNbrAddressLessIndex",
    "ospfIfIpAddress",
    "ospfLsdbAreaId",
    "ospfLsdbType",
    "ospfLsdbLsid",
    "ospfLsdbRouterId")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

(ModuleIdentity,
 Bits,
 Counter64,
 IpAddress,
 iso,
 Gauge32,
 ObjectIdentity,
 NotificationType,
 Integer32,
 TimeTicks,
 enterprises,
 Counter32,
 Unsigned32,
 MibIdentifier,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "ModuleIdentity",
    "Bits",
    "Counter64",
    "IpAddress",
    "iso",
    "Gauge32",
    "ObjectIdentity",
    "NotificationType",
    "Integer32",
    "TimeTicks",
    "enterprises",
    "Counter32",
    "Unsigned32",
    "MibIdentifier",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

(StorageType,
 DisplayString,
 DateAndTime,
 RowStatus,
 MacAddress,
 TruthValue,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "StorageType",
    "DisplayString",
    "DateAndTime",
    "RowStatus",
    "MacAddress",
    "TruthValue",
    "TextualConvention")


# MODULE-IDENTITY

faultMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36)
)
faultMIB.setLastUpdated("200411031200Z")
if mibBuilder.loadTexts:
    faultMIB.setOrganization("""\
ZyXEL
""")
if mibBuilder.loadTexts:
    faultMIB.setDescription("""\
Fault event table definitions
""")

faultTrapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 37)
)
faultTrapsMIB.setLastUpdated("200411011200Z")
if mibBuilder.loadTexts:
    faultTrapsMIB.setOrganization("""\
ZyXEL
""")
if mibBuilder.loadTexts:
    faultTrapsMIB.setDescription("""\
Fault event trap definitions
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class UtcTimeStamp(TextualConvention, Unsigned32):
    status = "current"
    if mibBuilder.loadTexts:
        description = """\
Universal Time Coordinated as a 32-bit value that designates the number of
seconds since Jan 1, 1970 12:00AM.
"""


class EventIdNumber(TextualConvention, Integer32):
    status = "current"
    if mibBuilder.loadTexts:
        description = """\
This textual convention describes the index that uniquely identifies a fault
event type in the entire system. Every fault event type, e.g. link down, has a
unique EventIdNumber.
"""


class EventSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("informational", 4),
          ("major", 2),
          ("minor", 3))
    )

    if mibBuilder.loadTexts:
        description = """\
This textual convention describes the severity of a fault event. The decreasing
order of severity is shown in the textual convention.
"""


class EventServiceAffective(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noServiceAffected", 1),
          ("serviceAffected", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
This textual convention indicates whether an event is immediately service
affecting or not.
"""


class InstanceType(TextualConvention, Integer32):
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
        *(("l2Interface", 7),
          ("l3Interface", 8),
          ("line", 4),
          ("lsp", 6),
          ("node", 2),
          ("rowIndex", 9),
          ("shelf", 3),
          ("switch", 5),
          ("unknown", 1))
    )

    if mibBuilder.loadTexts:
        description = """\
This textual convention describes the type of an instanceId associated with
each event and by that means specifies how the instanceId variable should be
intepreted. Various instanceId types are specified below to enable fault
monitoring for different kind of devices from fixed configuration pizza boxes
to multi chassis nodes. All instanceId types may not need to be used in every
device type. Note also that instanceId semantics are element type dependent
(e.g. different kind of interface naming conventions may be used) and thus
instanceId usage may vary from element to element.
========================================================================= Type
Description Example form of InstanceId
=========================================================================
unknown (1) unknown type - Irrelevant-
------------------------------------------------------------------------- node
(2) Associated with events originating from 1 the node. Used for general events
that (Node number) can not be associated with any specific block. InstanceId
value 1 is used for single node equipment.
------------------------------------------------------------------------- shelf
(3) Associated with events originating from 1 the shelf. In the case of fixed
(shelf number) configuration devices this type is used for events that are
associated with the physical enclosure, e.g. faults related to fan etc.
InstanceId value 1 is used for single self equipment.
------------------------------------------------------------------------- line
(4) Associated with events originating from physical interfaces or associated
components such as line cards. InstanceId usage examples for faults originating
from: - Physical port: Simply port number, e.g. .......1
-------------------------------------------------------------------------
switch (5) Associated with events originating from 1 from a switch chip or a
switch card. (switch number) For single switch equipment InstanceId value 1 is
used, for multi swich nodes InstanceId semantics if for further study.
------------------------------------------------------------------------- lsp
(6) Associated with events originating from 1 a particular lsp. (lsp index)
NOTE: In this case the InstanceName contains the lsp name and InstanceId
contains lsp index.
-------------------------------------------------------------------------
l2Interface(7) Associated with events originating from - TBD - a particular
layer 2 interface. Used for layer 2 related events such as L2 control protocol
faults. InstanceId semantics is for further study.
-------------------------------------------------------------------------
l3Interface(8) Associated with events originating from - TBD - a particular
layer 3 interface. Used for layer 3 related events such as L3 control protocol
faults. InstanceId semantics is for further study.
-------------------------------------------------------------------------
rowIndex (9) Associated with events reporting about a 'logical' or conceptual
table that consists of rows. The Instance Id is the index/key for a row in the
table. The format of the Instance Id will simply be a series of decimal numbers
seperated by a '.':
=========================================================================
"""


class EventPersistence(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delta", 2),
          ("normal", 1))
    )

    if mibBuilder.loadTexts:
        description = """\
This textual convention indicates whether the event is delta (automatically and
immediately cleared) or normal (not automatically cleared).
"""


# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_EsSeries_ObjectIdentity = ObjectIdentity
esSeries = _EsSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8)
)
_Gs4012f_ObjectIdentity = ObjectIdentity
gs4012f = _Gs4012f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20)
)
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1)
)
_SysSwPlatformMajorVers_Type = Integer32
_SysSwPlatformMajorVers_Object = MibScalar
sysSwPlatformMajorVers = _SysSwPlatformMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1, 1),
    _SysSwPlatformMajorVers_Type()
)
sysSwPlatformMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMajorVers.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysSwPlatformMajorVers.setDescription("""\
SW platform major version, e.g. 3.
""")
_SysSwPlatformMinorVers_Type = Integer32
_SysSwPlatformMinorVers_Object = MibScalar
sysSwPlatformMinorVers = _SysSwPlatformMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1, 2),
    _SysSwPlatformMinorVers_Type()
)
sysSwPlatformMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMinorVers.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysSwPlatformMinorVers.setDescription("""\
SW platform minor version, e.g. 50.
""")
_SysSwModelString_Type = DisplayString
_SysSwModelString_Object = MibScalar
sysSwModelString = _SysSwModelString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1, 3),
    _SysSwModelString_Type()
)
sysSwModelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwModelString.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysSwModelString.setDescription("""\
Model letters, e.g. TJ
""")
_SysSwVersionControlNbr_Type = Integer32
_SysSwVersionControlNbr_Object = MibScalar
sysSwVersionControlNbr = _SysSwVersionControlNbr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1, 4),
    _SysSwVersionControlNbr_Type()
)
sysSwVersionControlNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwVersionControlNbr.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysSwVersionControlNbr.setDescription("""\
Version control number, e.g. 0.
""")
_SysSwDay_Type = Integer32
_SysSwDay_Object = MibScalar
sysSwDay = _SysSwDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1, 5),
    _SysSwDay_Type()
)
sysSwDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwDay.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysSwDay.setDescription("""\
SW compilation day, e.g. 19.
""")
_SysSwMonth_Type = Integer32
_SysSwMonth_Object = MibScalar
sysSwMonth = _SysSwMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1, 6),
    _SysSwMonth_Type()
)
sysSwMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMonth.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysSwMonth.setDescription("""\
SW compilation month, e.g. 8.
""")
_SysSwYear_Type = Integer32
_SysSwYear_Object = MibScalar
sysSwYear = _SysSwYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1, 7),
    _SysSwYear_Type()
)
sysSwYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwYear.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysSwYear.setDescription("""\
SW compilation year, e.g. 2004.
""")
_SysHwMajorVers_Type = Integer32
_SysHwMajorVers_Object = MibScalar
sysHwMajorVers = _SysHwMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1, 8),
    _SysHwMajorVers_Type()
)
sysHwMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMajorVers.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysHwMajorVers.setDescription("""\
HW major version number, e.g. 1.
""")
_SysHwMinorVers_Type = Integer32
_SysHwMinorVers_Object = MibScalar
sysHwMinorVers = _SysHwMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1, 9),
    _SysHwMinorVers_Type()
)
sysHwMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMinorVers.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysHwMinorVers.setDescription("""\
HW minor version number, e.g. 0.
""")
_SysSerialNumber_Type = DisplayString
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 1, 10),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysSerialNumber.setDescription("""\
Serial number
""")
_RateLimitSetup_ObjectIdentity = ObjectIdentity
rateLimitSetup = _RateLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 2)
)
_RateLimitState_Type = EnabledStatus
_RateLimitState_Object = MibScalar
rateLimitState = _RateLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 2, 1),
    _RateLimitState_Type()
)
rateLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitState.setStatus("mandatory")
if mibBuilder.loadTexts:
    rateLimitState.setDescription("""\
Ingress/egress rate limiting enabled/disabled for the switch.
""")
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 2, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("mandatory")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 2, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    rateLimitPortEntry.setDescription("""\
An entry in rateLimitPortTable.
""")
_RateLimitPortState_Type = EnabledStatus
_RateLimitPortState_Object = MibTableColumn
rateLimitPortState = _RateLimitPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 2, 2, 1, 1),
    _RateLimitPortState_Type()
)
rateLimitPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortState.setStatus("mandatory")
if mibBuilder.loadTexts:
    rateLimitPortState.setDescription("""\
Ingress/egress rate limiting enabled/disabled on the port.
""")
_RateLimitPortCommitRate_Type = Integer32
_RateLimitPortCommitRate_Object = MibTableColumn
rateLimitPortCommitRate = _RateLimitPortCommitRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 2, 2, 1, 2),
    _RateLimitPortCommitRate_Type()
)
rateLimitPortCommitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortCommitRate.setStatus("mandatory")
if mibBuilder.loadTexts:
    rateLimitPortCommitRate.setDescription("""\
Commit rate in Kbit/s. The range of FE port is between 0 and 100,000. For GE
port, the range is between 0 and 1000,000.
""")
_RateLimitPortPeakRate_Type = Integer32
_RateLimitPortPeakRate_Object = MibTableColumn
rateLimitPortPeakRate = _RateLimitPortPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 2, 2, 1, 3),
    _RateLimitPortPeakRate_Type()
)
rateLimitPortPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortPeakRate.setStatus("mandatory")
if mibBuilder.loadTexts:
    rateLimitPortPeakRate.setDescription("""\
Peak rate in Kbit/s. The range of FE port is between 1 and 100,000. For GE
port, the range is between 1 and 1000,000.
""")
_RateLimitPortEgrRate_Type = Integer32
_RateLimitPortEgrRate_Object = MibTableColumn
rateLimitPortEgrRate = _RateLimitPortEgrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 2, 2, 1, 4),
    _RateLimitPortEgrRate_Type()
)
rateLimitPortEgrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortEgrRate.setStatus("mandatory")
if mibBuilder.loadTexts:
    rateLimitPortEgrRate.setDescription("""\
Egress rate in Mbit/s. The granularity of FE port is between 1 and 100. For GE
port, the granularity is between 1 and 1000.
""")
_BrLimitSetup_ObjectIdentity = ObjectIdentity
brLimitSetup = _BrLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 3)
)
_BrLimitState_Type = EnabledStatus
_BrLimitState_Object = MibScalar
brLimitState = _BrLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 3, 1),
    _BrLimitState_Type()
)
brLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitState.setStatus("mandatory")
if mibBuilder.loadTexts:
    brLimitState.setDescription("""\
Broadcast/multicast/DLF rate limiting enabled/disabled for the switch.
""")
_BrLimitPortTable_Object = MibTable
brLimitPortTable = _BrLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 3, 2)
)
if mibBuilder.loadTexts:
    brLimitPortTable.setStatus("mandatory")
_BrLimitPortEntry_Object = MibTableRow
brLimitPortEntry = _BrLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 3, 2, 1)
)
brLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    brLimitPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    brLimitPortEntry.setDescription("""\
An entry in brLimitPortTable.
""")
_BrLimitPortBrState_Type = EnabledStatus
_BrLimitPortBrState_Object = MibTableColumn
brLimitPortBrState = _BrLimitPortBrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 3, 2, 1, 1),
    _BrLimitPortBrState_Type()
)
brLimitPortBrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortBrState.setStatus("mandatory")
if mibBuilder.loadTexts:
    brLimitPortBrState.setDescription("""\
Broadcast rate limiting enabled/disabled on the port.
""")
_BrLimitPortBrRate_Type = Integer32
_BrLimitPortBrRate_Object = MibTableColumn
brLimitPortBrRate = _BrLimitPortBrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 3, 2, 1, 2),
    _BrLimitPortBrRate_Type()
)
brLimitPortBrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortBrRate.setStatus("mandatory")
if mibBuilder.loadTexts:
    brLimitPortBrRate.setDescription("""\
Allowed broadcast rate in pkts/s. For FE port, the maximum value is 148800. For
GE port, the maximum value is 262143.
""")
_BrLimitPortMcState_Type = EnabledStatus
_BrLimitPortMcState_Object = MibTableColumn
brLimitPortMcState = _BrLimitPortMcState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 3, 2, 1, 3),
    _BrLimitPortMcState_Type()
)
brLimitPortMcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortMcState.setStatus("mandatory")
if mibBuilder.loadTexts:
    brLimitPortMcState.setDescription("""\
Multicast rate limiting enabled/disabled on the port.
""")
_BrLimitPortMcRate_Type = Integer32
_BrLimitPortMcRate_Object = MibTableColumn
brLimitPortMcRate = _BrLimitPortMcRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 3, 2, 1, 4),
    _BrLimitPortMcRate_Type()
)
brLimitPortMcRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortMcRate.setStatus("mandatory")
if mibBuilder.loadTexts:
    brLimitPortMcRate.setDescription("""\
AAllowed mullticast rate in pkts/s. For FE port, the maximum value is 148800.
For GE port, the maximum value is 262143.
""")
_BrLimitPortDlfState_Type = EnabledStatus
_BrLimitPortDlfState_Object = MibTableColumn
brLimitPortDlfState = _BrLimitPortDlfState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 3, 2, 1, 5),
    _BrLimitPortDlfState_Type()
)
brLimitPortDlfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortDlfState.setStatus("mandatory")
if mibBuilder.loadTexts:
    brLimitPortDlfState.setDescription("""\
Destination lookup failure frames rate limiting enabled/disabled on the port.
""")
_BrLimitPortDlfRate_Type = Integer32
_BrLimitPortDlfRate_Object = MibTableColumn
brLimitPortDlfRate = _BrLimitPortDlfRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 3, 2, 1, 6),
    _BrLimitPortDlfRate_Type()
)
brLimitPortDlfRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortDlfRate.setStatus("mandatory")
if mibBuilder.loadTexts:
    brLimitPortDlfRate.setDescription("""\
Allowed destination lookup failure frames rate in pkts/s. For FE port, the
maximum value is 148800. For GE port, the maximum value is 262143.
""")
_PortSecuritySetup_ObjectIdentity = ObjectIdentity
portSecuritySetup = _PortSecuritySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 4)
)
_PortSecurityState_Type = EnabledStatus
_PortSecurityState_Object = MibScalar
portSecurityState = _PortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 4, 1),
    _PortSecurityState_Type()
)
portSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityState.setStatus("mandatory")
_PortSecurityPortTable_Object = MibTable
portSecurityPortTable = _PortSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 4, 2)
)
if mibBuilder.loadTexts:
    portSecurityPortTable.setStatus("mandatory")
_PortSecurityPortEntry_Object = MibTableRow
portSecurityPortEntry = _PortSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 4, 2, 1)
)
portSecurityPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portSecurityPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    portSecurityPortEntry.setDescription("""\
An entry in portSecurityPortTable.
""")
_PortSecurityPortState_Type = EnabledStatus
_PortSecurityPortState_Object = MibTableColumn
portSecurityPortState = _PortSecurityPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 4, 2, 1, 1),
    _PortSecurityPortState_Type()
)
portSecurityPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortState.setStatus("mandatory")
if mibBuilder.loadTexts:
    portSecurityPortState.setDescription("""\
Port Security enabled/disabled on the port. Active(1) means this port only
accept frames from static MAC addresses that are configured for the port, and
dynamic MAC address frames up to the number specified by portSecurityPortCount
object.
""")
_PortSecurityPortLearnState_Type = EnabledStatus
_PortSecurityPortLearnState_Object = MibTableColumn
portSecurityPortLearnState = _PortSecurityPortLearnState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 4, 2, 1, 2),
    _PortSecurityPortLearnState_Type()
)
portSecurityPortLearnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortLearnState.setStatus("mandatory")
if mibBuilder.loadTexts:
    portSecurityPortLearnState.setDescription("""\
MAC address learning enabled/disable on the port.
""")
_PortSecurityPortCount_Type = Integer32
_PortSecurityPortCount_Object = MibTableColumn
portSecurityPortCount = _PortSecurityPortCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 4, 2, 1, 3),
    _PortSecurityPortCount_Type()
)
portSecurityPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortCount.setStatus("mandatory")
if mibBuilder.loadTexts:
    portSecurityPortCount.setDescription("""\
Number of (dynamic) MAC addresses that may be learned on the port.
""")
_PortSecurityMacFreeze_Type = PortList
_PortSecurityMacFreeze_Object = MibScalar
portSecurityMacFreeze = _PortSecurityMacFreeze_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 4, 3),
    _PortSecurityMacFreeze_Type()
)
portSecurityMacFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMacFreeze.setStatus("mandatory")
_VlanTrunkSetup_ObjectIdentity = ObjectIdentity
vlanTrunkSetup = _VlanTrunkSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 5)
)
_VlanTrunkPortTable_Object = MibTable
vlanTrunkPortTable = _VlanTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 5, 1)
)
if mibBuilder.loadTexts:
    vlanTrunkPortTable.setStatus("mandatory")
_VlanTrunkPortEntry_Object = MibTableRow
vlanTrunkPortEntry = _VlanTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 5, 1, 1)
)
vlanTrunkPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanTrunkPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    vlanTrunkPortEntry.setDescription("""\
An entry in vlanTrunkPortTable.
""")
_VlanTrunkPortState_Type = EnabledStatus
_VlanTrunkPortState_Object = MibTableColumn
vlanTrunkPortState = _VlanTrunkPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 5, 1, 1, 1),
    _VlanTrunkPortState_Type()
)
vlanTrunkPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkPortState.setStatus("mandatory")
if mibBuilder.loadTexts:
    vlanTrunkPortState.setDescription("""\
VlanTrunking enabled/disabled on the port. Active(1) to allow frames belonging
to unknown VLAN groups to pass through the switch.
""")
_CtlProtTransSetup_ObjectIdentity = ObjectIdentity
ctlProtTransSetup = _CtlProtTransSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 6)
)
_CtlProtTransState_Type = EnabledStatus
_CtlProtTransState_Object = MibScalar
ctlProtTransState = _CtlProtTransState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 6, 1),
    _CtlProtTransState_Type()
)
ctlProtTransState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlProtTransState.setStatus("mandatory")
if mibBuilder.loadTexts:
    ctlProtTransState.setDescription("""\
Bridge control protocol transparency enabled/disabled for the switch
""")
_CtlProtTransTunnelPortTable_Object = MibTable
ctlProtTransTunnelPortTable = _CtlProtTransTunnelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 6, 2)
)
if mibBuilder.loadTexts:
    ctlProtTransTunnelPortTable.setStatus("mandatory")
_CtlProtTransTunnelPortEntry_Object = MibTableRow
ctlProtTransTunnelPortEntry = _CtlProtTransTunnelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 6, 2, 1)
)
ctlProtTransTunnelPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    ctlProtTransTunnelPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    ctlProtTransTunnelPortEntry.setDescription("""\
An entry in ctlProtTransTunnelPortTable.
""")


class _CtlProtTransTunnelMode_Type(Integer32):
    """Custom type ctlProtTransTunnelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("network", 3),
          ("peer", 0),
          ("tunnel", 1))
    )


_CtlProtTransTunnelMode_Type.__name__ = "Integer32"
_CtlProtTransTunnelMode_Object = MibTableColumn
ctlProtTransTunnelMode = _CtlProtTransTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 6, 2, 1, 1),
    _CtlProtTransTunnelMode_Type()
)
ctlProtTransTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlProtTransTunnelMode.setStatus("mandatory")
if mibBuilder.loadTexts:
    ctlProtTransTunnelMode.setDescription("""\
Bridge control protocol transparency mode for the port. Modes: Peer(0),
Tunnel(1), Discard(2), Network(3)
""")
_VlanStackSetup_ObjectIdentity = ObjectIdentity
vlanStackSetup = _VlanStackSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 7)
)
_VlanStackState_Type = EnabledStatus
_VlanStackState_Object = MibScalar
vlanStackState = _VlanStackState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 7, 1),
    _VlanStackState_Type()
)
vlanStackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackState.setStatus("mandatory")
if mibBuilder.loadTexts:
    vlanStackState.setDescription("""\
VLAN Stacking enabled/disabled for the switch.
""")
_VlanStackTpid_Type = Integer32
_VlanStackTpid_Object = MibScalar
vlanStackTpid = _VlanStackTpid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 7, 2),
    _VlanStackTpid_Type()
)
vlanStackTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackTpid.setStatus("mandatory")
if mibBuilder.loadTexts:
    vlanStackTpid.setDescription("""\
SP TPID in hex format, e.g. 8100.
""")
_VlanStackPortTable_Object = MibTable
vlanStackPortTable = _VlanStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 7, 3)
)
if mibBuilder.loadTexts:
    vlanStackPortTable.setStatus("mandatory")
_VlanStackPortEntry_Object = MibTableRow
vlanStackPortEntry = _VlanStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 7, 3, 1)
)
vlanStackPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanStackPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    vlanStackPortEntry.setDescription("""\
An entry in vlanStackPortTable.
""")


class _VlanStackPortMode_Type(Integer32):
    """Custom type vlanStackPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("normal", 1),
          ("tunnel", 3))
    )


_VlanStackPortMode_Type.__name__ = "Integer32"
_VlanStackPortMode_Object = MibTableColumn
vlanStackPortMode = _VlanStackPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 7, 3, 1, 1),
    _VlanStackPortMode_Type()
)
vlanStackPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortMode.setStatus("mandatory")
if mibBuilder.loadTexts:
    vlanStackPortMode.setDescription("""\
Mode of the port.Set Access mode to have the switch add the SP TPID tag to all
incoming frames received on this port. Set Access mode for ingress ports at the
edge of the service provider's network. Set Tunnel mode (available for Gigabit
ports only) for egress ports at the edge of the service provider's network. In
order to support VLAN stacking on a port, the port must be able to allow frames
of 1526 Bytes (1522 Bytes + 4 Bytes for the second tag) to pass through it.
Access (0), tunnel (1)
""")
_VlanStackPortVid_Type = Integer32
_VlanStackPortVid_Object = MibTableColumn
vlanStackPortVid = _VlanStackPortVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 7, 3, 1, 2),
    _VlanStackPortVid_Type()
)
vlanStackPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortVid.setStatus("mandatory")
if mibBuilder.loadTexts:
    vlanStackPortVid.setDescription("""\
VLAN ID used in service provider tag.
""")


class _VlanStackPortPrio_Type(Integer32):
    """Custom type vlanStackPortPrio based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("prioriry-0", 0),
          ("prioriry-1", 1),
          ("prioriry-2", 2),
          ("prioriry-3", 3),
          ("prioriry-4", 4),
          ("prioriry-5", 5),
          ("prioriry-6", 6),
          ("prioriry-7", 7))
    )


_VlanStackPortPrio_Type.__name__ = "Integer32"
_VlanStackPortPrio_Object = MibTableColumn
vlanStackPortPrio = _VlanStackPortPrio_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 7, 3, 1, 3),
    _VlanStackPortPrio_Type()
)
vlanStackPortPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortPrio.setStatus("mandatory")
if mibBuilder.loadTexts:
    vlanStackPortPrio.setDescription("""\
Priority value for service provider tag. 0 is the lowest priority level and 7
is the highest.
""")
_Radius8021xSetup_ObjectIdentity = ObjectIdentity
radius8021xSetup = _Radius8021xSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8)
)
_RadiusLoginPrecedence_Type = Integer32
_RadiusLoginPrecedence_Object = MibScalar
radiusLoginPrecedence = _RadiusLoginPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 1),
    _RadiusLoginPrecedence_Type()
)
radiusLoginPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginPrecedence.setStatus("mandatory")
if mibBuilder.loadTexts:
    radiusLoginPrecedence.setDescription("""\
1. Local Only 2. Local then RADIUS 3. RADIUS Only
""")
_RadiusAnd8021xServer_ObjectIdentity = ObjectIdentity
radiusAnd8021xServer = _RadiusAnd8021xServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 2)
)
_RadiusIpAddr_Type = IpAddress
_RadiusIpAddr_Object = MibScalar
radiusIpAddr = _RadiusIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 2, 1),
    _RadiusIpAddr_Type()
)
radiusIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusIpAddr.setStatus("mandatory")
if mibBuilder.loadTexts:
    radiusIpAddr.setDescription("""\
The IP address of the RADIUS server.
""")
_RadiusUdpPort_Type = Integer32
_RadiusUdpPort_Object = MibScalar
radiusUdpPort = _RadiusUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 2, 2),
    _RadiusUdpPort_Type()
)
radiusUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusUdpPort.setStatus("mandatory")
if mibBuilder.loadTexts:
    radiusUdpPort.setDescription("""\
The UDP port of the RADIUS server.
""")
_RadiusSharedSecret_Type = DisplayString
_RadiusSharedSecret_Object = MibScalar
radiusSharedSecret = _RadiusSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 2, 3),
    _RadiusSharedSecret_Type()
)
radiusSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSharedSecret.setStatus("mandatory")
if mibBuilder.loadTexts:
    radiusSharedSecret.setDescription("""\
Shared secret used for RADIUS and network eleemnt authentication.
""")
_PortAuthState_Type = EnabledStatus
_PortAuthState_Object = MibScalar
portAuthState = _PortAuthState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 3),
    _PortAuthState_Type()
)
portAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthState.setStatus("mandatory")
if mibBuilder.loadTexts:
    portAuthState.setDescription("""\
802.1x port authentication enabled/disabled for the switch.
""")
_PortAuthTable_Object = MibTable
portAuthTable = _PortAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 4)
)
if mibBuilder.loadTexts:
    portAuthTable.setStatus("mandatory")
_PortAuthEntry_Object = MibTableRow
portAuthEntry = _PortAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 4, 1)
)
portAuthEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portAuthEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    portAuthEntry.setDescription("""\
An entry in portAuthTable.
""")
_PortAuthEntryState_Type = EnabledStatus
_PortAuthEntryState_Object = MibTableColumn
portAuthEntryState = _PortAuthEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 4, 1, 1),
    _PortAuthEntryState_Type()
)
portAuthEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthEntryState.setStatus("mandatory")
if mibBuilder.loadTexts:
    portAuthEntryState.setDescription("""\
802.1x port authentication enabled or disabled on the port.
""")
_PortReAuthEntryState_Type = EnabledStatus
_PortReAuthEntryState_Object = MibTableColumn
portReAuthEntryState = _PortReAuthEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 4, 1, 2),
    _PortReAuthEntryState_Type()
)
portReAuthEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReAuthEntryState.setStatus("mandatory")
if mibBuilder.loadTexts:
    portReAuthEntryState.setDescription("""\
802.1x port re-authentication enabled or disabled on the port.
""")
_PortReAuthEntryTimer_Type = Integer32
_PortReAuthEntryTimer_Object = MibTableColumn
portReAuthEntryTimer = _PortReAuthEntryTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 8, 4, 1, 3),
    _PortReAuthEntryTimer_Type()
)
portReAuthEntryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReAuthEntryTimer.setStatus("mandatory")
if mibBuilder.loadTexts:
    portReAuthEntryTimer.setDescription("""\
Re-authentication timer in seconds.
""")
_HwMonitorInfo_ObjectIdentity = ObjectIdentity
hwMonitorInfo = _HwMonitorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9)
)
_FanRpmTable_Object = MibTable
fanRpmTable = _FanRpmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 1)
)
if mibBuilder.loadTexts:
    fanRpmTable.setStatus("current")
_FanRpmEntry_Object = MibTableRow
fanRpmEntry = _FanRpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 1, 1)
)
fanRpmEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "fanRpmIndex"),
)
if mibBuilder.loadTexts:
    fanRpmEntry.setStatus("current")
if mibBuilder.loadTexts:
    fanRpmEntry.setDescription("""\
An entry in fanRpmTable.
""")
_FanRpmIndex_Type = Integer32
_FanRpmIndex_Object = MibTableColumn
fanRpmIndex = _FanRpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 1, 1, 1),
    _FanRpmIndex_Type()
)
fanRpmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmIndex.setStatus("current")
if mibBuilder.loadTexts:
    fanRpmIndex.setDescription("""\
Index of FAN.
""")
_FanRpmCurValue_Type = Integer32
_FanRpmCurValue_Object = MibTableColumn
fanRpmCurValue = _FanRpmCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 1, 1, 2),
    _FanRpmCurValue_Type()
)
fanRpmCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmCurValue.setStatus("current")
if mibBuilder.loadTexts:
    fanRpmCurValue.setDescription("""\
Current speed in Revolutions Per Minute (RPM) on the fan.
""")
_FanRpmMaxValue_Type = Integer32
_FanRpmMaxValue_Object = MibTableColumn
fanRpmMaxValue = _FanRpmMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 1, 1, 3),
    _FanRpmMaxValue_Type()
)
fanRpmMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    fanRpmMaxValue.setDescription("""\
Maximum speed measured in Revolutions Per Minute (RPM) on the fan.
""")
_FanRpmMinValue_Type = Integer32
_FanRpmMinValue_Object = MibTableColumn
fanRpmMinValue = _FanRpmMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 1, 1, 4),
    _FanRpmMinValue_Type()
)
fanRpmMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMinValue.setStatus("current")
if mibBuilder.loadTexts:
    fanRpmMinValue.setDescription("""\
Minimum speed measured in Revolutions Per Minute (RPM) on the fan.
""")
_FanRpmLowThresh_Type = Integer32
_FanRpmLowThresh_Object = MibTableColumn
fanRpmLowThresh = _FanRpmLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 1, 1, 5),
    _FanRpmLowThresh_Type()
)
fanRpmLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    fanRpmLowThresh.setDescription("""\
The minimum speed at which a normal fan should work.
""")
_FanRpmDescr_Type = DisplayString
_FanRpmDescr_Object = MibTableColumn
fanRpmDescr = _FanRpmDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 1, 1, 6),
    _FanRpmDescr_Type()
)
fanRpmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmDescr.setStatus("current")
if mibBuilder.loadTexts:
    fanRpmDescr.setDescription("""\
'Normal' indicates that this fan is functioning above the minimum speed.
'Error' indicates that this fan is functioning below the minimum speed.
""")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("current")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 2, 1)
)
tempEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("current")
if mibBuilder.loadTexts:
    tempEntry.setDescription("""\
An entry in tempTable.
""")


class _TempIndex_Type(Integer32):
    """Custom type tempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 2),
          ("mac", 1),
          ("phy", 3))
    )


_TempIndex_Type.__name__ = "Integer32"
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempIndex.setStatus("current")
if mibBuilder.loadTexts:
    tempIndex.setDescription("""\
Index of temperature unit. 1:MAC, 2:CPU, 3:PHY
""")
_TempCurValue_Type = Integer32
_TempCurValue_Object = MibTableColumn
tempCurValue = _TempCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 2, 1, 2),
    _TempCurValue_Type()
)
tempCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCurValue.setStatus("current")
if mibBuilder.loadTexts:
    tempCurValue.setDescription("""\
The current temperature measured at this sensor.
""")
_TempMaxValue_Type = Integer32
_TempMaxValue_Object = MibTableColumn
tempMaxValue = _TempMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 2, 1, 3),
    _TempMaxValue_Type()
)
tempMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    tempMaxValue.setDescription("""\
The maximum temperature measured at this sensor.
""")
_TempMinValue_Type = Integer32
_TempMinValue_Object = MibTableColumn
tempMinValue = _TempMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 2, 1, 4),
    _TempMinValue_Type()
)
tempMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMinValue.setStatus("current")
if mibBuilder.loadTexts:
    tempMinValue.setDescription("""\
The minimum temperature measured at this sensor.
""")
_TempHighThresh_Type = Integer32
_TempHighThresh_Object = MibTableColumn
tempHighThresh = _TempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 2, 1, 5),
    _TempHighThresh_Type()
)
tempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    tempHighThresh.setDescription("""\
The upper temperature limit at this sensor.
""")
_TempDescr_Type = DisplayString
_TempDescr_Object = MibTableColumn
tempDescr = _TempDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 2, 1, 6),
    _TempDescr_Type()
)
tempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDescr.setStatus("current")
if mibBuilder.loadTexts:
    tempDescr.setDescription("""\
'Normal' indicates temperatures below the threshold and 'Error' for those
above.
""")
_VoltageTable_Object = MibTable
voltageTable = _VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 3)
)
if mibBuilder.loadTexts:
    voltageTable.setStatus("current")
_VoltageEntry_Object = MibTableRow
voltageEntry = _VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 3, 1)
)
voltageEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "voltageIndex"),
)
if mibBuilder.loadTexts:
    voltageEntry.setStatus("current")
if mibBuilder.loadTexts:
    voltageEntry.setDescription("""\
An entry in voltageTable.
""")
_VoltageIndex_Type = Integer32
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 3, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("current")
if mibBuilder.loadTexts:
    voltageIndex.setDescription("""\
Index of voltage.
""")
_VoltageCurValue_Type = Integer32
_VoltageCurValue_Object = MibTableColumn
voltageCurValue = _VoltageCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 3, 1, 2),
    _VoltageCurValue_Type()
)
voltageCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageCurValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageCurValue.setDescription("""\
The current voltage reading.
""")
_VoltageMaxValue_Type = Integer32
_VoltageMaxValue_Object = MibTableColumn
voltageMaxValue = _VoltageMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 3, 1, 3),
    _VoltageMaxValue_Type()
)
voltageMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageMaxValue.setDescription("""\
The maximum voltage measured at this point.
""")
_VoltageMinValue_Type = Integer32
_VoltageMinValue_Object = MibTableColumn
voltageMinValue = _VoltageMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 3, 1, 4),
    _VoltageMinValue_Type()
)
voltageMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMinValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageMinValue.setDescription("""\
The minimum voltage measured at this point.
""")
_VoltageNominalValue_Type = Integer32
_VoltageNominalValue_Object = MibTableColumn
voltageNominalValue = _VoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 3, 1, 5),
    _VoltageNominalValue_Type()
)
voltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageNominalValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageNominalValue.setDescription("""\
The normal voltage at wchich the switch work.
""")
_VoltageLowThresh_Type = Integer32
_VoltageLowThresh_Object = MibTableColumn
voltageLowThresh = _VoltageLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 3, 1, 6),
    _VoltageLowThresh_Type()
)
voltageLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    voltageLowThresh.setDescription("""\
The minimum voltage at which the switch should work.
""")
_VoltageDescr_Type = DisplayString
_VoltageDescr_Object = MibTableColumn
voltageDescr = _VoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 9, 3, 1, 7),
    _VoltageDescr_Type()
)
voltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageDescr.setStatus("current")
if mibBuilder.loadTexts:
    voltageDescr.setDescription("""\
'Normal' indicates that the voltage is within an acceptable operating range at
this point; otherwise 'Error' is displayed.
""")
_SnmpSetup_ObjectIdentity = ObjectIdentity
snmpSetup = _SnmpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 10)
)
_SnmpGetCommunity_Type = DisplayString
_SnmpGetCommunity_Object = MibScalar
snmpGetCommunity = _SnmpGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 10, 1),
    _SnmpGetCommunity_Type()
)
snmpGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGetCommunity.setStatus("mandatory")
_SnmpSetCommunity_Type = DisplayString
_SnmpSetCommunity_Object = MibScalar
snmpSetCommunity = _SnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 10, 2),
    _SnmpSetCommunity_Type()
)
snmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSetCommunity.setStatus("mandatory")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 10, 3),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("mandatory")
_SnmpTrapDestTable_Object = MibTable
snmpTrapDestTable = _SnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 10, 4)
)
if mibBuilder.loadTexts:
    snmpTrapDestTable.setStatus("mandatory")
_SnmpTrapDestEntry_Object = MibTableRow
snmpTrapDestEntry = _SnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 10, 4, 1)
)
snmpTrapDestEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "snmpTrapDestIP"),
)
if mibBuilder.loadTexts:
    snmpTrapDestEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    snmpTrapDestEntry.setDescription("""\
An entry in snmpTrapDestTable.
""")
_SnmpTrapDestIP_Type = IpAddress
_SnmpTrapDestIP_Object = MibTableColumn
snmpTrapDestIP = _SnmpTrapDestIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 10, 4, 1, 1),
    _SnmpTrapDestIP_Type()
)
snmpTrapDestIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTrapDestIP.setStatus("mandatory")
if mibBuilder.loadTexts:
    snmpTrapDestIP.setDescription("""\
IP address of trap destination.
""")
_SnmpTrapDestRowStatus_Type = RowStatus
_SnmpTrapDestRowStatus_Object = MibTableColumn
snmpTrapDestRowStatus = _SnmpTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 10, 4, 1, 2),
    _SnmpTrapDestRowStatus_Type()
)
snmpTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestRowStatus.setStatus("mandatory")
_DateTimeServerSetup_ObjectIdentity = ObjectIdentity
dateTimeServerSetup = _DateTimeServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 11)
)


class _DateTimeServerType_Type(Integer32):
    """Custom type dateTimeServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("daytime", 2),
          ("none", 1),
          ("ntp", 4),
          ("time", 3))
    )


_DateTimeServerType_Type.__name__ = "Integer32"
_DateTimeServerType_Object = MibScalar
dateTimeServerType = _DateTimeServerType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 11, 1),
    _DateTimeServerType_Type()
)
dateTimeServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerType.setStatus("mandatory")
if mibBuilder.loadTexts:
    dateTimeServerType.setDescription("""\
The time service protocol.
""")
_DateTimeServerIP_Type = IpAddress
_DateTimeServerIP_Object = MibScalar
dateTimeServerIP = _DateTimeServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 11, 2),
    _DateTimeServerIP_Type()
)
dateTimeServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerIP.setStatus("mandatory")
if mibBuilder.loadTexts:
    dateTimeServerIP.setDescription("""\
IP address of time server.
""")
_DateTimeZone_Type = Integer32
_DateTimeZone_Object = MibScalar
dateTimeZone = _DateTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 11, 3),
    _DateTimeZone_Type()
)
dateTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeZone.setStatus("mandatory")
if mibBuilder.loadTexts:
    dateTimeZone.setDescription("""\
The time difference between UTC. Ex: +01
""")
_DateTimeNewDateYear_Type = Integer32
_DateTimeNewDateYear_Object = MibScalar
dateTimeNewDateYear = _DateTimeNewDateYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 11, 4),
    _DateTimeNewDateYear_Type()
)
dateTimeNewDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateYear.setStatus("mandatory")
if mibBuilder.loadTexts:
    dateTimeNewDateYear.setDescription("""\
The new date in year.
""")
_DateTimeNewDateMonth_Type = Integer32
_DateTimeNewDateMonth_Object = MibScalar
dateTimeNewDateMonth = _DateTimeNewDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 11, 5),
    _DateTimeNewDateMonth_Type()
)
dateTimeNewDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateMonth.setStatus("mandatory")
if mibBuilder.loadTexts:
    dateTimeNewDateMonth.setDescription("""\
The new date in month.
""")
_DateTimeNewDateDay_Type = Integer32
_DateTimeNewDateDay_Object = MibScalar
dateTimeNewDateDay = _DateTimeNewDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 11, 6),
    _DateTimeNewDateDay_Type()
)
dateTimeNewDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateDay.setStatus("mandatory")
if mibBuilder.loadTexts:
    dateTimeNewDateDay.setDescription("""\
The new date in day.
""")
_DateTimeNewTimeHour_Type = Integer32
_DateTimeNewTimeHour_Object = MibScalar
dateTimeNewTimeHour = _DateTimeNewTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 11, 7),
    _DateTimeNewTimeHour_Type()
)
dateTimeNewTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeHour.setStatus("mandatory")
if mibBuilder.loadTexts:
    dateTimeNewTimeHour.setDescription("""\
The new time in hour.
""")
_DateTimeNewTimeMinute_Type = Integer32
_DateTimeNewTimeMinute_Object = MibScalar
dateTimeNewTimeMinute = _DateTimeNewTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 11, 8),
    _DateTimeNewTimeMinute_Type()
)
dateTimeNewTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeMinute.setStatus("mandatory")
if mibBuilder.loadTexts:
    dateTimeNewTimeMinute.setDescription("""\
The new time in minute.
""")
_DateTimeNewTimeSecond_Type = Integer32
_DateTimeNewTimeSecond_Object = MibScalar
dateTimeNewTimeSecond = _DateTimeNewTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 11, 9),
    _DateTimeNewTimeSecond_Type()
)
dateTimeNewTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeSecond.setStatus("mandatory")
if mibBuilder.loadTexts:
    dateTimeNewTimeSecond.setDescription("""\
The new time in second.
""")
_SysMgmt_ObjectIdentity = ObjectIdentity
sysMgmt = _SysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 12)
)


class _SysMgmtConfigSave_Type(Integer32):
    """Custom type sysMgmtConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config-1", 1),
          ("config-2", 2))
    )


_SysMgmtConfigSave_Type.__name__ = "Integer32"
_SysMgmtConfigSave_Object = MibScalar
sysMgmtConfigSave = _SysMgmtConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 12, 1),
    _SysMgmtConfigSave_Type()
)
sysMgmtConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtConfigSave.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysMgmtConfigSave.setDescription("""\
If setting value is given, the variable write index will be set and running-
config will be written to the assigned configuration file. If not, running-
config will be written to the booting one.
""")


class _SysMgmtBootupConfig_Type(Integer32):
    """Custom type sysMgmtBootupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config-1", 1),
          ("config-2", 2))
    )


_SysMgmtBootupConfig_Type.__name__ = "Integer32"
_SysMgmtBootupConfig_Object = MibScalar
sysMgmtBootupConfig = _SysMgmtBootupConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 12, 2),
    _SysMgmtBootupConfig_Type()
)
sysMgmtBootupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtBootupConfig.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysMgmtBootupConfig.setDescription("""\
The setting value (read index) will be written into non-volatile memory. While
rebooting, the variable write index is equal to read index initially. You can
change the value of write index by CLI / MIB.
""")


class _SysMgmtReboot_Type(Integer32):
    """Custom type sysMgmtReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reboot", 1))
    )


_SysMgmtReboot_Type.__name__ = "Integer32"
_SysMgmtReboot_Object = MibScalar
sysMgmtReboot = _SysMgmtReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 12, 3),
    _SysMgmtReboot_Type()
)
sysMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysMgmtReboot.setDescription("""\
Reboot switch from SNMP. 1:Reboot, 0:Nothing
""")


class _SysMgmtDefaultConfig_Type(Integer32):
    """Custom type sysMgmtDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reset-to-default", 1))
    )


_SysMgmtDefaultConfig_Type.__name__ = "Integer32"
_SysMgmtDefaultConfig_Object = MibScalar
sysMgmtDefaultConfig = _SysMgmtDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 12, 4),
    _SysMgmtDefaultConfig_Type()
)
sysMgmtDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtDefaultConfig.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysMgmtDefaultConfig.setDescription("""\
Erase running config and reset to default.
""")


class _SysMgmtLastActionStatus_Type(Integer32):
    """Custom type sysMgmtLastActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("none", 0),
          ("success", 1))
    )


_SysMgmtLastActionStatus_Type.__name__ = "Integer32"
_SysMgmtLastActionStatus_Object = MibScalar
sysMgmtLastActionStatus = _SysMgmtLastActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 12, 5),
    _SysMgmtLastActionStatus_Type()
)
sysMgmtLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtLastActionStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysMgmtLastActionStatus.setDescription("""\
Display status of last mgmt action.
""")


class _SysMgmtSystemStatus_Type(Bits):
    """Custom type sysMgmtSystemStatus based on Bits"""
    namedValues = NamedValues(
        *(("sysAlarmDetected", 0),
          ("sysFanRPMError", 2),
          ("sysTemperatureError", 1),
          ("sysVoltageRangeError", 3))
    )

_SysMgmtSystemStatus_Type.__name__ = "Bits"
_SysMgmtSystemStatus_Object = MibScalar
sysMgmtSystemStatus = _SysMgmtSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 12, 6),
    _SysMgmtSystemStatus_Type()
)
sysMgmtSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtSystemStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysMgmtSystemStatus.setDescription("""\
This variable indicates the status of the system. The sysMgmtAlarmStatus is a
bit map represented a sum, therefore, it can represent multiple defects
simultaneously. The sysNoDefect should be set if and only if no other flag is
set. The various bit positions are: 0 sysAlarmDetected 1 sysTemperatureError 2
sysFanRPMError 3 sysVoltageRangeError
""")
_SysMgmtCPUUsage_Type = Integer32
_SysMgmtCPUUsage_Object = MibScalar
sysMgmtCPUUsage = _SysMgmtCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 12, 7),
    _SysMgmtCPUUsage_Type()
)
sysMgmtCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCPUUsage.setStatus("mandatory")
if mibBuilder.loadTexts:
    sysMgmtCPUUsage.setDescription("""\
Show device CPU load in %, it's the snapshot of CPU load when getting the
values.
""")
_Layer2Setup_ObjectIdentity = ObjectIdentity
layer2Setup = _Layer2Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 13)
)


class _VlanTypeSetup_Type(Integer32):
    """Custom type vlanTypeSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1Q", 1),
          ("port-based", 2))
    )


_VlanTypeSetup_Type.__name__ = "Integer32"
_VlanTypeSetup_Object = MibScalar
vlanTypeSetup = _VlanTypeSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 13, 1),
    _VlanTypeSetup_Type()
)
vlanTypeSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTypeSetup.setStatus("mandatory")
_IgmpSnoopingStateSetup_Type = EnabledStatus
_IgmpSnoopingStateSetup_Object = MibScalar
igmpSnoopingStateSetup = _IgmpSnoopingStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 13, 2),
    _IgmpSnoopingStateSetup_Type()
)
igmpSnoopingStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingStateSetup.setStatus("mandatory")
_TagVlanPortIsolationState_Type = EnabledStatus
_TagVlanPortIsolationState_Object = MibScalar
tagVlanPortIsolationState = _TagVlanPortIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 13, 3),
    _TagVlanPortIsolationState_Type()
)
tagVlanPortIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tagVlanPortIsolationState.setStatus("mandatory")
_StpState_Type = EnabledStatus
_StpState_Object = MibScalar
stpState = _StpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 13, 4),
    _StpState_Type()
)
stpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpState.setStatus("mandatory")
_IgmpFilteringStateSetup_Type = EnabledStatus
_IgmpFilteringStateSetup_Object = MibScalar
igmpFilteringStateSetup = _IgmpFilteringStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 13, 5),
    _IgmpFilteringStateSetup_Type()
)
igmpFilteringStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpFilteringStateSetup.setStatus("mandatory")


class _UnknownMulticastFrameForwarding_Type(Integer32):
    """Custom type unknownMulticastFrameForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("flooding", 1))
    )


_UnknownMulticastFrameForwarding_Type.__name__ = "Integer32"
_UnknownMulticastFrameForwarding_Object = MibScalar
unknownMulticastFrameForwarding = _UnknownMulticastFrameForwarding_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 13, 6),
    _UnknownMulticastFrameForwarding_Type()
)
unknownMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownMulticastFrameForwarding.setStatus("mandatory")
_IpSetup_ObjectIdentity = ObjectIdentity
ipSetup = _IpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14)
)
_DnsIpAddress_Type = IpAddress
_DnsIpAddress_Object = MibScalar
dnsIpAddress = _DnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 1),
    _DnsIpAddress_Type()
)
dnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsIpAddress.setStatus("mandatory")


class _DefaultMgmt_Type(Integer32):
    """Custom type defaultMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in-band", 0),
          ("out-of-band", 1))
    )


_DefaultMgmt_Type.__name__ = "Integer32"
_DefaultMgmt_Object = MibScalar
defaultMgmt = _DefaultMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 2),
    _DefaultMgmt_Type()
)
defaultMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMgmt.setStatus("mandatory")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 3),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("mandatory")
_OutOfBandIpSetup_ObjectIdentity = ObjectIdentity
outOfBandIpSetup = _OutOfBandIpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 4)
)
_OutOfBandIp_Type = IpAddress
_OutOfBandIp_Object = MibScalar
outOfBandIp = _OutOfBandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 4, 1),
    _OutOfBandIp_Type()
)
outOfBandIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandIp.setStatus("mandatory")
_OutOfBandSubnetMask_Type = IpAddress
_OutOfBandSubnetMask_Object = MibScalar
outOfBandSubnetMask = _OutOfBandSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 4, 2),
    _OutOfBandSubnetMask_Type()
)
outOfBandSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandSubnetMask.setStatus("mandatory")
_OutOfBandGateway_Type = IpAddress
_OutOfBandGateway_Object = MibScalar
outOfBandGateway = _OutOfBandGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 4, 3),
    _OutOfBandGateway_Type()
)
outOfBandGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandGateway.setStatus("mandatory")
_MaxNumOfInbandIp_Type = Integer32
_MaxNumOfInbandIp_Object = MibScalar
maxNumOfInbandIp = _MaxNumOfInbandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 5),
    _MaxNumOfInbandIp_Type()
)
maxNumOfInbandIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfInbandIp.setStatus("mandatory")
_InbandIpTable_Object = MibTable
inbandIpTable = _InbandIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 6)
)
if mibBuilder.loadTexts:
    inbandIpTable.setStatus("mandatory")
_InbandIpEntry_Object = MibTableRow
inbandIpEntry = _InbandIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 6, 1)
)
inbandIpEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "inbandEntryIp"),
    (0, "ZYXEL-GS4012F-MIB", "inbandEntrySubnetMask"),
)
if mibBuilder.loadTexts:
    inbandIpEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    inbandIpEntry.setDescription("""\
An entry in inbandIpTable.
""")
_InbandEntryIp_Type = IpAddress
_InbandEntryIp_Object = MibTableColumn
inbandEntryIp = _InbandEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 6, 1, 1),
    _InbandEntryIp_Type()
)
inbandEntryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryIp.setStatus("mandatory")
_InbandEntrySubnetMask_Type = IpAddress
_InbandEntrySubnetMask_Object = MibTableColumn
inbandEntrySubnetMask = _InbandEntrySubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 6, 1, 2),
    _InbandEntrySubnetMask_Type()
)
inbandEntrySubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntrySubnetMask.setStatus("mandatory")
_InbandEntryVid_Type = Integer32
_InbandEntryVid_Object = MibTableColumn
inbandEntryVid = _InbandEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 6, 1, 3),
    _InbandEntryVid_Type()
)
inbandEntryVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryVid.setStatus("mandatory")
_InbandEntryRowStatus_Type = RowStatus
_InbandEntryRowStatus_Object = MibTableColumn
inbandEntryRowStatus = _InbandEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 14, 6, 1, 4),
    _InbandEntryRowStatus_Type()
)
inbandEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inbandEntryRowStatus.setStatus("mandatory")
_FilterSetup_ObjectIdentity = ObjectIdentity
filterSetup = _FilterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 15)
)
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 15, 1)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("mandatory")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 15, 1, 1)
)
filterEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "filterMacAddr"),
    (0, "ZYXEL-GS4012F-MIB", "filterVid"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    filterEntry.setDescription("""\
An entry in filterTable.
""")
_FilterName_Type = DisplayString
_FilterName_Object = MibTableColumn
filterName = _FilterName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 15, 1, 1, 1),
    _FilterName_Type()
)
filterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterName.setStatus("mandatory")


class _FilterActionState_Type(Integer32):
    """Custom type filterActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("discard-destination", 2),
          ("discard-source", 1))
    )


_FilterActionState_Type.__name__ = "Integer32"
_FilterActionState_Object = MibTableColumn
filterActionState = _FilterActionState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 15, 1, 1, 2),
    _FilterActionState_Type()
)
filterActionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterActionState.setStatus("mandatory")
_FilterMacAddr_Type = MacAddress
_FilterMacAddr_Object = MibTableColumn
filterMacAddr = _FilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 15, 1, 1, 3),
    _FilterMacAddr_Type()
)
filterMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterMacAddr.setStatus("mandatory")
_FilterVid_Type = Integer32
_FilterVid_Object = MibTableColumn
filterVid = _FilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 15, 1, 1, 4),
    _FilterVid_Type()
)
filterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterVid.setStatus("mandatory")
_FilterRowStatus_Type = RowStatus
_FilterRowStatus_Object = MibTableColumn
filterRowStatus = _FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 15, 1, 1, 5),
    _FilterRowStatus_Type()
)
filterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRowStatus.setStatus("mandatory")
_MirrorSetup_ObjectIdentity = ObjectIdentity
mirrorSetup = _MirrorSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 16)
)
_MirrorState_Type = EnabledStatus
_MirrorState_Object = MibScalar
mirrorState = _MirrorState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 16, 1),
    _MirrorState_Type()
)
mirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorState.setStatus("mandatory")
_MirrorMonitorPort_Type = Integer32
_MirrorMonitorPort_Object = MibScalar
mirrorMonitorPort = _MirrorMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 16, 2),
    _MirrorMonitorPort_Type()
)
mirrorMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMonitorPort.setStatus("mandatory")
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 16, 3)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("mandatory")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 16, 3, 1)
)
mirrorEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    mirrorEntry.setDescription("""\
An entry in mirrorTable.
""")
_MirrorMirroredState_Type = EnabledStatus
_MirrorMirroredState_Object = MibTableColumn
mirrorMirroredState = _MirrorMirroredState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 16, 3, 1, 1),
    _MirrorMirroredState_Type()
)
mirrorMirroredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMirroredState.setStatus("mandatory")


class _MirrorDirection_Type(Integer32):
    """Custom type mirrorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("egress", 1),
          ("ingress", 0))
    )


_MirrorDirection_Type.__name__ = "Integer32"
_MirrorDirection_Object = MibTableColumn
mirrorDirection = _MirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 16, 3, 1, 2),
    _MirrorDirection_Type()
)
mirrorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorDirection.setStatus("mandatory")
_AggrSetup_ObjectIdentity = ObjectIdentity
aggrSetup = _AggrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17)
)
_AggrState_Type = EnabledStatus
_AggrState_Object = MibScalar
aggrState = _AggrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 1),
    _AggrState_Type()
)
aggrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrState.setStatus("mandatory")
_AggrSystemPriority_Type = Integer32
_AggrSystemPriority_Object = MibScalar
aggrSystemPriority = _AggrSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 2),
    _AggrSystemPriority_Type()
)
aggrSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrSystemPriority.setStatus("mandatory")
_AggrGroupTable_Object = MibTable
aggrGroupTable = _AggrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 3)
)
if mibBuilder.loadTexts:
    aggrGroupTable.setStatus("mandatory")
_AggrGroupEntry_Object = MibTableRow
aggrGroupEntry = _AggrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 3, 1)
)
aggrGroupEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "aggrGroupIndex"),
)
if mibBuilder.loadTexts:
    aggrGroupEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    aggrGroupEntry.setDescription("""\
An entry in aggrGroupTable.
""")
_AggrGroupIndex_Type = Integer32
_AggrGroupIndex_Object = MibTableColumn
aggrGroupIndex = _AggrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 3, 1, 1),
    _AggrGroupIndex_Type()
)
aggrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrGroupIndex.setStatus("mandatory")
_AggrGroupState_Type = EnabledStatus
_AggrGroupState_Object = MibTableColumn
aggrGroupState = _AggrGroupState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 3, 1, 2),
    _AggrGroupState_Type()
)
aggrGroupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupState.setStatus("mandatory")
_AggrGroupDynamicState_Type = EnabledStatus
_AggrGroupDynamicState_Object = MibTableColumn
aggrGroupDynamicState = _AggrGroupDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 3, 1, 3),
    _AggrGroupDynamicState_Type()
)
aggrGroupDynamicState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupDynamicState.setStatus("mandatory")
_AggrPortTable_Object = MibTable
aggrPortTable = _AggrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 4)
)
if mibBuilder.loadTexts:
    aggrPortTable.setStatus("mandatory")
_AggrPortEntry_Object = MibTableRow
aggrPortEntry = _AggrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 4, 1)
)
aggrPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    aggrPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    aggrPortEntry.setDescription("""\
An entry in aggrPortTable.
""")


class _AggrPortGroup_Type(Integer32):
    """Custom type aggrPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("t1", 1),
          ("t2", 2),
          ("t3", 3),
          ("t4", 4),
          ("t5", 5),
          ("t6", 6))
    )


_AggrPortGroup_Type.__name__ = "Integer32"
_AggrPortGroup_Object = MibTableColumn
aggrPortGroup = _AggrPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 4, 1, 1),
    _AggrPortGroup_Type()
)
aggrPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortGroup.setStatus("mandatory")
_AggrPortDynamicStateTimeout_Type = Integer32
_AggrPortDynamicStateTimeout_Object = MibTableColumn
aggrPortDynamicStateTimeout = _AggrPortDynamicStateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 17, 4, 1, 2),
    _AggrPortDynamicStateTimeout_Type()
)
aggrPortDynamicStateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortDynamicStateTimeout.setStatus("mandatory")
_AccessCtlSetup_ObjectIdentity = ObjectIdentity
accessCtlSetup = _AccessCtlSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18)
)
_AccessCtlTable_Object = MibTable
accessCtlTable = _AccessCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 1)
)
if mibBuilder.loadTexts:
    accessCtlTable.setStatus("mandatory")
_AccessCtlEntry_Object = MibTableRow
accessCtlEntry = _AccessCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 1, 1)
)
accessCtlEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "accessCtlService"),
)
if mibBuilder.loadTexts:
    accessCtlEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    accessCtlEntry.setDescription("""\
An entry in accessCtlTable.
""")


class _AccessCtlService_Type(Integer32):
    """Custom type accessCtlService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 3),
          ("http", 4),
          ("https", 5),
          ("icmp", 6),
          ("snmp", 7),
          ("ssh", 2),
          ("telnet", 1))
    )


_AccessCtlService_Type.__name__ = "Integer32"
_AccessCtlService_Object = MibTableColumn
accessCtlService = _AccessCtlService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 1, 1, 1),
    _AccessCtlService_Type()
)
accessCtlService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessCtlService.setStatus("mandatory")
_AccessCtlEnable_Type = EnabledStatus
_AccessCtlEnable_Object = MibTableColumn
accessCtlEnable = _AccessCtlEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 1, 1, 2),
    _AccessCtlEnable_Type()
)
accessCtlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlEnable.setStatus("mandatory")
_AccessCtlServicePort_Type = Integer32
_AccessCtlServicePort_Object = MibTableColumn
accessCtlServicePort = _AccessCtlServicePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 1, 1, 3),
    _AccessCtlServicePort_Type()
)
accessCtlServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlServicePort.setStatus("mandatory")
_AccessCtlTimeout_Type = Integer32
_AccessCtlTimeout_Object = MibTableColumn
accessCtlTimeout = _AccessCtlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 1, 1, 4),
    _AccessCtlTimeout_Type()
)
accessCtlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlTimeout.setStatus("mandatory")
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 2)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("mandatory")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 2, 1)
)
securedClientEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    securedClientEntry.setDescription("""\
An entry in securedClientTable.
""")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 2, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("mandatory")
_SecuredClientEnable_Type = EnabledStatus
_SecuredClientEnable_Object = MibTableColumn
securedClientEnable = _SecuredClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 2, 1, 2),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("mandatory")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 2, 1, 3),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("mandatory")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 2, 1, 4),
    _SecuredClientEndIp_Type()
)
securedClientEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIp.setStatus("mandatory")


class _SecuredClientService_Type(Bits):
    """Custom type securedClientService based on Bits"""
    namedValues = NamedValues(
        *(("ftp", 1),
          ("http", 2),
          ("https", 6),
          ("icmp", 3),
          ("snmp", 4),
          ("ssh", 5),
          ("telnet", 0))
    )

_SecuredClientService_Type.__name__ = "Bits"
_SecuredClientService_Object = MibTableColumn
securedClientService = _SecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 18, 2, 1, 5),
    _SecuredClientService_Type()
)
securedClientService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientService.setStatus("mandatory")
_QueuingMethodSetup_ObjectIdentity = ObjectIdentity
queuingMethodSetup = _QueuingMethodSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 19)
)
_PortQueuingMethodTable_Object = MibTable
portQueuingMethodTable = _PortQueuingMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 19, 1)
)
if mibBuilder.loadTexts:
    portQueuingMethodTable.setStatus("mandatory")
_PortQueuingMethodEntry_Object = MibTableRow
portQueuingMethodEntry = _PortQueuingMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 19, 1, 1)
)
portQueuingMethodEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-GS4012F-MIB", "portQueuingMethodQueue"),
)
if mibBuilder.loadTexts:
    portQueuingMethodEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    portQueuingMethodEntry.setDescription("""\
An entry in portQueuingMethodTable.
""")
_PortQueuingMethodQueue_Type = Integer32
_PortQueuingMethodQueue_Object = MibTableColumn
portQueuingMethodQueue = _PortQueuingMethodQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 19, 1, 1, 1),
    _PortQueuingMethodQueue_Type()
)
portQueuingMethodQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portQueuingMethodQueue.setStatus("mandatory")
if mibBuilder.loadTexts:
    portQueuingMethodQueue.setDescription("""\
0...7
""")
_PortQueuingMethodWeight_Type = Integer32
_PortQueuingMethodWeight_Object = MibTableColumn
portQueuingMethodWeight = _PortQueuingMethodWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 19, 1, 1, 2),
    _PortQueuingMethodWeight_Type()
)
portQueuingMethodWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodWeight.setStatus("mandatory")
if mibBuilder.loadTexts:
    portQueuingMethodWeight.setDescription("""\
0...15
""")


class _PortQueuingMethodMode_Type(Integer32):
    """Custom type portQueuingMethodMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strictly-priority", 0),
          ("weighted-round-robin", 1))
    )


_PortQueuingMethodMode_Type.__name__ = "Integer32"
_PortQueuingMethodMode_Object = MibTableColumn
portQueuingMethodMode = _PortQueuingMethodMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 19, 1, 1, 3),
    _PortQueuingMethodMode_Type()
)
portQueuingMethodMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodMode.setStatus("mandatory")
_DhcpSetup_ObjectIdentity = ObjectIdentity
dhcpSetup = _DhcpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20)
)
_DhcpRelay_ObjectIdentity = ObjectIdentity
dhcpRelay = _DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 1)
)
_DhcpRelayEnable_Type = EnabledStatus
_DhcpRelayEnable_Object = MibScalar
dhcpRelayEnable = _DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 1, 1),
    _DhcpRelayEnable_Type()
)
dhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayEnable.setStatus("mandatory")
_DhcpRelayOption82Enable_Type = EnabledStatus
_DhcpRelayOption82Enable_Object = MibScalar
dhcpRelayOption82Enable = _DhcpRelayOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 1, 2),
    _DhcpRelayOption82Enable_Type()
)
dhcpRelayOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Enable.setStatus("mandatory")
_DhcpRelayInfoEnable_Type = EnabledStatus
_DhcpRelayInfoEnable_Object = MibScalar
dhcpRelayInfoEnable = _DhcpRelayInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 1, 3),
    _DhcpRelayInfoEnable_Type()
)
dhcpRelayInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayInfoEnable.setStatus("mandatory")
_DhcpRelayInfoData_Type = DisplayString
_DhcpRelayInfoData_Object = MibScalar
dhcpRelayInfoData = _DhcpRelayInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 1, 4),
    _DhcpRelayInfoData_Type()
)
dhcpRelayInfoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayInfoData.setStatus("mandatory")
_MaxNumberOfDhcpRemoteServer_Type = Integer32
_MaxNumberOfDhcpRemoteServer_Object = MibScalar
maxNumberOfDhcpRemoteServer = _MaxNumberOfDhcpRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 1, 5),
    _MaxNumberOfDhcpRemoteServer_Type()
)
maxNumberOfDhcpRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpRemoteServer.setStatus("mandatory")
_DhcpRemoteServerTable_Object = MibTable
dhcpRemoteServerTable = _DhcpRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 1, 6)
)
if mibBuilder.loadTexts:
    dhcpRemoteServerTable.setStatus("mandatory")
_DhcpRemoteServerEntry_Object = MibTableRow
dhcpRemoteServerEntry = _DhcpRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 1, 6, 1)
)
dhcpRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "dhcpRemoteServerIp"),
)
if mibBuilder.loadTexts:
    dhcpRemoteServerEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    dhcpRemoteServerEntry.setDescription("""\
An entry in dhcpRemoteServerTable.
""")
_DhcpRemoteServerIp_Type = IpAddress
_DhcpRemoteServerIp_Object = MibTableColumn
dhcpRemoteServerIp = _DhcpRemoteServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 1, 6, 1, 1),
    _DhcpRemoteServerIp_Type()
)
dhcpRemoteServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRemoteServerIp.setStatus("mandatory")
_DhcpRemoteServerRowStatus_Type = RowStatus
_DhcpRemoteServerRowStatus_Object = MibTableColumn
dhcpRemoteServerRowStatus = _DhcpRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 1, 6, 1, 2),
    _DhcpRemoteServerRowStatus_Type()
)
dhcpRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRemoteServerRowStatus.setStatus("mandatory")
_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2)
)
_MaxNumberOfDhcpServers_Type = Integer32
_MaxNumberOfDhcpServers_Object = MibScalar
maxNumberOfDhcpServers = _MaxNumberOfDhcpServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 1),
    _MaxNumberOfDhcpServers_Type()
)
maxNumberOfDhcpServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpServers.setStatus("mandatory")
_DhcpServerTable_Object = MibTable
dhcpServerTable = _DhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 2)
)
if mibBuilder.loadTexts:
    dhcpServerTable.setStatus("mandatory")
_DhcpServerEntry_Object = MibTableRow
dhcpServerEntry = _DhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 2, 1)
)
dhcpServerEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "dhcpServerVid"),
)
if mibBuilder.loadTexts:
    dhcpServerEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    dhcpServerEntry.setDescription("""\
An entry in dhcpServerTable.
""")
_DhcpServerVid_Type = Integer32
_DhcpServerVid_Object = MibTableColumn
dhcpServerVid = _DhcpServerVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 2, 1, 1),
    _DhcpServerVid_Type()
)
dhcpServerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerVid.setStatus("mandatory")
_DhcpServerStartAddr_Type = IpAddress
_DhcpServerStartAddr_Object = MibTableColumn
dhcpServerStartAddr = _DhcpServerStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 2, 1, 2),
    _DhcpServerStartAddr_Type()
)
dhcpServerStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerStartAddr.setStatus("mandatory")
_DhcpServerPoolSize_Type = Integer32
_DhcpServerPoolSize_Object = MibTableColumn
dhcpServerPoolSize = _DhcpServerPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 2, 1, 3),
    _DhcpServerPoolSize_Type()
)
dhcpServerPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerPoolSize.setStatus("mandatory")
_DhcpServerMask_Type = IpAddress
_DhcpServerMask_Object = MibTableColumn
dhcpServerMask = _DhcpServerMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 2, 1, 4),
    _DhcpServerMask_Type()
)
dhcpServerMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerMask.setStatus("mandatory")
_DhcpServerGateway_Type = IpAddress
_DhcpServerGateway_Object = MibTableColumn
dhcpServerGateway = _DhcpServerGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 2, 1, 5),
    _DhcpServerGateway_Type()
)
dhcpServerGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerGateway.setStatus("mandatory")
_DhcpServerPrimaryDNS_Type = IpAddress
_DhcpServerPrimaryDNS_Object = MibTableColumn
dhcpServerPrimaryDNS = _DhcpServerPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 2, 1, 6),
    _DhcpServerPrimaryDNS_Type()
)
dhcpServerPrimaryDNS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerPrimaryDNS.setStatus("mandatory")
_DhcpServerSecondaryDNS_Type = IpAddress
_DhcpServerSecondaryDNS_Object = MibTableColumn
dhcpServerSecondaryDNS = _DhcpServerSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 2, 1, 7),
    _DhcpServerSecondaryDNS_Type()
)
dhcpServerSecondaryDNS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerSecondaryDNS.setStatus("mandatory")
_DhcpServerRowStatus_Type = RowStatus
_DhcpServerRowStatus_Object = MibTableColumn
dhcpServerRowStatus = _DhcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 20, 2, 2, 1, 8),
    _DhcpServerRowStatus_Type()
)
dhcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerRowStatus.setStatus("mandatory")
_StaticRouteSetup_ObjectIdentity = ObjectIdentity
staticRouteSetup = _StaticRouteSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 21)
)
_MaxNumberOfStaticRoutes_Type = Integer32
_MaxNumberOfStaticRoutes_Object = MibScalar
maxNumberOfStaticRoutes = _MaxNumberOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 21, 1),
    _MaxNumberOfStaticRoutes_Type()
)
maxNumberOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfStaticRoutes.setStatus("mandatory")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 21, 2)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("mandatory")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 21, 2, 1)
)
staticRouteEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "staticRouteIp"),
    (0, "ZYXEL-GS4012F-MIB", "staticRouteMask"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    staticRouteEntry.setDescription("""\
An entry in staticRouteTable.
""")
_StaticRouteName_Type = DisplayString
_StaticRouteName_Object = MibTableColumn
staticRouteName = _StaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 21, 2, 1, 1),
    _StaticRouteName_Type()
)
staticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteName.setStatus("mandatory")
_StaticRouteIp_Type = IpAddress
_StaticRouteIp_Object = MibTableColumn
staticRouteIp = _StaticRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 21, 2, 1, 2),
    _StaticRouteIp_Type()
)
staticRouteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteIp.setStatus("mandatory")
_StaticRouteMask_Type = IpAddress
_StaticRouteMask_Object = MibTableColumn
staticRouteMask = _StaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 21, 2, 1, 3),
    _StaticRouteMask_Type()
)
staticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteMask.setStatus("mandatory")
_StaticRouteGateway_Type = IpAddress
_StaticRouteGateway_Object = MibTableColumn
staticRouteGateway = _StaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 21, 2, 1, 4),
    _StaticRouteGateway_Type()
)
staticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteGateway.setStatus("mandatory")
_StaticRouteMetric_Type = Integer32
_StaticRouteMetric_Object = MibTableColumn
staticRouteMetric = _StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 21, 2, 1, 5),
    _StaticRouteMetric_Type()
)
staticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteMetric.setStatus("mandatory")
_StaticRouteRowStatus_Type = RowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 21, 2, 1, 6),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("mandatory")
_ArpInfo_ObjectIdentity = ObjectIdentity
arpInfo = _ArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 22)
)
_ArpTable_Object = MibTable
arpTable = _ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 22, 1)
)
if mibBuilder.loadTexts:
    arpTable.setStatus("mandatory")
_ArpEntry_Object = MibTableRow
arpEntry = _ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 22, 1, 1)
)
arpEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "arpIpAddr"),
    (0, "ZYXEL-GS4012F-MIB", "arpMacVid"),
)
if mibBuilder.loadTexts:
    arpEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    arpEntry.setDescription("""\
An entry in arpTable.
""")
_ArpIndex_Type = Integer32
_ArpIndex_Object = MibTableColumn
arpIndex = _ArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 22, 1, 1, 1),
    _ArpIndex_Type()
)
arpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIndex.setStatus("mandatory")
_ArpIpAddr_Type = IpAddress
_ArpIpAddr_Object = MibTableColumn
arpIpAddr = _ArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 22, 1, 1, 2),
    _ArpIpAddr_Type()
)
arpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIpAddr.setStatus("mandatory")
_ArpMacAddr_Type = MacAddress
_ArpMacAddr_Object = MibTableColumn
arpMacAddr = _ArpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 22, 1, 1, 3),
    _ArpMacAddr_Type()
)
arpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacAddr.setStatus("mandatory")
_ArpMacVid_Type = Integer32
_ArpMacVid_Object = MibTableColumn
arpMacVid = _ArpMacVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 22, 1, 1, 4),
    _ArpMacVid_Type()
)
arpMacVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacVid.setStatus("mandatory")


class _ArpType_Type(Integer32):
    """Custom type arpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_ArpType_Type.__name__ = "Integer32"
_ArpType_Object = MibTableColumn
arpType = _ArpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 22, 1, 1, 5),
    _ArpType_Type()
)
arpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpType.setStatus("mandatory")
if mibBuilder.loadTexts:
    arpType.setDescription("""\
1-static, 2-dynamic
""")
_PortOpModeSetup_ObjectIdentity = ObjectIdentity
portOpModeSetup = _PortOpModeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 23)
)
_PortOpModePortTable_Object = MibTable
portOpModePortTable = _PortOpModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 23, 1)
)
if mibBuilder.loadTexts:
    portOpModePortTable.setStatus("mandatory")
_PortOpModePortEntry_Object = MibTableRow
portOpModePortEntry = _PortOpModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 23, 1, 1)
)
portOpModePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portOpModePortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    portOpModePortEntry.setDescription("""\
An entry in portOpModePortTable.
""")


class _PortOpModePortSpeedDuplex_Type(Integer32):
    """Custom type portOpModePortSpeedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("speed-10-full", 2),
          ("speed-10-half", 1),
          ("speed-100-full", 4),
          ("speed-100-half", 3),
          ("speed-1000-full", 5))
    )


_PortOpModePortSpeedDuplex_Type.__name__ = "Integer32"
_PortOpModePortSpeedDuplex_Object = MibTableColumn
portOpModePortSpeedDuplex = _PortOpModePortSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 23, 1, 1, 1),
    _PortOpModePortSpeedDuplex_Type()
)
portOpModePortSpeedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortSpeedDuplex.setStatus("mandatory")


class _PortOpModePortFlowCntl_Type(Integer32):
    """Custom type portOpModePortFlowCntl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PortOpModePortFlowCntl_Type.__name__ = "Integer32"
_PortOpModePortFlowCntl_Object = MibTableColumn
portOpModePortFlowCntl = _PortOpModePortFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 23, 1, 1, 2),
    _PortOpModePortFlowCntl_Type()
)
portOpModePortFlowCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortFlowCntl.setStatus("mandatory")


class _PortOpModePortName_Type(OctetString):
    """Custom type portOpModePortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortOpModePortName_Type.__name__ = "OctetString"
_PortOpModePortName_Object = MibTableColumn
portOpModePortName = _PortOpModePortName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 23, 1, 1, 3),
    _PortOpModePortName_Type()
)
portOpModePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortName.setStatus("mandatory")


class _PortOpModePortModuleType_Type(Integer32):
    """Custom type portOpModePortModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast-ethernet-10-100", 0),
          ("fiber-1000", 2),
          ("gigabit-ethernet-100-1000", 1))
    )


_PortOpModePortModuleType_Type.__name__ = "Integer32"
_PortOpModePortModuleType_Object = MibTableColumn
portOpModePortModuleType = _PortOpModePortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 23, 1, 1, 4),
    _PortOpModePortModuleType_Type()
)
portOpModePortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortModuleType.setStatus("mandatory")


class _PortOpModePortLinkUpType_Type(Integer32):
    """Custom type portOpModePortLinkUpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("down", 0),
          ("fiber", 2))
    )


_PortOpModePortLinkUpType_Type.__name__ = "Integer32"
_PortOpModePortLinkUpType_Object = MibTableColumn
portOpModePortLinkUpType = _PortOpModePortLinkUpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 23, 1, 1, 5),
    _PortOpModePortLinkUpType_Type()
)
portOpModePortLinkUpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLinkUpType.setStatus("mandatory")
_PortOpModePortIntrusionLock_Type = EnabledStatus
_PortOpModePortIntrusionLock_Object = MibTableColumn
portOpModePortIntrusionLock = _PortOpModePortIntrusionLock_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 23, 1, 1, 6),
    _PortOpModePortIntrusionLock_Type()
)
portOpModePortIntrusionLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortIntrusionLock.setStatus("mandatory")


class _PortOpModePortLBTestStatus_Type(Integer32):
    """Custom type portOpModePortLBTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("none", 0),
          ("success", 2),
          ("underTesting", 1))
    )


_PortOpModePortLBTestStatus_Type.__name__ = "Integer32"
_PortOpModePortLBTestStatus_Object = MibTableColumn
portOpModePortLBTestStatus = _PortOpModePortLBTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 23, 1, 1, 7),
    _PortOpModePortLBTestStatus_Type()
)
portOpModePortLBTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLBTestStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    portOpModePortLBTestStatus.setDescription("""\
This entry display latest loopback test status of port while performing
loopback test.
""")
_PortBasedVlanSetup_ObjectIdentity = ObjectIdentity
portBasedVlanSetup = _PortBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 24)
)
_PortBasedVlanPortListTable_Object = MibTable
portBasedVlanPortListTable = _PortBasedVlanPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 24, 1)
)
if mibBuilder.loadTexts:
    portBasedVlanPortListTable.setStatus("mandatory")
_PortBasedVlanPortListEntry_Object = MibTableRow
portBasedVlanPortListEntry = _PortBasedVlanPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 24, 1, 1)
)
portBasedVlanPortListEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portBasedVlanPortListEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    portBasedVlanPortListEntry.setDescription("""\
An entry in portBasedVlanPortListTable.
""")
_PortBasedVlanPortListMembers_Type = PortList
_PortBasedVlanPortListMembers_Object = MibTableColumn
portBasedVlanPortListMembers = _PortBasedVlanPortListMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 24, 1, 1, 1),
    _PortBasedVlanPortListMembers_Type()
)
portBasedVlanPortListMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBasedVlanPortListMembers.setStatus("mandatory")
_MulticastPortSetup_ObjectIdentity = ObjectIdentity
multicastPortSetup = _MulticastPortSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 25)
)
_MulticastPortTable_Object = MibTable
multicastPortTable = _MulticastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 25, 1)
)
if mibBuilder.loadTexts:
    multicastPortTable.setStatus("mandatory")
_MulticastPortEntry_Object = MibTableRow
multicastPortEntry = _MulticastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 25, 1, 1)
)
multicastPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    multicastPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    multicastPortEntry.setDescription("""\
An entry in multicastPortTable.
""")
_MulticastPortImmediateLeave_Type = EnabledStatus
_MulticastPortImmediateLeave_Object = MibTableColumn
multicastPortImmediateLeave = _MulticastPortImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 25, 1, 1, 1),
    _MulticastPortImmediateLeave_Type()
)
multicastPortImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortImmediateLeave.setStatus("mandatory")
_MulticastPortMaxGroupLimited_Type = EnabledStatus
_MulticastPortMaxGroupLimited_Object = MibTableColumn
multicastPortMaxGroupLimited = _MulticastPortMaxGroupLimited_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 25, 1, 1, 2),
    _MulticastPortMaxGroupLimited_Type()
)
multicastPortMaxGroupLimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortMaxGroupLimited.setStatus("mandatory")
_MulticastPortMaxOfGroup_Type = Integer32
_MulticastPortMaxOfGroup_Object = MibTableColumn
multicastPortMaxOfGroup = _MulticastPortMaxOfGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 25, 1, 1, 3),
    _MulticastPortMaxOfGroup_Type()
)
multicastPortMaxOfGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortMaxOfGroup.setStatus("mandatory")
if mibBuilder.loadTexts:
    multicastPortMaxOfGroup.setDescription("""\
0..255
""")
_MulticastPortIgmpFilteringProfile_Type = DisplayString
_MulticastPortIgmpFilteringProfile_Object = MibTableColumn
multicastPortIgmpFilteringProfile = _MulticastPortIgmpFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 25, 1, 1, 4),
    _MulticastPortIgmpFilteringProfile_Type()
)
multicastPortIgmpFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortIgmpFilteringProfile.setStatus("mandatory")
_MulticastStatus_ObjectIdentity = ObjectIdentity
multicastStatus = _MulticastStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 26)
)
_MulticastStatusTable_Object = MibTable
multicastStatusTable = _MulticastStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 26, 1)
)
if mibBuilder.loadTexts:
    multicastStatusTable.setStatus("mandatory")
_MulticastStatusEntry_Object = MibTableRow
multicastStatusEntry = _MulticastStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 26, 1, 1)
)
multicastStatusEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "multicastStatusVlanID"),
    (0, "ZYXEL-GS4012F-MIB", "multicastStatusPort"),
    (0, "ZYXEL-GS4012F-MIB", "multicastStatusGroup"),
)
if mibBuilder.loadTexts:
    multicastStatusEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    multicastStatusEntry.setDescription("""\
An entry in multicastStatusTable.
""")
_MulticastStatusIndex_Type = Integer32
_MulticastStatusIndex_Object = MibTableColumn
multicastStatusIndex = _MulticastStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 26, 1, 1, 1),
    _MulticastStatusIndex_Type()
)
multicastStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusIndex.setStatus("mandatory")
_MulticastStatusVlanID_Type = Integer32
_MulticastStatusVlanID_Object = MibTableColumn
multicastStatusVlanID = _MulticastStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 26, 1, 1, 2),
    _MulticastStatusVlanID_Type()
)
multicastStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusVlanID.setStatus("mandatory")
_MulticastStatusPort_Type = Integer32
_MulticastStatusPort_Object = MibTableColumn
multicastStatusPort = _MulticastStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 26, 1, 1, 3),
    _MulticastStatusPort_Type()
)
multicastStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusPort.setStatus("mandatory")
_MulticastStatusGroup_Type = IpAddress
_MulticastStatusGroup_Object = MibTableColumn
multicastStatusGroup = _MulticastStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 26, 1, 1, 4),
    _MulticastStatusGroup_Type()
)
multicastStatusGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusGroup.setStatus("mandatory")
_IgmpFilteringProfileSetup_ObjectIdentity = ObjectIdentity
igmpFilteringProfileSetup = _IgmpFilteringProfileSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 27)
)
_IgmpFilteringMaxNumberOfProfile_Type = Integer32
_IgmpFilteringMaxNumberOfProfile_Object = MibScalar
igmpFilteringMaxNumberOfProfile = _IgmpFilteringMaxNumberOfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 27, 1),
    _IgmpFilteringMaxNumberOfProfile_Type()
)
igmpFilteringMaxNumberOfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringMaxNumberOfProfile.setStatus("mandatory")
_IgmpFilteringProfileTable_Object = MibTable
igmpFilteringProfileTable = _IgmpFilteringProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 27, 2)
)
if mibBuilder.loadTexts:
    igmpFilteringProfileTable.setStatus("mandatory")
_IgmpFilteringProfileEntry_Object = MibTableRow
igmpFilteringProfileEntry = _IgmpFilteringProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 27, 2, 1)
)
igmpFilteringProfileEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "igmpFilteringProfileName"),
    (0, "ZYXEL-GS4012F-MIB", "igmpFilteringProfileStartAddress"),
    (0, "ZYXEL-GS4012F-MIB", "igmpFilteringProfileEndAddress"),
)
if mibBuilder.loadTexts:
    igmpFilteringProfileEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    igmpFilteringProfileEntry.setDescription("""\
An entry in igmpFilteringProfileTable.
""")
_IgmpFilteringProfileName_Type = DisplayString
_IgmpFilteringProfileName_Object = MibTableColumn
igmpFilteringProfileName = _IgmpFilteringProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 27, 2, 1, 1),
    _IgmpFilteringProfileName_Type()
)
igmpFilteringProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileName.setStatus("mandatory")
_IgmpFilteringProfileStartAddress_Type = IpAddress
_IgmpFilteringProfileStartAddress_Object = MibTableColumn
igmpFilteringProfileStartAddress = _IgmpFilteringProfileStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 27, 2, 1, 2),
    _IgmpFilteringProfileStartAddress_Type()
)
igmpFilteringProfileStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileStartAddress.setStatus("mandatory")
_IgmpFilteringProfileEndAddress_Type = IpAddress
_IgmpFilteringProfileEndAddress_Object = MibTableColumn
igmpFilteringProfileEndAddress = _IgmpFilteringProfileEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 27, 2, 1, 3),
    _IgmpFilteringProfileEndAddress_Type()
)
igmpFilteringProfileEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileEndAddress.setStatus("mandatory")
_IgmpFilteringProfileRowStatus_Type = RowStatus
_IgmpFilteringProfileRowStatus_Object = MibTableColumn
igmpFilteringProfileRowStatus = _IgmpFilteringProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 27, 2, 1, 4),
    _IgmpFilteringProfileRowStatus_Type()
)
igmpFilteringProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilteringProfileRowStatus.setStatus("mandatory")
_MvrSetup_ObjectIdentity = ObjectIdentity
mvrSetup = _MvrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28)
)
_MaxNumberOfMVR_Type = Integer32
_MaxNumberOfMVR_Object = MibScalar
maxNumberOfMVR = _MaxNumberOfMVR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 1),
    _MaxNumberOfMVR_Type()
)
maxNumberOfMVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMVR.setStatus("mandatory")
_MvrTable_Object = MibTable
mvrTable = _MvrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 2)
)
if mibBuilder.loadTexts:
    mvrTable.setStatus("mandatory")
_MvrEntry_Object = MibTableRow
mvrEntry = _MvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 2, 1)
)
mvrEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "mvrVlanID"),
)
if mibBuilder.loadTexts:
    mvrEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    mvrEntry.setDescription("""\
An entry in mvrTable.
""")
_MvrVlanID_Type = Integer32
_MvrVlanID_Object = MibTableColumn
mvrVlanID = _MvrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 2, 1, 1),
    _MvrVlanID_Type()
)
mvrVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanID.setStatus("mandatory")
if mibBuilder.loadTexts:
    mvrVlanID.setDescription("""\
1..4094
""")
_MvrName_Type = DisplayString
_MvrName_Object = MibTableColumn
mvrName = _MvrName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 2, 1, 2),
    _MvrName_Type()
)
mvrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrName.setStatus("mandatory")


class _MvrMode_Type(Integer32):
    """Custom type mvrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 1),
          ("dynamic", 0))
    )


_MvrMode_Type.__name__ = "Integer32"
_MvrMode_Object = MibTableColumn
mvrMode = _MvrMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 2, 1, 3),
    _MvrMode_Type()
)
mvrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMode.setStatus("mandatory")
_MvrRowStatus_Type = RowStatus
_MvrRowStatus_Object = MibTableColumn
mvrRowStatus = _MvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 2, 1, 4),
    _MvrRowStatus_Type()
)
mvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrRowStatus.setStatus("mandatory")
_MvrPortTable_Object = MibTable
mvrPortTable = _MvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 3)
)
if mibBuilder.loadTexts:
    mvrPortTable.setStatus("mandatory")
_MvrPortEntry_Object = MibTableRow
mvrPortEntry = _MvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 3, 1)
)
mvrPortEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "mvrVlanID"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mvrPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    mvrPortEntry.setDescription("""\
An entry in mvrPortTable.
""")


class _MvrPortRole_Type(Integer32):
    """Custom type mvrPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("receiver-port", 3),
          ("source-port", 2))
    )


_MvrPortRole_Type.__name__ = "Integer32"
_MvrPortRole_Object = MibTableColumn
mvrPortRole = _MvrPortRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 3, 1, 1),
    _MvrPortRole_Type()
)
mvrPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortRole.setStatus("mandatory")
_MvrPortTagging_Type = EnabledStatus
_MvrPortTagging_Object = MibTableColumn
mvrPortTagging = _MvrPortTagging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 3, 1, 2),
    _MvrPortTagging_Type()
)
mvrPortTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortTagging.setStatus("mandatory")
_MaxNumberOfMvrGroup_Type = Integer32
_MaxNumberOfMvrGroup_Object = MibScalar
maxNumberOfMvrGroup = _MaxNumberOfMvrGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 4),
    _MaxNumberOfMvrGroup_Type()
)
maxNumberOfMvrGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMvrGroup.setStatus("mandatory")
_MvrGroupTable_Object = MibTable
mvrGroupTable = _MvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 5)
)
if mibBuilder.loadTexts:
    mvrGroupTable.setStatus("mandatory")
_MvrGroupEntry_Object = MibTableRow
mvrGroupEntry = _MvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 5, 1)
)
mvrGroupEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "mvrVlanID"),
    (0, "ZYXEL-GS4012F-MIB", "mvrGroupName"),
)
if mibBuilder.loadTexts:
    mvrGroupEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    mvrGroupEntry.setDescription("""\
An entry in mvrGroupTable.
""")
_MvrGroupName_Type = DisplayString
_MvrGroupName_Object = MibTableColumn
mvrGroupName = _MvrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 5, 1, 1),
    _MvrGroupName_Type()
)
mvrGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroupName.setStatus("mandatory")
_MvrGroupStartAddress_Type = IpAddress
_MvrGroupStartAddress_Object = MibTableColumn
mvrGroupStartAddress = _MvrGroupStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 5, 1, 2),
    _MvrGroupStartAddress_Type()
)
mvrGroupStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStartAddress.setStatus("mandatory")
_MvrGroupEndAddress_Type = IpAddress
_MvrGroupEndAddress_Object = MibTableColumn
mvrGroupEndAddress = _MvrGroupEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 5, 1, 3),
    _MvrGroupEndAddress_Type()
)
mvrGroupEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupEndAddress.setStatus("mandatory")
_MvrGroupRowStatus_Type = RowStatus
_MvrGroupRowStatus_Object = MibTableColumn
mvrGroupRowStatus = _MvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 28, 5, 1, 4),
    _MvrGroupRowStatus_Type()
)
mvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrGroupRowStatus.setStatus("mandatory")
_Layer3Setup_ObjectIdentity = ObjectIdentity
layer3Setup = _Layer3Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 29)
)
_RouterRipState_Type = EnabledStatus
_RouterRipState_Object = MibScalar
routerRipState = _RouterRipState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 29, 1),
    _RouterRipState_Type()
)
routerRipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerRipState.setStatus("mandatory")
_RouterIgmpState_Type = EnabledStatus
_RouterIgmpState_Object = MibScalar
routerIgmpState = _RouterIgmpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 29, 2),
    _RouterIgmpState_Type()
)
routerIgmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerIgmpState.setStatus("mandatory")
_RouterDvmrpState_Type = EnabledStatus
_RouterDvmrpState_Object = MibScalar
routerDvmrpState = _RouterDvmrpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 29, 3),
    _RouterDvmrpState_Type()
)
routerDvmrpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerDvmrpState.setStatus("mandatory")
_RouterDvmrpThreshold_Type = Integer32
_RouterDvmrpThreshold_Object = MibScalar
routerDvmrpThreshold = _RouterDvmrpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 29, 4),
    _RouterDvmrpThreshold_Type()
)
routerDvmrpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerDvmrpThreshold.setStatus("mandatory")
_RouterIpmcPortSetup_ObjectIdentity = ObjectIdentity
routerIpmcPortSetup = _RouterIpmcPortSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 30)
)
_RouterIpmcPortTable_Object = MibTable
routerIpmcPortTable = _RouterIpmcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 30, 1)
)
if mibBuilder.loadTexts:
    routerIpmcPortTable.setStatus("mandatory")
_RouterIpmcPortEntry_Object = MibTableRow
routerIpmcPortEntry = _RouterIpmcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 30, 1, 1)
)
routerIpmcPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    routerIpmcPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    routerIpmcPortEntry.setDescription("""\
An entry in routerIpmcPortTable.
""")
_RouterIpmcPortEgressUntagVlan_Type = Integer32
_RouterIpmcPortEgressUntagVlan_Object = MibTableColumn
routerIpmcPortEgressUntagVlan = _RouterIpmcPortEgressUntagVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 30, 1, 1, 1),
    _RouterIpmcPortEgressUntagVlan_Type()
)
routerIpmcPortEgressUntagVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerIpmcPortEgressUntagVlan.setStatus("mandatory")
_RouterVrrpSetup_ObjectIdentity = ObjectIdentity
routerVrrpSetup = _RouterVrrpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31)
)
_RouterVrrpMaxNumber_Type = Integer32
_RouterVrrpMaxNumber_Object = MibScalar
routerVrrpMaxNumber = _RouterVrrpMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 1),
    _RouterVrrpMaxNumber_Type()
)
routerVrrpMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerVrrpMaxNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    routerVrrpMaxNumber.setDescription("""\
Always set it as 14.
""")
_RouterVrrpTable_Object = MibTable
routerVrrpTable = _RouterVrrpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2)
)
if mibBuilder.loadTexts:
    routerVrrpTable.setStatus("mandatory")
_RouterVrrpEntry_Object = MibTableRow
routerVrrpEntry = _RouterVrrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2, 1)
)
routerVrrpEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "routerDomainIpAddress"),
    (0, "ZYXEL-GS4012F-MIB", "routerDomainIpMaskBits"),
    (0, "ZYXEL-GS4012F-MIB", "routerVrrpVirtualID"),
    (0, "ZYXEL-GS4012F-MIB", "routerVrrpUplinkGateway"),
)
if mibBuilder.loadTexts:
    routerVrrpEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    routerVrrpEntry.setDescription("""\
An entry in routerVrrpTable.
""")
_RouterVrrpVirtualID_Type = Integer32
_RouterVrrpVirtualID_Object = MibTableColumn
routerVrrpVirtualID = _RouterVrrpVirtualID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2, 1, 1),
    _RouterVrrpVirtualID_Type()
)
routerVrrpVirtualID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerVrrpVirtualID.setStatus("mandatory")
_RouterVrrpUplinkGateway_Type = IpAddress
_RouterVrrpUplinkGateway_Object = MibTableColumn
routerVrrpUplinkGateway = _RouterVrrpUplinkGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2, 1, 2),
    _RouterVrrpUplinkGateway_Type()
)
routerVrrpUplinkGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerVrrpUplinkGateway.setStatus("mandatory")
_RouterVrrpPreempt_Type = EnabledStatus
_RouterVrrpPreempt_Object = MibTableColumn
routerVrrpPreempt = _RouterVrrpPreempt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2, 1, 3),
    _RouterVrrpPreempt_Type()
)
routerVrrpPreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerVrrpPreempt.setStatus("mandatory")
_RouterVrrpInterval_Type = Integer32
_RouterVrrpInterval_Object = MibTableColumn
routerVrrpInterval = _RouterVrrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2, 1, 4),
    _RouterVrrpInterval_Type()
)
routerVrrpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerVrrpInterval.setStatus("mandatory")
if mibBuilder.loadTexts:
    routerVrrpInterval.setDescription("""\
1-255
""")
_RouterVrrpPriority_Type = Integer32
_RouterVrrpPriority_Object = MibTableColumn
routerVrrpPriority = _RouterVrrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2, 1, 5),
    _RouterVrrpPriority_Type()
)
routerVrrpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerVrrpPriority.setStatus("mandatory")
if mibBuilder.loadTexts:
    routerVrrpPriority.setDescription("""\
1-254
""")
_RouterVrrpPrimaryVirtualIP_Type = IpAddress
_RouterVrrpPrimaryVirtualIP_Object = MibTableColumn
routerVrrpPrimaryVirtualIP = _RouterVrrpPrimaryVirtualIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2, 1, 6),
    _RouterVrrpPrimaryVirtualIP_Type()
)
routerVrrpPrimaryVirtualIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerVrrpPrimaryVirtualIP.setStatus("mandatory")
_RouterVrrpName_Type = DisplayString
_RouterVrrpName_Object = MibTableColumn
routerVrrpName = _RouterVrrpName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2, 1, 7),
    _RouterVrrpName_Type()
)
routerVrrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerVrrpName.setStatus("mandatory")
_RouterVrrpSecondaryVirtualIP_Type = IpAddress
_RouterVrrpSecondaryVirtualIP_Object = MibTableColumn
routerVrrpSecondaryVirtualIP = _RouterVrrpSecondaryVirtualIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2, 1, 8),
    _RouterVrrpSecondaryVirtualIP_Type()
)
routerVrrpSecondaryVirtualIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerVrrpSecondaryVirtualIP.setStatus("mandatory")
_RpVrrpRowStatus_Type = RowStatus
_RpVrrpRowStatus_Object = MibTableColumn
rpVrrpRowStatus = _RpVrrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 2, 1, 9),
    _RpVrrpRowStatus_Type()
)
rpVrrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpVrrpRowStatus.setStatus("mandatory")
_RouterVrrpDomainTable_Object = MibTable
routerVrrpDomainTable = _RouterVrrpDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 3)
)
if mibBuilder.loadTexts:
    routerVrrpDomainTable.setStatus("mandatory")
_RouterVrrpDomainEntry_Object = MibTableRow
routerVrrpDomainEntry = _RouterVrrpDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 3, 1)
)
routerVrrpDomainEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "routerDomainIpAddress"),
    (0, "ZYXEL-GS4012F-MIB", "routerDomainIpMaskBits"),
)
if mibBuilder.loadTexts:
    routerVrrpDomainEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    routerVrrpDomainEntry.setDescription("""\
An entry in routerVrrpTable.
""")


class _RouterVrrpAuthType_Type(Integer32):
    """Custom type routerVrrpAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("simple", 1))
    )


_RouterVrrpAuthType_Type.__name__ = "Integer32"
_RouterVrrpAuthType_Object = MibTableColumn
routerVrrpAuthType = _RouterVrrpAuthType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 3, 1, 1),
    _RouterVrrpAuthType_Type()
)
routerVrrpAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerVrrpAuthType.setStatus("mandatory")
_RouterVrrpAuthKey_Type = DisplayString
_RouterVrrpAuthKey_Object = MibTableColumn
routerVrrpAuthKey = _RouterVrrpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 31, 3, 1, 2),
    _RouterVrrpAuthKey_Type()
)
routerVrrpAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerVrrpAuthKey.setStatus("mandatory")
_RouterVrrpStatus_ObjectIdentity = ObjectIdentity
routerVrrpStatus = _RouterVrrpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 32)
)
_RouterVrrpStatusTable_Object = MibTable
routerVrrpStatusTable = _RouterVrrpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 32, 1)
)
if mibBuilder.loadTexts:
    routerVrrpStatusTable.setStatus("mandatory")
_RouterVrrpStatusEntry_Object = MibTableRow
routerVrrpStatusEntry = _RouterVrrpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 32, 1, 1)
)
routerVrrpStatusEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "routerVrrpStatusIpAddress"),
    (0, "ZYXEL-GS4012F-MIB", "routerVrrpStatusIpMaskBits"),
    (0, "ZYXEL-GS4012F-MIB", "routerVrrpStatusVirtualID"),
)
if mibBuilder.loadTexts:
    routerVrrpStatusEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    routerVrrpStatusEntry.setDescription("""\

""")
_RouterVrrpStatusIpAddress_Type = IpAddress
_RouterVrrpStatusIpAddress_Object = MibTableColumn
routerVrrpStatusIpAddress = _RouterVrrpStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 32, 1, 1, 1),
    _RouterVrrpStatusIpAddress_Type()
)
routerVrrpStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerVrrpStatusIpAddress.setStatus("mandatory")
_RouterVrrpStatusIpMaskBits_Type = Integer32
_RouterVrrpStatusIpMaskBits_Object = MibTableColumn
routerVrrpStatusIpMaskBits = _RouterVrrpStatusIpMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 32, 1, 1, 2),
    _RouterVrrpStatusIpMaskBits_Type()
)
routerVrrpStatusIpMaskBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerVrrpStatusIpMaskBits.setStatus("mandatory")
_RouterVrrpStatusVirtualID_Type = Integer32
_RouterVrrpStatusVirtualID_Object = MibTableColumn
routerVrrpStatusVirtualID = _RouterVrrpStatusVirtualID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 32, 1, 1, 3),
    _RouterVrrpStatusVirtualID_Type()
)
routerVrrpStatusVirtualID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerVrrpStatusVirtualID.setStatus("mandatory")
_RouterVrrpStatusVRStatus_Type = DisplayString
_RouterVrrpStatusVRStatus_Object = MibTableColumn
routerVrrpStatusVRStatus = _RouterVrrpStatusVRStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 32, 1, 1, 4),
    _RouterVrrpStatusVRStatus_Type()
)
routerVrrpStatusVRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerVrrpStatusVRStatus.setStatus("mandatory")
_RouterVrrpStatusUpLinkStatus_Type = DisplayString
_RouterVrrpStatusUpLinkStatus_Object = MibTableColumn
routerVrrpStatusUpLinkStatus = _RouterVrrpStatusUpLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 32, 1, 1, 5),
    _RouterVrrpStatusUpLinkStatus_Type()
)
routerVrrpStatusUpLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerVrrpStatusUpLinkStatus.setStatus("mandatory")
_RouterDomainSetup_ObjectIdentity = ObjectIdentity
routerDomainSetup = _RouterDomainSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33)
)
_RouterDomainTable_Object = MibTable
routerDomainTable = _RouterDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 1)
)
if mibBuilder.loadTexts:
    routerDomainTable.setStatus("mandatory")
_RouterDomainEntry_Object = MibTableRow
routerDomainEntry = _RouterDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 1, 1)
)
routerDomainEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "routerDomainIpAddress"),
    (0, "ZYXEL-GS4012F-MIB", "routerDomainIpMaskBits"),
)
if mibBuilder.loadTexts:
    routerDomainEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    routerDomainEntry.setDescription("""\
An entry in routerDomainTable.
""")
_RouterDomainIpAddress_Type = IpAddress
_RouterDomainIpAddress_Object = MibTableColumn
routerDomainIpAddress = _RouterDomainIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 1, 1, 1),
    _RouterDomainIpAddress_Type()
)
routerDomainIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerDomainIpAddress.setStatus("mandatory")
_RouterDomainIpMaskBits_Type = Integer32
_RouterDomainIpMaskBits_Object = MibTableColumn
routerDomainIpMaskBits = _RouterDomainIpMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 1, 1, 2),
    _RouterDomainIpMaskBits_Type()
)
routerDomainIpMaskBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerDomainIpMaskBits.setStatus("mandatory")
_RouterDomainVid_Type = Integer32
_RouterDomainVid_Object = MibTableColumn
routerDomainVid = _RouterDomainVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 1, 1, 3),
    _RouterDomainVid_Type()
)
routerDomainVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerDomainVid.setStatus("mandatory")
_RouterDomainIpTable_Object = MibTable
routerDomainIpTable = _RouterDomainIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 2)
)
if mibBuilder.loadTexts:
    routerDomainIpTable.setStatus("mandatory")
_RouterDomainIpEntry_Object = MibTableRow
routerDomainIpEntry = _RouterDomainIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 2, 1)
)
routerDomainIpEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "routerDomainIpAddress"),
    (0, "ZYXEL-GS4012F-MIB", "routerDomainIpMaskBits"),
)
if mibBuilder.loadTexts:
    routerDomainIpEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    routerDomainIpEntry.setDescription("""\
An entry in routerDomainIpTable.
""")


class _RouterDomainIpRipDirection_Type(Integer32):
    """Custom type routerDomainIpRipDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("incoming", 2),
          ("none", 0),
          ("outgoing", 1))
    )


_RouterDomainIpRipDirection_Type.__name__ = "Integer32"
_RouterDomainIpRipDirection_Object = MibTableColumn
routerDomainIpRipDirection = _RouterDomainIpRipDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 2, 1, 1),
    _RouterDomainIpRipDirection_Type()
)
routerDomainIpRipDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerDomainIpRipDirection.setStatus("mandatory")


class _RouterDomainIpRipVersion_Type(Integer32):
    """Custom type routerDomainIpRipVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2b", 1),
          ("v2m", 2))
    )


_RouterDomainIpRipVersion_Type.__name__ = "Integer32"
_RouterDomainIpRipVersion_Object = MibTableColumn
routerDomainIpRipVersion = _RouterDomainIpRipVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 2, 1, 2),
    _RouterDomainIpRipVersion_Type()
)
routerDomainIpRipVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerDomainIpRipVersion.setStatus("mandatory")


class _RouterDomainIpIgmpVersion_Type(Integer32):
    """Custom type routerDomainIpIgmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmp-v1", 1),
          ("igmp-v2", 2),
          ("none", 0))
    )


_RouterDomainIpIgmpVersion_Type.__name__ = "Integer32"
_RouterDomainIpIgmpVersion_Object = MibTableColumn
routerDomainIpIgmpVersion = _RouterDomainIpIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 2, 1, 3),
    _RouterDomainIpIgmpVersion_Type()
)
routerDomainIpIgmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerDomainIpIgmpVersion.setStatus("mandatory")
_RouterDomainIpDvmrp_Type = EnabledStatus
_RouterDomainIpDvmrp_Object = MibTableColumn
routerDomainIpDvmrp = _RouterDomainIpDvmrp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 33, 2, 1, 4),
    _RouterDomainIpDvmrp_Type()
)
routerDomainIpDvmrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerDomainIpDvmrp.setStatus("mandatory")
_DiffservSetup_ObjectIdentity = ObjectIdentity
diffservSetup = _DiffservSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 34)
)
_DiffservState_Type = EnabledStatus
_DiffservState_Object = MibScalar
diffservState = _DiffservState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 34, 1),
    _DiffservState_Type()
)
diffservState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservState.setStatus("mandatory")
_DiffservMapTable_Object = MibTable
diffservMapTable = _DiffservMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 34, 2)
)
if mibBuilder.loadTexts:
    diffservMapTable.setStatus("mandatory")
_DiffservMapEntry_Object = MibTableRow
diffservMapEntry = _DiffservMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 34, 2, 1)
)
diffservMapEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "diffservMapDscp"),
)
if mibBuilder.loadTexts:
    diffservMapEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    diffservMapEntry.setDescription("""\
An entry in diffservMapTable.
""")
_DiffservMapDscp_Type = Integer32
_DiffservMapDscp_Object = MibTableColumn
diffservMapDscp = _DiffservMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 34, 2, 1, 1),
    _DiffservMapDscp_Type()
)
diffservMapDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffservMapDscp.setStatus("mandatory")
if mibBuilder.loadTexts:
    diffservMapDscp.setDescription("""\
0-63
""")
_DiffservMapPriority_Type = Integer32
_DiffservMapPriority_Object = MibTableColumn
diffservMapPriority = _DiffservMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 34, 2, 1, 2),
    _DiffservMapPriority_Type()
)
diffservMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservMapPriority.setStatus("mandatory")
if mibBuilder.loadTexts:
    diffservMapPriority.setDescription("""\
0-7
""")
_DiffservPortTable_Object = MibTable
diffservPortTable = _DiffservPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 34, 3)
)
if mibBuilder.loadTexts:
    diffservPortTable.setStatus("mandatory")
_DiffservPortEntry_Object = MibTableRow
diffservPortEntry = _DiffservPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 34, 3, 1)
)
diffservPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    diffservPortEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    diffservPortEntry.setDescription("""\
An entry in diffservPortTable.
""")
_DiffservPortState_Type = EnabledStatus
_DiffservPortState_Object = MibTableColumn
diffservPortState = _DiffservPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 34, 3, 1, 1),
    _DiffservPortState_Type()
)
diffservPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservPortState.setStatus("mandatory")
_ClusterSetup_ObjectIdentity = ObjectIdentity
clusterSetup = _ClusterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35)
)
_ClusterManager_ObjectIdentity = ObjectIdentity
clusterManager = _ClusterManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 1)
)
_ClusterMaxNumOfManager_Type = Integer32
_ClusterMaxNumOfManager_Object = MibScalar
clusterMaxNumOfManager = _ClusterMaxNumOfManager_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 1, 1),
    _ClusterMaxNumOfManager_Type()
)
clusterMaxNumOfManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMaxNumOfManager.setStatus("mandatory")
_ClusterManagerTable_Object = MibTable
clusterManagerTable = _ClusterManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 1, 2)
)
if mibBuilder.loadTexts:
    clusterManagerTable.setStatus("mandatory")
_ClusterManagerEntry_Object = MibTableRow
clusterManagerEntry = _ClusterManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 1, 2, 1)
)
clusterManagerEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "clusterManagerVid"),
)
if mibBuilder.loadTexts:
    clusterManagerEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    clusterManagerEntry.setDescription("""\
An entry in clusterManagerTable.
""")
_ClusterManagerVid_Type = Integer32
_ClusterManagerVid_Object = MibTableColumn
clusterManagerVid = _ClusterManagerVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 1, 2, 1, 1),
    _ClusterManagerVid_Type()
)
clusterManagerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterManagerVid.setStatus("mandatory")
_ClusterManagerName_Type = DisplayString
_ClusterManagerName_Object = MibTableColumn
clusterManagerName = _ClusterManagerName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 1, 2, 1, 2),
    _ClusterManagerName_Type()
)
clusterManagerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterManagerName.setStatus("mandatory")
_ClusterManagerRowStatus_Type = RowStatus
_ClusterManagerRowStatus_Object = MibTableColumn
clusterManagerRowStatus = _ClusterManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 1, 2, 1, 3),
    _ClusterManagerRowStatus_Type()
)
clusterManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusterManagerRowStatus.setStatus("mandatory")
_ClusterMembers_ObjectIdentity = ObjectIdentity
clusterMembers = _ClusterMembers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 2)
)
_ClusterMaxNumOfMember_Type = Integer32
_ClusterMaxNumOfMember_Object = MibScalar
clusterMaxNumOfMember = _ClusterMaxNumOfMember_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 2, 1),
    _ClusterMaxNumOfMember_Type()
)
clusterMaxNumOfMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMaxNumOfMember.setStatus("mandatory")
_ClusterMemberTable_Object = MibTable
clusterMemberTable = _ClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 2, 2)
)
if mibBuilder.loadTexts:
    clusterMemberTable.setStatus("mandatory")
_ClusterMemberEntry_Object = MibTableRow
clusterMemberEntry = _ClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 2, 2, 1)
)
clusterMemberEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "clusterMemberMac"),
    (0, "ZYXEL-GS4012F-MIB", "clusterMemberPassword"),
)
if mibBuilder.loadTexts:
    clusterMemberEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    clusterMemberEntry.setDescription("""\
An entry in clusterMemberTable.
""")
_ClusterMemberMac_Type = DisplayString
_ClusterMemberMac_Object = MibTableColumn
clusterMemberMac = _ClusterMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 2, 2, 1, 1),
    _ClusterMemberMac_Type()
)
clusterMemberMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberMac.setStatus("mandatory")
_ClusterMemberName_Type = DisplayString
_ClusterMemberName_Object = MibTableColumn
clusterMemberName = _ClusterMemberName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 2, 2, 1, 2),
    _ClusterMemberName_Type()
)
clusterMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberName.setStatus("mandatory")
_ClusterMemberModel_Type = DisplayString
_ClusterMemberModel_Object = MibTableColumn
clusterMemberModel = _ClusterMemberModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 2, 2, 1, 3),
    _ClusterMemberModel_Type()
)
clusterMemberModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberModel.setStatus("mandatory")
_ClusterMemberPassword_Type = DisplayString
_ClusterMemberPassword_Object = MibTableColumn
clusterMemberPassword = _ClusterMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 2, 2, 1, 4),
    _ClusterMemberPassword_Type()
)
clusterMemberPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterMemberPassword.setStatus("mandatory")
_ClusterMemberRowStatus_Type = RowStatus
_ClusterMemberRowStatus_Object = MibTableColumn
clusterMemberRowStatus = _ClusterMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 2, 2, 1, 5),
    _ClusterMemberRowStatus_Type()
)
clusterMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusterMemberRowStatus.setStatus("mandatory")
_ClusterCandidates_ObjectIdentity = ObjectIdentity
clusterCandidates = _ClusterCandidates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 3)
)
_ClusterCandidateTable_Object = MibTable
clusterCandidateTable = _ClusterCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 3, 1)
)
if mibBuilder.loadTexts:
    clusterCandidateTable.setStatus("mandatory")
_ClusterCandidateEntry_Object = MibTableRow
clusterCandidateEntry = _ClusterCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 3, 1, 1)
)
clusterCandidateEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "clusterCandidateMac"),
)
if mibBuilder.loadTexts:
    clusterCandidateEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    clusterCandidateEntry.setDescription("""\
An entry in clusterCandidateTable.
""")
_ClusterCandidateMac_Type = DisplayString
_ClusterCandidateMac_Object = MibTableColumn
clusterCandidateMac = _ClusterCandidateMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 3, 1, 1, 1),
    _ClusterCandidateMac_Type()
)
clusterCandidateMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateMac.setStatus("mandatory")
_ClusterCandidateName_Type = DisplayString
_ClusterCandidateName_Object = MibTableColumn
clusterCandidateName = _ClusterCandidateName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 3, 1, 1, 2),
    _ClusterCandidateName_Type()
)
clusterCandidateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateName.setStatus("mandatory")
_ClusterCandidateModel_Type = DisplayString
_ClusterCandidateModel_Object = MibTableColumn
clusterCandidateModel = _ClusterCandidateModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 3, 1, 1, 3),
    _ClusterCandidateModel_Type()
)
clusterCandidateModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateModel.setStatus("mandatory")
_ClusterStatus_ObjectIdentity = ObjectIdentity
clusterStatus = _ClusterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 4)
)


class _ClusterStatusRole_Type(Integer32):
    """Custom type clusterStatusRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manager", 1),
          ("member", 2),
          ("none", 0))
    )


_ClusterStatusRole_Type.__name__ = "Integer32"
_ClusterStatusRole_Object = MibScalar
clusterStatusRole = _ClusterStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 4, 1),
    _ClusterStatusRole_Type()
)
clusterStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusRole.setStatus("mandatory")
_ClusterStatusManager_Type = DisplayString
_ClusterStatusManager_Object = MibScalar
clusterStatusManager = _ClusterStatusManager_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 4, 2),
    _ClusterStatusManager_Type()
)
clusterStatusManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusManager.setStatus("mandatory")
_ClsuterStatusMaxNumOfMember_Type = Integer32
_ClsuterStatusMaxNumOfMember_Object = MibScalar
clsuterStatusMaxNumOfMember = _ClsuterStatusMaxNumOfMember_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 4, 3),
    _ClsuterStatusMaxNumOfMember_Type()
)
clsuterStatusMaxNumOfMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsuterStatusMaxNumOfMember.setStatus("mandatory")
_ClusterStatusMemberTable_Object = MibTable
clusterStatusMemberTable = _ClusterStatusMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 4, 4)
)
if mibBuilder.loadTexts:
    clusterStatusMemberTable.setStatus("mandatory")
_ClusterStatusMemberEntry_Object = MibTableRow
clusterStatusMemberEntry = _ClusterStatusMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 4, 4, 1)
)
clusterStatusMemberEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "clusterStatusMemberMac"),
)
if mibBuilder.loadTexts:
    clusterStatusMemberEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    clusterStatusMemberEntry.setDescription("""\
An entry in clusterStatusMemberTable.
""")
_ClusterStatusMemberMac_Type = DisplayString
_ClusterStatusMemberMac_Object = MibTableColumn
clusterStatusMemberMac = _ClusterStatusMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 4, 4, 1, 1),
    _ClusterStatusMemberMac_Type()
)
clusterStatusMemberMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberMac.setStatus("mandatory")
_ClusterStatusMemberName_Type = DisplayString
_ClusterStatusMemberName_Object = MibTableColumn
clusterStatusMemberName = _ClusterStatusMemberName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 4, 4, 1, 2),
    _ClusterStatusMemberName_Type()
)
clusterStatusMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberName.setStatus("mandatory")
_ClusterStatusMemberModel_Type = DisplayString
_ClusterStatusMemberModel_Object = MibTableColumn
clusterStatusMemberModel = _ClusterStatusMemberModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 4, 4, 1, 3),
    _ClusterStatusMemberModel_Type()
)
clusterStatusMemberModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberModel.setStatus("mandatory")


class _ClusterStatusMemberStatus_Type(Integer32):
    """Custom type clusterStatusMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("offline", 2),
          ("online", 1))
    )


_ClusterStatusMemberStatus_Type.__name__ = "Integer32"
_ClusterStatusMemberStatus_Object = MibTableColumn
clusterStatusMemberStatus = _ClusterStatusMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 35, 4, 4, 1, 4),
    _ClusterStatusMemberStatus_Type()
)
clusterStatusMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberStatus.setStatus("mandatory")
_EventObjects_ObjectIdentity = ObjectIdentity
eventObjects = _EventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
if mibBuilder.loadTexts:
    eventTable.setDescription("""\
A list of currently active fault events. All faults of normal type regardless
of their severity level are recorded in the event table. When a normal type
fault is cleared it is deleted from the event table.
""")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1)
)
eventEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "eventSeqNum"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
if mibBuilder.loadTexts:
    eventEntry.setDescription("""\
An entry containing information about an event in the event table.
""")
_EventSeqNum_Type = Integer32
_EventSeqNum_Object = MibTableColumn
eventSeqNum = _EventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1, 1),
    _EventSeqNum_Type()
)
eventSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeqNum.setStatus("current")
if mibBuilder.loadTexts:
    eventSeqNum.setDescription("""\
This variable represents the sequence number of an event. Sequence number is
incremented monotonically starting from 0 until it reaches its maximum and
wraps around back to 0. Sequence number is incremented when - the state of a
normal type fault is set on (the same sequence number is present in the events
table as well as in the trap that is sent to notify about the fault on event) -
delta event occurs (sequence number present in trap message) - the state of a
normal type fault is set off (sequence number present in trap that is sent to
notify for clearing).
""")
_EventEventId_Type = EventIdNumber
_EventEventId_Object = MibTableColumn
eventEventId = _EventEventId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1, 2),
    _EventEventId_Type()
)
eventEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventEventId.setStatus("current")
if mibBuilder.loadTexts:
    eventEventId.setDescription("""\
This variable represents the event ID which uniquely identifies the event in
the entire system.
""")


class _EventName_Type(DisplayString):
    """Custom type eventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EventName_Type.__name__ = "DisplayString"
_EventName_Object = MibTableColumn
eventName = _EventName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1, 3),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("current")
if mibBuilder.loadTexts:
    eventName.setDescription("""\
This variable represents the name of the event, for example 'Ethernet Link
Down'
""")
_EventInstanceType_Type = InstanceType
_EventInstanceType_Object = MibTableColumn
eventInstanceType = _EventInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1, 4),
    _EventInstanceType_Type()
)
eventInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceType.setStatus("current")
if mibBuilder.loadTexts:
    eventInstanceType.setDescription("""\
This variable represents the type of InstanceId of a particular event in the
event table. In brief the instanceType refers to the type of sub-component
generating this event in the system, for example switch (5). For more details
see the textual conventions section. AFFECTS: eventInstanceId,
eventInstanceName
""")
_EventInstanceId_Type = DisplayString
_EventInstanceId_Object = MibTableColumn
eventInstanceId = _EventInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1, 5),
    _EventInstanceId_Type()
)
eventInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceId.setStatus("current")
if mibBuilder.loadTexts:
    eventInstanceId.setDescription("""\
This variable represents the InstanceId of a particular event in the event
current table. In brief the instanceId refers to the sub-component generating
this event in the system, for example '1' for port 1. For more details see the
textual conventions section. DEPENDS ON: eventInstanceType
""")
_EventInstanceName_Type = DisplayString
_EventInstanceName_Object = MibTableColumn
eventInstanceName = _EventInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1, 6),
    _EventInstanceName_Type()
)
eventInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceName.setStatus("current")
if mibBuilder.loadTexts:
    eventInstanceName.setDescription("""\
This variable is mainly used to store additional information about the sub-
component that is generating an event. For example this field may specify what
cooling fan is faulty. DEPENDS ON: eventInstanceType
""")
_EventSeverity_Type = EventSeverity
_EventSeverity_Object = MibTableColumn
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1, 7),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
if mibBuilder.loadTexts:
    eventSeverity.setDescription("""\
This variable dictates the urgency of action when a event occurs. There are
four severity levels - Critical, Major, Minor, and Informational. Critical
events are those, which require immediate operator intervention to
prevent/reduce system down time. Major events require quick attention and Minor
events possibly require some attention. Informational events indicate the
occurrence of events that may need to be investigated.
""")
_EventSetTime_Type = UtcTimeStamp
_EventSetTime_Object = MibTableColumn
eventSetTime = _EventSetTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1, 8),
    _EventSetTime_Type()
)
eventSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSetTime.setStatus("current")
if mibBuilder.loadTexts:
    eventSetTime.setDescription("""\
This table contains only normal events and this variable represents the time
when the event become active, i.e. the number of seconds since Jan 1, 1970
12:00AM.
""")


class _EventDescription_Type(DisplayString):
    """Custom type eventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventDescription_Type.__name__ = "DisplayString"
_EventDescription_Object = MibTableColumn
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1, 9),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
if mibBuilder.loadTexts:
    eventDescription.setDescription("""\
This variable contains a description of the event and reasons behind the event.
This is a free format alpha-numeric string that is set by the entity generating
this event. This variable may be empty if there is no usefull information to
report. The maximum length of this string is 255 characters.
""")
_EventServAffective_Type = EventServiceAffective
_EventServAffective_Object = MibTableColumn
eventServAffective = _EventServAffective_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 36, 1, 1, 1, 10),
    _EventServAffective_Type()
)
eventServAffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventServAffective.setStatus("current")
if mibBuilder.loadTexts:
    eventServAffective.setDescription("""\
This variable indicates whether the event is service affective or not
""")
_TrapInfoObjects_ObjectIdentity = ObjectIdentity
trapInfoObjects = _TrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 37, 1)
)
_TrapRefSeqNum_Type = Integer32
_TrapRefSeqNum_Object = MibScalar
trapRefSeqNum = _TrapRefSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 37, 1, 1),
    _TrapRefSeqNum_Type()
)
trapRefSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRefSeqNum.setStatus("current")
if mibBuilder.loadTexts:
    trapRefSeqNum.setDescription("""\
Indicates the former sequence number of a cleared event in the event table. Not
intended to read but only used in trap notifications.
""")
_TrapPersistence_Type = EventPersistence
_TrapPersistence_Object = MibScalar
trapPersistence = _TrapPersistence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 37, 1, 2),
    _TrapPersistence_Type()
)
trapPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPersistence.setStatus("current")
if mibBuilder.loadTexts:
    trapPersistence.setDescription("""\
Indicates whether the event is delta (automatically and immediately cleared) or
normal (not automatically cleared). Not intended to read but only used in trap
notifications.
""")
_TrapSenderNodeId_Type = Integer32
_TrapSenderNodeId_Object = MibScalar
trapSenderNodeId = _TrapSenderNodeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 37, 1, 3),
    _TrapSenderNodeId_Type()
)
trapSenderNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSenderNodeId.setStatus("current")
if mibBuilder.loadTexts:
    trapSenderNodeId.setDescription("""\
Represents the node ID of the sending network element. If not supported should
be set to 0. Not intended to read but only used in trap notifications.
""")
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 37, 2)
)
_IpStatus_ObjectIdentity = ObjectIdentity
ipStatus = _IpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 38)
)
_IpStatusTable_Object = MibTable
ipStatusTable = _IpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 38, 1)
)
if mibBuilder.loadTexts:
    ipStatusTable.setStatus("mandatory")
_IpStatusEntry_Object = MibTableRow
ipStatusEntry = _IpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 38, 1, 1)
)
ipStatusEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "ipStatusIPAddress"),
    (0, "ZYXEL-GS4012F-MIB", "ipStatusVid"),
)
if mibBuilder.loadTexts:
    ipStatusEntry.setStatus("mandatory")
_IpStatusIPAddress_Type = IpAddress
_IpStatusIPAddress_Object = MibTableColumn
ipStatusIPAddress = _IpStatusIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 38, 1, 1, 1),
    _IpStatusIPAddress_Type()
)
ipStatusIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStatusIPAddress.setStatus("mandatory")
_IpStatusVid_Type = Integer32
_IpStatusVid_Object = MibTableColumn
ipStatusVid = _IpStatusVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 38, 1, 1, 2),
    _IpStatusVid_Type()
)
ipStatusVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStatusVid.setStatus("mandatory")
_IpStatusPort_Type = DisplayString
_IpStatusPort_Object = MibTableColumn
ipStatusPort = _IpStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 38, 1, 1, 3),
    _IpStatusPort_Type()
)
ipStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStatusPort.setStatus("mandatory")


class _IpStatusType_Type(Integer32):
    """Custom type ipStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_IpStatusType_Type.__name__ = "Integer32"
_IpStatusType_Object = MibTableColumn
ipStatusType = _IpStatusType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 38, 1, 1, 4),
    _IpStatusType_Type()
)
ipStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStatusType.setStatus("mandatory")
_RoutingStatus_ObjectIdentity = ObjectIdentity
routingStatus = _RoutingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 39)
)
_RoutingStatusTable_Object = MibTable
routingStatusTable = _RoutingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 39, 1)
)
if mibBuilder.loadTexts:
    routingStatusTable.setStatus("mandatory")
_RoutingStatusEntry_Object = MibTableRow
routingStatusEntry = _RoutingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 39, 1, 1)
)
routingStatusEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "routingStatusDestAddress"),
)
if mibBuilder.loadTexts:
    routingStatusEntry.setStatus("mandatory")
_RoutingStatusDestAddress_Type = IpAddress
_RoutingStatusDestAddress_Object = MibTableColumn
routingStatusDestAddress = _RoutingStatusDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 39, 1, 1, 1),
    _RoutingStatusDestAddress_Type()
)
routingStatusDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusDestAddress.setStatus("mandatory")
_RoutingStatusDestMaskbits_Type = Integer32
_RoutingStatusDestMaskbits_Object = MibTableColumn
routingStatusDestMaskbits = _RoutingStatusDestMaskbits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 39, 1, 1, 2),
    _RoutingStatusDestMaskbits_Type()
)
routingStatusDestMaskbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusDestMaskbits.setStatus("mandatory")
_RoutingStatusGateway_Type = IpAddress
_RoutingStatusGateway_Object = MibTableColumn
routingStatusGateway = _RoutingStatusGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 39, 1, 1, 3),
    _RoutingStatusGateway_Type()
)
routingStatusGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusGateway.setStatus("mandatory")
_RoutingStatusInterface_Type = IpAddress
_RoutingStatusInterface_Object = MibTableColumn
routingStatusInterface = _RoutingStatusInterface_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 39, 1, 1, 4),
    _RoutingStatusInterface_Type()
)
routingStatusInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusInterface.setStatus("mandatory")
_RoutingStatusMetric_Type = Integer32
_RoutingStatusMetric_Object = MibTableColumn
routingStatusMetric = _RoutingStatusMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 39, 1, 1, 5),
    _RoutingStatusMetric_Type()
)
routingStatusMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusMetric.setStatus("mandatory")


class _RoutingStatusType_Type(Integer32):
    """Custom type routingStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 2),
          ("ospf", 3),
          ("rip", 1),
          ("static", 4))
    )


_RoutingStatusType_Type.__name__ = "Integer32"
_RoutingStatusType_Object = MibTableColumn
routingStatusType = _RoutingStatusType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 39, 1, 1, 6),
    _RoutingStatusType_Type()
)
routingStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusType.setStatus("mandatory")
_OspfExt_ObjectIdentity = ObjectIdentity
ospfExt = _OspfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40)
)
_OspfInterfaceTable_Object = MibTable
ospfInterfaceTable = _OspfInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 1)
)
if mibBuilder.loadTexts:
    ospfInterfaceTable.setStatus("mandatory")
_OspfInterfaceEntry_Object = MibTableRow
ospfInterfaceEntry = _OspfInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 1, 1)
)
ospfInterfaceEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    ospfInterfaceEntry.setStatus("mandatory")
_OspfIfKeyId_Type = Integer32
_OspfIfKeyId_Object = MibTableColumn
ospfIfKeyId = _OspfIfKeyId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 1, 1, 1),
    _OspfIfKeyId_Type()
)
ospfIfKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfKeyId.setStatus("mandatory")
_OspfIfMaskbits_Type = Integer32
_OspfIfMaskbits_Object = MibTableColumn
ospfIfMaskbits = _OspfIfMaskbits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 1, 1, 2),
    _OspfIfMaskbits_Type()
)
ospfIfMaskbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfMaskbits.setStatus("mandatory")
_OspfIfDesignatedRouterID_Type = IpAddress
_OspfIfDesignatedRouterID_Object = MibTableColumn
ospfIfDesignatedRouterID = _OspfIfDesignatedRouterID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 1, 1, 3),
    _OspfIfDesignatedRouterID_Type()
)
ospfIfDesignatedRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfDesignatedRouterID.setStatus("mandatory")
_OspfIfBackupDesignatedRouterID_Type = IpAddress
_OspfIfBackupDesignatedRouterID_Object = MibTableColumn
ospfIfBackupDesignatedRouterID = _OspfIfBackupDesignatedRouterID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 1, 1, 4),
    _OspfIfBackupDesignatedRouterID_Type()
)
ospfIfBackupDesignatedRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfBackupDesignatedRouterID.setStatus("mandatory")
_OspfIfNbrCount_Type = Integer32
_OspfIfNbrCount_Object = MibTableColumn
ospfIfNbrCount = _OspfIfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 1, 1, 5),
    _OspfIfNbrCount_Type()
)
ospfIfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrCount.setStatus("mandatory")
_OspfIfAdjacentNbrCount_Type = Integer32
_OspfIfAdjacentNbrCount_Object = MibTableColumn
ospfIfAdjacentNbrCount = _OspfIfAdjacentNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 1, 1, 6),
    _OspfIfAdjacentNbrCount_Type()
)
ospfIfAdjacentNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfAdjacentNbrCount.setStatus("mandatory")
_OspfIfHelloDueTime_Type = DisplayString
_OspfIfHelloDueTime_Object = MibTableColumn
ospfIfHelloDueTime = _OspfIfHelloDueTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 1, 1, 7),
    _OspfIfHelloDueTime_Type()
)
ospfIfHelloDueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfHelloDueTime.setStatus("mandatory")
_OspfAreaExtTable_Object = MibTable
ospfAreaExtTable = _OspfAreaExtTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 2)
)
if mibBuilder.loadTexts:
    ospfAreaExtTable.setStatus("mandatory")
_OspfAreaExtEntry_Object = MibTableRow
ospfAreaExtEntry = _OspfAreaExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 2, 1)
)
ospfAreaExtEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfAreaId"),
)
if mibBuilder.loadTexts:
    ospfAreaExtEntry.setStatus("mandatory")
_OspfAreaExtName_Type = DisplayString
_OspfAreaExtName_Object = MibTableColumn
ospfAreaExtName = _OspfAreaExtName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 2, 1, 1),
    _OspfAreaExtName_Type()
)
ospfAreaExtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaExtName.setStatus("mandatory")
_OspfRedistributeRouteTable_Object = MibTable
ospfRedistributeRouteTable = _OspfRedistributeRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 3)
)
if mibBuilder.loadTexts:
    ospfRedistributeRouteTable.setStatus("mandatory")
_OspfRedistributeRouteEntry_Object = MibTableRow
ospfRedistributeRouteEntry = _OspfRedistributeRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 3, 1)
)
ospfRedistributeRouteEntry.setIndexNames(
    (0, "ZYXEL-GS4012F-MIB", "ospfRedistributeRouteProtocol"),
)
if mibBuilder.loadTexts:
    ospfRedistributeRouteEntry.setStatus("mandatory")


class _OspfRedistributeRouteProtocol_Type(Integer32):
    """Custom type ospfRedistributeRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rip", 1),
          ("static", 2))
    )


_OspfRedistributeRouteProtocol_Type.__name__ = "Integer32"
_OspfRedistributeRouteProtocol_Object = MibTableColumn
ospfRedistributeRouteProtocol = _OspfRedistributeRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 3, 1, 1),
    _OspfRedistributeRouteProtocol_Type()
)
ospfRedistributeRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRedistributeRouteProtocol.setStatus("mandatory")
_OspfRedistributeRouteState_Type = EnabledStatus
_OspfRedistributeRouteState_Object = MibTableColumn
ospfRedistributeRouteState = _OspfRedistributeRouteState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 3, 1, 2),
    _OspfRedistributeRouteState_Type()
)
ospfRedistributeRouteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistributeRouteState.setStatus("mandatory")
_OspfRedistributeRouteType_Type = Integer32
_OspfRedistributeRouteType_Object = MibTableColumn
ospfRedistributeRouteType = _OspfRedistributeRouteType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 3, 1, 3),
    _OspfRedistributeRouteType_Type()
)
ospfRedistributeRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistributeRouteType.setStatus("mandatory")
_OspfRedistributeRouteMetric_Type = Integer32
_OspfRedistributeRouteMetric_Object = MibTableColumn
ospfRedistributeRouteMetric = _OspfRedistributeRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 3, 1, 4),
    _OspfRedistributeRouteMetric_Type()
)
ospfRedistributeRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistributeRouteMetric.setStatus("mandatory")
_OspfNbrExtTable_Object = MibTable
ospfNbrExtTable = _OspfNbrExtTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 4)
)
if mibBuilder.loadTexts:
    ospfNbrExtTable.setStatus("mandatory")
_OspfNbrExtEntry_Object = MibTableRow
ospfNbrExtEntry = _OspfNbrExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 4, 1)
)
ospfNbrExtEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfNbrIpAddr"),
    (0, "OSPF-MIB", "ospfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    ospfNbrExtEntry.setStatus("mandatory")


class _OspfNbrExtRole_Type(Integer32):
    """Custom type ospfNbrExtRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("dr", 1),
          ("dr-other", 3))
    )


_OspfNbrExtRole_Type.__name__ = "Integer32"
_OspfNbrExtRole_Object = MibTableColumn
ospfNbrExtRole = _OspfNbrExtRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 4, 1, 1),
    _OspfNbrExtRole_Type()
)
ospfNbrExtRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrExtRole.setStatus("mandatory")
_OspfNbrExtDeadtime_Type = DisplayString
_OspfNbrExtDeadtime_Object = MibTableColumn
ospfNbrExtDeadtime = _OspfNbrExtDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 4, 1, 2),
    _OspfNbrExtDeadtime_Type()
)
ospfNbrExtDeadtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrExtDeadtime.setStatus("mandatory")
_OspfNbrExtInterface_Type = IpAddress
_OspfNbrExtInterface_Object = MibTableColumn
ospfNbrExtInterface = _OspfNbrExtInterface_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 4, 1, 3),
    _OspfNbrExtInterface_Type()
)
ospfNbrExtInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrExtInterface.setStatus("mandatory")
_OspfNbrExtRXmtL_Type = Integer32
_OspfNbrExtRXmtL_Object = MibTableColumn
ospfNbrExtRXmtL = _OspfNbrExtRXmtL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 4, 1, 4),
    _OspfNbrExtRXmtL_Type()
)
ospfNbrExtRXmtL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrExtRXmtL.setStatus("mandatory")
_OspfNbrExtRqstL_Type = Integer32
_OspfNbrExtRqstL_Object = MibTableColumn
ospfNbrExtRqstL = _OspfNbrExtRqstL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 4, 1, 5),
    _OspfNbrExtRqstL_Type()
)
ospfNbrExtRqstL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrExtRqstL.setStatus("mandatory")
_OspfNbrExtDBsmL_Type = Integer32
_OspfNbrExtDBsmL_Object = MibTableColumn
ospfNbrExtDBsmL = _OspfNbrExtDBsmL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 4, 1, 6),
    _OspfNbrExtDBsmL_Type()
)
ospfNbrExtDBsmL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrExtDBsmL.setStatus("mandatory")
_OspfLsdbExtTable_Object = MibTable
ospfLsdbExtTable = _OspfLsdbExtTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 5)
)
if mibBuilder.loadTexts:
    ospfLsdbExtTable.setStatus("mandatory")
_OspfLsdbExtEntry_Object = MibTableRow
ospfLsdbExtEntry = _OspfLsdbExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 5, 1)
)
ospfLsdbExtEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfLsdbAreaId"),
    (0, "OSPF-MIB", "ospfLsdbType"),
    (0, "OSPF-MIB", "ospfLsdbLsid"),
    (0, "OSPF-MIB", "ospfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfLsdbExtEntry.setStatus("mandatory")
_OspfLsdbExtLinkCount_Type = Integer32
_OspfLsdbExtLinkCount_Object = MibTableColumn
ospfLsdbExtLinkCount = _OspfLsdbExtLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 5, 1, 1),
    _OspfLsdbExtLinkCount_Type()
)
ospfLsdbExtLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbExtLinkCount.setStatus("mandatory")
_OspfLsdbExtRouteAddress_Type = IpAddress
_OspfLsdbExtRouteAddress_Object = MibTableColumn
ospfLsdbExtRouteAddress = _OspfLsdbExtRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 5, 1, 2),
    _OspfLsdbExtRouteAddress_Type()
)
ospfLsdbExtRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbExtRouteAddress.setStatus("mandatory")
_OspfLsdbExtRouteMaskbits_Type = Integer32
_OspfLsdbExtRouteMaskbits_Object = MibTableColumn
ospfLsdbExtRouteMaskbits = _OspfLsdbExtRouteMaskbits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 5, 1, 3),
    _OspfLsdbExtRouteMaskbits_Type()
)
ospfLsdbExtRouteMaskbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbExtRouteMaskbits.setStatus("mandatory")
_OspfVirtualLinkTable_Object = MibTable
ospfVirtualLinkTable = _OspfVirtualLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 6)
)
if mibBuilder.loadTexts:
    ospfVirtualLinkTable.setStatus("mandatory")
_OspfVirtualLinkEntry_Object = MibTableRow
ospfVirtualLinkEntry = _OspfVirtualLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 6, 1)
)
ospfVirtualLinkEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfVirtIfAreaId"),
    (0, "OSPF-MIB", "ospfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    ospfVirtualLinkEntry.setStatus("mandatory")
_OspfVirtualLinkName_Type = DisplayString
_OspfVirtualLinkName_Object = MibTableColumn
ospfVirtualLinkName = _OspfVirtualLinkName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 6, 1, 1),
    _OspfVirtualLinkName_Type()
)
ospfVirtualLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtualLinkName.setStatus("mandatory")
_OspfVirtualLinkKeyId_Type = Integer32
_OspfVirtualLinkKeyId_Object = MibTableColumn
ospfVirtualLinkKeyId = _OspfVirtualLinkKeyId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 40, 6, 1, 2),
    _OspfVirtualLinkKeyId_Type()
)
ospfVirtualLinkKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtualLinkKeyId.setStatus("mandatory")

# Managed Objects groups


# Notification objects

eventOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 37, 2, 1)
)
eventOnTrap.setObjects(
      *(("ZYXEL-GS4012F-MIB", "eventSeqNum"),
        ("ZYXEL-GS4012F-MIB", "eventEventId"),
        ("ZYXEL-GS4012F-MIB", "eventName"),
        ("ZYXEL-GS4012F-MIB", "eventSetTime"),
        ("ZYXEL-GS4012F-MIB", "eventSeverity"),
        ("ZYXEL-GS4012F-MIB", "eventInstanceType"),
        ("ZYXEL-GS4012F-MIB", "eventInstanceId"),
        ("ZYXEL-GS4012F-MIB", "eventInstanceName"),
        ("ZYXEL-GS4012F-MIB", "eventServAffective"),
        ("ZYXEL-GS4012F-MIB", "eventDescription"),
        ("ZYXEL-GS4012F-MIB", "trapPersistence"),
        ("ZYXEL-GS4012F-MIB", "trapSenderNodeId"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventOnTrap.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    eventOnTrap.setDescription("""\
This trap is used to inform network management system that a delta fault event
(events that are automatically cleared) has occured or a normal fault event
(not automatically cleared) state has been set on. Objects are used as follows:
- eventSeqNum is the sequence number of the event. For normal type of events
must equal to the sequence number of the event in the events table. -
eventEventId specifies what fault event has occured. - eventName specifies the
name of the fault event. - eventSetTime indicates when fault event has occured
(delta events) or when fault has been set on (normal events). - eventSeverity
reports the severity level of the event. - eventInstanceType indicates what
kind of object is faulty. - eventInstanceId specifies what instance is faulty.
- eventInstanceName may contain textual description for the faulty object. -
eventServAffective specifies whether the event is immediately service
affcetive. - eventDescription reports possible additional information about the
event. - trapPersistence tells whether this event is a delta or normal event. -
trapSenderNodeId specifies the node ID of the sending network element if
configuring it is supported for the network element, otherwise 0. - sysObjectID
specifies what kind of equipment reports the fault event. For more information
see the eventTable specification
""")

eventClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20, 37, 2, 2)
)
eventClearedTrap.setObjects(
      *(("ZYXEL-GS4012F-MIB", "eventSeqNum"),
        ("ZYXEL-GS4012F-MIB", "eventEventId"),
        ("ZYXEL-GS4012F-MIB", "eventSetTime"),
        ("ZYXEL-GS4012F-MIB", "eventInstanceType"),
        ("ZYXEL-GS4012F-MIB", "eventInstanceId"),
        ("ZYXEL-GS4012F-MIB", "trapRefSeqNum"),
        ("ZYXEL-GS4012F-MIB", "trapSenderNodeId"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventClearedTrap.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    eventClearedTrap.setDescription("""\
This trap is used to inform network management system that a normal type fault
event has been cleared (state set off). Objects are used as follows: -
eventSeqNum is the sequence number of the this clearing event. Note that the
sequence number of the cleared event is reported in the trapRefSeqNum object. -
eventEventId specifies what event has been cleared. - eventSetTime indicates
when fault event has been cleared. - eventInstanceType indicates what kind of
object has been faulty. - eventInstanceId specifies what instance has been
faulty. - trapRefSeqNum specifies the sequence number of the cleared event
(i.e. the sequence number was assigned for the event in the events table). -
trapSenderNodeId specifies the node ID of the sending network element if
configuring it is supported for the network element, otherwise 0. - sysObjectID
specifies what kind of equipment reports the clearing event. For more
information see the eventTable specification
""")


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-GS4012F-MIB",
    **{"UtcTimeStamp": UtcTimeStamp,
       "EventIdNumber": EventIdNumber,
       "EventSeverity": EventSeverity,
       "EventServiceAffective": EventServiceAffective,
       "InstanceType": InstanceType,
       "EventPersistence": EventPersistence,
       "zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "esSeries": esSeries,
       "gs4012f": gs4012f,
       "sysInfo": sysInfo,
       "sysSwPlatformMajorVers": sysSwPlatformMajorVers,
       "sysSwPlatformMinorVers": sysSwPlatformMinorVers,
       "sysSwModelString": sysSwModelString,
       "sysSwVersionControlNbr": sysSwVersionControlNbr,
       "sysSwDay": sysSwDay,
       "sysSwMonth": sysSwMonth,
       "sysSwYear": sysSwYear,
       "sysHwMajorVers": sysHwMajorVers,
       "sysHwMinorVers": sysHwMinorVers,
       "sysSerialNumber": sysSerialNumber,
       "rateLimitSetup": rateLimitSetup,
       "rateLimitState": rateLimitState,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rateLimitPortState": rateLimitPortState,
       "rateLimitPortCommitRate": rateLimitPortCommitRate,
       "rateLimitPortPeakRate": rateLimitPortPeakRate,
       "rateLimitPortEgrRate": rateLimitPortEgrRate,
       "brLimitSetup": brLimitSetup,
       "brLimitState": brLimitState,
       "brLimitPortTable": brLimitPortTable,
       "brLimitPortEntry": brLimitPortEntry,
       "brLimitPortBrState": brLimitPortBrState,
       "brLimitPortBrRate": brLimitPortBrRate,
       "brLimitPortMcState": brLimitPortMcState,
       "brLimitPortMcRate": brLimitPortMcRate,
       "brLimitPortDlfState": brLimitPortDlfState,
       "brLimitPortDlfRate": brLimitPortDlfRate,
       "portSecuritySetup": portSecuritySetup,
       "portSecurityState": portSecurityState,
       "portSecurityPortTable": portSecurityPortTable,
       "portSecurityPortEntry": portSecurityPortEntry,
       "portSecurityPortState": portSecurityPortState,
       "portSecurityPortLearnState": portSecurityPortLearnState,
       "portSecurityPortCount": portSecurityPortCount,
       "portSecurityMacFreeze": portSecurityMacFreeze,
       "vlanTrunkSetup": vlanTrunkSetup,
       "vlanTrunkPortTable": vlanTrunkPortTable,
       "vlanTrunkPortEntry": vlanTrunkPortEntry,
       "vlanTrunkPortState": vlanTrunkPortState,
       "ctlProtTransSetup": ctlProtTransSetup,
       "ctlProtTransState": ctlProtTransState,
       "ctlProtTransTunnelPortTable": ctlProtTransTunnelPortTable,
       "ctlProtTransTunnelPortEntry": ctlProtTransTunnelPortEntry,
       "ctlProtTransTunnelMode": ctlProtTransTunnelMode,
       "vlanStackSetup": vlanStackSetup,
       "vlanStackState": vlanStackState,
       "vlanStackTpid": vlanStackTpid,
       "vlanStackPortTable": vlanStackPortTable,
       "vlanStackPortEntry": vlanStackPortEntry,
       "vlanStackPortMode": vlanStackPortMode,
       "vlanStackPortVid": vlanStackPortVid,
       "vlanStackPortPrio": vlanStackPortPrio,
       "radius8021xSetup": radius8021xSetup,
       "radiusLoginPrecedence": radiusLoginPrecedence,
       "radiusAnd8021xServer": radiusAnd8021xServer,
       "radiusIpAddr": radiusIpAddr,
       "radiusUdpPort": radiusUdpPort,
       "radiusSharedSecret": radiusSharedSecret,
       "portAuthState": portAuthState,
       "portAuthTable": portAuthTable,
       "portAuthEntry": portAuthEntry,
       "portAuthEntryState": portAuthEntryState,
       "portReAuthEntryState": portReAuthEntryState,
       "portReAuthEntryTimer": portReAuthEntryTimer,
       "hwMonitorInfo": hwMonitorInfo,
       "fanRpmTable": fanRpmTable,
       "fanRpmEntry": fanRpmEntry,
       "fanRpmIndex": fanRpmIndex,
       "fanRpmCurValue": fanRpmCurValue,
       "fanRpmMaxValue": fanRpmMaxValue,
       "fanRpmMinValue": fanRpmMinValue,
       "fanRpmLowThresh": fanRpmLowThresh,
       "fanRpmDescr": fanRpmDescr,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempCurValue": tempCurValue,
       "tempMaxValue": tempMaxValue,
       "tempMinValue": tempMinValue,
       "tempHighThresh": tempHighThresh,
       "tempDescr": tempDescr,
       "voltageTable": voltageTable,
       "voltageEntry": voltageEntry,
       "voltageIndex": voltageIndex,
       "voltageCurValue": voltageCurValue,
       "voltageMaxValue": voltageMaxValue,
       "voltageMinValue": voltageMinValue,
       "voltageNominalValue": voltageNominalValue,
       "voltageLowThresh": voltageLowThresh,
       "voltageDescr": voltageDescr,
       "snmpSetup": snmpSetup,
       "snmpGetCommunity": snmpGetCommunity,
       "snmpSetCommunity": snmpSetCommunity,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpTrapDestTable": snmpTrapDestTable,
       "snmpTrapDestEntry": snmpTrapDestEntry,
       "snmpTrapDestIP": snmpTrapDestIP,
       "snmpTrapDestRowStatus": snmpTrapDestRowStatus,
       "dateTimeServerSetup": dateTimeServerSetup,
       "dateTimeServerType": dateTimeServerType,
       "dateTimeServerIP": dateTimeServerIP,
       "dateTimeZone": dateTimeZone,
       "dateTimeNewDateYear": dateTimeNewDateYear,
       "dateTimeNewDateMonth": dateTimeNewDateMonth,
       "dateTimeNewDateDay": dateTimeNewDateDay,
       "dateTimeNewTimeHour": dateTimeNewTimeHour,
       "dateTimeNewTimeMinute": dateTimeNewTimeMinute,
       "dateTimeNewTimeSecond": dateTimeNewTimeSecond,
       "sysMgmt": sysMgmt,
       "sysMgmtConfigSave": sysMgmtConfigSave,
       "sysMgmtBootupConfig": sysMgmtBootupConfig,
       "sysMgmtReboot": sysMgmtReboot,
       "sysMgmtDefaultConfig": sysMgmtDefaultConfig,
       "sysMgmtLastActionStatus": sysMgmtLastActionStatus,
       "sysMgmtSystemStatus": sysMgmtSystemStatus,
       "sysMgmtCPUUsage": sysMgmtCPUUsage,
       "layer2Setup": layer2Setup,
       "vlanTypeSetup": vlanTypeSetup,
       "igmpSnoopingStateSetup": igmpSnoopingStateSetup,
       "tagVlanPortIsolationState": tagVlanPortIsolationState,
       "stpState": stpState,
       "igmpFilteringStateSetup": igmpFilteringStateSetup,
       "unknownMulticastFrameForwarding": unknownMulticastFrameForwarding,
       "ipSetup": ipSetup,
       "dnsIpAddress": dnsIpAddress,
       "defaultMgmt": defaultMgmt,
       "defaultGateway": defaultGateway,
       "outOfBandIpSetup": outOfBandIpSetup,
       "outOfBandIp": outOfBandIp,
       "outOfBandSubnetMask": outOfBandSubnetMask,
       "outOfBandGateway": outOfBandGateway,
       "maxNumOfInbandIp": maxNumOfInbandIp,
       "inbandIpTable": inbandIpTable,
       "inbandIpEntry": inbandIpEntry,
       "inbandEntryIp": inbandEntryIp,
       "inbandEntrySubnetMask": inbandEntrySubnetMask,
       "inbandEntryVid": inbandEntryVid,
       "inbandEntryRowStatus": inbandEntryRowStatus,
       "filterSetup": filterSetup,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterName": filterName,
       "filterActionState": filterActionState,
       "filterMacAddr": filterMacAddr,
       "filterVid": filterVid,
       "filterRowStatus": filterRowStatus,
       "mirrorSetup": mirrorSetup,
       "mirrorState": mirrorState,
       "mirrorMonitorPort": mirrorMonitorPort,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "mirrorMirroredState": mirrorMirroredState,
       "mirrorDirection": mirrorDirection,
       "aggrSetup": aggrSetup,
       "aggrState": aggrState,
       "aggrSystemPriority": aggrSystemPriority,
       "aggrGroupTable": aggrGroupTable,
       "aggrGroupEntry": aggrGroupEntry,
       "aggrGroupIndex": aggrGroupIndex,
       "aggrGroupState": aggrGroupState,
       "aggrGroupDynamicState": aggrGroupDynamicState,
       "aggrPortTable": aggrPortTable,
       "aggrPortEntry": aggrPortEntry,
       "aggrPortGroup": aggrPortGroup,
       "aggrPortDynamicStateTimeout": aggrPortDynamicStateTimeout,
       "accessCtlSetup": accessCtlSetup,
       "accessCtlTable": accessCtlTable,
       "accessCtlEntry": accessCtlEntry,
       "accessCtlService": accessCtlService,
       "accessCtlEnable": accessCtlEnable,
       "accessCtlServicePort": accessCtlServicePort,
       "accessCtlTimeout": accessCtlTimeout,
       "securedClientTable": securedClientTable,
       "securedClientEntry": securedClientEntry,
       "securedClientIndex": securedClientIndex,
       "securedClientEnable": securedClientEnable,
       "securedClientStartIp": securedClientStartIp,
       "securedClientEndIp": securedClientEndIp,
       "securedClientService": securedClientService,
       "queuingMethodSetup": queuingMethodSetup,
       "portQueuingMethodTable": portQueuingMethodTable,
       "portQueuingMethodEntry": portQueuingMethodEntry,
       "portQueuingMethodQueue": portQueuingMethodQueue,
       "portQueuingMethodWeight": portQueuingMethodWeight,
       "portQueuingMethodMode": portQueuingMethodMode,
       "dhcpSetup": dhcpSetup,
       "dhcpRelay": dhcpRelay,
       "dhcpRelayEnable": dhcpRelayEnable,
       "dhcpRelayOption82Enable": dhcpRelayOption82Enable,
       "dhcpRelayInfoEnable": dhcpRelayInfoEnable,
       "dhcpRelayInfoData": dhcpRelayInfoData,
       "maxNumberOfDhcpRemoteServer": maxNumberOfDhcpRemoteServer,
       "dhcpRemoteServerTable": dhcpRemoteServerTable,
       "dhcpRemoteServerEntry": dhcpRemoteServerEntry,
       "dhcpRemoteServerIp": dhcpRemoteServerIp,
       "dhcpRemoteServerRowStatus": dhcpRemoteServerRowStatus,
       "dhcpServer": dhcpServer,
       "maxNumberOfDhcpServers": maxNumberOfDhcpServers,
       "dhcpServerTable": dhcpServerTable,
       "dhcpServerEntry": dhcpServerEntry,
       "dhcpServerVid": dhcpServerVid,
       "dhcpServerStartAddr": dhcpServerStartAddr,
       "dhcpServerPoolSize": dhcpServerPoolSize,
       "dhcpServerMask": dhcpServerMask,
       "dhcpServerGateway": dhcpServerGateway,
       "dhcpServerPrimaryDNS": dhcpServerPrimaryDNS,
       "dhcpServerSecondaryDNS": dhcpServerSecondaryDNS,
       "dhcpServerRowStatus": dhcpServerRowStatus,
       "staticRouteSetup": staticRouteSetup,
       "maxNumberOfStaticRoutes": maxNumberOfStaticRoutes,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteName": staticRouteName,
       "staticRouteIp": staticRouteIp,
       "staticRouteMask": staticRouteMask,
       "staticRouteGateway": staticRouteGateway,
       "staticRouteMetric": staticRouteMetric,
       "staticRouteRowStatus": staticRouteRowStatus,
       "arpInfo": arpInfo,
       "arpTable": arpTable,
       "arpEntry": arpEntry,
       "arpIndex": arpIndex,
       "arpIpAddr": arpIpAddr,
       "arpMacAddr": arpMacAddr,
       "arpMacVid": arpMacVid,
       "arpType": arpType,
       "portOpModeSetup": portOpModeSetup,
       "portOpModePortTable": portOpModePortTable,
       "portOpModePortEntry": portOpModePortEntry,
       "portOpModePortSpeedDuplex": portOpModePortSpeedDuplex,
       "portOpModePortFlowCntl": portOpModePortFlowCntl,
       "portOpModePortName": portOpModePortName,
       "portOpModePortModuleType": portOpModePortModuleType,
       "portOpModePortLinkUpType": portOpModePortLinkUpType,
       "portOpModePortIntrusionLock": portOpModePortIntrusionLock,
       "portOpModePortLBTestStatus": portOpModePortLBTestStatus,
       "portBasedVlanSetup": portBasedVlanSetup,
       "portBasedVlanPortListTable": portBasedVlanPortListTable,
       "portBasedVlanPortListEntry": portBasedVlanPortListEntry,
       "portBasedVlanPortListMembers": portBasedVlanPortListMembers,
       "multicastPortSetup": multicastPortSetup,
       "multicastPortTable": multicastPortTable,
       "multicastPortEntry": multicastPortEntry,
       "multicastPortImmediateLeave": multicastPortImmediateLeave,
       "multicastPortMaxGroupLimited": multicastPortMaxGroupLimited,
       "multicastPortMaxOfGroup": multicastPortMaxOfGroup,
       "multicastPortIgmpFilteringProfile": multicastPortIgmpFilteringProfile,
       "multicastStatus": multicastStatus,
       "multicastStatusTable": multicastStatusTable,
       "multicastStatusEntry": multicastStatusEntry,
       "multicastStatusIndex": multicastStatusIndex,
       "multicastStatusVlanID": multicastStatusVlanID,
       "multicastStatusPort": multicastStatusPort,
       "multicastStatusGroup": multicastStatusGroup,
       "igmpFilteringProfileSetup": igmpFilteringProfileSetup,
       "igmpFilteringMaxNumberOfProfile": igmpFilteringMaxNumberOfProfile,
       "igmpFilteringProfileTable": igmpFilteringProfileTable,
       "igmpFilteringProfileEntry": igmpFilteringProfileEntry,
       "igmpFilteringProfileName": igmpFilteringProfileName,
       "igmpFilteringProfileStartAddress": igmpFilteringProfileStartAddress,
       "igmpFilteringProfileEndAddress": igmpFilteringProfileEndAddress,
       "igmpFilteringProfileRowStatus": igmpFilteringProfileRowStatus,
       "mvrSetup": mvrSetup,
       "maxNumberOfMVR": maxNumberOfMVR,
       "mvrTable": mvrTable,
       "mvrEntry": mvrEntry,
       "mvrVlanID": mvrVlanID,
       "mvrName": mvrName,
       "mvrMode": mvrMode,
       "mvrRowStatus": mvrRowStatus,
       "mvrPortTable": mvrPortTable,
       "mvrPortEntry": mvrPortEntry,
       "mvrPortRole": mvrPortRole,
       "mvrPortTagging": mvrPortTagging,
       "maxNumberOfMvrGroup": maxNumberOfMvrGroup,
       "mvrGroupTable": mvrGroupTable,
       "mvrGroupEntry": mvrGroupEntry,
       "mvrGroupName": mvrGroupName,
       "mvrGroupStartAddress": mvrGroupStartAddress,
       "mvrGroupEndAddress": mvrGroupEndAddress,
       "mvrGroupRowStatus": mvrGroupRowStatus,
       "layer3Setup": layer3Setup,
       "routerRipState": routerRipState,
       "routerIgmpState": routerIgmpState,
       "routerDvmrpState": routerDvmrpState,
       "routerDvmrpThreshold": routerDvmrpThreshold,
       "routerIpmcPortSetup": routerIpmcPortSetup,
       "routerIpmcPortTable": routerIpmcPortTable,
       "routerIpmcPortEntry": routerIpmcPortEntry,
       "routerIpmcPortEgressUntagVlan": routerIpmcPortEgressUntagVlan,
       "routerVrrpSetup": routerVrrpSetup,
       "routerVrrpMaxNumber": routerVrrpMaxNumber,
       "routerVrrpTable": routerVrrpTable,
       "routerVrrpEntry": routerVrrpEntry,
       "routerVrrpVirtualID": routerVrrpVirtualID,
       "routerVrrpUplinkGateway": routerVrrpUplinkGateway,
       "routerVrrpPreempt": routerVrrpPreempt,
       "routerVrrpInterval": routerVrrpInterval,
       "routerVrrpPriority": routerVrrpPriority,
       "routerVrrpPrimaryVirtualIP": routerVrrpPrimaryVirtualIP,
       "routerVrrpName": routerVrrpName,
       "routerVrrpSecondaryVirtualIP": routerVrrpSecondaryVirtualIP,
       "rpVrrpRowStatus": rpVrrpRowStatus,
       "routerVrrpDomainTable": routerVrrpDomainTable,
       "routerVrrpDomainEntry": routerVrrpDomainEntry,
       "routerVrrpAuthType": routerVrrpAuthType,
       "routerVrrpAuthKey": routerVrrpAuthKey,
       "routerVrrpStatus": routerVrrpStatus,
       "routerVrrpStatusTable": routerVrrpStatusTable,
       "routerVrrpStatusEntry": routerVrrpStatusEntry,
       "routerVrrpStatusIpAddress": routerVrrpStatusIpAddress,
       "routerVrrpStatusIpMaskBits": routerVrrpStatusIpMaskBits,
       "routerVrrpStatusVirtualID": routerVrrpStatusVirtualID,
       "routerVrrpStatusVRStatus": routerVrrpStatusVRStatus,
       "routerVrrpStatusUpLinkStatus": routerVrrpStatusUpLinkStatus,
       "routerDomainSetup": routerDomainSetup,
       "routerDomainTable": routerDomainTable,
       "routerDomainEntry": routerDomainEntry,
       "routerDomainIpAddress": routerDomainIpAddress,
       "routerDomainIpMaskBits": routerDomainIpMaskBits,
       "routerDomainVid": routerDomainVid,
       "routerDomainIpTable": routerDomainIpTable,
       "routerDomainIpEntry": routerDomainIpEntry,
       "routerDomainIpRipDirection": routerDomainIpRipDirection,
       "routerDomainIpRipVersion": routerDomainIpRipVersion,
       "routerDomainIpIgmpVersion": routerDomainIpIgmpVersion,
       "routerDomainIpDvmrp": routerDomainIpDvmrp,
       "diffservSetup": diffservSetup,
       "diffservState": diffservState,
       "diffservMapTable": diffservMapTable,
       "diffservMapEntry": diffservMapEntry,
       "diffservMapDscp": diffservMapDscp,
       "diffservMapPriority": diffservMapPriority,
       "diffservPortTable": diffservPortTable,
       "diffservPortEntry": diffservPortEntry,
       "diffservPortState": diffservPortState,
       "clusterSetup": clusterSetup,
       "clusterManager": clusterManager,
       "clusterMaxNumOfManager": clusterMaxNumOfManager,
       "clusterManagerTable": clusterManagerTable,
       "clusterManagerEntry": clusterManagerEntry,
       "clusterManagerVid": clusterManagerVid,
       "clusterManagerName": clusterManagerName,
       "clusterManagerRowStatus": clusterManagerRowStatus,
       "clusterMembers": clusterMembers,
       "clusterMaxNumOfMember": clusterMaxNumOfMember,
       "clusterMemberTable": clusterMemberTable,
       "clusterMemberEntry": clusterMemberEntry,
       "clusterMemberMac": clusterMemberMac,
       "clusterMemberName": clusterMemberName,
       "clusterMemberModel": clusterMemberModel,
       "clusterMemberPassword": clusterMemberPassword,
       "clusterMemberRowStatus": clusterMemberRowStatus,
       "clusterCandidates": clusterCandidates,
       "clusterCandidateTable": clusterCandidateTable,
       "clusterCandidateEntry": clusterCandidateEntry,
       "clusterCandidateMac": clusterCandidateMac,
       "clusterCandidateName": clusterCandidateName,
       "clusterCandidateModel": clusterCandidateModel,
       "clusterStatus": clusterStatus,
       "clusterStatusRole": clusterStatusRole,
       "clusterStatusManager": clusterStatusManager,
       "clsuterStatusMaxNumOfMember": clsuterStatusMaxNumOfMember,
       "clusterStatusMemberTable": clusterStatusMemberTable,
       "clusterStatusMemberEntry": clusterStatusMemberEntry,
       "clusterStatusMemberMac": clusterStatusMemberMac,
       "clusterStatusMemberName": clusterStatusMemberName,
       "clusterStatusMemberModel": clusterStatusMemberModel,
       "clusterStatusMemberStatus": clusterStatusMemberStatus,
       "faultMIB": faultMIB,
       "eventObjects": eventObjects,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventSeqNum": eventSeqNum,
       "eventEventId": eventEventId,
       "eventName": eventName,
       "eventInstanceType": eventInstanceType,
       "eventInstanceId": eventInstanceId,
       "eventInstanceName": eventInstanceName,
       "eventSeverity": eventSeverity,
       "eventSetTime": eventSetTime,
       "eventDescription": eventDescription,
       "eventServAffective": eventServAffective,
       "faultTrapsMIB": faultTrapsMIB,
       "trapInfoObjects": trapInfoObjects,
       "trapRefSeqNum": trapRefSeqNum,
       "trapPersistence": trapPersistence,
       "trapSenderNodeId": trapSenderNodeId,
       "trapNotifications": trapNotifications,
       "eventOnTrap": eventOnTrap,
       "eventClearedTrap": eventClearedTrap,
       "ipStatus": ipStatus,
       "ipStatusTable": ipStatusTable,
       "ipStatusEntry": ipStatusEntry,
       "ipStatusIPAddress": ipStatusIPAddress,
       "ipStatusVid": ipStatusVid,
       "ipStatusPort": ipStatusPort,
       "ipStatusType": ipStatusType,
       "routingStatus": routingStatus,
       "routingStatusTable": routingStatusTable,
       "routingStatusEntry": routingStatusEntry,
       "routingStatusDestAddress": routingStatusDestAddress,
       "routingStatusDestMaskbits": routingStatusDestMaskbits,
       "routingStatusGateway": routingStatusGateway,
       "routingStatusInterface": routingStatusInterface,
       "routingStatusMetric": routingStatusMetric,
       "routingStatusType": routingStatusType,
       "ospfExt": ospfExt,
       "ospfInterfaceTable": ospfInterfaceTable,
       "ospfInterfaceEntry": ospfInterfaceEntry,
       "ospfIfKeyId": ospfIfKeyId,
       "ospfIfMaskbits": ospfIfMaskbits,
       "ospfIfDesignatedRouterID": ospfIfDesignatedRouterID,
       "ospfIfBackupDesignatedRouterID": ospfIfBackupDesignatedRouterID,
       "ospfIfNbrCount": ospfIfNbrCount,
       "ospfIfAdjacentNbrCount": ospfIfAdjacentNbrCount,
       "ospfIfHelloDueTime": ospfIfHelloDueTime,
       "ospfAreaExtTable": ospfAreaExtTable,
       "ospfAreaExtEntry": ospfAreaExtEntry,
       "ospfAreaExtName": ospfAreaExtName,
       "ospfRedistributeRouteTable": ospfRedistributeRouteTable,
       "ospfRedistributeRouteEntry": ospfRedistributeRouteEntry,
       "ospfRedistributeRouteProtocol": ospfRedistributeRouteProtocol,
       "ospfRedistributeRouteState": ospfRedistributeRouteState,
       "ospfRedistributeRouteType": ospfRedistributeRouteType,
       "ospfRedistributeRouteMetric": ospfRedistributeRouteMetric,
       "ospfNbrExtTable": ospfNbrExtTable,
       "ospfNbrExtEntry": ospfNbrExtEntry,
       "ospfNbrExtRole": ospfNbrExtRole,
       "ospfNbrExtDeadtime": ospfNbrExtDeadtime,
       "ospfNbrExtInterface": ospfNbrExtInterface,
       "ospfNbrExtRXmtL": ospfNbrExtRXmtL,
       "ospfNbrExtRqstL": ospfNbrExtRqstL,
       "ospfNbrExtDBsmL": ospfNbrExtDBsmL,
       "ospfLsdbExtTable": ospfLsdbExtTable,
       "ospfLsdbExtEntry": ospfLsdbExtEntry,
       "ospfLsdbExtLinkCount": ospfLsdbExtLinkCount,
       "ospfLsdbExtRouteAddress": ospfLsdbExtRouteAddress,
       "ospfLsdbExtRouteMaskbits": ospfLsdbExtRouteMaskbits,
       "ospfVirtualLinkTable": ospfVirtualLinkTable,
       "ospfVirtualLinkEntry": ospfVirtualLinkEntry,
       "ospfVirtualLinkName": ospfVirtualLinkName,
       "ospfVirtualLinkKeyId": ospfVirtualLinkKeyId}
)
