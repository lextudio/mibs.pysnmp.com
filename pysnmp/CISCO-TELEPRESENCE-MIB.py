# SNMP MIB module (CISCO-TELEPRESENCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TELEPRESENCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:40 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoTelepresenceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 643)
)
ciscoTelepresenceMIB.setRevisions(
        ("2014-07-18 00:00",
         "2012-07-17 00:00",
         "2012-03-23 00:00",
         "2011-08-23 00:00",
         "2010-07-23 00:00",
         "2010-07-13 00:00",
         "2009-07-12 00:00",
         "2008-02-13 00:00",
         "2007-12-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CtpSystemResetMode(Integer32, TextualConvention):
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
        *(("forceReset", 4),
          ("noRestart", 1),
          ("resetPending", 3),
          ("restartPending", 2))
    )



class CtpPeripheralCableCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("internalError", 5),
          ("loose", 2),
          ("plugged", 1),
          ("unknown", 4),
          ("unplugged", 3))
    )



class CtpPeripheralPowerCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("internalError", 5),
          ("off", 3),
          ("on", 1),
          ("standby", 2),
          ("unknown", 4))
    )



class CtpPeripheralStatusCode(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("cableError", 2),
          ("commError", 8),
          ("detectionDisabled", 9),
          ("deviceError", 6),
          ("linkError", 7),
          ("mgmtSysConfigError", 4),
          ("noError", 0),
          ("other", 1),
          ("powerError", 3),
          ("systemError", 5))
    )



class CtpSystemAccessProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("snmp", 2),
          ("ssh", 3))
    )



class CtpPeripheralDeviceCategoryCode(Integer32, TextualConvention):
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
        *(("audioExpansionUnit", 12),
          ("auxHDMIInputDevice", 19),
          ("auxHDMIOutputDevice", 17),
          ("auxiliaryControlUnit", 11),
          ("bringYourOwnDevice", 20),
          ("camera", 4),
          ("digitialMediaSystem", 16),
          ("display", 5),
          ("docCamera", 7),
          ("dviDevice", 9),
          ("headset", 14),
          ("ipPhone", 3),
          ("microphone", 13),
          ("other", 1),
          ("positionMic", 15),
          ("presentationCodec", 10),
          ("projector", 8),
          ("secCodec", 6),
          ("uiDevice", 18),
          ("unknown", 0),
          ("uplinkDevice", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoTelepresenceMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTelepresenceMIBNotifs = _CiscoTelepresenceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 0)
)
_CiscoTelepresenceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTelepresenceMIBObjects = _CiscoTelepresenceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1)
)
_CtpObjects_ObjectIdentity = ObjectIdentity
ctpObjects = _CtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 1)
)


class _CtpPeripheralErrorNotifyEnable_Type(TruthValue):
    """Custom type ctpPeripheralErrorNotifyEnable based on TruthValue"""


_CtpPeripheralErrorNotifyEnable_Object = MibScalar
ctpPeripheralErrorNotifyEnable = _CtpPeripheralErrorNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 1, 1),
    _CtpPeripheralErrorNotifyEnable_Type()
)
ctpPeripheralErrorNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpPeripheralErrorNotifyEnable.setStatus("deprecated")


class _CtpSysUserAuthFailNotifyEnable_Type(TruthValue):
    """Custom type ctpSysUserAuthFailNotifyEnable based on TruthValue"""


_CtpSysUserAuthFailNotifyEnable_Object = MibScalar
ctpSysUserAuthFailNotifyEnable = _CtpSysUserAuthFailNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 1, 2),
    _CtpSysUserAuthFailNotifyEnable_Type()
)
ctpSysUserAuthFailNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpSysUserAuthFailNotifyEnable.setStatus("current")


class _CtpSystemReset_Type(CtpSystemResetMode):
    """Custom type ctpSystemReset based on CtpSystemResetMode"""


_CtpSystemReset_Object = MibScalar
ctpSystemReset = _CtpSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 1, 3),
    _CtpSystemReset_Type()
)
ctpSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpSystemReset.setStatus("current")


class _CtpPeriStatusChangeNotifyEnable_Type(TruthValue):
    """Custom type ctpPeriStatusChangeNotifyEnable based on TruthValue"""


_CtpPeriStatusChangeNotifyEnable_Object = MibScalar
ctpPeriStatusChangeNotifyEnable = _CtpPeriStatusChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 1, 4),
    _CtpPeriStatusChangeNotifyEnable_Type()
)
ctpPeriStatusChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpPeriStatusChangeNotifyEnable.setStatus("current")
_CtpVlanId_Type = Unsigned32
_CtpVlanId_Object = MibScalar
ctpVlanId = _CtpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 1, 5),
    _CtpVlanId_Type()
)
ctpVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpVlanId.setStatus("current")
_CtpDefaultGatewayAddrType_Type = InetAddressType
_CtpDefaultGatewayAddrType_Object = MibScalar
ctpDefaultGatewayAddrType = _CtpDefaultGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 1, 6),
    _CtpDefaultGatewayAddrType_Type()
)
ctpDefaultGatewayAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpDefaultGatewayAddrType.setStatus("current")
_CtpDefaultGateway_Type = InetAddress
_CtpDefaultGateway_Object = MibScalar
ctpDefaultGateway = _CtpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 1, 7),
    _CtpDefaultGateway_Type()
)
ctpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpDefaultGateway.setStatus("current")
_CtpPeripheralStatusObjects_ObjectIdentity = ObjectIdentity
ctpPeripheralStatusObjects = _CtpPeripheralStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2)
)
_CtpPeripheralStatusTable_Object = MibTable
ctpPeripheralStatusTable = _CtpPeripheralStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ctpPeripheralStatusTable.setStatus("current")
_CtpPeripheralStatusEntry_Object = MibTableRow
ctpPeripheralStatusEntry = _CtpPeripheralStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 1, 1)
)
ctpPeripheralStatusEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralIndex"),
)
if mibBuilder.loadTexts:
    ctpPeripheralStatusEntry.setStatus("current")
_CtpPeripheralIndex_Type = Unsigned32
_CtpPeripheralIndex_Object = MibTableColumn
ctpPeripheralIndex = _CtpPeripheralIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 1, 1, 1),
    _CtpPeripheralIndex_Type()
)
ctpPeripheralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpPeripheralIndex.setStatus("current")


class _CtpPeripheralDescription_Type(SnmpAdminString):
    """Custom type ctpPeripheralDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtpPeripheralDescription_Type.__name__ = "SnmpAdminString"
_CtpPeripheralDescription_Object = MibTableColumn
ctpPeripheralDescription = _CtpPeripheralDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 1, 1, 2),
    _CtpPeripheralDescription_Type()
)
ctpPeripheralDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralDescription.setStatus("current")
_CtpPeripheralStatus_Type = CtpPeripheralStatusCode
_CtpPeripheralStatus_Object = MibTableColumn
ctpPeripheralStatus = _CtpPeripheralStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 1, 1, 3),
    _CtpPeripheralStatus_Type()
)
ctpPeripheralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralStatus.setStatus("current")
_CtpPeripheralDeviceCategory_Type = CtpPeripheralDeviceCategoryCode
_CtpPeripheralDeviceCategory_Object = MibTableColumn
ctpPeripheralDeviceCategory = _CtpPeripheralDeviceCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 1, 1, 4),
    _CtpPeripheralDeviceCategory_Type()
)
ctpPeripheralDeviceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralDeviceCategory.setStatus("current")
_CtpPeripheralDeviceNumber_Type = Unsigned32
_CtpPeripheralDeviceNumber_Object = MibTableColumn
ctpPeripheralDeviceNumber = _CtpPeripheralDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 1, 1, 5),
    _CtpPeripheralDeviceNumber_Type()
)
ctpPeripheralDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralDeviceNumber.setStatus("current")
_CtpEtherPeripheralStatusTable_Object = MibTable
ctpEtherPeripheralStatusTable = _CtpEtherPeripheralStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ctpEtherPeripheralStatusTable.setStatus("current")
_CtpEtherPeripheralStatusEntry_Object = MibTableRow
ctpEtherPeripheralStatusEntry = _CtpEtherPeripheralStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 2, 1)
)
ctpEtherPeripheralStatusEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralIndex"),
    (0, "CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralIndex"),
)
if mibBuilder.loadTexts:
    ctpEtherPeripheralStatusEntry.setStatus("current")
_CtpEtherPeripheralIndex_Type = Unsigned32
_CtpEtherPeripheralIndex_Object = MibTableColumn
ctpEtherPeripheralIndex = _CtpEtherPeripheralIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 2, 1, 1),
    _CtpEtherPeripheralIndex_Type()
)
ctpEtherPeripheralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpEtherPeripheralIndex.setStatus("current")
_CtpEtherPeripheralIfIndex_Type = InterfaceIndexOrZero
_CtpEtherPeripheralIfIndex_Object = MibTableColumn
ctpEtherPeripheralIfIndex = _CtpEtherPeripheralIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 2, 1, 2),
    _CtpEtherPeripheralIfIndex_Type()
)
ctpEtherPeripheralIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpEtherPeripheralIfIndex.setStatus("current")
_CtpEtherPeripheralAddrType_Type = InetAddressType
_CtpEtherPeripheralAddrType_Object = MibTableColumn
ctpEtherPeripheralAddrType = _CtpEtherPeripheralAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 2, 1, 3),
    _CtpEtherPeripheralAddrType_Type()
)
ctpEtherPeripheralAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpEtherPeripheralAddrType.setStatus("current")
_CtpEtherPeripheralAddr_Type = InetAddress
_CtpEtherPeripheralAddr_Object = MibTableColumn
ctpEtherPeripheralAddr = _CtpEtherPeripheralAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 2, 1, 4),
    _CtpEtherPeripheralAddr_Type()
)
ctpEtherPeripheralAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpEtherPeripheralAddr.setStatus("current")
_CtpEtherPeripheralStatus_Type = CtpPeripheralStatusCode
_CtpEtherPeripheralStatus_Object = MibTableColumn
ctpEtherPeripheralStatus = _CtpEtherPeripheralStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 2, 1, 5),
    _CtpEtherPeripheralStatus_Type()
)
ctpEtherPeripheralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpEtherPeripheralStatus.setStatus("current")
_CtpHDMIPeripheralStatusTable_Object = MibTable
ctpHDMIPeripheralStatusTable = _CtpHDMIPeripheralStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ctpHDMIPeripheralStatusTable.setStatus("current")
_CtpHDMIPeripheralStatusEntry_Object = MibTableRow
ctpHDMIPeripheralStatusEntry = _CtpHDMIPeripheralStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 3, 1)
)
ctpHDMIPeripheralStatusEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralIndex"),
    (0, "CISCO-TELEPRESENCE-MIB", "ctpHDMIPeripheralIndex"),
)
if mibBuilder.loadTexts:
    ctpHDMIPeripheralStatusEntry.setStatus("current")
_CtpHDMIPeripheralIndex_Type = Unsigned32
_CtpHDMIPeripheralIndex_Object = MibTableColumn
ctpHDMIPeripheralIndex = _CtpHDMIPeripheralIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 3, 1, 1),
    _CtpHDMIPeripheralIndex_Type()
)
ctpHDMIPeripheralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpHDMIPeripheralIndex.setStatus("current")
_CtpHDMIPeripheralCableStatus_Type = CtpPeripheralCableCode
_CtpHDMIPeripheralCableStatus_Object = MibTableColumn
ctpHDMIPeripheralCableStatus = _CtpHDMIPeripheralCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 3, 1, 2),
    _CtpHDMIPeripheralCableStatus_Type()
)
ctpHDMIPeripheralCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpHDMIPeripheralCableStatus.setStatus("current")
_CtpHDMIPeripheralPowerStatus_Type = CtpPeripheralPowerCode
_CtpHDMIPeripheralPowerStatus_Object = MibTableColumn
ctpHDMIPeripheralPowerStatus = _CtpHDMIPeripheralPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 3, 1, 3),
    _CtpHDMIPeripheralPowerStatus_Type()
)
ctpHDMIPeripheralPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpHDMIPeripheralPowerStatus.setStatus("current")
_CtpDVIPeripheralStatusTable_Object = MibTable
ctpDVIPeripheralStatusTable = _CtpDVIPeripheralStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ctpDVIPeripheralStatusTable.setStatus("current")
_CtpDVIPeripheralStatusEntry_Object = MibTableRow
ctpDVIPeripheralStatusEntry = _CtpDVIPeripheralStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 4, 1)
)
ctpDVIPeripheralStatusEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralIndex"),
    (0, "CISCO-TELEPRESENCE-MIB", "ctpDVIPeripheralIndex"),
)
if mibBuilder.loadTexts:
    ctpDVIPeripheralStatusEntry.setStatus("current")
_CtpDVIPeripheralIndex_Type = Unsigned32
_CtpDVIPeripheralIndex_Object = MibTableColumn
ctpDVIPeripheralIndex = _CtpDVIPeripheralIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 4, 1, 1),
    _CtpDVIPeripheralIndex_Type()
)
ctpDVIPeripheralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpDVIPeripheralIndex.setStatus("current")
_CtpDVIPeripheralCableStatus_Type = CtpPeripheralCableCode
_CtpDVIPeripheralCableStatus_Object = MibTableColumn
ctpDVIPeripheralCableStatus = _CtpDVIPeripheralCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 4, 1, 2),
    _CtpDVIPeripheralCableStatus_Type()
)
ctpDVIPeripheralCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpDVIPeripheralCableStatus.setStatus("current")
_CtpRS232PeripheralStatusTable_Object = MibTable
ctpRS232PeripheralStatusTable = _CtpRS232PeripheralStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ctpRS232PeripheralStatusTable.setStatus("current")
_CtpRS232PeripheralStatusEntry_Object = MibTableRow
ctpRS232PeripheralStatusEntry = _CtpRS232PeripheralStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 5, 1)
)
ctpRS232PeripheralStatusEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralIndex"),
    (0, "CISCO-TELEPRESENCE-MIB", "ctpRS232PeripheralIndex"),
)
if mibBuilder.loadTexts:
    ctpRS232PeripheralStatusEntry.setStatus("current")
_CtpRS232PeripheralIndex_Type = Unsigned32
_CtpRS232PeripheralIndex_Object = MibTableColumn
ctpRS232PeripheralIndex = _CtpRS232PeripheralIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 5, 1, 1),
    _CtpRS232PeripheralIndex_Type()
)
ctpRS232PeripheralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpRS232PeripheralIndex.setStatus("current")
_CtpRS232PortIndex_Type = InterfaceIndexOrZero
_CtpRS232PortIndex_Object = MibTableColumn
ctpRS232PortIndex = _CtpRS232PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 5, 1, 2),
    _CtpRS232PortIndex_Type()
)
ctpRS232PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpRS232PortIndex.setStatus("current")


class _CtpRS232PeripheralConnStatus_Type(Integer32):
    """Custom type ctpRS232PeripheralConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("unknown", 2))
    )


_CtpRS232PeripheralConnStatus_Type.__name__ = "Integer32"
_CtpRS232PeripheralConnStatus_Object = MibTableColumn
ctpRS232PeripheralConnStatus = _CtpRS232PeripheralConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 5, 1, 3),
    _CtpRS232PeripheralConnStatus_Type()
)
ctpRS232PeripheralConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpRS232PeripheralConnStatus.setStatus("current")
_CtpPeripheralAttributeTable_Object = MibTable
ctpPeripheralAttributeTable = _CtpPeripheralAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ctpPeripheralAttributeTable.setStatus("current")
_CtpPeripheralAttributeEntry_Object = MibTableRow
ctpPeripheralAttributeEntry = _CtpPeripheralAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 6, 1)
)
ctpPeripheralAttributeEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralIndex"),
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralAttributeIndex"),
)
if mibBuilder.loadTexts:
    ctpPeripheralAttributeEntry.setStatus("current")
_CtpPeripheralAttributeIndex_Type = Unsigned32
_CtpPeripheralAttributeIndex_Object = MibTableColumn
ctpPeripheralAttributeIndex = _CtpPeripheralAttributeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 6, 1, 1),
    _CtpPeripheralAttributeIndex_Type()
)
ctpPeripheralAttributeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpPeripheralAttributeIndex.setStatus("current")


class _CtpPeripheralAttributeDescr_Type(Integer32):
    """Custom type ctpPeripheralAttributeDescr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lampOperTime", 1),
          ("lampState", 2),
          ("powerSwitchState", 3))
    )


_CtpPeripheralAttributeDescr_Type.__name__ = "Integer32"
_CtpPeripheralAttributeDescr_Object = MibTableColumn
ctpPeripheralAttributeDescr = _CtpPeripheralAttributeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 6, 1, 2),
    _CtpPeripheralAttributeDescr_Type()
)
ctpPeripheralAttributeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralAttributeDescr.setStatus("current")
_CtpPeripheralAttributeValue_Type = Unsigned32
_CtpPeripheralAttributeValue_Object = MibTableColumn
ctpPeripheralAttributeValue = _CtpPeripheralAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 6, 1, 3),
    _CtpPeripheralAttributeValue_Type()
)
ctpPeripheralAttributeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralAttributeValue.setStatus("current")
_CtpUSBPeripheralStatusTable_Object = MibTable
ctpUSBPeripheralStatusTable = _CtpUSBPeripheralStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ctpUSBPeripheralStatusTable.setStatus("current")
_CtpUSBPeripheralStatusEntry_Object = MibTableRow
ctpUSBPeripheralStatusEntry = _CtpUSBPeripheralStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 7, 1)
)
ctpUSBPeripheralStatusEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralIndex"),
    (0, "CISCO-TELEPRESENCE-MIB", "ctpUSBPeripheralIndex"),
)
if mibBuilder.loadTexts:
    ctpUSBPeripheralStatusEntry.setStatus("current")
_CtpUSBPeripheralIndex_Type = Unsigned32
_CtpUSBPeripheralIndex_Object = MibTableColumn
ctpUSBPeripheralIndex = _CtpUSBPeripheralIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 7, 1, 1),
    _CtpUSBPeripheralIndex_Type()
)
ctpUSBPeripheralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpUSBPeripheralIndex.setStatus("current")
_CtpUSBPeripheralCableStatus_Type = CtpPeripheralCableCode
_CtpUSBPeripheralCableStatus_Object = MibTableColumn
ctpUSBPeripheralCableStatus = _CtpUSBPeripheralCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 7, 1, 2),
    _CtpUSBPeripheralCableStatus_Type()
)
ctpUSBPeripheralCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpUSBPeripheralCableStatus.setStatus("current")


class _CtpUSBPeripheralPowerStatus_Type(Integer32):
    """Custom type ctpUSBPeripheralPowerStatus based on Integer32"""
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
        *(("both", 4),
          ("bus", 3),
          ("self", 2),
          ("unknown", 1))
    )


_CtpUSBPeripheralPowerStatus_Type.__name__ = "Integer32"
_CtpUSBPeripheralPowerStatus_Object = MibTableColumn
ctpUSBPeripheralPowerStatus = _CtpUSBPeripheralPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 7, 1, 3),
    _CtpUSBPeripheralPowerStatus_Type()
)
ctpUSBPeripheralPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpUSBPeripheralPowerStatus.setStatus("current")


class _CtpUSBPeripheralPortType_Type(Integer32):
    """Custom type ctpUSBPeripheralPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("device", 2),
          ("host", 1),
          ("hub", 3))
    )


_CtpUSBPeripheralPortType_Type.__name__ = "Integer32"
_CtpUSBPeripheralPortType_Object = MibTableColumn
ctpUSBPeripheralPortType = _CtpUSBPeripheralPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 7, 1, 4),
    _CtpUSBPeripheralPortType_Type()
)
ctpUSBPeripheralPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpUSBPeripheralPortType.setStatus("current")


class _CtpUSBPeripheralPortRate_Type(Integer32):
    """Custom type ctpUSBPeripheralPortRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("high", 3),
          ("low", 1))
    )


_CtpUSBPeripheralPortRate_Type.__name__ = "Integer32"
_CtpUSBPeripheralPortRate_Object = MibTableColumn
ctpUSBPeripheralPortRate = _CtpUSBPeripheralPortRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 7, 1, 5),
    _CtpUSBPeripheralPortRate_Type()
)
ctpUSBPeripheralPortRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpUSBPeripheralPortRate.setStatus("current")
_Ctp802dot11PeripheralStatusTable_Object = MibTable
ctp802dot11PeripheralStatusTable = _Ctp802dot11PeripheralStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ctp802dot11PeripheralStatusTable.setStatus("current")
_Ctp802dot11PeripheralStatusEntry_Object = MibTableRow
ctp802dot11PeripheralStatusEntry = _Ctp802dot11PeripheralStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 8, 1)
)
ctp802dot11PeripheralStatusEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralIndex"),
    (0, "CISCO-TELEPRESENCE-MIB", "ctp802dot11PeripheralIndex"),
)
if mibBuilder.loadTexts:
    ctp802dot11PeripheralStatusEntry.setStatus("current")
_Ctp802dot11PeripheralIndex_Type = Unsigned32
_Ctp802dot11PeripheralIndex_Object = MibTableColumn
ctp802dot11PeripheralIndex = _Ctp802dot11PeripheralIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 8, 1, 1),
    _Ctp802dot11PeripheralIndex_Type()
)
ctp802dot11PeripheralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctp802dot11PeripheralIndex.setStatus("current")
_Ctp802dot11PeripheralIfIndex_Type = InterfaceIndexOrZero
_Ctp802dot11PeripheralIfIndex_Object = MibTableColumn
ctp802dot11PeripheralIfIndex = _Ctp802dot11PeripheralIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 8, 1, 2),
    _Ctp802dot11PeripheralIfIndex_Type()
)
ctp802dot11PeripheralIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctp802dot11PeripheralIfIndex.setStatus("current")
_Ctp802dot11PeripheralAddrType_Type = InetAddressType
_Ctp802dot11PeripheralAddrType_Object = MibTableColumn
ctp802dot11PeripheralAddrType = _Ctp802dot11PeripheralAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 8, 1, 3),
    _Ctp802dot11PeripheralAddrType_Type()
)
ctp802dot11PeripheralAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctp802dot11PeripheralAddrType.setStatus("current")
_Ctp802dot11PeripheralAddr_Type = InetAddress
_Ctp802dot11PeripheralAddr_Object = MibTableColumn
ctp802dot11PeripheralAddr = _Ctp802dot11PeripheralAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 8, 1, 4),
    _Ctp802dot11PeripheralAddr_Type()
)
ctp802dot11PeripheralAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctp802dot11PeripheralAddr.setStatus("current")
_Ctp802dot11PeripheralLinkStrength_Type = Unsigned32
_Ctp802dot11PeripheralLinkStrength_Object = MibTableColumn
ctp802dot11PeripheralLinkStrength = _Ctp802dot11PeripheralLinkStrength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 8, 1, 5),
    _Ctp802dot11PeripheralLinkStrength_Type()
)
ctp802dot11PeripheralLinkStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctp802dot11PeripheralLinkStrength.setStatus("current")
_Ctp802dot11PeripheralLinkStatus_Type = CtpPeripheralCableCode
_Ctp802dot11PeripheralLinkStatus_Object = MibTableColumn
ctp802dot11PeripheralLinkStatus = _Ctp802dot11PeripheralLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 8, 1, 6),
    _Ctp802dot11PeripheralLinkStatus_Type()
)
ctp802dot11PeripheralLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctp802dot11PeripheralLinkStatus.setStatus("current")
_CtpDPPeripheralStatusTable_Object = MibTable
ctpDPPeripheralStatusTable = _CtpDPPeripheralStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 9)
)
if mibBuilder.loadTexts:
    ctpDPPeripheralStatusTable.setStatus("current")
_CtpDPPeripheralStatusEntry_Object = MibTableRow
ctpDPPeripheralStatusEntry = _CtpDPPeripheralStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 9, 1)
)
ctpDPPeripheralStatusEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralIndex"),
    (0, "CISCO-TELEPRESENCE-MIB", "ctpDPPeripheralIndex"),
)
if mibBuilder.loadTexts:
    ctpDPPeripheralStatusEntry.setStatus("current")
_CtpDPPeripheralIndex_Type = Unsigned32
_CtpDPPeripheralIndex_Object = MibTableColumn
ctpDPPeripheralIndex = _CtpDPPeripheralIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 9, 1, 1),
    _CtpDPPeripheralIndex_Type()
)
ctpDPPeripheralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpDPPeripheralIndex.setStatus("current")
_CtpDPPeripheralCableStatus_Type = CtpPeripheralCableCode
_CtpDPPeripheralCableStatus_Object = MibTableColumn
ctpDPPeripheralCableStatus = _CtpDPPeripheralCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 9, 1, 2),
    _CtpDPPeripheralCableStatus_Type()
)
ctpDPPeripheralCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpDPPeripheralCableStatus.setStatus("current")
_CtpDPPeripheralPowerStatus_Type = CtpPeripheralPowerCode
_CtpDPPeripheralPowerStatus_Object = MibTableColumn
ctpDPPeripheralPowerStatus = _CtpDPPeripheralPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 2, 9, 1, 3),
    _CtpDPPeripheralPowerStatus_Type()
)
ctpDPPeripheralPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpDPPeripheralPowerStatus.setStatus("current")
_CtpEventHistory_ObjectIdentity = ObjectIdentity
ctpEventHistory = _CtpEventHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3)
)


class _CtpPeripheralErrorHistTableSize_Type(Unsigned32):
    """Custom type ctpPeripheralErrorHistTableSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CtpPeripheralErrorHistTableSize_Type.__name__ = "Unsigned32"
_CtpPeripheralErrorHistTableSize_Object = MibScalar
ctpPeripheralErrorHistTableSize = _CtpPeripheralErrorHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 1),
    _CtpPeripheralErrorHistTableSize_Type()
)
ctpPeripheralErrorHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpPeripheralErrorHistTableSize.setStatus("current")


class _CtpPeripheralErrorHistLastIndex_Type(Unsigned32):
    """Custom type ctpPeripheralErrorHistLastIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CtpPeripheralErrorHistLastIndex_Type.__name__ = "Unsigned32"
_CtpPeripheralErrorHistLastIndex_Object = MibScalar
ctpPeripheralErrorHistLastIndex = _CtpPeripheralErrorHistLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 2),
    _CtpPeripheralErrorHistLastIndex_Type()
)
ctpPeripheralErrorHistLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralErrorHistLastIndex.setStatus("current")
_CtpPeripheralErrorHistoryTable_Object = MibTable
ctpPeripheralErrorHistoryTable = _CtpPeripheralErrorHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ctpPeripheralErrorHistoryTable.setStatus("current")
_CtpPeripheralErrorHistoryEntry_Object = MibTableRow
ctpPeripheralErrorHistoryEntry = _CtpPeripheralErrorHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 3, 1)
)
ctpPeripheralErrorHistoryEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorHistoryIndex"),
)
if mibBuilder.loadTexts:
    ctpPeripheralErrorHistoryEntry.setStatus("current")


class _CtpPeripheralErrorHistoryIndex_Type(Unsigned32):
    """Custom type ctpPeripheralErrorHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CtpPeripheralErrorHistoryIndex_Type.__name__ = "Unsigned32"
_CtpPeripheralErrorHistoryIndex_Object = MibTableColumn
ctpPeripheralErrorHistoryIndex = _CtpPeripheralErrorHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 3, 1, 1),
    _CtpPeripheralErrorHistoryIndex_Type()
)
ctpPeripheralErrorHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpPeripheralErrorHistoryIndex.setStatus("current")
_CtpPeripheralErrorIndex_Type = Unsigned32
_CtpPeripheralErrorIndex_Object = MibTableColumn
ctpPeripheralErrorIndex = _CtpPeripheralErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 3, 1, 2),
    _CtpPeripheralErrorIndex_Type()
)
ctpPeripheralErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralErrorIndex.setStatus("current")
_CtpPeripheralErrorStatus_Type = CtpPeripheralStatusCode
_CtpPeripheralErrorStatus_Object = MibTableColumn
ctpPeripheralErrorStatus = _CtpPeripheralErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 3, 1, 3),
    _CtpPeripheralErrorStatus_Type()
)
ctpPeripheralErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralErrorStatus.setStatus("current")
_CtpPeripheralErrorTimeStamp_Type = TimeStamp
_CtpPeripheralErrorTimeStamp_Object = MibTableColumn
ctpPeripheralErrorTimeStamp = _CtpPeripheralErrorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 3, 1, 4),
    _CtpPeripheralErrorTimeStamp_Type()
)
ctpPeripheralErrorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralErrorTimeStamp.setStatus("current")
_CtpPeripheralErrorDeviceCategory_Type = CtpPeripheralDeviceCategoryCode
_CtpPeripheralErrorDeviceCategory_Object = MibTableColumn
ctpPeripheralErrorDeviceCategory = _CtpPeripheralErrorDeviceCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 3, 1, 5),
    _CtpPeripheralErrorDeviceCategory_Type()
)
ctpPeripheralErrorDeviceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralErrorDeviceCategory.setStatus("current")
_CtpPeripheralErrorDeviceNumber_Type = Unsigned32
_CtpPeripheralErrorDeviceNumber_Object = MibTableColumn
ctpPeripheralErrorDeviceNumber = _CtpPeripheralErrorDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 3, 1, 6),
    _CtpPeripheralErrorDeviceNumber_Type()
)
ctpPeripheralErrorDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpPeripheralErrorDeviceNumber.setStatus("current")


class _CtpSysUserAuthFailHistTableSize_Type(Unsigned32):
    """Custom type ctpSysUserAuthFailHistTableSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CtpSysUserAuthFailHistTableSize_Type.__name__ = "Unsigned32"
_CtpSysUserAuthFailHistTableSize_Object = MibScalar
ctpSysUserAuthFailHistTableSize = _CtpSysUserAuthFailHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 4),
    _CtpSysUserAuthFailHistTableSize_Type()
)
ctpSysUserAuthFailHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpSysUserAuthFailHistTableSize.setStatus("current")


class _CtpSysUserAuthFailHistLastIndex_Type(Unsigned32):
    """Custom type ctpSysUserAuthFailHistLastIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CtpSysUserAuthFailHistLastIndex_Type.__name__ = "Unsigned32"
_CtpSysUserAuthFailHistLastIndex_Object = MibScalar
ctpSysUserAuthFailHistLastIndex = _CtpSysUserAuthFailHistLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 5),
    _CtpSysUserAuthFailHistLastIndex_Type()
)
ctpSysUserAuthFailHistLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpSysUserAuthFailHistLastIndex.setStatus("current")
_CtpSysUserAuthFailHistoryTable_Object = MibTable
ctpSysUserAuthFailHistoryTable = _CtpSysUserAuthFailHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 6)
)
if mibBuilder.loadTexts:
    ctpSysUserAuthFailHistoryTable.setStatus("current")
_CtpSysUserAuthFailHistoryEntry_Object = MibTableRow
ctpSysUserAuthFailHistoryEntry = _CtpSysUserAuthFailHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 6, 1)
)
ctpSysUserAuthFailHistoryEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailHistoryIndex"),
)
if mibBuilder.loadTexts:
    ctpSysUserAuthFailHistoryEntry.setStatus("current")


class _CtpSysUserAuthFailHistoryIndex_Type(Unsigned32):
    """Custom type ctpSysUserAuthFailHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CtpSysUserAuthFailHistoryIndex_Type.__name__ = "Unsigned32"
_CtpSysUserAuthFailHistoryIndex_Object = MibTableColumn
ctpSysUserAuthFailHistoryIndex = _CtpSysUserAuthFailHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 6, 1, 1),
    _CtpSysUserAuthFailHistoryIndex_Type()
)
ctpSysUserAuthFailHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpSysUserAuthFailHistoryIndex.setStatus("current")
_CtpSysUserAuthFailSourceAddrType_Type = InetAddressType
_CtpSysUserAuthFailSourceAddrType_Object = MibTableColumn
ctpSysUserAuthFailSourceAddrType = _CtpSysUserAuthFailSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 6, 1, 2),
    _CtpSysUserAuthFailSourceAddrType_Type()
)
ctpSysUserAuthFailSourceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpSysUserAuthFailSourceAddrType.setStatus("current")
_CtpSysUserAuthFailSourceAddr_Type = InetAddress
_CtpSysUserAuthFailSourceAddr_Object = MibTableColumn
ctpSysUserAuthFailSourceAddr = _CtpSysUserAuthFailSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 6, 1, 3),
    _CtpSysUserAuthFailSourceAddr_Type()
)
ctpSysUserAuthFailSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpSysUserAuthFailSourceAddr.setStatus("current")
_CtpSysUserAuthFailSourcePort_Type = Unsigned32
_CtpSysUserAuthFailSourcePort_Object = MibTableColumn
ctpSysUserAuthFailSourcePort = _CtpSysUserAuthFailSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 6, 1, 4),
    _CtpSysUserAuthFailSourcePort_Type()
)
ctpSysUserAuthFailSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpSysUserAuthFailSourcePort.setStatus("current")


class _CtpSysUserAuthFailUserName_Type(SnmpAdminString):
    """Custom type ctpSysUserAuthFailUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CtpSysUserAuthFailUserName_Type.__name__ = "SnmpAdminString"
_CtpSysUserAuthFailUserName_Object = MibTableColumn
ctpSysUserAuthFailUserName = _CtpSysUserAuthFailUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 6, 1, 5),
    _CtpSysUserAuthFailUserName_Type()
)
ctpSysUserAuthFailUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpSysUserAuthFailUserName.setStatus("current")
_CtpSysUserAuthFailAccessProtocol_Type = CtpSystemAccessProtocol
_CtpSysUserAuthFailAccessProtocol_Object = MibTableColumn
ctpSysUserAuthFailAccessProtocol = _CtpSysUserAuthFailAccessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 6, 1, 6),
    _CtpSysUserAuthFailAccessProtocol_Type()
)
ctpSysUserAuthFailAccessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpSysUserAuthFailAccessProtocol.setStatus("current")
_CtpSysUserAuthFailTimeStamp_Type = TimeStamp
_CtpSysUserAuthFailTimeStamp_Object = MibTableColumn
ctpSysUserAuthFailTimeStamp = _CtpSysUserAuthFailTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 1, 3, 6, 1, 7),
    _CtpSysUserAuthFailTimeStamp_Type()
)
ctpSysUserAuthFailTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpSysUserAuthFailTimeStamp.setStatus("current")
_CiscoTelepresenceMIBConform_ObjectIdentity = ObjectIdentity
ciscoTelepresenceMIBConform = _CiscoTelepresenceMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2)
)
_CiscoTelepresenceCompliances_ObjectIdentity = ObjectIdentity
ciscoTelepresenceCompliances = _CiscoTelepresenceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 1)
)
_CiscoTelepresenceMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTelepresenceMIBGroups = _CiscoTelepresenceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2)
)

# Managed Objects groups

ciscoTpConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 1)
)
ciscoTpConfigurationGroup.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorNotifyEnable"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailNotifyEnable"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSystemReset"))
)
if mibBuilder.loadTexts:
    ciscoTpConfigurationGroup.setStatus("deprecated")

ciscoTpPeripheralStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 2)
)
ciscoTpPeripheralStatusGroup.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeripheralDescription"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralIfIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralAddrType"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralAddr"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpHDMIPeripheralCableStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpHDMIPeripheralPowerStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpDVIPeripheralCableStatus"))
)
if mibBuilder.loadTexts:
    ciscoTpPeripheralStatusGroup.setStatus("deprecated")

ciscoTpEventHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 3)
)
ciscoTpEventHistoryGroup.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorHistTableSize"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorHistLastIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorTimeStamp"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailHistTableSize"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailHistLastIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailSourceAddrType"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailSourceAddr"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailSourcePort"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailUserName"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailAccessProtocol"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoTpEventHistoryGroup.setStatus("deprecated")

ciscoTpRS232PeripheralStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 5)
)
ciscoTpRS232PeripheralStatusGroup.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpRS232PortIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpRS232PeripheralConnStatus"))
)
if mibBuilder.loadTexts:
    ciscoTpRS232PeripheralStatusGroup.setStatus("current")

ciscoTpPeripheralAttributeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 6)
)
ciscoTpPeripheralAttributeGroup.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeripheralAttributeDescr"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralAttributeValue"))
)
if mibBuilder.loadTexts:
    ciscoTpPeripheralAttributeGroup.setStatus("current")

ciscoTpPeripheralStatusGroupR01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 7)
)
ciscoTpPeripheralStatusGroupR01.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeripheralDescription"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralDeviceCategory"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralDeviceNumber"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralIfIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralAddrType"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralAddr"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpHDMIPeripheralCableStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpHDMIPeripheralPowerStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpDVIPeripheralCableStatus"))
)
if mibBuilder.loadTexts:
    ciscoTpPeripheralStatusGroupR01.setStatus("deprecated")

ciscoTpEventHistoryGroupR01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 8)
)
ciscoTpEventHistoryGroupR01.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorHistTableSize"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorHistLastIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorTimeStamp"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorDeviceCategory"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorDeviceNumber"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailHistTableSize"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailHistLastIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailSourceAddrType"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailSourceAddr"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailSourcePort"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailUserName"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailAccessProtocol"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoTpEventHistoryGroupR01.setStatus("current")

ciscoTpConfigurationGroupR01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 10)
)
ciscoTpConfigurationGroupR01.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailNotifyEnable"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSystemReset"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeriStatusChangeNotifyEnable"))
)
if mibBuilder.loadTexts:
    ciscoTpConfigurationGroupR01.setStatus("current")

ciscoTpPeripheralStatusGroupR02 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 11)
)
ciscoTpPeripheralStatusGroupR02.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeripheralDescription"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralDeviceCategory"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralDeviceNumber"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralIfIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralAddrType"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralAddr"),
        ("CISCO-TELEPRESENCE-MIB", "ctpEtherPeripheralStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpHDMIPeripheralCableStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpHDMIPeripheralPowerStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpDVIPeripheralCableStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpUSBPeripheralCableStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpUSBPeripheralPowerStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpUSBPeripheralPortType"),
        ("CISCO-TELEPRESENCE-MIB", "ctpUSBPeripheralPortRate"),
        ("CISCO-TELEPRESENCE-MIB", "ctp802dot11PeripheralIfIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctp802dot11PeripheralAddrType"),
        ("CISCO-TELEPRESENCE-MIB", "ctp802dot11PeripheralAddr"),
        ("CISCO-TELEPRESENCE-MIB", "ctp802dot11PeripheralLinkStrength"),
        ("CISCO-TELEPRESENCE-MIB", "ctp802dot11PeripheralLinkStatus"))
)
if mibBuilder.loadTexts:
    ciscoTpPeripheralStatusGroupR02.setStatus("current")

ciscoTpConfigurationGroupR02 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 12)
)
ciscoTpConfigurationGroupR02.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpVlanId"),
        ("CISCO-TELEPRESENCE-MIB", "ctpDefaultGateway"),
        ("CISCO-TELEPRESENCE-MIB", "ctpDefaultGatewayAddrType"))
)
if mibBuilder.loadTexts:
    ciscoTpConfigurationGroupR02.setStatus("current")

ciscoTpDPPeripheralStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 13)
)
ciscoTpDPPeripheralStatusGroup.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpDPPeripheralCableStatus"),
        ("CISCO-TELEPRESENCE-MIB", "ctpDPPeripheralPowerStatus"))
)
if mibBuilder.loadTexts:
    ciscoTpDPPeripheralStatusGroup.setStatus("current")


# Notification objects

ctpPeripheralErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 0, 1)
)
ctpPeripheralErrorNotification.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorStatus"))
)
if mibBuilder.loadTexts:
    ctpPeripheralErrorNotification.setStatus(
        "deprecated"
    )

ctpSysUserAuthFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 0, 2)
)
ctpSysUserAuthFailNotification.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailSourceAddrType"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailSourceAddr"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailSourcePort"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailUserName"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailAccessProtocol"))
)
if mibBuilder.loadTexts:
    ctpSysUserAuthFailNotification.setStatus(
        "current"
    )

ctpPeriStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 0, 3)
)
ctpPeriStatusChangeNotification.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorIndex"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorDeviceCategory"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorDeviceNumber"),
        ("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorStatus"))
)
if mibBuilder.loadTexts:
    ctpPeriStatusChangeNotification.setStatus(
        "current"
    )


# Notifications groups

ciscoTpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 4)
)
ciscoTpNotificationGroup.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeripheralErrorNotification"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailNotification"))
)
if mibBuilder.loadTexts:
    ciscoTpNotificationGroup.setStatus(
        "deprecated"
    )

ciscoTpNotificationGroupR01 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 2, 9)
)
ciscoTpNotificationGroupR01.setObjects(
      *(("CISCO-TELEPRESENCE-MIB", "ctpPeriStatusChangeNotification"),
        ("CISCO-TELEPRESENCE-MIB", "ctpSysUserAuthFailNotification"))
)
if mibBuilder.loadTexts:
    ciscoTpNotificationGroupR01.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTelepresenceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTelepresenceCompliance.setStatus(
        "deprecated"
    )

ciscoTelepresenceComplianceR01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoTelepresenceComplianceR01.setStatus(
        "deprecated"
    )

ciscoTelepresenceComplianceR02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoTelepresenceComplianceR02.setStatus(
        "deprecated"
    )

ciscoTelepresenceComplianceR03 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoTelepresenceComplianceR03.setStatus(
        "deprecated"
    )

ciscoTelepresenceComplianceR04 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoTelepresenceComplianceR04.setStatus(
        "deprecated"
    )

ciscoTelepresenceComplianceR05 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 643, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoTelepresenceComplianceR05.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TELEPRESENCE-MIB",
    **{"CtpSystemResetMode": CtpSystemResetMode,
       "CtpPeripheralCableCode": CtpPeripheralCableCode,
       "CtpPeripheralPowerCode": CtpPeripheralPowerCode,
       "CtpPeripheralStatusCode": CtpPeripheralStatusCode,
       "CtpSystemAccessProtocol": CtpSystemAccessProtocol,
       "CtpPeripheralDeviceCategoryCode": CtpPeripheralDeviceCategoryCode,
       "ciscoTelepresenceMIB": ciscoTelepresenceMIB,
       "ciscoTelepresenceMIBNotifs": ciscoTelepresenceMIBNotifs,
       "ctpPeripheralErrorNotification": ctpPeripheralErrorNotification,
       "ctpSysUserAuthFailNotification": ctpSysUserAuthFailNotification,
       "ctpPeriStatusChangeNotification": ctpPeriStatusChangeNotification,
       "ciscoTelepresenceMIBObjects": ciscoTelepresenceMIBObjects,
       "ctpObjects": ctpObjects,
       "ctpPeripheralErrorNotifyEnable": ctpPeripheralErrorNotifyEnable,
       "ctpSysUserAuthFailNotifyEnable": ctpSysUserAuthFailNotifyEnable,
       "ctpSystemReset": ctpSystemReset,
       "ctpPeriStatusChangeNotifyEnable": ctpPeriStatusChangeNotifyEnable,
       "ctpVlanId": ctpVlanId,
       "ctpDefaultGatewayAddrType": ctpDefaultGatewayAddrType,
       "ctpDefaultGateway": ctpDefaultGateway,
       "ctpPeripheralStatusObjects": ctpPeripheralStatusObjects,
       "ctpPeripheralStatusTable": ctpPeripheralStatusTable,
       "ctpPeripheralStatusEntry": ctpPeripheralStatusEntry,
       "ctpPeripheralIndex": ctpPeripheralIndex,
       "ctpPeripheralDescription": ctpPeripheralDescription,
       "ctpPeripheralStatus": ctpPeripheralStatus,
       "ctpPeripheralDeviceCategory": ctpPeripheralDeviceCategory,
       "ctpPeripheralDeviceNumber": ctpPeripheralDeviceNumber,
       "ctpEtherPeripheralStatusTable": ctpEtherPeripheralStatusTable,
       "ctpEtherPeripheralStatusEntry": ctpEtherPeripheralStatusEntry,
       "ctpEtherPeripheralIndex": ctpEtherPeripheralIndex,
       "ctpEtherPeripheralIfIndex": ctpEtherPeripheralIfIndex,
       "ctpEtherPeripheralAddrType": ctpEtherPeripheralAddrType,
       "ctpEtherPeripheralAddr": ctpEtherPeripheralAddr,
       "ctpEtherPeripheralStatus": ctpEtherPeripheralStatus,
       "ctpHDMIPeripheralStatusTable": ctpHDMIPeripheralStatusTable,
       "ctpHDMIPeripheralStatusEntry": ctpHDMIPeripheralStatusEntry,
       "ctpHDMIPeripheralIndex": ctpHDMIPeripheralIndex,
       "ctpHDMIPeripheralCableStatus": ctpHDMIPeripheralCableStatus,
       "ctpHDMIPeripheralPowerStatus": ctpHDMIPeripheralPowerStatus,
       "ctpDVIPeripheralStatusTable": ctpDVIPeripheralStatusTable,
       "ctpDVIPeripheralStatusEntry": ctpDVIPeripheralStatusEntry,
       "ctpDVIPeripheralIndex": ctpDVIPeripheralIndex,
       "ctpDVIPeripheralCableStatus": ctpDVIPeripheralCableStatus,
       "ctpRS232PeripheralStatusTable": ctpRS232PeripheralStatusTable,
       "ctpRS232PeripheralStatusEntry": ctpRS232PeripheralStatusEntry,
       "ctpRS232PeripheralIndex": ctpRS232PeripheralIndex,
       "ctpRS232PortIndex": ctpRS232PortIndex,
       "ctpRS232PeripheralConnStatus": ctpRS232PeripheralConnStatus,
       "ctpPeripheralAttributeTable": ctpPeripheralAttributeTable,
       "ctpPeripheralAttributeEntry": ctpPeripheralAttributeEntry,
       "ctpPeripheralAttributeIndex": ctpPeripheralAttributeIndex,
       "ctpPeripheralAttributeDescr": ctpPeripheralAttributeDescr,
       "ctpPeripheralAttributeValue": ctpPeripheralAttributeValue,
       "ctpUSBPeripheralStatusTable": ctpUSBPeripheralStatusTable,
       "ctpUSBPeripheralStatusEntry": ctpUSBPeripheralStatusEntry,
       "ctpUSBPeripheralIndex": ctpUSBPeripheralIndex,
       "ctpUSBPeripheralCableStatus": ctpUSBPeripheralCableStatus,
       "ctpUSBPeripheralPowerStatus": ctpUSBPeripheralPowerStatus,
       "ctpUSBPeripheralPortType": ctpUSBPeripheralPortType,
       "ctpUSBPeripheralPortRate": ctpUSBPeripheralPortRate,
       "ctp802dot11PeripheralStatusTable": ctp802dot11PeripheralStatusTable,
       "ctp802dot11PeripheralStatusEntry": ctp802dot11PeripheralStatusEntry,
       "ctp802dot11PeripheralIndex": ctp802dot11PeripheralIndex,
       "ctp802dot11PeripheralIfIndex": ctp802dot11PeripheralIfIndex,
       "ctp802dot11PeripheralAddrType": ctp802dot11PeripheralAddrType,
       "ctp802dot11PeripheralAddr": ctp802dot11PeripheralAddr,
       "ctp802dot11PeripheralLinkStrength": ctp802dot11PeripheralLinkStrength,
       "ctp802dot11PeripheralLinkStatus": ctp802dot11PeripheralLinkStatus,
       "ctpDPPeripheralStatusTable": ctpDPPeripheralStatusTable,
       "ctpDPPeripheralStatusEntry": ctpDPPeripheralStatusEntry,
       "ctpDPPeripheralIndex": ctpDPPeripheralIndex,
       "ctpDPPeripheralCableStatus": ctpDPPeripheralCableStatus,
       "ctpDPPeripheralPowerStatus": ctpDPPeripheralPowerStatus,
       "ctpEventHistory": ctpEventHistory,
       "ctpPeripheralErrorHistTableSize": ctpPeripheralErrorHistTableSize,
       "ctpPeripheralErrorHistLastIndex": ctpPeripheralErrorHistLastIndex,
       "ctpPeripheralErrorHistoryTable": ctpPeripheralErrorHistoryTable,
       "ctpPeripheralErrorHistoryEntry": ctpPeripheralErrorHistoryEntry,
       "ctpPeripheralErrorHistoryIndex": ctpPeripheralErrorHistoryIndex,
       "ctpPeripheralErrorIndex": ctpPeripheralErrorIndex,
       "ctpPeripheralErrorStatus": ctpPeripheralErrorStatus,
       "ctpPeripheralErrorTimeStamp": ctpPeripheralErrorTimeStamp,
       "ctpPeripheralErrorDeviceCategory": ctpPeripheralErrorDeviceCategory,
       "ctpPeripheralErrorDeviceNumber": ctpPeripheralErrorDeviceNumber,
       "ctpSysUserAuthFailHistTableSize": ctpSysUserAuthFailHistTableSize,
       "ctpSysUserAuthFailHistLastIndex": ctpSysUserAuthFailHistLastIndex,
       "ctpSysUserAuthFailHistoryTable": ctpSysUserAuthFailHistoryTable,
       "ctpSysUserAuthFailHistoryEntry": ctpSysUserAuthFailHistoryEntry,
       "ctpSysUserAuthFailHistoryIndex": ctpSysUserAuthFailHistoryIndex,
       "ctpSysUserAuthFailSourceAddrType": ctpSysUserAuthFailSourceAddrType,
       "ctpSysUserAuthFailSourceAddr": ctpSysUserAuthFailSourceAddr,
       "ctpSysUserAuthFailSourcePort": ctpSysUserAuthFailSourcePort,
       "ctpSysUserAuthFailUserName": ctpSysUserAuthFailUserName,
       "ctpSysUserAuthFailAccessProtocol": ctpSysUserAuthFailAccessProtocol,
       "ctpSysUserAuthFailTimeStamp": ctpSysUserAuthFailTimeStamp,
       "ciscoTelepresenceMIBConform": ciscoTelepresenceMIBConform,
       "ciscoTelepresenceCompliances": ciscoTelepresenceCompliances,
       "ciscoTelepresenceCompliance": ciscoTelepresenceCompliance,
       "ciscoTelepresenceComplianceR01": ciscoTelepresenceComplianceR01,
       "ciscoTelepresenceComplianceR02": ciscoTelepresenceComplianceR02,
       "ciscoTelepresenceComplianceR03": ciscoTelepresenceComplianceR03,
       "ciscoTelepresenceComplianceR04": ciscoTelepresenceComplianceR04,
       "ciscoTelepresenceComplianceR05": ciscoTelepresenceComplianceR05,
       "ciscoTelepresenceMIBGroups": ciscoTelepresenceMIBGroups,
       "ciscoTpConfigurationGroup": ciscoTpConfigurationGroup,
       "ciscoTpPeripheralStatusGroup": ciscoTpPeripheralStatusGroup,
       "ciscoTpEventHistoryGroup": ciscoTpEventHistoryGroup,
       "ciscoTpNotificationGroup": ciscoTpNotificationGroup,
       "ciscoTpRS232PeripheralStatusGroup": ciscoTpRS232PeripheralStatusGroup,
       "ciscoTpPeripheralAttributeGroup": ciscoTpPeripheralAttributeGroup,
       "ciscoTpPeripheralStatusGroupR01": ciscoTpPeripheralStatusGroupR01,
       "ciscoTpEventHistoryGroupR01": ciscoTpEventHistoryGroupR01,
       "ciscoTpNotificationGroupR01": ciscoTpNotificationGroupR01,
       "ciscoTpConfigurationGroupR01": ciscoTpConfigurationGroupR01,
       "ciscoTpPeripheralStatusGroupR02": ciscoTpPeripheralStatusGroupR02,
       "ciscoTpConfigurationGroupR02": ciscoTpConfigurationGroupR02,
       "ciscoTpDPPeripheralStatusGroup": ciscoTpDPPeripheralStatusGroup}
)
