# SNMP MIB module (CISCO-CDSTV-INGEST-TUNING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDSTV-INGEST-TUNING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:18 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCdstvIngestTuningMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 750)
)
ciscoCdstvIngestTuningMIB.setRevisions(
        ("2010-06-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCdstvIngestTuningMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCdstvIngestTuningMIBNotifs = _CiscoCdstvIngestTuningMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 0)
)
_CiscoCdstvIngestTuningMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdstvIngestTuningMIBObjects = _CiscoCdstvIngestTuningMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 1)
)
_CdstvTrickModeSpeedTable_Object = MibTable
cdstvTrickModeSpeedTable = _CdstvTrickModeSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1)
)
if mibBuilder.loadTexts:
    cdstvTrickModeSpeedTable.setStatus("current")
_CdstvTrickModeSpeedEntry_Object = MibTableRow
cdstvTrickModeSpeedEntry = _CdstvTrickModeSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1)
)
cdstvTrickModeSpeedEntry.setIndexNames(
    (0, "CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvTrickModeSpeedIndex"),
)
if mibBuilder.loadTexts:
    cdstvTrickModeSpeedEntry.setStatus("current")
_CdstvTrickModeSpeedIndex_Type = Unsigned32
_CdstvTrickModeSpeedIndex_Object = MibTableColumn
cdstvTrickModeSpeedIndex = _CdstvTrickModeSpeedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1, 1),
    _CdstvTrickModeSpeedIndex_Type()
)
cdstvTrickModeSpeedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdstvTrickModeSpeedIndex.setStatus("current")


class _CdstvTrickModeSpeed_Type(Integer32):
    """Custom type cdstvTrickModeSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_CdstvTrickModeSpeed_Type.__name__ = "Integer32"
_CdstvTrickModeSpeed_Object = MibTableColumn
cdstvTrickModeSpeed = _CdstvTrickModeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1, 2),
    _CdstvTrickModeSpeed_Type()
)
cdstvTrickModeSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvTrickModeSpeed.setStatus("current")
_CdstvServerIngestMPEGSettings_ObjectIdentity = ObjectIdentity
cdstvServerIngestMPEGSettings = _CdstvServerIngestMPEGSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2)
)


class _CdstvServerPIDStandardization_Type(Integer32):
    """Custom type cdstvServerPIDStandardization based on Integer32"""
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


_CdstvServerPIDStandardization_Type.__name__ = "Integer32"
_CdstvServerPIDStandardization_Object = MibScalar
cdstvServerPIDStandardization = _CdstvServerPIDStandardization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 1),
    _CdstvServerPIDStandardization_Type()
)
cdstvServerPIDStandardization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerPIDStandardization.setStatus("current")


class _CdstvServerSequenceEndRemove_Type(Integer32):
    """Custom type cdstvServerSequenceEndRemove based on Integer32"""
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


_CdstvServerSequenceEndRemove_Type.__name__ = "Integer32"
_CdstvServerSequenceEndRemove_Object = MibScalar
cdstvServerSequenceEndRemove = _CdstvServerSequenceEndRemove_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 2),
    _CdstvServerSequenceEndRemove_Type()
)
cdstvServerSequenceEndRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerSequenceEndRemove.setStatus("current")


class _CdstvServerRateStandardize_Type(Integer32):
    """Custom type cdstvServerRateStandardize based on Integer32"""
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


_CdstvServerRateStandardize_Type.__name__ = "Integer32"
_CdstvServerRateStandardize_Object = MibScalar
cdstvServerRateStandardize = _CdstvServerRateStandardize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 3),
    _CdstvServerRateStandardize_Type()
)
cdstvServerRateStandardize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerRateStandardize.setStatus("current")
_CiscoCdstvIngestTuningMIBConform_ObjectIdentity = ObjectIdentity
ciscoCdstvIngestTuningMIBConform = _CiscoCdstvIngestTuningMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 2)
)
_CiscoCdstvIngestTuningMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdstvIngestTuningMIBCompliances = _CiscoCdstvIngestTuningMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 1)
)
_CiscoCdstvIngestTuningMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdstvIngestTuningMIBGroups = _CiscoCdstvIngestTuningMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 2)
)

# Managed Objects groups

ciscoCdstvIngestTuningMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 2, 1)
)
ciscoCdstvIngestTuningMIBMainObjectGroup.setObjects(
      *(("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvTrickModeSpeed"),
        ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerPIDStandardization"),
        ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerSequenceEndRemove"),
        ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerRateStandardize"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIngestTuningMIBMainObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCdstvIngestTuningMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCdstvIngestTuningMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDSTV-INGEST-TUNING-MIB",
    **{"ciscoCdstvIngestTuningMIB": ciscoCdstvIngestTuningMIB,
       "ciscoCdstvIngestTuningMIBNotifs": ciscoCdstvIngestTuningMIBNotifs,
       "ciscoCdstvIngestTuningMIBObjects": ciscoCdstvIngestTuningMIBObjects,
       "cdstvTrickModeSpeedTable": cdstvTrickModeSpeedTable,
       "cdstvTrickModeSpeedEntry": cdstvTrickModeSpeedEntry,
       "cdstvTrickModeSpeedIndex": cdstvTrickModeSpeedIndex,
       "cdstvTrickModeSpeed": cdstvTrickModeSpeed,
       "cdstvServerIngestMPEGSettings": cdstvServerIngestMPEGSettings,
       "cdstvServerPIDStandardization": cdstvServerPIDStandardization,
       "cdstvServerSequenceEndRemove": cdstvServerSequenceEndRemove,
       "cdstvServerRateStandardize": cdstvServerRateStandardize,
       "ciscoCdstvIngestTuningMIBConform": ciscoCdstvIngestTuningMIBConform,
       "ciscoCdstvIngestTuningMIBCompliances": ciscoCdstvIngestTuningMIBCompliances,
       "ciscoCdstvIngestTuningMIBCompliance": ciscoCdstvIngestTuningMIBCompliance,
       "ciscoCdstvIngestTuningMIBGroups": ciscoCdstvIngestTuningMIBGroups,
       "ciscoCdstvIngestTuningMIBMainObjectGroup": ciscoCdstvIngestTuningMIBMainObjectGroup}
)
