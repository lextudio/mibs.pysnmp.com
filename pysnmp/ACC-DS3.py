# SNMP MIB module (ACC-DS3) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-DS3
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:08 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccDs3InfcTable_Object = MibTable
accDs3InfcTable = _AccDs3InfcTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79)
)
if mibBuilder.loadTexts:
    accDs3InfcTable.setStatus("mandatory")
_AccDs3InfcEntry_Object = MibTableRow
accDs3InfcEntry = _AccDs3InfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1)
)
accDs3InfcEntry.setIndexNames(
    (0, "ACC-DS3", "accDs3InfcServiceState"),
)
if mibBuilder.loadTexts:
    accDs3InfcEntry.setStatus("mandatory")


class _AccDs3InfcServiceState_Type(Integer32):
    """Custom type accDs3InfcServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3InfcInService", 1),
          ("ds3InfcOutOfServer", 2))
    )


_AccDs3InfcServiceState_Type.__name__ = "Integer32"
_AccDs3InfcServiceState_Object = MibTableColumn
accDs3InfcServiceState = _AccDs3InfcServiceState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 1),
    _AccDs3InfcServiceState_Type()
)
accDs3InfcServiceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcServiceState.setStatus("mandatory")


class _AccDs3InfcLoopbackOp_Type(Integer32):
    """Custom type accDs3InfcLoopbackOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60)
        )
    )
    namedValues = NamedValues(
        *(("accDs3InfcEquipLoop", 4),
          ("accDs3InfcLineLoop", 3),
          ("accDs3NoInfcLoop", 1),
          ("accDs3PaybackLoop", 2),
          ("ds1loop-1", 33),
          ("ds1loop-10", 42),
          ("ds1loop-11", 43),
          ("ds1loop-12", 44),
          ("ds1loop-13", 45),
          ("ds1loop-14", 46),
          ("ds1loop-15", 47),
          ("ds1loop-16", 48),
          ("ds1loop-17", 49),
          ("ds1loop-18", 50),
          ("ds1loop-19", 51),
          ("ds1loop-2", 34),
          ("ds1loop-20", 52),
          ("ds1loop-21", 53),
          ("ds1loop-22", 54),
          ("ds1loop-23", 55),
          ("ds1loop-24", 56),
          ("ds1loop-25", 57),
          ("ds1loop-26", 58),
          ("ds1loop-27", 59),
          ("ds1loop-28", 60),
          ("ds1loop-3", 35),
          ("ds1loop-4", 36),
          ("ds1loop-5", 37),
          ("ds1loop-6", 38),
          ("ds1loop-7", 39),
          ("ds1loop-8", 40),
          ("ds1loop-9", 41))
    )


_AccDs3InfcLoopbackOp_Type.__name__ = "Integer32"
_AccDs3InfcLoopbackOp_Object = MibTableColumn
accDs3InfcLoopbackOp = _AccDs3InfcLoopbackOp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 2),
    _AccDs3InfcLoopbackOp_Type()
)
accDs3InfcLoopbackOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcLoopbackOp.setStatus("mandatory")


class _AccDs3InfcLoopbackCO_Type(Integer32):
    """Custom type accDs3InfcLoopbackCO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              19,
              27,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60)
        )
    )
    namedValues = NamedValues(
        *(("accDs3DS1LoopAll", 19),
          ("accDs3LineLoop", 27),
          ("accDs3NoLoop", 1),
          ("ds1loop-1", 33),
          ("ds1loop-10", 42),
          ("ds1loop-11", 43),
          ("ds1loop-12", 44),
          ("ds1loop-13", 45),
          ("ds1loop-14", 46),
          ("ds1loop-15", 47),
          ("ds1loop-16", 48),
          ("ds1loop-17", 49),
          ("ds1loop-18", 50),
          ("ds1loop-19", 51),
          ("ds1loop-2", 34),
          ("ds1loop-20", 52),
          ("ds1loop-21", 53),
          ("ds1loop-22", 54),
          ("ds1loop-23", 55),
          ("ds1loop-24", 56),
          ("ds1loop-25", 57),
          ("ds1loop-26", 58),
          ("ds1loop-27", 59),
          ("ds1loop-28", 60),
          ("ds1loop-3", 35),
          ("ds1loop-4", 36),
          ("ds1loop-5", 37),
          ("ds1loop-6", 38),
          ("ds1loop-7", 39),
          ("ds1loop-8", 40),
          ("ds1loop-9", 41))
    )


_AccDs3InfcLoopbackCO_Type.__name__ = "Integer32"
_AccDs3InfcLoopbackCO_Object = MibTableColumn
accDs3InfcLoopbackCO = _AccDs3InfcLoopbackCO_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 3),
    _AccDs3InfcLoopbackCO_Type()
)
accDs3InfcLoopbackCO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcLoopbackCO.setStatus("mandatory")


class _AccDs3InfcLineLength_Type(Integer32):
    """Custom type accDs3InfcLineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3LongLine", 2),
          ("ds3ShortLine", 1))
    )


_AccDs3InfcLineLength_Type.__name__ = "Integer32"
_AccDs3InfcLineLength_Object = MibTableColumn
accDs3InfcLineLength = _AccDs3InfcLineLength_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 4),
    _AccDs3InfcLineLength_Type()
)
accDs3InfcLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcLineLength.setStatus("mandatory")


class _AccDs3InfcMdlProtocol_Type(Integer32):
    """Custom type accDs3InfcMdlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3Ansi", 1),
          ("ds3NoProtocol", 2))
    )


_AccDs3InfcMdlProtocol_Type.__name__ = "Integer32"
_AccDs3InfcMdlProtocol_Object = MibTableColumn
accDs3InfcMdlProtocol = _AccDs3InfcMdlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 5),
    _AccDs3InfcMdlProtocol_Type()
)
accDs3InfcMdlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcMdlProtocol.setStatus("mandatory")
_AccDs3InfcTxMdlEic_Type = DisplayString
_AccDs3InfcTxMdlEic_Object = MibTableColumn
accDs3InfcTxMdlEic = _AccDs3InfcTxMdlEic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 6),
    _AccDs3InfcTxMdlEic_Type()
)
accDs3InfcTxMdlEic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcTxMdlEic.setStatus("mandatory")
_AccDs3InfcTxMdlLic_Type = DisplayString
_AccDs3InfcTxMdlLic_Object = MibTableColumn
accDs3InfcTxMdlLic = _AccDs3InfcTxMdlLic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 7),
    _AccDs3InfcTxMdlLic_Type()
)
accDs3InfcTxMdlLic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcTxMdlLic.setStatus("mandatory")
_AccDs3InfcTxMdlFic_Type = DisplayString
_AccDs3InfcTxMdlFic_Object = MibTableColumn
accDs3InfcTxMdlFic = _AccDs3InfcTxMdlFic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 8),
    _AccDs3InfcTxMdlFic_Type()
)
accDs3InfcTxMdlFic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcTxMdlFic.setStatus("mandatory")
_AccDs3InfcTxMdlUnit_Type = DisplayString
_AccDs3InfcTxMdlUnit_Object = MibTableColumn
accDs3InfcTxMdlUnit = _AccDs3InfcTxMdlUnit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 9),
    _AccDs3InfcTxMdlUnit_Type()
)
accDs3InfcTxMdlUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcTxMdlUnit.setStatus("mandatory")
_AccDs3InfcTxMdlFac_Type = DisplayString
_AccDs3InfcTxMdlFac_Object = MibTableColumn
accDs3InfcTxMdlFac = _AccDs3InfcTxMdlFac_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 10),
    _AccDs3InfcTxMdlFac_Type()
)
accDs3InfcTxMdlFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcTxMdlFac.setStatus("mandatory")
_AccDs3InfcTxMdlPort_Type = DisplayString
_AccDs3InfcTxMdlPort_Object = MibTableColumn
accDs3InfcTxMdlPort = _AccDs3InfcTxMdlPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 11),
    _AccDs3InfcTxMdlPort_Type()
)
accDs3InfcTxMdlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcTxMdlPort.setStatus("mandatory")
_AccDs3InfcTxMdlGen_Type = DisplayString
_AccDs3InfcTxMdlGen_Object = MibTableColumn
accDs3InfcTxMdlGen = _AccDs3InfcTxMdlGen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 12),
    _AccDs3InfcTxMdlGen_Type()
)
accDs3InfcTxMdlGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs3InfcTxMdlGen.setStatus("mandatory")
_AccDs3InfcRxMdlEic_Type = DisplayString
_AccDs3InfcRxMdlEic_Object = MibTableColumn
accDs3InfcRxMdlEic = _AccDs3InfcRxMdlEic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 13),
    _AccDs3InfcRxMdlEic_Type()
)
accDs3InfcRxMdlEic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcRxMdlEic.setStatus("mandatory")
_AccDs3InfcRxMdlLic_Type = DisplayString
_AccDs3InfcRxMdlLic_Object = MibTableColumn
accDs3InfcRxMdlLic = _AccDs3InfcRxMdlLic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 14),
    _AccDs3InfcRxMdlLic_Type()
)
accDs3InfcRxMdlLic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcRxMdlLic.setStatus("mandatory")
_AccDs3InfcRxMdlFic_Type = DisplayString
_AccDs3InfcRxMdlFic_Object = MibTableColumn
accDs3InfcRxMdlFic = _AccDs3InfcRxMdlFic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 15),
    _AccDs3InfcRxMdlFic_Type()
)
accDs3InfcRxMdlFic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcRxMdlFic.setStatus("mandatory")
_AccDs3InfcRxMdlUnit_Type = DisplayString
_AccDs3InfcRxMdlUnit_Object = MibTableColumn
accDs3InfcRxMdlUnit = _AccDs3InfcRxMdlUnit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 16),
    _AccDs3InfcRxMdlUnit_Type()
)
accDs3InfcRxMdlUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcRxMdlUnit.setStatus("mandatory")
_AccDs3InfcRxMdlFac_Type = DisplayString
_AccDs3InfcRxMdlFac_Object = MibTableColumn
accDs3InfcRxMdlFac = _AccDs3InfcRxMdlFac_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 17),
    _AccDs3InfcRxMdlFac_Type()
)
accDs3InfcRxMdlFac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcRxMdlFac.setStatus("mandatory")
_AccDs3InfcRxMdlPort_Type = DisplayString
_AccDs3InfcRxMdlPort_Object = MibTableColumn
accDs3InfcRxMdlPort = _AccDs3InfcRxMdlPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 18),
    _AccDs3InfcRxMdlPort_Type()
)
accDs3InfcRxMdlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcRxMdlPort.setStatus("mandatory")
_AccDs3InfcRxMdlGen_Type = DisplayString
_AccDs3InfcRxMdlGen_Object = MibTableColumn
accDs3InfcRxMdlGen = _AccDs3InfcRxMdlGen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 19),
    _AccDs3InfcRxMdlGen_Type()
)
accDs3InfcRxMdlGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcRxMdlGen.setStatus("mandatory")
_AccDs3InfcRxMdlPathAges_Type = Counter32
_AccDs3InfcRxMdlPathAges_Object = MibTableColumn
accDs3InfcRxMdlPathAges = _AccDs3InfcRxMdlPathAges_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 20),
    _AccDs3InfcRxMdlPathAges_Type()
)
accDs3InfcRxMdlPathAges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcRxMdlPathAges.setStatus("mandatory")
_AccDs3InfcRxMdlIdleAges_Type = Counter32
_AccDs3InfcRxMdlIdleAges_Object = MibTableColumn
accDs3InfcRxMdlIdleAges = _AccDs3InfcRxMdlIdleAges_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 21),
    _AccDs3InfcRxMdlIdleAges_Type()
)
accDs3InfcRxMdlIdleAges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcRxMdlIdleAges.setStatus("mandatory")
_AccDs3InfcRxMdlTestAges_Type = Counter32
_AccDs3InfcRxMdlTestAges_Object = MibTableColumn
accDs3InfcRxMdlTestAges = _AccDs3InfcRxMdlTestAges_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 79, 1, 22),
    _AccDs3InfcRxMdlTestAges_Type()
)
accDs3InfcRxMdlTestAges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs3InfcRxMdlTestAges.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-DS3",
    **{"accDs3InfcTable": accDs3InfcTable,
       "accDs3InfcEntry": accDs3InfcEntry,
       "accDs3InfcServiceState": accDs3InfcServiceState,
       "accDs3InfcLoopbackOp": accDs3InfcLoopbackOp,
       "accDs3InfcLoopbackCO": accDs3InfcLoopbackCO,
       "accDs3InfcLineLength": accDs3InfcLineLength,
       "accDs3InfcMdlProtocol": accDs3InfcMdlProtocol,
       "accDs3InfcTxMdlEic": accDs3InfcTxMdlEic,
       "accDs3InfcTxMdlLic": accDs3InfcTxMdlLic,
       "accDs3InfcTxMdlFic": accDs3InfcTxMdlFic,
       "accDs3InfcTxMdlUnit": accDs3InfcTxMdlUnit,
       "accDs3InfcTxMdlFac": accDs3InfcTxMdlFac,
       "accDs3InfcTxMdlPort": accDs3InfcTxMdlPort,
       "accDs3InfcTxMdlGen": accDs3InfcTxMdlGen,
       "accDs3InfcRxMdlEic": accDs3InfcRxMdlEic,
       "accDs3InfcRxMdlLic": accDs3InfcRxMdlLic,
       "accDs3InfcRxMdlFic": accDs3InfcRxMdlFic,
       "accDs3InfcRxMdlUnit": accDs3InfcRxMdlUnit,
       "accDs3InfcRxMdlFac": accDs3InfcRxMdlFac,
       "accDs3InfcRxMdlPort": accDs3InfcRxMdlPort,
       "accDs3InfcRxMdlGen": accDs3InfcRxMdlGen,
       "accDs3InfcRxMdlPathAges": accDs3InfcRxMdlPathAges,
       "accDs3InfcRxMdlIdleAges": accDs3InfcRxMdlIdleAges,
       "accDs3InfcRxMdlTestAges": accDs3InfcRxMdlTestAges}
)
