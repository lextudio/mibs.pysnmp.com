# SNMP MIB module (HH3C-INFOCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-INFOCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:34 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowStatus,
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cInfoCenter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119)
)
hh3cInfoCenter.setRevisions(
        ("2012-03-07 19:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ICMessageLevelType(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("informational", 6),
          ("invalid", 8),
          ("notice", 5),
          ("warning", 4))
    )



class ICFacilityType(Integer32, TextualConvention):
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
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("clockDaemon", 9),
          ("clockDaemon2", 15),
          ("ftpDaemon", 11),
          ("internallyMessages", 5),
          ("kernel", 0),
          ("linePrinter", 6),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("logAlert", 14),
          ("logAudit", 13),
          ("mailSystem", 2),
          ("networkNews", 7),
          ("ntp", 12),
          ("securityAuthorization", 4),
          ("securityAuthorization2", 10),
          ("systemDaemons", 3),
          ("userLevel", 1),
          ("uucp", 8))
    )



class ICTimeStampType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("date", 0),
          ("dateWithoutYear", 3),
          ("iso", 2),
          ("none", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cICLogbuffer_ObjectIdentity = ObjectIdentity
hh3cICLogbuffer = _Hh3cICLogbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1)
)
_Hh3cICLogbufferObjects_ObjectIdentity = ObjectIdentity
hh3cICLogbufferObjects = _Hh3cICLogbufferObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1)
)
_Hh3cICMaxLogbufferSize_Type = Unsigned32
_Hh3cICMaxLogbufferSize_Object = MibScalar
hh3cICMaxLogbufferSize = _Hh3cICMaxLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1, 1),
    _Hh3cICMaxLogbufferSize_Type()
)
hh3cICMaxLogbufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cICMaxLogbufferSize.setStatus("current")


class _Hh3cICLogbufferSize_Type(Unsigned32):
    """Custom type hh3cICLogbufferSize based on Unsigned32"""
    defaultValue = 512


_Hh3cICLogbufferSize_Object = MibScalar
hh3cICLogbufferSize = _Hh3cICLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1, 2),
    _Hh3cICLogbufferSize_Type()
)
hh3cICLogbufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cICLogbufferSize.setStatus("current")
_Hh3cICLogbufferCurrentMessages_Type = Unsigned32
_Hh3cICLogbufferCurrentMessages_Object = MibScalar
hh3cICLogbufferCurrentMessages = _Hh3cICLogbufferCurrentMessages_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1, 3),
    _Hh3cICLogbufferCurrentMessages_Type()
)
hh3cICLogbufferCurrentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cICLogbufferCurrentMessages.setStatus("current")
_Hh3cICLogbufferOverwrittenMessages_Type = Counter32
_Hh3cICLogbufferOverwrittenMessages_Object = MibScalar
hh3cICLogbufferOverwrittenMessages = _Hh3cICLogbufferOverwrittenMessages_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1, 4),
    _Hh3cICLogbufferOverwrittenMessages_Type()
)
hh3cICLogbufferOverwrittenMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cICLogbufferOverwrittenMessages.setStatus("current")
_Hh3cICLogbufferDroppedMessages_Type = Counter32
_Hh3cICLogbufferDroppedMessages_Object = MibScalar
hh3cICLogbufferDroppedMessages = _Hh3cICLogbufferDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1, 5),
    _Hh3cICLogbufferDroppedMessages_Type()
)
hh3cICLogbufferDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cICLogbufferDroppedMessages.setStatus("current")
_Hh3cICLogbufferContTable_Object = MibTable
hh3cICLogbufferContTable = _Hh3cICLogbufferContTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cICLogbufferContTable.setStatus("current")
_Hh3cICLogbufferContEntry_Object = MibTableRow
hh3cICLogbufferContEntry = _Hh3cICLogbufferContEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 2, 1)
)
hh3cICLogbufferContEntry.setIndexNames(
    (0, "HH3C-INFOCENTER-MIB", "hh3cICLogbufferContIndex"),
)
if mibBuilder.loadTexts:
    hh3cICLogbufferContEntry.setStatus("current")


class _Hh3cICLogbufferContIndex_Type(Integer32):
    """Custom type hh3cICLogbufferContIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cICLogbufferContIndex_Type.__name__ = "Integer32"
_Hh3cICLogbufferContIndex_Object = MibTableColumn
hh3cICLogbufferContIndex = _Hh3cICLogbufferContIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 2, 1, 1),
    _Hh3cICLogbufferContIndex_Type()
)
hh3cICLogbufferContIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cICLogbufferContIndex.setStatus("current")


class _Hh3cICLogbufferContDescription_Type(DisplayString):
    """Custom type hh3cICLogbufferContDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_Hh3cICLogbufferContDescription_Type.__name__ = "DisplayString"
_Hh3cICLogbufferContDescription_Object = MibTableColumn
hh3cICLogbufferContDescription = _Hh3cICLogbufferContDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 2, 1, 2),
    _Hh3cICLogbufferContDescription_Type()
)
hh3cICLogbufferContDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cICLogbufferContDescription.setStatus("current")
_Hh3cICLoghost_ObjectIdentity = ObjectIdentity
hh3cICLoghost = _Hh3cICLoghost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2)
)
_Hh3cICLoghostObjects_ObjectIdentity = ObjectIdentity
hh3cICLoghostObjects = _Hh3cICLoghostObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 1)
)
_Hh3cICMaxLoghost_Type = Unsigned32
_Hh3cICMaxLoghost_Object = MibScalar
hh3cICMaxLoghost = _Hh3cICMaxLoghost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 1, 1),
    _Hh3cICMaxLoghost_Type()
)
hh3cICMaxLoghost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cICMaxLoghost.setStatus("current")
_Hh3cICLoghostSourceInterface_Type = InterfaceIndexOrZero
_Hh3cICLoghostSourceInterface_Object = MibScalar
hh3cICLoghostSourceInterface = _Hh3cICLoghostSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 1, 2),
    _Hh3cICLoghostSourceInterface_Type()
)
hh3cICLoghostSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cICLoghostSourceInterface.setStatus("current")


class _Hh3cICLoghostTimestampType_Type(ICTimeStampType):
    """Custom type hh3cICLoghostTimestampType based on ICTimeStampType"""


_Hh3cICLoghostTimestampType_Object = MibScalar
hh3cICLoghostTimestampType = _Hh3cICLoghostTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 1, 3),
    _Hh3cICLoghostTimestampType_Type()
)
hh3cICLoghostTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cICLoghostTimestampType.setStatus("current")
_Hh3cICLoghostTable_Object = MibTable
hh3cICLoghostTable = _Hh3cICLoghostTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cICLoghostTable.setStatus("current")
_Hh3cICLoghostEntry_Object = MibTableRow
hh3cICLoghostEntry = _Hh3cICLoghostEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1)
)
hh3cICLoghostEntry.setIndexNames(
    (0, "HH3C-INFOCENTER-MIB", "hh3cICLoghostIndex"),
)
if mibBuilder.loadTexts:
    hh3cICLoghostEntry.setStatus("current")


class _Hh3cICLoghostIndex_Type(Unsigned32):
    """Custom type hh3cICLoghostIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cICLoghostIndex_Type.__name__ = "Unsigned32"
_Hh3cICLoghostIndex_Object = MibTableColumn
hh3cICLoghostIndex = _Hh3cICLoghostIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 1),
    _Hh3cICLoghostIndex_Type()
)
hh3cICLoghostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cICLoghostIndex.setStatus("current")


class _Hh3cICLoghostIpaddressType_Type(InetAddressType):
    """Custom type hh3cICLoghostIpaddressType based on InetAddressType"""


_Hh3cICLoghostIpaddressType_Object = MibTableColumn
hh3cICLoghostIpaddressType = _Hh3cICLoghostIpaddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 2),
    _Hh3cICLoghostIpaddressType_Type()
)
hh3cICLoghostIpaddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cICLoghostIpaddressType.setStatus("current")
_Hh3cICLoghostIpaddress_Type = InetAddress
_Hh3cICLoghostIpaddress_Object = MibTableColumn
hh3cICLoghostIpaddress = _Hh3cICLoghostIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 3),
    _Hh3cICLoghostIpaddress_Type()
)
hh3cICLoghostIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cICLoghostIpaddress.setStatus("current")
_Hh3cICLoghostVPNName_Type = DisplayString
_Hh3cICLoghostVPNName_Object = MibTableColumn
hh3cICLoghostVPNName = _Hh3cICLoghostVPNName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 4),
    _Hh3cICLoghostVPNName_Type()
)
hh3cICLoghostVPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cICLoghostVPNName.setStatus("current")


class _Hh3cICLoghostFacility_Type(ICFacilityType):
    """Custom type hh3cICLoghostFacility based on ICFacilityType"""


_Hh3cICLoghostFacility_Object = MibTableColumn
hh3cICLoghostFacility = _Hh3cICLoghostFacility_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 5),
    _Hh3cICLoghostFacility_Type()
)
hh3cICLoghostFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cICLoghostFacility.setStatus("current")
_Hh3cICLoghostOperateRowStatus_Type = RowStatus
_Hh3cICLoghostOperateRowStatus_Object = MibTableColumn
hh3cICLoghostOperateRowStatus = _Hh3cICLoghostOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 6),
    _Hh3cICLoghostOperateRowStatus_Type()
)
hh3cICLoghostOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cICLoghostOperateRowStatus.setStatus("current")


class _Hh3cICLoghostIpaddressPort_Type(Unsigned32):
    """Custom type hh3cICLoghostIpaddressPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cICLoghostIpaddressPort_Type.__name__ = "Unsigned32"
_Hh3cICLoghostIpaddressPort_Object = MibTableColumn
hh3cICLoghostIpaddressPort = _Hh3cICLoghostIpaddressPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 7),
    _Hh3cICLoghostIpaddressPort_Type()
)
hh3cICLoghostIpaddressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cICLoghostIpaddressPort.setStatus("current")
_Hh3cICLoghostTAddress_Type = TAddress
_Hh3cICLoghostTAddress_Object = MibTableColumn
hh3cICLoghostTAddress = _Hh3cICLoghostTAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 8),
    _Hh3cICLoghostTAddress_Type()
)
hh3cICLoghostTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cICLoghostTAddress.setStatus("current")
_Hh3cICDirection_ObjectIdentity = ObjectIdentity
hh3cICDirection = _Hh3cICDirection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 3)
)
_Hh3cICDirectionTable_Object = MibTable
hh3cICDirectionTable = _Hh3cICDirectionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cICDirectionTable.setStatus("current")
_Hh3cICDirectionEntry_Object = MibTableRow
hh3cICDirectionEntry = _Hh3cICDirectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 3, 1, 1)
)
hh3cICDirectionEntry.setIndexNames(
    (0, "HH3C-INFOCENTER-MIB", "hh3cICDirectionIndex"),
)
if mibBuilder.loadTexts:
    hh3cICDirectionEntry.setStatus("current")
_Hh3cICDirectionIndex_Type = Unsigned32
_Hh3cICDirectionIndex_Object = MibTableColumn
hh3cICDirectionIndex = _Hh3cICDirectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 3, 1, 1, 1),
    _Hh3cICDirectionIndex_Type()
)
hh3cICDirectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cICDirectionIndex.setStatus("current")


class _Hh3cICDirectionName_Type(DisplayString):
    """Custom type hh3cICDirectionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_Hh3cICDirectionName_Type.__name__ = "DisplayString"
_Hh3cICDirectionName_Object = MibTableColumn
hh3cICDirectionName = _Hh3cICDirectionName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 3, 1, 1, 2),
    _Hh3cICDirectionName_Type()
)
hh3cICDirectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cICDirectionName.setStatus("current")
_Hh3cICDirectionState_Type = TruthValue
_Hh3cICDirectionState_Object = MibTableColumn
hh3cICDirectionState = _Hh3cICDirectionState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 3, 1, 1, 3),
    _Hh3cICDirectionState_Type()
)
hh3cICDirectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cICDirectionState.setStatus("current")
_Hh3cICModule_ObjectIdentity = ObjectIdentity
hh3cICModule = _Hh3cICModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 4)
)
_Hh3cICModuleTable_Object = MibTable
hh3cICModuleTable = _Hh3cICModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cICModuleTable.setStatus("current")
_Hh3cICModuleEntry_Object = MibTableRow
hh3cICModuleEntry = _Hh3cICModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 4, 1, 1)
)
hh3cICModuleEntry.setIndexNames(
    (1, "HH3C-INFOCENTER-MIB", "hh3cICModuleName"),
)
if mibBuilder.loadTexts:
    hh3cICModuleEntry.setStatus("current")


class _Hh3cICModuleName_Type(DisplayString):
    """Custom type hh3cICModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Hh3cICModuleName_Type.__name__ = "DisplayString"
_Hh3cICModuleName_Object = MibTableColumn
hh3cICModuleName = _Hh3cICModuleName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 4, 1, 1, 1),
    _Hh3cICModuleName_Type()
)
hh3cICModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cICModuleName.setStatus("current")
_Hh3cICLog_ObjectIdentity = ObjectIdentity
hh3cICLog = _Hh3cICLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 5)
)
_Hh3cICLogObjects_ObjectIdentity = ObjectIdentity
hh3cICLogObjects = _Hh3cICLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 1)
)


class _Hh3cICLogGlobalState_Type(TruthValue):
    """Custom type hh3cICLogGlobalState based on TruthValue"""


_Hh3cICLogGlobalState_Object = MibScalar
hh3cICLogGlobalState = _Hh3cICLogGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 1, 1),
    _Hh3cICLogGlobalState_Type()
)
hh3cICLogGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cICLogGlobalState.setStatus("current")


class _Hh3cICLogTimestampType_Type(ICTimeStampType):
    """Custom type hh3cICLogTimestampType based on ICTimeStampType"""


_Hh3cICLogTimestampType_Object = MibScalar
hh3cICLogTimestampType = _Hh3cICLogTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 1, 2),
    _Hh3cICLogTimestampType_Type()
)
hh3cICLogTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cICLogTimestampType.setStatus("current")
_Hh3cICLogTable_Object = MibTable
hh3cICLogTable = _Hh3cICLogTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 2)
)
if mibBuilder.loadTexts:
    hh3cICLogTable.setStatus("current")
_Hh3cICLogEntry_Object = MibTableRow
hh3cICLogEntry = _Hh3cICLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 2, 1)
)
hh3cICLogEntry.setIndexNames(
    (0, "HH3C-INFOCENTER-MIB", "hh3cICDirectionIndex"),
    (1, "HH3C-INFOCENTER-MIB", "hh3cICModuleName"),
)
if mibBuilder.loadTexts:
    hh3cICLogEntry.setStatus("current")
_Hh3cICLogLevel_Type = ICMessageLevelType
_Hh3cICLogLevel_Object = MibTableColumn
hh3cICLogLevel = _Hh3cICLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 2, 1, 1),
    _Hh3cICLogLevel_Type()
)
hh3cICLogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cICLogLevel.setStatus("current")
_Hh3cICLogRowStatus_Type = RowStatus
_Hh3cICLogRowStatus_Object = MibTableColumn
hh3cICLogRowStatus = _Hh3cICLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 2, 1, 2),
    _Hh3cICLogRowStatus_Type()
)
hh3cICLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cICLogRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-INFOCENTER-MIB",
    **{"ICMessageLevelType": ICMessageLevelType,
       "ICFacilityType": ICFacilityType,
       "ICTimeStampType": ICTimeStampType,
       "hh3cInfoCenter": hh3cInfoCenter,
       "hh3cICLogbuffer": hh3cICLogbuffer,
       "hh3cICLogbufferObjects": hh3cICLogbufferObjects,
       "hh3cICMaxLogbufferSize": hh3cICMaxLogbufferSize,
       "hh3cICLogbufferSize": hh3cICLogbufferSize,
       "hh3cICLogbufferCurrentMessages": hh3cICLogbufferCurrentMessages,
       "hh3cICLogbufferOverwrittenMessages": hh3cICLogbufferOverwrittenMessages,
       "hh3cICLogbufferDroppedMessages": hh3cICLogbufferDroppedMessages,
       "hh3cICLogbufferContTable": hh3cICLogbufferContTable,
       "hh3cICLogbufferContEntry": hh3cICLogbufferContEntry,
       "hh3cICLogbufferContIndex": hh3cICLogbufferContIndex,
       "hh3cICLogbufferContDescription": hh3cICLogbufferContDescription,
       "hh3cICLoghost": hh3cICLoghost,
       "hh3cICLoghostObjects": hh3cICLoghostObjects,
       "hh3cICMaxLoghost": hh3cICMaxLoghost,
       "hh3cICLoghostSourceInterface": hh3cICLoghostSourceInterface,
       "hh3cICLoghostTimestampType": hh3cICLoghostTimestampType,
       "hh3cICLoghostTable": hh3cICLoghostTable,
       "hh3cICLoghostEntry": hh3cICLoghostEntry,
       "hh3cICLoghostIndex": hh3cICLoghostIndex,
       "hh3cICLoghostIpaddressType": hh3cICLoghostIpaddressType,
       "hh3cICLoghostIpaddress": hh3cICLoghostIpaddress,
       "hh3cICLoghostVPNName": hh3cICLoghostVPNName,
       "hh3cICLoghostFacility": hh3cICLoghostFacility,
       "hh3cICLoghostOperateRowStatus": hh3cICLoghostOperateRowStatus,
       "hh3cICLoghostIpaddressPort": hh3cICLoghostIpaddressPort,
       "hh3cICLoghostTAddress": hh3cICLoghostTAddress,
       "hh3cICDirection": hh3cICDirection,
       "hh3cICDirectionTable": hh3cICDirectionTable,
       "hh3cICDirectionEntry": hh3cICDirectionEntry,
       "hh3cICDirectionIndex": hh3cICDirectionIndex,
       "hh3cICDirectionName": hh3cICDirectionName,
       "hh3cICDirectionState": hh3cICDirectionState,
       "hh3cICModule": hh3cICModule,
       "hh3cICModuleTable": hh3cICModuleTable,
       "hh3cICModuleEntry": hh3cICModuleEntry,
       "hh3cICModuleName": hh3cICModuleName,
       "hh3cICLog": hh3cICLog,
       "hh3cICLogObjects": hh3cICLogObjects,
       "hh3cICLogGlobalState": hh3cICLogGlobalState,
       "hh3cICLogTimestampType": hh3cICLogTimestampType,
       "hh3cICLogTable": hh3cICLogTable,
       "hh3cICLogEntry": hh3cICLogEntry,
       "hh3cICLogLevel": hh3cICLogLevel,
       "hh3cICLogRowStatus": hh3cICLogRowStatus}
)
