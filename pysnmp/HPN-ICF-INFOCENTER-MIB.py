# SNMP MIB module (HPN-ICF-INFOCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-INFOCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:34 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfInfoCenter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119)
)
hpnicfInfoCenter.setRevisions(
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

_HpnicfICLogbuffer_ObjectIdentity = ObjectIdentity
hpnicfICLogbuffer = _HpnicfICLogbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1)
)
_HpnicfICLogbufferObjects_ObjectIdentity = ObjectIdentity
hpnicfICLogbufferObjects = _HpnicfICLogbufferObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1)
)
_HpnicfICMaxLogbufferSize_Type = Unsigned32
_HpnicfICMaxLogbufferSize_Object = MibScalar
hpnicfICMaxLogbufferSize = _HpnicfICMaxLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1, 1),
    _HpnicfICMaxLogbufferSize_Type()
)
hpnicfICMaxLogbufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfICMaxLogbufferSize.setStatus("current")


class _HpnicfICLogbufferSize_Type(Unsigned32):
    """Custom type hpnicfICLogbufferSize based on Unsigned32"""
    defaultValue = 512


_HpnicfICLogbufferSize_Object = MibScalar
hpnicfICLogbufferSize = _HpnicfICLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1, 2),
    _HpnicfICLogbufferSize_Type()
)
hpnicfICLogbufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfICLogbufferSize.setStatus("current")
_HpnicfICLogbufferCurrentMessages_Type = Unsigned32
_HpnicfICLogbufferCurrentMessages_Object = MibScalar
hpnicfICLogbufferCurrentMessages = _HpnicfICLogbufferCurrentMessages_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1, 3),
    _HpnicfICLogbufferCurrentMessages_Type()
)
hpnicfICLogbufferCurrentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfICLogbufferCurrentMessages.setStatus("current")
_HpnicfICLogbufferOverwrittenMessages_Type = Counter32
_HpnicfICLogbufferOverwrittenMessages_Object = MibScalar
hpnicfICLogbufferOverwrittenMessages = _HpnicfICLogbufferOverwrittenMessages_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1, 4),
    _HpnicfICLogbufferOverwrittenMessages_Type()
)
hpnicfICLogbufferOverwrittenMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfICLogbufferOverwrittenMessages.setStatus("current")
_HpnicfICLogbufferDroppedMessages_Type = Counter32
_HpnicfICLogbufferDroppedMessages_Object = MibScalar
hpnicfICLogbufferDroppedMessages = _HpnicfICLogbufferDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1, 5),
    _HpnicfICLogbufferDroppedMessages_Type()
)
hpnicfICLogbufferDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfICLogbufferDroppedMessages.setStatus("current")
_HpnicfICLogbufferContTable_Object = MibTable
hpnicfICLogbufferContTable = _HpnicfICLogbufferContTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfICLogbufferContTable.setStatus("current")
_HpnicfICLogbufferContEntry_Object = MibTableRow
hpnicfICLogbufferContEntry = _HpnicfICLogbufferContEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 2, 1)
)
hpnicfICLogbufferContEntry.setIndexNames(
    (0, "HPN-ICF-INFOCENTER-MIB", "hpnicfICLogbufferContIndex"),
)
if mibBuilder.loadTexts:
    hpnicfICLogbufferContEntry.setStatus("current")


class _HpnicfICLogbufferContIndex_Type(Integer32):
    """Custom type hpnicfICLogbufferContIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfICLogbufferContIndex_Type.__name__ = "Integer32"
_HpnicfICLogbufferContIndex_Object = MibTableColumn
hpnicfICLogbufferContIndex = _HpnicfICLogbufferContIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 2, 1, 1),
    _HpnicfICLogbufferContIndex_Type()
)
hpnicfICLogbufferContIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfICLogbufferContIndex.setStatus("current")


class _HpnicfICLogbufferContDescription_Type(DisplayString):
    """Custom type hpnicfICLogbufferContDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_HpnicfICLogbufferContDescription_Type.__name__ = "DisplayString"
_HpnicfICLogbufferContDescription_Object = MibTableColumn
hpnicfICLogbufferContDescription = _HpnicfICLogbufferContDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 2, 1, 2),
    _HpnicfICLogbufferContDescription_Type()
)
hpnicfICLogbufferContDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfICLogbufferContDescription.setStatus("current")
_HpnicfICLoghost_ObjectIdentity = ObjectIdentity
hpnicfICLoghost = _HpnicfICLoghost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2)
)
_HpnicfICLoghostObjects_ObjectIdentity = ObjectIdentity
hpnicfICLoghostObjects = _HpnicfICLoghostObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 1)
)
_HpnicfICMaxLoghost_Type = Unsigned32
_HpnicfICMaxLoghost_Object = MibScalar
hpnicfICMaxLoghost = _HpnicfICMaxLoghost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 1, 1),
    _HpnicfICMaxLoghost_Type()
)
hpnicfICMaxLoghost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfICMaxLoghost.setStatus("current")
_HpnicfICLoghostSourceInterface_Type = InterfaceIndexOrZero
_HpnicfICLoghostSourceInterface_Object = MibScalar
hpnicfICLoghostSourceInterface = _HpnicfICLoghostSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 1, 2),
    _HpnicfICLoghostSourceInterface_Type()
)
hpnicfICLoghostSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfICLoghostSourceInterface.setStatus("current")


class _HpnicfICLoghostTimestampType_Type(ICTimeStampType):
    """Custom type hpnicfICLoghostTimestampType based on ICTimeStampType"""


_HpnicfICLoghostTimestampType_Object = MibScalar
hpnicfICLoghostTimestampType = _HpnicfICLoghostTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 1, 3),
    _HpnicfICLoghostTimestampType_Type()
)
hpnicfICLoghostTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfICLoghostTimestampType.setStatus("current")
_HpnicfICLoghostTable_Object = MibTable
hpnicfICLoghostTable = _HpnicfICLoghostTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfICLoghostTable.setStatus("current")
_HpnicfICLoghostEntry_Object = MibTableRow
hpnicfICLoghostEntry = _HpnicfICLoghostEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1)
)
hpnicfICLoghostEntry.setIndexNames(
    (0, "HPN-ICF-INFOCENTER-MIB", "hpnicfICLoghostIndex"),
)
if mibBuilder.loadTexts:
    hpnicfICLoghostEntry.setStatus("current")


class _HpnicfICLoghostIndex_Type(Unsigned32):
    """Custom type hpnicfICLoghostIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfICLoghostIndex_Type.__name__ = "Unsigned32"
_HpnicfICLoghostIndex_Object = MibTableColumn
hpnicfICLoghostIndex = _HpnicfICLoghostIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 1),
    _HpnicfICLoghostIndex_Type()
)
hpnicfICLoghostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfICLoghostIndex.setStatus("current")


class _HpnicfICLoghostIpaddressType_Type(InetAddressType):
    """Custom type hpnicfICLoghostIpaddressType based on InetAddressType"""


_HpnicfICLoghostIpaddressType_Object = MibTableColumn
hpnicfICLoghostIpaddressType = _HpnicfICLoghostIpaddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 2),
    _HpnicfICLoghostIpaddressType_Type()
)
hpnicfICLoghostIpaddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfICLoghostIpaddressType.setStatus("current")
_HpnicfICLoghostIpaddress_Type = InetAddress
_HpnicfICLoghostIpaddress_Object = MibTableColumn
hpnicfICLoghostIpaddress = _HpnicfICLoghostIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 3),
    _HpnicfICLoghostIpaddress_Type()
)
hpnicfICLoghostIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfICLoghostIpaddress.setStatus("current")
_HpnicfICLoghostVPNName_Type = DisplayString
_HpnicfICLoghostVPNName_Object = MibTableColumn
hpnicfICLoghostVPNName = _HpnicfICLoghostVPNName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 4),
    _HpnicfICLoghostVPNName_Type()
)
hpnicfICLoghostVPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfICLoghostVPNName.setStatus("current")


class _HpnicfICLoghostFacility_Type(ICFacilityType):
    """Custom type hpnicfICLoghostFacility based on ICFacilityType"""


_HpnicfICLoghostFacility_Object = MibTableColumn
hpnicfICLoghostFacility = _HpnicfICLoghostFacility_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 5),
    _HpnicfICLoghostFacility_Type()
)
hpnicfICLoghostFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfICLoghostFacility.setStatus("current")
_HpnicfICLoghostOperateRowStatus_Type = RowStatus
_HpnicfICLoghostOperateRowStatus_Object = MibTableColumn
hpnicfICLoghostOperateRowStatus = _HpnicfICLoghostOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 6),
    _HpnicfICLoghostOperateRowStatus_Type()
)
hpnicfICLoghostOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfICLoghostOperateRowStatus.setStatus("current")


class _HpnicfICLoghostIpaddressPort_Type(Unsigned32):
    """Custom type hpnicfICLoghostIpaddressPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfICLoghostIpaddressPort_Type.__name__ = "Unsigned32"
_HpnicfICLoghostIpaddressPort_Object = MibTableColumn
hpnicfICLoghostIpaddressPort = _HpnicfICLoghostIpaddressPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 7),
    _HpnicfICLoghostIpaddressPort_Type()
)
hpnicfICLoghostIpaddressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfICLoghostIpaddressPort.setStatus("current")
_HpnicfICLoghostTAddress_Type = TAddress
_HpnicfICLoghostTAddress_Object = MibTableColumn
hpnicfICLoghostTAddress = _HpnicfICLoghostTAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 8),
    _HpnicfICLoghostTAddress_Type()
)
hpnicfICLoghostTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfICLoghostTAddress.setStatus("current")
_HpnicfICDirection_ObjectIdentity = ObjectIdentity
hpnicfICDirection = _HpnicfICDirection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3)
)
_HpnicfICDirectionTable_Object = MibTable
hpnicfICDirectionTable = _HpnicfICDirectionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfICDirectionTable.setStatus("current")
_HpnicfICDirectionEntry_Object = MibTableRow
hpnicfICDirectionEntry = _HpnicfICDirectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3, 1, 1)
)
hpnicfICDirectionEntry.setIndexNames(
    (0, "HPN-ICF-INFOCENTER-MIB", "hpnicfICDirectionIndex"),
)
if mibBuilder.loadTexts:
    hpnicfICDirectionEntry.setStatus("current")
_HpnicfICDirectionIndex_Type = Unsigned32
_HpnicfICDirectionIndex_Object = MibTableColumn
hpnicfICDirectionIndex = _HpnicfICDirectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3, 1, 1, 1),
    _HpnicfICDirectionIndex_Type()
)
hpnicfICDirectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfICDirectionIndex.setStatus("current")


class _HpnicfICDirectionName_Type(DisplayString):
    """Custom type hpnicfICDirectionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HpnicfICDirectionName_Type.__name__ = "DisplayString"
_HpnicfICDirectionName_Object = MibTableColumn
hpnicfICDirectionName = _HpnicfICDirectionName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3, 1, 1, 2),
    _HpnicfICDirectionName_Type()
)
hpnicfICDirectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfICDirectionName.setStatus("current")
_HpnicfICDirectionState_Type = TruthValue
_HpnicfICDirectionState_Object = MibTableColumn
hpnicfICDirectionState = _HpnicfICDirectionState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3, 1, 1, 3),
    _HpnicfICDirectionState_Type()
)
hpnicfICDirectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfICDirectionState.setStatus("current")
_HpnicfICModule_ObjectIdentity = ObjectIdentity
hpnicfICModule = _HpnicfICModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 4)
)
_HpnicfICModuleTable_Object = MibTable
hpnicfICModuleTable = _HpnicfICModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfICModuleTable.setStatus("current")
_HpnicfICModuleEntry_Object = MibTableRow
hpnicfICModuleEntry = _HpnicfICModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 4, 1, 1)
)
hpnicfICModuleEntry.setIndexNames(
    (1, "HPN-ICF-INFOCENTER-MIB", "hpnicfICModuleName"),
)
if mibBuilder.loadTexts:
    hpnicfICModuleEntry.setStatus("current")


class _HpnicfICModuleName_Type(DisplayString):
    """Custom type hpnicfICModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HpnicfICModuleName_Type.__name__ = "DisplayString"
_HpnicfICModuleName_Object = MibTableColumn
hpnicfICModuleName = _HpnicfICModuleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 4, 1, 1, 1),
    _HpnicfICModuleName_Type()
)
hpnicfICModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfICModuleName.setStatus("current")
_HpnicfICLog_ObjectIdentity = ObjectIdentity
hpnicfICLog = _HpnicfICLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5)
)
_HpnicfICLogObjects_ObjectIdentity = ObjectIdentity
hpnicfICLogObjects = _HpnicfICLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 1)
)


class _HpnicfICLogGlobalState_Type(TruthValue):
    """Custom type hpnicfICLogGlobalState based on TruthValue"""


_HpnicfICLogGlobalState_Object = MibScalar
hpnicfICLogGlobalState = _HpnicfICLogGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 1, 1),
    _HpnicfICLogGlobalState_Type()
)
hpnicfICLogGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfICLogGlobalState.setStatus("current")


class _HpnicfICLogTimestampType_Type(ICTimeStampType):
    """Custom type hpnicfICLogTimestampType based on ICTimeStampType"""


_HpnicfICLogTimestampType_Object = MibScalar
hpnicfICLogTimestampType = _HpnicfICLogTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 1, 2),
    _HpnicfICLogTimestampType_Type()
)
hpnicfICLogTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfICLogTimestampType.setStatus("current")
_HpnicfICLogTable_Object = MibTable
hpnicfICLogTable = _HpnicfICLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 2)
)
if mibBuilder.loadTexts:
    hpnicfICLogTable.setStatus("current")
_HpnicfICLogEntry_Object = MibTableRow
hpnicfICLogEntry = _HpnicfICLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 2, 1)
)
hpnicfICLogEntry.setIndexNames(
    (0, "HPN-ICF-INFOCENTER-MIB", "hpnicfICDirectionIndex"),
    (1, "HPN-ICF-INFOCENTER-MIB", "hpnicfICModuleName"),
)
if mibBuilder.loadTexts:
    hpnicfICLogEntry.setStatus("current")
_HpnicfICLogLevel_Type = ICMessageLevelType
_HpnicfICLogLevel_Object = MibTableColumn
hpnicfICLogLevel = _HpnicfICLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 2, 1, 1),
    _HpnicfICLogLevel_Type()
)
hpnicfICLogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfICLogLevel.setStatus("current")
_HpnicfICLogRowStatus_Type = RowStatus
_HpnicfICLogRowStatus_Object = MibTableColumn
hpnicfICLogRowStatus = _HpnicfICLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 2, 1, 2),
    _HpnicfICLogRowStatus_Type()
)
hpnicfICLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfICLogRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-INFOCENTER-MIB",
    **{"ICMessageLevelType": ICMessageLevelType,
       "ICFacilityType": ICFacilityType,
       "ICTimeStampType": ICTimeStampType,
       "hpnicfInfoCenter": hpnicfInfoCenter,
       "hpnicfICLogbuffer": hpnicfICLogbuffer,
       "hpnicfICLogbufferObjects": hpnicfICLogbufferObjects,
       "hpnicfICMaxLogbufferSize": hpnicfICMaxLogbufferSize,
       "hpnicfICLogbufferSize": hpnicfICLogbufferSize,
       "hpnicfICLogbufferCurrentMessages": hpnicfICLogbufferCurrentMessages,
       "hpnicfICLogbufferOverwrittenMessages": hpnicfICLogbufferOverwrittenMessages,
       "hpnicfICLogbufferDroppedMessages": hpnicfICLogbufferDroppedMessages,
       "hpnicfICLogbufferContTable": hpnicfICLogbufferContTable,
       "hpnicfICLogbufferContEntry": hpnicfICLogbufferContEntry,
       "hpnicfICLogbufferContIndex": hpnicfICLogbufferContIndex,
       "hpnicfICLogbufferContDescription": hpnicfICLogbufferContDescription,
       "hpnicfICLoghost": hpnicfICLoghost,
       "hpnicfICLoghostObjects": hpnicfICLoghostObjects,
       "hpnicfICMaxLoghost": hpnicfICMaxLoghost,
       "hpnicfICLoghostSourceInterface": hpnicfICLoghostSourceInterface,
       "hpnicfICLoghostTimestampType": hpnicfICLoghostTimestampType,
       "hpnicfICLoghostTable": hpnicfICLoghostTable,
       "hpnicfICLoghostEntry": hpnicfICLoghostEntry,
       "hpnicfICLoghostIndex": hpnicfICLoghostIndex,
       "hpnicfICLoghostIpaddressType": hpnicfICLoghostIpaddressType,
       "hpnicfICLoghostIpaddress": hpnicfICLoghostIpaddress,
       "hpnicfICLoghostVPNName": hpnicfICLoghostVPNName,
       "hpnicfICLoghostFacility": hpnicfICLoghostFacility,
       "hpnicfICLoghostOperateRowStatus": hpnicfICLoghostOperateRowStatus,
       "hpnicfICLoghostIpaddressPort": hpnicfICLoghostIpaddressPort,
       "hpnicfICLoghostTAddress": hpnicfICLoghostTAddress,
       "hpnicfICDirection": hpnicfICDirection,
       "hpnicfICDirectionTable": hpnicfICDirectionTable,
       "hpnicfICDirectionEntry": hpnicfICDirectionEntry,
       "hpnicfICDirectionIndex": hpnicfICDirectionIndex,
       "hpnicfICDirectionName": hpnicfICDirectionName,
       "hpnicfICDirectionState": hpnicfICDirectionState,
       "hpnicfICModule": hpnicfICModule,
       "hpnicfICModuleTable": hpnicfICModuleTable,
       "hpnicfICModuleEntry": hpnicfICModuleEntry,
       "hpnicfICModuleName": hpnicfICModuleName,
       "hpnicfICLog": hpnicfICLog,
       "hpnicfICLogObjects": hpnicfICLogObjects,
       "hpnicfICLogGlobalState": hpnicfICLogGlobalState,
       "hpnicfICLogTimestampType": hpnicfICLogTimestampType,
       "hpnicfICLogTable": hpnicfICLogTable,
       "hpnicfICLogEntry": hpnicfICLogEntry,
       "hpnicfICLogLevel": hpnicfICLogLevel,
       "hpnicfICLogRowStatus": hpnicfICLogRowStatus}
)
