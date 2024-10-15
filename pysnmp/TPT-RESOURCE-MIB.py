# SNMP MIB module (TPT-RESOURCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-RESOURCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:08 2024
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

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_resource = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5)
)
tpt_resource.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ResourceIdentifier(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("chassisTemp", 4),
          ("fan", 5),
          ("filesystem", 1),
          ("hardDisk", 7),
          ("hpCPU", 2),
          ("hpMemory", 3),
          ("i2cBus", 8),
          ("powerSupply", 6))
    )



class ResourceState(Integer32, TextualConvention):
    status = "current"
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
        *(("green", 3),
          ("red", 1),
          ("unknown", 0),
          ("yellow", 2))
    )



class PowerSupplyState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 2),
          ("red", 1),
          ("unknown", 0))
    )



class SnmpVersions(Integer32, TextualConvention):
    status = "current"
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
        *(("none", 0),
          ("snmpv2", 1),
          ("snmpv2-and-snmpv3", 3),
          ("snmpv3", 2))
    )



class EnabledOrNot(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class FilesystemState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("formatted", 1),
          ("mounted", 2),
          ("unformatted", 0))
    )



class RemoteAuthType(Integer32, TextualConvention):
    status = "current"
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
        *(("none", 0),
          ("radius", 1),
          ("sms", 2),
          ("tacacs", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ResourceNumberOfFilesystems_Type = Unsigned32
_ResourceNumberOfFilesystems_Object = MibScalar
resourceNumberOfFilesystems = _ResourceNumberOfFilesystems_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 1),
    _ResourceNumberOfFilesystems_Type()
)
resourceNumberOfFilesystems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNumberOfFilesystems.setStatus("current")
_ResourceFSTable_Object = MibTable
resourceFSTable = _ResourceFSTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2)
)
if mibBuilder.loadTexts:
    resourceFSTable.setStatus("current")
_ResourceFSEntry_Object = MibTableRow
resourceFSEntry = _ResourceFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2, 1)
)
resourceFSEntry.setIndexNames(
    (0, "TPT-RESOURCE-MIB", "resourceFSIndex"),
)
if mibBuilder.loadTexts:
    resourceFSEntry.setStatus("current")
_ResourceFSInUseMB_Type = Integer32
_ResourceFSInUseMB_Object = MibTableColumn
resourceFSInUseMB = _ResourceFSInUseMB_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2, 1, 1),
    _ResourceFSInUseMB_Type()
)
resourceFSInUseMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceFSInUseMB.setStatus("current")
_ResourceFSThresholdMaj_Type = Integer32
_ResourceFSThresholdMaj_Object = MibTableColumn
resourceFSThresholdMaj = _ResourceFSThresholdMaj_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2, 1, 2),
    _ResourceFSThresholdMaj_Type()
)
resourceFSThresholdMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceFSThresholdMaj.setStatus("current")
_ResourceFSThresholdCrit_Type = Integer32
_ResourceFSThresholdCrit_Object = MibTableColumn
resourceFSThresholdCrit = _ResourceFSThresholdCrit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2, 1, 3),
    _ResourceFSThresholdCrit_Type()
)
resourceFSThresholdCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceFSThresholdCrit.setStatus("current")
_ResourceFSRangeMin_Type = Integer32
_ResourceFSRangeMin_Object = MibTableColumn
resourceFSRangeMin = _ResourceFSRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2, 1, 4),
    _ResourceFSRangeMin_Type()
)
resourceFSRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceFSRangeMin.setStatus("current")
_ResourceFSRangeMax_Type = Integer32
_ResourceFSRangeMax_Object = MibTableColumn
resourceFSRangeMax = _ResourceFSRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2, 1, 5),
    _ResourceFSRangeMax_Type()
)
resourceFSRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceFSRangeMax.setStatus("current")


class _ResourceFSName_Type(OctetString):
    """Custom type resourceFSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ResourceFSName_Type.__name__ = "OctetString"
_ResourceFSName_Object = MibTableColumn
resourceFSName = _ResourceFSName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2, 1, 6),
    _ResourceFSName_Type()
)
resourceFSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceFSName.setStatus("current")
_ResourceFSIndex_Type = Unsigned32
_ResourceFSIndex_Object = MibTableColumn
resourceFSIndex = _ResourceFSIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2, 1, 7),
    _ResourceFSIndex_Type()
)
resourceFSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    resourceFSIndex.setStatus("current")
_ResourceFSState_Type = FilesystemState
_ResourceFSState_Object = MibTableColumn
resourceFSState = _ResourceFSState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2, 1, 8),
    _ResourceFSState_Type()
)
resourceFSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceFSState.setStatus("current")
_ResourceFSEncryption_Type = EnabledOrNot
_ResourceFSEncryption_Object = MibTableColumn
resourceFSEncryption = _ResourceFSEncryption_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 2, 1, 9),
    _ResourceFSEncryption_Type()
)
resourceFSEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceFSEncryption.setStatus("current")
_ResourceHPMemoryObjs_ObjectIdentity = ObjectIdentity
resourceHPMemoryObjs = _ResourceHPMemoryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 3)
)
if mibBuilder.loadTexts:
    resourceHPMemoryObjs.setStatus("current")
_ResourceHPMemoryInUsePercent_Type = Integer32
_ResourceHPMemoryInUsePercent_Object = MibScalar
resourceHPMemoryInUsePercent = _ResourceHPMemoryInUsePercent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 3, 1),
    _ResourceHPMemoryInUsePercent_Type()
)
resourceHPMemoryInUsePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPMemoryInUsePercent.setStatus("current")
_ResourceHPMemoryThresholdMaj_Type = Integer32
_ResourceHPMemoryThresholdMaj_Object = MibScalar
resourceHPMemoryThresholdMaj = _ResourceHPMemoryThresholdMaj_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 3, 2),
    _ResourceHPMemoryThresholdMaj_Type()
)
resourceHPMemoryThresholdMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPMemoryThresholdMaj.setStatus("current")
_ResourceHPMemoryThresholdCrit_Type = Integer32
_ResourceHPMemoryThresholdCrit_Object = MibScalar
resourceHPMemoryThresholdCrit = _ResourceHPMemoryThresholdCrit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 3, 3),
    _ResourceHPMemoryThresholdCrit_Type()
)
resourceHPMemoryThresholdCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPMemoryThresholdCrit.setStatus("current")
_ResourceHPMemoryRangeMin_Type = Integer32
_ResourceHPMemoryRangeMin_Object = MibScalar
resourceHPMemoryRangeMin = _ResourceHPMemoryRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 3, 4),
    _ResourceHPMemoryRangeMin_Type()
)
resourceHPMemoryRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPMemoryRangeMin.setStatus("current")
_ResourceHPMemoryRangeMax_Type = Integer32
_ResourceHPMemoryRangeMax_Object = MibScalar
resourceHPMemoryRangeMax = _ResourceHPMemoryRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 3, 5),
    _ResourceHPMemoryRangeMax_Type()
)
resourceHPMemoryRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPMemoryRangeMax.setStatus("current")
_ResourceHPMemoryTotal_Type = Unsigned32
_ResourceHPMemoryTotal_Object = MibScalar
resourceHPMemoryTotal = _ResourceHPMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 3, 6),
    _ResourceHPMemoryTotal_Type()
)
resourceHPMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPMemoryTotal.setStatus("current")
_ResourceHPCPUObjs_ObjectIdentity = ObjectIdentity
resourceHPCPUObjs = _ResourceHPCPUObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4)
)
if mibBuilder.loadTexts:
    resourceHPCPUObjs.setStatus("current")
_ResourceHPCPUBusyPercent_Type = Integer32
_ResourceHPCPUBusyPercent_Object = MibScalar
resourceHPCPUBusyPercent = _ResourceHPCPUBusyPercent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 1),
    _ResourceHPCPUBusyPercent_Type()
)
resourceHPCPUBusyPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPCPUBusyPercent.setStatus("current")
_ResourceHPCPUThresholdMaj_Type = Integer32
_ResourceHPCPUThresholdMaj_Object = MibScalar
resourceHPCPUThresholdMaj = _ResourceHPCPUThresholdMaj_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 2),
    _ResourceHPCPUThresholdMaj_Type()
)
resourceHPCPUThresholdMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPCPUThresholdMaj.setStatus("current")
_ResourceHPCPUThresholdCrit_Type = Integer32
_ResourceHPCPUThresholdCrit_Object = MibScalar
resourceHPCPUThresholdCrit = _ResourceHPCPUThresholdCrit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 3),
    _ResourceHPCPUThresholdCrit_Type()
)
resourceHPCPUThresholdCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPCPUThresholdCrit.setStatus("current")
_ResourceHPCPURangeMin_Type = Integer32
_ResourceHPCPURangeMin_Object = MibScalar
resourceHPCPURangeMin = _ResourceHPCPURangeMin_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 4),
    _ResourceHPCPURangeMin_Type()
)
resourceHPCPURangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPCPURangeMin.setStatus("current")
_ResourceHPCPURangeMax_Type = Integer32
_ResourceHPCPURangeMax_Object = MibScalar
resourceHPCPURangeMax = _ResourceHPCPURangeMax_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 5),
    _ResourceHPCPURangeMax_Type()
)
resourceHPCPURangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceHPCPURangeMax.setStatus("current")
_ResourceNPCPUBusyPercentA_Type = Integer32
_ResourceNPCPUBusyPercentA_Object = MibScalar
resourceNPCPUBusyPercentA = _ResourceNPCPUBusyPercentA_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 6),
    _ResourceNPCPUBusyPercentA_Type()
)
resourceNPCPUBusyPercentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentA.setStatus("current")
_ResourceNPCPUBusyPercentTier2A_Type = Integer32
_ResourceNPCPUBusyPercentTier2A_Object = MibScalar
resourceNPCPUBusyPercentTier2A = _ResourceNPCPUBusyPercentTier2A_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 7),
    _ResourceNPCPUBusyPercentTier2A_Type()
)
resourceNPCPUBusyPercentTier2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentTier2A.setStatus("current")
_ResourceNPCPUBusyPercentTier3A_Type = Integer32
_ResourceNPCPUBusyPercentTier3A_Object = MibScalar
resourceNPCPUBusyPercentTier3A = _ResourceNPCPUBusyPercentTier3A_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 8),
    _ResourceNPCPUBusyPercentTier3A_Type()
)
resourceNPCPUBusyPercentTier3A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentTier3A.setStatus("current")
_ResourceNPCPUBusyPercentTier4A_Type = Integer32
_ResourceNPCPUBusyPercentTier4A_Object = MibScalar
resourceNPCPUBusyPercentTier4A = _ResourceNPCPUBusyPercentTier4A_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 9),
    _ResourceNPCPUBusyPercentTier4A_Type()
)
resourceNPCPUBusyPercentTier4A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentTier4A.setStatus("current")
_ResourceNPCPUBusyPercentB_Type = Integer32
_ResourceNPCPUBusyPercentB_Object = MibScalar
resourceNPCPUBusyPercentB = _ResourceNPCPUBusyPercentB_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 10),
    _ResourceNPCPUBusyPercentB_Type()
)
resourceNPCPUBusyPercentB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentB.setStatus("current")
_ResourceNPCPUBusyPercentTier2B_Type = Integer32
_ResourceNPCPUBusyPercentTier2B_Object = MibScalar
resourceNPCPUBusyPercentTier2B = _ResourceNPCPUBusyPercentTier2B_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 11),
    _ResourceNPCPUBusyPercentTier2B_Type()
)
resourceNPCPUBusyPercentTier2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentTier2B.setStatus("current")
_ResourceNPCPUBusyPercentTier3B_Type = Integer32
_ResourceNPCPUBusyPercentTier3B_Object = MibScalar
resourceNPCPUBusyPercentTier3B = _ResourceNPCPUBusyPercentTier3B_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 12),
    _ResourceNPCPUBusyPercentTier3B_Type()
)
resourceNPCPUBusyPercentTier3B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentTier3B.setStatus("current")
_ResourceNPCPUBusyPercentTier4B_Type = Integer32
_ResourceNPCPUBusyPercentTier4B_Object = MibScalar
resourceNPCPUBusyPercentTier4B = _ResourceNPCPUBusyPercentTier4B_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 13),
    _ResourceNPCPUBusyPercentTier4B_Type()
)
resourceNPCPUBusyPercentTier4B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentTier4B.setStatus("current")
_ResourceNPCPUBusyPercentC_Type = Integer32
_ResourceNPCPUBusyPercentC_Object = MibScalar
resourceNPCPUBusyPercentC = _ResourceNPCPUBusyPercentC_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 14),
    _ResourceNPCPUBusyPercentC_Type()
)
resourceNPCPUBusyPercentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentC.setStatus("current")
_ResourceNPCPUBusyPercentTier2C_Type = Integer32
_ResourceNPCPUBusyPercentTier2C_Object = MibScalar
resourceNPCPUBusyPercentTier2C = _ResourceNPCPUBusyPercentTier2C_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 15),
    _ResourceNPCPUBusyPercentTier2C_Type()
)
resourceNPCPUBusyPercentTier2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentTier2C.setStatus("current")
_ResourceNPCPUBusyPercentTier3C_Type = Integer32
_ResourceNPCPUBusyPercentTier3C_Object = MibScalar
resourceNPCPUBusyPercentTier3C = _ResourceNPCPUBusyPercentTier3C_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 16),
    _ResourceNPCPUBusyPercentTier3C_Type()
)
resourceNPCPUBusyPercentTier3C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentTier3C.setStatus("current")
_ResourceNPCPUBusyPercentTier4C_Type = Integer32
_ResourceNPCPUBusyPercentTier4C_Object = MibScalar
resourceNPCPUBusyPercentTier4C = _ResourceNPCPUBusyPercentTier4C_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 4, 17),
    _ResourceNPCPUBusyPercentTier4C_Type()
)
resourceNPCPUBusyPercentTier4C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNPCPUBusyPercentTier4C.setStatus("current")
_ResourceChassisTempObjs_ObjectIdentity = ObjectIdentity
resourceChassisTempObjs = _ResourceChassisTempObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 5)
)
if mibBuilder.loadTexts:
    resourceChassisTempObjs.setStatus("current")
_ResourceChassisTempDegreesC_Type = Integer32
_ResourceChassisTempDegreesC_Object = MibScalar
resourceChassisTempDegreesC = _ResourceChassisTempDegreesC_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 5, 1),
    _ResourceChassisTempDegreesC_Type()
)
resourceChassisTempDegreesC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceChassisTempDegreesC.setStatus("current")
_ResourceChassisTempThresholdMaj_Type = Integer32
_ResourceChassisTempThresholdMaj_Object = MibScalar
resourceChassisTempThresholdMaj = _ResourceChassisTempThresholdMaj_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 5, 2),
    _ResourceChassisTempThresholdMaj_Type()
)
resourceChassisTempThresholdMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceChassisTempThresholdMaj.setStatus("current")
_ResourceChassisTempThresholdCrit_Type = Integer32
_ResourceChassisTempThresholdCrit_Object = MibScalar
resourceChassisTempThresholdCrit = _ResourceChassisTempThresholdCrit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 5, 3),
    _ResourceChassisTempThresholdCrit_Type()
)
resourceChassisTempThresholdCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceChassisTempThresholdCrit.setStatus("current")
_ResourceChassisTempRangeMin_Type = Integer32
_ResourceChassisTempRangeMin_Object = MibScalar
resourceChassisTempRangeMin = _ResourceChassisTempRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 5, 4),
    _ResourceChassisTempRangeMin_Type()
)
resourceChassisTempRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceChassisTempRangeMin.setStatus("current")
_ResourceChassisTempRangeMax_Type = Integer32
_ResourceChassisTempRangeMax_Object = MibScalar
resourceChassisTempRangeMax = _ResourceChassisTempRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 5, 5),
    _ResourceChassisTempRangeMax_Type()
)
resourceChassisTempRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceChassisTempRangeMax.setStatus("current")


class _ResourceVersion_Type(OctetString):
    """Custom type resourceVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_ResourceVersion_Type.__name__ = "OctetString"
_ResourceVersion_Object = MibScalar
resourceVersion = _ResourceVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 6),
    _ResourceVersion_Type()
)
resourceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceVersion.setStatus("current")
_ResourceLogCountObjs_ObjectIdentity = ObjectIdentity
resourceLogCountObjs = _ResourceLogCountObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 7)
)
if mibBuilder.loadTexts:
    resourceLogCountObjs.setStatus("current")
_ResourceLogCountCritical_Type = Unsigned32
_ResourceLogCountCritical_Object = MibScalar
resourceLogCountCritical = _ResourceLogCountCritical_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 7, 1),
    _ResourceLogCountCritical_Type()
)
resourceLogCountCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceLogCountCritical.setStatus("current")
_ResourceLogCountError_Type = Unsigned32
_ResourceLogCountError_Object = MibScalar
resourceLogCountError = _ResourceLogCountError_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 7, 2),
    _ResourceLogCountError_Type()
)
resourceLogCountError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceLogCountError.setStatus("current")
_ResourceLogCountWarning_Type = Unsigned32
_ResourceLogCountWarning_Object = MibScalar
resourceLogCountWarning = _ResourceLogCountWarning_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 7, 3),
    _ResourceLogCountWarning_Type()
)
resourceLogCountWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceLogCountWarning.setStatus("current")
_ResourceLogCountInfo_Type = Unsigned32
_ResourceLogCountInfo_Object = MibScalar
resourceLogCountInfo = _ResourceLogCountInfo_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 7, 4),
    _ResourceLogCountInfo_Type()
)
resourceLogCountInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceLogCountInfo.setStatus("current")
_ResourceMetricObjs_ObjectIdentity = ObjectIdentity
resourceMetricObjs = _ResourceMetricObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 8)
)
if mibBuilder.loadTexts:
    resourceMetricObjs.setStatus("current")
_ResourceMetricFastpath_Type = Counter64
_ResourceMetricFastpath_Object = MibScalar
resourceMetricFastpath = _ResourceMetricFastpath_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 8, 1),
    _ResourceMetricFastpath_Type()
)
resourceMetricFastpath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceMetricFastpath.setStatus("current")
_ResourceMetricSmartpath_Type = Counter64
_ResourceMetricSmartpath_Object = MibScalar
resourceMetricSmartpath = _ResourceMetricSmartpath_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 8, 2),
    _ResourceMetricSmartpath_Type()
)
resourceMetricSmartpath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceMetricSmartpath.setStatus("current")
_ResourceMetricCongestion_Type = Counter64
_ResourceMetricCongestion_Object = MibScalar
resourceMetricCongestion = _ResourceMetricCongestion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 8, 3),
    _ResourceMetricCongestion_Type()
)
resourceMetricCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceMetricCongestion.setStatus("current")
_ResourcePowerSupplyObjs_ObjectIdentity = ObjectIdentity
resourcePowerSupplyObjs = _ResourcePowerSupplyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 9)
)
if mibBuilder.loadTexts:
    resourcePowerSupplyObjs.setStatus("current")
_ResourcePowerSupplyStatus_Type = ResourceState
_ResourcePowerSupplyStatus_Object = MibScalar
resourcePowerSupplyStatus = _ResourcePowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 9, 1),
    _ResourcePowerSupplyStatus_Type()
)
resourcePowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourcePowerSupplyStatus.setStatus("deprecated")
_ResourcePowerSupplyQuantity_Type = Integer32
_ResourcePowerSupplyQuantity_Object = MibScalar
resourcePowerSupplyQuantity = _ResourcePowerSupplyQuantity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 9, 2),
    _ResourcePowerSupplyQuantity_Type()
)
resourcePowerSupplyQuantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourcePowerSupplyQuantity.setStatus("current")
_ResourcePowerSupplyMonitoring_Type = Integer32
_ResourcePowerSupplyMonitoring_Object = MibScalar
resourcePowerSupplyMonitoring = _ResourcePowerSupplyMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 9, 3),
    _ResourcePowerSupplyMonitoring_Type()
)
resourcePowerSupplyMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourcePowerSupplyMonitoring.setStatus("current")
_ResourcePowerSupplyTable_Object = MibTable
resourcePowerSupplyTable = _ResourcePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 9, 4)
)
if mibBuilder.loadTexts:
    resourcePowerSupplyTable.setStatus("current")
_ResourcePowerSupplyEntry_Object = MibTableRow
resourcePowerSupplyEntry = _ResourcePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 9, 4, 1)
)
resourcePowerSupplyEntry.setIndexNames(
    (0, "TPT-RESOURCE-MIB", "powerSupplyUnitIndex"),
)
if mibBuilder.loadTexts:
    resourcePowerSupplyEntry.setStatus("current")
_PowerSupplyUnitIndex_Type = Integer32
_PowerSupplyUnitIndex_Object = MibTableColumn
powerSupplyUnitIndex = _PowerSupplyUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 9, 4, 1, 1),
    _PowerSupplyUnitIndex_Type()
)
powerSupplyUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyUnitIndex.setStatus("current")
_PowerSupplyStatus_Type = ResourceState
_PowerSupplyStatus_Object = MibTableColumn
powerSupplyStatus = _PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 9, 4, 1, 2),
    _PowerSupplyStatus_Type()
)
powerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatus.setStatus("current")
_ResourceDateTime_Type = Unsigned32
_ResourceDateTime_Object = MibScalar
resourceDateTime = _ResourceDateTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 10),
    _ResourceDateTime_Type()
)
resourceDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceDateTime.setStatus("current")
_ResourceSnmpRunState_Type = SnmpVersions
_ResourceSnmpRunState_Object = MibScalar
resourceSnmpRunState = _ResourceSnmpRunState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 11),
    _ResourceSnmpRunState_Type()
)
resourceSnmpRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceSnmpRunState.setStatus("current")
_ResourceSnmpConfig_Type = SnmpVersions
_ResourceSnmpConfig_Object = MibScalar
resourceSnmpConfig = _ResourceSnmpConfig_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 12),
    _ResourceSnmpConfig_Type()
)
resourceSnmpConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceSnmpConfig.setStatus("current")
_ResourceRemoteAuthEnabled_Type = EnabledOrNot
_ResourceRemoteAuthEnabled_Object = MibScalar
resourceRemoteAuthEnabled = _ResourceRemoteAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 13),
    _ResourceRemoteAuthEnabled_Type()
)
resourceRemoteAuthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceRemoteAuthEnabled.setStatus("current")
_ResourceRemoteAuthTimeout_Type = Integer32
_ResourceRemoteAuthTimeout_Object = MibScalar
resourceRemoteAuthTimeout = _ResourceRemoteAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 14),
    _ResourceRemoteAuthTimeout_Type()
)
resourceRemoteAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceRemoteAuthTimeout.setStatus("current")
_ResourceRemoteAuthType_Type = RemoteAuthType
_ResourceRemoteAuthType_Object = MibScalar
resourceRemoteAuthType = _ResourceRemoteAuthType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 5, 15),
    _ResourceRemoteAuthType_Type()
)
resourceRemoteAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceRemoteAuthType.setStatus("current")


class _TptResourceNotifyDeviceID_Type(OctetString):
    """Custom type tptResourceNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptResourceNotifyDeviceID_Type.__name__ = "OctetString"
_TptResourceNotifyDeviceID_Object = MibScalar
tptResourceNotifyDeviceID = _TptResourceNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 61),
    _TptResourceNotifyDeviceID_Type()
)
tptResourceNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyDeviceID.setStatus("current")
_TptResourceNotifyIdentifier_Type = ResourceIdentifier
_TptResourceNotifyIdentifier_Object = MibScalar
tptResourceNotifyIdentifier = _TptResourceNotifyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 62),
    _TptResourceNotifyIdentifier_Type()
)
tptResourceNotifyIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyIdentifier.setStatus("current")
_TptResourceNotifyFSIndex_Type = Unsigned32
_TptResourceNotifyFSIndex_Object = MibScalar
tptResourceNotifyFSIndex = _TptResourceNotifyFSIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 63),
    _TptResourceNotifyFSIndex_Type()
)
tptResourceNotifyFSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyFSIndex.setStatus("current")
_TptResourceNotifyCurrentValue_Type = Integer32
_TptResourceNotifyCurrentValue_Object = MibScalar
tptResourceNotifyCurrentValue = _TptResourceNotifyCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 64),
    _TptResourceNotifyCurrentValue_Type()
)
tptResourceNotifyCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyCurrentValue.setStatus("current")
_TptResourceNotifyThresholdMaj_Type = Integer32
_TptResourceNotifyThresholdMaj_Object = MibScalar
tptResourceNotifyThresholdMaj = _TptResourceNotifyThresholdMaj_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 65),
    _TptResourceNotifyThresholdMaj_Type()
)
tptResourceNotifyThresholdMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyThresholdMaj.setStatus("current")
_TptResourceNotifyThresholdCrit_Type = Integer32
_TptResourceNotifyThresholdCrit_Object = MibScalar
tptResourceNotifyThresholdCrit = _TptResourceNotifyThresholdCrit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 66),
    _TptResourceNotifyThresholdCrit_Type()
)
tptResourceNotifyThresholdCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyThresholdCrit.setStatus("current")
_TptResourceNotifyRangeMin_Type = Integer32
_TptResourceNotifyRangeMin_Object = MibScalar
tptResourceNotifyRangeMin = _TptResourceNotifyRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 67),
    _TptResourceNotifyRangeMin_Type()
)
tptResourceNotifyRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyRangeMin.setStatus("current")
_TptResourceNotifyRangeMax_Type = Integer32
_TptResourceNotifyRangeMax_Object = MibScalar
tptResourceNotifyRangeMax = _TptResourceNotifyRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 68),
    _TptResourceNotifyRangeMax_Type()
)
tptResourceNotifyRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyRangeMax.setStatus("current")
_TptResourceNotifyStateBefore_Type = ResourceState
_TptResourceNotifyStateBefore_Object = MibScalar
tptResourceNotifyStateBefore = _TptResourceNotifyStateBefore_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 69),
    _TptResourceNotifyStateBefore_Type()
)
tptResourceNotifyStateBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyStateBefore.setStatus("current")
_TptResourceNotifyStateAfter_Type = ResourceState
_TptResourceNotifyStateAfter_Object = MibScalar
tptResourceNotifyStateAfter = _TptResourceNotifyStateAfter_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 70),
    _TptResourceNotifyStateAfter_Type()
)
tptResourceNotifyStateAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyStateAfter.setStatus("current")
_TptResourceNotifyTimeStamp_Type = Unsigned32
_TptResourceNotifyTimeStamp_Object = MibScalar
tptResourceNotifyTimeStamp = _TptResourceNotifyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 71),
    _TptResourceNotifyTimeStamp_Type()
)
tptResourceNotifyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifyTimeStamp.setStatus("current")
_TptResourceNotifySubIdentifier_Type = Integer32
_TptResourceNotifySubIdentifier_Object = MibScalar
tptResourceNotifySubIdentifier = _TptResourceNotifySubIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 72),
    _TptResourceNotifySubIdentifier_Type()
)
tptResourceNotifySubIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptResourceNotifySubIdentifier.setStatus("current")

# Managed Objects groups


# Notification objects

tptResourceNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 14)
)
tptResourceNotify.setObjects(
      *(("TPT-RESOURCE-MIB", "tptResourceNotifyDeviceID"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifyIdentifier"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifyFSIndex"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifyCurrentValue"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifyThresholdMaj"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifyThresholdCrit"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifyRangeMin"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifyRangeMax"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifyStateBefore"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifyStateAfter"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifyTimeStamp"),
        ("TPT-RESOURCE-MIB", "tptResourceNotifySubIdentifier"))
)
if mibBuilder.loadTexts:
    tptResourceNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-RESOURCE-MIB",
    **{"ResourceIdentifier": ResourceIdentifier,
       "ResourceState": ResourceState,
       "PowerSupplyState": PowerSupplyState,
       "SnmpVersions": SnmpVersions,
       "EnabledOrNot": EnabledOrNot,
       "FilesystemState": FilesystemState,
       "RemoteAuthType": RemoteAuthType,
       "tpt-resource": tpt_resource,
       "resourceNumberOfFilesystems": resourceNumberOfFilesystems,
       "resourceFSTable": resourceFSTable,
       "resourceFSEntry": resourceFSEntry,
       "resourceFSInUseMB": resourceFSInUseMB,
       "resourceFSThresholdMaj": resourceFSThresholdMaj,
       "resourceFSThresholdCrit": resourceFSThresholdCrit,
       "resourceFSRangeMin": resourceFSRangeMin,
       "resourceFSRangeMax": resourceFSRangeMax,
       "resourceFSName": resourceFSName,
       "resourceFSIndex": resourceFSIndex,
       "resourceFSState": resourceFSState,
       "resourceFSEncryption": resourceFSEncryption,
       "resourceHPMemoryObjs": resourceHPMemoryObjs,
       "resourceHPMemoryInUsePercent": resourceHPMemoryInUsePercent,
       "resourceHPMemoryThresholdMaj": resourceHPMemoryThresholdMaj,
       "resourceHPMemoryThresholdCrit": resourceHPMemoryThresholdCrit,
       "resourceHPMemoryRangeMin": resourceHPMemoryRangeMin,
       "resourceHPMemoryRangeMax": resourceHPMemoryRangeMax,
       "resourceHPMemoryTotal": resourceHPMemoryTotal,
       "resourceHPCPUObjs": resourceHPCPUObjs,
       "resourceHPCPUBusyPercent": resourceHPCPUBusyPercent,
       "resourceHPCPUThresholdMaj": resourceHPCPUThresholdMaj,
       "resourceHPCPUThresholdCrit": resourceHPCPUThresholdCrit,
       "resourceHPCPURangeMin": resourceHPCPURangeMin,
       "resourceHPCPURangeMax": resourceHPCPURangeMax,
       "resourceNPCPUBusyPercentA": resourceNPCPUBusyPercentA,
       "resourceNPCPUBusyPercentTier2A": resourceNPCPUBusyPercentTier2A,
       "resourceNPCPUBusyPercentTier3A": resourceNPCPUBusyPercentTier3A,
       "resourceNPCPUBusyPercentTier4A": resourceNPCPUBusyPercentTier4A,
       "resourceNPCPUBusyPercentB": resourceNPCPUBusyPercentB,
       "resourceNPCPUBusyPercentTier2B": resourceNPCPUBusyPercentTier2B,
       "resourceNPCPUBusyPercentTier3B": resourceNPCPUBusyPercentTier3B,
       "resourceNPCPUBusyPercentTier4B": resourceNPCPUBusyPercentTier4B,
       "resourceNPCPUBusyPercentC": resourceNPCPUBusyPercentC,
       "resourceNPCPUBusyPercentTier2C": resourceNPCPUBusyPercentTier2C,
       "resourceNPCPUBusyPercentTier3C": resourceNPCPUBusyPercentTier3C,
       "resourceNPCPUBusyPercentTier4C": resourceNPCPUBusyPercentTier4C,
       "resourceChassisTempObjs": resourceChassisTempObjs,
       "resourceChassisTempDegreesC": resourceChassisTempDegreesC,
       "resourceChassisTempThresholdMaj": resourceChassisTempThresholdMaj,
       "resourceChassisTempThresholdCrit": resourceChassisTempThresholdCrit,
       "resourceChassisTempRangeMin": resourceChassisTempRangeMin,
       "resourceChassisTempRangeMax": resourceChassisTempRangeMax,
       "resourceVersion": resourceVersion,
       "resourceLogCountObjs": resourceLogCountObjs,
       "resourceLogCountCritical": resourceLogCountCritical,
       "resourceLogCountError": resourceLogCountError,
       "resourceLogCountWarning": resourceLogCountWarning,
       "resourceLogCountInfo": resourceLogCountInfo,
       "resourceMetricObjs": resourceMetricObjs,
       "resourceMetricFastpath": resourceMetricFastpath,
       "resourceMetricSmartpath": resourceMetricSmartpath,
       "resourceMetricCongestion": resourceMetricCongestion,
       "resourcePowerSupplyObjs": resourcePowerSupplyObjs,
       "resourcePowerSupplyStatus": resourcePowerSupplyStatus,
       "resourcePowerSupplyQuantity": resourcePowerSupplyQuantity,
       "resourcePowerSupplyMonitoring": resourcePowerSupplyMonitoring,
       "resourcePowerSupplyTable": resourcePowerSupplyTable,
       "resourcePowerSupplyEntry": resourcePowerSupplyEntry,
       "powerSupplyUnitIndex": powerSupplyUnitIndex,
       "powerSupplyStatus": powerSupplyStatus,
       "resourceDateTime": resourceDateTime,
       "resourceSnmpRunState": resourceSnmpRunState,
       "resourceSnmpConfig": resourceSnmpConfig,
       "resourceRemoteAuthEnabled": resourceRemoteAuthEnabled,
       "resourceRemoteAuthTimeout": resourceRemoteAuthTimeout,
       "resourceRemoteAuthType": resourceRemoteAuthType,
       "tptResourceNotify": tptResourceNotify,
       "tptResourceNotifyDeviceID": tptResourceNotifyDeviceID,
       "tptResourceNotifyIdentifier": tptResourceNotifyIdentifier,
       "tptResourceNotifyFSIndex": tptResourceNotifyFSIndex,
       "tptResourceNotifyCurrentValue": tptResourceNotifyCurrentValue,
       "tptResourceNotifyThresholdMaj": tptResourceNotifyThresholdMaj,
       "tptResourceNotifyThresholdCrit": tptResourceNotifyThresholdCrit,
       "tptResourceNotifyRangeMin": tptResourceNotifyRangeMin,
       "tptResourceNotifyRangeMax": tptResourceNotifyRangeMax,
       "tptResourceNotifyStateBefore": tptResourceNotifyStateBefore,
       "tptResourceNotifyStateAfter": tptResourceNotifyStateAfter,
       "tptResourceNotifyTimeStamp": tptResourceNotifyTimeStamp,
       "tptResourceNotifySubIdentifier": tptResourceNotifySubIdentifier}
)
