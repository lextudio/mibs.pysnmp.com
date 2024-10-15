# SNMP MIB module (CTRON-ENVIRONMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-ENVIRONMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:49 2024
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

(ctenv,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctenv")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChEnv_ObjectIdentity = ObjectIdentity
chEnv = _ChEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1)
)
_ChEnvAmbientTemp_Type = Integer32
_ChEnvAmbientTemp_Object = MibScalar
chEnvAmbientTemp = _ChEnvAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 1),
    _ChEnvAmbientTemp_Type()
)
chEnvAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvAmbientTemp.setStatus("mandatory")


class _ChEnvAmbientStatus_Type(Integer32):
    """Custom type chEnvAmbientStatus based on Integer32"""
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
        *(("cold", 2),
          ("cool", 3),
          ("hot", 6),
          ("inoperative", 7),
          ("normal", 4),
          ("unknown", 1),
          ("warm", 5))
    )


_ChEnvAmbientStatus_Type.__name__ = "Integer32"
_ChEnvAmbientStatus_Object = MibScalar
chEnvAmbientStatus = _ChEnvAmbientStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 2),
    _ChEnvAmbientStatus_Type()
)
chEnvAmbientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvAmbientStatus.setStatus("mandatory")
_ChEnvHumidity_Type = Integer32
_ChEnvHumidity_Object = MibScalar
chEnvHumidity = _ChEnvHumidity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 3),
    _ChEnvHumidity_Type()
)
chEnvHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvHumidity.setStatus("mandatory")


class _ChEnvHumidityStatus_Type(Integer32):
    """Custom type chEnvHumidityStatus based on Integer32"""
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
        *(("dry", 2),
          ("inoperative", 5),
          ("moist", 4),
          ("normal", 3),
          ("unknown", 1))
    )


_ChEnvHumidityStatus_Type.__name__ = "Integer32"
_ChEnvHumidityStatus_Object = MibScalar
chEnvHumidityStatus = _ChEnvHumidityStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 4),
    _ChEnvHumidityStatus_Type()
)
chEnvHumidityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvHumidityStatus.setStatus("mandatory")
_ChEnvAmbientHot_Type = Integer32
_ChEnvAmbientHot_Object = MibScalar
chEnvAmbientHot = _ChEnvAmbientHot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 5),
    _ChEnvAmbientHot_Type()
)
chEnvAmbientHot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvAmbientHot.setStatus("mandatory")
_ChEnvAmbientWarm_Type = Integer32
_ChEnvAmbientWarm_Object = MibScalar
chEnvAmbientWarm = _ChEnvAmbientWarm_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 6),
    _ChEnvAmbientWarm_Type()
)
chEnvAmbientWarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvAmbientWarm.setStatus("mandatory")
_ChEnvAmbientCool_Type = Integer32
_ChEnvAmbientCool_Object = MibScalar
chEnvAmbientCool = _ChEnvAmbientCool_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 7),
    _ChEnvAmbientCool_Type()
)
chEnvAmbientCool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvAmbientCool.setStatus("mandatory")
_ChEnvAmbientCold_Type = Integer32
_ChEnvAmbientCold_Object = MibScalar
chEnvAmbientCold = _ChEnvAmbientCold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 8),
    _ChEnvAmbientCold_Type()
)
chEnvAmbientCold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvAmbientCold.setStatus("mandatory")
_ChEnvHumidityMoist_Type = Integer32
_ChEnvHumidityMoist_Object = MibScalar
chEnvHumidityMoist = _ChEnvHumidityMoist_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 9),
    _ChEnvHumidityMoist_Type()
)
chEnvHumidityMoist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvHumidityMoist.setStatus("mandatory")
_ChEnvHumidityDry_Type = Integer32
_ChEnvHumidityDry_Object = MibScalar
chEnvHumidityDry = _ChEnvHumidityDry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 10),
    _ChEnvHumidityDry_Type()
)
chEnvHumidityDry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvHumidityDry.setStatus("mandatory")


class _ChEnvNumFans_Type(Integer32):
    """Custom type chEnvNumFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ChEnvNumFans_Type.__name__ = "Integer32"
_ChEnvNumFans_Object = MibScalar
chEnvNumFans = _ChEnvNumFans_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 11),
    _ChEnvNumFans_Type()
)
chEnvNumFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvNumFans.setStatus("mandatory")
_ChEnvFanTable_Object = MibTable
chEnvFanTable = _ChEnvFanTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12)
)
if mibBuilder.loadTexts:
    chEnvFanTable.setStatus("mandatory")
_ChEnvFanEntry_Object = MibTableRow
chEnvFanEntry = _ChEnvFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1)
)
chEnvFanEntry.setIndexNames(
    (0, "CTRON-ENVIRONMENT-MIB", "chEnvFanID"),
)
if mibBuilder.loadTexts:
    chEnvFanEntry.setStatus("mandatory")
_ChEnvFanID_Type = Integer32
_ChEnvFanID_Object = MibTableColumn
chEnvFanID = _ChEnvFanID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 1),
    _ChEnvFanID_Type()
)
chEnvFanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvFanID.setStatus("mandatory")


class _ChEnvFanStatus_Type(Integer32):
    """Custom type chEnvFanStatus based on Integer32"""
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
        *(("inoperative", 5),
          ("normal", 2),
          ("off", 6),
          ("slow", 4),
          ("testing", 3),
          ("unknown", 1))
    )


_ChEnvFanStatus_Type.__name__ = "Integer32"
_ChEnvFanStatus_Object = MibTableColumn
chEnvFanStatus = _ChEnvFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 2),
    _ChEnvFanStatus_Type()
)
chEnvFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvFanStatus.setStatus("mandatory")


class _ChEnvFanAdmin_Type(Integer32):
    """Custom type chEnvFanAdmin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoMode", 1),
          ("fullSpeed", 2),
          ("testingMode", 3))
    )


_ChEnvFanAdmin_Type.__name__ = "Integer32"
_ChEnvFanAdmin_Object = MibTableColumn
chEnvFanAdmin = _ChEnvFanAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 3),
    _ChEnvFanAdmin_Type()
)
chEnvFanAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chEnvFanAdmin.setStatus("mandatory")
_ChEnvFanSpeed_Type = Integer32
_ChEnvFanSpeed_Object = MibTableColumn
chEnvFanSpeed = _ChEnvFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 4),
    _ChEnvFanSpeed_Type()
)
chEnvFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEnvFanSpeed.setStatus("mandatory")
_BoardEnv_ObjectIdentity = ObjectIdentity
boardEnv = _BoardEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2)
)
_BoardEnvSlotTable_Object = MibTable
boardEnvSlotTable = _BoardEnvSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    boardEnvSlotTable.setStatus("mandatory")
_BoardEnvSlotEntry_Object = MibTableRow
boardEnvSlotEntry = _BoardEnvSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1)
)
boardEnvSlotEntry.setIndexNames(
    (0, "CTRON-ENVIRONMENT-MIB", "boardEnvSlotID"),
)
if mibBuilder.loadTexts:
    boardEnvSlotEntry.setStatus("mandatory")
_BoardEnvSlotID_Type = Integer32
_BoardEnvSlotID_Object = MibTableColumn
boardEnvSlotID = _BoardEnvSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 1),
    _BoardEnvSlotID_Type()
)
boardEnvSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvSlotID.setStatus("mandatory")
_BoardEnvTemp_Type = Integer32
_BoardEnvTemp_Object = MibTableColumn
boardEnvTemp = _BoardEnvTemp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 2),
    _BoardEnvTemp_Type()
)
boardEnvTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTemp.setStatus("mandatory")


class _BoardEnvTempStatus_Type(Integer32):
    """Custom type boardEnvTempStatus based on Integer32"""
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
        *(("cold", 2),
          ("cool", 3),
          ("hot", 6),
          ("inoperative", 7),
          ("normal", 4),
          ("unknown", 1),
          ("warm", 5))
    )


_BoardEnvTempStatus_Type.__name__ = "Integer32"
_BoardEnvTempStatus_Object = MibTableColumn
boardEnvTempStatus = _BoardEnvTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 3),
    _BoardEnvTempStatus_Type()
)
boardEnvTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTempStatus.setStatus("mandatory")


class _BoardEnvTempRelStatus_Type(Integer32):
    """Custom type boardEnvTempRelStatus based on Integer32"""
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
        *(("hot", 4),
          ("inoperative", 5),
          ("normal", 2),
          ("unknown", 1),
          ("warm", 3))
    )


_BoardEnvTempRelStatus_Type.__name__ = "Integer32"
_BoardEnvTempRelStatus_Object = MibTableColumn
boardEnvTempRelStatus = _BoardEnvTempRelStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 4),
    _BoardEnvTempRelStatus_Type()
)
boardEnvTempRelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTempRelStatus.setStatus("mandatory")


class _BoardEnvShutdownAdmin_Type(Integer32):
    """Custom type boardEnvShutdownAdmin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BoardEnvShutdownAdmin_Type.__name__ = "Integer32"
_BoardEnvShutdownAdmin_Object = MibTableColumn
boardEnvShutdownAdmin = _BoardEnvShutdownAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 5),
    _BoardEnvShutdownAdmin_Type()
)
boardEnvShutdownAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardEnvShutdownAdmin.setStatus("mandatory")
_BoardEnvTempHot_Type = Integer32
_BoardEnvTempHot_Object = MibTableColumn
boardEnvTempHot = _BoardEnvTempHot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 6),
    _BoardEnvTempHot_Type()
)
boardEnvTempHot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTempHot.setStatus("mandatory")
_BoardEnvTempWarm_Type = Integer32
_BoardEnvTempWarm_Object = MibTableColumn
boardEnvTempWarm = _BoardEnvTempWarm_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 7),
    _BoardEnvTempWarm_Type()
)
boardEnvTempWarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTempWarm.setStatus("mandatory")
_BoardEnvTempCool_Type = Integer32
_BoardEnvTempCool_Object = MibTableColumn
boardEnvTempCool = _BoardEnvTempCool_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 8),
    _BoardEnvTempCool_Type()
)
boardEnvTempCool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTempCool.setStatus("mandatory")
_BoardEnvTempCold_Type = Integer32
_BoardEnvTempCold_Object = MibTableColumn
boardEnvTempCold = _BoardEnvTempCold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 9),
    _BoardEnvTempCold_Type()
)
boardEnvTempCold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTempCold.setStatus("mandatory")
_BoardEnvTempRelHot_Type = Integer32
_BoardEnvTempRelHot_Object = MibTableColumn
boardEnvTempRelHot = _BoardEnvTempRelHot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 10),
    _BoardEnvTempRelHot_Type()
)
boardEnvTempRelHot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTempRelHot.setStatus("mandatory")
_BoardEnvTempRelWarm_Type = Integer32
_BoardEnvTempRelWarm_Object = MibTableColumn
boardEnvTempRelWarm = _BoardEnvTempRelWarm_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 11),
    _BoardEnvTempRelWarm_Type()
)
boardEnvTempRelWarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTempRelWarm.setStatus("mandatory")
_BoardEnvTempMaxFanRelHot_Type = Integer32
_BoardEnvTempMaxFanRelHot_Object = MibTableColumn
boardEnvTempMaxFanRelHot = _BoardEnvTempMaxFanRelHot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 12),
    _BoardEnvTempMaxFanRelHot_Type()
)
boardEnvTempMaxFanRelHot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTempMaxFanRelHot.setStatus("mandatory")
_BoardEnvTempMaxFanRelWarm_Type = Integer32
_BoardEnvTempMaxFanRelWarm_Object = MibTableColumn
boardEnvTempMaxFanRelWarm = _BoardEnvTempMaxFanRelWarm_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 13),
    _BoardEnvTempMaxFanRelWarm_Type()
)
boardEnvTempMaxFanRelWarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEnvTempMaxFanRelWarm.setStatus("mandatory")
_PsEnv_ObjectIdentity = ObjectIdentity
psEnv = _PsEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3)
)
_PsEnvSlotTable_Object = MibTable
psEnvSlotTable = _PsEnvSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    psEnvSlotTable.setStatus("mandatory")
_PsEnvSlotEntry_Object = MibTableRow
psEnvSlotEntry = _PsEnvSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1)
)
psEnvSlotEntry.setIndexNames(
    (0, "CTRON-ENVIRONMENT-MIB", "psEnvSlotID"),
)
if mibBuilder.loadTexts:
    psEnvSlotEntry.setStatus("mandatory")
_PsEnvSlotID_Type = Integer32
_PsEnvSlotID_Object = MibTableColumn
psEnvSlotID = _PsEnvSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 1),
    _PsEnvSlotID_Type()
)
psEnvSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnvSlotID.setStatus("mandatory")
_PsEnvTemp_Type = Integer32
_PsEnvTemp_Object = MibTableColumn
psEnvTemp = _PsEnvTemp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 2),
    _PsEnvTemp_Type()
)
psEnvTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnvTemp.setStatus("mandatory")


class _PsEnvTempStatus_Type(Integer32):
    """Custom type psEnvTempStatus based on Integer32"""
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
        *(("cold", 2),
          ("cool", 3),
          ("hot", 6),
          ("inoperative", 7),
          ("normal", 4),
          ("unknown", 1),
          ("warm", 5))
    )


_PsEnvTempStatus_Type.__name__ = "Integer32"
_PsEnvTempStatus_Object = MibTableColumn
psEnvTempStatus = _PsEnvTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 3),
    _PsEnvTempStatus_Type()
)
psEnvTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnvTempStatus.setStatus("mandatory")
_PsEnvTempHot_Type = Integer32
_PsEnvTempHot_Object = MibTableColumn
psEnvTempHot = _PsEnvTempHot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 4),
    _PsEnvTempHot_Type()
)
psEnvTempHot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnvTempHot.setStatus("mandatory")
_PsEnvTempWarm_Type = Integer32
_PsEnvTempWarm_Object = MibTableColumn
psEnvTempWarm = _PsEnvTempWarm_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 5),
    _PsEnvTempWarm_Type()
)
psEnvTempWarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnvTempWarm.setStatus("mandatory")
_PsEnvTempCool_Type = Integer32
_PsEnvTempCool_Object = MibTableColumn
psEnvTempCool = _PsEnvTempCool_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 6),
    _PsEnvTempCool_Type()
)
psEnvTempCool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnvTempCool.setStatus("mandatory")
_PsEnvTempCold_Type = Integer32
_PsEnvTempCold_Object = MibTableColumn
psEnvTempCold = _PsEnvTempCold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 7),
    _PsEnvTempCold_Type()
)
psEnvTempCold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnvTempCold.setStatus("mandatory")


class _PsEnvFanStatus_Type(Integer32):
    """Custom type psEnvFanStatus based on Integer32"""
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
        *(("inoperative", 5),
          ("normal", 2),
          ("off", 6),
          ("slow", 4),
          ("testing", 3),
          ("unknown", 1))
    )


_PsEnvFanStatus_Type.__name__ = "Integer32"
_PsEnvFanStatus_Object = MibTableColumn
psEnvFanStatus = _PsEnvFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 8),
    _PsEnvFanStatus_Type()
)
psEnvFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnvFanStatus.setStatus("mandatory")


class _PsEnvFanAdmin_Type(Integer32):
    """Custom type psEnvFanAdmin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoMode", 1),
          ("fullSpeed", 2),
          ("testingMode", 3))
    )


_PsEnvFanAdmin_Type.__name__ = "Integer32"
_PsEnvFanAdmin_Object = MibTableColumn
psEnvFanAdmin = _PsEnvFanAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 9),
    _PsEnvFanAdmin_Type()
)
psEnvFanAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEnvFanAdmin.setStatus("mandatory")
_PsEnvFanSpeed_Type = Integer32
_PsEnvFanSpeed_Object = MibTableColumn
psEnvFanSpeed = _PsEnvFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 10),
    _PsEnvFanSpeed_Type()
)
psEnvFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnvFanSpeed.setStatus("mandatory")
_BbuEnv_ObjectIdentity = ObjectIdentity
bbuEnv = _BbuEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ENVIRONMENT-MIB",
    **{"chEnv": chEnv,
       "chEnvAmbientTemp": chEnvAmbientTemp,
       "chEnvAmbientStatus": chEnvAmbientStatus,
       "chEnvHumidity": chEnvHumidity,
       "chEnvHumidityStatus": chEnvHumidityStatus,
       "chEnvAmbientHot": chEnvAmbientHot,
       "chEnvAmbientWarm": chEnvAmbientWarm,
       "chEnvAmbientCool": chEnvAmbientCool,
       "chEnvAmbientCold": chEnvAmbientCold,
       "chEnvHumidityMoist": chEnvHumidityMoist,
       "chEnvHumidityDry": chEnvHumidityDry,
       "chEnvNumFans": chEnvNumFans,
       "chEnvFanTable": chEnvFanTable,
       "chEnvFanEntry": chEnvFanEntry,
       "chEnvFanID": chEnvFanID,
       "chEnvFanStatus": chEnvFanStatus,
       "chEnvFanAdmin": chEnvFanAdmin,
       "chEnvFanSpeed": chEnvFanSpeed,
       "boardEnv": boardEnv,
       "boardEnvSlotTable": boardEnvSlotTable,
       "boardEnvSlotEntry": boardEnvSlotEntry,
       "boardEnvSlotID": boardEnvSlotID,
       "boardEnvTemp": boardEnvTemp,
       "boardEnvTempStatus": boardEnvTempStatus,
       "boardEnvTempRelStatus": boardEnvTempRelStatus,
       "boardEnvShutdownAdmin": boardEnvShutdownAdmin,
       "boardEnvTempHot": boardEnvTempHot,
       "boardEnvTempWarm": boardEnvTempWarm,
       "boardEnvTempCool": boardEnvTempCool,
       "boardEnvTempCold": boardEnvTempCold,
       "boardEnvTempRelHot": boardEnvTempRelHot,
       "boardEnvTempRelWarm": boardEnvTempRelWarm,
       "boardEnvTempMaxFanRelHot": boardEnvTempMaxFanRelHot,
       "boardEnvTempMaxFanRelWarm": boardEnvTempMaxFanRelWarm,
       "psEnv": psEnv,
       "psEnvSlotTable": psEnvSlotTable,
       "psEnvSlotEntry": psEnvSlotEntry,
       "psEnvSlotID": psEnvSlotID,
       "psEnvTemp": psEnvTemp,
       "psEnvTempStatus": psEnvTempStatus,
       "psEnvTempHot": psEnvTempHot,
       "psEnvTempWarm": psEnvTempWarm,
       "psEnvTempCool": psEnvTempCool,
       "psEnvTempCold": psEnvTempCold,
       "psEnvFanStatus": psEnvFanStatus,
       "psEnvFanAdmin": psEnvFanAdmin,
       "psEnvFanSpeed": psEnvFanSpeed,
       "bbuEnv": bbuEnv}
)
