# SNMP MIB module (SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:41 2024
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

sonetMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonetObjects_ObjectIdentity = ObjectIdentity
sonetObjects = _SonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 1)
)
_SonetMedium_ObjectIdentity = ObjectIdentity
sonetMedium = _SonetMedium_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 1)
)
_SonetMediumTable_Object = MibTable
sonetMediumTable = _SonetMediumTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sonetMediumTable.setStatus("current")
_SonetMediumEntry_Object = MibTableRow
sonetMediumEntry = _SonetMediumEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1)
)
sonetMediumEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetMediumEntry.setStatus("current")


class _SonetMediumType_Type(Integer32):
    """Custom type sonetMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_SonetMediumType_Type.__name__ = "Integer32"
_SonetMediumType_Object = MibTableColumn
sonetMediumType = _SonetMediumType_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 1),
    _SonetMediumType_Type()
)
sonetMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetMediumType.setStatus("current")


class _SonetMediumTimeElapsed_Type(Integer32):
    """Custom type sonetMediumTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetMediumTimeElapsed_Type.__name__ = "Integer32"
_SonetMediumTimeElapsed_Object = MibTableColumn
sonetMediumTimeElapsed = _SonetMediumTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 2),
    _SonetMediumTimeElapsed_Type()
)
sonetMediumTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetMediumTimeElapsed.setStatus("current")


class _SonetMediumValidIntervals_Type(Integer32):
    """Custom type sonetMediumValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_SonetMediumValidIntervals_Type.__name__ = "Integer32"
_SonetMediumValidIntervals_Object = MibTableColumn
sonetMediumValidIntervals = _SonetMediumValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 3),
    _SonetMediumValidIntervals_Type()
)
sonetMediumValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetMediumValidIntervals.setStatus("current")


class _SonetMediumLineCoding_Type(Integer32):
    """Custom type sonetMediumLineCoding based on Integer32"""
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
        *(("sonetMediumB3ZS", 2),
          ("sonetMediumCMI", 3),
          ("sonetMediumNRZ", 4),
          ("sonetMediumOther", 1),
          ("sonetMediumRZ", 5))
    )


_SonetMediumLineCoding_Type.__name__ = "Integer32"
_SonetMediumLineCoding_Object = MibTableColumn
sonetMediumLineCoding = _SonetMediumLineCoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 4),
    _SonetMediumLineCoding_Type()
)
sonetMediumLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetMediumLineCoding.setStatus("current")


class _SonetMediumLineType_Type(Integer32):
    """Custom type sonetMediumLineType based on Integer32"""
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
        *(("sonetCoax", 5),
          ("sonetLongSingleMode", 3),
          ("sonetMultiMode", 4),
          ("sonetOther", 1),
          ("sonetShortSingleMode", 2),
          ("sonetUTP", 6))
    )


_SonetMediumLineType_Type.__name__ = "Integer32"
_SonetMediumLineType_Object = MibTableColumn
sonetMediumLineType = _SonetMediumLineType_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 5),
    _SonetMediumLineType_Type()
)
sonetMediumLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetMediumLineType.setStatus("current")


class _SonetMediumCircuitIdentifier_Type(DisplayString):
    """Custom type sonetMediumCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SonetMediumCircuitIdentifier_Type.__name__ = "DisplayString"
_SonetMediumCircuitIdentifier_Object = MibTableColumn
sonetMediumCircuitIdentifier = _SonetMediumCircuitIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 6),
    _SonetMediumCircuitIdentifier_Type()
)
sonetMediumCircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetMediumCircuitIdentifier.setStatus("current")
_SonetSection_ObjectIdentity = ObjectIdentity
sonetSection = _SonetSection_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2)
)
_SonetSectionCurrentTable_Object = MibTable
sonetSectionCurrentTable = _SonetSectionCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sonetSectionCurrentTable.setStatus("current")
_SonetSectionCurrentEntry_Object = MibTableRow
sonetSectionCurrentEntry = _SonetSectionCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1)
)
sonetSectionCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetSectionCurrentEntry.setStatus("current")


class _SonetSectionCurrentStatus_Type(Integer32):
    """Custom type sonetSectionCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonetSectionCurrentStatus_Type.__name__ = "Integer32"
_SonetSectionCurrentStatus_Object = MibTableColumn
sonetSectionCurrentStatus = _SonetSectionCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 1),
    _SonetSectionCurrentStatus_Type()
)
sonetSectionCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentStatus.setStatus("current")
_SonetSectionCurrentESs_Type = Gauge32
_SonetSectionCurrentESs_Object = MibTableColumn
sonetSectionCurrentESs = _SonetSectionCurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 2),
    _SonetSectionCurrentESs_Type()
)
sonetSectionCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentESs.setStatus("current")
_SonetSectionCurrentSESs_Type = Gauge32
_SonetSectionCurrentSESs_Object = MibTableColumn
sonetSectionCurrentSESs = _SonetSectionCurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 3),
    _SonetSectionCurrentSESs_Type()
)
sonetSectionCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentSESs.setStatus("current")
_SonetSectionCurrentSEFSs_Type = Gauge32
_SonetSectionCurrentSEFSs_Object = MibTableColumn
sonetSectionCurrentSEFSs = _SonetSectionCurrentSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 4),
    _SonetSectionCurrentSEFSs_Type()
)
sonetSectionCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentSEFSs.setStatus("current")
_SonetSectionCurrentCVs_Type = Gauge32
_SonetSectionCurrentCVs_Object = MibTableColumn
sonetSectionCurrentCVs = _SonetSectionCurrentCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 5),
    _SonetSectionCurrentCVs_Type()
)
sonetSectionCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentCVs.setStatus("current")
_SonetSectionIntervalTable_Object = MibTable
sonetSectionIntervalTable = _SonetSectionIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonetSectionIntervalTable.setStatus("current")
_SonetSectionIntervalEntry_Object = MibTableRow
sonetSectionIntervalEntry = _SonetSectionIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1)
)
sonetSectionIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetSectionIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetSectionIntervalEntry.setStatus("current")


class _SonetSectionIntervalNumber_Type(Integer32):
    """Custom type sonetSectionIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SonetSectionIntervalNumber_Type.__name__ = "Integer32"
_SonetSectionIntervalNumber_Object = MibTableColumn
sonetSectionIntervalNumber = _SonetSectionIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 1),
    _SonetSectionIntervalNumber_Type()
)
sonetSectionIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetSectionIntervalNumber.setStatus("current")
_SonetSectionIntervalESs_Type = Gauge32
_SonetSectionIntervalESs_Object = MibTableColumn
sonetSectionIntervalESs = _SonetSectionIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 2),
    _SonetSectionIntervalESs_Type()
)
sonetSectionIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionIntervalESs.setStatus("current")
_SonetSectionIntervalSESs_Type = Gauge32
_SonetSectionIntervalSESs_Object = MibTableColumn
sonetSectionIntervalSESs = _SonetSectionIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 3),
    _SonetSectionIntervalSESs_Type()
)
sonetSectionIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionIntervalSESs.setStatus("current")
_SonetSectionIntervalSEFSs_Type = Gauge32
_SonetSectionIntervalSEFSs_Object = MibTableColumn
sonetSectionIntervalSEFSs = _SonetSectionIntervalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 4),
    _SonetSectionIntervalSEFSs_Type()
)
sonetSectionIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionIntervalSEFSs.setStatus("current")
_SonetSectionIntervalCVs_Type = Gauge32
_SonetSectionIntervalCVs_Object = MibTableColumn
sonetSectionIntervalCVs = _SonetSectionIntervalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 5),
    _SonetSectionIntervalCVs_Type()
)
sonetSectionIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionIntervalCVs.setStatus("current")
_SonetLine_ObjectIdentity = ObjectIdentity
sonetLine = _SonetLine_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3)
)
_SonetLineCurrentTable_Object = MibTable
sonetLineCurrentTable = _SonetLineCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sonetLineCurrentTable.setStatus("current")
_SonetLineCurrentEntry_Object = MibTableRow
sonetLineCurrentEntry = _SonetLineCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1)
)
sonetLineCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetLineCurrentEntry.setStatus("current")


class _SonetLineCurrentStatus_Type(Integer32):
    """Custom type sonetLineCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonetLineCurrentStatus_Type.__name__ = "Integer32"
_SonetLineCurrentStatus_Object = MibTableColumn
sonetLineCurrentStatus = _SonetLineCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 1),
    _SonetLineCurrentStatus_Type()
)
sonetLineCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentStatus.setStatus("current")
_SonetLineCurrentESs_Type = Gauge32
_SonetLineCurrentESs_Object = MibTableColumn
sonetLineCurrentESs = _SonetLineCurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 2),
    _SonetLineCurrentESs_Type()
)
sonetLineCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentESs.setStatus("current")
_SonetLineCurrentSESs_Type = Gauge32
_SonetLineCurrentSESs_Object = MibTableColumn
sonetLineCurrentSESs = _SonetLineCurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 3),
    _SonetLineCurrentSESs_Type()
)
sonetLineCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentSESs.setStatus("current")
_SonetLineCurrentCVs_Type = Gauge32
_SonetLineCurrentCVs_Object = MibTableColumn
sonetLineCurrentCVs = _SonetLineCurrentCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 4),
    _SonetLineCurrentCVs_Type()
)
sonetLineCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentCVs.setStatus("current")
_SonetLineCurrentUASs_Type = Gauge32
_SonetLineCurrentUASs_Object = MibTableColumn
sonetLineCurrentUASs = _SonetLineCurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 5),
    _SonetLineCurrentUASs_Type()
)
sonetLineCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentUASs.setStatus("current")
_SonetLineIntervalTable_Object = MibTable
sonetLineIntervalTable = _SonetLineIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sonetLineIntervalTable.setStatus("current")
_SonetLineIntervalEntry_Object = MibTableRow
sonetLineIntervalEntry = _SonetLineIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1)
)
sonetLineIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetLineIntervalEntry.setStatus("current")


class _SonetLineIntervalNumber_Type(Integer32):
    """Custom type sonetLineIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SonetLineIntervalNumber_Type.__name__ = "Integer32"
_SonetLineIntervalNumber_Object = MibTableColumn
sonetLineIntervalNumber = _SonetLineIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 1),
    _SonetLineIntervalNumber_Type()
)
sonetLineIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetLineIntervalNumber.setStatus("current")
_SonetLineIntervalESs_Type = Gauge32
_SonetLineIntervalESs_Object = MibTableColumn
sonetLineIntervalESs = _SonetLineIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 2),
    _SonetLineIntervalESs_Type()
)
sonetLineIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineIntervalESs.setStatus("current")
_SonetLineIntervalSESs_Type = Gauge32
_SonetLineIntervalSESs_Object = MibTableColumn
sonetLineIntervalSESs = _SonetLineIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 3),
    _SonetLineIntervalSESs_Type()
)
sonetLineIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineIntervalSESs.setStatus("current")
_SonetLineIntervalCVs_Type = Gauge32
_SonetLineIntervalCVs_Object = MibTableColumn
sonetLineIntervalCVs = _SonetLineIntervalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 4),
    _SonetLineIntervalCVs_Type()
)
sonetLineIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineIntervalCVs.setStatus("current")
_SonetLineIntervalUASs_Type = Gauge32
_SonetLineIntervalUASs_Object = MibTableColumn
sonetLineIntervalUASs = _SonetLineIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 5),
    _SonetLineIntervalUASs_Type()
)
sonetLineIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineIntervalUASs.setStatus("current")
_SonetFarEndLine_ObjectIdentity = ObjectIdentity
sonetFarEndLine = _SonetFarEndLine_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4)
)
_SonetFarEndLineCurrentTable_Object = MibTable
sonetFarEndLineCurrentTable = _SonetFarEndLineCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentTable.setStatus("current")
_SonetFarEndLineCurrentEntry_Object = MibTableRow
sonetFarEndLineCurrentEntry = _SonetFarEndLineCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1)
)
sonetFarEndLineCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentEntry.setStatus("current")
_SonetFarEndLineCurrentESs_Type = Gauge32
_SonetFarEndLineCurrentESs_Object = MibTableColumn
sonetFarEndLineCurrentESs = _SonetFarEndLineCurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 1),
    _SonetFarEndLineCurrentESs_Type()
)
sonetFarEndLineCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentESs.setStatus("current")
_SonetFarEndLineCurrentSESs_Type = Gauge32
_SonetFarEndLineCurrentSESs_Object = MibTableColumn
sonetFarEndLineCurrentSESs = _SonetFarEndLineCurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 2),
    _SonetFarEndLineCurrentSESs_Type()
)
sonetFarEndLineCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentSESs.setStatus("current")
_SonetFarEndLineCurrentCVs_Type = Gauge32
_SonetFarEndLineCurrentCVs_Object = MibTableColumn
sonetFarEndLineCurrentCVs = _SonetFarEndLineCurrentCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 3),
    _SonetFarEndLineCurrentCVs_Type()
)
sonetFarEndLineCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentCVs.setStatus("current")
_SonetFarEndLineCurrentUASs_Type = Gauge32
_SonetFarEndLineCurrentUASs_Object = MibTableColumn
sonetFarEndLineCurrentUASs = _SonetFarEndLineCurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 4),
    _SonetFarEndLineCurrentUASs_Type()
)
sonetFarEndLineCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentUASs.setStatus("current")
_SonetFarEndLineIntervalTable_Object = MibTable
sonetFarEndLineIntervalTable = _SonetFarEndLineIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sonetFarEndLineIntervalTable.setStatus("current")
_SonetFarEndLineIntervalEntry_Object = MibTableRow
sonetFarEndLineIntervalEntry = _SonetFarEndLineIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1)
)
sonetFarEndLineIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetFarEndLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetFarEndLineIntervalEntry.setStatus("current")


class _SonetFarEndLineIntervalNumber_Type(Integer32):
    """Custom type sonetFarEndLineIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SonetFarEndLineIntervalNumber_Type.__name__ = "Integer32"
_SonetFarEndLineIntervalNumber_Object = MibTableColumn
sonetFarEndLineIntervalNumber = _SonetFarEndLineIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 1),
    _SonetFarEndLineIntervalNumber_Type()
)
sonetFarEndLineIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetFarEndLineIntervalNumber.setStatus("current")
_SonetFarEndLineIntervalESs_Type = Gauge32
_SonetFarEndLineIntervalESs_Object = MibTableColumn
sonetFarEndLineIntervalESs = _SonetFarEndLineIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 2),
    _SonetFarEndLineIntervalESs_Type()
)
sonetFarEndLineIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineIntervalESs.setStatus("current")
_SonetFarEndLineIntervalSESs_Type = Gauge32
_SonetFarEndLineIntervalSESs_Object = MibTableColumn
sonetFarEndLineIntervalSESs = _SonetFarEndLineIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 3),
    _SonetFarEndLineIntervalSESs_Type()
)
sonetFarEndLineIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineIntervalSESs.setStatus("current")
_SonetFarEndLineIntervalCVs_Type = Gauge32
_SonetFarEndLineIntervalCVs_Object = MibTableColumn
sonetFarEndLineIntervalCVs = _SonetFarEndLineIntervalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 4),
    _SonetFarEndLineIntervalCVs_Type()
)
sonetFarEndLineIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineIntervalCVs.setStatus("current")
_SonetFarEndLineIntervalUASs_Type = Gauge32
_SonetFarEndLineIntervalUASs_Object = MibTableColumn
sonetFarEndLineIntervalUASs = _SonetFarEndLineIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 5),
    _SonetFarEndLineIntervalUASs_Type()
)
sonetFarEndLineIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineIntervalUASs.setStatus("current")
_SonetObjectsPath_ObjectIdentity = ObjectIdentity
sonetObjectsPath = _SonetObjectsPath_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 2)
)
_SonetPath_ObjectIdentity = ObjectIdentity
sonetPath = _SonetPath_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1)
)
_SonetPathCurrentTable_Object = MibTable
sonetPathCurrentTable = _SonetPathCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sonetPathCurrentTable.setStatus("current")
_SonetPathCurrentEntry_Object = MibTableRow
sonetPathCurrentEntry = _SonetPathCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1)
)
sonetPathCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetPathCurrentEntry.setStatus("current")


class _SonetPathCurrentWidth_Type(Integer32):
    """Custom type sonetPathCurrentWidth based on Integer32"""
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
        *(("sts1", 1),
          ("sts12cSTM4", 3),
          ("sts24c", 4),
          ("sts3cSTM1", 2),
          ("sts48cSTM16", 5))
    )


_SonetPathCurrentWidth_Type.__name__ = "Integer32"
_SonetPathCurrentWidth_Object = MibTableColumn
sonetPathCurrentWidth = _SonetPathCurrentWidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 1),
    _SonetPathCurrentWidth_Type()
)
sonetPathCurrentWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrentWidth.setStatus("current")


class _SonetPathCurrentStatus_Type(Integer32):
    """Custom type sonetPathCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_SonetPathCurrentStatus_Type.__name__ = "Integer32"
_SonetPathCurrentStatus_Object = MibTableColumn
sonetPathCurrentStatus = _SonetPathCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 2),
    _SonetPathCurrentStatus_Type()
)
sonetPathCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentStatus.setStatus("current")
_SonetPathCurrentESs_Type = Gauge32
_SonetPathCurrentESs_Object = MibTableColumn
sonetPathCurrentESs = _SonetPathCurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 3),
    _SonetPathCurrentESs_Type()
)
sonetPathCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentESs.setStatus("current")
_SonetPathCurrentSESs_Type = Gauge32
_SonetPathCurrentSESs_Object = MibTableColumn
sonetPathCurrentSESs = _SonetPathCurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 4),
    _SonetPathCurrentSESs_Type()
)
sonetPathCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentSESs.setStatus("current")
_SonetPathCurrentCVs_Type = Gauge32
_SonetPathCurrentCVs_Object = MibTableColumn
sonetPathCurrentCVs = _SonetPathCurrentCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 5),
    _SonetPathCurrentCVs_Type()
)
sonetPathCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentCVs.setStatus("current")
_SonetPathCurrentUASs_Type = Gauge32
_SonetPathCurrentUASs_Object = MibTableColumn
sonetPathCurrentUASs = _SonetPathCurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 6),
    _SonetPathCurrentUASs_Type()
)
sonetPathCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentUASs.setStatus("current")
_SonetPathIntervalTable_Object = MibTable
sonetPathIntervalTable = _SonetPathIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sonetPathIntervalTable.setStatus("current")
_SonetPathIntervalEntry_Object = MibTableRow
sonetPathIntervalEntry = _SonetPathIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1)
)
sonetPathIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetPathIntervalEntry.setStatus("current")


class _SonetPathIntervalNumber_Type(Integer32):
    """Custom type sonetPathIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SonetPathIntervalNumber_Type.__name__ = "Integer32"
_SonetPathIntervalNumber_Object = MibTableColumn
sonetPathIntervalNumber = _SonetPathIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 1),
    _SonetPathIntervalNumber_Type()
)
sonetPathIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetPathIntervalNumber.setStatus("current")
_SonetPathIntervalESs_Type = Gauge32
_SonetPathIntervalESs_Object = MibTableColumn
sonetPathIntervalESs = _SonetPathIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 2),
    _SonetPathIntervalESs_Type()
)
sonetPathIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathIntervalESs.setStatus("current")
_SonetPathIntervalSESs_Type = Gauge32
_SonetPathIntervalSESs_Object = MibTableColumn
sonetPathIntervalSESs = _SonetPathIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 3),
    _SonetPathIntervalSESs_Type()
)
sonetPathIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathIntervalSESs.setStatus("current")
_SonetPathIntervalCVs_Type = Gauge32
_SonetPathIntervalCVs_Object = MibTableColumn
sonetPathIntervalCVs = _SonetPathIntervalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 4),
    _SonetPathIntervalCVs_Type()
)
sonetPathIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathIntervalCVs.setStatus("current")
_SonetPathIntervalUASs_Type = Gauge32
_SonetPathIntervalUASs_Object = MibTableColumn
sonetPathIntervalUASs = _SonetPathIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 5),
    _SonetPathIntervalUASs_Type()
)
sonetPathIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathIntervalUASs.setStatus("current")
_SonetFarEndPath_ObjectIdentity = ObjectIdentity
sonetFarEndPath = _SonetFarEndPath_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2)
)
_SonetFarEndPathCurrentTable_Object = MibTable
sonetFarEndPathCurrentTable = _SonetFarEndPathCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentTable.setStatus("current")
_SonetFarEndPathCurrentEntry_Object = MibTableRow
sonetFarEndPathCurrentEntry = _SonetFarEndPathCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1)
)
sonetFarEndPathCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentEntry.setStatus("current")
_SonetFarEndPathCurrentESs_Type = Gauge32
_SonetFarEndPathCurrentESs_Object = MibTableColumn
sonetFarEndPathCurrentESs = _SonetFarEndPathCurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 1),
    _SonetFarEndPathCurrentESs_Type()
)
sonetFarEndPathCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentESs.setStatus("current")
_SonetFarEndPathCurrentSESs_Type = Gauge32
_SonetFarEndPathCurrentSESs_Object = MibTableColumn
sonetFarEndPathCurrentSESs = _SonetFarEndPathCurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 2),
    _SonetFarEndPathCurrentSESs_Type()
)
sonetFarEndPathCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentSESs.setStatus("current")
_SonetFarEndPathCurrentCVs_Type = Gauge32
_SonetFarEndPathCurrentCVs_Object = MibTableColumn
sonetFarEndPathCurrentCVs = _SonetFarEndPathCurrentCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 3),
    _SonetFarEndPathCurrentCVs_Type()
)
sonetFarEndPathCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentCVs.setStatus("current")
_SonetFarEndPathCurrentUASs_Type = Gauge32
_SonetFarEndPathCurrentUASs_Object = MibTableColumn
sonetFarEndPathCurrentUASs = _SonetFarEndPathCurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 4),
    _SonetFarEndPathCurrentUASs_Type()
)
sonetFarEndPathCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentUASs.setStatus("current")
_SonetFarEndPathIntervalTable_Object = MibTable
sonetFarEndPathIntervalTable = _SonetFarEndPathIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sonetFarEndPathIntervalTable.setStatus("current")
_SonetFarEndPathIntervalEntry_Object = MibTableRow
sonetFarEndPathIntervalEntry = _SonetFarEndPathIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1)
)
sonetFarEndPathIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetFarEndPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetFarEndPathIntervalEntry.setStatus("current")


class _SonetFarEndPathIntervalNumber_Type(Integer32):
    """Custom type sonetFarEndPathIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SonetFarEndPathIntervalNumber_Type.__name__ = "Integer32"
_SonetFarEndPathIntervalNumber_Object = MibTableColumn
sonetFarEndPathIntervalNumber = _SonetFarEndPathIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 1),
    _SonetFarEndPathIntervalNumber_Type()
)
sonetFarEndPathIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetFarEndPathIntervalNumber.setStatus("current")
_SonetFarEndPathIntervalESs_Type = Gauge32
_SonetFarEndPathIntervalESs_Object = MibTableColumn
sonetFarEndPathIntervalESs = _SonetFarEndPathIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 2),
    _SonetFarEndPathIntervalESs_Type()
)
sonetFarEndPathIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathIntervalESs.setStatus("current")
_SonetFarEndPathIntervalSESs_Type = Gauge32
_SonetFarEndPathIntervalSESs_Object = MibTableColumn
sonetFarEndPathIntervalSESs = _SonetFarEndPathIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 3),
    _SonetFarEndPathIntervalSESs_Type()
)
sonetFarEndPathIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathIntervalSESs.setStatus("current")
_SonetFarEndPathIntervalCVs_Type = Gauge32
_SonetFarEndPathIntervalCVs_Object = MibTableColumn
sonetFarEndPathIntervalCVs = _SonetFarEndPathIntervalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 4),
    _SonetFarEndPathIntervalCVs_Type()
)
sonetFarEndPathIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathIntervalCVs.setStatus("current")
_SonetFarEndPathIntervalUASs_Type = Gauge32
_SonetFarEndPathIntervalUASs_Object = MibTableColumn
sonetFarEndPathIntervalUASs = _SonetFarEndPathIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 5),
    _SonetFarEndPathIntervalUASs_Type()
)
sonetFarEndPathIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathIntervalUASs.setStatus("current")
_SonetObjectsVT_ObjectIdentity = ObjectIdentity
sonetObjectsVT = _SonetObjectsVT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 3)
)
_SonetVT_ObjectIdentity = ObjectIdentity
sonetVT = _SonetVT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1)
)
_SonetVTCurrentTable_Object = MibTable
sonetVTCurrentTable = _SonetVTCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sonetVTCurrentTable.setStatus("current")
_SonetVTCurrentEntry_Object = MibTableRow
sonetVTCurrentEntry = _SonetVTCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1)
)
sonetVTCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetVTCurrentEntry.setStatus("current")


class _SonetVTCurrentWidth_Type(Integer32):
    """Custom type sonetVTCurrentWidth based on Integer32"""
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
        *(("vtWidth15VC11", 1),
          ("vtWidth2VC12", 2),
          ("vtWidth3", 3),
          ("vtWidth6VC2", 4),
          ("vtWidth6c", 5))
    )


_SonetVTCurrentWidth_Type.__name__ = "Integer32"
_SonetVTCurrentWidth_Object = MibTableColumn
sonetVTCurrentWidth = _SonetVTCurrentWidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 1),
    _SonetVTCurrentWidth_Type()
)
sonetVTCurrentWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTCurrentWidth.setStatus("current")


class _SonetVTCurrentStatus_Type(Integer32):
    """Custom type sonetVTCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SonetVTCurrentStatus_Type.__name__ = "Integer32"
_SonetVTCurrentStatus_Object = MibTableColumn
sonetVTCurrentStatus = _SonetVTCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 2),
    _SonetVTCurrentStatus_Type()
)
sonetVTCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTCurrentStatus.setStatus("current")
_SonetVTCurrentESs_Type = Gauge32
_SonetVTCurrentESs_Object = MibTableColumn
sonetVTCurrentESs = _SonetVTCurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 3),
    _SonetVTCurrentESs_Type()
)
sonetVTCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTCurrentESs.setStatus("current")
_SonetVTCurrentSESs_Type = Gauge32
_SonetVTCurrentSESs_Object = MibTableColumn
sonetVTCurrentSESs = _SonetVTCurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 4),
    _SonetVTCurrentSESs_Type()
)
sonetVTCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTCurrentSESs.setStatus("current")
_SonetVTCurrentCVs_Type = Gauge32
_SonetVTCurrentCVs_Object = MibTableColumn
sonetVTCurrentCVs = _SonetVTCurrentCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 5),
    _SonetVTCurrentCVs_Type()
)
sonetVTCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTCurrentCVs.setStatus("current")
_SonetVTCurrentUASs_Type = Gauge32
_SonetVTCurrentUASs_Object = MibTableColumn
sonetVTCurrentUASs = _SonetVTCurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 6),
    _SonetVTCurrentUASs_Type()
)
sonetVTCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTCurrentUASs.setStatus("current")
_SonetVTIntervalTable_Object = MibTable
sonetVTIntervalTable = _SonetVTIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sonetVTIntervalTable.setStatus("current")
_SonetVTIntervalEntry_Object = MibTableRow
sonetVTIntervalEntry = _SonetVTIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1)
)
sonetVTIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetVTIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetVTIntervalEntry.setStatus("current")


class _SonetVTIntervalNumber_Type(Integer32):
    """Custom type sonetVTIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SonetVTIntervalNumber_Type.__name__ = "Integer32"
_SonetVTIntervalNumber_Object = MibTableColumn
sonetVTIntervalNumber = _SonetVTIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 1),
    _SonetVTIntervalNumber_Type()
)
sonetVTIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetVTIntervalNumber.setStatus("current")
_SonetVTIntervalESs_Type = Gauge32
_SonetVTIntervalESs_Object = MibTableColumn
sonetVTIntervalESs = _SonetVTIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 2),
    _SonetVTIntervalESs_Type()
)
sonetVTIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTIntervalESs.setStatus("current")
_SonetVTIntervalSESs_Type = Gauge32
_SonetVTIntervalSESs_Object = MibTableColumn
sonetVTIntervalSESs = _SonetVTIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 3),
    _SonetVTIntervalSESs_Type()
)
sonetVTIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTIntervalSESs.setStatus("current")
_SonetVTIntervalCVs_Type = Gauge32
_SonetVTIntervalCVs_Object = MibTableColumn
sonetVTIntervalCVs = _SonetVTIntervalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 4),
    _SonetVTIntervalCVs_Type()
)
sonetVTIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTIntervalCVs.setStatus("current")
_SonetVTIntervalUASs_Type = Gauge32
_SonetVTIntervalUASs_Object = MibTableColumn
sonetVTIntervalUASs = _SonetVTIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 5),
    _SonetVTIntervalUASs_Type()
)
sonetVTIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTIntervalUASs.setStatus("current")
_SonetFarEndVT_ObjectIdentity = ObjectIdentity
sonetFarEndVT = _SonetFarEndVT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2)
)
_SonetFarEndVTCurrentTable_Object = MibTable
sonetFarEndVTCurrentTable = _SonetFarEndVTCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sonetFarEndVTCurrentTable.setStatus("current")
_SonetFarEndVTCurrentEntry_Object = MibTableRow
sonetFarEndVTCurrentEntry = _SonetFarEndVTCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1)
)
sonetFarEndVTCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetFarEndVTCurrentEntry.setStatus("current")
_SonetFarEndVTCurrentESs_Type = Gauge32
_SonetFarEndVTCurrentESs_Object = MibTableColumn
sonetFarEndVTCurrentESs = _SonetFarEndVTCurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 1),
    _SonetFarEndVTCurrentESs_Type()
)
sonetFarEndVTCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTCurrentESs.setStatus("current")
_SonetFarEndVTCurrentSESs_Type = Gauge32
_SonetFarEndVTCurrentSESs_Object = MibTableColumn
sonetFarEndVTCurrentSESs = _SonetFarEndVTCurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 2),
    _SonetFarEndVTCurrentSESs_Type()
)
sonetFarEndVTCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTCurrentSESs.setStatus("current")
_SonetFarEndVTCurrentCVs_Type = Gauge32
_SonetFarEndVTCurrentCVs_Object = MibTableColumn
sonetFarEndVTCurrentCVs = _SonetFarEndVTCurrentCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 3),
    _SonetFarEndVTCurrentCVs_Type()
)
sonetFarEndVTCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTCurrentCVs.setStatus("current")
_SonetFarEndVTCurrentUASs_Type = Gauge32
_SonetFarEndVTCurrentUASs_Object = MibTableColumn
sonetFarEndVTCurrentUASs = _SonetFarEndVTCurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 4),
    _SonetFarEndVTCurrentUASs_Type()
)
sonetFarEndVTCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTCurrentUASs.setStatus("current")
_SonetFarEndVTIntervalTable_Object = MibTable
sonetFarEndVTIntervalTable = _SonetFarEndVTIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sonetFarEndVTIntervalTable.setStatus("current")
_SonetFarEndVTIntervalEntry_Object = MibTableRow
sonetFarEndVTIntervalEntry = _SonetFarEndVTIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1)
)
sonetFarEndVTIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetFarEndVTIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetFarEndVTIntervalEntry.setStatus("current")


class _SonetFarEndVTIntervalNumber_Type(Integer32):
    """Custom type sonetFarEndVTIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SonetFarEndVTIntervalNumber_Type.__name__ = "Integer32"
_SonetFarEndVTIntervalNumber_Object = MibTableColumn
sonetFarEndVTIntervalNumber = _SonetFarEndVTIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 1),
    _SonetFarEndVTIntervalNumber_Type()
)
sonetFarEndVTIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetFarEndVTIntervalNumber.setStatus("current")
_SonetFarEndVTIntervalESs_Type = Gauge32
_SonetFarEndVTIntervalESs_Object = MibTableColumn
sonetFarEndVTIntervalESs = _SonetFarEndVTIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 2),
    _SonetFarEndVTIntervalESs_Type()
)
sonetFarEndVTIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTIntervalESs.setStatus("current")
_SonetFarEndVTIntervalSESs_Type = Gauge32
_SonetFarEndVTIntervalSESs_Object = MibTableColumn
sonetFarEndVTIntervalSESs = _SonetFarEndVTIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 3),
    _SonetFarEndVTIntervalSESs_Type()
)
sonetFarEndVTIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTIntervalSESs.setStatus("current")
_SonetFarEndVTIntervalCVs_Type = Gauge32
_SonetFarEndVTIntervalCVs_Object = MibTableColumn
sonetFarEndVTIntervalCVs = _SonetFarEndVTIntervalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 4),
    _SonetFarEndVTIntervalCVs_Type()
)
sonetFarEndVTIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTIntervalCVs.setStatus("current")
_SonetFarEndVTIntervalUASs_Type = Gauge32
_SonetFarEndVTIntervalUASs_Object = MibTableColumn
sonetFarEndVTIntervalUASs = _SonetFarEndVTIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 5),
    _SonetFarEndVTIntervalUASs_Type()
)
sonetFarEndVTIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTIntervalUASs.setStatus("current")
_SonetConformance_ObjectIdentity = ObjectIdentity
sonetConformance = _SonetConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 4)
)
_SonetGroups_ObjectIdentity = ObjectIdentity
sonetGroups = _SonetGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 1)
)
_SonetCompliances_ObjectIdentity = ObjectIdentity
sonetCompliances = _SonetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 2)
)

# Managed Objects groups

sonetMediumStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 1)
)
sonetMediumStuff.setObjects(
      *(("SONET-MIB", "sonetMediumType"),
        ("SONET-MIB", "sonetMediumTimeElapsed"),
        ("SONET-MIB", "sonetMediumValidIntervals"),
        ("SONET-MIB", "sonetMediumLineCoding"),
        ("SONET-MIB", "sonetMediumLineType"),
        ("SONET-MIB", "sonetMediumCircuitIdentifier"))
)
if mibBuilder.loadTexts:
    sonetMediumStuff.setStatus("current")

sonetSectionStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 2)
)
sonetSectionStuff.setObjects(
      *(("SONET-MIB", "sonetSectionCurrentStatus"),
        ("SONET-MIB", "sonetSectionCurrentESs"),
        ("SONET-MIB", "sonetSectionCurrentSESs"),
        ("SONET-MIB", "sonetSectionCurrentSEFSs"),
        ("SONET-MIB", "sonetSectionCurrentCVs"),
        ("SONET-MIB", "sonetSectionIntervalESs"),
        ("SONET-MIB", "sonetSectionIntervalSESs"),
        ("SONET-MIB", "sonetSectionIntervalSEFSs"),
        ("SONET-MIB", "sonetSectionIntervalCVs"))
)
if mibBuilder.loadTexts:
    sonetSectionStuff.setStatus("current")

sonetLineStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 3)
)
sonetLineStuff.setObjects(
      *(("SONET-MIB", "sonetLineCurrentStatus"),
        ("SONET-MIB", "sonetLineCurrentESs"),
        ("SONET-MIB", "sonetLineCurrentSESs"),
        ("SONET-MIB", "sonetLineCurrentCVs"),
        ("SONET-MIB", "sonetLineCurrentUASs"),
        ("SONET-MIB", "sonetLineIntervalESs"),
        ("SONET-MIB", "sonetLineIntervalSESs"),
        ("SONET-MIB", "sonetLineIntervalCVs"),
        ("SONET-MIB", "sonetLineIntervalUASs"))
)
if mibBuilder.loadTexts:
    sonetLineStuff.setStatus("current")

sonetFarEndLineStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 4)
)
sonetFarEndLineStuff.setObjects(
      *(("SONET-MIB", "sonetFarEndLineCurrentESs"),
        ("SONET-MIB", "sonetFarEndLineCurrentSESs"),
        ("SONET-MIB", "sonetFarEndLineCurrentCVs"),
        ("SONET-MIB", "sonetFarEndLineCurrentUASs"),
        ("SONET-MIB", "sonetFarEndLineIntervalESs"),
        ("SONET-MIB", "sonetFarEndLineIntervalSESs"),
        ("SONET-MIB", "sonetFarEndLineIntervalCVs"),
        ("SONET-MIB", "sonetFarEndLineIntervalUASs"))
)
if mibBuilder.loadTexts:
    sonetFarEndLineStuff.setStatus("current")

sonetPathStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 5)
)
sonetPathStuff.setObjects(
      *(("SONET-MIB", "sonetPathCurrentWidth"),
        ("SONET-MIB", "sonetPathCurrentStatus"),
        ("SONET-MIB", "sonetPathCurrentESs"),
        ("SONET-MIB", "sonetPathCurrentSESs"),
        ("SONET-MIB", "sonetPathCurrentCVs"),
        ("SONET-MIB", "sonetPathCurrentUASs"),
        ("SONET-MIB", "sonetPathIntervalESs"),
        ("SONET-MIB", "sonetPathIntervalSESs"),
        ("SONET-MIB", "sonetPathIntervalCVs"),
        ("SONET-MIB", "sonetPathIntervalUASs"))
)
if mibBuilder.loadTexts:
    sonetPathStuff.setStatus("current")

sonetFarEndPathStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 6)
)
sonetFarEndPathStuff.setObjects(
      *(("SONET-MIB", "sonetFarEndPathCurrentESs"),
        ("SONET-MIB", "sonetFarEndPathCurrentSESs"),
        ("SONET-MIB", "sonetFarEndPathCurrentCVs"),
        ("SONET-MIB", "sonetFarEndPathCurrentUASs"),
        ("SONET-MIB", "sonetFarEndPathIntervalESs"),
        ("SONET-MIB", "sonetFarEndPathIntervalSESs"),
        ("SONET-MIB", "sonetFarEndPathIntervalCVs"),
        ("SONET-MIB", "sonetFarEndPathIntervalUASs"))
)
if mibBuilder.loadTexts:
    sonetFarEndPathStuff.setStatus("current")

sonetVTStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 7)
)
sonetVTStuff.setObjects(
      *(("SONET-MIB", "sonetVTCurrentWidth"),
        ("SONET-MIB", "sonetVTCurrentStatus"),
        ("SONET-MIB", "sonetVTCurrentESs"),
        ("SONET-MIB", "sonetVTCurrentSESs"),
        ("SONET-MIB", "sonetVTCurrentCVs"),
        ("SONET-MIB", "sonetVTCurrentUASs"),
        ("SONET-MIB", "sonetVTIntervalESs"),
        ("SONET-MIB", "sonetVTIntervalSESs"),
        ("SONET-MIB", "sonetVTIntervalCVs"),
        ("SONET-MIB", "sonetVTIntervalUASs"))
)
if mibBuilder.loadTexts:
    sonetVTStuff.setStatus("current")

sonetFarEndVTStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 8)
)
sonetFarEndVTStuff.setObjects(
      *(("SONET-MIB", "sonetFarEndVTCurrentESs"),
        ("SONET-MIB", "sonetFarEndVTCurrentSESs"),
        ("SONET-MIB", "sonetFarEndVTCurrentCVs"),
        ("SONET-MIB", "sonetFarEndVTCurrentUASs"),
        ("SONET-MIB", "sonetFarEndVTIntervalESs"),
        ("SONET-MIB", "sonetFarEndVTIntervalSESs"),
        ("SONET-MIB", "sonetFarEndVTIntervalCVs"),
        ("SONET-MIB", "sonetFarEndVTIntervalUASs"))
)
if mibBuilder.loadTexts:
    sonetFarEndVTStuff.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sonetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 39, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sonetCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONET-MIB",
    **{"sonetMIB": sonetMIB,
       "sonetObjects": sonetObjects,
       "sonetMedium": sonetMedium,
       "sonetMediumTable": sonetMediumTable,
       "sonetMediumEntry": sonetMediumEntry,
       "sonetMediumType": sonetMediumType,
       "sonetMediumTimeElapsed": sonetMediumTimeElapsed,
       "sonetMediumValidIntervals": sonetMediumValidIntervals,
       "sonetMediumLineCoding": sonetMediumLineCoding,
       "sonetMediumLineType": sonetMediumLineType,
       "sonetMediumCircuitIdentifier": sonetMediumCircuitIdentifier,
       "sonetSection": sonetSection,
       "sonetSectionCurrentTable": sonetSectionCurrentTable,
       "sonetSectionCurrentEntry": sonetSectionCurrentEntry,
       "sonetSectionCurrentStatus": sonetSectionCurrentStatus,
       "sonetSectionCurrentESs": sonetSectionCurrentESs,
       "sonetSectionCurrentSESs": sonetSectionCurrentSESs,
       "sonetSectionCurrentSEFSs": sonetSectionCurrentSEFSs,
       "sonetSectionCurrentCVs": sonetSectionCurrentCVs,
       "sonetSectionIntervalTable": sonetSectionIntervalTable,
       "sonetSectionIntervalEntry": sonetSectionIntervalEntry,
       "sonetSectionIntervalNumber": sonetSectionIntervalNumber,
       "sonetSectionIntervalESs": sonetSectionIntervalESs,
       "sonetSectionIntervalSESs": sonetSectionIntervalSESs,
       "sonetSectionIntervalSEFSs": sonetSectionIntervalSEFSs,
       "sonetSectionIntervalCVs": sonetSectionIntervalCVs,
       "sonetLine": sonetLine,
       "sonetLineCurrentTable": sonetLineCurrentTable,
       "sonetLineCurrentEntry": sonetLineCurrentEntry,
       "sonetLineCurrentStatus": sonetLineCurrentStatus,
       "sonetLineCurrentESs": sonetLineCurrentESs,
       "sonetLineCurrentSESs": sonetLineCurrentSESs,
       "sonetLineCurrentCVs": sonetLineCurrentCVs,
       "sonetLineCurrentUASs": sonetLineCurrentUASs,
       "sonetLineIntervalTable": sonetLineIntervalTable,
       "sonetLineIntervalEntry": sonetLineIntervalEntry,
       "sonetLineIntervalNumber": sonetLineIntervalNumber,
       "sonetLineIntervalESs": sonetLineIntervalESs,
       "sonetLineIntervalSESs": sonetLineIntervalSESs,
       "sonetLineIntervalCVs": sonetLineIntervalCVs,
       "sonetLineIntervalUASs": sonetLineIntervalUASs,
       "sonetFarEndLine": sonetFarEndLine,
       "sonetFarEndLineCurrentTable": sonetFarEndLineCurrentTable,
       "sonetFarEndLineCurrentEntry": sonetFarEndLineCurrentEntry,
       "sonetFarEndLineCurrentESs": sonetFarEndLineCurrentESs,
       "sonetFarEndLineCurrentSESs": sonetFarEndLineCurrentSESs,
       "sonetFarEndLineCurrentCVs": sonetFarEndLineCurrentCVs,
       "sonetFarEndLineCurrentUASs": sonetFarEndLineCurrentUASs,
       "sonetFarEndLineIntervalTable": sonetFarEndLineIntervalTable,
       "sonetFarEndLineIntervalEntry": sonetFarEndLineIntervalEntry,
       "sonetFarEndLineIntervalNumber": sonetFarEndLineIntervalNumber,
       "sonetFarEndLineIntervalESs": sonetFarEndLineIntervalESs,
       "sonetFarEndLineIntervalSESs": sonetFarEndLineIntervalSESs,
       "sonetFarEndLineIntervalCVs": sonetFarEndLineIntervalCVs,
       "sonetFarEndLineIntervalUASs": sonetFarEndLineIntervalUASs,
       "sonetObjectsPath": sonetObjectsPath,
       "sonetPath": sonetPath,
       "sonetPathCurrentTable": sonetPathCurrentTable,
       "sonetPathCurrentEntry": sonetPathCurrentEntry,
       "sonetPathCurrentWidth": sonetPathCurrentWidth,
       "sonetPathCurrentStatus": sonetPathCurrentStatus,
       "sonetPathCurrentESs": sonetPathCurrentESs,
       "sonetPathCurrentSESs": sonetPathCurrentSESs,
       "sonetPathCurrentCVs": sonetPathCurrentCVs,
       "sonetPathCurrentUASs": sonetPathCurrentUASs,
       "sonetPathIntervalTable": sonetPathIntervalTable,
       "sonetPathIntervalEntry": sonetPathIntervalEntry,
       "sonetPathIntervalNumber": sonetPathIntervalNumber,
       "sonetPathIntervalESs": sonetPathIntervalESs,
       "sonetPathIntervalSESs": sonetPathIntervalSESs,
       "sonetPathIntervalCVs": sonetPathIntervalCVs,
       "sonetPathIntervalUASs": sonetPathIntervalUASs,
       "sonetFarEndPath": sonetFarEndPath,
       "sonetFarEndPathCurrentTable": sonetFarEndPathCurrentTable,
       "sonetFarEndPathCurrentEntry": sonetFarEndPathCurrentEntry,
       "sonetFarEndPathCurrentESs": sonetFarEndPathCurrentESs,
       "sonetFarEndPathCurrentSESs": sonetFarEndPathCurrentSESs,
       "sonetFarEndPathCurrentCVs": sonetFarEndPathCurrentCVs,
       "sonetFarEndPathCurrentUASs": sonetFarEndPathCurrentUASs,
       "sonetFarEndPathIntervalTable": sonetFarEndPathIntervalTable,
       "sonetFarEndPathIntervalEntry": sonetFarEndPathIntervalEntry,
       "sonetFarEndPathIntervalNumber": sonetFarEndPathIntervalNumber,
       "sonetFarEndPathIntervalESs": sonetFarEndPathIntervalESs,
       "sonetFarEndPathIntervalSESs": sonetFarEndPathIntervalSESs,
       "sonetFarEndPathIntervalCVs": sonetFarEndPathIntervalCVs,
       "sonetFarEndPathIntervalUASs": sonetFarEndPathIntervalUASs,
       "sonetObjectsVT": sonetObjectsVT,
       "sonetVT": sonetVT,
       "sonetVTCurrentTable": sonetVTCurrentTable,
       "sonetVTCurrentEntry": sonetVTCurrentEntry,
       "sonetVTCurrentWidth": sonetVTCurrentWidth,
       "sonetVTCurrentStatus": sonetVTCurrentStatus,
       "sonetVTCurrentESs": sonetVTCurrentESs,
       "sonetVTCurrentSESs": sonetVTCurrentSESs,
       "sonetVTCurrentCVs": sonetVTCurrentCVs,
       "sonetVTCurrentUASs": sonetVTCurrentUASs,
       "sonetVTIntervalTable": sonetVTIntervalTable,
       "sonetVTIntervalEntry": sonetVTIntervalEntry,
       "sonetVTIntervalNumber": sonetVTIntervalNumber,
       "sonetVTIntervalESs": sonetVTIntervalESs,
       "sonetVTIntervalSESs": sonetVTIntervalSESs,
       "sonetVTIntervalCVs": sonetVTIntervalCVs,
       "sonetVTIntervalUASs": sonetVTIntervalUASs,
       "sonetFarEndVT": sonetFarEndVT,
       "sonetFarEndVTCurrentTable": sonetFarEndVTCurrentTable,
       "sonetFarEndVTCurrentEntry": sonetFarEndVTCurrentEntry,
       "sonetFarEndVTCurrentESs": sonetFarEndVTCurrentESs,
       "sonetFarEndVTCurrentSESs": sonetFarEndVTCurrentSESs,
       "sonetFarEndVTCurrentCVs": sonetFarEndVTCurrentCVs,
       "sonetFarEndVTCurrentUASs": sonetFarEndVTCurrentUASs,
       "sonetFarEndVTIntervalTable": sonetFarEndVTIntervalTable,
       "sonetFarEndVTIntervalEntry": sonetFarEndVTIntervalEntry,
       "sonetFarEndVTIntervalNumber": sonetFarEndVTIntervalNumber,
       "sonetFarEndVTIntervalESs": sonetFarEndVTIntervalESs,
       "sonetFarEndVTIntervalSESs": sonetFarEndVTIntervalSESs,
       "sonetFarEndVTIntervalCVs": sonetFarEndVTIntervalCVs,
       "sonetFarEndVTIntervalUASs": sonetFarEndVTIntervalUASs,
       "sonetConformance": sonetConformance,
       "sonetGroups": sonetGroups,
       "sonetMediumStuff": sonetMediumStuff,
       "sonetSectionStuff": sonetSectionStuff,
       "sonetLineStuff": sonetLineStuff,
       "sonetFarEndLineStuff": sonetFarEndLineStuff,
       "sonetPathStuff": sonetPathStuff,
       "sonetFarEndPathStuff": sonetFarEndPathStuff,
       "sonetVTStuff": sonetVTStuff,
       "sonetFarEndVTStuff": sonetFarEndVTStuff,
       "sonetCompliances": sonetCompliances,
       "sonetCompliance": sonetCompliance}
)
