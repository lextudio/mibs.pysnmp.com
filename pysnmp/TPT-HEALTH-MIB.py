# SNMP MIB module (TPT-HEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-HEALTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:56 2024
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

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_health_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13)
)
tpt_health_objs.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HealthSeverity(Integer32, TextualConvention):
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
        *(("critical", 4),
          ("info", 1),
          ("major", 3),
          ("minor", 2),
          ("normal", 0))
    )



class HealthThresholdType(Integer32, TextualConvention):
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
        *(("maximum", 3),
          ("minimum", 1),
          ("range", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HealthTempTable_Object = MibTable
healthTempTable = _HealthTempTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 1)
)
if mibBuilder.loadTexts:
    healthTempTable.setStatus("current")
_HealthTempEntry_Object = MibTableRow
healthTempEntry = _HealthTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 1, 1)
)
healthTempEntry.setIndexNames(
    (0, "TPT-HEALTH-MIB", "healthTempIndex"),
)
if mibBuilder.loadTexts:
    healthTempEntry.setStatus("current")
_HealthTempIndex_Type = Unsigned32
_HealthTempIndex_Object = MibTableColumn
healthTempIndex = _HealthTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 1, 1, 1),
    _HealthTempIndex_Type()
)
healthTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthTempIndex.setStatus("current")


class _HealthTempChannel_Type(OctetString):
    """Custom type healthTempChannel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HealthTempChannel_Type.__name__ = "OctetString"
_HealthTempChannel_Object = MibTableColumn
healthTempChannel = _HealthTempChannel_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 1, 1, 2),
    _HealthTempChannel_Type()
)
healthTempChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthTempChannel.setStatus("current")
_HealthTempValue_Type = Unsigned32
_HealthTempValue_Object = MibTableColumn
healthTempValue = _HealthTempValue_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 1, 1, 3),
    _HealthTempValue_Type()
)
healthTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthTempValue.setStatus("current")
_HealthTempSeverity_Type = HealthSeverity
_HealthTempSeverity_Object = MibTableColumn
healthTempSeverity = _HealthTempSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 1, 1, 4),
    _HealthTempSeverity_Type()
)
healthTempSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthTempSeverity.setStatus("current")
_HealthTempThresholdType_Type = HealthThresholdType
_HealthTempThresholdType_Object = MibTableColumn
healthTempThresholdType = _HealthTempThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 1, 1, 5),
    _HealthTempThresholdType_Type()
)
healthTempThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthTempThresholdType.setStatus("current")
_HealthTempMajor_Type = Unsigned32
_HealthTempMajor_Object = MibTableColumn
healthTempMajor = _HealthTempMajor_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 1, 1, 6),
    _HealthTempMajor_Type()
)
healthTempMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthTempMajor.setStatus("current")
_HealthTempCritical_Type = Unsigned32
_HealthTempCritical_Object = MibTableColumn
healthTempCritical = _HealthTempCritical_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 1, 1, 7),
    _HealthTempCritical_Type()
)
healthTempCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthTempCritical.setStatus("current")
_HealthFanTable_Object = MibTable
healthFanTable = _HealthFanTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 2)
)
if mibBuilder.loadTexts:
    healthFanTable.setStatus("current")
_HealthFanEntry_Object = MibTableRow
healthFanEntry = _HealthFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 2, 1)
)
healthFanEntry.setIndexNames(
    (0, "TPT-HEALTH-MIB", "healthFanIndex"),
)
if mibBuilder.loadTexts:
    healthFanEntry.setStatus("current")
_HealthFanIndex_Type = Unsigned32
_HealthFanIndex_Object = MibTableColumn
healthFanIndex = _HealthFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 2, 1, 1),
    _HealthFanIndex_Type()
)
healthFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthFanIndex.setStatus("current")


class _HealthFanChannel_Type(OctetString):
    """Custom type healthFanChannel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HealthFanChannel_Type.__name__ = "OctetString"
_HealthFanChannel_Object = MibTableColumn
healthFanChannel = _HealthFanChannel_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 2, 1, 2),
    _HealthFanChannel_Type()
)
healthFanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFanChannel.setStatus("current")
_HealthFanValue_Type = Unsigned32
_HealthFanValue_Object = MibTableColumn
healthFanValue = _HealthFanValue_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 2, 1, 3),
    _HealthFanValue_Type()
)
healthFanValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFanValue.setStatus("current")
_HealthFanSeverity_Type = HealthSeverity
_HealthFanSeverity_Object = MibTableColumn
healthFanSeverity = _HealthFanSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 2, 1, 4),
    _HealthFanSeverity_Type()
)
healthFanSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFanSeverity.setStatus("current")
_HealthFanThresholdType_Type = HealthThresholdType
_HealthFanThresholdType_Object = MibTableColumn
healthFanThresholdType = _HealthFanThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 2, 1, 5),
    _HealthFanThresholdType_Type()
)
healthFanThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFanThresholdType.setStatus("current")
_HealthFanMajor_Type = Unsigned32
_HealthFanMajor_Object = MibTableColumn
healthFanMajor = _HealthFanMajor_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 2, 1, 6),
    _HealthFanMajor_Type()
)
healthFanMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFanMajor.setStatus("current")
_HealthFanCritical_Type = Unsigned32
_HealthFanCritical_Object = MibTableColumn
healthFanCritical = _HealthFanCritical_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 2, 1, 7),
    _HealthFanCritical_Type()
)
healthFanCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFanCritical.setStatus("current")
_HealthVoltageTable_Object = MibTable
healthVoltageTable = _HealthVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 3)
)
if mibBuilder.loadTexts:
    healthVoltageTable.setStatus("current")
_HealthVoltageEntry_Object = MibTableRow
healthVoltageEntry = _HealthVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 3, 1)
)
healthVoltageEntry.setIndexNames(
    (0, "TPT-HEALTH-MIB", "healthVoltageIndex"),
)
if mibBuilder.loadTexts:
    healthVoltageEntry.setStatus("current")
_HealthVoltageIndex_Type = Unsigned32
_HealthVoltageIndex_Object = MibTableColumn
healthVoltageIndex = _HealthVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 3, 1, 1),
    _HealthVoltageIndex_Type()
)
healthVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthVoltageIndex.setStatus("current")


class _HealthVoltageChannel_Type(OctetString):
    """Custom type healthVoltageChannel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HealthVoltageChannel_Type.__name__ = "OctetString"
_HealthVoltageChannel_Object = MibTableColumn
healthVoltageChannel = _HealthVoltageChannel_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 3, 1, 2),
    _HealthVoltageChannel_Type()
)
healthVoltageChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthVoltageChannel.setStatus("current")
_HealthVoltageValue_Type = Unsigned32
_HealthVoltageValue_Object = MibTableColumn
healthVoltageValue = _HealthVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 3, 1, 3),
    _HealthVoltageValue_Type()
)
healthVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthVoltageValue.setStatus("current")
_HealthVoltageSeverity_Type = HealthSeverity
_HealthVoltageSeverity_Object = MibTableColumn
healthVoltageSeverity = _HealthVoltageSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 3, 1, 4),
    _HealthVoltageSeverity_Type()
)
healthVoltageSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthVoltageSeverity.setStatus("current")
_HealthVoltageThresholdType_Type = HealthThresholdType
_HealthVoltageThresholdType_Object = MibTableColumn
healthVoltageThresholdType = _HealthVoltageThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 3, 1, 5),
    _HealthVoltageThresholdType_Type()
)
healthVoltageThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthVoltageThresholdType.setStatus("current")
_HealthVoltageMajor_Type = Unsigned32
_HealthVoltageMajor_Object = MibTableColumn
healthVoltageMajor = _HealthVoltageMajor_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 3, 1, 6),
    _HealthVoltageMajor_Type()
)
healthVoltageMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthVoltageMajor.setStatus("current")
_HealthVoltageCritical_Type = Unsigned32
_HealthVoltageCritical_Object = MibTableColumn
healthVoltageCritical = _HealthVoltageCritical_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 3, 1, 7),
    _HealthVoltageCritical_Type()
)
healthVoltageCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthVoltageCritical.setStatus("current")
_HealthVoltageNominal_Type = Unsigned32
_HealthVoltageNominal_Object = MibTableColumn
healthVoltageNominal = _HealthVoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 3, 1, 8),
    _HealthVoltageNominal_Type()
)
healthVoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthVoltageNominal.setStatus("current")
_HealthI2CTable_Object = MibTable
healthI2CTable = _HealthI2CTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 4)
)
if mibBuilder.loadTexts:
    healthI2CTable.setStatus("current")
_HealthI2CEntry_Object = MibTableRow
healthI2CEntry = _HealthI2CEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 4, 1)
)
healthI2CEntry.setIndexNames(
    (0, "TPT-HEALTH-MIB", "healthI2CIndex"),
)
if mibBuilder.loadTexts:
    healthI2CEntry.setStatus("current")
_HealthI2CIndex_Type = Unsigned32
_HealthI2CIndex_Object = MibTableColumn
healthI2CIndex = _HealthI2CIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 4, 1, 1),
    _HealthI2CIndex_Type()
)
healthI2CIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthI2CIndex.setStatus("current")


class _HealthI2CChannel_Type(OctetString):
    """Custom type healthI2CChannel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HealthI2CChannel_Type.__name__ = "OctetString"
_HealthI2CChannel_Object = MibTableColumn
healthI2CChannel = _HealthI2CChannel_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 4, 1, 2),
    _HealthI2CChannel_Type()
)
healthI2CChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthI2CChannel.setStatus("current")
_HealthI2CValue_Type = Unsigned32
_HealthI2CValue_Object = MibTableColumn
healthI2CValue = _HealthI2CValue_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 4, 1, 3),
    _HealthI2CValue_Type()
)
healthI2CValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthI2CValue.setStatus("current")
_HealthI2CSeverity_Type = HealthSeverity
_HealthI2CSeverity_Object = MibTableColumn
healthI2CSeverity = _HealthI2CSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 4, 1, 4),
    _HealthI2CSeverity_Type()
)
healthI2CSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthI2CSeverity.setStatus("current")
_HealthI2CThresholdType_Type = HealthThresholdType
_HealthI2CThresholdType_Object = MibTableColumn
healthI2CThresholdType = _HealthI2CThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 4, 1, 5),
    _HealthI2CThresholdType_Type()
)
healthI2CThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthI2CThresholdType.setStatus("current")
_HealthI2CMajor_Type = Unsigned32
_HealthI2CMajor_Object = MibTableColumn
healthI2CMajor = _HealthI2CMajor_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 4, 1, 6),
    _HealthI2CMajor_Type()
)
healthI2CMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthI2CMajor.setStatus("current")
_HealthI2CCritical_Type = Unsigned32
_HealthI2CCritical_Object = MibTableColumn
healthI2CCritical = _HealthI2CCritical_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 13, 4, 1, 7),
    _HealthI2CCritical_Type()
)
healthI2CCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthI2CCritical.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-HEALTH-MIB",
    **{"HealthSeverity": HealthSeverity,
       "HealthThresholdType": HealthThresholdType,
       "tpt-health-objs": tpt_health_objs,
       "healthTempTable": healthTempTable,
       "healthTempEntry": healthTempEntry,
       "healthTempIndex": healthTempIndex,
       "healthTempChannel": healthTempChannel,
       "healthTempValue": healthTempValue,
       "healthTempSeverity": healthTempSeverity,
       "healthTempThresholdType": healthTempThresholdType,
       "healthTempMajor": healthTempMajor,
       "healthTempCritical": healthTempCritical,
       "healthFanTable": healthFanTable,
       "healthFanEntry": healthFanEntry,
       "healthFanIndex": healthFanIndex,
       "healthFanChannel": healthFanChannel,
       "healthFanValue": healthFanValue,
       "healthFanSeverity": healthFanSeverity,
       "healthFanThresholdType": healthFanThresholdType,
       "healthFanMajor": healthFanMajor,
       "healthFanCritical": healthFanCritical,
       "healthVoltageTable": healthVoltageTable,
       "healthVoltageEntry": healthVoltageEntry,
       "healthVoltageIndex": healthVoltageIndex,
       "healthVoltageChannel": healthVoltageChannel,
       "healthVoltageValue": healthVoltageValue,
       "healthVoltageSeverity": healthVoltageSeverity,
       "healthVoltageThresholdType": healthVoltageThresholdType,
       "healthVoltageMajor": healthVoltageMajor,
       "healthVoltageCritical": healthVoltageCritical,
       "healthVoltageNominal": healthVoltageNominal,
       "healthI2CTable": healthI2CTable,
       "healthI2CEntry": healthI2CEntry,
       "healthI2CIndex": healthI2CIndex,
       "healthI2CChannel": healthI2CChannel,
       "healthI2CValue": healthI2CValue,
       "healthI2CSeverity": healthI2CSeverity,
       "healthI2CThresholdType": healthI2CThresholdType,
       "healthI2CMajor": healthI2CMajor,
       "healthI2CCritical": healthI2CCritical}
)
