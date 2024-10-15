# SNMP MIB module (MADGECAU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MADGECAU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:57 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Madge_ObjectIdentity = ObjectIdentity
madge = _Madge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494)
)
_MadgeCau_ObjectIdentity = ObjectIdentity
madgeCau = _MadgeCau_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2)
)
_MadgeCauTop_ObjectIdentity = ObjectIdentity
madgeCauTop = _MadgeCauTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 1)
)


class _MadgeCauTopWrap_Type(Integer32):
    """Custom type madgeCauTopWrap based on Integer32"""
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
        *(("normal", 1),
          ("wrap-both", 4),
          ("wrap-ri", 2),
          ("wrap-ro", 3))
    )


_MadgeCauTopWrap_Type.__name__ = "Integer32"
_MadgeCauTopWrap_Object = MibScalar
madgeCauTopWrap = _MadgeCauTopWrap_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 1, 1),
    _MadgeCauTopWrap_Type()
)
madgeCauTopWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauTopWrap.setStatus("mandatory")


class _MadgeCauTopWrapCtrl_Type(Integer32):
    """Custom type madgeCauTopWrapCtrl based on Integer32"""
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
        *(("normal", 1),
          ("wrap-both", 4),
          ("wrap-ri", 2),
          ("wrap-ro", 3))
    )


_MadgeCauTopWrapCtrl_Type.__name__ = "Integer32"
_MadgeCauTopWrapCtrl_Object = MibScalar
madgeCauTopWrapCtrl = _MadgeCauTopWrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 1, 2),
    _MadgeCauTopWrapCtrl_Type()
)
madgeCauTopWrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauTopWrapCtrl.setStatus("mandatory")


class _MadgeCauTopRIType_Type(Integer32):
    """Custom type madgeCauTopRIType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fibre", 1),
          ("utp", 3))
    )


_MadgeCauTopRIType_Type.__name__ = "Integer32"
_MadgeCauTopRIType_Object = MibScalar
madgeCauTopRIType = _MadgeCauTopRIType_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 1, 3),
    _MadgeCauTopRIType_Type()
)
madgeCauTopRIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauTopRIType.setStatus("mandatory")


class _MadgeCauTopRIState_Type(Integer32):
    """Custom type madgeCauTopRIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSignal", 1),
          ("yesSignal", 2))
    )


_MadgeCauTopRIState_Type.__name__ = "Integer32"
_MadgeCauTopRIState_Object = MibScalar
madgeCauTopRIState = _MadgeCauTopRIState_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 1, 4),
    _MadgeCauTopRIState_Type()
)
madgeCauTopRIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauTopRIState.setStatus("mandatory")


class _MadgeCauTopROType_Type(Integer32):
    """Custom type madgeCauTopROType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fibre", 1),
          ("utp", 3))
    )


_MadgeCauTopROType_Type.__name__ = "Integer32"
_MadgeCauTopROType_Object = MibScalar
madgeCauTopROType = _MadgeCauTopROType_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 1, 5),
    _MadgeCauTopROType_Type()
)
madgeCauTopROType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauTopROType.setStatus("mandatory")


class _MadgeCauTopROState_Type(Integer32):
    """Custom type madgeCauTopROState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSignal", 1),
          ("yesSignal", 2))
    )


_MadgeCauTopROState_Type.__name__ = "Integer32"
_MadgeCauTopROState_Object = MibScalar
madgeCauTopROState = _MadgeCauTopROState_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 1, 6),
    _MadgeCauTopROState_Type()
)
madgeCauTopROState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauTopROState.setStatus("mandatory")


class _MadgeCauTopBackupRing_Type(Integer32):
    """Custom type madgeCauTopBackupRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("badly-cabled", 3),
          ("beaconing", 1),
          ("normal", 2))
    )


_MadgeCauTopBackupRing_Type.__name__ = "Integer32"
_MadgeCauTopBackupRing_Object = MibScalar
madgeCauTopBackupRing = _MadgeCauTopBackupRing_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 1, 7),
    _MadgeCauTopBackupRing_Type()
)
madgeCauTopBackupRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauTopBackupRing.setStatus("mandatory")


class _MadgeCauTopBackupUsed_Type(Integer32):
    """Custom type madgeCauTopBackupUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unUsed", 1),
          ("used", 2))
    )


_MadgeCauTopBackupUsed_Type.__name__ = "Integer32"
_MadgeCauTopBackupUsed_Object = MibScalar
madgeCauTopBackupUsed = _MadgeCauTopBackupUsed_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 1, 8),
    _MadgeCauTopBackupUsed_Type()
)
madgeCauTopBackupUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauTopBackupUsed.setStatus("mandatory")
_MadgeCauInfo_ObjectIdentity = ObjectIdentity
madgeCauInfo = _MadgeCauInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 2)
)


class _MadgeCauInfoVersion_Type(OctetString):
    """Custom type madgeCauInfoVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_MadgeCauInfoVersion_Type.__name__ = "OctetString"
_MadgeCauInfoVersion_Object = MibScalar
madgeCauInfoVersion = _MadgeCauInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 2, 1),
    _MadgeCauInfoVersion_Type()
)
madgeCauInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauInfoVersion.setStatus("mandatory")


class _MadgeCauInfoRemoval_Type(Integer32):
    """Custom type madgeCauInfoRemoval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MadgeCauInfoRemoval_Type.__name__ = "Integer32"
_MadgeCauInfoRemoval_Object = MibScalar
madgeCauInfoRemoval = _MadgeCauInfoRemoval_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 2, 2),
    _MadgeCauInfoRemoval_Type()
)
madgeCauInfoRemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauInfoRemoval.setStatus("mandatory")


class _MadgeCauInfoSRNet_Type(Integer32):
    """Custom type madgeCauInfoSRNet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MadgeCauInfoSRNet_Type.__name__ = "Integer32"
_MadgeCauInfoSRNet_Object = MibScalar
madgeCauInfoSRNet = _MadgeCauInfoSRNet_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 2, 3),
    _MadgeCauInfoSRNet_Type()
)
madgeCauInfoSRNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauInfoSRNet.setStatus("mandatory")
_MadgeCauInfoIPXNet_Type = Integer32
_MadgeCauInfoIPXNet_Object = MibScalar
madgeCauInfoIPXNet = _MadgeCauInfoIPXNet_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 2, 4),
    _MadgeCauInfoIPXNet_Type()
)
madgeCauInfoIPXNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauInfoIPXNet.setStatus("mandatory")
_MadgeCauInfoFanSpeed_Type = Integer32
_MadgeCauInfoFanSpeed_Object = MibScalar
madgeCauInfoFanSpeed = _MadgeCauInfoFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 2, 5),
    _MadgeCauInfoFanSpeed_Type()
)
madgeCauInfoFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauInfoFanSpeed.setStatus("mandatory")
_MadgeCauInfoTherm_Type = Integer32
_MadgeCauInfoTherm_Object = MibScalar
madgeCauInfoTherm = _MadgeCauInfoTherm_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 2, 6),
    _MadgeCauInfoTherm_Type()
)
madgeCauInfoTherm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauInfoTherm.setStatus("mandatory")


class _MadgeCauInfoType_Type(Integer32):
    """Custom type madgeCauInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("smartCau", 2),
          ("smartCauPlus", 3),
          ("smartRam", 5),
          ("smartRamPlus", 7))
    )


_MadgeCauInfoType_Type.__name__ = "Integer32"
_MadgeCauInfoType_Object = MibScalar
madgeCauInfoType = _MadgeCauInfoType_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 2, 7),
    _MadgeCauInfoType_Type()
)
madgeCauInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauInfoType.setStatus("mandatory")
_MadgeCauLam_ObjectIdentity = ObjectIdentity
madgeCauLam = _MadgeCauLam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 3)
)
_MadgeCauLamTable_Object = MibTable
madgeCauLamTable = _MadgeCauLamTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 3, 1)
)
if mibBuilder.loadTexts:
    madgeCauLamTable.setStatus("mandatory")
_MadgeCauLamEntry_Object = MibTableRow
madgeCauLamEntry = _MadgeCauLamEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1)
)
madgeCauLamEntry.setIndexNames(
    (0, "MADGECAU-MIB", "madgeCauLamNo"),
)
if mibBuilder.loadTexts:
    madgeCauLamEntry.setStatus("mandatory")
_MadgeCauLamNo_Type = Integer32
_MadgeCauLamNo_Object = MibTableColumn
madgeCauLamNo = _MadgeCauLamNo_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 1),
    _MadgeCauLamNo_Type()
)
madgeCauLamNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauLamNo.setStatus("mandatory")


class _MadgeCauLamType_Type(Integer32):
    """Custom type madgeCauLamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("badlyCabled", 6),
          ("ibmLam", 2),
          ("mau", 8),
          ("noLam", 1),
          ("node", 5),
          ("raylanLam", 10),
          ("stpLam", 4),
          ("userMau", 9),
          ("utpLam", 3),
          ("utpLam2", 11))
    )


_MadgeCauLamType_Type.__name__ = "Integer32"
_MadgeCauLamType_Object = MibTableColumn
madgeCauLamType = _MadgeCauLamType_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 2),
    _MadgeCauLamType_Type()
)
madgeCauLamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauLamType.setStatus("mandatory")


class _MadgeCauLamState_Type(Integer32):
    """Custom type madgeCauLamState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fault", 8),
          ("inserted", 5),
          ("noLam", 1),
          ("nodeInserting", 4),
          ("wrongSpeed", 7))
    )


_MadgeCauLamState_Type.__name__ = "Integer32"
_MadgeCauLamState_Object = MibTableColumn
madgeCauLamState = _MadgeCauLamState_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 3),
    _MadgeCauLamState_Type()
)
madgeCauLamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauLamState.setStatus("mandatory")


class _MadgeCauLamAdminState_Type(Integer32):
    """Custom type madgeCauLamAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lamDisabled", 2),
          ("lamEnabled", 1))
    )


_MadgeCauLamAdminState_Type.__name__ = "Integer32"
_MadgeCauLamAdminState_Object = MibTableColumn
madgeCauLamAdminState = _MadgeCauLamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 4),
    _MadgeCauLamAdminState_Type()
)
madgeCauLamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauLamAdminState.setStatus("mandatory")


class _MadgeCauLamAllPorts_Type(OctetString):
    """Custom type madgeCauLamAllPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MadgeCauLamAllPorts_Type.__name__ = "OctetString"
_MadgeCauLamAllPorts_Object = MibTableColumn
madgeCauLamAllPorts = _MadgeCauLamAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 5),
    _MadgeCauLamAllPorts_Type()
)
madgeCauLamAllPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauLamAllPorts.setStatus("mandatory")


class _MadgeCauLamSpeedDetect_Type(Integer32):
    """Custom type madgeCauLamSpeedDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdDisabled", 1),
          ("sdEnabled", 2))
    )


_MadgeCauLamSpeedDetect_Type.__name__ = "Integer32"
_MadgeCauLamSpeedDetect_Object = MibTableColumn
madgeCauLamSpeedDetect = _MadgeCauLamSpeedDetect_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 6),
    _MadgeCauLamSpeedDetect_Type()
)
madgeCauLamSpeedDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauLamSpeedDetect.setStatus("mandatory")
_MadgeCauLCD_ObjectIdentity = ObjectIdentity
madgeCauLCD = _MadgeCauLCD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 5)
)
_MadgeCauLCDMax_Type = Integer32
_MadgeCauLCDMax_Object = MibScalar
madgeCauLCDMax = _MadgeCauLCDMax_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 5, 1),
    _MadgeCauLCDMax_Type()
)
madgeCauLCDMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauLCDMax.setStatus("mandatory")
_MadgeCauLCDCurrent_Type = Integer32
_MadgeCauLCDCurrent_Object = MibScalar
madgeCauLCDCurrent = _MadgeCauLCDCurrent_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 5, 2),
    _MadgeCauLCDCurrent_Type()
)
madgeCauLCDCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauLCDCurrent.setStatus("mandatory")
_MadgeCauLCDTable_Object = MibTable
madgeCauLCDTable = _MadgeCauLCDTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 5, 3)
)
if mibBuilder.loadTexts:
    madgeCauLCDTable.setStatus("mandatory")
_MadgeCauLCDEntry_Object = MibTableRow
madgeCauLCDEntry = _MadgeCauLCDEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 5, 3, 1)
)
madgeCauLCDEntry.setIndexNames(
    (0, "MADGECAU-MIB", "madgeCauLCDNo"),
)
if mibBuilder.loadTexts:
    madgeCauLCDEntry.setStatus("mandatory")
_MadgeCauLCDNo_Type = Integer32
_MadgeCauLCDNo_Object = MibTableColumn
madgeCauLCDNo = _MadgeCauLCDNo_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 5, 3, 1, 1),
    _MadgeCauLCDNo_Type()
)
madgeCauLCDNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauLCDNo.setStatus("mandatory")


class _MadgeCauLCDInfo_Type(OctetString):
    """Custom type madgeCauLCDInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_MadgeCauLCDInfo_Type.__name__ = "OctetString"
_MadgeCauLCDInfo_Object = MibTableColumn
madgeCauLCDInfo = _MadgeCauLCDInfo_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 5, 3, 1, 2),
    _MadgeCauLCDInfo_Type()
)
madgeCauLCDInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauLCDInfo.setStatus("mandatory")
_MadgeCauAddr_ObjectIdentity = ObjectIdentity
madgeCauAddr = _MadgeCauAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 6)
)
_MadgeCauAddrTable_Object = MibTable
madgeCauAddrTable = _MadgeCauAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 6, 1)
)
if mibBuilder.loadTexts:
    madgeCauAddrTable.setStatus("mandatory")
_MadgeCauAddrEntry_Object = MibTableRow
madgeCauAddrEntry = _MadgeCauAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 6, 1, 1)
)
madgeCauAddrEntry.setIndexNames(
    (0, "MADGECAU-MIB", "madgeCauAddrLamNo"),
    (0, "MADGECAU-MIB", "madgeCauAddrPortNo"),
)
if mibBuilder.loadTexts:
    madgeCauAddrEntry.setStatus("mandatory")


class _MadgeCauAddrLamNo_Type(Integer32):
    """Custom type madgeCauAddrLamNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MadgeCauAddrLamNo_Type.__name__ = "Integer32"
_MadgeCauAddrLamNo_Object = MibTableColumn
madgeCauAddrLamNo = _MadgeCauAddrLamNo_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 6, 1, 1, 1),
    _MadgeCauAddrLamNo_Type()
)
madgeCauAddrLamNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauAddrLamNo.setStatus("mandatory")


class _MadgeCauAddrPortNo_Type(Integer32):
    """Custom type madgeCauAddrPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21),
    )


_MadgeCauAddrPortNo_Type.__name__ = "Integer32"
_MadgeCauAddrPortNo_Object = MibTableColumn
madgeCauAddrPortNo = _MadgeCauAddrPortNo_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 6, 1, 1, 2),
    _MadgeCauAddrPortNo_Type()
)
madgeCauAddrPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauAddrPortNo.setStatus("mandatory")
_MadgeCauAddrInfo_Type = OctetString
_MadgeCauAddrInfo_Object = MibTableColumn
madgeCauAddrInfo = _MadgeCauAddrInfo_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 6, 1, 1, 3),
    _MadgeCauAddrInfo_Type()
)
madgeCauAddrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauAddrInfo.setStatus("mandatory")


class _MadgeCauAddrAllowedNode_Type(OctetString):
    """Custom type madgeCauAddrAllowedNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MadgeCauAddrAllowedNode_Type.__name__ = "OctetString"
_MadgeCauAddrAllowedNode_Object = MibTableColumn
madgeCauAddrAllowedNode = _MadgeCauAddrAllowedNode_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 6, 1, 1, 4),
    _MadgeCauAddrAllowedNode_Type()
)
madgeCauAddrAllowedNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauAddrAllowedNode.setStatus("mandatory")
_MadgeCauConfig_ObjectIdentity = ObjectIdentity
madgeCauConfig = _MadgeCauConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 7)
)


class _MadgeCauConfigLAA_Type(OctetString):
    """Custom type madgeCauConfigLAA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MadgeCauConfigLAA_Type.__name__ = "OctetString"
_MadgeCauConfigLAA_Object = MibScalar
madgeCauConfigLAA = _MadgeCauConfigLAA_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 7, 1),
    _MadgeCauConfigLAA_Type()
)
madgeCauConfigLAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauConfigLAA.setStatus("mandatory")


class _MadgeCauConfigNodePort_Type(Integer32):
    """Custom type madgeCauConfigNodePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doActiveNodeMatching", 2),
          ("noActiveNodeMatching", 1))
    )


_MadgeCauConfigNodePort_Type.__name__ = "Integer32"
_MadgeCauConfigNodePort_Object = MibScalar
madgeCauConfigNodePort = _MadgeCauConfigNodePort_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 7, 2),
    _MadgeCauConfigNodePort_Type()
)
madgeCauConfigNodePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauConfigNodePort.setStatus("mandatory")


class _MadgeCauConfig24HourClock_Type(Integer32):
    """Custom type madgeCauConfig24HourClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clock12Hour", 1),
          ("clock24Hour", 2),
          ("clockNotSupported", 3))
    )


_MadgeCauConfig24HourClock_Type.__name__ = "Integer32"
_MadgeCauConfig24HourClock_Object = MibScalar
madgeCauConfig24HourClock = _MadgeCauConfig24HourClock_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 7, 3),
    _MadgeCauConfig24HourClock_Type()
)
madgeCauConfig24HourClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauConfig24HourClock.setStatus("mandatory")
_MadgeCauConfigClock_Type = Integer32
_MadgeCauConfigClock_Object = MibScalar
madgeCauConfigClock = _MadgeCauConfigClock_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 7, 4),
    _MadgeCauConfigClock_Type()
)
madgeCauConfigClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauConfigClock.setStatus("mandatory")


class _MadgeCauConfigPromiscousRmon_Type(Integer32):
    """Custom type madgeCauConfigPromiscousRmon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("promiscuousRmonOff", 2),
          ("promiscuousRmonOn", 3))
    )


_MadgeCauConfigPromiscousRmon_Type.__name__ = "Integer32"
_MadgeCauConfigPromiscousRmon_Object = MibScalar
madgeCauConfigPromiscousRmon = _MadgeCauConfigPromiscousRmon_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 7, 5),
    _MadgeCauConfigPromiscousRmon_Type()
)
madgeCauConfigPromiscousRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauConfigPromiscousRmon.setStatus("mandatory")
_MadgeCauNewConfig_ObjectIdentity = ObjectIdentity
madgeCauNewConfig = _MadgeCauNewConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 8)
)


class _MadgeCauNewConfigMauStore_Type(Integer32):
    """Custom type madgeCauNewConfigMauStore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mauDeduce", 1),
          ("mauRecall", 2))
    )


_MadgeCauNewConfigMauStore_Type.__name__ = "Integer32"
_MadgeCauNewConfigMauStore_Object = MibScalar
madgeCauNewConfigMauStore = _MadgeCauNewConfigMauStore_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 8, 1),
    _MadgeCauNewConfigMauStore_Type()
)
madgeCauNewConfigMauStore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauNewConfigMauStore.setStatus("mandatory")


class _MadgeCauNewConfigNonPromiscuousRmon_Type(Integer32):
    """Custom type madgeCauNewConfigNonPromiscuousRmon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonPromiscuousRmonOff", 1),
          ("nonPromiscuousRmonOn", 2))
    )


_MadgeCauNewConfigNonPromiscuousRmon_Type.__name__ = "Integer32"
_MadgeCauNewConfigNonPromiscuousRmon_Object = MibScalar
madgeCauNewConfigNonPromiscuousRmon = _MadgeCauNewConfigNonPromiscuousRmon_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 8, 2),
    _MadgeCauNewConfigNonPromiscuousRmon_Type()
)
madgeCauNewConfigNonPromiscuousRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauNewConfigNonPromiscuousRmon.setStatus("mandatory")


class _MadgeCauNewConfigSAPControl_Type(Integer32):
    """Custom type madgeCauNewConfigSAPControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sapsDisabled", 1),
          ("sapsEnabled", 2))
    )


_MadgeCauNewConfigSAPControl_Type.__name__ = "Integer32"
_MadgeCauNewConfigSAPControl_Object = MibScalar
madgeCauNewConfigSAPControl = _MadgeCauNewConfigSAPControl_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 8, 3),
    _MadgeCauNewConfigSAPControl_Type()
)
madgeCauNewConfigSAPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauNewConfigSAPControl.setStatus("mandatory")
_MadgeCauSecurity_ObjectIdentity = ObjectIdentity
madgeCauSecurity = _MadgeCauSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 9)
)


class _MadgeCauSecurityPMAnnounce_Type(Integer32):
    """Custom type madgeCauSecurityPMAnnounce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pmAnnounceOff", 1),
          ("pmAnnounceOn", 2))
    )


_MadgeCauSecurityPMAnnounce_Type.__name__ = "Integer32"
_MadgeCauSecurityPMAnnounce_Object = MibScalar
madgeCauSecurityPMAnnounce = _MadgeCauSecurityPMAnnounce_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 1),
    _MadgeCauSecurityPMAnnounce_Type()
)
madgeCauSecurityPMAnnounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityPMAnnounce.setStatus("mandatory")


class _MadgeCauSecurityPMSafePollTimer_Type(Integer32):
    """Custom type madgeCauSecurityPMSafePollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MadgeCauSecurityPMSafePollTimer_Type.__name__ = "Integer32"
_MadgeCauSecurityPMSafePollTimer_Object = MibScalar
madgeCauSecurityPMSafePollTimer = _MadgeCauSecurityPMSafePollTimer_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 2),
    _MadgeCauSecurityPMSafePollTimer_Type()
)
madgeCauSecurityPMSafePollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityPMSafePollTimer.setStatus("mandatory")


class _MadgeCauSecurityPMSafeReplyTimeout_Type(Integer32):
    """Custom type madgeCauSecurityPMSafeReplyTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MadgeCauSecurityPMSafeReplyTimeout_Type.__name__ = "Integer32"
_MadgeCauSecurityPMSafeReplyTimeout_Object = MibScalar
madgeCauSecurityPMSafeReplyTimeout = _MadgeCauSecurityPMSafeReplyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 3),
    _MadgeCauSecurityPMSafeReplyTimeout_Type()
)
madgeCauSecurityPMSafeReplyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityPMSafeReplyTimeout.setStatus("mandatory")


class _MadgeCauSecurityPMSafeRetries_Type(Integer32):
    """Custom type madgeCauSecurityPMSafeRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MadgeCauSecurityPMSafeRetries_Type.__name__ = "Integer32"
_MadgeCauSecurityPMSafeRetries_Object = MibScalar
madgeCauSecurityPMSafeRetries = _MadgeCauSecurityPMSafeRetries_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 4),
    _MadgeCauSecurityPMSafeRetries_Type()
)
madgeCauSecurityPMSafeRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityPMSafeRetries.setStatus("mandatory")


class _MadgeCauSecurityAllowedManufacturers_Type(Integer32):
    """Custom type madgeCauSecurityAllowedManufacturers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allManufacturers", 1),
          ("madgeIBMOnly", 2),
          ("madgeOnly", 3))
    )


_MadgeCauSecurityAllowedManufacturers_Type.__name__ = "Integer32"
_MadgeCauSecurityAllowedManufacturers_Object = MibScalar
madgeCauSecurityAllowedManufacturers = _MadgeCauSecurityAllowedManufacturers_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 5),
    _MadgeCauSecurityAllowedManufacturers_Type()
)
madgeCauSecurityAllowedManufacturers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityAllowedManufacturers.setStatus("mandatory")


class _MadgeCauSecurityActionPM_Type(Integer32):
    """Custom type madgeCauSecurityActionPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_MadgeCauSecurityActionPM_Type.__name__ = "Integer32"
_MadgeCauSecurityActionPM_Object = MibScalar
madgeCauSecurityActionPM = _MadgeCauSecurityActionPM_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 6),
    _MadgeCauSecurityActionPM_Type()
)
madgeCauSecurityActionPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityActionPM.setStatus("mandatory")


class _MadgeCauSecurityActionPMUnsafe_Type(Integer32):
    """Custom type madgeCauSecurityActionPMUnsafe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_MadgeCauSecurityActionPMUnsafe_Type.__name__ = "Integer32"
_MadgeCauSecurityActionPMUnsafe_Object = MibScalar
madgeCauSecurityActionPMUnsafe = _MadgeCauSecurityActionPMUnsafe_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 7),
    _MadgeCauSecurityActionPMUnsafe_Type()
)
madgeCauSecurityActionPMUnsafe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityActionPMUnsafe.setStatus("mandatory")


class _MadgeCauSecurityActionRogueNode_Type(Integer32):
    """Custom type madgeCauSecurityActionRogueNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_MadgeCauSecurityActionRogueNode_Type.__name__ = "Integer32"
_MadgeCauSecurityActionRogueNode_Object = MibScalar
madgeCauSecurityActionRogueNode = _MadgeCauSecurityActionRogueNode_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 8),
    _MadgeCauSecurityActionRogueNode_Type()
)
madgeCauSecurityActionRogueNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityActionRogueNode.setStatus("mandatory")


class _MadgeCauSecurityActionIllegalMF_Type(Integer32):
    """Custom type madgeCauSecurityActionIllegalMF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_MadgeCauSecurityActionIllegalMF_Type.__name__ = "Integer32"
_MadgeCauSecurityActionIllegalMF_Object = MibScalar
madgeCauSecurityActionIllegalMF = _MadgeCauSecurityActionIllegalMF_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 9),
    _MadgeCauSecurityActionIllegalMF_Type()
)
madgeCauSecurityActionIllegalMF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityActionIllegalMF.setStatus("mandatory")
_MadgeCauSecurityTable_Object = MibTable
madgeCauSecurityTable = _MadgeCauSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 10)
)
if mibBuilder.loadTexts:
    madgeCauSecurityTable.setStatus("mandatory")
_MadgeCauSecurityEntry_Object = MibTableRow
madgeCauSecurityEntry = _MadgeCauSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1)
)
madgeCauSecurityEntry.setIndexNames(
    (0, "MADGECAU-MIB", "madgeCauSecurityIndex"),
)
if mibBuilder.loadTexts:
    madgeCauSecurityEntry.setStatus("mandatory")
_MadgeCauSecurityIndex_Type = Integer32
_MadgeCauSecurityIndex_Object = MibTableColumn
madgeCauSecurityIndex = _MadgeCauSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 1),
    _MadgeCauSecurityIndex_Type()
)
madgeCauSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauSecurityIndex.setStatus("mandatory")


class _MadgeCauSecurityNodeAddress_Type(OctetString):
    """Custom type madgeCauSecurityNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MadgeCauSecurityNodeAddress_Type.__name__ = "OctetString"
_MadgeCauSecurityNodeAddress_Object = MibTableColumn
madgeCauSecurityNodeAddress = _MadgeCauSecurityNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 2),
    _MadgeCauSecurityNodeAddress_Type()
)
madgeCauSecurityNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityNodeAddress.setStatus("mandatory")


class _MadgeCauSecurityExceptionPM_Type(Integer32):
    """Custom type madgeCauSecurityExceptionPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("disallow", 1))
    )


_MadgeCauSecurityExceptionPM_Type.__name__ = "Integer32"
_MadgeCauSecurityExceptionPM_Object = MibTableColumn
madgeCauSecurityExceptionPM = _MadgeCauSecurityExceptionPM_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 3),
    _MadgeCauSecurityExceptionPM_Type()
)
madgeCauSecurityExceptionPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityExceptionPM.setStatus("mandatory")


class _MadgeCauSecurityExceptionPMUnsafe_Type(Integer32):
    """Custom type madgeCauSecurityExceptionPMUnsafe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("disallow", 1))
    )


_MadgeCauSecurityExceptionPMUnsafe_Type.__name__ = "Integer32"
_MadgeCauSecurityExceptionPMUnsafe_Object = MibTableColumn
madgeCauSecurityExceptionPMUnsafe = _MadgeCauSecurityExceptionPMUnsafe_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 4),
    _MadgeCauSecurityExceptionPMUnsafe_Type()
)
madgeCauSecurityExceptionPMUnsafe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityExceptionPMUnsafe.setStatus("mandatory")


class _MadgeCauSecurityExceptionRogueNode_Type(Integer32):
    """Custom type madgeCauSecurityExceptionRogueNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("disallow", 1))
    )


_MadgeCauSecurityExceptionRogueNode_Type.__name__ = "Integer32"
_MadgeCauSecurityExceptionRogueNode_Object = MibTableColumn
madgeCauSecurityExceptionRogueNode = _MadgeCauSecurityExceptionRogueNode_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 5),
    _MadgeCauSecurityExceptionRogueNode_Type()
)
madgeCauSecurityExceptionRogueNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityExceptionRogueNode.setStatus("mandatory")


class _MadgeCauSecurityExceptionIllegalMF_Type(Integer32):
    """Custom type madgeCauSecurityExceptionIllegalMF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("disallow", 1))
    )


_MadgeCauSecurityExceptionIllegalMF_Type.__name__ = "Integer32"
_MadgeCauSecurityExceptionIllegalMF_Object = MibTableColumn
madgeCauSecurityExceptionIllegalMF = _MadgeCauSecurityExceptionIllegalMF_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 6),
    _MadgeCauSecurityExceptionIllegalMF_Type()
)
madgeCauSecurityExceptionIllegalMF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityExceptionIllegalMF.setStatus("mandatory")


class _MadgeCauSecurityExceptionWrongNode_Type(Integer32):
    """Custom type madgeCauSecurityExceptionWrongNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("disallow", 1))
    )


_MadgeCauSecurityExceptionWrongNode_Type.__name__ = "Integer32"
_MadgeCauSecurityExceptionWrongNode_Object = MibTableColumn
madgeCauSecurityExceptionWrongNode = _MadgeCauSecurityExceptionWrongNode_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 7),
    _MadgeCauSecurityExceptionWrongNode_Type()
)
madgeCauSecurityExceptionWrongNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityExceptionWrongNode.setStatus("mandatory")


class _MadgeCauSecurityActionWrongNode_Type(Integer32):
    """Custom type madgeCauSecurityActionWrongNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_MadgeCauSecurityActionWrongNode_Type.__name__ = "Integer32"
_MadgeCauSecurityActionWrongNode_Object = MibScalar
madgeCauSecurityActionWrongNode = _MadgeCauSecurityActionWrongNode_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 11),
    _MadgeCauSecurityActionWrongNode_Type()
)
madgeCauSecurityActionWrongNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityActionWrongNode.setStatus("mandatory")


class _MadgeCauSecurityExtendedException_Type(Integer32):
    """Custom type madgeCauSecurityExtendedException based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inNewMode", 3),
          ("inOldMode", 2),
          ("oldModeOnly", 1))
    )


_MadgeCauSecurityExtendedException_Type.__name__ = "Integer32"
_MadgeCauSecurityExtendedException_Object = MibScalar
madgeCauSecurityExtendedException = _MadgeCauSecurityExtendedException_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 9, 12),
    _MadgeCauSecurityExtendedException_Type()
)
madgeCauSecurityExtendedException.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauSecurityExtendedException.setStatus("mandatory")
_MadgeCauFault_ObjectIdentity = ObjectIdentity
madgeCauFault = _MadgeCauFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 10)
)


class _MadgeCauFaultRPFailAction_Type(Integer32):
    """Custom type madgeCauFaultRPFailAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_MadgeCauFaultRPFailAction_Type.__name__ = "Integer32"
_MadgeCauFaultRPFailAction_Object = MibScalar
madgeCauFaultRPFailAction = _MadgeCauFaultRPFailAction_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 10, 1),
    _MadgeCauFaultRPFailAction_Type()
)
madgeCauFaultRPFailAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauFaultRPFailAction.setStatus("mandatory")


class _MadgeCauFaultBeaconDefault_Type(Integer32):
    """Custom type madgeCauFaultBeaconDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MadgeCauFaultBeaconDefault_Type.__name__ = "Integer32"
_MadgeCauFaultBeaconDefault_Object = MibScalar
madgeCauFaultBeaconDefault = _MadgeCauFaultBeaconDefault_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 10, 2),
    _MadgeCauFaultBeaconDefault_Type()
)
madgeCauFaultBeaconDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauFaultBeaconDefault.setStatus("mandatory")


class _MadgeCauFaultBeaconThreshold_Type(Integer32):
    """Custom type madgeCauFaultBeaconThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MadgeCauFaultBeaconThreshold_Type.__name__ = "Integer32"
_MadgeCauFaultBeaconThreshold_Object = MibScalar
madgeCauFaultBeaconThreshold = _MadgeCauFaultBeaconThreshold_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 10, 3),
    _MadgeCauFaultBeaconThreshold_Type()
)
madgeCauFaultBeaconThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauFaultBeaconThreshold.setStatus("mandatory")


class _MadgeCauFaultBeaconAction_Type(Integer32):
    """Custom type madgeCauFaultBeaconAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_MadgeCauFaultBeaconAction_Type.__name__ = "Integer32"
_MadgeCauFaultBeaconAction_Object = MibScalar
madgeCauFaultBeaconAction = _MadgeCauFaultBeaconAction_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 10, 4),
    _MadgeCauFaultBeaconAction_Type()
)
madgeCauFaultBeaconAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauFaultBeaconAction.setStatus("mandatory")


class _MadgeCauFaultRingPurgeDefault_Type(Integer32):
    """Custom type madgeCauFaultRingPurgeDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MadgeCauFaultRingPurgeDefault_Type.__name__ = "Integer32"
_MadgeCauFaultRingPurgeDefault_Object = MibScalar
madgeCauFaultRingPurgeDefault = _MadgeCauFaultRingPurgeDefault_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 10, 5),
    _MadgeCauFaultRingPurgeDefault_Type()
)
madgeCauFaultRingPurgeDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauFaultRingPurgeDefault.setStatus("mandatory")


class _MadgeCauFaultRingPurgeThreshold_Type(Integer32):
    """Custom type madgeCauFaultRingPurgeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MadgeCauFaultRingPurgeThreshold_Type.__name__ = "Integer32"
_MadgeCauFaultRingPurgeThreshold_Object = MibScalar
madgeCauFaultRingPurgeThreshold = _MadgeCauFaultRingPurgeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 10, 6),
    _MadgeCauFaultRingPurgeThreshold_Type()
)
madgeCauFaultRingPurgeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauFaultRingPurgeThreshold.setStatus("mandatory")


class _MadgeCauFaultRingPurgeAction_Type(Integer32):
    """Custom type madgeCauFaultRingPurgeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_MadgeCauFaultRingPurgeAction_Type.__name__ = "Integer32"
_MadgeCauFaultRingPurgeAction_Object = MibScalar
madgeCauFaultRingPurgeAction = _MadgeCauFaultRingPurgeAction_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 10, 7),
    _MadgeCauFaultRingPurgeAction_Type()
)
madgeCauFaultRingPurgeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauFaultRingPurgeAction.setStatus("mandatory")


class _MadgeCauFaultIsoErrDefault_Type(Integer32):
    """Custom type madgeCauFaultIsoErrDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MadgeCauFaultIsoErrDefault_Type.__name__ = "Integer32"
_MadgeCauFaultIsoErrDefault_Object = MibScalar
madgeCauFaultIsoErrDefault = _MadgeCauFaultIsoErrDefault_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 10, 8),
    _MadgeCauFaultIsoErrDefault_Type()
)
madgeCauFaultIsoErrDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauFaultIsoErrDefault.setStatus("mandatory")


class _MadgeCauFaultIsoErrThreshold_Type(Integer32):
    """Custom type madgeCauFaultIsoErrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MadgeCauFaultIsoErrThreshold_Type.__name__ = "Integer32"
_MadgeCauFaultIsoErrThreshold_Object = MibScalar
madgeCauFaultIsoErrThreshold = _MadgeCauFaultIsoErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 10, 9),
    _MadgeCauFaultIsoErrThreshold_Type()
)
madgeCauFaultIsoErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauFaultIsoErrThreshold.setStatus("mandatory")


class _MadgeCauFaultIsoErrAction_Type(Integer32):
    """Custom type madgeCauFaultIsoErrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_MadgeCauFaultIsoErrAction_Type.__name__ = "Integer32"
_MadgeCauFaultIsoErrAction_Object = MibScalar
madgeCauFaultIsoErrAction = _MadgeCauFaultIsoErrAction_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 10, 10),
    _MadgeCauFaultIsoErrAction_Type()
)
madgeCauFaultIsoErrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeCauFaultIsoErrAction.setStatus("mandatory")
_MadgeCauKill_ObjectIdentity = ObjectIdentity
madgeCauKill = _MadgeCauKill_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 11)
)


class _MadgeCauKillNodeAddress_Type(OctetString):
    """Custom type madgeCauKillNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MadgeCauKillNodeAddress_Type.__name__ = "OctetString"
_MadgeCauKillNodeAddress_Object = MibScalar
madgeCauKillNodeAddress = _MadgeCauKillNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 11, 1),
    _MadgeCauKillNodeAddress_Type()
)
madgeCauKillNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauKillNodeAddress.setStatus("mandatory")


class _MadgeCauKillReason_Type(Integer32):
    """Custom type madgeCauKillReason based on Integer32"""
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
        *(("beaconing", 7),
          ("illegalManufacturer", 5),
          ("isolatingErrors", 9),
          ("pmUnsafe", 3),
          ("pmViolation", 2),
          ("reasonUnknown", 1),
          ("ringPollFailure", 6),
          ("ringPurges", 8),
          ("rogueNode", 4),
          ("wrongNode", 10))
    )


_MadgeCauKillReason_Type.__name__ = "Integer32"
_MadgeCauKillReason_Object = MibScalar
madgeCauKillReason = _MadgeCauKillReason_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 11, 2),
    _MadgeCauKillReason_Type()
)
madgeCauKillReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauKillReason.setStatus("mandatory")


class _MadgeCauKillStatus_Type(Integer32):
    """Custom type madgeCauKillStatus based on Integer32"""
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
        *(("aboutToKill", 2),
          ("information", 1),
          ("killAbandoned", 5),
          ("killFailed", 3),
          ("killed", 4),
          ("resurrected", 6))
    )


_MadgeCauKillStatus_Type.__name__ = "Integer32"
_MadgeCauKillStatus_Object = MibScalar
madgeCauKillStatus = _MadgeCauKillStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 11, 3),
    _MadgeCauKillStatus_Type()
)
madgeCauKillStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauKillStatus.setStatus("mandatory")


class _MadgeCauKillLamNo_Type(Integer32):
    """Custom type madgeCauKillLamNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MadgeCauKillLamNo_Type.__name__ = "Integer32"
_MadgeCauKillLamNo_Object = MibScalar
madgeCauKillLamNo = _MadgeCauKillLamNo_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 11, 4),
    _MadgeCauKillLamNo_Type()
)
madgeCauKillLamNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauKillLamNo.setStatus("mandatory")


class _MadgeCauKillPortNo_Type(Integer32):
    """Custom type madgeCauKillPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MadgeCauKillPortNo_Type.__name__ = "Integer32"
_MadgeCauKillPortNo_Object = MibScalar
madgeCauKillPortNo = _MadgeCauKillPortNo_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 11, 5),
    _MadgeCauKillPortNo_Type()
)
madgeCauKillPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauKillPortNo.setStatus("mandatory")
_MadgeCauTrapInfo_ObjectIdentity = ObjectIdentity
madgeCauTrapInfo = _MadgeCauTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 2, 12)
)


class _MadgeCauTrapInfoLamNo_Type(Integer32):
    """Custom type madgeCauTrapInfoLamNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MadgeCauTrapInfoLamNo_Type.__name__ = "Integer32"
_MadgeCauTrapInfoLamNo_Object = MibScalar
madgeCauTrapInfoLamNo = _MadgeCauTrapInfoLamNo_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 12, 1),
    _MadgeCauTrapInfoLamNo_Type()
)
madgeCauTrapInfoLamNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauTrapInfoLamNo.setStatus("mandatory")


class _MadgeCauTrapInfoPortNo_Type(Integer32):
    """Custom type madgeCauTrapInfoPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21),
    )


_MadgeCauTrapInfoPortNo_Type.__name__ = "Integer32"
_MadgeCauTrapInfoPortNo_Object = MibScalar
madgeCauTrapInfoPortNo = _MadgeCauTrapInfoPortNo_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 12, 2),
    _MadgeCauTrapInfoPortNo_Type()
)
madgeCauTrapInfoPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauTrapInfoPortNo.setStatus("mandatory")


class _MadgeCauTrapInfoState_Type(Integer32):
    """Custom type madgeCauTrapInfoState based on Integer32"""
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
        *(("fault", 4),
          ("inserted", 2),
          ("noNode", 1),
          ("wrongSpeed", 3))
    )


_MadgeCauTrapInfoState_Type.__name__ = "Integer32"
_MadgeCauTrapInfoState_Object = MibScalar
madgeCauTrapInfoState = _MadgeCauTrapInfoState_Object(
    (1, 3, 6, 1, 4, 1, 494, 2, 12, 3),
    _MadgeCauTrapInfoState_Type()
)
madgeCauTrapInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeCauTrapInfoState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

backupPathStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 2, 0, 1)
)
backupPathStateChange.setObjects(
    ("MADGECAU-MIB", "madgeCauTopBackupRing")
)
if mibBuilder.loadTexts:
    backupPathStateChange.setStatus(
        ""
    )

backupPathStateUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 2, 0, 2)
)
backupPathStateUse.setObjects(
    ("MADGECAU-MIB", "madgeCauTopBackupUsed")
)
if mibBuilder.loadTexts:
    backupPathStateUse.setStatus(
        ""
    )

wrapStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 2, 0, 3)
)
wrapStateChange.setObjects(
    ("MADGECAU-MIB", "madgeCauTopWrap")
)
if mibBuilder.loadTexts:
    wrapStateChange.setStatus(
        ""
    )

lamPortDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 2, 0, 4)
)
if mibBuilder.loadTexts:
    lamPortDisabled.setStatus(
        ""
    )

mCaufanSpeedFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 2, 0, 5)
)
mCaufanSpeedFailed.setObjects(
    ("MADGECAU-MIB", "madgeCauInfoFanSpeed")
)
if mibBuilder.loadTexts:
    mCaufanSpeedFailed.setStatus(
        ""
    )

temperatureExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 2, 0, 6)
)
temperatureExceeded.setObjects(
    ("MADGECAU-MIB", "madgeCauInfoTherm")
)
if mibBuilder.loadTexts:
    temperatureExceeded.setStatus(
        ""
    )

killInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 2, 0, 7)
)
killInformation.setObjects(
      *(("MADGECAU-MIB", "madgeCauKillNodeAddress"),
        ("MADGECAU-MIB", "madgeCauKillReason"),
        ("MADGECAU-MIB", "madgeCauKillStatus"))
)
if mibBuilder.loadTexts:
    killInformation.setStatus(
        ""
    )

killInformation2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 2, 0, 8)
)
killInformation2.setObjects(
      *(("MADGECAU-MIB", "madgeCauKillNodeAddress"),
        ("MADGECAU-MIB", "madgeCauKillReason"),
        ("MADGECAU-MIB", "madgeCauKillStatus"),
        ("MADGECAU-MIB", "madgeCauKillLamNo"),
        ("MADGECAU-MIB", "madgeCauKillPortNo"))
)
if mibBuilder.loadTexts:
    killInformation2.setStatus(
        ""
    )

lamPortDisabled2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 2, 0, 9)
)
lamPortDisabled2.setObjects(
      *(("MADGECAU-MIB", "madgeCauTrapInfoLamNo"),
        ("MADGECAU-MIB", "madgeCauTrapInfoPortNo"),
        ("MADGECAU-MIB", "madgeCauTrapInfoState"))
)
if mibBuilder.loadTexts:
    lamPortDisabled2.setStatus(
        ""
    )

lamStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 2, 0, 10)
)
lamStateChanged.setObjects(
      *(("MADGECAU-MIB", "madgeCauTrapInfoLamNo"),
        ("MADGECAU-MIB", "madgeCauTrapInfoState"))
)
if mibBuilder.loadTexts:
    lamStateChanged.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MADGECAU-MIB",
    **{"madge": madge,
       "madgeCau": madgeCau,
       "backupPathStateChange": backupPathStateChange,
       "backupPathStateUse": backupPathStateUse,
       "wrapStateChange": wrapStateChange,
       "lamPortDisabled": lamPortDisabled,
       "mCaufanSpeedFailed": mCaufanSpeedFailed,
       "temperatureExceeded": temperatureExceeded,
       "killInformation": killInformation,
       "killInformation2": killInformation2,
       "lamPortDisabled2": lamPortDisabled2,
       "lamStateChanged": lamStateChanged,
       "madgeCauTop": madgeCauTop,
       "madgeCauTopWrap": madgeCauTopWrap,
       "madgeCauTopWrapCtrl": madgeCauTopWrapCtrl,
       "madgeCauTopRIType": madgeCauTopRIType,
       "madgeCauTopRIState": madgeCauTopRIState,
       "madgeCauTopROType": madgeCauTopROType,
       "madgeCauTopROState": madgeCauTopROState,
       "madgeCauTopBackupRing": madgeCauTopBackupRing,
       "madgeCauTopBackupUsed": madgeCauTopBackupUsed,
       "madgeCauInfo": madgeCauInfo,
       "madgeCauInfoVersion": madgeCauInfoVersion,
       "madgeCauInfoRemoval": madgeCauInfoRemoval,
       "madgeCauInfoSRNet": madgeCauInfoSRNet,
       "madgeCauInfoIPXNet": madgeCauInfoIPXNet,
       "madgeCauInfoFanSpeed": madgeCauInfoFanSpeed,
       "madgeCauInfoTherm": madgeCauInfoTherm,
       "madgeCauInfoType": madgeCauInfoType,
       "madgeCauLam": madgeCauLam,
       "madgeCauLamTable": madgeCauLamTable,
       "madgeCauLamEntry": madgeCauLamEntry,
       "madgeCauLamNo": madgeCauLamNo,
       "madgeCauLamType": madgeCauLamType,
       "madgeCauLamState": madgeCauLamState,
       "madgeCauLamAdminState": madgeCauLamAdminState,
       "madgeCauLamAllPorts": madgeCauLamAllPorts,
       "madgeCauLamSpeedDetect": madgeCauLamSpeedDetect,
       "madgeCauLCD": madgeCauLCD,
       "madgeCauLCDMax": madgeCauLCDMax,
       "madgeCauLCDCurrent": madgeCauLCDCurrent,
       "madgeCauLCDTable": madgeCauLCDTable,
       "madgeCauLCDEntry": madgeCauLCDEntry,
       "madgeCauLCDNo": madgeCauLCDNo,
       "madgeCauLCDInfo": madgeCauLCDInfo,
       "madgeCauAddr": madgeCauAddr,
       "madgeCauAddrTable": madgeCauAddrTable,
       "madgeCauAddrEntry": madgeCauAddrEntry,
       "madgeCauAddrLamNo": madgeCauAddrLamNo,
       "madgeCauAddrPortNo": madgeCauAddrPortNo,
       "madgeCauAddrInfo": madgeCauAddrInfo,
       "madgeCauAddrAllowedNode": madgeCauAddrAllowedNode,
       "madgeCauConfig": madgeCauConfig,
       "madgeCauConfigLAA": madgeCauConfigLAA,
       "madgeCauConfigNodePort": madgeCauConfigNodePort,
       "madgeCauConfig24HourClock": madgeCauConfig24HourClock,
       "madgeCauConfigClock": madgeCauConfigClock,
       "madgeCauConfigPromiscousRmon": madgeCauConfigPromiscousRmon,
       "madgeCauNewConfig": madgeCauNewConfig,
       "madgeCauNewConfigMauStore": madgeCauNewConfigMauStore,
       "madgeCauNewConfigNonPromiscuousRmon": madgeCauNewConfigNonPromiscuousRmon,
       "madgeCauNewConfigSAPControl": madgeCauNewConfigSAPControl,
       "madgeCauSecurity": madgeCauSecurity,
       "madgeCauSecurityPMAnnounce": madgeCauSecurityPMAnnounce,
       "madgeCauSecurityPMSafePollTimer": madgeCauSecurityPMSafePollTimer,
       "madgeCauSecurityPMSafeReplyTimeout": madgeCauSecurityPMSafeReplyTimeout,
       "madgeCauSecurityPMSafeRetries": madgeCauSecurityPMSafeRetries,
       "madgeCauSecurityAllowedManufacturers": madgeCauSecurityAllowedManufacturers,
       "madgeCauSecurityActionPM": madgeCauSecurityActionPM,
       "madgeCauSecurityActionPMUnsafe": madgeCauSecurityActionPMUnsafe,
       "madgeCauSecurityActionRogueNode": madgeCauSecurityActionRogueNode,
       "madgeCauSecurityActionIllegalMF": madgeCauSecurityActionIllegalMF,
       "madgeCauSecurityTable": madgeCauSecurityTable,
       "madgeCauSecurityEntry": madgeCauSecurityEntry,
       "madgeCauSecurityIndex": madgeCauSecurityIndex,
       "madgeCauSecurityNodeAddress": madgeCauSecurityNodeAddress,
       "madgeCauSecurityExceptionPM": madgeCauSecurityExceptionPM,
       "madgeCauSecurityExceptionPMUnsafe": madgeCauSecurityExceptionPMUnsafe,
       "madgeCauSecurityExceptionRogueNode": madgeCauSecurityExceptionRogueNode,
       "madgeCauSecurityExceptionIllegalMF": madgeCauSecurityExceptionIllegalMF,
       "madgeCauSecurityExceptionWrongNode": madgeCauSecurityExceptionWrongNode,
       "madgeCauSecurityActionWrongNode": madgeCauSecurityActionWrongNode,
       "madgeCauSecurityExtendedException": madgeCauSecurityExtendedException,
       "madgeCauFault": madgeCauFault,
       "madgeCauFaultRPFailAction": madgeCauFaultRPFailAction,
       "madgeCauFaultBeaconDefault": madgeCauFaultBeaconDefault,
       "madgeCauFaultBeaconThreshold": madgeCauFaultBeaconThreshold,
       "madgeCauFaultBeaconAction": madgeCauFaultBeaconAction,
       "madgeCauFaultRingPurgeDefault": madgeCauFaultRingPurgeDefault,
       "madgeCauFaultRingPurgeThreshold": madgeCauFaultRingPurgeThreshold,
       "madgeCauFaultRingPurgeAction": madgeCauFaultRingPurgeAction,
       "madgeCauFaultIsoErrDefault": madgeCauFaultIsoErrDefault,
       "madgeCauFaultIsoErrThreshold": madgeCauFaultIsoErrThreshold,
       "madgeCauFaultIsoErrAction": madgeCauFaultIsoErrAction,
       "madgeCauKill": madgeCauKill,
       "madgeCauKillNodeAddress": madgeCauKillNodeAddress,
       "madgeCauKillReason": madgeCauKillReason,
       "madgeCauKillStatus": madgeCauKillStatus,
       "madgeCauKillLamNo": madgeCauKillLamNo,
       "madgeCauKillPortNo": madgeCauKillPortNo,
       "madgeCauTrapInfo": madgeCauTrapInfo,
       "madgeCauTrapInfoLamNo": madgeCauTrapInfoLamNo,
       "madgeCauTrapInfoPortNo": madgeCauTrapInfoPortNo,
       "madgeCauTrapInfoState": madgeCauTrapInfoState}
)
