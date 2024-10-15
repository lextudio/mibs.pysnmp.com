# SNMP MIB module (LLDP-EXT-PNO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-EXT-PNO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:10 2024
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

(lldpExtensions,
 lldpLocPortNum,
 lldpPortConfigEntry,
 lldpRemIndex,
 lldpRemLocalPortNum,
 lldpRemTimeMark) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpExtensions",
    "lldpLocPortNum",
    "lldpPortConfigEntry",
    "lldpRemIndex",
    "lldpRemLocalPortNum",
    "lldpRemTimeMark")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lldpXPnoMIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791)
)
lldpXPnoMIB.setRevisions(
        ("2006-03-09 00:00",
         "2006-02-28 00:00",
         "2005-08-31 00:00",
         "2005-05-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpXPnoObjects_ObjectIdentity = ObjectIdentity
lldpXPnoObjects = _LldpXPnoObjects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1)
)
_LldpXPnoConfig_ObjectIdentity = ObjectIdentity
lldpXPnoConfig = _LldpXPnoConfig_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1)
)
_LldpXPnoConfigTable_Object = MibTable
lldpXPnoConfigTable = _LldpXPnoConfigTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXPnoConfigTable.setStatus("current")
_LldpXPnoConfigEntry_Object = MibTableRow
lldpXPnoConfigEntry = _LldpXPnoConfigEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXPnoConfigEntry.setStatus("current")


class _LldpXPnoConfigSPDTxEnable_Type(TruthValue):
    """Custom type lldpXPnoConfigSPDTxEnable based on TruthValue"""


_LldpXPnoConfigSPDTxEnable_Object = MibTableColumn
lldpXPnoConfigSPDTxEnable = _LldpXPnoConfigSPDTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1, 1, 1),
    _LldpXPnoConfigSPDTxEnable_Type()
)
lldpXPnoConfigSPDTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXPnoConfigSPDTxEnable.setStatus("current")


class _LldpXPnoConfigPortStatusTxEnable_Type(TruthValue):
    """Custom type lldpXPnoConfigPortStatusTxEnable based on TruthValue"""


_LldpXPnoConfigPortStatusTxEnable_Object = MibTableColumn
lldpXPnoConfigPortStatusTxEnable = _LldpXPnoConfigPortStatusTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1, 1, 2),
    _LldpXPnoConfigPortStatusTxEnable_Type()
)
lldpXPnoConfigPortStatusTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXPnoConfigPortStatusTxEnable.setStatus("current")


class _LldpXPnoConfigAliasTxEnable_Type(TruthValue):
    """Custom type lldpXPnoConfigAliasTxEnable based on TruthValue"""


_LldpXPnoConfigAliasTxEnable_Object = MibTableColumn
lldpXPnoConfigAliasTxEnable = _LldpXPnoConfigAliasTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1, 1, 3),
    _LldpXPnoConfigAliasTxEnable_Type()
)
lldpXPnoConfigAliasTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXPnoConfigAliasTxEnable.setStatus("current")


class _LldpXPnoConfigMrpTxEnable_Type(TruthValue):
    """Custom type lldpXPnoConfigMrpTxEnable based on TruthValue"""


_LldpXPnoConfigMrpTxEnable_Object = MibTableColumn
lldpXPnoConfigMrpTxEnable = _LldpXPnoConfigMrpTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1, 1, 4),
    _LldpXPnoConfigMrpTxEnable_Type()
)
lldpXPnoConfigMrpTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXPnoConfigMrpTxEnable.setStatus("current")
_LldpXPnoLocalData_ObjectIdentity = ObjectIdentity
lldpXPnoLocalData = _LldpXPnoLocalData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2)
)
_LldpXPnoLocTable_Object = MibTable
lldpXPnoLocTable = _LldpXPnoLocTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXPnoLocTable.setStatus("current")
_LldpXPnoLocEntry_Object = MibTableRow
lldpXPnoLocEntry = _LldpXPnoLocEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1)
)
lldpXPnoLocEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXPnoLocEntry.setStatus("current")


class _LldpXPnoLocLPDValue_Type(Unsigned32):
    """Custom type lldpXPnoLocLPDValue based on Unsigned32"""
    defaultValue = 0


_LldpXPnoLocLPDValue_Object = MibTableColumn
lldpXPnoLocLPDValue = _LldpXPnoLocLPDValue_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 1),
    _LldpXPnoLocLPDValue_Type()
)
lldpXPnoLocLPDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoLocLPDValue.setStatus("current")
if mibBuilder.loadTexts:
    lldpXPnoLocLPDValue.setUnits("ns")


class _LldpXPnoLocPortTxDValue_Type(Unsigned32):
    """Custom type lldpXPnoLocPortTxDValue based on Unsigned32"""
    defaultValue = 0


_LldpXPnoLocPortTxDValue_Object = MibTableColumn
lldpXPnoLocPortTxDValue = _LldpXPnoLocPortTxDValue_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 2),
    _LldpXPnoLocPortTxDValue_Type()
)
lldpXPnoLocPortTxDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoLocPortTxDValue.setStatus("current")
if mibBuilder.loadTexts:
    lldpXPnoLocPortTxDValue.setUnits("ns")


class _LldpXPnoLocPortRxDValue_Type(Unsigned32):
    """Custom type lldpXPnoLocPortRxDValue based on Unsigned32"""
    defaultValue = 0


_LldpXPnoLocPortRxDValue_Object = MibTableColumn
lldpXPnoLocPortRxDValue = _LldpXPnoLocPortRxDValue_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 3),
    _LldpXPnoLocPortRxDValue_Type()
)
lldpXPnoLocPortRxDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoLocPortRxDValue.setStatus("current")
if mibBuilder.loadTexts:
    lldpXPnoLocPortRxDValue.setUnits("ns")


class _LldpXPnoLocPortStatusRT2_Type(Integer32):
    """Custom type lldpXPnoLocPortStatusRT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("off", 0),
          ("running", 2))
    )


_LldpXPnoLocPortStatusRT2_Type.__name__ = "Integer32"
_LldpXPnoLocPortStatusRT2_Object = MibTableColumn
lldpXPnoLocPortStatusRT2 = _LldpXPnoLocPortStatusRT2_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 4),
    _LldpXPnoLocPortStatusRT2_Type()
)
lldpXPnoLocPortStatusRT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoLocPortStatusRT2.setStatus("current")


class _LldpXPnoLocPortStatusRT3_Type(Integer32):
    """Custom type lldpXPnoLocPortStatusRT3 based on Integer32"""
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
        *(("configured", 1),
          ("down", 3),
          ("off", 0),
          ("running", 4),
          ("up", 2))
    )


_LldpXPnoLocPortStatusRT3_Type.__name__ = "Integer32"
_LldpXPnoLocPortStatusRT3_Object = MibTableColumn
lldpXPnoLocPortStatusRT3 = _LldpXPnoLocPortStatusRT3_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 5),
    _LldpXPnoLocPortStatusRT3_Type()
)
lldpXPnoLocPortStatusRT3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoLocPortStatusRT3.setStatus("current")
_LldpXPnoLocPortNoS_Type = DisplayString
_LldpXPnoLocPortNoS_Object = MibTableColumn
lldpXPnoLocPortNoS = _LldpXPnoLocPortNoS_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 6),
    _LldpXPnoLocPortNoS_Type()
)
lldpXPnoLocPortNoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoLocPortNoS.setStatus("current")


class _LldpXPnoLocPortMrpUuId_Type(OctetString):
    """Custom type lldpXPnoLocPortMrpUuId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_LldpXPnoLocPortMrpUuId_Type.__name__ = "OctetString"
_LldpXPnoLocPortMrpUuId_Object = MibTableColumn
lldpXPnoLocPortMrpUuId = _LldpXPnoLocPortMrpUuId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 7),
    _LldpXPnoLocPortMrpUuId_Type()
)
lldpXPnoLocPortMrpUuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoLocPortMrpUuId.setStatus("current")


class _LldpXPnoLocPortMrrtStatus_Type(Integer32):
    """Custom type lldpXPnoLocPortMrrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("off", 0),
          ("up", 2))
    )


_LldpXPnoLocPortMrrtStatus_Type.__name__ = "Integer32"
_LldpXPnoLocPortMrrtStatus_Object = MibTableColumn
lldpXPnoLocPortMrrtStatus = _LldpXPnoLocPortMrrtStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 8),
    _LldpXPnoLocPortMrrtStatus_Type()
)
lldpXPnoLocPortMrrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoLocPortMrrtStatus.setStatus("current")
_LldpXPnoRemoteData_ObjectIdentity = ObjectIdentity
lldpXPnoRemoteData = _LldpXPnoRemoteData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3)
)
_LldpXPnoRemTable_Object = MibTable
lldpXPnoRemTable = _LldpXPnoRemTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXPnoRemTable.setStatus("current")
_LldpXPnoRemEntry_Object = MibTableRow
lldpXPnoRemEntry = _LldpXPnoRemEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1)
)
lldpXPnoRemEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXPnoRemEntry.setStatus("current")
_LldpXPnoRemLPDValue_Type = Unsigned32
_LldpXPnoRemLPDValue_Object = MibTableColumn
lldpXPnoRemLPDValue = _LldpXPnoRemLPDValue_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 1),
    _LldpXPnoRemLPDValue_Type()
)
lldpXPnoRemLPDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoRemLPDValue.setStatus("current")
if mibBuilder.loadTexts:
    lldpXPnoRemLPDValue.setUnits("ns")
_LldpXPnoRemPortTxDValue_Type = Unsigned32
_LldpXPnoRemPortTxDValue_Object = MibTableColumn
lldpXPnoRemPortTxDValue = _LldpXPnoRemPortTxDValue_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 2),
    _LldpXPnoRemPortTxDValue_Type()
)
lldpXPnoRemPortTxDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoRemPortTxDValue.setStatus("current")
if mibBuilder.loadTexts:
    lldpXPnoRemPortTxDValue.setUnits("ns")
_LldpXPnoRemPortRxDValue_Type = Unsigned32
_LldpXPnoRemPortRxDValue_Object = MibTableColumn
lldpXPnoRemPortRxDValue = _LldpXPnoRemPortRxDValue_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 3),
    _LldpXPnoRemPortRxDValue_Type()
)
lldpXPnoRemPortRxDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoRemPortRxDValue.setStatus("current")
if mibBuilder.loadTexts:
    lldpXPnoRemPortRxDValue.setUnits("ns")


class _LldpXPnoRemPortStatusRT2_Type(Integer32):
    """Custom type lldpXPnoRemPortStatusRT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("off", 0),
          ("running", 2))
    )


_LldpXPnoRemPortStatusRT2_Type.__name__ = "Integer32"
_LldpXPnoRemPortStatusRT2_Object = MibTableColumn
lldpXPnoRemPortStatusRT2 = _LldpXPnoRemPortStatusRT2_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 4),
    _LldpXPnoRemPortStatusRT2_Type()
)
lldpXPnoRemPortStatusRT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoRemPortStatusRT2.setStatus("current")


class _LldpXPnoRemPortStatusRT3_Type(Integer32):
    """Custom type lldpXPnoRemPortStatusRT3 based on Integer32"""
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
        *(("configured", 1),
          ("down", 3),
          ("off", 0),
          ("running", 4),
          ("up", 2))
    )


_LldpXPnoRemPortStatusRT3_Type.__name__ = "Integer32"
_LldpXPnoRemPortStatusRT3_Object = MibTableColumn
lldpXPnoRemPortStatusRT3 = _LldpXPnoRemPortStatusRT3_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 5),
    _LldpXPnoRemPortStatusRT3_Type()
)
lldpXPnoRemPortStatusRT3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoRemPortStatusRT3.setStatus("current")
_LldpXPnoRemPortNoS_Type = DisplayString
_LldpXPnoRemPortNoS_Object = MibTableColumn
lldpXPnoRemPortNoS = _LldpXPnoRemPortNoS_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 6),
    _LldpXPnoRemPortNoS_Type()
)
lldpXPnoRemPortNoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoRemPortNoS.setStatus("current")


class _LldpXPnoRemPortMrpUuId_Type(OctetString):
    """Custom type lldpXPnoRemPortMrpUuId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_LldpXPnoRemPortMrpUuId_Type.__name__ = "OctetString"
_LldpXPnoRemPortMrpUuId_Object = MibTableColumn
lldpXPnoRemPortMrpUuId = _LldpXPnoRemPortMrpUuId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 7),
    _LldpXPnoRemPortMrpUuId_Type()
)
lldpXPnoRemPortMrpUuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoRemPortMrpUuId.setStatus("current")


class _LldpXPnoRemPortMrrtStatus_Type(Integer32):
    """Custom type lldpXPnoRemPortMrrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("off", 0),
          ("up", 2))
    )


_LldpXPnoRemPortMrrtStatus_Type.__name__ = "Integer32"
_LldpXPnoRemPortMrrtStatus_Object = MibTableColumn
lldpXPnoRemPortMrrtStatus = _LldpXPnoRemPortMrrtStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 8),
    _LldpXPnoRemPortMrrtStatus_Type()
)
lldpXPnoRemPortMrrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXPnoRemPortMrrtStatus.setStatus("current")
_LldpXPnoConformance_ObjectIdentity = ObjectIdentity
lldpXPnoConformance = _LldpXPnoConformance_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2)
)
_LldpXPnoCompliances_ObjectIdentity = ObjectIdentity
lldpXPnoCompliances = _LldpXPnoCompliances_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 1)
)
_LldpXPnoGroups_ObjectIdentity = ObjectIdentity
lldpXPnoGroups = _LldpXPnoGroups_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 2)
)
lldpPortConfigEntry.registerAugmentions(
    ("LLDP-EXT-PNO-MIB",
     "lldpXPnoConfigEntry")
)
lldpXPnoConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())

# Managed Objects groups

lldpXPnoConfigGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 2, 1)
)
lldpXPnoConfigGroup.setObjects(
      *(("LLDP-EXT-PNO-MIB", "lldpXPnoConfigSPDTxEnable"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoConfigPortStatusTxEnable"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoConfigAliasTxEnable"))
)
if mibBuilder.loadTexts:
    lldpXPnoConfigGroup.setStatus("current")

lldpXPnoLocGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 2, 2)
)
lldpXPnoLocGroup.setObjects(
      *(("LLDP-EXT-PNO-MIB", "lldpXPnoLocLPDValue"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortTxDValue"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortRxDValue"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortStatusRT2"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortStatusRT3"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortNoS"))
)
if mibBuilder.loadTexts:
    lldpXPnoLocGroup.setStatus("current")

lldpXPnoRemGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 2, 3)
)
lldpXPnoRemGroup.setObjects(
      *(("LLDP-EXT-PNO-MIB", "lldpXPnoRemLPDValue"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortTxDValue"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortRxDValue"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortStatusRT2"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortStatusRT3"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortNoS"))
)
if mibBuilder.loadTexts:
    lldpXPnoRemGroup.setStatus("current")

lldpXPnoMRPGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 2, 4)
)
lldpXPnoMRPGroup.setObjects(
      *(("LLDP-EXT-PNO-MIB", "lldpXPnoConfigMrpTxEnable"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortMrpUuId"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortMrrtStatus"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortMrpUuId"),
        ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortMrrtStatus"))
)
if mibBuilder.loadTexts:
    lldpXPnoMRPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpXPnoCompliance = ModuleCompliance(
    (1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXPnoCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-PNO-MIB",
    **{"lldpXPnoMIB": lldpXPnoMIB,
       "lldpXPnoObjects": lldpXPnoObjects,
       "lldpXPnoConfig": lldpXPnoConfig,
       "lldpXPnoConfigTable": lldpXPnoConfigTable,
       "lldpXPnoConfigEntry": lldpXPnoConfigEntry,
       "lldpXPnoConfigSPDTxEnable": lldpXPnoConfigSPDTxEnable,
       "lldpXPnoConfigPortStatusTxEnable": lldpXPnoConfigPortStatusTxEnable,
       "lldpXPnoConfigAliasTxEnable": lldpXPnoConfigAliasTxEnable,
       "lldpXPnoConfigMrpTxEnable": lldpXPnoConfigMrpTxEnable,
       "lldpXPnoLocalData": lldpXPnoLocalData,
       "lldpXPnoLocTable": lldpXPnoLocTable,
       "lldpXPnoLocEntry": lldpXPnoLocEntry,
       "lldpXPnoLocLPDValue": lldpXPnoLocLPDValue,
       "lldpXPnoLocPortTxDValue": lldpXPnoLocPortTxDValue,
       "lldpXPnoLocPortRxDValue": lldpXPnoLocPortRxDValue,
       "lldpXPnoLocPortStatusRT2": lldpXPnoLocPortStatusRT2,
       "lldpXPnoLocPortStatusRT3": lldpXPnoLocPortStatusRT3,
       "lldpXPnoLocPortNoS": lldpXPnoLocPortNoS,
       "lldpXPnoLocPortMrpUuId": lldpXPnoLocPortMrpUuId,
       "lldpXPnoLocPortMrrtStatus": lldpXPnoLocPortMrrtStatus,
       "lldpXPnoRemoteData": lldpXPnoRemoteData,
       "lldpXPnoRemTable": lldpXPnoRemTable,
       "lldpXPnoRemEntry": lldpXPnoRemEntry,
       "lldpXPnoRemLPDValue": lldpXPnoRemLPDValue,
       "lldpXPnoRemPortTxDValue": lldpXPnoRemPortTxDValue,
       "lldpXPnoRemPortRxDValue": lldpXPnoRemPortRxDValue,
       "lldpXPnoRemPortStatusRT2": lldpXPnoRemPortStatusRT2,
       "lldpXPnoRemPortStatusRT3": lldpXPnoRemPortStatusRT3,
       "lldpXPnoRemPortNoS": lldpXPnoRemPortNoS,
       "lldpXPnoRemPortMrpUuId": lldpXPnoRemPortMrpUuId,
       "lldpXPnoRemPortMrrtStatus": lldpXPnoRemPortMrrtStatus,
       "lldpXPnoConformance": lldpXPnoConformance,
       "lldpXPnoCompliances": lldpXPnoCompliances,
       "lldpXPnoCompliance": lldpXPnoCompliance,
       "lldpXPnoGroups": lldpXPnoGroups,
       "lldpXPnoConfigGroup": lldpXPnoConfigGroup,
       "lldpXPnoLocGroup": lldpXPnoLocGroup,
       "lldpXPnoRemGroup": lldpXPnoRemGroup,
       "lldpXPnoMRPGroup": lldpXPnoMRPGroup}
)
