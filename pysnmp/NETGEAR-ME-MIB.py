# SNMP MIB module (NETGEAR-ME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETGEAR-ME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:02 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netgear_ObjectIdentity = ObjectIdentity
netgear = _Netgear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526)
)
_WirelessProducts_ObjectIdentity = ObjectIdentity
wirelessProducts = _WirelessProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4)
)
_WirelessAccessPointDev_ObjectIdentity = ObjectIdentity
wirelessAccessPointDev = _WirelessAccessPointDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1)
)
_WirelessAPSystemGroup_ObjectIdentity = ObjectIdentity
wirelessAPSystemGroup = _WirelessAPSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1)
)
_WirelessAPMacAddr_Type = PhysAddress
_WirelessAPMacAddr_Object = MibScalar
wirelessAPMacAddr = _WirelessAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 1),
    _WirelessAPMacAddr_Type()
)
wirelessAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPMacAddr.setStatus("mandatory")
_WirelessAPFWVer_Type = DisplayString
_WirelessAPFWVer_Object = MibScalar
wirelessAPFWVer = _WirelessAPFWVer_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 2),
    _WirelessAPFWVer_Type()
)
wirelessAPFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPFWVer.setStatus("mandatory")
_WirelessAPDateTime_Type = DisplayString
_WirelessAPDateTime_Object = MibScalar
wirelessAPDateTime = _WirelessAPDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 3),
    _WirelessAPDateTime_Type()
)
wirelessAPDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPDateTime.setStatus("mandatory")
_WirelessAPUpTime_Type = TimeTicks
_WirelessAPUpTime_Object = MibScalar
wirelessAPUpTime = _WirelessAPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 4),
    _WirelessAPUpTime_Type()
)
wirelessAPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPUpTime.setStatus("mandatory")


class _WirelessAPResetNow_Type(Integer32):
    """Custom type wirelessAPResetNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-reset", 0),
          ("reset", 1))
    )


_WirelessAPResetNow_Type.__name__ = "Integer32"
_WirelessAPResetNow_Object = MibScalar
wirelessAPResetNow = _WirelessAPResetNow_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 5),
    _WirelessAPResetNow_Type()
)
wirelessAPResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPResetNow.setStatus("mandatory")


class _WirelessAPResetToFactoryDefault_Type(Integer32):
    """Custom type wirelessAPResetToFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("erase", 1),
          ("not-erase", 0))
    )


_WirelessAPResetToFactoryDefault_Type.__name__ = "Integer32"
_WirelessAPResetToFactoryDefault_Object = MibScalar
wirelessAPResetToFactoryDefault = _WirelessAPResetToFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 6),
    _WirelessAPResetToFactoryDefault_Type()
)
wirelessAPResetToFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPResetToFactoryDefault.setStatus("mandatory")


class _WirelessAPPassword_Type(DisplayString):
    """Custom type wirelessAPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_WirelessAPPassword_Type.__name__ = "DisplayString"
_WirelessAPPassword_Object = MibScalar
wirelessAPPassword = _WirelessAPPassword_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 7),
    _WirelessAPPassword_Type()
)
wirelessAPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPPassword.setStatus("mandatory")


class _WirelessAPClearLog_Type(Integer32):
    """Custom type wirelessAPClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("not-clear", 0))
    )


_WirelessAPClearLog_Type.__name__ = "Integer32"
_WirelessAPClearLog_Object = MibScalar
wirelessAPClearLog = _WirelessAPClearLog_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 8),
    _WirelessAPClearLog_Type()
)
wirelessAPClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPClearLog.setStatus("mandatory")


class _WirelessAPSaveConfiguration_Type(Integer32):
    """Custom type wirelessAPSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-save", 0),
          ("save", 1))
    )


_WirelessAPSaveConfiguration_Type.__name__ = "Integer32"
_WirelessAPSaveConfiguration_Object = MibScalar
wirelessAPSaveConfiguration = _WirelessAPSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 9),
    _WirelessAPSaveConfiguration_Type()
)
wirelessAPSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPSaveConfiguration.setStatus("mandatory")


class _SnmpTrapVersion_Type(Integer32):
    """Custom type snmpTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("V1", 0),
          ("V2c", 1))
    )


_SnmpTrapVersion_Type.__name__ = "Integer32"
_SnmpTrapVersion_Object = MibScalar
snmpTrapVersion = _SnmpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 10),
    _SnmpTrapVersion_Type()
)
snmpTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapVersion.setStatus("mandatory")


class _SnmpTrapRcvIpType_Type(Integer32):
    """Custom type snmpTrapRcvIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Broadcast", 1),
          ("Uni-cast", 0))
    )


_SnmpTrapRcvIpType_Type.__name__ = "Integer32"
_SnmpTrapRcvIpType_Object = MibScalar
snmpTrapRcvIpType = _SnmpTrapRcvIpType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 11),
    _SnmpTrapRcvIpType_Type()
)
snmpTrapRcvIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvIpType.setStatus("mandatory")
_SnmpAPTrapRcvIpAddress_Type = IpAddress
_SnmpAPTrapRcvIpAddress_Object = MibScalar
snmpAPTrapRcvIpAddress = _SnmpAPTrapRcvIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 12),
    _SnmpAPTrapRcvIpAddress_Type()
)
snmpAPTrapRcvIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAPTrapRcvIpAddress.setStatus("mandatory")


class _SnmpAPSNMPEnable_Type(Integer32):
    """Custom type snmpAPSNMPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_SnmpAPSNMPEnable_Type.__name__ = "Integer32"
_SnmpAPSNMPEnable_Object = MibScalar
snmpAPSNMPEnable = _SnmpAPSNMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 13),
    _SnmpAPSNMPEnable_Type()
)
snmpAPSNMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAPSNMPEnable.setStatus("mandatory")


class _SnmpAPCommunity_Type(DisplayString):
    """Custom type snmpAPCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SnmpAPCommunity_Type.__name__ = "DisplayString"
_SnmpAPCommunity_Object = MibScalar
snmpAPCommunity = _SnmpAPCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 14),
    _SnmpAPCommunity_Type()
)
snmpAPCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAPCommunity.setStatus("mandatory")


class _SnmpAPAccessRight_Type(Integer32):
    """Custom type snmpAPAccessRight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Read-Only", 0),
          ("Read-and-Write", 1))
    )


_SnmpAPAccessRight_Type.__name__ = "Integer32"
_SnmpAPAccessRight_Object = MibScalar
snmpAPAccessRight = _SnmpAPAccessRight_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 15),
    _SnmpAPAccessRight_Type()
)
snmpAPAccessRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAPAccessRight.setStatus("mandatory")


class _SnmpAPManagersType_Type(Integer32):
    """Custom type snmpAPManagersType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("A-Specific-Station", 0),
          ("Any-Station", 1))
    )


_SnmpAPManagersType_Type.__name__ = "Integer32"
_SnmpAPManagersType_Object = MibScalar
snmpAPManagersType = _SnmpAPManagersType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 16),
    _SnmpAPManagersType_Type()
)
snmpAPManagersType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAPManagersType.setStatus("mandatory")
_SnmpAPSpecificStationIp_Type = IpAddress
_SnmpAPSpecificStationIp_Object = MibScalar
snmpAPSpecificStationIp = _SnmpAPSpecificStationIp_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 17),
    _SnmpAPSpecificStationIp_Type()
)
snmpAPSpecificStationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAPSpecificStationIp.setStatus("mandatory")


class _SnmpAPTrapEnable_Type(Integer32):
    """Custom type snmpAPTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_SnmpAPTrapEnable_Type.__name__ = "Integer32"
_SnmpAPTrapEnable_Object = MibScalar
snmpAPTrapEnable = _SnmpAPTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 1, 18),
    _SnmpAPTrapEnable_Type()
)
snmpAPTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAPTrapEnable.setStatus("mandatory")
_WirelessAPConnectedStationGroup_ObjectIdentity = ObjectIdentity
wirelessAPConnectedStationGroup = _WirelessAPConnectedStationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2)
)


class _WirelessAPConnectedStationTableRefresh_Type(Integer32):
    """Custom type wirelessAPConnectedStationTableRefresh based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-refresh", 0),
          ("refresh", 1))
    )


_WirelessAPConnectedStationTableRefresh_Type.__name__ = "Integer32"
_WirelessAPConnectedStationTableRefresh_Object = MibScalar
wirelessAPConnectedStationTableRefresh = _WirelessAPConnectedStationTableRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 1),
    _WirelessAPConnectedStationTableRefresh_Type()
)
wirelessAPConnectedStationTableRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPConnectedStationTableRefresh.setStatus("mandatory")
_WirelessAPConnectedStation_ObjectIdentity = ObjectIdentity
wirelessAPConnectedStation = _WirelessAPConnectedStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 2)
)
_WirelessAPConnectedStationTable_Object = MibTable
wirelessAPConnectedStationTable = _WirelessAPConnectedStationTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    wirelessAPConnectedStationTable.setStatus("mandatory")
_WirelessAPConnectedStationEntry_Object = MibTableRow
wirelessAPConnectedStationEntry = _WirelessAPConnectedStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 2, 1, 1)
)
wirelessAPConnectedStationEntry.setIndexNames(
    (0, "NETGEAR-ME-MIB", "wirelessAPConnectedStationMacAddr"),
)
if mibBuilder.loadTexts:
    wirelessAPConnectedStationEntry.setStatus("mandatory")
_WirelessAPConnectedStationMacAddr_Type = PhysAddress
_WirelessAPConnectedStationMacAddr_Object = MibTableColumn
wirelessAPConnectedStationMacAddr = _WirelessAPConnectedStationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 2, 1, 1, 2),
    _WirelessAPConnectedStationMacAddr_Type()
)
wirelessAPConnectedStationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPConnectedStationMacAddr.setStatus("mandatory")


class _WirelessAPConnectedStationStatus_Type(Integer32):
    """Custom type wirelessAPConnectedStationStatus based on Integer32"""
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
        *(("associated", 0),
          ("athenticating", 1),
          ("authenticated", 2),
          ("not-associated", 3))
    )


_WirelessAPConnectedStationStatus_Type.__name__ = "Integer32"
_WirelessAPConnectedStationStatus_Object = MibTableColumn
wirelessAPConnectedStationStatus = _WirelessAPConnectedStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 2, 1, 1, 3),
    _WirelessAPConnectedStationStatus_Type()
)
wirelessAPConnectedStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPConnectedStationStatus.setStatus("mandatory")


class _WirelessAPControl_Type(Integer32):
    """Custom type wirelessAPControl based on Integer32"""
    defaultValue = 0

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


_WirelessAPControl_Type.__name__ = "Integer32"
_WirelessAPControl_Object = MibScalar
wirelessAPControl = _WirelessAPControl_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 3),
    _WirelessAPControl_Type()
)
wirelessAPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPControl.setStatus("mandatory")
_WirelessAPControlList_ObjectIdentity = ObjectIdentity
wirelessAPControlList = _WirelessAPControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 4)
)
_WirelessAPControlListTable_Object = MibTable
wirelessAPControlListTable = _WirelessAPControlListTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    wirelessAPControlListTable.setStatus("mandatory")
_WirelessAPControlListEntry_Object = MibTableRow
wirelessAPControlListEntry = _WirelessAPControlListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 4, 1, 1)
)
wirelessAPControlListEntry.setIndexNames(
    (0, "NETGEAR-ME-MIB", "wirelessAPControlListMacAddr"),
)
if mibBuilder.loadTexts:
    wirelessAPControlListEntry.setStatus("mandatory")
_WirelessAPControlListMacAddr_Type = PhysAddress
_WirelessAPControlListMacAddr_Object = MibTableColumn
wirelessAPControlListMacAddr = _WirelessAPControlListMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 4, 1, 1, 2),
    _WirelessAPControlListMacAddr_Type()
)
wirelessAPControlListMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPControlListMacAddr.setStatus("mandatory")
_WirelessAPCtlOperate_ObjectIdentity = ObjectIdentity
wirelessAPCtlOperate = _WirelessAPCtlOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 5)
)
_WirelessAPAddCtlMacAddr_Type = PhysAddress
_WirelessAPAddCtlMacAddr_Object = MibScalar
wirelessAPAddCtlMacAddr = _WirelessAPAddCtlMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 5, 1),
    _WirelessAPAddCtlMacAddr_Type()
)
wirelessAPAddCtlMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPAddCtlMacAddr.setStatus("mandatory")
_WirelessAPDelCtlMacAddr_Type = PhysAddress
_WirelessAPDelCtlMacAddr_Object = MibScalar
wirelessAPDelCtlMacAddr = _WirelessAPDelCtlMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 2, 5, 2),
    _WirelessAPDelCtlMacAddr_Type()
)
wirelessAPDelCtlMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPDelCtlMacAddr.setStatus("mandatory")
_WirelessAPIfTrafficGroup_ObjectIdentity = ObjectIdentity
wirelessAPIfTrafficGroup = _WirelessAPIfTrafficGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3)
)
_WirelessAPIfWiredTrafficGroup_ObjectIdentity = ObjectIdentity
wirelessAPIfWiredTrafficGroup = _WirelessAPIfWiredTrafficGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 1)
)
_WirelessAPIfWiredTotalOctetsIn_Type = Counter32
_WirelessAPIfWiredTotalOctetsIn_Object = MibScalar
wirelessAPIfWiredTotalOctetsIn = _WirelessAPIfWiredTotalOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 1, 1),
    _WirelessAPIfWiredTotalOctetsIn_Type()
)
wirelessAPIfWiredTotalOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWiredTotalOctetsIn.setStatus("mandatory")
_WirelessAPIfWiredTotalOctetsOut_Type = Counter32
_WirelessAPIfWiredTotalOctetsOut_Object = MibScalar
wirelessAPIfWiredTotalOctetsOut = _WirelessAPIfWiredTotalOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 1, 2),
    _WirelessAPIfWiredTotalOctetsOut_Type()
)
wirelessAPIfWiredTotalOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWiredTotalOctetsOut.setStatus("mandatory")
_WirelessAPIfWiredPacketsIn_Type = Counter32
_WirelessAPIfWiredPacketsIn_Object = MibScalar
wirelessAPIfWiredPacketsIn = _WirelessAPIfWiredPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 1, 3),
    _WirelessAPIfWiredPacketsIn_Type()
)
wirelessAPIfWiredPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWiredPacketsIn.setStatus("mandatory")
_WirelessAPIfWiredPacketsOut_Type = Counter32
_WirelessAPIfWiredPacketsOut_Object = MibScalar
wirelessAPIfWiredPacketsOut = _WirelessAPIfWiredPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 1, 4),
    _WirelessAPIfWiredPacketsOut_Type()
)
wirelessAPIfWiredPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWiredPacketsOut.setStatus("mandatory")
_WirelessAPIfWiredThroughputIn_Type = Counter32
_WirelessAPIfWiredThroughputIn_Object = MibScalar
wirelessAPIfWiredThroughputIn = _WirelessAPIfWiredThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 1, 5),
    _WirelessAPIfWiredThroughputIn_Type()
)
wirelessAPIfWiredThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWiredThroughputIn.setStatus("mandatory")
_WirelessAPIfWiredThroughputOut_Type = Counter32
_WirelessAPIfWiredThroughputOut_Object = MibScalar
wirelessAPIfWiredThroughputOut = _WirelessAPIfWiredThroughputOut_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 1, 6),
    _WirelessAPIfWiredThroughputOut_Type()
)
wirelessAPIfWiredThroughputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWiredThroughputOut.setStatus("mandatory")
_WirelessAPIfWiredErrorsIn_Type = Counter32
_WirelessAPIfWiredErrorsIn_Object = MibScalar
wirelessAPIfWiredErrorsIn = _WirelessAPIfWiredErrorsIn_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 1, 7),
    _WirelessAPIfWiredErrorsIn_Type()
)
wirelessAPIfWiredErrorsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWiredErrorsIn.setStatus("mandatory")
_WirelessAPIfWiredErrorsOut_Type = Counter32
_WirelessAPIfWiredErrorsOut_Object = MibScalar
wirelessAPIfWiredErrorsOut = _WirelessAPIfWiredErrorsOut_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 1, 8),
    _WirelessAPIfWiredErrorsOut_Type()
)
wirelessAPIfWiredErrorsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWiredErrorsOut.setStatus("mandatory")


class _WirelessAPIfWiredTrafficResetCounter_Type(Integer32):
    """Custom type wirelessAPIfWiredTrafficResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_WirelessAPIfWiredTrafficResetCounter_Type.__name__ = "Integer32"
_WirelessAPIfWiredTrafficResetCounter_Object = MibScalar
wirelessAPIfWiredTrafficResetCounter = _WirelessAPIfWiredTrafficResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 1, 9),
    _WirelessAPIfWiredTrafficResetCounter_Type()
)
wirelessAPIfWiredTrafficResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPIfWiredTrafficResetCounter.setStatus("mandatory")
_WirelessAPIfWlanTrafficGroup_ObjectIdentity = ObjectIdentity
wirelessAPIfWlanTrafficGroup = _WirelessAPIfWlanTrafficGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2)
)
_WirelessAPIfWLANTotalOctetsIn_Type = Counter32
_WirelessAPIfWLANTotalOctetsIn_Object = MibScalar
wirelessAPIfWLANTotalOctetsIn = _WirelessAPIfWLANTotalOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 1),
    _WirelessAPIfWLANTotalOctetsIn_Type()
)
wirelessAPIfWLANTotalOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANTotalOctetsIn.setStatus("mandatory")
_WirelessAPIfWLANTotalOctetsOut_Type = Counter32
_WirelessAPIfWLANTotalOctetsOut_Object = MibScalar
wirelessAPIfWLANTotalOctetsOut = _WirelessAPIfWLANTotalOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 2),
    _WirelessAPIfWLANTotalOctetsOut_Type()
)
wirelessAPIfWLANTotalOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANTotalOctetsOut.setStatus("mandatory")
_WirelessAPIfWLANUnicastPacketsIn_Type = Counter32
_WirelessAPIfWLANUnicastPacketsIn_Object = MibScalar
wirelessAPIfWLANUnicastPacketsIn = _WirelessAPIfWLANUnicastPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 3),
    _WirelessAPIfWLANUnicastPacketsIn_Type()
)
wirelessAPIfWLANUnicastPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANUnicastPacketsIn.setStatus("mandatory")
_WirelessAPIfWLANUnicastPacketsOut_Type = Counter32
_WirelessAPIfWLANUnicastPacketsOut_Object = MibScalar
wirelessAPIfWLANUnicastPacketsOut = _WirelessAPIfWLANUnicastPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 4),
    _WirelessAPIfWLANUnicastPacketsOut_Type()
)
wirelessAPIfWLANUnicastPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANUnicastPacketsOut.setStatus("mandatory")
_WirelessAPIfWLANBroadcastPacketsIn_Type = Counter32
_WirelessAPIfWLANBroadcastPacketsIn_Object = MibScalar
wirelessAPIfWLANBroadcastPacketsIn = _WirelessAPIfWLANBroadcastPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 5),
    _WirelessAPIfWLANBroadcastPacketsIn_Type()
)
wirelessAPIfWLANBroadcastPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANBroadcastPacketsIn.setStatus("mandatory")
_WirelessAPIfWLANBroadcastPacketsOut_Type = Counter32
_WirelessAPIfWLANBroadcastPacketsOut_Object = MibScalar
wirelessAPIfWLANBroadcastPacketsOut = _WirelessAPIfWLANBroadcastPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 6),
    _WirelessAPIfWLANBroadcastPacketsOut_Type()
)
wirelessAPIfWLANBroadcastPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANBroadcastPacketsOut.setStatus("mandatory")
_WirelessAPIfWLANMulticastPacketsIn_Type = Counter32
_WirelessAPIfWLANMulticastPacketsIn_Object = MibScalar
wirelessAPIfWLANMulticastPacketsIn = _WirelessAPIfWLANMulticastPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 7),
    _WirelessAPIfWLANMulticastPacketsIn_Type()
)
wirelessAPIfWLANMulticastPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANMulticastPacketsIn.setStatus("mandatory")
_WirelessAPIfWLANMulticastPacketsOut_Type = Counter32
_WirelessAPIfWLANMulticastPacketsOut_Object = MibScalar
wirelessAPIfWLANMulticastPacketsOut = _WirelessAPIfWLANMulticastPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 8),
    _WirelessAPIfWLANMulticastPacketsOut_Type()
)
wirelessAPIfWLANMulticastPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANMulticastPacketsOut.setStatus("mandatory")
_WirelessAPIfWLANThroughputIn_Type = Counter32
_WirelessAPIfWLANThroughputIn_Object = MibScalar
wirelessAPIfWLANThroughputIn = _WirelessAPIfWLANThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 9),
    _WirelessAPIfWLANThroughputIn_Type()
)
wirelessAPIfWLANThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANThroughputIn.setStatus("mandatory")
_WirelessAPIfWLANThroughputOut_Type = Counter32
_WirelessAPIfWLANThroughputOut_Object = MibScalar
wirelessAPIfWLANThroughputOut = _WirelessAPIfWLANThroughputOut_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 10),
    _WirelessAPIfWLANThroughputOut_Type()
)
wirelessAPIfWLANThroughputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANThroughputOut.setStatus("mandatory")
_WirelessAPIfWLANPacketsIn_Type = Counter32
_WirelessAPIfWLANPacketsIn_Object = MibScalar
wirelessAPIfWLANPacketsIn = _WirelessAPIfWLANPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 11),
    _WirelessAPIfWLANPacketsIn_Type()
)
wirelessAPIfWLANPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANPacketsIn.setStatus("mandatory")
_WirelessAPIfWLANPacketsOut_Type = Counter32
_WirelessAPIfWLANPacketsOut_Object = MibScalar
wirelessAPIfWLANPacketsOut = _WirelessAPIfWLANPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 12),
    _WirelessAPIfWLANPacketsOut_Type()
)
wirelessAPIfWLANPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPIfWLANPacketsOut.setStatus("mandatory")


class _WirelessAPIfWLANTrafficResetCounter_Type(Integer32):
    """Custom type wirelessAPIfWLANTrafficResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_WirelessAPIfWLANTrafficResetCounter_Type.__name__ = "Integer32"
_WirelessAPIfWLANTrafficResetCounter_Object = MibScalar
wirelessAPIfWLANTrafficResetCounter = _WirelessAPIfWLANTrafficResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 3, 2, 13),
    _WirelessAPIfWLANTrafficResetCounter_Type()
)
wirelessAPIfWLANTrafficResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPIfWLANTrafficResetCounter.setStatus("mandatory")
_WirelessAPIfSettingsGroup_ObjectIdentity = ObjectIdentity
wirelessAPIfSettingsGroup = _WirelessAPIfSettingsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4)
)


class _WirelessAPDHCPClientObtainIPchoice_Type(Integer32):
    """Custom type wirelessAPDHCPClientObtainIPchoice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("static", 0))
    )


_WirelessAPDHCPClientObtainIPchoice_Type.__name__ = "Integer32"
_WirelessAPDHCPClientObtainIPchoice_Object = MibScalar
wirelessAPDHCPClientObtainIPchoice = _WirelessAPDHCPClientObtainIPchoice_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 1),
    _WirelessAPDHCPClientObtainIPchoice_Type()
)
wirelessAPDHCPClientObtainIPchoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientObtainIPchoice.setStatus("mandatory")
_WirelessAPDHCPClientIPaddr_Type = IpAddress
_WirelessAPDHCPClientIPaddr_Object = MibScalar
wirelessAPDHCPClientIPaddr = _WirelessAPDHCPClientIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 2),
    _WirelessAPDHCPClientIPaddr_Type()
)
wirelessAPDHCPClientIPaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientIPaddr.setStatus("mandatory")
_WirelessAPDHCPClientIPsubnetMask_Type = IpAddress
_WirelessAPDHCPClientIPsubnetMask_Object = MibScalar
wirelessAPDHCPClientIPsubnetMask = _WirelessAPDHCPClientIPsubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 3),
    _WirelessAPDHCPClientIPsubnetMask_Type()
)
wirelessAPDHCPClientIPsubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientIPsubnetMask.setStatus("mandatory")
_WirelessAPDHCPClientGateway_Type = IpAddress
_WirelessAPDHCPClientGateway_Object = MibScalar
wirelessAPDHCPClientGateway = _WirelessAPDHCPClientGateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 4),
    _WirelessAPDHCPClientGateway_Type()
)
wirelessAPDHCPClientGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientGateway.setStatus("mandatory")
_WirelessAPDHCPClientPriDNS_Type = IpAddress
_WirelessAPDHCPClientPriDNS_Object = MibScalar
wirelessAPDHCPClientPriDNS = _WirelessAPDHCPClientPriDNS_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 5),
    _WirelessAPDHCPClientPriDNS_Type()
)
wirelessAPDHCPClientPriDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientPriDNS.setStatus("mandatory")
_WirelessAPDHCPClientSecDNS_Type = IpAddress
_WirelessAPDHCPClientSecDNS_Object = MibScalar
wirelessAPDHCPClientSecDNS = _WirelessAPDHCPClientSecDNS_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 6),
    _WirelessAPDHCPClientSecDNS_Type()
)
wirelessAPDHCPClientSecDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientSecDNS.setStatus("mandatory")
_WirelessAPDHCPClientStaticIPaddr_Type = IpAddress
_WirelessAPDHCPClientStaticIPaddr_Object = MibScalar
wirelessAPDHCPClientStaticIPaddr = _WirelessAPDHCPClientStaticIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 7),
    _WirelessAPDHCPClientStaticIPaddr_Type()
)
wirelessAPDHCPClientStaticIPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientStaticIPaddr.setStatus("mandatory")
_WirelessAPDHCPClientStaticIPsubnetMask_Type = IpAddress
_WirelessAPDHCPClientStaticIPsubnetMask_Object = MibScalar
wirelessAPDHCPClientStaticIPsubnetMask = _WirelessAPDHCPClientStaticIPsubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 8),
    _WirelessAPDHCPClientStaticIPsubnetMask_Type()
)
wirelessAPDHCPClientStaticIPsubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientStaticIPsubnetMask.setStatus("mandatory")
_WirelessAPDHCPClientStaticGateway_Type = IpAddress
_WirelessAPDHCPClientStaticGateway_Object = MibScalar
wirelessAPDHCPClientStaticGateway = _WirelessAPDHCPClientStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 9),
    _WirelessAPDHCPClientStaticGateway_Type()
)
wirelessAPDHCPClientStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientStaticGateway.setStatus("mandatory")
_WirelessAPDHCPClientStaticPriDNS_Type = IpAddress
_WirelessAPDHCPClientStaticPriDNS_Object = MibScalar
wirelessAPDHCPClientStaticPriDNS = _WirelessAPDHCPClientStaticPriDNS_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 10),
    _WirelessAPDHCPClientStaticPriDNS_Type()
)
wirelessAPDHCPClientStaticPriDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientStaticPriDNS.setStatus("mandatory")
_WirelessAPDHCPClientStaticSecDNS_Type = IpAddress
_WirelessAPDHCPClientStaticSecDNS_Object = MibScalar
wirelessAPDHCPClientStaticSecDNS = _WirelessAPDHCPClientStaticSecDNS_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 11),
    _WirelessAPDHCPClientStaticSecDNS_Type()
)
wirelessAPDHCPClientStaticSecDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPDHCPClientStaticSecDNS.setStatus("mandatory")


class _WirelessAPName_Type(DisplayString):
    """Custom type wirelessAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WirelessAPName_Type.__name__ = "DisplayString"
_WirelessAPName_Object = MibScalar
wirelessAPName = _WirelessAPName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 12),
    _WirelessAPName_Type()
)
wirelessAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPName.setStatus("mandatory")


class _WirelessAPWINSchoice_Type(Integer32):
    """Custom type wirelessAPWINSchoice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disAbled", 0),
          ("enAbled", 1))
    )


_WirelessAPWINSchoice_Type.__name__ = "Integer32"
_WirelessAPWINSchoice_Object = MibScalar
wirelessAPWINSchoice = _WirelessAPWINSchoice_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 13),
    _WirelessAPWINSchoice_Type()
)
wirelessAPWINSchoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPWINSchoice.setStatus("mandatory")


class _WirelessAPWINSServerName_Type(DisplayString):
    """Custom type wirelessAPWINSServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WirelessAPWINSServerName_Type.__name__ = "DisplayString"
_WirelessAPWINSServerName_Object = MibScalar
wirelessAPWINSServerName = _WirelessAPWINSServerName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 4, 14),
    _WirelessAPWINSServerName_Type()
)
wirelessAPWINSServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPWINSServerName.setStatus("mandatory")
_WirelessAPWirelessSettingsGroup_ObjectIdentity = ObjectIdentity
wirelessAPWirelessSettingsGroup = _WirelessAPWirelessSettingsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5)
)


class _WirelessAPCountryDomain_Type(Integer32):
    """Custom type wirelessAPCountryDomain based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("africa", 1),
          ("asia", 2),
          ("australia", 3),
          ("canada", 4),
          ("europe", 5),
          ("france", 6),
          ("israel", 7),
          ("japan", 8),
          ("mexico", 9),
          ("none", 0),
          ("southAmerica", 10),
          ("usa", 11))
    )


_WirelessAPCountryDomain_Type.__name__ = "Integer32"
_WirelessAPCountryDomain_Object = MibScalar
wirelessAPCountryDomain = _WirelessAPCountryDomain_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 1),
    _WirelessAPCountryDomain_Type()
)
wirelessAPCountryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPCountryDomain.setStatus("mandatory")


class _WirelessAPChannelNo_Type(Integer32):
    """Custom type wirelessAPChannelNo based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_WirelessAPChannelNo_Type.__name__ = "Integer32"
_WirelessAPChannelNo_Object = MibScalar
wirelessAPChannelNo = _WirelessAPChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 2),
    _WirelessAPChannelNo_Type()
)
wirelessAPChannelNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPChannelNo.setStatus("mandatory")


class _WirelessAPSSID_Type(DisplayString):
    """Custom type wirelessAPSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WirelessAPSSID_Type.__name__ = "DisplayString"
_WirelessAPSSID_Object = MibScalar
wirelessAPSSID = _WirelessAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 3),
    _WirelessAPSSID_Type()
)
wirelessAPSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPSSID.setStatus("mandatory")


class _WirelessAPPassphrase_Type(DisplayString):
    """Custom type wirelessAPPassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessAPPassphrase_Type.__name__ = "DisplayString"
_WirelessAPPassphrase_Object = MibScalar
wirelessAPPassphrase = _WirelessAPPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 7),
    _WirelessAPPassphrase_Type()
)
wirelessAPPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPPassphrase.setStatus("mandatory")


class _WirelessAPGenerateKeysEnabled_Type(Integer32):
    """Custom type wirelessAPGenerateKeysEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disAbled", 0),
          ("enAbled", 1))
    )


_WirelessAPGenerateKeysEnabled_Type.__name__ = "Integer32"
_WirelessAPGenerateKeysEnabled_Object = MibScalar
wirelessAPGenerateKeysEnabled = _WirelessAPGenerateKeysEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 8),
    _WirelessAPGenerateKeysEnabled_Type()
)
wirelessAPGenerateKeysEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPGenerateKeysEnabled.setStatus("mandatory")
_WirelessAPKeysSet_ObjectIdentity = ObjectIdentity
wirelessAPKeysSet = _WirelessAPKeysSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 9)
)
_WirelessAPKeysSetTable_Object = MibTable
wirelessAPKeysSetTable = _WirelessAPKeysSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 9, 1)
)
if mibBuilder.loadTexts:
    wirelessAPKeysSetTable.setStatus("mandatory")
_WirelessAPKeysSetEntry_Object = MibTableRow
wirelessAPKeysSetEntry = _WirelessAPKeysSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 9, 1, 1)
)
wirelessAPKeysSetEntry.setIndexNames(
    (0, "NETGEAR-ME-MIB", "wirelessAPKeysSetEnabled"),
)
if mibBuilder.loadTexts:
    wirelessAPKeysSetEntry.setStatus("mandatory")


class _WirelessAPKeysSetEnabled_Type(Integer32):
    """Custom type wirelessAPKeysSetEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disAbled", 0),
          ("enAbled", 1))
    )


_WirelessAPKeysSetEnabled_Type.__name__ = "Integer32"
_WirelessAPKeysSetEnabled_Object = MibTableColumn
wirelessAPKeysSetEnabled = _WirelessAPKeysSetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 9, 1, 1, 2),
    _WirelessAPKeysSetEnabled_Type()
)
wirelessAPKeysSetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPKeysSetEnabled.setStatus("mandatory")


class _WirelessAPKeys_Type(OctetString):
    """Custom type wirelessAPKeys based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_WirelessAPKeys_Type.__name__ = "OctetString"
_WirelessAPKeys_Object = MibTableColumn
wirelessAPKeys = _WirelessAPKeys_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 9, 1, 1, 3),
    _WirelessAPKeys_Type()
)
wirelessAPKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPKeys.setStatus("mandatory")


class _WirelessAPBasicRateChoice_Type(Integer32):
    """Custom type wirelessAPBasicRateChoice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("fixed", 1))
    )


_WirelessAPBasicRateChoice_Type.__name__ = "Integer32"
_WirelessAPBasicRateChoice_Object = MibScalar
wirelessAPBasicRateChoice = _WirelessAPBasicRateChoice_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 10),
    _WirelessAPBasicRateChoice_Type()
)
wirelessAPBasicRateChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPBasicRateChoice.setStatus("mandatory")
_WirelessAPFixedRate_ObjectIdentity = ObjectIdentity
wirelessAPFixedRate = _WirelessAPFixedRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 11)
)


class _WirelessAPFixedRate1_Type(Integer32):
    """Custom type wirelessAPFixedRate1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oneM-disabled", 0),
          ("oneM-enabled", 1))
    )


_WirelessAPFixedRate1_Type.__name__ = "Integer32"
_WirelessAPFixedRate1_Object = MibScalar
wirelessAPFixedRate1 = _WirelessAPFixedRate1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 11, 1),
    _WirelessAPFixedRate1_Type()
)
wirelessAPFixedRate1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPFixedRate1.setStatus("mandatory")


class _WirelessAPFixedRate2_Type(Integer32):
    """Custom type wirelessAPFixedRate2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("twoM-disabled", 0),
          ("twoM-enabled", 1))
    )


_WirelessAPFixedRate2_Type.__name__ = "Integer32"
_WirelessAPFixedRate2_Object = MibScalar
wirelessAPFixedRate2 = _WirelessAPFixedRate2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 11, 2),
    _WirelessAPFixedRate2_Type()
)
wirelessAPFixedRate2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPFixedRate2.setStatus("mandatory")


class _WirelessAPFixedRate5_5_Type(Integer32):
    """Custom type wirelessAPFixedRate5_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fiveDotFiveM-disabled", 0),
          ("fiveDotFiveM-enabled", 1))
    )


_WirelessAPFixedRate5_5_Type.__name__ = "Integer32"
_WirelessAPFixedRate5_5_Object = MibScalar
wirelessAPFixedRate5_5 = _WirelessAPFixedRate5_5_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 11, 3),
    _WirelessAPFixedRate5_5_Type()
)
wirelessAPFixedRate5_5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPFixedRate5_5.setStatus("mandatory")


class _WirelessAPFixedRate11_Type(Integer32):
    """Custom type wirelessAPFixedRate11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("elevenM-disabled", 0),
          ("elevenM-enabled", 1))
    )


_WirelessAPFixedRate11_Type.__name__ = "Integer32"
_WirelessAPFixedRate11_Object = MibScalar
wirelessAPFixedRate11 = _WirelessAPFixedRate11_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 11, 4),
    _WirelessAPFixedRate11_Type()
)
wirelessAPFixedRate11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPFixedRate11.setStatus("mandatory")


class _WirelessAPRTSThreshold_Type(Integer32):
    """Custom type wirelessAPRTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_WirelessAPRTSThreshold_Type.__name__ = "Integer32"
_WirelessAPRTSThreshold_Object = MibScalar
wirelessAPRTSThreshold = _WirelessAPRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 12),
    _WirelessAPRTSThreshold_Type()
)
wirelessAPRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPRTSThreshold.setStatus("mandatory")


class _WirelessAPFragmentationThreshold_Type(Integer32):
    """Custom type wirelessAPFragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_WirelessAPFragmentationThreshold_Type.__name__ = "Integer32"
_WirelessAPFragmentationThreshold_Object = MibScalar
wirelessAPFragmentationThreshold = _WirelessAPFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 13),
    _WirelessAPFragmentationThreshold_Type()
)
wirelessAPFragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPFragmentationThreshold.setStatus("mandatory")


class _WirelessAPBeaconPeriod_Type(Integer32):
    """Custom type wirelessAPBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WirelessAPBeaconPeriod_Type.__name__ = "Integer32"
_WirelessAPBeaconPeriod_Object = MibScalar
wirelessAPBeaconPeriod = _WirelessAPBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 14),
    _WirelessAPBeaconPeriod_Type()
)
wirelessAPBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPBeaconPeriod.setStatus("mandatory")


class _WirelessAPShortPreambleOptionImplemented_Type(Integer32):
    """Custom type wirelessAPShortPreambleOptionImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 0))
    )


_WirelessAPShortPreambleOptionImplemented_Type.__name__ = "Integer32"
_WirelessAPShortPreambleOptionImplemented_Object = MibScalar
wirelessAPShortPreambleOptionImplemented = _WirelessAPShortPreambleOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 15),
    _WirelessAPShortPreambleOptionImplemented_Type()
)
wirelessAPShortPreambleOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPShortPreambleOptionImplemented.setStatus("mandatory")


class _WirelessAPAntennaSelection_Type(Integer32):
    """Custom type wirelessAPAntennaSelection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diversity", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_WirelessAPAntennaSelection_Type.__name__ = "Integer32"
_WirelessAPAntennaSelection_Object = MibScalar
wirelessAPAntennaSelection = _WirelessAPAntennaSelection_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 16),
    _WirelessAPAntennaSelection_Type()
)
wirelessAPAntennaSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPAntennaSelection.setStatus("mandatory")


class _WirelessAPMaximumTransmitPowerLevel_Type(Integer32):
    """Custom type wirelessAPMaximumTransmitPowerLevel based on Integer32"""
    defaultValue = 1

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
        *(("eighteendbm", 1),
          ("fifteendbm", 3),
          ("sevendbm", 5),
          ("seventeendbm", 2),
          ("thirteendbm", 4),
          ("zerodbm", 6))
    )


_WirelessAPMaximumTransmitPowerLevel_Type.__name__ = "Integer32"
_WirelessAPMaximumTransmitPowerLevel_Object = MibScalar
wirelessAPMaximumTransmitPowerLevel = _WirelessAPMaximumTransmitPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 17),
    _WirelessAPMaximumTransmitPowerLevel_Type()
)
wirelessAPMaximumTransmitPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPMaximumTransmitPowerLevel.setStatus("mandatory")


class _WirelessAPOperatingMode_Type(Integer32):
    """Custom type wirelessAPOperatingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eight0twoDot1xAP", 0),
          ("noneight0twoDot1xAP", 1))
    )


_WirelessAPOperatingMode_Type.__name__ = "Integer32"
_WirelessAPOperatingMode_Object = MibScalar
wirelessAPOperatingMode = _WirelessAPOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 18),
    _WirelessAPOperatingMode_Type()
)
wirelessAPOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPOperatingMode.setStatus("mandatory")


class _WirelessAPSSIDEnabled_Type(Integer32):
    """Custom type wirelessAPSSIDEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disAbled", 0),
          ("enAbled", 1))
    )


_WirelessAPSSIDEnabled_Type.__name__ = "Integer32"
_WirelessAPSSIDEnabled_Object = MibScalar
wirelessAPSSIDEnabled = _WirelessAPSSIDEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 5, 19),
    _WirelessAPSSIDEnabled_Type()
)
wirelessAPSSIDEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPSSIDEnabled.setStatus("mandatory")
_WirelessAPSecuritySettingsGroup_ObjectIdentity = ObjectIdentity
wirelessAPSecuritySettingsGroup = _WirelessAPSecuritySettingsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6)
)


class _WirelessAP802dot1xSecurityEnabled_Type(Integer32):
    """Custom type wirelessAP802dot1xSecurityEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disAbled", 1),
          ("enAbled", 0))
    )


_WirelessAP802dot1xSecurityEnabled_Type.__name__ = "Integer32"
_WirelessAP802dot1xSecurityEnabled_Object = MibScalar
wirelessAP802dot1xSecurityEnabled = _WirelessAP802dot1xSecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 1),
    _WirelessAP802dot1xSecurityEnabled_Type()
)
wirelessAP802dot1xSecurityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAP802dot1xSecurityEnabled.setStatus("mandatory")


class _WirelessAPEAPauthType_Type(Integer32):
    """Custom type wirelessAPEAPauthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("AllowEAP-MD5", 1),
          ("NotAllowEAP-MD5", 0))
    )


_WirelessAPEAPauthType_Type.__name__ = "Integer32"
_WirelessAPEAPauthType_Object = MibScalar
wirelessAPEAPauthType = _WirelessAPEAPauthType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 2),
    _WirelessAPEAPauthType_Type()
)
wirelessAPEAPauthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPEAPauthType.setStatus("mandatory")
_WirelessAPRadiusServer_Type = DisplayString
_WirelessAPRadiusServer_Object = MibScalar
wirelessAPRadiusServer = _WirelessAPRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 3),
    _WirelessAPRadiusServer_Type()
)
wirelessAPRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPRadiusServer.setStatus("mandatory")


class _WirelessAPRadiusPort_Type(Integer32):
    """Custom type wirelessAPRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WirelessAPRadiusPort_Type.__name__ = "Integer32"
_WirelessAPRadiusPort_Object = MibScalar
wirelessAPRadiusPort = _WirelessAPRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 4),
    _WirelessAPRadiusPort_Type()
)
wirelessAPRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPRadiusPort.setStatus("mandatory")


class _WirelessAPSharedKey_Type(DisplayString):
    """Custom type wirelessAPSharedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WirelessAPSharedKey_Type.__name__ = "DisplayString"
_WirelessAPSharedKey_Object = MibScalar
wirelessAPSharedKey = _WirelessAPSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 5),
    _WirelessAPSharedKey_Type()
)
wirelessAPSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPSharedKey.setStatus("mandatory")
_WirelessAPRadiusServer2_Type = DisplayString
_WirelessAPRadiusServer2_Object = MibScalar
wirelessAPRadiusServer2 = _WirelessAPRadiusServer2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 7),
    _WirelessAPRadiusServer2_Type()
)
wirelessAPRadiusServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPRadiusServer2.setStatus("mandatory")


class _WirelessAPRadAccountPort_Type(Integer32):
    """Custom type wirelessAPRadAccountPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WirelessAPRadAccountPort_Type.__name__ = "Integer32"
_WirelessAPRadAccountPort_Object = MibScalar
wirelessAPRadAccountPort = _WirelessAPRadAccountPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 11),
    _WirelessAPRadAccountPort_Type()
)
wirelessAPRadAccountPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPRadAccountPort.setStatus("mandatory")


class _WirelessAPKeyExchange_Type(Integer32):
    """Custom type wirelessAPKeyExchange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disAbled", 0),
          ("enAbled", 1))
    )


_WirelessAPKeyExchange_Type.__name__ = "Integer32"
_WirelessAPKeyExchange_Object = MibScalar
wirelessAPKeyExchange = _WirelessAPKeyExchange_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 16),
    _WirelessAPKeyExchange_Type()
)
wirelessAPKeyExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPKeyExchange.setStatus("mandatory")


class _WirelessAPKeyExchangeKeylife_Type(Integer32):
    """Custom type wirelessAPKeyExchangeKeylife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WirelessAPKeyExchangeKeylife_Type.__name__ = "Integer32"
_WirelessAPKeyExchangeKeylife_Object = MibScalar
wirelessAPKeyExchangeKeylife = _WirelessAPKeyExchangeKeylife_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 17),
    _WirelessAPKeyExchangeKeylife_Type()
)
wirelessAPKeyExchangeKeylife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPKeyExchangeKeylife.setStatus("mandatory")


class _WirelessAPRadAccountEnable_Type(Integer32):
    """Custom type wirelessAPRadAccountEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disAbled", 0),
          ("enAbled", 1))
    )


_WirelessAPRadAccountEnable_Type.__name__ = "Integer32"
_WirelessAPRadAccountEnable_Object = MibScalar
wirelessAPRadAccountEnable = _WirelessAPRadAccountEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 18),
    _WirelessAPRadAccountEnable_Type()
)
wirelessAPRadAccountEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPRadAccountEnable.setStatus("mandatory")


class _WirelessAPMacAuthEnable_Type(Integer32):
    """Custom type wirelessAPMacAuthEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disAbled", 0),
          ("enAbled", 1))
    )


_WirelessAPMacAuthEnable_Type.__name__ = "Integer32"
_WirelessAPMacAuthEnable_Object = MibScalar
wirelessAPMacAuthEnable = _WirelessAPMacAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 19),
    _WirelessAPMacAuthEnable_Type()
)
wirelessAPMacAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPMacAuthEnable.setStatus("mandatory")


class _WirelessAPRadAccountUpdateEnable_Type(Integer32):
    """Custom type wirelessAPRadAccountUpdateEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disAbled", 0),
          ("enAbled", 1))
    )


_WirelessAPRadAccountUpdateEnable_Type.__name__ = "Integer32"
_WirelessAPRadAccountUpdateEnable_Object = MibScalar
wirelessAPRadAccountUpdateEnable = _WirelessAPRadAccountUpdateEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 21),
    _WirelessAPRadAccountUpdateEnable_Type()
)
wirelessAPRadAccountUpdateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPRadAccountUpdateEnable.setStatus("mandatory")


class _WirelessAPRadAccountUpdatePeriod_Type(Integer32):
    """Custom type wirelessAPRadAccountUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WirelessAPRadAccountUpdatePeriod_Type.__name__ = "Integer32"
_WirelessAPRadAccountUpdatePeriod_Object = MibScalar
wirelessAPRadAccountUpdatePeriod = _WirelessAPRadAccountUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 22),
    _WirelessAPRadAccountUpdatePeriod_Type()
)
wirelessAPRadAccountUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPRadAccountUpdatePeriod.setStatus("mandatory")


class _WirelessAPRadAccountIdlePeriod_Type(Integer32):
    """Custom type wirelessAPRadAccountIdlePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_WirelessAPRadAccountIdlePeriod_Type.__name__ = "Integer32"
_WirelessAPRadAccountIdlePeriod_Object = MibScalar
wirelessAPRadAccountIdlePeriod = _WirelessAPRadAccountIdlePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 23),
    _WirelessAPRadAccountIdlePeriod_Type()
)
wirelessAPRadAccountIdlePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPRadAccountIdlePeriod.setStatus("mandatory")


class _WirelessTIOperateMode_Type(Integer32):
    """Custom type wirelessTIOperateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ClientAccessPoint", 3),
          ("Point-to-Multi-PointBridge", 5),
          ("Point-to-PointBridge", 4),
          ("RepeaterAccessPoint", 2),
          ("WirelessAccessPoint", 0))
    )


_WirelessTIOperateMode_Type.__name__ = "Integer32"
_WirelessTIOperateMode_Object = MibScalar
wirelessTIOperateMode = _WirelessTIOperateMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 25),
    _WirelessTIOperateMode_Type()
)
wirelessTIOperateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessTIOperateMode.setStatus("mandatory")
_WirelessTIDstMac_Type = PhysAddress
_WirelessTIDstMac_Object = MibScalar
wirelessTIDstMac = _WirelessTIDstMac_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 26),
    _WirelessTIDstMac_Type()
)
wirelessTIDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessTIDstMac.setStatus("mandatory")


class _WirelessTIIsolation_Type(Integer32):
    """Custom type wirelessTIIsolation based on Integer32"""
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


_WirelessTIIsolation_Type.__name__ = "Integer32"
_WirelessTIIsolation_Object = MibScalar
wirelessTIIsolation = _WirelessTIIsolation_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 28),
    _WirelessTIIsolation_Type()
)
wirelessTIIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessTIIsolation.setStatus("mandatory")


class _WirelessTIEnable80211d_Type(Integer32):
    """Custom type wirelessTIEnable80211d based on Integer32"""
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


_WirelessTIEnable80211d_Type.__name__ = "Integer32"
_WirelessTIEnable80211d_Object = MibScalar
wirelessTIEnable80211d = _WirelessTIEnable80211d_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 29),
    _WirelessTIEnable80211d_Type()
)
wirelessTIEnable80211d.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessTIEnable80211d.setStatus("mandatory")


class _WirelessAPSecurityMode_Type(Integer32):
    """Custom type wirelessAPSecurityMode based on Integer32"""
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
        *(("OPEN-128WEP-MODE", 2),
          ("OPEN-64WEP-MODE", 1),
          ("OPEN-DISABLE-MODE", 0),
          ("SHARED-128WEP-MODE", 4),
          ("SHARED-64WEP-MODE", 3))
    )


_WirelessAPSecurityMode_Type.__name__ = "Integer32"
_WirelessAPSecurityMode_Object = MibScalar
wirelessAPSecurityMode = _WirelessAPSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1, 6, 37),
    _WirelessAPSecurityMode_Type()
)
wirelessAPSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPSecurityMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETGEAR-ME-MIB",
    **{"netgear": netgear,
       "wirelessProducts": wirelessProducts,
       "wirelessAccessPointDev": wirelessAccessPointDev,
       "wirelessAPSystemGroup": wirelessAPSystemGroup,
       "wirelessAPMacAddr": wirelessAPMacAddr,
       "wirelessAPFWVer": wirelessAPFWVer,
       "wirelessAPDateTime": wirelessAPDateTime,
       "wirelessAPUpTime": wirelessAPUpTime,
       "wirelessAPResetNow": wirelessAPResetNow,
       "wirelessAPResetToFactoryDefault": wirelessAPResetToFactoryDefault,
       "wirelessAPPassword": wirelessAPPassword,
       "wirelessAPClearLog": wirelessAPClearLog,
       "wirelessAPSaveConfiguration": wirelessAPSaveConfiguration,
       "snmpTrapVersion": snmpTrapVersion,
       "snmpTrapRcvIpType": snmpTrapRcvIpType,
       "snmpAPTrapRcvIpAddress": snmpAPTrapRcvIpAddress,
       "snmpAPSNMPEnable": snmpAPSNMPEnable,
       "snmpAPCommunity": snmpAPCommunity,
       "snmpAPAccessRight": snmpAPAccessRight,
       "snmpAPManagersType": snmpAPManagersType,
       "snmpAPSpecificStationIp": snmpAPSpecificStationIp,
       "snmpAPTrapEnable": snmpAPTrapEnable,
       "wirelessAPConnectedStationGroup": wirelessAPConnectedStationGroup,
       "wirelessAPConnectedStationTableRefresh": wirelessAPConnectedStationTableRefresh,
       "wirelessAPConnectedStation": wirelessAPConnectedStation,
       "wirelessAPConnectedStationTable": wirelessAPConnectedStationTable,
       "wirelessAPConnectedStationEntry": wirelessAPConnectedStationEntry,
       "wirelessAPConnectedStationMacAddr": wirelessAPConnectedStationMacAddr,
       "wirelessAPConnectedStationStatus": wirelessAPConnectedStationStatus,
       "wirelessAPControl": wirelessAPControl,
       "wirelessAPControlList": wirelessAPControlList,
       "wirelessAPControlListTable": wirelessAPControlListTable,
       "wirelessAPControlListEntry": wirelessAPControlListEntry,
       "wirelessAPControlListMacAddr": wirelessAPControlListMacAddr,
       "wirelessAPCtlOperate": wirelessAPCtlOperate,
       "wirelessAPAddCtlMacAddr": wirelessAPAddCtlMacAddr,
       "wirelessAPDelCtlMacAddr": wirelessAPDelCtlMacAddr,
       "wirelessAPIfTrafficGroup": wirelessAPIfTrafficGroup,
       "wirelessAPIfWiredTrafficGroup": wirelessAPIfWiredTrafficGroup,
       "wirelessAPIfWiredTotalOctetsIn": wirelessAPIfWiredTotalOctetsIn,
       "wirelessAPIfWiredTotalOctetsOut": wirelessAPIfWiredTotalOctetsOut,
       "wirelessAPIfWiredPacketsIn": wirelessAPIfWiredPacketsIn,
       "wirelessAPIfWiredPacketsOut": wirelessAPIfWiredPacketsOut,
       "wirelessAPIfWiredThroughputIn": wirelessAPIfWiredThroughputIn,
       "wirelessAPIfWiredThroughputOut": wirelessAPIfWiredThroughputOut,
       "wirelessAPIfWiredErrorsIn": wirelessAPIfWiredErrorsIn,
       "wirelessAPIfWiredErrorsOut": wirelessAPIfWiredErrorsOut,
       "wirelessAPIfWiredTrafficResetCounter": wirelessAPIfWiredTrafficResetCounter,
       "wirelessAPIfWlanTrafficGroup": wirelessAPIfWlanTrafficGroup,
       "wirelessAPIfWLANTotalOctetsIn": wirelessAPIfWLANTotalOctetsIn,
       "wirelessAPIfWLANTotalOctetsOut": wirelessAPIfWLANTotalOctetsOut,
       "wirelessAPIfWLANUnicastPacketsIn": wirelessAPIfWLANUnicastPacketsIn,
       "wirelessAPIfWLANUnicastPacketsOut": wirelessAPIfWLANUnicastPacketsOut,
       "wirelessAPIfWLANBroadcastPacketsIn": wirelessAPIfWLANBroadcastPacketsIn,
       "wirelessAPIfWLANBroadcastPacketsOut": wirelessAPIfWLANBroadcastPacketsOut,
       "wirelessAPIfWLANMulticastPacketsIn": wirelessAPIfWLANMulticastPacketsIn,
       "wirelessAPIfWLANMulticastPacketsOut": wirelessAPIfWLANMulticastPacketsOut,
       "wirelessAPIfWLANThroughputIn": wirelessAPIfWLANThroughputIn,
       "wirelessAPIfWLANThroughputOut": wirelessAPIfWLANThroughputOut,
       "wirelessAPIfWLANPacketsIn": wirelessAPIfWLANPacketsIn,
       "wirelessAPIfWLANPacketsOut": wirelessAPIfWLANPacketsOut,
       "wirelessAPIfWLANTrafficResetCounter": wirelessAPIfWLANTrafficResetCounter,
       "wirelessAPIfSettingsGroup": wirelessAPIfSettingsGroup,
       "wirelessAPDHCPClientObtainIPchoice": wirelessAPDHCPClientObtainIPchoice,
       "wirelessAPDHCPClientIPaddr": wirelessAPDHCPClientIPaddr,
       "wirelessAPDHCPClientIPsubnetMask": wirelessAPDHCPClientIPsubnetMask,
       "wirelessAPDHCPClientGateway": wirelessAPDHCPClientGateway,
       "wirelessAPDHCPClientPriDNS": wirelessAPDHCPClientPriDNS,
       "wirelessAPDHCPClientSecDNS": wirelessAPDHCPClientSecDNS,
       "wirelessAPDHCPClientStaticIPaddr": wirelessAPDHCPClientStaticIPaddr,
       "wirelessAPDHCPClientStaticIPsubnetMask": wirelessAPDHCPClientStaticIPsubnetMask,
       "wirelessAPDHCPClientStaticGateway": wirelessAPDHCPClientStaticGateway,
       "wirelessAPDHCPClientStaticPriDNS": wirelessAPDHCPClientStaticPriDNS,
       "wirelessAPDHCPClientStaticSecDNS": wirelessAPDHCPClientStaticSecDNS,
       "wirelessAPName": wirelessAPName,
       "wirelessAPWINSchoice": wirelessAPWINSchoice,
       "wirelessAPWINSServerName": wirelessAPWINSServerName,
       "wirelessAPWirelessSettingsGroup": wirelessAPWirelessSettingsGroup,
       "wirelessAPCountryDomain": wirelessAPCountryDomain,
       "wirelessAPChannelNo": wirelessAPChannelNo,
       "wirelessAPSSID": wirelessAPSSID,
       "wirelessAPPassphrase": wirelessAPPassphrase,
       "wirelessAPGenerateKeysEnabled": wirelessAPGenerateKeysEnabled,
       "wirelessAPKeysSet": wirelessAPKeysSet,
       "wirelessAPKeysSetTable": wirelessAPKeysSetTable,
       "wirelessAPKeysSetEntry": wirelessAPKeysSetEntry,
       "wirelessAPKeysSetEnabled": wirelessAPKeysSetEnabled,
       "wirelessAPKeys": wirelessAPKeys,
       "wirelessAPBasicRateChoice": wirelessAPBasicRateChoice,
       "wirelessAPFixedRate": wirelessAPFixedRate,
       "wirelessAPFixedRate1": wirelessAPFixedRate1,
       "wirelessAPFixedRate2": wirelessAPFixedRate2,
       "wirelessAPFixedRate5-5": wirelessAPFixedRate5_5,
       "wirelessAPFixedRate11": wirelessAPFixedRate11,
       "wirelessAPRTSThreshold": wirelessAPRTSThreshold,
       "wirelessAPFragmentationThreshold": wirelessAPFragmentationThreshold,
       "wirelessAPBeaconPeriod": wirelessAPBeaconPeriod,
       "wirelessAPShortPreambleOptionImplemented": wirelessAPShortPreambleOptionImplemented,
       "wirelessAPAntennaSelection": wirelessAPAntennaSelection,
       "wirelessAPMaximumTransmitPowerLevel": wirelessAPMaximumTransmitPowerLevel,
       "wirelessAPOperatingMode": wirelessAPOperatingMode,
       "wirelessAPSSIDEnabled": wirelessAPSSIDEnabled,
       "wirelessAPSecuritySettingsGroup": wirelessAPSecuritySettingsGroup,
       "wirelessAP802dot1xSecurityEnabled": wirelessAP802dot1xSecurityEnabled,
       "wirelessAPEAPauthType": wirelessAPEAPauthType,
       "wirelessAPRadiusServer": wirelessAPRadiusServer,
       "wirelessAPRadiusPort": wirelessAPRadiusPort,
       "wirelessAPSharedKey": wirelessAPSharedKey,
       "wirelessAPRadiusServer2": wirelessAPRadiusServer2,
       "wirelessAPRadAccountPort": wirelessAPRadAccountPort,
       "wirelessAPKeyExchange": wirelessAPKeyExchange,
       "wirelessAPKeyExchangeKeylife": wirelessAPKeyExchangeKeylife,
       "wirelessAPRadAccountEnable": wirelessAPRadAccountEnable,
       "wirelessAPMacAuthEnable": wirelessAPMacAuthEnable,
       "wirelessAPRadAccountUpdateEnable": wirelessAPRadAccountUpdateEnable,
       "wirelessAPRadAccountUpdatePeriod": wirelessAPRadAccountUpdatePeriod,
       "wirelessAPRadAccountIdlePeriod": wirelessAPRadAccountIdlePeriod,
       "wirelessTIOperateMode": wirelessTIOperateMode,
       "wirelessTIDstMac": wirelessTIDstMac,
       "wirelessTIIsolation": wirelessTIIsolation,
       "wirelessTIEnable80211d": wirelessTIEnable80211d,
       "wirelessAPSecurityMode": wirelessAPSecurityMode}
)
