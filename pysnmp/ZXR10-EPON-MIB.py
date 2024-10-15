# SNMP MIB module (ZXR10-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-EPON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:51 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10EponObjects_ObjectIdentity = ObjectIdentity
zxr10EponObjects = _Zxr10EponObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309)
)
_Zxr10EponLocal_ObjectIdentity = ObjectIdentity
zxr10EponLocal = _Zxr10EponLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1)
)
_Zxr10EponOnuAuthTable_Object = MibTable
zxr10EponOnuAuthTable = _Zxr10EponOnuAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 1)
)
if mibBuilder.loadTexts:
    zxr10EponOnuAuthTable.setStatus("current")
_Zxr10EponOnuAuthEntry_Object = MibTableRow
zxr10EponOnuAuthEntry = _Zxr10EponOnuAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 1, 1)
)
zxr10EponOnuAuthEntry.setIndexNames(
    (0, "ZXR10-EPON-MIB", "eponSlotId"),
)
if mibBuilder.loadTexts:
    zxr10EponOnuAuthEntry.setStatus("current")


class _EponSlotId_Type(Integer32):
    """Custom type eponSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EponSlotId_Type.__name__ = "Integer32"
_EponSlotId_Object = MibTableColumn
eponSlotId = _EponSlotId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 1, 1, 1),
    _EponSlotId_Type()
)
eponSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponSlotId.setStatus("current")


class _OnuSoftwareAuth_Type(Integer32):
    """Custom type onuSoftwareAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("sn", 0))
    )


_OnuSoftwareAuth_Type.__name__ = "Integer32"
_OnuSoftwareAuth_Object = MibTableColumn
onuSoftwareAuth = _OnuSoftwareAuth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 1, 1, 2),
    _OnuSoftwareAuth_Type()
)
onuSoftwareAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSoftwareAuth.setStatus("current")


class _OnuHardwareSwitch_Type(Integer32):
    """Custom type onuHardwareSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuHardwareSwitch_Type.__name__ = "Integer32"
_OnuHardwareSwitch_Object = MibTableColumn
onuHardwareSwitch = _OnuHardwareSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 1, 1, 3),
    _OnuHardwareSwitch_Type()
)
onuHardwareSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuHardwareSwitch.setStatus("current")


class _OnuAutoAuthSwtich_Type(Integer32):
    """Custom type onuAutoAuthSwtich based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuAutoAuthSwtich_Type.__name__ = "Integer32"
_OnuAutoAuthSwtich_Object = MibTableColumn
onuAutoAuthSwtich = _OnuAutoAuthSwtich_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 1, 1, 4),
    _OnuAutoAuthSwtich_Type()
)
onuAutoAuthSwtich.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAutoAuthSwtich.setStatus("current")
_Zxr10EponOltOptiInfoTable_Object = MibTable
zxr10EponOltOptiInfoTable = _Zxr10EponOltOptiInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2)
)
if mibBuilder.loadTexts:
    zxr10EponOltOptiInfoTable.setStatus("current")
_Zxr10EponOltOptiInfoEntry_Object = MibTableRow
zxr10EponOltOptiInfoEntry = _Zxr10EponOltOptiInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2, 1)
)
zxr10EponOltOptiInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxr10EponOltOptiInfoEntry.setStatus("current")
_EponOltPortName_Type = DisplayString
_EponOltPortName_Object = MibTableColumn
eponOltPortName = _EponOltPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2, 1, 1),
    _EponOltPortName_Type()
)
eponOltPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOltPortName.setStatus("current")
_OptiInfoSFPID_Type = Integer32
_OptiInfoSFPID_Object = MibTableColumn
optiInfoSFPID = _OptiInfoSFPID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2, 1, 2),
    _OptiInfoSFPID_Type()
)
optiInfoSFPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optiInfoSFPID.setStatus("current")
_OptiInfoVendor_Type = DisplayString
_OptiInfoVendor_Object = MibTableColumn
optiInfoVendor = _OptiInfoVendor_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2, 1, 3),
    _OptiInfoVendor_Type()
)
optiInfoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optiInfoVendor.setStatus("current")
_OptiInfoWavelength_Type = Integer32
_OptiInfoWavelength_Object = MibTableColumn
optiInfoWavelength = _OptiInfoWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2, 1, 4),
    _OptiInfoWavelength_Type()
)
optiInfoWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optiInfoWavelength.setStatus("current")
_OptiInfoVendorPN_Type = DisplayString
_OptiInfoVendorPN_Object = MibTableColumn
optiInfoVendorPN = _OptiInfoVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2, 1, 5),
    _OptiInfoVendorPN_Type()
)
optiInfoVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optiInfoVendorPN.setStatus("current")
_OltPortSupportedLlidNum_Type = Integer32
_OltPortSupportedLlidNum_Object = MibTableColumn
oltPortSupportedLlidNum = _OltPortSupportedLlidNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2, 1, 6),
    _OltPortSupportedLlidNum_Type()
)
oltPortSupportedLlidNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltPortSupportedLlidNum.setStatus("current")
_OltPortSoftwareVersion_Type = DisplayString
_OltPortSoftwareVersion_Object = MibTableColumn
oltPortSoftwareVersion = _OltPortSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2, 1, 7),
    _OltPortSoftwareVersion_Type()
)
oltPortSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltPortSoftwareVersion.setStatus("current")
_OltPortAGCLockTime_Type = Integer32
_OltPortAGCLockTime_Object = MibTableColumn
oltPortAGCLockTime = _OltPortAGCLockTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2, 1, 8),
    _OltPortAGCLockTime_Type()
)
oltPortAGCLockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltPortAGCLockTime.setStatus("current")
_OltPortCDRLockTime_Type = Integer32
_OltPortCDRLockTime_Object = MibTableColumn
oltPortCDRLockTime = _OltPortCDRLockTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 2, 1, 9),
    _OltPortCDRLockTime_Type()
)
oltPortCDRLockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltPortCDRLockTime.setStatus("current")
_Zxr10EponOltEncryptTable_Object = MibTable
zxr10EponOltEncryptTable = _Zxr10EponOltEncryptTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3)
)
if mibBuilder.loadTexts:
    zxr10EponOltEncryptTable.setStatus("current")
_Zxr10EponOltEncryptEntry_Object = MibTableRow
zxr10EponOltEncryptEntry = _Zxr10EponOltEncryptEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1)
)
zxr10EponOltEncryptEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxr10EponOltEncryptEntry.setStatus("current")


class _OltEncryptAlgorithm_Type(Integer32):
    """Custom type oltEncryptAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("triple-churning", 1))
    )


_OltEncryptAlgorithm_Type.__name__ = "Integer32"
_OltEncryptAlgorithm_Object = MibTableColumn
oltEncryptAlgorithm = _OltEncryptAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 1),
    _OltEncryptAlgorithm_Type()
)
oltEncryptAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltEncryptAlgorithm.setStatus("current")


class _OltKeyUpdatePeriod_Type(Integer32):
    """Custom type oltKeyUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OltKeyUpdatePeriod_Type.__name__ = "Integer32"
_OltKeyUpdatePeriod_Object = MibTableColumn
oltKeyUpdatePeriod = _OltKeyUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 2),
    _OltKeyUpdatePeriod_Type()
)
oltKeyUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltKeyUpdatePeriod.setStatus("current")


class _OltChurningTimer_Type(Integer32):
    """Custom type oltChurningTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OltChurningTimer_Type.__name__ = "Integer32"
_OltChurningTimer_Object = MibTableColumn
oltChurningTimer = _OltChurningTimer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 3),
    _OltChurningTimer_Type()
)
oltChurningTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltChurningTimer.setStatus("current")


class _OltMaxRtt_Type(Integer32):
    """Custom type oltMaxRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 25000),
    )


_OltMaxRtt_Type.__name__ = "Integer32"
_OltMaxRtt_Object = MibTableColumn
oltMaxRtt = _OltMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 4),
    _OltMaxRtt_Type()
)
oltMaxRtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltMaxRtt.setStatus("current")


class _OltLaserSwitch_Type(Integer32):
    """Custom type oltLaserSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_OltLaserSwitch_Type.__name__ = "Integer32"
_OltLaserSwitch_Object = MibTableColumn
oltLaserSwitch = _OltLaserSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 5),
    _OltLaserSwitch_Type()
)
oltLaserSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltLaserSwitch.setStatus("current")
_OpticsMeasureLow_Type = Integer32
_OpticsMeasureLow_Object = MibTableColumn
opticsMeasureLow = _OpticsMeasureLow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 6),
    _OpticsMeasureLow_Type()
)
opticsMeasureLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticsMeasureLow.setStatus("current")
_OpticsMeasureHigh_Type = Integer32
_OpticsMeasureHigh_Object = MibTableColumn
opticsMeasureHigh = _OpticsMeasureHigh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 7),
    _OpticsMeasureHigh_Type()
)
opticsMeasureHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticsMeasureHigh.setStatus("current")
_PacketLimitType_Type = DisplayString
_PacketLimitType_Object = MibTableColumn
packetLimitType = _PacketLimitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 8),
    _PacketLimitType_Type()
)
packetLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    packetLimitType.setStatus("current")


class _PacketLimitSwitch_Type(Integer32):
    """Custom type packetLimitSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PacketLimitSwitch_Type.__name__ = "Integer32"
_PacketLimitSwitch_Object = MibTableColumn
packetLimitSwitch = _PacketLimitSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 9),
    _PacketLimitSwitch_Type()
)
packetLimitSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    packetLimitSwitch.setStatus("current")
_ProtocolProtectMode_Type = DisplayString
_ProtocolProtectMode_Object = MibTableColumn
protocolProtectMode = _ProtocolProtectMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 10),
    _ProtocolProtectMode_Type()
)
protocolProtectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolProtectMode.setStatus("current")


class _ProtocolProtectSwitch_Type(Integer32):
    """Custom type protocolProtectSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ProtocolProtectSwitch_Type.__name__ = "Integer32"
_ProtocolProtectSwitch_Object = MibTableColumn
protocolProtectSwitch = _ProtocolProtectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 11),
    _ProtocolProtectSwitch_Type()
)
protocolProtectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolProtectSwitch.setStatus("current")
_OptiDiagInterval_Type = Integer32
_OptiDiagInterval_Object = MibTableColumn
optiDiagInterval = _OptiDiagInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 12),
    _OptiDiagInterval_Type()
)
optiDiagInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optiDiagInterval.setStatus("current")
_OltEncryptRowStatus_Type = RowStatus
_OltEncryptRowStatus_Object = MibTableColumn
oltEncryptRowStatus = _OltEncryptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 13),
    _OltEncryptRowStatus_Type()
)
oltEncryptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltEncryptRowStatus.setStatus("current")


class _OltPortDBAType_Type(Integer32):
    """Custom type oltPortDBAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("archimedes", 0),
          ("plato", 2),
          ("thales", 1))
    )


_OltPortDBAType_Type.__name__ = "Integer32"
_OltPortDBAType_Object = MibTableColumn
oltPortDBAType = _OltPortDBAType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 3, 1, 14),
    _OltPortDBAType_Type()
)
oltPortDBAType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltPortDBAType.setStatus("current")
_Zxr10EponOnuAuthInfoTable_Object = MibTable
zxr10EponOnuAuthInfoTable = _Zxr10EponOnuAuthInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4)
)
if mibBuilder.loadTexts:
    zxr10EponOnuAuthInfoTable.setStatus("current")
_Zxr10EponOnuAuthInfoEntry_Object = MibTableRow
zxr10EponOnuAuthInfoEntry = _Zxr10EponOnuAuthInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1)
)
zxr10EponOnuAuthInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-EPON-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    zxr10EponOnuAuthInfoEntry.setStatus("current")


class _OnuId_Type(Integer32):
    """Custom type onuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_OnuId_Type.__name__ = "Integer32"
_OnuId_Object = MibTableColumn
onuId = _OnuId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 1),
    _OnuId_Type()
)
onuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuId.setStatus("current")


class _OnuAuthState_Type(Integer32):
    """Custom type onuAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("offline", 0),
          ("up", 1))
    )


_OnuAuthState_Type.__name__ = "Integer32"
_OnuAuthState_Object = MibTableColumn
onuAuthState = _OnuAuthState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 2),
    _OnuAuthState_Type()
)
onuAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAuthState.setStatus("current")


class _OnuType_Type(Integer32):
    """Custom type onuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mac", 0),
          ("sn", 1))
    )


_OnuType_Type.__name__ = "Integer32"
_OnuType_Object = MibTableColumn
onuType = _OnuType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 3),
    _OnuType_Type()
)
onuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuType.setStatus("current")
_OnuAuthPCBVer_Type = DisplayString
_OnuAuthPCBVer_Object = MibTableColumn
onuAuthPCBVer = _OnuAuthPCBVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 4),
    _OnuAuthPCBVer_Type()
)
onuAuthPCBVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAuthPCBVer.setStatus("current")
_OnuAuthSoftVer_Type = DisplayString
_OnuAuthSoftVer_Object = MibTableColumn
onuAuthSoftVer = _OnuAuthSoftVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 5),
    _OnuAuthSoftVer_Type()
)
onuAuthSoftVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAuthSoftVer.setStatus("current")
_OnuEEPROMVer_Type = DisplayString
_OnuEEPROMVer_Object = MibTableColumn
onuEEPROMVer = _OnuEEPROMVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 6),
    _OnuEEPROMVer_Type()
)
onuEEPROMVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuEEPROMVer.setStatus("current")
_OnuHostType_Type = DisplayString
_OnuHostType_Object = MibTableColumn
onuHostType = _OnuHostType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 7),
    _OnuHostType_Type()
)
onuHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuHostType.setStatus("current")
_OnuOpticalLen_Type = Integer32
_OnuOpticalLen_Object = MibTableColumn
onuOpticalLen = _OnuOpticalLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 8),
    _OnuOpticalLen_Type()
)
onuOpticalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuOpticalLen.setStatus("current")
_OnuHardVer_Type = DisplayString
_OnuHardVer_Object = MibTableColumn
onuHardVer = _OnuHardVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 9),
    _OnuHardVer_Type()
)
onuHardVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuHardVer.setStatus("current")
_OnuRTT_Type = Integer32
_OnuRTT_Object = MibTableColumn
onuRTT = _OnuRTT_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 10),
    _OnuRTT_Type()
)
onuRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuRTT.setStatus("current")
_OnuMacPortName_Type = DisplayString
_OnuMacPortName_Object = MibTableColumn
onuMacPortName = _OnuMacPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 11),
    _OnuMacPortName_Type()
)
onuMacPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuMacPortName.setStatus("current")
_OnuBindTypeName_Type = DisplayString
_OnuBindTypeName_Object = MibTableColumn
onuBindTypeName = _OnuBindTypeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 12),
    _OnuBindTypeName_Type()
)
onuBindTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuBindTypeName.setStatus("current")
_OnuBindMacAddr_Type = MacAddress
_OnuBindMacAddr_Object = MibTableColumn
onuBindMacAddr = _OnuBindMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 13),
    _OnuBindMacAddr_Type()
)
onuBindMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuBindMacAddr.setStatus("current")
_OnuBindSN_Type = Integer32
_OnuBindSN_Object = MibTableColumn
onuBindSN = _OnuBindSN_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 14),
    _OnuBindSN_Type()
)
onuBindSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuBindSN.setStatus("current")


class _OnuMacMaxNum_Type(Integer32):
    """Custom type onuMacMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_OnuMacMaxNum_Type.__name__ = "Integer32"
_OnuMacMaxNum_Object = MibTableColumn
onuMacMaxNum = _OnuMacMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 15),
    _OnuMacMaxNum_Type()
)
onuMacMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMacMaxNum.setStatus("current")
_OnuBindRowStatus_Type = RowStatus
_OnuBindRowStatus_Object = MibTableColumn
onuBindRowStatus = _OnuBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 4, 1, 16),
    _OnuBindRowStatus_Type()
)
onuBindRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuBindRowStatus.setStatus("current")
_Zxr10EponOltPortStatTable_Object = MibTable
zxr10EponOltPortStatTable = _Zxr10EponOltPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5)
)
if mibBuilder.loadTexts:
    zxr10EponOltPortStatTable.setStatus("current")
_Zxr10EponOltPortStatEntry_Object = MibTableRow
zxr10EponOltPortStatEntry = _Zxr10EponOltPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1)
)
zxr10EponOltPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxr10EponOltPortStatEntry.setStatus("current")
_OltStatisBer_Type = Counter64
_OltStatisBer_Object = MibTableColumn
oltStatisBer = _OltStatisBer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 1),
    _OltStatisBer_Type()
)
oltStatisBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisBer.setStatus("current")
_OltStatisFer_Type = Counter64
_OltStatisFer_Object = MibTableColumn
oltStatisFer = _OltStatisFer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 2),
    _OltStatisFer_Type()
)
oltStatisFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisFer.setStatus("current")
_OltStatisPortBer_Type = Counter64
_OltStatisPortBer_Object = MibTableColumn
oltStatisPortBer = _OltStatisPortBer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 3),
    _OltStatisPortBer_Type()
)
oltStatisPortBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisPortBer.setStatus("current")
_OltStatisInPkts_Type = Counter64
_OltStatisInPkts_Object = MibTableColumn
oltStatisInPkts = _OltStatisInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 4),
    _OltStatisInPkts_Type()
)
oltStatisInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisInPkts.setStatus("current")
_OltStatisInOctes_Type = Counter64
_OltStatisInOctes_Object = MibTableColumn
oltStatisInOctes = _OltStatisInOctes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 5),
    _OltStatisInOctes_Type()
)
oltStatisInOctes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisInOctes.setStatus("current")
_OltStatisInUniPkts_Type = Counter64
_OltStatisInUniPkts_Object = MibTableColumn
oltStatisInUniPkts = _OltStatisInUniPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 6),
    _OltStatisInUniPkts_Type()
)
oltStatisInUniPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisInUniPkts.setStatus("current")
_OltStatisInMultiPkts_Type = Counter64
_OltStatisInMultiPkts_Object = MibTableColumn
oltStatisInMultiPkts = _OltStatisInMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 7),
    _OltStatisInMultiPkts_Type()
)
oltStatisInMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisInMultiPkts.setStatus("current")
_OltStatisInBroadPkts_Type = Counter64
_OltStatisInBroadPkts_Object = MibTableColumn
oltStatisInBroadPkts = _OltStatisInBroadPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 8),
    _OltStatisInBroadPkts_Type()
)
oltStatisInBroadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisInBroadPkts.setStatus("current")
_OltStatisOutPkts_Type = Counter64
_OltStatisOutPkts_Object = MibTableColumn
oltStatisOutPkts = _OltStatisOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 9),
    _OltStatisOutPkts_Type()
)
oltStatisOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisOutPkts.setStatus("current")
_OltStatisOutOctes_Type = Counter64
_OltStatisOutOctes_Object = MibTableColumn
oltStatisOutOctes = _OltStatisOutOctes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 10),
    _OltStatisOutOctes_Type()
)
oltStatisOutOctes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisOutOctes.setStatus("current")
_OltStatisOutUniPkts_Type = Counter64
_OltStatisOutUniPkts_Object = MibTableColumn
oltStatisOutUniPkts = _OltStatisOutUniPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 11),
    _OltStatisOutUniPkts_Type()
)
oltStatisOutUniPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisOutUniPkts.setStatus("current")
_OltStatisOutMultiPkts_Type = Counter64
_OltStatisOutMultiPkts_Object = MibTableColumn
oltStatisOutMultiPkts = _OltStatisOutMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 12),
    _OltStatisOutMultiPkts_Type()
)
oltStatisOutMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisOutMultiPkts.setStatus("current")
_OltStatisOutBroadPkts_Type = Counter64
_OltStatisOutBroadPkts_Object = MibTableColumn
oltStatisOutBroadPkts = _OltStatisOutBroadPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 13),
    _OltStatisOutBroadPkts_Type()
)
oltStatisOutBroadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltStatisOutBroadPkts.setStatus("current")
_OamFramesCounters_Type = Counter64
_OamFramesCounters_Object = MibTableColumn
oamFramesCounters = _OamFramesCounters_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 14),
    _OamFramesCounters_Type()
)
oamFramesCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamFramesCounters.setStatus("current")
_StandardOamStatistics_Type = Counter64
_StandardOamStatistics_Object = MibTableColumn
standardOamStatistics = _StandardOamStatistics_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 15),
    _StandardOamStatistics_Type()
)
standardOamStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standardOamStatistics.setStatus("current")
_StandardOamMpcpStatistic_Type = Counter64
_StandardOamMpcpStatistic_Object = MibTableColumn
standardOamMpcpStatistic = _StandardOamMpcpStatistic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 16),
    _StandardOamMpcpStatistic_Type()
)
standardOamMpcpStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standardOamMpcpStatistic.setStatus("current")
_CpuPortsOctets_Type = Counter64
_CpuPortsOctets_Object = MibTableColumn
cpuPortsOctets = _CpuPortsOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 17),
    _CpuPortsOctets_Type()
)
cpuPortsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPortsOctets.setStatus("current")
_CpuPortsFrames_Type = Counter64
_CpuPortsFrames_Object = MibTableColumn
cpuPortsFrames = _CpuPortsFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 18),
    _CpuPortsFrames_Type()
)
cpuPortsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPortsFrames.setStatus("current")
_TransmittedFramesPerLLID_Type = Counter64
_TransmittedFramesPerLLID_Object = MibTableColumn
transmittedFramesPerLLID = _TransmittedFramesPerLLID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 19),
    _TransmittedFramesPerLLID_Type()
)
transmittedFramesPerLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmittedFramesPerLLID.setStatus("current")
_DroppedFramesPerLLID_Type = Counter64
_DroppedFramesPerLLID_Object = MibTableColumn
droppedFramesPerLLID = _DroppedFramesPerLLID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 20),
    _DroppedFramesPerLLID_Type()
)
droppedFramesPerLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    droppedFramesPerLLID.setStatus("current")
_TransmittedOctetsPerLLID_Type = Counter64
_TransmittedOctetsPerLLID_Object = MibTableColumn
transmittedOctetsPerLLID = _TransmittedOctetsPerLLID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 21),
    _TransmittedOctetsPerLLID_Type()
)
transmittedOctetsPerLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmittedOctetsPerLLID.setStatus("current")
_InRangeLengthErrorsPerLLID_Type = Counter64
_InRangeLengthErrorsPerLLID_Object = MibTableColumn
inRangeLengthErrorsPerLLID = _InRangeLengthErrorsPerLLID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 22),
    _InRangeLengthErrorsPerLLID_Type()
)
inRangeLengthErrorsPerLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inRangeLengthErrorsPerLLID.setStatus("current")
_FrameTooLongErrorsPerLLID_Type = Counter64
_FrameTooLongErrorsPerLLID_Object = MibTableColumn
frameTooLongErrorsPerLLID = _FrameTooLongErrorsPerLLID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 5, 1, 23),
    _FrameTooLongErrorsPerLLID_Type()
)
frameTooLongErrorsPerLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameTooLongErrorsPerLLID.setStatus("current")
_Zxr10EponOnuPortStatTable_Object = MibTable
zxr10EponOnuPortStatTable = _Zxr10EponOnuPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6)
)
if mibBuilder.loadTexts:
    zxr10EponOnuPortStatTable.setStatus("current")
_Zxr10EponOnuPortStatEntry_Object = MibTableRow
zxr10EponOnuPortStatEntry = _Zxr10EponOnuPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1)
)
zxr10EponOnuPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-EPON-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    zxr10EponOnuPortStatEntry.setStatus("current")
_OnuStatisBer_Type = Counter64
_OnuStatisBer_Object = MibTableColumn
onuStatisBer = _OnuStatisBer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1, 1),
    _OnuStatisBer_Type()
)
onuStatisBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuStatisBer.setStatus("current")
_OnuStatisFer_Type = Counter64
_OnuStatisFer_Object = MibTableColumn
onuStatisFer = _OnuStatisFer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1, 2),
    _OnuStatisFer_Type()
)
onuStatisFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuStatisFer.setStatus("current")
_OnuStatisInPkts_Type = Counter64
_OnuStatisInPkts_Object = MibTableColumn
onuStatisInPkts = _OnuStatisInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1, 3),
    _OnuStatisInPkts_Type()
)
onuStatisInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuStatisInPkts.setStatus("current")
_OnuStatisInOctes_Type = Counter64
_OnuStatisInOctes_Object = MibTableColumn
onuStatisInOctes = _OnuStatisInOctes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1, 4),
    _OnuStatisInOctes_Type()
)
onuStatisInOctes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuStatisInOctes.setStatus("current")
_OnuStatisInMultiPkts_Type = Counter64
_OnuStatisInMultiPkts_Object = MibTableColumn
onuStatisInMultiPkts = _OnuStatisInMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1, 5),
    _OnuStatisInMultiPkts_Type()
)
onuStatisInMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuStatisInMultiPkts.setStatus("current")
_OnuStatisInBroadPkts_Type = Counter64
_OnuStatisInBroadPkts_Object = MibTableColumn
onuStatisInBroadPkts = _OnuStatisInBroadPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1, 6),
    _OnuStatisInBroadPkts_Type()
)
onuStatisInBroadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuStatisInBroadPkts.setStatus("current")
_OnuStatisOutPkts_Type = Counter64
_OnuStatisOutPkts_Object = MibTableColumn
onuStatisOutPkts = _OnuStatisOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1, 7),
    _OnuStatisOutPkts_Type()
)
onuStatisOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuStatisOutPkts.setStatus("current")
_OnuStatisOutOctes_Type = Counter64
_OnuStatisOutOctes_Object = MibTableColumn
onuStatisOutOctes = _OnuStatisOutOctes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1, 8),
    _OnuStatisOutOctes_Type()
)
onuStatisOutOctes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuStatisOutOctes.setStatus("current")
_OnuStatisOutMultiPkts_Type = Counter64
_OnuStatisOutMultiPkts_Object = MibTableColumn
onuStatisOutMultiPkts = _OnuStatisOutMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1, 9),
    _OnuStatisOutMultiPkts_Type()
)
onuStatisOutMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuStatisOutMultiPkts.setStatus("current")
_OnuStatisOutBroadPkts_Type = Counter64
_OnuStatisOutBroadPkts_Object = MibTableColumn
onuStatisOutBroadPkts = _OnuStatisOutBroadPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 6, 1, 10),
    _OnuStatisOutBroadPkts_Type()
)
onuStatisOutBroadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuStatisOutBroadPkts.setStatus("current")
_Zxr10EponProtectGroupTable_Object = MibTable
zxr10EponProtectGroupTable = _Zxr10EponProtectGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 7)
)
if mibBuilder.loadTexts:
    zxr10EponProtectGroupTable.setStatus("current")
_Zxr10EponProtectGroupEntry_Object = MibTableRow
zxr10EponProtectGroupEntry = _Zxr10EponProtectGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 7, 1)
)
zxr10EponProtectGroupEntry.setIndexNames(
    (0, "ZXR10-EPON-MIB", "protectGroupid"),
)
if mibBuilder.loadTexts:
    zxr10EponProtectGroupEntry.setStatus("current")


class _ProtectGroupid_Type(Integer32):
    """Custom type protectGroupid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ProtectGroupid_Type.__name__ = "Integer32"
_ProtectGroupid_Object = MibTableColumn
protectGroupid = _ProtectGroupid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 7, 1, 1),
    _ProtectGroupid_Type()
)
protectGroupid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectGroupid.setStatus("current")
_ProtectOltMasterIfName_Type = DisplayString
_ProtectOltMasterIfName_Object = MibTableColumn
protectOltMasterIfName = _ProtectOltMasterIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 7, 1, 2),
    _ProtectOltMasterIfName_Type()
)
protectOltMasterIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectOltMasterIfName.setStatus("current")
_ProtectOltBackupIfName_Type = DisplayString
_ProtectOltBackupIfName_Object = MibTableColumn
protectOltBackupIfName = _ProtectOltBackupIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 7, 1, 3),
    _ProtectOltBackupIfName_Type()
)
protectOltBackupIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectOltBackupIfName.setStatus("current")
_ProtectOltActiveIfName_Type = DisplayString
_ProtectOltActiveIfName_Object = MibTableColumn
protectOltActiveIfName = _ProtectOltActiveIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 7, 1, 4),
    _ProtectOltActiveIfName_Type()
)
protectOltActiveIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectOltActiveIfName.setStatus("current")
_ProtectOltEnableSwitch_Type = Integer32
_ProtectOltEnableSwitch_Object = MibTableColumn
protectOltEnableSwitch = _ProtectOltEnableSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 7, 1, 5),
    _ProtectOltEnableSwitch_Type()
)
protectOltEnableSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectOltEnableSwitch.setStatus("current")
_ProtectReverEnable_Type = Integer32
_ProtectReverEnable_Object = MibTableColumn
protectReverEnable = _ProtectReverEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 7, 1, 6),
    _ProtectReverEnable_Type()
)
protectReverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectReverEnable.setStatus("current")


class _ProtectReverTime_Type(Integer32):
    """Custom type protectReverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProtectReverTime_Type.__name__ = "Integer32"
_ProtectReverTime_Object = MibTableColumn
protectReverTime = _ProtectReverTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 7, 1, 7),
    _ProtectReverTime_Type()
)
protectReverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectReverTime.setStatus("current")
_ProtectRowStatus_Type = RowStatus
_ProtectRowStatus_Object = MibTableColumn
protectRowStatus = _ProtectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 7, 1, 8),
    _ProtectRowStatus_Type()
)
protectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectRowStatus.setStatus("current")
_Zxr10EponSwitchRecordTable_Object = MibTable
zxr10EponSwitchRecordTable = _Zxr10EponSwitchRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 8)
)
if mibBuilder.loadTexts:
    zxr10EponSwitchRecordTable.setStatus("current")
_Zxr10EponSwitchRecordEntry_Object = MibTableRow
zxr10EponSwitchRecordEntry = _Zxr10EponSwitchRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 8, 1)
)
zxr10EponSwitchRecordEntry.setIndexNames(
    (0, "ZXR10-EPON-MIB", "switchRecordGroupid"),
    (0, "ZXR10-EPON-MIB", "switchRecordNum"),
)
if mibBuilder.loadTexts:
    zxr10EponSwitchRecordEntry.setStatus("current")


class _SwitchRecordGroupid_Type(Integer32):
    """Custom type switchRecordGroupid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwitchRecordGroupid_Type.__name__ = "Integer32"
_SwitchRecordGroupid_Object = MibTableColumn
switchRecordGroupid = _SwitchRecordGroupid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 8, 1, 1),
    _SwitchRecordGroupid_Type()
)
switchRecordGroupid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRecordGroupid.setStatus("current")


class _SwitchRecordNum_Type(Integer32):
    """Custom type switchRecordNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SwitchRecordNum_Type.__name__ = "Integer32"
_SwitchRecordNum_Object = MibTableColumn
switchRecordNum = _SwitchRecordNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 8, 1, 2),
    _SwitchRecordNum_Type()
)
switchRecordNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRecordNum.setStatus("current")
_SwitchTime_Type = DisplayString
_SwitchTime_Object = MibTableColumn
switchTime = _SwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 8, 1, 3),
    _SwitchTime_Type()
)
switchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchTime.setStatus("current")


class _SwitchType_Type(Integer32):
    """Custom type switchType based on Integer32"""
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
        *(("alarm", 4),
          ("auto", 1),
          ("force", 2),
          ("ifchange", 5),
          ("retiver", 3))
    )


_SwitchType_Type.__name__ = "Integer32"
_SwitchType_Object = MibTableColumn
switchType = _SwitchType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 8, 1, 4),
    _SwitchType_Type()
)
switchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchType.setStatus("current")


class _SwitchTypeMtoB_Type(Integer32):
    """Custom type switchTypeMtoB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SwitchTypeMtoB_Type.__name__ = "Integer32"
_SwitchTypeMtoB_Object = MibTableColumn
switchTypeMtoB = _SwitchTypeMtoB_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 8, 1, 5),
    _SwitchTypeMtoB_Type()
)
switchTypeMtoB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchTypeMtoB.setStatus("current")
_Zxr10EponAlarmTable_Object = MibTable
zxr10EponAlarmTable = _Zxr10EponAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 9)
)
if mibBuilder.loadTexts:
    zxr10EponAlarmTable.setStatus("current")
_Zxr10EponAlarmEntry_Object = MibTableRow
zxr10EponAlarmEntry = _Zxr10EponAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 9, 1)
)
zxr10EponAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxr10EponAlarmEntry.setStatus("current")
_OltAlarmSwitch_Type = DisplayString
_OltAlarmSwitch_Object = MibTableColumn
oltAlarmSwitch = _OltAlarmSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 9, 1, 1),
    _OltAlarmSwitch_Type()
)
oltAlarmSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltAlarmSwitch.setStatus("current")
_OltAlarmDirectSwitch_Type = DisplayString
_OltAlarmDirectSwitch_Object = MibTableColumn
oltAlarmDirectSwitch = _OltAlarmDirectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 9, 1, 2),
    _OltAlarmDirectSwitch_Type()
)
oltAlarmDirectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltAlarmDirectSwitch.setStatus("current")
_OltAlarmThreshold_Type = DisplayString
_OltAlarmThreshold_Object = MibTableColumn
oltAlarmThreshold = _OltAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 1, 9, 1, 3),
    _OltAlarmThreshold_Type()
)
oltAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltAlarmThreshold.setStatus("current")
_Zxr10EponRemoteOnu_ObjectIdentity = ObjectIdentity
zxr10EponRemoteOnu = _Zxr10EponRemoteOnu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2)
)
_Zxr10EponRemoteOnuInfoTable_Object = MibTable
zxr10EponRemoteOnuInfoTable = _Zxr10EponRemoteOnuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1)
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuInfoTable.setStatus("current")
_Zxr10EponRemoteOnuInfoEntry_Object = MibTableRow
zxr10EponRemoteOnuInfoEntry = _Zxr10EponRemoteOnuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1)
)
zxr10EponRemoteOnuInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-EPON-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuInfoEntry.setStatus("current")
_RemoteOnuVendorId_Type = DisplayString
_RemoteOnuVendorId_Object = MibTableColumn
remoteOnuVendorId = _RemoteOnuVendorId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 1),
    _RemoteOnuVendorId_Type()
)
remoteOnuVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOnuVendorId.setStatus("current")
_RemoteOnuModel_Type = DisplayString
_RemoteOnuModel_Object = MibTableColumn
remoteOnuModel = _RemoteOnuModel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 2),
    _RemoteOnuModel_Type()
)
remoteOnuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOnuModel.setStatus("current")
_RemoteOnuId_Type = MacAddress
_RemoteOnuId_Object = MibTableColumn
remoteOnuId = _RemoteOnuId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 3),
    _RemoteOnuId_Type()
)
remoteOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOnuId.setStatus("current")
_RemoteHardwareVersion_Type = DisplayString
_RemoteHardwareVersion_Object = MibTableColumn
remoteHardwareVersion = _RemoteHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 4),
    _RemoteHardwareVersion_Type()
)
remoteHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteHardwareVersion.setStatus("current")
_RemoteSoftwareVersion_Type = DisplayString
_RemoteSoftwareVersion_Object = MibTableColumn
remoteSoftwareVersion = _RemoteSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 5),
    _RemoteSoftwareVersion_Type()
)
remoteSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSoftwareVersion.setStatus("current")
_RemoteFirmwareVersion_Type = DisplayString
_RemoteFirmwareVersion_Object = MibTableColumn
remoteFirmwareVersion = _RemoteFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 6),
    _RemoteFirmwareVersion_Type()
)
remoteFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFirmwareVersion.setStatus("current")
_RemoteChipVendorId_Type = DisplayString
_RemoteChipVendorId_Object = MibTableColumn
remoteChipVendorId = _RemoteChipVendorId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 7),
    _RemoteChipVendorId_Type()
)
remoteChipVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteChipVendorId.setStatus("current")
_RemoteChipModel_Type = DisplayString
_RemoteChipModel_Object = MibTableColumn
remoteChipModel = _RemoteChipModel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 8),
    _RemoteChipModel_Type()
)
remoteChipModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteChipModel.setStatus("current")
_RemoteChipRevison_Type = DisplayString
_RemoteChipRevison_Object = MibTableColumn
remoteChipRevison = _RemoteChipRevison_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 9),
    _RemoteChipRevison_Type()
)
remoteChipRevison.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteChipRevison.setStatus("current")
_RemoteIcVersion_Type = DisplayString
_RemoteIcVersion_Object = MibTableColumn
remoteIcVersion = _RemoteIcVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 10),
    _RemoteIcVersion_Type()
)
remoteIcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIcVersion.setStatus("current")
_RemoteGePortNum_Type = Integer32
_RemoteGePortNum_Object = MibTableColumn
remoteGePortNum = _RemoteGePortNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 11),
    _RemoteGePortNum_Type()
)
remoteGePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteGePortNum.setStatus("current")
_RemoteBitmapGePort_Type = DisplayString
_RemoteBitmapGePort_Object = MibTableColumn
remoteBitmapGePort = _RemoteBitmapGePort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 12),
    _RemoteBitmapGePort_Type()
)
remoteBitmapGePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteBitmapGePort.setStatus("current")
_RemoteFePortNum_Type = Integer32
_RemoteFePortNum_Object = MibTableColumn
remoteFePortNum = _RemoteFePortNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 13),
    _RemoteFePortNum_Type()
)
remoteFePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFePortNum.setStatus("current")
_RemoteBitmapFePort_Type = DisplayString
_RemoteBitmapFePort_Object = MibTableColumn
remoteBitmapFePort = _RemoteBitmapFePort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 14),
    _RemoteBitmapFePort_Type()
)
remoteBitmapFePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteBitmapFePort.setStatus("current")
_RemotePortsNum_Type = Integer32
_RemotePortsNum_Object = MibTableColumn
remotePortsNum = _RemotePortsNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 15),
    _RemotePortsNum_Type()
)
remotePortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortsNum.setStatus("current")
_RemoteE1PortNum_Type = Integer32
_RemoteE1PortNum_Object = MibTableColumn
remoteE1PortNum = _RemoteE1PortNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 16),
    _RemoteE1PortNum_Type()
)
remoteE1PortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteE1PortNum.setStatus("current")
_RemoteUsQueuesNum_Type = Integer32
_RemoteUsQueuesNum_Object = MibTableColumn
remoteUsQueuesNum = _RemoteUsQueuesNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 17),
    _RemoteUsQueuesNum_Type()
)
remoteUsQueuesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUsQueuesNum.setStatus("current")
_RemoteMaxQueuesPerUSport_Type = Integer32
_RemoteMaxQueuesPerUSport_Object = MibTableColumn
remoteMaxQueuesPerUSport = _RemoteMaxQueuesPerUSport_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 18),
    _RemoteMaxQueuesPerUSport_Type()
)
remoteMaxQueuesPerUSport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMaxQueuesPerUSport.setStatus("current")
_RemoteDSQueuesNum_Type = Integer32
_RemoteDSQueuesNum_Object = MibTableColumn
remoteDSQueuesNum = _RemoteDSQueuesNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 19),
    _RemoteDSQueuesNum_Type()
)
remoteDSQueuesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDSQueuesNum.setStatus("current")
_RemoteMaxQueuesPerDSport_Type = Integer32
_RemoteMaxQueuesPerDSport_Object = MibTableColumn
remoteMaxQueuesPerDSport = _RemoteMaxQueuesPerDSport_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 20),
    _RemoteMaxQueuesPerDSport_Type()
)
remoteMaxQueuesPerDSport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMaxQueuesPerDSport.setStatus("current")


class _RemoteBatteryBackup_Type(Integer32):
    """Custom type remoteBatteryBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RemoteBatteryBackup_Type.__name__ = "Integer32"
_RemoteBatteryBackup_Object = MibTableColumn
remoteBatteryBackup = _RemoteBatteryBackup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 1, 1, 21),
    _RemoteBatteryBackup_Type()
)
remoteBatteryBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteBatteryBackup.setStatus("current")
_Zxr10EponRemoteOnuDbaTable_Object = MibTable
zxr10EponRemoteOnuDbaTable = _Zxr10EponRemoteOnuDbaTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2)
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuDbaTable.setStatus("current")
_Zxr10EponRemoteOnuDbaEntry_Object = MibTableRow
zxr10EponRemoteOnuDbaEntry = _Zxr10EponRemoteOnuDbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1)
)
zxr10EponRemoteOnuDbaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-EPON-MIB", "onuId"),
    (0, "ZXR10-EPON-MIB", "queueSetId"),
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuDbaEntry.setStatus("current")


class _QueueSetId_Type(Integer32):
    """Custom type queueSetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_QueueSetId_Type.__name__ = "Integer32"
_QueueSetId_Object = MibTableColumn
queueSetId = _QueueSetId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 1),
    _QueueSetId_Type()
)
queueSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueSetId.setStatus("current")


class _QueueValue1_Type(Integer32):
    """Custom type queueValue1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QueueValue1_Type.__name__ = "Integer32"
_QueueValue1_Object = MibTableColumn
queueValue1 = _QueueValue1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 2),
    _QueueValue1_Type()
)
queueValue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueValue1.setStatus("current")


class _QueueValue2_Type(Integer32):
    """Custom type queueValue2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QueueValue2_Type.__name__ = "Integer32"
_QueueValue2_Object = MibTableColumn
queueValue2 = _QueueValue2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 3),
    _QueueValue2_Type()
)
queueValue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueValue2.setStatus("current")


class _QueueValue3_Type(Integer32):
    """Custom type queueValue3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QueueValue3_Type.__name__ = "Integer32"
_QueueValue3_Object = MibTableColumn
queueValue3 = _QueueValue3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 4),
    _QueueValue3_Type()
)
queueValue3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueValue3.setStatus("current")


class _QueueValue4_Type(Integer32):
    """Custom type queueValue4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QueueValue4_Type.__name__ = "Integer32"
_QueueValue4_Object = MibTableColumn
queueValue4 = _QueueValue4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 5),
    _QueueValue4_Type()
)
queueValue4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueValue4.setStatus("current")


class _QueueValue5_Type(Integer32):
    """Custom type queueValue5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QueueValue5_Type.__name__ = "Integer32"
_QueueValue5_Object = MibTableColumn
queueValue5 = _QueueValue5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 6),
    _QueueValue5_Type()
)
queueValue5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueValue5.setStatus("current")


class _QueueValue6_Type(Integer32):
    """Custom type queueValue6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QueueValue6_Type.__name__ = "Integer32"
_QueueValue6_Object = MibTableColumn
queueValue6 = _QueueValue6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 7),
    _QueueValue6_Type()
)
queueValue6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueValue6.setStatus("current")


class _QueueValue7_Type(Integer32):
    """Custom type queueValue7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QueueValue7_Type.__name__ = "Integer32"
_QueueValue7_Object = MibTableColumn
queueValue7 = _QueueValue7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 8),
    _QueueValue7_Type()
)
queueValue7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueValue7.setStatus("current")


class _QueueValue8_Type(Integer32):
    """Custom type queueValue8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QueueValue8_Type.__name__ = "Integer32"
_QueueValue8_Object = MibTableColumn
queueValue8 = _QueueValue8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 9),
    _QueueValue8_Type()
)
queueValue8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueValue8.setStatus("current")


class _DbaQueueActive_Type(Integer32):
    """Custom type dbaQueueActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DbaQueueActive_Type.__name__ = "Integer32"
_DbaQueueActive_Object = MibTableColumn
dbaQueueActive = _DbaQueueActive_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 10),
    _DbaQueueActive_Type()
)
dbaQueueActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbaQueueActive.setStatus("current")
_OnuDbaRowStatus_Type = RowStatus
_OnuDbaRowStatus_Object = MibTableColumn
onuDbaRowStatus = _OnuDbaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 2, 1, 11),
    _OnuDbaRowStatus_Type()
)
onuDbaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuDbaRowStatus.setStatus("current")
_Zxr10EponRemoteOnuClassRuleTable_Object = MibTable
zxr10EponRemoteOnuClassRuleTable = _Zxr10EponRemoteOnuClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 3)
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuClassRuleTable.setStatus("current")
_Zxr10EponRemoteOnuClassRuleEntry_Object = MibTableRow
zxr10EponRemoteOnuClassRuleEntry = _Zxr10EponRemoteOnuClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 3, 1)
)
zxr10EponRemoteOnuClassRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-EPON-MIB", "onuId"),
    (0, "ZXR10-EPON-MIB", "ruleProfileNum"),
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuClassRuleEntry.setStatus("current")


class _RuleProfileNum_Type(Integer32):
    """Custom type ruleProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RuleProfileNum_Type.__name__ = "Integer32"
_RuleProfileNum_Object = MibTableColumn
ruleProfileNum = _RuleProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 3, 1, 1),
    _RuleProfileNum_Type()
)
ruleProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleProfileNum.setStatus("current")


class _QueueVlaue_Type(Integer32):
    """Custom type queueVlaue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QueueVlaue_Type.__name__ = "Integer32"
_QueueVlaue_Object = MibTableColumn
queueVlaue = _QueueVlaue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 3, 1, 2),
    _QueueVlaue_Type()
)
queueVlaue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueVlaue.setStatus("current")


class _PriorityValue_Type(Integer32):
    """Custom type priorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PriorityValue_Type.__name__ = "Integer32"
_PriorityValue_Object = MibTableColumn
priorityValue = _PriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 3, 1, 3),
    _PriorityValue_Type()
)
priorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityValue.setStatus("current")
_RuleRowStatus_Type = RowStatus
_RuleRowStatus_Object = MibTableColumn
ruleRowStatus = _RuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 3, 1, 4),
    _RuleRowStatus_Type()
)
ruleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleRowStatus.setStatus("current")
_Zxr10EponRemoteOnuClassCondiTable_Object = MibTable
zxr10EponRemoteOnuClassCondiTable = _Zxr10EponRemoteOnuClassCondiTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4)
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuClassCondiTable.setStatus("current")
_Zxr10EponRemoteOnuClassCondiEntry_Object = MibTableRow
zxr10EponRemoteOnuClassCondiEntry = _Zxr10EponRemoteOnuClassCondiEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1)
)
zxr10EponRemoteOnuClassCondiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-EPON-MIB", "onuId"),
    (0, "ZXR10-EPON-MIB", "conditionProfileNum"),
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuClassCondiEntry.setStatus("current")


class _ConditionProfileNum_Type(Integer32):
    """Custom type conditionProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ConditionProfileNum_Type.__name__ = "Integer32"
_ConditionProfileNum_Object = MibTableColumn
conditionProfileNum = _ConditionProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 1),
    _ConditionProfileNum_Type()
)
conditionProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conditionProfileNum.setStatus("current")


class _ConditionMacAddressType_Type(Integer32):
    """Custom type conditionMacAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dest-mac", 1),
          ("null", -1),
          ("source-mac", 0))
    )


_ConditionMacAddressType_Type.__name__ = "Integer32"
_ConditionMacAddressType_Object = MibTableColumn
conditionMacAddressType = _ConditionMacAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 2),
    _ConditionMacAddressType_Type()
)
conditionMacAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionMacAddressType.setStatus("current")
_ConditionMacAddress_Type = MacAddress
_ConditionMacAddress_Object = MibTableColumn
conditionMacAddress = _ConditionMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 3),
    _ConditionMacAddress_Type()
)
conditionMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionMacAddress.setStatus("current")


class _ConditionIpAddressType_Type(Integer32):
    """Custom type conditionIpAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("destIp", 5),
          ("null", -1),
          ("sourceIp", 6))
    )


_ConditionIpAddressType_Type.__name__ = "Integer32"
_ConditionIpAddressType_Object = MibTableColumn
conditionIpAddressType = _ConditionIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 4),
    _ConditionIpAddressType_Type()
)
conditionIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionIpAddressType.setStatus("current")
_ConditionIpAddress_Type = IpAddress
_ConditionIpAddress_Object = MibTableColumn
conditionIpAddress = _ConditionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 5),
    _ConditionIpAddress_Type()
)
conditionIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionIpAddress.setStatus("current")


class _ConditionPriority_Type(Integer32):
    """Custom type conditionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ConditionPriority_Type.__name__ = "Integer32"
_ConditionPriority_Object = MibTableColumn
conditionPriority = _ConditionPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 6),
    _ConditionPriority_Type()
)
conditionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionPriority.setStatus("current")


class _ConditionVlanId_Type(Integer32):
    """Custom type conditionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ConditionVlanId_Type.__name__ = "Integer32"
_ConditionVlanId_Object = MibTableColumn
conditionVlanId = _ConditionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 7),
    _ConditionVlanId_Type()
)
conditionVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionVlanId.setStatus("current")


class _ConditionDscp_Type(Integer32):
    """Custom type conditionDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ConditionDscp_Type.__name__ = "Integer32"
_ConditionDscp_Object = MibTableColumn
conditionDscp = _ConditionDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 8),
    _ConditionDscp_Type()
)
conditionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionDscp.setStatus("current")


class _ConditionL4PortType_Type(Integer32):
    """Custom type conditionL4PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("l4DestPort", 11),
          ("l4SourcePort", 10),
          ("null", -1))
    )


_ConditionL4PortType_Type.__name__ = "Integer32"
_ConditionL4PortType_Object = MibTableColumn
conditionL4PortType = _ConditionL4PortType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 9),
    _ConditionL4PortType_Type()
)
conditionL4PortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionL4PortType.setStatus("current")


class _ConditionPortNum_Type(Integer32):
    """Custom type conditionPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 79),
    )


_ConditionPortNum_Type.__name__ = "Integer32"
_ConditionPortNum_Object = MibTableColumn
conditionPortNum = _ConditionPortNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 10),
    _ConditionPortNum_Type()
)
conditionPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionPortNum.setStatus("current")


class _ConditionEthType_Type(Integer32):
    """Custom type conditionEthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConditionEthType_Type.__name__ = "Integer32"
_ConditionEthType_Object = MibTableColumn
conditionEthType = _ConditionEthType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 11),
    _ConditionEthType_Type()
)
conditionEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionEthType.setStatus("current")


class _ConditionIpProtocolType_Type(Integer32):
    """Custom type conditionIpProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConditionIpProtocolType_Type.__name__ = "Integer32"
_ConditionIpProtocolType_Object = MibTableColumn
conditionIpProtocolType = _ConditionIpProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 12),
    _ConditionIpProtocolType_Type()
)
conditionIpProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionIpProtocolType.setStatus("current")


class _ConditionOperatorType_Type(Integer32):
    """Custom type conditionOperatorType based on Integer32"""
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
        *(("always-match", 7),
          ("equal", 1),
          ("exists", 5),
          ("greater-equal", 4),
          ("less-equal", 3),
          ("never-match", 0),
          ("not-equal", 2),
          ("not-exists", 6))
    )


_ConditionOperatorType_Type.__name__ = "Integer32"
_ConditionOperatorType_Object = MibTableColumn
conditionOperatorType = _ConditionOperatorType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 13),
    _ConditionOperatorType_Type()
)
conditionOperatorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionOperatorType.setStatus("current")
_ConditionRowStatus_Type = RowStatus
_ConditionRowStatus_Object = MibTableColumn
conditionRowStatus = _ConditionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 4, 1, 14),
    _ConditionRowStatus_Type()
)
conditionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conditionRowStatus.setStatus("current")
_Zxr10EponRemoteOnuPortTable_Object = MibTable
zxr10EponRemoteOnuPortTable = _Zxr10EponRemoteOnuPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5)
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuPortTable.setStatus("current")
_Zxr10EponRemoteOnuPortEntry_Object = MibTableRow
zxr10EponRemoteOnuPortEntry = _Zxr10EponRemoteOnuPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1)
)
zxr10EponRemoteOnuPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-EPON-MIB", "onuId"),
    (0, "ZXR10-EPON-MIB", "onuEthUniNumber"),
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuPortEntry.setStatus("current")


class _OnuEthUniNumber_Type(Integer32):
    """Custom type onuEthUniNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 79),
    )


_OnuEthUniNumber_Type.__name__ = "Integer32"
_OnuEthUniNumber_Object = MibTableColumn
onuEthUniNumber = _OnuEthUniNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 1),
    _OnuEthUniNumber_Type()
)
onuEthUniNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuEthUniNumber.setStatus("current")


class _OnuPortFlowControl_Type(Integer32):
    """Custom type onuPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuPortFlowControl_Type.__name__ = "Integer32"
_OnuPortFlowControl_Object = MibTableColumn
onuPortFlowControl = _OnuPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 2),
    _OnuPortFlowControl_Type()
)
onuPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortFlowControl.setStatus("current")


class _OnuPortUpPolicySwitch_Type(Integer32):
    """Custom type onuPortUpPolicySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuPortUpPolicySwitch_Type.__name__ = "Integer32"
_OnuPortUpPolicySwitch_Object = MibTableColumn
onuPortUpPolicySwitch = _OnuPortUpPolicySwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 3),
    _OnuPortUpPolicySwitch_Type()
)
onuPortUpPolicySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortUpPolicySwitch.setStatus("current")


class _OnuPortUpPolicyCIR_Type(Integer32):
    """Custom type onuPortUpPolicyCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OnuPortUpPolicyCIR_Type.__name__ = "Integer32"
_OnuPortUpPolicyCIR_Object = MibTableColumn
onuPortUpPolicyCIR = _OnuPortUpPolicyCIR_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 4),
    _OnuPortUpPolicyCIR_Type()
)
onuPortUpPolicyCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortUpPolicyCIR.setStatus("current")


class _OnuPortUpPolicyCBS_Type(Integer32):
    """Custom type onuPortUpPolicyCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OnuPortUpPolicyCBS_Type.__name__ = "Integer32"
_OnuPortUpPolicyCBS_Object = MibTableColumn
onuPortUpPolicyCBS = _OnuPortUpPolicyCBS_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 5),
    _OnuPortUpPolicyCBS_Type()
)
onuPortUpPolicyCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortUpPolicyCBS.setStatus("current")


class _OnuPortUpPolicyEBS_Type(Integer32):
    """Custom type onuPortUpPolicyEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OnuPortUpPolicyEBS_Type.__name__ = "Integer32"
_OnuPortUpPolicyEBS_Object = MibTableColumn
onuPortUpPolicyEBS = _OnuPortUpPolicyEBS_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 6),
    _OnuPortUpPolicyEBS_Type()
)
onuPortUpPolicyEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortUpPolicyEBS.setStatus("current")


class _OnuPortDownPolicySwitch_Type(Integer32):
    """Custom type onuPortDownPolicySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuPortDownPolicySwitch_Type.__name__ = "Integer32"
_OnuPortDownPolicySwitch_Object = MibTableColumn
onuPortDownPolicySwitch = _OnuPortDownPolicySwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 7),
    _OnuPortDownPolicySwitch_Type()
)
onuPortDownPolicySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortDownPolicySwitch.setStatus("current")


class _OnuPortDownPolicyCIR_Type(Integer32):
    """Custom type onuPortDownPolicyCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OnuPortDownPolicyCIR_Type.__name__ = "Integer32"
_OnuPortDownPolicyCIR_Object = MibTableColumn
onuPortDownPolicyCIR = _OnuPortDownPolicyCIR_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 8),
    _OnuPortDownPolicyCIR_Type()
)
onuPortDownPolicyCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortDownPolicyCIR.setStatus("current")


class _OnuPortDownPolicyPIR_Type(Integer32):
    """Custom type onuPortDownPolicyPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OnuPortDownPolicyPIR_Type.__name__ = "Integer32"
_OnuPortDownPolicyPIR_Object = MibTableColumn
onuPortDownPolicyPIR = _OnuPortDownPolicyPIR_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 9),
    _OnuPortDownPolicyPIR_Type()
)
onuPortDownPolicyPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortDownPolicyPIR.setStatus("current")


class _OnuPortVlanMode_Type(Integer32):
    """Custom type onuPortVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("translation", 2),
          ("transparent", 0))
    )


_OnuPortVlanMode_Type.__name__ = "Integer32"
_OnuPortVlanMode_Object = MibTableColumn
onuPortVlanMode = _OnuPortVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 10),
    _OnuPortVlanMode_Type()
)
onuPortVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortVlanMode.setStatus("current")


class _OnuPortVlanTagValue_Type(Integer32):
    """Custom type onuPortVlanTagValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuPortVlanTagValue_Type.__name__ = "Integer32"
_OnuPortVlanTagValue_Object = MibTableColumn
onuPortVlanTagValue = _OnuPortVlanTagValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 11),
    _OnuPortVlanTagValue_Type()
)
onuPortVlanTagValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortVlanTagValue.setStatus("current")


class _OnuDefaultVlan_Type(Integer32):
    """Custom type onuDefaultVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuDefaultVlan_Type.__name__ = "Integer32"
_OnuDefaultVlan_Object = MibTableColumn
onuDefaultVlan = _OnuDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 12),
    _OnuDefaultVlan_Type()
)
onuDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuDefaultVlan.setStatus("current")


class _OnuVlanDelVid1_Type(Integer32):
    """Custom type onuVlanDelVid1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanDelVid1_Type.__name__ = "Integer32"
_OnuVlanDelVid1_Object = MibTableColumn
onuVlanDelVid1 = _OnuVlanDelVid1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 13),
    _OnuVlanDelVid1_Type()
)
onuVlanDelVid1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanDelVid1.setStatus("current")


class _OnuVlanAddVid1_Type(Integer32):
    """Custom type onuVlanAddVid1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanAddVid1_Type.__name__ = "Integer32"
_OnuVlanAddVid1_Object = MibTableColumn
onuVlanAddVid1 = _OnuVlanAddVid1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 14),
    _OnuVlanAddVid1_Type()
)
onuVlanAddVid1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanAddVid1.setStatus("current")


class _OnuVlanDelVid2_Type(Integer32):
    """Custom type onuVlanDelVid2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanDelVid2_Type.__name__ = "Integer32"
_OnuVlanDelVid2_Object = MibTableColumn
onuVlanDelVid2 = _OnuVlanDelVid2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 15),
    _OnuVlanDelVid2_Type()
)
onuVlanDelVid2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanDelVid2.setStatus("current")


class _OnuVlanAddVid2_Type(Integer32):
    """Custom type onuVlanAddVid2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanAddVid2_Type.__name__ = "Integer32"
_OnuVlanAddVid2_Object = MibTableColumn
onuVlanAddVid2 = _OnuVlanAddVid2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 16),
    _OnuVlanAddVid2_Type()
)
onuVlanAddVid2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanAddVid2.setStatus("current")


class _OnuVlanDelVid3_Type(Integer32):
    """Custom type onuVlanDelVid3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanDelVid3_Type.__name__ = "Integer32"
_OnuVlanDelVid3_Object = MibTableColumn
onuVlanDelVid3 = _OnuVlanDelVid3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 17),
    _OnuVlanDelVid3_Type()
)
onuVlanDelVid3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanDelVid3.setStatus("current")


class _OnuVlanAddVid3_Type(Integer32):
    """Custom type onuVlanAddVid3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanAddVid3_Type.__name__ = "Integer32"
_OnuVlanAddVid3_Object = MibTableColumn
onuVlanAddVid3 = _OnuVlanAddVid3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 18),
    _OnuVlanAddVid3_Type()
)
onuVlanAddVid3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanAddVid3.setStatus("current")


class _OnuVlanDelVid4_Type(Integer32):
    """Custom type onuVlanDelVid4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanDelVid4_Type.__name__ = "Integer32"
_OnuVlanDelVid4_Object = MibTableColumn
onuVlanDelVid4 = _OnuVlanDelVid4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 19),
    _OnuVlanDelVid4_Type()
)
onuVlanDelVid4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanDelVid4.setStatus("current")


class _OnuVlanAddVid4_Type(Integer32):
    """Custom type onuVlanAddVid4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanAddVid4_Type.__name__ = "Integer32"
_OnuVlanAddVid4_Object = MibTableColumn
onuVlanAddVid4 = _OnuVlanAddVid4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 20),
    _OnuVlanAddVid4_Type()
)
onuVlanAddVid4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanAddVid4.setStatus("current")


class _OnuVlanDelVid5_Type(Integer32):
    """Custom type onuVlanDelVid5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanDelVid5_Type.__name__ = "Integer32"
_OnuVlanDelVid5_Object = MibTableColumn
onuVlanDelVid5 = _OnuVlanDelVid5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 21),
    _OnuVlanDelVid5_Type()
)
onuVlanDelVid5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanDelVid5.setStatus("current")


class _OnuVlanAddVid5_Type(Integer32):
    """Custom type onuVlanAddVid5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanAddVid5_Type.__name__ = "Integer32"
_OnuVlanAddVid5_Object = MibTableColumn
onuVlanAddVid5 = _OnuVlanAddVid5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 22),
    _OnuVlanAddVid5_Type()
)
onuVlanAddVid5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanAddVid5.setStatus("current")


class _OnuVlanDelVid6_Type(Integer32):
    """Custom type onuVlanDelVid6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanDelVid6_Type.__name__ = "Integer32"
_OnuVlanDelVid6_Object = MibTableColumn
onuVlanDelVid6 = _OnuVlanDelVid6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 23),
    _OnuVlanDelVid6_Type()
)
onuVlanDelVid6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanDelVid6.setStatus("current")


class _OnuVlanAddVid6_Type(Integer32):
    """Custom type onuVlanAddVid6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanAddVid6_Type.__name__ = "Integer32"
_OnuVlanAddVid6_Object = MibTableColumn
onuVlanAddVid6 = _OnuVlanAddVid6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 24),
    _OnuVlanAddVid6_Type()
)
onuVlanAddVid6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanAddVid6.setStatus("current")


class _OnuVlanDelVid7_Type(Integer32):
    """Custom type onuVlanDelVid7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanDelVid7_Type.__name__ = "Integer32"
_OnuVlanDelVid7_Object = MibTableColumn
onuVlanDelVid7 = _OnuVlanDelVid7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 25),
    _OnuVlanDelVid7_Type()
)
onuVlanDelVid7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanDelVid7.setStatus("current")


class _OnuVlanAddVid7_Type(Integer32):
    """Custom type onuVlanAddVid7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanAddVid7_Type.__name__ = "Integer32"
_OnuVlanAddVid7_Object = MibTableColumn
onuVlanAddVid7 = _OnuVlanAddVid7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 26),
    _OnuVlanAddVid7_Type()
)
onuVlanAddVid7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanAddVid7.setStatus("current")


class _OnuVlanDelVid8_Type(Integer32):
    """Custom type onuVlanDelVid8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanDelVid8_Type.__name__ = "Integer32"
_OnuVlanDelVid8_Object = MibTableColumn
onuVlanDelVid8 = _OnuVlanDelVid8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 27),
    _OnuVlanDelVid8_Type()
)
onuVlanDelVid8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanDelVid8.setStatus("current")


class _OnuVlanAddVid8_Type(Integer32):
    """Custom type onuVlanAddVid8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuVlanAddVid8_Type.__name__ = "Integer32"
_OnuVlanAddVid8_Object = MibTableColumn
onuVlanAddVid8 = _OnuVlanAddVid8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 28),
    _OnuVlanAddVid8_Type()
)
onuVlanAddVid8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVlanAddVid8.setStatus("current")


class _OnuRulePrecedenceSwitch_Type(Integer32):
    """Custom type onuRulePrecedenceSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("null", -1))
    )


_OnuRulePrecedenceSwitch_Type.__name__ = "Integer32"
_OnuRulePrecedenceSwitch_Object = MibTableColumn
onuRulePrecedenceSwitch = _OnuRulePrecedenceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 29),
    _OnuRulePrecedenceSwitch_Type()
)
onuRulePrecedenceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuRulePrecedenceSwitch.setStatus("current")
_OnuRulePrecedenceNum_Type = Integer32
_OnuRulePrecedenceNum_Object = MibTableColumn
onuRulePrecedenceNum = _OnuRulePrecedenceNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 30),
    _OnuRulePrecedenceNum_Type()
)
onuRulePrecedenceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuRulePrecedenceNum.setStatus("current")
_OnuRuleProfile_Type = DisplayString
_OnuRuleProfile_Object = MibTableColumn
onuRuleProfile = _OnuRuleProfile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 31),
    _OnuRuleProfile_Type()
)
onuRuleProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuRuleProfile.setStatus("current")
_OnuConditionList_Type = DisplayString
_OnuConditionList_Object = MibTableColumn
onuConditionList = _OnuConditionList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 32),
    _OnuConditionList_Type()
)
onuConditionList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuConditionList.setStatus("current")


class _OnuMultiVlanSwitch_Type(Integer32):
    """Custom type onuMultiVlanSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("clear", 2),
          ("delete", 1),
          ("null", -1))
    )


_OnuMultiVlanSwitch_Type.__name__ = "Integer32"
_OnuMultiVlanSwitch_Object = MibTableColumn
onuMultiVlanSwitch = _OnuMultiVlanSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 33),
    _OnuMultiVlanSwitch_Type()
)
onuMultiVlanSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMultiVlanSwitch.setStatus("current")
_OnuMultiVlanList_Type = DisplayString
_OnuMultiVlanList_Object = MibTableColumn
onuMultiVlanList = _OnuMultiVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 34),
    _OnuMultiVlanList_Type()
)
onuMultiVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMultiVlanList.setStatus("current")


class _OnuMultiVlanTagStripe_Type(Integer32):
    """Custom type onuMultiVlanTagStripe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuMultiVlanTagStripe_Type.__name__ = "Integer32"
_OnuMultiVlanTagStripe_Object = MibTableColumn
onuMultiVlanTagStripe = _OnuMultiVlanTagStripe_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 35),
    _OnuMultiVlanTagStripe_Type()
)
onuMultiVlanTagStripe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMultiVlanTagStripe.setStatus("current")


class _OnuMultiGroupMaxNum_Type(Integer32):
    """Custom type onuMultiGroupMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OnuMultiGroupMaxNum_Type.__name__ = "Integer32"
_OnuMultiGroupMaxNum_Object = MibTableColumn
onuMultiGroupMaxNum = _OnuMultiGroupMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 36),
    _OnuMultiGroupMaxNum_Type()
)
onuMultiGroupMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMultiGroupMaxNum.setStatus("current")
_OnuPortRowStatus_Type = RowStatus
_OnuPortRowStatus_Object = MibTableColumn
onuPortRowStatus = _OnuPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 5, 1, 37),
    _OnuPortRowStatus_Type()
)
onuPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortRowStatus.setStatus("current")
_Zxr10EponRemoteFastRebootTable_Object = MibTable
zxr10EponRemoteFastRebootTable = _Zxr10EponRemoteFastRebootTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 6)
)
if mibBuilder.loadTexts:
    zxr10EponRemoteFastRebootTable.setStatus("current")
_Zxr10EponRemoteFastRebootEntry_Object = MibTableRow
zxr10EponRemoteFastRebootEntry = _Zxr10EponRemoteFastRebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 6, 1)
)
zxr10EponRemoteFastRebootEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-EPON-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    zxr10EponRemoteFastRebootEntry.setStatus("current")


class _RemoteMultiFastLeave_Type(Integer32):
    """Custom type remoteMultiFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RemoteMultiFastLeave_Type.__name__ = "Integer32"
_RemoteMultiFastLeave_Object = MibTableColumn
remoteMultiFastLeave = _RemoteMultiFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 6, 1, 1),
    _RemoteMultiFastLeave_Type()
)
remoteMultiFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteMultiFastLeave.setStatus("current")


class _RemoteReboot_Type(Integer32):
    """Custom type remoteReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RemoteReboot_Type.__name__ = "Integer32"
_RemoteReboot_Object = MibTableColumn
remoteReboot = _RemoteReboot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 6, 1, 2),
    _RemoteReboot_Type()
)
remoteReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteReboot.setStatus("current")
_Zxr10EponRemoteOnuVoipTable_Object = MibTable
zxr10EponRemoteOnuVoipTable = _Zxr10EponRemoteOnuVoipTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 7)
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuVoipTable.setStatus("current")
_Zxr10EponRemoteOnuVoipEntry_Object = MibTableRow
zxr10EponRemoteOnuVoipEntry = _Zxr10EponRemoteOnuVoipEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 7, 1)
)
zxr10EponRemoteOnuVoipEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-EPON-MIB", "onuId"),
    (0, "ZXR10-EPON-MIB", "onuVoipUniNumber"),
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuVoipEntry.setStatus("current")


class _OnuVoipUniNumber_Type(Integer32):
    """Custom type onuVoipUniNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OnuVoipUniNumber_Type.__name__ = "Integer32"
_OnuVoipUniNumber_Object = MibTableColumn
onuVoipUniNumber = _OnuVoipUniNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 7, 1, 1),
    _OnuVoipUniNumber_Type()
)
onuVoipUniNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuVoipUniNumber.setStatus("current")


class _OnuVoipEnableSwitch_Type(Integer32):
    """Custom type onuVoipEnableSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuVoipEnableSwitch_Type.__name__ = "Integer32"
_OnuVoipEnableSwitch_Object = MibTableColumn
onuVoipEnableSwitch = _OnuVoipEnableSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 7, 1, 2),
    _OnuVoipEnableSwitch_Type()
)
onuVoipEnableSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVoipEnableSwitch.setStatus("current")
_Zxr10EponRemoteOnuE1Table_Object = MibTable
zxr10EponRemoteOnuE1Table = _Zxr10EponRemoteOnuE1Table_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 8)
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuE1Table.setStatus("current")
_Zxr10EponRemoteOnuE1Entry_Object = MibTableRow
zxr10EponRemoteOnuE1Entry = _Zxr10EponRemoteOnuE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 8, 1)
)
zxr10EponRemoteOnuE1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-EPON-MIB", "onuId"),
    (0, "ZXR10-EPON-MIB", "onuE1UniNumber"),
)
if mibBuilder.loadTexts:
    zxr10EponRemoteOnuE1Entry.setStatus("current")


class _OnuE1UniNumber_Type(Integer32):
    """Custom type onuE1UniNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OnuE1UniNumber_Type.__name__ = "Integer32"
_OnuE1UniNumber_Object = MibTableColumn
onuE1UniNumber = _OnuE1UniNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 8, 1, 1),
    _OnuE1UniNumber_Type()
)
onuE1UniNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuE1UniNumber.setStatus("current")


class _OnuE1EnableSwitch_Type(Integer32):
    """Custom type onuE1EnableSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuE1EnableSwitch_Type.__name__ = "Integer32"
_OnuE1EnableSwitch_Object = MibTableColumn
onuE1EnableSwitch = _OnuE1EnableSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 2, 8, 1, 2),
    _OnuE1EnableSwitch_Type()
)
onuE1EnableSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuE1EnableSwitch.setStatus("current")
_Zxr10EponTopologyCollect_ObjectIdentity = ObjectIdentity
zxr10EponTopologyCollect = _Zxr10EponTopologyCollect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 309, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-EPON-MIB",
    **{"zte": zte,
       "zxr10": zxr10,
       "zxr10EponObjects": zxr10EponObjects,
       "zxr10EponLocal": zxr10EponLocal,
       "zxr10EponOnuAuthTable": zxr10EponOnuAuthTable,
       "zxr10EponOnuAuthEntry": zxr10EponOnuAuthEntry,
       "eponSlotId": eponSlotId,
       "onuSoftwareAuth": onuSoftwareAuth,
       "onuHardwareSwitch": onuHardwareSwitch,
       "onuAutoAuthSwtich": onuAutoAuthSwtich,
       "zxr10EponOltOptiInfoTable": zxr10EponOltOptiInfoTable,
       "zxr10EponOltOptiInfoEntry": zxr10EponOltOptiInfoEntry,
       "eponOltPortName": eponOltPortName,
       "optiInfoSFPID": optiInfoSFPID,
       "optiInfoVendor": optiInfoVendor,
       "optiInfoWavelength": optiInfoWavelength,
       "optiInfoVendorPN": optiInfoVendorPN,
       "oltPortSupportedLlidNum": oltPortSupportedLlidNum,
       "oltPortSoftwareVersion": oltPortSoftwareVersion,
       "oltPortAGCLockTime": oltPortAGCLockTime,
       "oltPortCDRLockTime": oltPortCDRLockTime,
       "zxr10EponOltEncryptTable": zxr10EponOltEncryptTable,
       "zxr10EponOltEncryptEntry": zxr10EponOltEncryptEntry,
       "oltEncryptAlgorithm": oltEncryptAlgorithm,
       "oltKeyUpdatePeriod": oltKeyUpdatePeriod,
       "oltChurningTimer": oltChurningTimer,
       "oltMaxRtt": oltMaxRtt,
       "oltLaserSwitch": oltLaserSwitch,
       "opticsMeasureLow": opticsMeasureLow,
       "opticsMeasureHigh": opticsMeasureHigh,
       "packetLimitType": packetLimitType,
       "packetLimitSwitch": packetLimitSwitch,
       "protocolProtectMode": protocolProtectMode,
       "protocolProtectSwitch": protocolProtectSwitch,
       "optiDiagInterval": optiDiagInterval,
       "oltEncryptRowStatus": oltEncryptRowStatus,
       "oltPortDBAType": oltPortDBAType,
       "zxr10EponOnuAuthInfoTable": zxr10EponOnuAuthInfoTable,
       "zxr10EponOnuAuthInfoEntry": zxr10EponOnuAuthInfoEntry,
       "onuId": onuId,
       "onuAuthState": onuAuthState,
       "onuType": onuType,
       "onuAuthPCBVer": onuAuthPCBVer,
       "onuAuthSoftVer": onuAuthSoftVer,
       "onuEEPROMVer": onuEEPROMVer,
       "onuHostType": onuHostType,
       "onuOpticalLen": onuOpticalLen,
       "onuHardVer": onuHardVer,
       "onuRTT": onuRTT,
       "onuMacPortName": onuMacPortName,
       "onuBindTypeName": onuBindTypeName,
       "onuBindMacAddr": onuBindMacAddr,
       "onuBindSN": onuBindSN,
       "onuMacMaxNum": onuMacMaxNum,
       "onuBindRowStatus": onuBindRowStatus,
       "zxr10EponOltPortStatTable": zxr10EponOltPortStatTable,
       "zxr10EponOltPortStatEntry": zxr10EponOltPortStatEntry,
       "oltStatisBer": oltStatisBer,
       "oltStatisFer": oltStatisFer,
       "oltStatisPortBer": oltStatisPortBer,
       "oltStatisInPkts": oltStatisInPkts,
       "oltStatisInOctes": oltStatisInOctes,
       "oltStatisInUniPkts": oltStatisInUniPkts,
       "oltStatisInMultiPkts": oltStatisInMultiPkts,
       "oltStatisInBroadPkts": oltStatisInBroadPkts,
       "oltStatisOutPkts": oltStatisOutPkts,
       "oltStatisOutOctes": oltStatisOutOctes,
       "oltStatisOutUniPkts": oltStatisOutUniPkts,
       "oltStatisOutMultiPkts": oltStatisOutMultiPkts,
       "oltStatisOutBroadPkts": oltStatisOutBroadPkts,
       "oamFramesCounters": oamFramesCounters,
       "standardOamStatistics": standardOamStatistics,
       "standardOamMpcpStatistic": standardOamMpcpStatistic,
       "cpuPortsOctets": cpuPortsOctets,
       "cpuPortsFrames": cpuPortsFrames,
       "transmittedFramesPerLLID": transmittedFramesPerLLID,
       "droppedFramesPerLLID": droppedFramesPerLLID,
       "transmittedOctetsPerLLID": transmittedOctetsPerLLID,
       "inRangeLengthErrorsPerLLID": inRangeLengthErrorsPerLLID,
       "frameTooLongErrorsPerLLID": frameTooLongErrorsPerLLID,
       "zxr10EponOnuPortStatTable": zxr10EponOnuPortStatTable,
       "zxr10EponOnuPortStatEntry": zxr10EponOnuPortStatEntry,
       "onuStatisBer": onuStatisBer,
       "onuStatisFer": onuStatisFer,
       "onuStatisInPkts": onuStatisInPkts,
       "onuStatisInOctes": onuStatisInOctes,
       "onuStatisInMultiPkts": onuStatisInMultiPkts,
       "onuStatisInBroadPkts": onuStatisInBroadPkts,
       "onuStatisOutPkts": onuStatisOutPkts,
       "onuStatisOutOctes": onuStatisOutOctes,
       "onuStatisOutMultiPkts": onuStatisOutMultiPkts,
       "onuStatisOutBroadPkts": onuStatisOutBroadPkts,
       "zxr10EponProtectGroupTable": zxr10EponProtectGroupTable,
       "zxr10EponProtectGroupEntry": zxr10EponProtectGroupEntry,
       "protectGroupid": protectGroupid,
       "protectOltMasterIfName": protectOltMasterIfName,
       "protectOltBackupIfName": protectOltBackupIfName,
       "protectOltActiveIfName": protectOltActiveIfName,
       "protectOltEnableSwitch": protectOltEnableSwitch,
       "protectReverEnable": protectReverEnable,
       "protectReverTime": protectReverTime,
       "protectRowStatus": protectRowStatus,
       "zxr10EponSwitchRecordTable": zxr10EponSwitchRecordTable,
       "zxr10EponSwitchRecordEntry": zxr10EponSwitchRecordEntry,
       "switchRecordGroupid": switchRecordGroupid,
       "switchRecordNum": switchRecordNum,
       "switchTime": switchTime,
       "switchType": switchType,
       "switchTypeMtoB": switchTypeMtoB,
       "zxr10EponAlarmTable": zxr10EponAlarmTable,
       "zxr10EponAlarmEntry": zxr10EponAlarmEntry,
       "oltAlarmSwitch": oltAlarmSwitch,
       "oltAlarmDirectSwitch": oltAlarmDirectSwitch,
       "oltAlarmThreshold": oltAlarmThreshold,
       "zxr10EponRemoteOnu": zxr10EponRemoteOnu,
       "zxr10EponRemoteOnuInfoTable": zxr10EponRemoteOnuInfoTable,
       "zxr10EponRemoteOnuInfoEntry": zxr10EponRemoteOnuInfoEntry,
       "remoteOnuVendorId": remoteOnuVendorId,
       "remoteOnuModel": remoteOnuModel,
       "remoteOnuId": remoteOnuId,
       "remoteHardwareVersion": remoteHardwareVersion,
       "remoteSoftwareVersion": remoteSoftwareVersion,
       "remoteFirmwareVersion": remoteFirmwareVersion,
       "remoteChipVendorId": remoteChipVendorId,
       "remoteChipModel": remoteChipModel,
       "remoteChipRevison": remoteChipRevison,
       "remoteIcVersion": remoteIcVersion,
       "remoteGePortNum": remoteGePortNum,
       "remoteBitmapGePort": remoteBitmapGePort,
       "remoteFePortNum": remoteFePortNum,
       "remoteBitmapFePort": remoteBitmapFePort,
       "remotePortsNum": remotePortsNum,
       "remoteE1PortNum": remoteE1PortNum,
       "remoteUsQueuesNum": remoteUsQueuesNum,
       "remoteMaxQueuesPerUSport": remoteMaxQueuesPerUSport,
       "remoteDSQueuesNum": remoteDSQueuesNum,
       "remoteMaxQueuesPerDSport": remoteMaxQueuesPerDSport,
       "remoteBatteryBackup": remoteBatteryBackup,
       "zxr10EponRemoteOnuDbaTable": zxr10EponRemoteOnuDbaTable,
       "zxr10EponRemoteOnuDbaEntry": zxr10EponRemoteOnuDbaEntry,
       "queueSetId": queueSetId,
       "queueValue1": queueValue1,
       "queueValue2": queueValue2,
       "queueValue3": queueValue3,
       "queueValue4": queueValue4,
       "queueValue5": queueValue5,
       "queueValue6": queueValue6,
       "queueValue7": queueValue7,
       "queueValue8": queueValue8,
       "dbaQueueActive": dbaQueueActive,
       "onuDbaRowStatus": onuDbaRowStatus,
       "zxr10EponRemoteOnuClassRuleTable": zxr10EponRemoteOnuClassRuleTable,
       "zxr10EponRemoteOnuClassRuleEntry": zxr10EponRemoteOnuClassRuleEntry,
       "ruleProfileNum": ruleProfileNum,
       "queueVlaue": queueVlaue,
       "priorityValue": priorityValue,
       "ruleRowStatus": ruleRowStatus,
       "zxr10EponRemoteOnuClassCondiTable": zxr10EponRemoteOnuClassCondiTable,
       "zxr10EponRemoteOnuClassCondiEntry": zxr10EponRemoteOnuClassCondiEntry,
       "conditionProfileNum": conditionProfileNum,
       "conditionMacAddressType": conditionMacAddressType,
       "conditionMacAddress": conditionMacAddress,
       "conditionIpAddressType": conditionIpAddressType,
       "conditionIpAddress": conditionIpAddress,
       "conditionPriority": conditionPriority,
       "conditionVlanId": conditionVlanId,
       "conditionDscp": conditionDscp,
       "conditionL4PortType": conditionL4PortType,
       "conditionPortNum": conditionPortNum,
       "conditionEthType": conditionEthType,
       "conditionIpProtocolType": conditionIpProtocolType,
       "conditionOperatorType": conditionOperatorType,
       "conditionRowStatus": conditionRowStatus,
       "zxr10EponRemoteOnuPortTable": zxr10EponRemoteOnuPortTable,
       "zxr10EponRemoteOnuPortEntry": zxr10EponRemoteOnuPortEntry,
       "onuEthUniNumber": onuEthUniNumber,
       "onuPortFlowControl": onuPortFlowControl,
       "onuPortUpPolicySwitch": onuPortUpPolicySwitch,
       "onuPortUpPolicyCIR": onuPortUpPolicyCIR,
       "onuPortUpPolicyCBS": onuPortUpPolicyCBS,
       "onuPortUpPolicyEBS": onuPortUpPolicyEBS,
       "onuPortDownPolicySwitch": onuPortDownPolicySwitch,
       "onuPortDownPolicyCIR": onuPortDownPolicyCIR,
       "onuPortDownPolicyPIR": onuPortDownPolicyPIR,
       "onuPortVlanMode": onuPortVlanMode,
       "onuPortVlanTagValue": onuPortVlanTagValue,
       "onuDefaultVlan": onuDefaultVlan,
       "onuVlanDelVid1": onuVlanDelVid1,
       "onuVlanAddVid1": onuVlanAddVid1,
       "onuVlanDelVid2": onuVlanDelVid2,
       "onuVlanAddVid2": onuVlanAddVid2,
       "onuVlanDelVid3": onuVlanDelVid3,
       "onuVlanAddVid3": onuVlanAddVid3,
       "onuVlanDelVid4": onuVlanDelVid4,
       "onuVlanAddVid4": onuVlanAddVid4,
       "onuVlanDelVid5": onuVlanDelVid5,
       "onuVlanAddVid5": onuVlanAddVid5,
       "onuVlanDelVid6": onuVlanDelVid6,
       "onuVlanAddVid6": onuVlanAddVid6,
       "onuVlanDelVid7": onuVlanDelVid7,
       "onuVlanAddVid7": onuVlanAddVid7,
       "onuVlanDelVid8": onuVlanDelVid8,
       "onuVlanAddVid8": onuVlanAddVid8,
       "onuRulePrecedenceSwitch": onuRulePrecedenceSwitch,
       "onuRulePrecedenceNum": onuRulePrecedenceNum,
       "onuRuleProfile": onuRuleProfile,
       "onuConditionList": onuConditionList,
       "onuMultiVlanSwitch": onuMultiVlanSwitch,
       "onuMultiVlanList": onuMultiVlanList,
       "onuMultiVlanTagStripe": onuMultiVlanTagStripe,
       "onuMultiGroupMaxNum": onuMultiGroupMaxNum,
       "onuPortRowStatus": onuPortRowStatus,
       "zxr10EponRemoteFastRebootTable": zxr10EponRemoteFastRebootTable,
       "zxr10EponRemoteFastRebootEntry": zxr10EponRemoteFastRebootEntry,
       "remoteMultiFastLeave": remoteMultiFastLeave,
       "remoteReboot": remoteReboot,
       "zxr10EponRemoteOnuVoipTable": zxr10EponRemoteOnuVoipTable,
       "zxr10EponRemoteOnuVoipEntry": zxr10EponRemoteOnuVoipEntry,
       "onuVoipUniNumber": onuVoipUniNumber,
       "onuVoipEnableSwitch": onuVoipEnableSwitch,
       "zxr10EponRemoteOnuE1Table": zxr10EponRemoteOnuE1Table,
       "zxr10EponRemoteOnuE1Entry": zxr10EponRemoteOnuE1Entry,
       "onuE1UniNumber": onuE1UniNumber,
       "onuE1EnableSwitch": onuE1EnableSwitch,
       "zxr10EponTopologyCollect": zxr10EponTopologyCollect}
)
