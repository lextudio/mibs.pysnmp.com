# SNMP MIB module (FD-PERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FD-PERFORMANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:29 2024
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

(epon,
 mediaConverter) = mibBuilder.importSymbols(
    "EPON-EOC-MIB",
    "epon",
    "mediaConverter")

(directionId,
 linkId,
 oltId) = mibBuilder.importSymbols(
    "FD-OLT-MIB",
    "directionId",
    "linkId",
    "oltId")

(onuId,
 uniPortId) = mibBuilder.importSymbols(
    "FD-ONU-MIB",
    "onuId",
    "uniPortId")

(swSniPortId,) = mibBuilder.importSymbols(
    "FD-SWITCH-MIB",
    "swSniPortId")

(ponCardSlotId,) = mibBuilder.importSymbols(
    "FD-SYSTEM-MIB",
    "ponCardSlotId")

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

performance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class StatsCollection(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 11),
          ("bcFrameTrans", 4),
          ("crc32Errors", 6),
          ("framesDropped", 9),
          ("mcFrameTrans", 5),
          ("octetTrans", 1),
          ("octetsDropped", 10),
          ("oversizeFrames", 8),
          ("totFrameTrans", 2),
          ("ucFrameTrans", 3),
          ("undersizeFrames", 7))
    )



# MIB Managed Objects in the order of their OIDs

_AlarmThreshHold_ObjectIdentity = ObjectIdentity
alarmThreshHold = _AlarmThreshHold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1)
)
_SwThresholdTable_Object = MibTable
swThresholdTable = _SwThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    swThresholdTable.setStatus("current")
_SwThresholdEntry_Object = MibTableRow
swThresholdEntry = _SwThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 1, 1)
)
swThresholdEntry.setIndexNames(
    (0, "FD-PERFORMANCE-MIB", "statsId"),
)
if mibBuilder.loadTexts:
    swThresholdEntry.setStatus("current")
_StatsId_Type = StatsCollection
_StatsId_Object = MibTableColumn
statsId = _StatsId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 1, 1, 2),
    _StatsId_Type()
)
statsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statsId.setStatus("current")
_SniPortThresholdLo_Type = Counter32
_SniPortThresholdLo_Object = MibTableColumn
sniPortThresholdLo = _SniPortThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 1, 1, 3),
    _SniPortThresholdLo_Type()
)
sniPortThresholdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniPortThresholdLo.setStatus("current")
_SniPortThresholdHi_Type = Counter32
_SniPortThresholdHi_Object = MibTableColumn
sniPortThresholdHi = _SniPortThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 1, 1, 4),
    _SniPortThresholdHi_Type()
)
sniPortThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniPortThresholdHi.setStatus("current")
_OltThresholdTable_Object = MibTable
oltThresholdTable = _OltThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    oltThresholdTable.setStatus("current")
_OltThresholdEntry_Object = MibTableRow
oltThresholdEntry = _OltThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 2, 1)
)
oltThresholdEntry.setIndexNames(
    (0, "FD-PERFORMANCE-MIB", "statsId"),
)
if mibBuilder.loadTexts:
    oltThresholdEntry.setStatus("current")
_OltThresholdLo_Type = Counter32
_OltThresholdLo_Object = MibTableColumn
oltThresholdLo = _OltThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 2, 1, 2),
    _OltThresholdLo_Type()
)
oltThresholdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltThresholdLo.setStatus("current")
_OltThresholdHi_Type = Counter32
_OltThresholdHi_Object = MibTableColumn
oltThresholdHi = _OltThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 2, 1, 3),
    _OltThresholdHi_Type()
)
oltThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltThresholdHi.setStatus("current")
_OnuUniThresholdTable_Object = MibTable
onuUniThresholdTable = _OnuUniThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    onuUniThresholdTable.setStatus("current")
_OnuUniThresholdEntry_Object = MibTableRow
onuUniThresholdEntry = _OnuUniThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 3, 1)
)
onuUniThresholdEntry.setIndexNames(
    (0, "FD-PERFORMANCE-MIB", "statsId"),
)
if mibBuilder.loadTexts:
    onuUniThresholdEntry.setStatus("current")
_OnuUniThresholdLo_Type = Counter32
_OnuUniThresholdLo_Object = MibTableColumn
onuUniThresholdLo = _OnuUniThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 3, 1, 2),
    _OnuUniThresholdLo_Type()
)
onuUniThresholdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuUniThresholdLo.setStatus("current")
_OnuUniThresholdHi_Type = Counter32
_OnuUniThresholdHi_Object = MibTableColumn
onuUniThresholdHi = _OnuUniThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 3, 1, 3),
    _OnuUniThresholdHi_Type()
)
onuUniThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuUniThresholdHi.setStatus("current")
_SwTrafficChangeTable_Object = MibTable
swTrafficChangeTable = _SwTrafficChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 4)
)
if mibBuilder.loadTexts:
    swTrafficChangeTable.setStatus("current")
_SwTrafficChangeEntry_Object = MibTableRow
swTrafficChangeEntry = _SwTrafficChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 4, 1)
)
swTrafficChangeEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "swSniPortId"),
    (0, "FD-PERFORMANCE-MIB", "statsId"),
)
if mibBuilder.loadTexts:
    swTrafficChangeEntry.setStatus("current")
_SwSniPortTrafficChangeVal_Type = Counter32
_SwSniPortTrafficChangeVal_Object = MibTableColumn
swSniPortTrafficChangeVal = _SwSniPortTrafficChangeVal_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 4, 1, 1),
    _SwSniPortTrafficChangeVal_Type()
)
swSniPortTrafficChangeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniPortTrafficChangeVal.setStatus("current")
_OltTrafficChangeTable_Object = MibTable
oltTrafficChangeTable = _OltTrafficChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 5)
)
if mibBuilder.loadTexts:
    oltTrafficChangeTable.setStatus("current")
_OltTrafficChangeEntry_Object = MibTableRow
oltTrafficChangeEntry = _OltTrafficChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 5, 1)
)
oltTrafficChangeEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-PERFORMANCE-MIB", "statsId"),
)
if mibBuilder.loadTexts:
    oltTrafficChangeEntry.setStatus("current")
_OltTrafficChangeVal_Type = Counter32
_OltTrafficChangeVal_Object = MibTableColumn
oltTrafficChangeVal = _OltTrafficChangeVal_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 5, 1, 1),
    _OltTrafficChangeVal_Type()
)
oltTrafficChangeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltTrafficChangeVal.setStatus("current")
_OnuTrafficChangeTable_Object = MibTable
onuTrafficChangeTable = _OnuTrafficChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 6)
)
if mibBuilder.loadTexts:
    onuTrafficChangeTable.setStatus("current")
_OnuTrafficChangeEntry_Object = MibTableRow
onuTrafficChangeEntry = _OnuTrafficChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 6, 1)
)
onuTrafficChangeEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
    (0, "FD-PERFORMANCE-MIB", "statsId"),
)
if mibBuilder.loadTexts:
    onuTrafficChangeEntry.setStatus("current")
_OnuTrafficChangeVal_Type = Counter32
_OnuTrafficChangeVal_Object = MibTableColumn
onuTrafficChangeVal = _OnuTrafficChangeVal_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 1, 6, 1, 1),
    _OnuTrafficChangeVal_Type()
)
onuTrafficChangeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTrafficChangeVal.setStatus("current")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2)
)
_LlidStatsTable_Object = MibTable
llidStatsTable = _LlidStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    llidStatsTable.setStatus("current")
_LlidStatsEntry_Object = MibTableRow
llidStatsEntry = _LlidStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1)
)
llidStatsEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    llidStatsEntry.setStatus("current")
_LlidOctetsTransferred_Type = Counter64
_LlidOctetsTransferred_Object = MibTableColumn
llidOctetsTransferred = _LlidOctetsTransferred_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 3),
    _LlidOctetsTransferred_Type()
)
llidOctetsTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidOctetsTransferred.setStatus("current")
_LlidTotFrameTransferred_Type = Counter64
_LlidTotFrameTransferred_Object = MibTableColumn
llidTotFrameTransferred = _LlidTotFrameTransferred_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 4),
    _LlidTotFrameTransferred_Type()
)
llidTotFrameTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidTotFrameTransferred.setStatus("current")
_LlidUniFrametransferred_Type = Counter64
_LlidUniFrametransferred_Object = MibTableColumn
llidUniFrametransferred = _LlidUniFrametransferred_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 5),
    _LlidUniFrametransferred_Type()
)
llidUniFrametransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidUniFrametransferred.setStatus("current")
_LlidBroadFrametransferred_Type = Counter64
_LlidBroadFrametransferred_Object = MibTableColumn
llidBroadFrametransferred = _LlidBroadFrametransferred_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 6),
    _LlidBroadFrametransferred_Type()
)
llidBroadFrametransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidBroadFrametransferred.setStatus("current")
_LlidMulFrametransferred_Type = Counter64
_LlidMulFrametransferred_Object = MibTableColumn
llidMulFrametransferred = _LlidMulFrametransferred_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 7),
    _LlidMulFrametransferred_Type()
)
llidMulFrametransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidMulFrametransferred.setStatus("current")
_LlidCrc32Errors_Type = Counter64
_LlidCrc32Errors_Object = MibTableColumn
llidCrc32Errors = _LlidCrc32Errors_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 8),
    _LlidCrc32Errors_Type()
)
llidCrc32Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidCrc32Errors.setStatus("current")
_LlidUndersizeFrames_Type = Counter64
_LlidUndersizeFrames_Object = MibTableColumn
llidUndersizeFrames = _LlidUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 9),
    _LlidUndersizeFrames_Type()
)
llidUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidUndersizeFrames.setStatus("current")
_LlidOversizeFrames_Type = Counter64
_LlidOversizeFrames_Object = MibTableColumn
llidOversizeFrames = _LlidOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 10),
    _LlidOversizeFrames_Type()
)
llidOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidOversizeFrames.setStatus("current")
_LlidFrom0to64OctetFrames_Type = Counter64
_LlidFrom0to64OctetFrames_Object = MibTableColumn
llidFrom0to64OctetFrames = _LlidFrom0to64OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 11),
    _LlidFrom0to64OctetFrames_Type()
)
llidFrom0to64OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidFrom0to64OctetFrames.setStatus("current")
_LlidFrom65to127OctetFrames_Type = Counter64
_LlidFrom65to127OctetFrames_Object = MibTableColumn
llidFrom65to127OctetFrames = _LlidFrom65to127OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 12),
    _LlidFrom65to127OctetFrames_Type()
)
llidFrom65to127OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidFrom65to127OctetFrames.setStatus("current")
_LlidFrom128to255OctetFrames_Type = Counter64
_LlidFrom128to255OctetFrames_Object = MibTableColumn
llidFrom128to255OctetFrames = _LlidFrom128to255OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 13),
    _LlidFrom128to255OctetFrames_Type()
)
llidFrom128to255OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidFrom128to255OctetFrames.setStatus("current")
_LlidFrom256to511OctetFrames_Type = Counter64
_LlidFrom256to511OctetFrames_Object = MibTableColumn
llidFrom256to511OctetFrames = _LlidFrom256to511OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 14),
    _LlidFrom256to511OctetFrames_Type()
)
llidFrom256to511OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidFrom256to511OctetFrames.setStatus("current")
_LlidFrom512to1023OctetFrames_Type = Counter64
_LlidFrom512to1023OctetFrames_Object = MibTableColumn
llidFrom512to1023OctetFrames = _LlidFrom512to1023OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 15),
    _LlidFrom512to1023OctetFrames_Type()
)
llidFrom512to1023OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidFrom512to1023OctetFrames.setStatus("current")
_LlidFrom1024to1518OctetFrames_Type = Counter64
_LlidFrom1024to1518OctetFrames_Object = MibTableColumn
llidFrom1024to1518OctetFrames = _LlidFrom1024to1518OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 16),
    _LlidFrom1024to1518OctetFrames_Type()
)
llidFrom1024to1518OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidFrom1024to1518OctetFrames.setStatus("current")
_LlidMore1519ctetFrames_Type = Counter64
_LlidMore1519ctetFrames_Object = MibTableColumn
llidMore1519ctetFrames = _LlidMore1519ctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 17),
    _LlidMore1519ctetFrames_Type()
)
llidMore1519ctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidMore1519ctetFrames.setStatus("current")
_LlidFramesDropped_Type = Counter64
_LlidFramesDropped_Object = MibTableColumn
llidFramesDropped = _LlidFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 18),
    _LlidFramesDropped_Type()
)
llidFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidFramesDropped.setStatus("current")
_LlidOctetsDropped_Type = Counter64
_LlidOctetsDropped_Object = MibTableColumn
llidOctetsDropped = _LlidOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 19),
    _LlidOctetsDropped_Type()
)
llidOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidOctetsDropped.setStatus("current")
_LlidOctetsDelayed_Type = Counter64
_LlidOctetsDelayed_Object = MibTableColumn
llidOctetsDelayed = _LlidOctetsDelayed_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 20),
    _LlidOctetsDelayed_Type()
)
llidOctetsDelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidOctetsDelayed.setStatus("current")
_LlidOctetsGranted_Type = Counter64
_LlidOctetsGranted_Object = MibTableColumn
llidOctetsGranted = _LlidOctetsGranted_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 21),
    _LlidOctetsGranted_Type()
)
llidOctetsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidOctetsGranted.setStatus("current")
_LlidUnusedGrantedOctets_Type = Counter64
_LlidUnusedGrantedOctets_Object = MibTableColumn
llidUnusedGrantedOctets = _LlidUnusedGrantedOctets_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 22),
    _LlidUnusedGrantedOctets_Type()
)
llidUnusedGrantedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidUnusedGrantedOctets.setStatus("current")
_LlidMaximumDelay_Type = Counter64
_LlidMaximumDelay_Object = MibTableColumn
llidMaximumDelay = _LlidMaximumDelay_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 23),
    _LlidMaximumDelay_Type()
)
llidMaximumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidMaximumDelay.setStatus("current")
_LlidLineCodeViolation_Type = Counter64
_LlidLineCodeViolation_Object = MibTableColumn
llidLineCodeViolation = _LlidLineCodeViolation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 24),
    _LlidLineCodeViolation_Type()
)
llidLineCodeViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidLineCodeViolation.setStatus("current")
_LlidErrFrameSecond_Type = Counter64
_LlidErrFrameSecond_Object = MibTableColumn
llidErrFrameSecond = _LlidErrFrameSecond_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 25),
    _LlidErrFrameSecond_Type()
)
llidErrFrameSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidErrFrameSecond.setStatus("current")
_LlidErrFramePeriod_Type = Counter64
_LlidErrFramePeriod_Object = MibTableColumn
llidErrFramePeriod = _LlidErrFramePeriod_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 26),
    _LlidErrFramePeriod_Type()
)
llidErrFramePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidErrFramePeriod.setStatus("current")
_LlidSumErrFrameSecond_Type = Counter64
_LlidSumErrFrameSecond_Object = MibTableColumn
llidSumErrFrameSecond = _LlidSumErrFrameSecond_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 27),
    _LlidSumErrFrameSecond_Type()
)
llidSumErrFrameSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidSumErrFrameSecond.setStatus("current")


class _LlidStatsOperation_Type(Integer32):
    """Custom type llidStatsOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("fresh", 1))
    )


_LlidStatsOperation_Type.__name__ = "Integer32"
_LlidStatsOperation_Object = MibTableColumn
llidStatsOperation = _LlidStatsOperation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 1, 1, 37),
    _LlidStatsOperation_Type()
)
llidStatsOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidStatsOperation.setStatus("current")
_OnuUniPortStatsTable_Object = MibTable
onuUniPortStatsTable = _OnuUniPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    onuUniPortStatsTable.setStatus("current")
_OnuUniPortStatsEntry_Object = MibTableRow
onuUniPortStatsEntry = _OnuUniPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1)
)
onuUniPortStatsEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    onuUniPortStatsEntry.setStatus("current")
_OnuUniOctetsTransferred_Type = Counter64
_OnuUniOctetsTransferred_Object = MibTableColumn
onuUniOctetsTransferred = _OnuUniOctetsTransferred_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 3),
    _OnuUniOctetsTransferred_Type()
)
onuUniOctetsTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOctetsTransferred.setStatus("current")
_OnuUniTotFrameTransferred_Type = Counter64
_OnuUniTotFrameTransferred_Object = MibTableColumn
onuUniTotFrameTransferred = _OnuUniTotFrameTransferred_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 4),
    _OnuUniTotFrameTransferred_Type()
)
onuUniTotFrameTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniTotFrameTransferred.setStatus("current")
_OnuUniUniFrametransferred_Type = Counter64
_OnuUniUniFrametransferred_Object = MibTableColumn
onuUniUniFrametransferred = _OnuUniUniFrametransferred_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 5),
    _OnuUniUniFrametransferred_Type()
)
onuUniUniFrametransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniUniFrametransferred.setStatus("current")
_OnuUniBroadFrametransferred_Type = Counter64
_OnuUniBroadFrametransferred_Object = MibTableColumn
onuUniBroadFrametransferred = _OnuUniBroadFrametransferred_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 6),
    _OnuUniBroadFrametransferred_Type()
)
onuUniBroadFrametransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniBroadFrametransferred.setStatus("current")
_OnuUniMulFrametransferred_Type = Integer32
_OnuUniMulFrametransferred_Object = MibTableColumn
onuUniMulFrametransferred = _OnuUniMulFrametransferred_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 7),
    _OnuUniMulFrametransferred_Type()
)
onuUniMulFrametransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniMulFrametransferred.setStatus("current")
_OnuUniCrc32Errors_Type = Counter64
_OnuUniCrc32Errors_Object = MibTableColumn
onuUniCrc32Errors = _OnuUniCrc32Errors_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 8),
    _OnuUniCrc32Errors_Type()
)
onuUniCrc32Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniCrc32Errors.setStatus("current")
_OnuUniUndersizeFrames_Type = Counter64
_OnuUniUndersizeFrames_Object = MibTableColumn
onuUniUndersizeFrames = _OnuUniUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 9),
    _OnuUniUndersizeFrames_Type()
)
onuUniUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniUndersizeFrames.setStatus("current")
_OnuUniOversizeFrames_Type = Counter64
_OnuUniOversizeFrames_Object = MibTableColumn
onuUniOversizeFrames = _OnuUniOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 10),
    _OnuUniOversizeFrames_Type()
)
onuUniOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOversizeFrames.setStatus("current")
_OnuUniCollosions_Type = Counter64
_OnuUniCollosions_Object = MibTableColumn
onuUniCollosions = _OnuUniCollosions_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 11),
    _OnuUniCollosions_Type()
)
onuUniCollosions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniCollosions.setStatus("current")
_OnuUniFrom0to64OctetFrames_Type = Counter64
_OnuUniFrom0to64OctetFrames_Object = MibTableColumn
onuUniFrom0to64OctetFrames = _OnuUniFrom0to64OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 12),
    _OnuUniFrom0to64OctetFrames_Type()
)
onuUniFrom0to64OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniFrom0to64OctetFrames.setStatus("current")
_OnuUniFrom65to127OctetFrames_Type = Counter64
_OnuUniFrom65to127OctetFrames_Object = MibTableColumn
onuUniFrom65to127OctetFrames = _OnuUniFrom65to127OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 13),
    _OnuUniFrom65to127OctetFrames_Type()
)
onuUniFrom65to127OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniFrom65to127OctetFrames.setStatus("current")
_OnuUniFrom128to255OctetFrames_Type = Counter64
_OnuUniFrom128to255OctetFrames_Object = MibTableColumn
onuUniFrom128to255OctetFrames = _OnuUniFrom128to255OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 14),
    _OnuUniFrom128to255OctetFrames_Type()
)
onuUniFrom128to255OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniFrom128to255OctetFrames.setStatus("current")
_OnuUniFrom256to511OctetFrames_Type = Counter64
_OnuUniFrom256to511OctetFrames_Object = MibTableColumn
onuUniFrom256to511OctetFrames = _OnuUniFrom256to511OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 15),
    _OnuUniFrom256to511OctetFrames_Type()
)
onuUniFrom256to511OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniFrom256to511OctetFrames.setStatus("current")
_OnuUniFrom512to1023OctetFrames_Type = Counter64
_OnuUniFrom512to1023OctetFrames_Object = MibTableColumn
onuUniFrom512to1023OctetFrames = _OnuUniFrom512to1023OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 16),
    _OnuUniFrom512to1023OctetFrames_Type()
)
onuUniFrom512to1023OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniFrom512to1023OctetFrames.setStatus("current")
_OnuUniFrom1024to1518OctetFrames_Type = Counter64
_OnuUniFrom1024to1518OctetFrames_Object = MibTableColumn
onuUniFrom1024to1518OctetFrames = _OnuUniFrom1024to1518OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 17),
    _OnuUniFrom1024to1518OctetFrames_Type()
)
onuUniFrom1024to1518OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniFrom1024to1518OctetFrames.setStatus("current")
_OnuUniMore1519ctetFrames_Type = Counter64
_OnuUniMore1519ctetFrames_Object = MibTableColumn
onuUniMore1519ctetFrames = _OnuUniMore1519ctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 18),
    _OnuUniMore1519ctetFrames_Type()
)
onuUniMore1519ctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniMore1519ctetFrames.setStatus("current")
_OnuUniFramesDropped_Type = Counter64
_OnuUniFramesDropped_Object = MibTableColumn
onuUniFramesDropped = _OnuUniFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 19),
    _OnuUniFramesDropped_Type()
)
onuUniFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniFramesDropped.setStatus("current")
_OnuUniOctetsDropped_Type = Counter64
_OnuUniOctetsDropped_Object = MibTableColumn
onuUniOctetsDropped = _OnuUniOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 20),
    _OnuUniOctetsDropped_Type()
)
onuUniOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOctetsDropped.setStatus("current")
_OnuUniOctetsDelayed_Type = Counter64
_OnuUniOctetsDelayed_Object = MibTableColumn
onuUniOctetsDelayed = _OnuUniOctetsDelayed_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 21),
    _OnuUniOctetsDelayed_Type()
)
onuUniOctetsDelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOctetsDelayed.setStatus("current")
_OnuUniOctetsGranted_Type = Counter64
_OnuUniOctetsGranted_Object = MibTableColumn
onuUniOctetsGranted = _OnuUniOctetsGranted_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 22),
    _OnuUniOctetsGranted_Type()
)
onuUniOctetsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOctetsGranted.setStatus("current")
_OnuUniUnusedGrantedOctets_Type = Counter64
_OnuUniUnusedGrantedOctets_Object = MibTableColumn
onuUniUnusedGrantedOctets = _OnuUniUnusedGrantedOctets_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 23),
    _OnuUniUnusedGrantedOctets_Type()
)
onuUniUnusedGrantedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniUnusedGrantedOctets.setStatus("current")
_OnuUniCrc8Errors_Type = Counter64
_OnuUniCrc8Errors_Object = MibTableColumn
onuUniCrc8Errors = _OnuUniCrc8Errors_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 24),
    _OnuUniCrc8Errors_Type()
)
onuUniCrc8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniCrc8Errors.setStatus("current")
_OnuUniPauseFrames_Type = Counter64
_OnuUniPauseFrames_Object = MibTableColumn
onuUniPauseFrames = _OnuUniPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 25),
    _OnuUniPauseFrames_Type()
)
onuUniPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniPauseFrames.setStatus("current")


class _OnuUniStatsOperation_Type(Integer32):
    """Custom type onuUniStatsOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("fresh", 1))
    )


_OnuUniStatsOperation_Type.__name__ = "Integer32"
_OnuUniStatsOperation_Object = MibTableColumn
onuUniStatsOperation = _OnuUniStatsOperation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 2, 2, 1, 35),
    _OnuUniStatsOperation_Type()
)
onuUniStatsOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuUniStatsOperation.setStatus("current")
_PerformanceMonitor_ObjectIdentity = ObjectIdentity
performanceMonitor = _PerformanceMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3)
)
_HisPerformanceMonitor_ObjectIdentity = ObjectIdentity
hisPerformanceMonitor = _HisPerformanceMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1)
)
_SwSniHisMonitorTable_Object = MibTable
swSniHisMonitorTable = _SwSniHisMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    swSniHisMonitorTable.setStatus("current")
_SwSniHisMonitorEntry_Object = MibTableRow
swSniHisMonitorEntry = _SwSniHisMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1)
)
swSniHisMonitorEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "swSniPortId"),
    (0, "FD-OLT-MIB", "directionId"),
    (0, "FD-PERFORMANCE-MIB", "swSniHisMonitorTimeSerial"),
)
if mibBuilder.loadTexts:
    swSniHisMonitorEntry.setStatus("current")


class _SwSniHisMonitorTimeSerial_Type(Integer32):
    """Custom type swSniHisMonitorTimeSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_SwSniHisMonitorTimeSerial_Type.__name__ = "Integer32"
_SwSniHisMonitorTimeSerial_Object = MibTableColumn
swSniHisMonitorTimeSerial = _SwSniHisMonitorTimeSerial_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 2),
    _SwSniHisMonitorTimeSerial_Type()
)
swSniHisMonitorTimeSerial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSniHisMonitorTimeSerial.setStatus("current")
_SwSniOctetTransHis_Type = Counter32
_SwSniOctetTransHis_Object = MibTableColumn
swSniOctetTransHis = _SwSniOctetTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 5),
    _SwSniOctetTransHis_Type()
)
swSniOctetTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniOctetTransHis.setStatus("current")
_SwSniTotalFrameTransHis_Type = Counter32
_SwSniTotalFrameTransHis_Object = MibTableColumn
swSniTotalFrameTransHis = _SwSniTotalFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 6),
    _SwSniTotalFrameTransHis_Type()
)
swSniTotalFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniTotalFrameTransHis.setStatus("current")
_SwSniUCFrameTransHis_Type = Counter32
_SwSniUCFrameTransHis_Object = MibTableColumn
swSniUCFrameTransHis = _SwSniUCFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 7),
    _SwSniUCFrameTransHis_Type()
)
swSniUCFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniUCFrameTransHis.setStatus("current")
_SwSniBCFrameTransHis_Type = Counter32
_SwSniBCFrameTransHis_Object = MibTableColumn
swSniBCFrameTransHis = _SwSniBCFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 8),
    _SwSniBCFrameTransHis_Type()
)
swSniBCFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniBCFrameTransHis.setStatus("current")
_SwSniMCFrameTransHis_Type = Counter32
_SwSniMCFrameTransHis_Object = MibTableColumn
swSniMCFrameTransHis = _SwSniMCFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 9),
    _SwSniMCFrameTransHis_Type()
)
swSniMCFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniMCFrameTransHis.setStatus("current")
_SwSniCRC32ErrorsHis_Type = Counter32
_SwSniCRC32ErrorsHis_Object = MibTableColumn
swSniCRC32ErrorsHis = _SwSniCRC32ErrorsHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 10),
    _SwSniCRC32ErrorsHis_Type()
)
swSniCRC32ErrorsHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniCRC32ErrorsHis.setStatus("current")
_SwSniUndersizeFramesHis_Type = Counter32
_SwSniUndersizeFramesHis_Object = MibTableColumn
swSniUndersizeFramesHis = _SwSniUndersizeFramesHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 11),
    _SwSniUndersizeFramesHis_Type()
)
swSniUndersizeFramesHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniUndersizeFramesHis.setStatus("current")
_SwSniOversizeFramesHis_Type = Counter32
_SwSniOversizeFramesHis_Object = MibTableColumn
swSniOversizeFramesHis = _SwSniOversizeFramesHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 12),
    _SwSniOversizeFramesHis_Type()
)
swSniOversizeFramesHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniOversizeFramesHis.setStatus("current")
_SwSniFramesDroppedHis_Type = Counter32
_SwSniFramesDroppedHis_Object = MibTableColumn
swSniFramesDroppedHis = _SwSniFramesDroppedHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 13),
    _SwSniFramesDroppedHis_Type()
)
swSniFramesDroppedHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniFramesDroppedHis.setStatus("current")
_SwSniOctetsDroppedHis_Type = Counter32
_SwSniOctetsDroppedHis_Object = MibTableColumn
swSniOctetsDroppedHis = _SwSniOctetsDroppedHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 14),
    _SwSniOctetsDroppedHis_Type()
)
swSniOctetsDroppedHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniOctetsDroppedHis.setStatus("current")
_SwSniBandwidthHis_Type = Counter32
_SwSniBandwidthHis_Object = MibTableColumn
swSniBandwidthHis = _SwSniBandwidthHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 1, 1, 15),
    _SwSniBandwidthHis_Type()
)
swSniBandwidthHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniBandwidthHis.setStatus("current")
_OltHisMonitorTable_Object = MibTable
oltHisMonitorTable = _OltHisMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    oltHisMonitorTable.setStatus("current")
_OltHisMonitorEntry_Object = MibTableRow
oltHisMonitorEntry = _OltHisMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1)
)
oltHisMonitorEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "directionId"),
    (0, "FD-PERFORMANCE-MIB", "oltHisMonitorTimeSerial"),
)
if mibBuilder.loadTexts:
    oltHisMonitorEntry.setStatus("current")


class _OltHisMonitorTimeSerial_Type(Integer32):
    """Custom type oltHisMonitorTimeSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_OltHisMonitorTimeSerial_Type.__name__ = "Integer32"
_OltHisMonitorTimeSerial_Object = MibTableColumn
oltHisMonitorTimeSerial = _OltHisMonitorTimeSerial_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 2),
    _OltHisMonitorTimeSerial_Type()
)
oltHisMonitorTimeSerial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oltHisMonitorTimeSerial.setStatus("current")
_OltOctetTransHis_Type = Counter32
_OltOctetTransHis_Object = MibTableColumn
oltOctetTransHis = _OltOctetTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 5),
    _OltOctetTransHis_Type()
)
oltOctetTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltOctetTransHis.setStatus("current")
_OltTotalFrameTransHis_Type = Counter32
_OltTotalFrameTransHis_Object = MibTableColumn
oltTotalFrameTransHis = _OltTotalFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 6),
    _OltTotalFrameTransHis_Type()
)
oltTotalFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltTotalFrameTransHis.setStatus("current")
_OltUCFrameTransHis_Type = Counter32
_OltUCFrameTransHis_Object = MibTableColumn
oltUCFrameTransHis = _OltUCFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 7),
    _OltUCFrameTransHis_Type()
)
oltUCFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltUCFrameTransHis.setStatus("current")
_OltBCFrameTransHis_Type = Counter32
_OltBCFrameTransHis_Object = MibTableColumn
oltBCFrameTransHis = _OltBCFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 8),
    _OltBCFrameTransHis_Type()
)
oltBCFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltBCFrameTransHis.setStatus("current")
_OltMCFrameTransHis_Type = Counter32
_OltMCFrameTransHis_Object = MibTableColumn
oltMCFrameTransHis = _OltMCFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 9),
    _OltMCFrameTransHis_Type()
)
oltMCFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltMCFrameTransHis.setStatus("current")
_OltCRC32ErrorsHis_Type = Counter32
_OltCRC32ErrorsHis_Object = MibTableColumn
oltCRC32ErrorsHis = _OltCRC32ErrorsHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 10),
    _OltCRC32ErrorsHis_Type()
)
oltCRC32ErrorsHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltCRC32ErrorsHis.setStatus("current")
_OltUndersizeFramesHis_Type = Counter32
_OltUndersizeFramesHis_Object = MibTableColumn
oltUndersizeFramesHis = _OltUndersizeFramesHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 11),
    _OltUndersizeFramesHis_Type()
)
oltUndersizeFramesHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltUndersizeFramesHis.setStatus("current")
_OltOversizeFramesHis_Type = Counter32
_OltOversizeFramesHis_Object = MibTableColumn
oltOversizeFramesHis = _OltOversizeFramesHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 12),
    _OltOversizeFramesHis_Type()
)
oltOversizeFramesHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltOversizeFramesHis.setStatus("current")
_OltFramesDroppedHis_Type = Counter32
_OltFramesDroppedHis_Object = MibTableColumn
oltFramesDroppedHis = _OltFramesDroppedHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 13),
    _OltFramesDroppedHis_Type()
)
oltFramesDroppedHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltFramesDroppedHis.setStatus("current")
_OltOctetsDroppedHis_Type = Counter32
_OltOctetsDroppedHis_Object = MibTableColumn
oltOctetsDroppedHis = _OltOctetsDroppedHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 14),
    _OltOctetsDroppedHis_Type()
)
oltOctetsDroppedHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltOctetsDroppedHis.setStatus("current")
_OltBandwidthHis_Type = Counter32
_OltBandwidthHis_Object = MibTableColumn
oltBandwidthHis = _OltBandwidthHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 2, 1, 15),
    _OltBandwidthHis_Type()
)
oltBandwidthHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltBandwidthHis.setStatus("current")
_OnuUniHisMonitorTable_Object = MibTable
onuUniHisMonitorTable = _OnuUniHisMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3)
)
if mibBuilder.loadTexts:
    onuUniHisMonitorTable.setStatus("current")
_OnuUniHisMonitorEntry_Object = MibTableRow
onuUniHisMonitorEntry = _OnuUniHisMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1)
)
onuUniHisMonitorEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
    (0, "FD-OLT-MIB", "directionId"),
    (0, "FD-PERFORMANCE-MIB", "onuUniHisMonitorTimeSerial"),
)
if mibBuilder.loadTexts:
    onuUniHisMonitorEntry.setStatus("current")


class _OnuUniHisMonitorTimeSerial_Type(Integer32):
    """Custom type onuUniHisMonitorTimeSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_OnuUniHisMonitorTimeSerial_Type.__name__ = "Integer32"
_OnuUniHisMonitorTimeSerial_Object = MibTableColumn
onuUniHisMonitorTimeSerial = _OnuUniHisMonitorTimeSerial_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 1),
    _OnuUniHisMonitorTimeSerial_Type()
)
onuUniHisMonitorTimeSerial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuUniHisMonitorTimeSerial.setStatus("current")
_OnuUniOctetTransHis_Type = Counter32
_OnuUniOctetTransHis_Object = MibTableColumn
onuUniOctetTransHis = _OnuUniOctetTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 5),
    _OnuUniOctetTransHis_Type()
)
onuUniOctetTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOctetTransHis.setStatus("current")
_OnuUniTotalFrameTransHis_Type = Counter32
_OnuUniTotalFrameTransHis_Object = MibTableColumn
onuUniTotalFrameTransHis = _OnuUniTotalFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 6),
    _OnuUniTotalFrameTransHis_Type()
)
onuUniTotalFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniTotalFrameTransHis.setStatus("current")
_OnuUniUCFrameTransHis_Type = Counter32
_OnuUniUCFrameTransHis_Object = MibTableColumn
onuUniUCFrameTransHis = _OnuUniUCFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 7),
    _OnuUniUCFrameTransHis_Type()
)
onuUniUCFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniUCFrameTransHis.setStatus("current")
_OnuUniBCFrameTransHis_Type = Counter32
_OnuUniBCFrameTransHis_Object = MibTableColumn
onuUniBCFrameTransHis = _OnuUniBCFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 8),
    _OnuUniBCFrameTransHis_Type()
)
onuUniBCFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniBCFrameTransHis.setStatus("current")
_OnuUniMCFrameTransHis_Type = Counter32
_OnuUniMCFrameTransHis_Object = MibTableColumn
onuUniMCFrameTransHis = _OnuUniMCFrameTransHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 9),
    _OnuUniMCFrameTransHis_Type()
)
onuUniMCFrameTransHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniMCFrameTransHis.setStatus("current")
_OnuUniCRC32ErrorsHis_Type = Counter32
_OnuUniCRC32ErrorsHis_Object = MibTableColumn
onuUniCRC32ErrorsHis = _OnuUniCRC32ErrorsHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 10),
    _OnuUniCRC32ErrorsHis_Type()
)
onuUniCRC32ErrorsHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniCRC32ErrorsHis.setStatus("current")
_OnuUniUndersizeFramesHis_Type = Counter32
_OnuUniUndersizeFramesHis_Object = MibTableColumn
onuUniUndersizeFramesHis = _OnuUniUndersizeFramesHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 11),
    _OnuUniUndersizeFramesHis_Type()
)
onuUniUndersizeFramesHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniUndersizeFramesHis.setStatus("current")
_OnuUniOversizeFramesHis_Type = Counter32
_OnuUniOversizeFramesHis_Object = MibTableColumn
onuUniOversizeFramesHis = _OnuUniOversizeFramesHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 12),
    _OnuUniOversizeFramesHis_Type()
)
onuUniOversizeFramesHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOversizeFramesHis.setStatus("current")
_OnuUniFramesDroppedHis_Type = Counter32
_OnuUniFramesDroppedHis_Object = MibTableColumn
onuUniFramesDroppedHis = _OnuUniFramesDroppedHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 13),
    _OnuUniFramesDroppedHis_Type()
)
onuUniFramesDroppedHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniFramesDroppedHis.setStatus("current")
_OnuUniOctetsDroppedHis_Type = Counter32
_OnuUniOctetsDroppedHis_Object = MibTableColumn
onuUniOctetsDroppedHis = _OnuUniOctetsDroppedHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 14),
    _OnuUniOctetsDroppedHis_Type()
)
onuUniOctetsDroppedHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOctetsDroppedHis.setStatus("current")
_OnuUniBandwidthHis_Type = Counter32
_OnuUniBandwidthHis_Object = MibTableColumn
onuUniBandwidthHis = _OnuUniBandwidthHis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 1, 3, 1, 15),
    _OnuUniBandwidthHis_Type()
)
onuUniBandwidthHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniBandwidthHis.setStatus("current")
_RealTimePerformanceMonitor_ObjectIdentity = ObjectIdentity
realTimePerformanceMonitor = _RealTimePerformanceMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2)
)
_MonitorTimeout_Type = Integer32
_MonitorTimeout_Object = MibScalar
monitorTimeout = _MonitorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 1),
    _MonitorTimeout_Type()
)
monitorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorTimeout.setStatus("current")


class _MonitorOperator_Type(Integer32):
    """Custom type monitorOperator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("monitorResultClear", 3),
          ("monitorStart", 1),
          ("monitorStop", 2))
    )


_MonitorOperator_Type.__name__ = "Integer32"
_MonitorOperator_Object = MibScalar
monitorOperator = _MonitorOperator_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 2),
    _MonitorOperator_Type()
)
monitorOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorOperator.setStatus("current")
_SwSniMonitorTable_Object = MibTable
swSniMonitorTable = _SwSniMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3)
)
if mibBuilder.loadTexts:
    swSniMonitorTable.setStatus("current")
_SwSniMonitorEntry_Object = MibTableRow
swSniMonitorEntry = _SwSniMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1)
)
swSniMonitorEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "swSniPortId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    swSniMonitorEntry.setStatus("current")
_SwSniOctetTransRel_Type = Counter64
_SwSniOctetTransRel_Object = MibTableColumn
swSniOctetTransRel = _SwSniOctetTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 5),
    _SwSniOctetTransRel_Type()
)
swSniOctetTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniOctetTransRel.setStatus("current")
_SwSniTotalFrameTransRel_Type = Counter64
_SwSniTotalFrameTransRel_Object = MibTableColumn
swSniTotalFrameTransRel = _SwSniTotalFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 6),
    _SwSniTotalFrameTransRel_Type()
)
swSniTotalFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniTotalFrameTransRel.setStatus("current")
_SwSniUCFrameTransRel_Type = Counter64
_SwSniUCFrameTransRel_Object = MibTableColumn
swSniUCFrameTransRel = _SwSniUCFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 7),
    _SwSniUCFrameTransRel_Type()
)
swSniUCFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniUCFrameTransRel.setStatus("current")
_SwSniBCFrameTransRel_Type = Counter64
_SwSniBCFrameTransRel_Object = MibTableColumn
swSniBCFrameTransRel = _SwSniBCFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 8),
    _SwSniBCFrameTransRel_Type()
)
swSniBCFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniBCFrameTransRel.setStatus("current")
_SwSniMCFrameTransRel_Type = Counter64
_SwSniMCFrameTransRel_Object = MibTableColumn
swSniMCFrameTransRel = _SwSniMCFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 9),
    _SwSniMCFrameTransRel_Type()
)
swSniMCFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniMCFrameTransRel.setStatus("current")
_SwSniCRC32ErrorsRel_Type = Counter64
_SwSniCRC32ErrorsRel_Object = MibTableColumn
swSniCRC32ErrorsRel = _SwSniCRC32ErrorsRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 10),
    _SwSniCRC32ErrorsRel_Type()
)
swSniCRC32ErrorsRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniCRC32ErrorsRel.setStatus("current")
_SwSniUndersizeFramesRel_Type = Counter64
_SwSniUndersizeFramesRel_Object = MibTableColumn
swSniUndersizeFramesRel = _SwSniUndersizeFramesRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 11),
    _SwSniUndersizeFramesRel_Type()
)
swSniUndersizeFramesRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniUndersizeFramesRel.setStatus("current")
_SwSniOversizeFramesRel_Type = Counter64
_SwSniOversizeFramesRel_Object = MibTableColumn
swSniOversizeFramesRel = _SwSniOversizeFramesRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 12),
    _SwSniOversizeFramesRel_Type()
)
swSniOversizeFramesRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniOversizeFramesRel.setStatus("current")
_SwSniFramesDroppedRel_Type = Counter64
_SwSniFramesDroppedRel_Object = MibTableColumn
swSniFramesDroppedRel = _SwSniFramesDroppedRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 13),
    _SwSniFramesDroppedRel_Type()
)
swSniFramesDroppedRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniFramesDroppedRel.setStatus("current")
_SwSniOctetsDroppedRel_Type = Counter64
_SwSniOctetsDroppedRel_Object = MibTableColumn
swSniOctetsDroppedRel = _SwSniOctetsDroppedRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 14),
    _SwSniOctetsDroppedRel_Type()
)
swSniOctetsDroppedRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniOctetsDroppedRel.setStatus("current")
_SwSniBandwidthRel_Type = Counter64
_SwSniBandwidthRel_Object = MibTableColumn
swSniBandwidthRel = _SwSniBandwidthRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 3, 1, 15),
    _SwSniBandwidthRel_Type()
)
swSniBandwidthRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniBandwidthRel.setStatus("current")
_SwSniMonitorCtrTable_Object = MibTable
swSniMonitorCtrTable = _SwSniMonitorCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 4)
)
if mibBuilder.loadTexts:
    swSniMonitorCtrTable.setStatus("current")
_SwSniMonitorCtrEntry_Object = MibTableRow
swSniMonitorCtrEntry = _SwSniMonitorCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 4, 1)
)
swSniMonitorCtrEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "swSniPortId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    swSniMonitorCtrEntry.setStatus("current")
_SwSniMonitorMap_Type = Unsigned32
_SwSniMonitorMap_Object = MibTableColumn
swSniMonitorMap = _SwSniMonitorMap_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 4, 1, 1),
    _SwSniMonitorMap_Type()
)
swSniMonitorMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSniMonitorMap.setStatus("current")
_OltMonitorTable_Object = MibTable
oltMonitorTable = _OltMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5)
)
if mibBuilder.loadTexts:
    oltMonitorTable.setStatus("current")
_OltMonitorEntry_Object = MibTableRow
oltMonitorEntry = _OltMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1)
)
oltMonitorEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    oltMonitorEntry.setStatus("current")
_OltOctetTransRel_Type = Counter64
_OltOctetTransRel_Object = MibTableColumn
oltOctetTransRel = _OltOctetTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 5),
    _OltOctetTransRel_Type()
)
oltOctetTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltOctetTransRel.setStatus("current")
_OltTotalFrameTransRel_Type = Counter64
_OltTotalFrameTransRel_Object = MibTableColumn
oltTotalFrameTransRel = _OltTotalFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 6),
    _OltTotalFrameTransRel_Type()
)
oltTotalFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltTotalFrameTransRel.setStatus("current")
_OltUCFrameTransRel_Type = Counter64
_OltUCFrameTransRel_Object = MibTableColumn
oltUCFrameTransRel = _OltUCFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 7),
    _OltUCFrameTransRel_Type()
)
oltUCFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltUCFrameTransRel.setStatus("current")
_OltBCFrameTransRel_Type = Counter64
_OltBCFrameTransRel_Object = MibTableColumn
oltBCFrameTransRel = _OltBCFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 8),
    _OltBCFrameTransRel_Type()
)
oltBCFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltBCFrameTransRel.setStatus("current")
_OltMCFrameTransRel_Type = Counter64
_OltMCFrameTransRel_Object = MibTableColumn
oltMCFrameTransRel = _OltMCFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 9),
    _OltMCFrameTransRel_Type()
)
oltMCFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltMCFrameTransRel.setStatus("current")
_OltCRC32ErrorsRel_Type = Counter64
_OltCRC32ErrorsRel_Object = MibTableColumn
oltCRC32ErrorsRel = _OltCRC32ErrorsRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 10),
    _OltCRC32ErrorsRel_Type()
)
oltCRC32ErrorsRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltCRC32ErrorsRel.setStatus("current")
_OltUndersizeFramesRel_Type = Counter64
_OltUndersizeFramesRel_Object = MibTableColumn
oltUndersizeFramesRel = _OltUndersizeFramesRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 11),
    _OltUndersizeFramesRel_Type()
)
oltUndersizeFramesRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltUndersizeFramesRel.setStatus("current")
_OltOversizeFramesRel_Type = Counter64
_OltOversizeFramesRel_Object = MibTableColumn
oltOversizeFramesRel = _OltOversizeFramesRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 12),
    _OltOversizeFramesRel_Type()
)
oltOversizeFramesRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltOversizeFramesRel.setStatus("current")
_OltFramesDroppedRel_Type = Counter64
_OltFramesDroppedRel_Object = MibTableColumn
oltFramesDroppedRel = _OltFramesDroppedRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 13),
    _OltFramesDroppedRel_Type()
)
oltFramesDroppedRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltFramesDroppedRel.setStatus("current")
_OltOctetsDroppedRel_Type = Counter64
_OltOctetsDroppedRel_Object = MibTableColumn
oltOctetsDroppedRel = _OltOctetsDroppedRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 14),
    _OltOctetsDroppedRel_Type()
)
oltOctetsDroppedRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltOctetsDroppedRel.setStatus("current")
_OltBandwidthRel_Type = Counter64
_OltBandwidthRel_Object = MibTableColumn
oltBandwidthRel = _OltBandwidthRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 5, 1, 15),
    _OltBandwidthRel_Type()
)
oltBandwidthRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltBandwidthRel.setStatus("current")
_OltMonitorCtrTable_Object = MibTable
oltMonitorCtrTable = _OltMonitorCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 6)
)
if mibBuilder.loadTexts:
    oltMonitorCtrTable.setStatus("current")
_OltMonitorCtrEntry_Object = MibTableRow
oltMonitorCtrEntry = _OltMonitorCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 6, 1)
)
oltMonitorCtrEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    oltMonitorCtrEntry.setStatus("current")
_OltMonitorMap_Type = Unsigned32
_OltMonitorMap_Object = MibTableColumn
oltMonitorMap = _OltMonitorMap_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 6, 1, 1),
    _OltMonitorMap_Type()
)
oltMonitorMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltMonitorMap.setStatus("current")
_OnuUniMonitorTable_Object = MibTable
onuUniMonitorTable = _OnuUniMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7)
)
if mibBuilder.loadTexts:
    onuUniMonitorTable.setStatus("current")
_OnuUniMonitorEntry_Object = MibTableRow
onuUniMonitorEntry = _OnuUniMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1)
)
onuUniMonitorEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    onuUniMonitorEntry.setStatus("current")
_OnuUniOctetTransRel_Type = Counter64
_OnuUniOctetTransRel_Object = MibTableColumn
onuUniOctetTransRel = _OnuUniOctetTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 5),
    _OnuUniOctetTransRel_Type()
)
onuUniOctetTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOctetTransRel.setStatus("current")
_OnuUniTotalFrameTransRel_Type = Counter64
_OnuUniTotalFrameTransRel_Object = MibTableColumn
onuUniTotalFrameTransRel = _OnuUniTotalFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 6),
    _OnuUniTotalFrameTransRel_Type()
)
onuUniTotalFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniTotalFrameTransRel.setStatus("current")
_OnuUniUCFrameTransRel_Type = Counter64
_OnuUniUCFrameTransRel_Object = MibTableColumn
onuUniUCFrameTransRel = _OnuUniUCFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 7),
    _OnuUniUCFrameTransRel_Type()
)
onuUniUCFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniUCFrameTransRel.setStatus("current")
_OnuUniBCFrameTransRel_Type = Counter64
_OnuUniBCFrameTransRel_Object = MibTableColumn
onuUniBCFrameTransRel = _OnuUniBCFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 8),
    _OnuUniBCFrameTransRel_Type()
)
onuUniBCFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniBCFrameTransRel.setStatus("current")
_OnuUniMCFrameTransRel_Type = Counter64
_OnuUniMCFrameTransRel_Object = MibTableColumn
onuUniMCFrameTransRel = _OnuUniMCFrameTransRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 9),
    _OnuUniMCFrameTransRel_Type()
)
onuUniMCFrameTransRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniMCFrameTransRel.setStatus("current")
_OnuUniCRC32ErrorsRel_Type = Counter64
_OnuUniCRC32ErrorsRel_Object = MibTableColumn
onuUniCRC32ErrorsRel = _OnuUniCRC32ErrorsRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 10),
    _OnuUniCRC32ErrorsRel_Type()
)
onuUniCRC32ErrorsRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniCRC32ErrorsRel.setStatus("current")
_OnuUniUndersizeRel_Type = Counter64
_OnuUniUndersizeRel_Object = MibTableColumn
onuUniUndersizeRel = _OnuUniUndersizeRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 11),
    _OnuUniUndersizeRel_Type()
)
onuUniUndersizeRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniUndersizeRel.setStatus("current")
_OnuUniOversizeFramesRel_Type = Counter64
_OnuUniOversizeFramesRel_Object = MibTableColumn
onuUniOversizeFramesRel = _OnuUniOversizeFramesRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 12),
    _OnuUniOversizeFramesRel_Type()
)
onuUniOversizeFramesRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOversizeFramesRel.setStatus("current")
_OnuUniFramesDroppedRel_Type = Counter64
_OnuUniFramesDroppedRel_Object = MibTableColumn
onuUniFramesDroppedRel = _OnuUniFramesDroppedRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 13),
    _OnuUniFramesDroppedRel_Type()
)
onuUniFramesDroppedRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniFramesDroppedRel.setStatus("current")
_OnuUniOctetsDroppedRel_Type = Counter64
_OnuUniOctetsDroppedRel_Object = MibTableColumn
onuUniOctetsDroppedRel = _OnuUniOctetsDroppedRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 14),
    _OnuUniOctetsDroppedRel_Type()
)
onuUniOctetsDroppedRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniOctetsDroppedRel.setStatus("current")
_OnuUniBandwidthRel_Type = Counter64
_OnuUniBandwidthRel_Object = MibTableColumn
onuUniBandwidthRel = _OnuUniBandwidthRel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 7, 1, 15),
    _OnuUniBandwidthRel_Type()
)
onuUniBandwidthRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUniBandwidthRel.setStatus("current")
_OnuUniMonitorCtrTable_Object = MibTable
onuUniMonitorCtrTable = _OnuUniMonitorCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 8)
)
if mibBuilder.loadTexts:
    onuUniMonitorCtrTable.setStatus("current")
_OnuUniMonitorCtrEntry_Object = MibTableRow
onuUniMonitorCtrEntry = _OnuUniMonitorCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 8, 1)
)
onuUniMonitorCtrEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    onuUniMonitorCtrEntry.setStatus("current")
_OnuUniMonitorMap_Type = Unsigned32
_OnuUniMonitorMap_Object = MibTableColumn
onuUniMonitorMap = _OnuUniMonitorMap_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 3, 2, 8, 1, 1),
    _OnuUniMonitorMap_Type()
)
onuUniMonitorMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuUniMonitorMap.setStatus("current")
_PerformanceConform_ObjectIdentity = ObjectIdentity
performanceConform = _PerformanceConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6)
)
_PerformanceGroups_ObjectIdentity = ObjectIdentity
performanceGroups = _PerformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1)
)
_PerformanceCompliances_ObjectIdentity = ObjectIdentity
performanceCompliances = _PerformanceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 2)
)

# Managed Objects groups

alarmThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1, 1)
)
alarmThresholdGroup.setObjects(
      *(("FD-PERFORMANCE-MIB", "sniPortThresholdLo"),
        ("FD-PERFORMANCE-MIB", "sniPortThresholdHi"),
        ("FD-PERFORMANCE-MIB", "swSniPortTrafficChangeVal"),
        ("FD-PERFORMANCE-MIB", "oltThresholdLo"),
        ("FD-PERFORMANCE-MIB", "oltThresholdHi"),
        ("FD-PERFORMANCE-MIB", "oltTrafficChangeVal"),
        ("FD-PERFORMANCE-MIB", "onuUniThresholdLo"),
        ("FD-PERFORMANCE-MIB", "onuUniThresholdHi"),
        ("FD-PERFORMANCE-MIB", "onuTrafficChangeVal"))
)
if mibBuilder.loadTexts:
    alarmThresholdGroup.setStatus("current")

fdOltStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1, 2)
)
fdOltStatsGroup.setObjects(
      *(("FD-PERFORMANCE-MIB", "llidOctetsTransferred"),
        ("FD-PERFORMANCE-MIB", "llidTotFrameTransferred"),
        ("FD-PERFORMANCE-MIB", "llidUniFrametransferred"),
        ("FD-PERFORMANCE-MIB", "llidBroadFrametransferred"),
        ("FD-PERFORMANCE-MIB", "llidMulFrametransferred"),
        ("FD-PERFORMANCE-MIB", "llidCrc32Errors"),
        ("FD-PERFORMANCE-MIB", "llidUndersizeFrames"),
        ("FD-PERFORMANCE-MIB", "llidOversizeFrames"),
        ("FD-PERFORMANCE-MIB", "llidFrom0to64OctetFrames"),
        ("FD-PERFORMANCE-MIB", "llidFrom65to127OctetFrames"),
        ("FD-PERFORMANCE-MIB", "llidFrom128to255OctetFrames"),
        ("FD-PERFORMANCE-MIB", "llidFrom256to511OctetFrames"),
        ("FD-PERFORMANCE-MIB", "llidFrom512to1023OctetFrames"),
        ("FD-PERFORMANCE-MIB", "llidFrom1024to1518OctetFrames"),
        ("FD-PERFORMANCE-MIB", "llidMore1519ctetFrames"),
        ("FD-PERFORMANCE-MIB", "llidFramesDropped"),
        ("FD-PERFORMANCE-MIB", "llidOctetsDropped"),
        ("FD-PERFORMANCE-MIB", "llidOctetsDelayed"),
        ("FD-PERFORMANCE-MIB", "llidOctetsGranted"),
        ("FD-PERFORMANCE-MIB", "llidUnusedGrantedOctets"),
        ("FD-PERFORMANCE-MIB", "llidMaximumDelay"),
        ("FD-PERFORMANCE-MIB", "llidLineCodeViolation"),
        ("FD-PERFORMANCE-MIB", "llidErrFrameSecond"),
        ("FD-PERFORMANCE-MIB", "llidErrFramePeriod"),
        ("FD-PERFORMANCE-MIB", "llidSumErrFrameSecond"),
        ("FD-PERFORMANCE-MIB", "llidStatsOperation"))
)
if mibBuilder.loadTexts:
    fdOltStatsGroup.setStatus("current")

fdOnuStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1, 3)
)
fdOnuStatsGroup.setObjects(
      *(("FD-PERFORMANCE-MIB", "onuUniOctetsTransferred"),
        ("FD-PERFORMANCE-MIB", "onuUniTotFrameTransferred"),
        ("FD-PERFORMANCE-MIB", "onuUniUniFrametransferred"),
        ("FD-PERFORMANCE-MIB", "onuUniBroadFrametransferred"),
        ("FD-PERFORMANCE-MIB", "onuUniMulFrametransferred"),
        ("FD-PERFORMANCE-MIB", "onuUniCrc32Errors"),
        ("FD-PERFORMANCE-MIB", "onuUniUndersizeFrames"),
        ("FD-PERFORMANCE-MIB", "onuUniOversizeFrames"),
        ("FD-PERFORMANCE-MIB", "onuUniCollosions"),
        ("FD-PERFORMANCE-MIB", "onuUniFrom0to64OctetFrames"),
        ("FD-PERFORMANCE-MIB", "onuUniFrom65to127OctetFrames"),
        ("FD-PERFORMANCE-MIB", "onuUniFrom128to255OctetFrames"),
        ("FD-PERFORMANCE-MIB", "onuUniFrom256to511OctetFrames"),
        ("FD-PERFORMANCE-MIB", "onuUniFrom512to1023OctetFrames"),
        ("FD-PERFORMANCE-MIB", "onuUniFrom1024to1518OctetFrames"),
        ("FD-PERFORMANCE-MIB", "onuUniMore1519ctetFrames"),
        ("FD-PERFORMANCE-MIB", "onuUniFramesDropped"),
        ("FD-PERFORMANCE-MIB", "onuUniOctetsDropped"),
        ("FD-PERFORMANCE-MIB", "onuUniOctetsDelayed"),
        ("FD-PERFORMANCE-MIB", "onuUniOctetsGranted"),
        ("FD-PERFORMANCE-MIB", "onuUniUnusedGrantedOctets"),
        ("FD-PERFORMANCE-MIB", "onuUniCrc8Errors"),
        ("FD-PERFORMANCE-MIB", "onuUniPauseFrames"),
        ("FD-PERFORMANCE-MIB", "onuUniStatsOperation"))
)
if mibBuilder.loadTexts:
    fdOnuStatsGroup.setStatus("current")

swHisMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1, 4)
)
swHisMonitorGroup.setObjects(
      *(("FD-PERFORMANCE-MIB", "swSniOctetTransHis"),
        ("FD-PERFORMANCE-MIB", "swSniTotalFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "swSniUCFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "swSniBCFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "swSniMCFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "swSniCRC32ErrorsHis"),
        ("FD-PERFORMANCE-MIB", "swSniUndersizeFramesHis"),
        ("FD-PERFORMANCE-MIB", "swSniOversizeFramesHis"),
        ("FD-PERFORMANCE-MIB", "swSniFramesDroppedHis"),
        ("FD-PERFORMANCE-MIB", "swSniOctetsDroppedHis"),
        ("FD-PERFORMANCE-MIB", "swSniBandwidthHis"))
)
if mibBuilder.loadTexts:
    swHisMonitorGroup.setStatus("current")

oltHisMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1, 5)
)
oltHisMonitorGroup.setObjects(
      *(("FD-PERFORMANCE-MIB", "oltOctetTransHis"),
        ("FD-PERFORMANCE-MIB", "oltTotalFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "oltUCFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "oltBCFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "oltMCFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "oltCRC32ErrorsHis"),
        ("FD-PERFORMANCE-MIB", "oltUndersizeFramesHis"),
        ("FD-PERFORMANCE-MIB", "oltOversizeFramesHis"),
        ("FD-PERFORMANCE-MIB", "oltFramesDroppedHis"),
        ("FD-PERFORMANCE-MIB", "oltOctetsDroppedHis"),
        ("FD-PERFORMANCE-MIB", "oltBandwidthHis"))
)
if mibBuilder.loadTexts:
    oltHisMonitorGroup.setStatus("current")

onuHisMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1, 6)
)
onuHisMonitorGroup.setObjects(
      *(("FD-PERFORMANCE-MIB", "onuUniOctetTransHis"),
        ("FD-PERFORMANCE-MIB", "onuUniTotalFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "onuUniUCFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "onuUniBCFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "onuUniMCFrameTransHis"),
        ("FD-PERFORMANCE-MIB", "onuUniCRC32ErrorsHis"),
        ("FD-PERFORMANCE-MIB", "onuUniUndersizeFramesHis"),
        ("FD-PERFORMANCE-MIB", "onuUniOversizeFramesHis"),
        ("FD-PERFORMANCE-MIB", "onuUniFramesDroppedHis"),
        ("FD-PERFORMANCE-MIB", "onuUniOctetsDroppedHis"),
        ("FD-PERFORMANCE-MIB", "onuUniBandwidthHis"))
)
if mibBuilder.loadTexts:
    onuHisMonitorGroup.setStatus("current")

swRelMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1, 7)
)
swRelMonitorGroup.setObjects(
      *(("FD-PERFORMANCE-MIB", "swSniOctetTransRel"),
        ("FD-PERFORMANCE-MIB", "swSniTotalFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "swSniUCFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "swSniBCFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "swSniMCFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "swSniCRC32ErrorsRel"),
        ("FD-PERFORMANCE-MIB", "swSniUndersizeFramesRel"),
        ("FD-PERFORMANCE-MIB", "swSniOversizeFramesRel"),
        ("FD-PERFORMANCE-MIB", "swSniFramesDroppedRel"),
        ("FD-PERFORMANCE-MIB", "swSniOctetsDroppedRel"),
        ("FD-PERFORMANCE-MIB", "swSniBandwidthRel"))
)
if mibBuilder.loadTexts:
    swRelMonitorGroup.setStatus("current")

oltRelMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1, 8)
)
oltRelMonitorGroup.setObjects(
      *(("FD-PERFORMANCE-MIB", "oltOctetTransRel"),
        ("FD-PERFORMANCE-MIB", "oltTotalFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "oltUCFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "oltBCFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "oltMCFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "oltCRC32ErrorsRel"),
        ("FD-PERFORMANCE-MIB", "oltUndersizeFramesRel"),
        ("FD-PERFORMANCE-MIB", "oltOversizeFramesRel"),
        ("FD-PERFORMANCE-MIB", "oltFramesDroppedRel"),
        ("FD-PERFORMANCE-MIB", "oltOctetsDroppedRel"),
        ("FD-PERFORMANCE-MIB", "oltBandwidthRel"))
)
if mibBuilder.loadTexts:
    oltRelMonitorGroup.setStatus("current")

onuRelMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1, 9)
)
onuRelMonitorGroup.setObjects(
      *(("FD-PERFORMANCE-MIB", "onuUniOctetTransRel"),
        ("FD-PERFORMANCE-MIB", "onuUniTotalFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "onuUniUCFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "onuUniBCFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "onuUniMCFrameTransRel"),
        ("FD-PERFORMANCE-MIB", "onuUniCRC32ErrorsRel"),
        ("FD-PERFORMANCE-MIB", "onuUniUndersizeRel"),
        ("FD-PERFORMANCE-MIB", "onuUniOversizeFramesRel"),
        ("FD-PERFORMANCE-MIB", "onuUniFramesDroppedRel"),
        ("FD-PERFORMANCE-MIB", "onuUniOctetsDroppedRel"),
        ("FD-PERFORMANCE-MIB", "onuUniBandwidthRel"))
)
if mibBuilder.loadTexts:
    onuRelMonitorGroup.setStatus("current")

monitorMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 1, 10)
)
monitorMapGroup.setObjects(
      *(("FD-PERFORMANCE-MIB", "onuUniMonitorMap"),
        ("FD-PERFORMANCE-MIB", "monitorTimeout"),
        ("FD-PERFORMANCE-MIB", "monitorOperator"),
        ("FD-PERFORMANCE-MIB", "oltMonitorMap"),
        ("FD-PERFORMANCE-MIB", "swSniMonitorMap"))
)
if mibBuilder.loadTexts:
    monitorMapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

performanceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 5, 6, 2, 1)
)
if mibBuilder.loadTexts:
    performanceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FD-PERFORMANCE-MIB",
    **{"StatsCollection": StatsCollection,
       "performance": performance,
       "alarmThreshHold": alarmThreshHold,
       "swThresholdTable": swThresholdTable,
       "swThresholdEntry": swThresholdEntry,
       "statsId": statsId,
       "sniPortThresholdLo": sniPortThresholdLo,
       "sniPortThresholdHi": sniPortThresholdHi,
       "oltThresholdTable": oltThresholdTable,
       "oltThresholdEntry": oltThresholdEntry,
       "oltThresholdLo": oltThresholdLo,
       "oltThresholdHi": oltThresholdHi,
       "onuUniThresholdTable": onuUniThresholdTable,
       "onuUniThresholdEntry": onuUniThresholdEntry,
       "onuUniThresholdLo": onuUniThresholdLo,
       "onuUniThresholdHi": onuUniThresholdHi,
       "swTrafficChangeTable": swTrafficChangeTable,
       "swTrafficChangeEntry": swTrafficChangeEntry,
       "swSniPortTrafficChangeVal": swSniPortTrafficChangeVal,
       "oltTrafficChangeTable": oltTrafficChangeTable,
       "oltTrafficChangeEntry": oltTrafficChangeEntry,
       "oltTrafficChangeVal": oltTrafficChangeVal,
       "onuTrafficChangeTable": onuTrafficChangeTable,
       "onuTrafficChangeEntry": onuTrafficChangeEntry,
       "onuTrafficChangeVal": onuTrafficChangeVal,
       "statistics": statistics,
       "llidStatsTable": llidStatsTable,
       "llidStatsEntry": llidStatsEntry,
       "llidOctetsTransferred": llidOctetsTransferred,
       "llidTotFrameTransferred": llidTotFrameTransferred,
       "llidUniFrametransferred": llidUniFrametransferred,
       "llidBroadFrametransferred": llidBroadFrametransferred,
       "llidMulFrametransferred": llidMulFrametransferred,
       "llidCrc32Errors": llidCrc32Errors,
       "llidUndersizeFrames": llidUndersizeFrames,
       "llidOversizeFrames": llidOversizeFrames,
       "llidFrom0to64OctetFrames": llidFrom0to64OctetFrames,
       "llidFrom65to127OctetFrames": llidFrom65to127OctetFrames,
       "llidFrom128to255OctetFrames": llidFrom128to255OctetFrames,
       "llidFrom256to511OctetFrames": llidFrom256to511OctetFrames,
       "llidFrom512to1023OctetFrames": llidFrom512to1023OctetFrames,
       "llidFrom1024to1518OctetFrames": llidFrom1024to1518OctetFrames,
       "llidMore1519ctetFrames": llidMore1519ctetFrames,
       "llidFramesDropped": llidFramesDropped,
       "llidOctetsDropped": llidOctetsDropped,
       "llidOctetsDelayed": llidOctetsDelayed,
       "llidOctetsGranted": llidOctetsGranted,
       "llidUnusedGrantedOctets": llidUnusedGrantedOctets,
       "llidMaximumDelay": llidMaximumDelay,
       "llidLineCodeViolation": llidLineCodeViolation,
       "llidErrFrameSecond": llidErrFrameSecond,
       "llidErrFramePeriod": llidErrFramePeriod,
       "llidSumErrFrameSecond": llidSumErrFrameSecond,
       "llidStatsOperation": llidStatsOperation,
       "onuUniPortStatsTable": onuUniPortStatsTable,
       "onuUniPortStatsEntry": onuUniPortStatsEntry,
       "onuUniOctetsTransferred": onuUniOctetsTransferred,
       "onuUniTotFrameTransferred": onuUniTotFrameTransferred,
       "onuUniUniFrametransferred": onuUniUniFrametransferred,
       "onuUniBroadFrametransferred": onuUniBroadFrametransferred,
       "onuUniMulFrametransferred": onuUniMulFrametransferred,
       "onuUniCrc32Errors": onuUniCrc32Errors,
       "onuUniUndersizeFrames": onuUniUndersizeFrames,
       "onuUniOversizeFrames": onuUniOversizeFrames,
       "onuUniCollosions": onuUniCollosions,
       "onuUniFrom0to64OctetFrames": onuUniFrom0to64OctetFrames,
       "onuUniFrom65to127OctetFrames": onuUniFrom65to127OctetFrames,
       "onuUniFrom128to255OctetFrames": onuUniFrom128to255OctetFrames,
       "onuUniFrom256to511OctetFrames": onuUniFrom256to511OctetFrames,
       "onuUniFrom512to1023OctetFrames": onuUniFrom512to1023OctetFrames,
       "onuUniFrom1024to1518OctetFrames": onuUniFrom1024to1518OctetFrames,
       "onuUniMore1519ctetFrames": onuUniMore1519ctetFrames,
       "onuUniFramesDropped": onuUniFramesDropped,
       "onuUniOctetsDropped": onuUniOctetsDropped,
       "onuUniOctetsDelayed": onuUniOctetsDelayed,
       "onuUniOctetsGranted": onuUniOctetsGranted,
       "onuUniUnusedGrantedOctets": onuUniUnusedGrantedOctets,
       "onuUniCrc8Errors": onuUniCrc8Errors,
       "onuUniPauseFrames": onuUniPauseFrames,
       "onuUniStatsOperation": onuUniStatsOperation,
       "performanceMonitor": performanceMonitor,
       "hisPerformanceMonitor": hisPerformanceMonitor,
       "swSniHisMonitorTable": swSniHisMonitorTable,
       "swSniHisMonitorEntry": swSniHisMonitorEntry,
       "swSniHisMonitorTimeSerial": swSniHisMonitorTimeSerial,
       "swSniOctetTransHis": swSniOctetTransHis,
       "swSniTotalFrameTransHis": swSniTotalFrameTransHis,
       "swSniUCFrameTransHis": swSniUCFrameTransHis,
       "swSniBCFrameTransHis": swSniBCFrameTransHis,
       "swSniMCFrameTransHis": swSniMCFrameTransHis,
       "swSniCRC32ErrorsHis": swSniCRC32ErrorsHis,
       "swSniUndersizeFramesHis": swSniUndersizeFramesHis,
       "swSniOversizeFramesHis": swSniOversizeFramesHis,
       "swSniFramesDroppedHis": swSniFramesDroppedHis,
       "swSniOctetsDroppedHis": swSniOctetsDroppedHis,
       "swSniBandwidthHis": swSniBandwidthHis,
       "oltHisMonitorTable": oltHisMonitorTable,
       "oltHisMonitorEntry": oltHisMonitorEntry,
       "oltHisMonitorTimeSerial": oltHisMonitorTimeSerial,
       "oltOctetTransHis": oltOctetTransHis,
       "oltTotalFrameTransHis": oltTotalFrameTransHis,
       "oltUCFrameTransHis": oltUCFrameTransHis,
       "oltBCFrameTransHis": oltBCFrameTransHis,
       "oltMCFrameTransHis": oltMCFrameTransHis,
       "oltCRC32ErrorsHis": oltCRC32ErrorsHis,
       "oltUndersizeFramesHis": oltUndersizeFramesHis,
       "oltOversizeFramesHis": oltOversizeFramesHis,
       "oltFramesDroppedHis": oltFramesDroppedHis,
       "oltOctetsDroppedHis": oltOctetsDroppedHis,
       "oltBandwidthHis": oltBandwidthHis,
       "onuUniHisMonitorTable": onuUniHisMonitorTable,
       "onuUniHisMonitorEntry": onuUniHisMonitorEntry,
       "onuUniHisMonitorTimeSerial": onuUniHisMonitorTimeSerial,
       "onuUniOctetTransHis": onuUniOctetTransHis,
       "onuUniTotalFrameTransHis": onuUniTotalFrameTransHis,
       "onuUniUCFrameTransHis": onuUniUCFrameTransHis,
       "onuUniBCFrameTransHis": onuUniBCFrameTransHis,
       "onuUniMCFrameTransHis": onuUniMCFrameTransHis,
       "onuUniCRC32ErrorsHis": onuUniCRC32ErrorsHis,
       "onuUniUndersizeFramesHis": onuUniUndersizeFramesHis,
       "onuUniOversizeFramesHis": onuUniOversizeFramesHis,
       "onuUniFramesDroppedHis": onuUniFramesDroppedHis,
       "onuUniOctetsDroppedHis": onuUniOctetsDroppedHis,
       "onuUniBandwidthHis": onuUniBandwidthHis,
       "realTimePerformanceMonitor": realTimePerformanceMonitor,
       "monitorTimeout": monitorTimeout,
       "monitorOperator": monitorOperator,
       "swSniMonitorTable": swSniMonitorTable,
       "swSniMonitorEntry": swSniMonitorEntry,
       "swSniOctetTransRel": swSniOctetTransRel,
       "swSniTotalFrameTransRel": swSniTotalFrameTransRel,
       "swSniUCFrameTransRel": swSniUCFrameTransRel,
       "swSniBCFrameTransRel": swSniBCFrameTransRel,
       "swSniMCFrameTransRel": swSniMCFrameTransRel,
       "swSniCRC32ErrorsRel": swSniCRC32ErrorsRel,
       "swSniUndersizeFramesRel": swSniUndersizeFramesRel,
       "swSniOversizeFramesRel": swSniOversizeFramesRel,
       "swSniFramesDroppedRel": swSniFramesDroppedRel,
       "swSniOctetsDroppedRel": swSniOctetsDroppedRel,
       "swSniBandwidthRel": swSniBandwidthRel,
       "swSniMonitorCtrTable": swSniMonitorCtrTable,
       "swSniMonitorCtrEntry": swSniMonitorCtrEntry,
       "swSniMonitorMap": swSniMonitorMap,
       "oltMonitorTable": oltMonitorTable,
       "oltMonitorEntry": oltMonitorEntry,
       "oltOctetTransRel": oltOctetTransRel,
       "oltTotalFrameTransRel": oltTotalFrameTransRel,
       "oltUCFrameTransRel": oltUCFrameTransRel,
       "oltBCFrameTransRel": oltBCFrameTransRel,
       "oltMCFrameTransRel": oltMCFrameTransRel,
       "oltCRC32ErrorsRel": oltCRC32ErrorsRel,
       "oltUndersizeFramesRel": oltUndersizeFramesRel,
       "oltOversizeFramesRel": oltOversizeFramesRel,
       "oltFramesDroppedRel": oltFramesDroppedRel,
       "oltOctetsDroppedRel": oltOctetsDroppedRel,
       "oltBandwidthRel": oltBandwidthRel,
       "oltMonitorCtrTable": oltMonitorCtrTable,
       "oltMonitorCtrEntry": oltMonitorCtrEntry,
       "oltMonitorMap": oltMonitorMap,
       "onuUniMonitorTable": onuUniMonitorTable,
       "onuUniMonitorEntry": onuUniMonitorEntry,
       "onuUniOctetTransRel": onuUniOctetTransRel,
       "onuUniTotalFrameTransRel": onuUniTotalFrameTransRel,
       "onuUniUCFrameTransRel": onuUniUCFrameTransRel,
       "onuUniBCFrameTransRel": onuUniBCFrameTransRel,
       "onuUniMCFrameTransRel": onuUniMCFrameTransRel,
       "onuUniCRC32ErrorsRel": onuUniCRC32ErrorsRel,
       "onuUniUndersizeRel": onuUniUndersizeRel,
       "onuUniOversizeFramesRel": onuUniOversizeFramesRel,
       "onuUniFramesDroppedRel": onuUniFramesDroppedRel,
       "onuUniOctetsDroppedRel": onuUniOctetsDroppedRel,
       "onuUniBandwidthRel": onuUniBandwidthRel,
       "onuUniMonitorCtrTable": onuUniMonitorCtrTable,
       "onuUniMonitorCtrEntry": onuUniMonitorCtrEntry,
       "onuUniMonitorMap": onuUniMonitorMap,
       "performanceConform": performanceConform,
       "performanceGroups": performanceGroups,
       "alarmThresholdGroup": alarmThresholdGroup,
       "fdOltStatsGroup": fdOltStatsGroup,
       "fdOnuStatsGroup": fdOnuStatsGroup,
       "swHisMonitorGroup": swHisMonitorGroup,
       "oltHisMonitorGroup": oltHisMonitorGroup,
       "onuHisMonitorGroup": onuHisMonitorGroup,
       "swRelMonitorGroup": swRelMonitorGroup,
       "oltRelMonitorGroup": oltRelMonitorGroup,
       "onuRelMonitorGroup": onuRelMonitorGroup,
       "monitorMapGroup": monitorMapGroup,
       "performanceCompliances": performanceCompliances,
       "performanceCompliance": performanceCompliance}
)
