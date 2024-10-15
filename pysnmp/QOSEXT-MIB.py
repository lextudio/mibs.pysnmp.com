# SNMP MIB module (QOSEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QOSEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:03 2024
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

(qosExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "qosExt")

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

apQosExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApQosTable_Object = MibTable
apQosTable = _ApQosTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2)
)
if mibBuilder.loadTexts:
    apQosTable.setStatus("current")
_ApQosEntry_Object = MibTableRow
apQosEntry = _ApQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1)
)
apQosEntry.setIndexNames(
    (0, "QOSEXT-MIB", "apQosType"),
    (0, "QOSEXT-MIB", "apQosSubType"),
)
if mibBuilder.loadTexts:
    apQosEntry.setStatus("current")


class _ApQosType_Type(Integer32):
    """Custom type apQosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("best-effort", 1),
          ("streamed", 2))
    )


_ApQosType_Type.__name__ = "Integer32"
_ApQosType_Object = MibTableColumn
apQosType = _ApQosType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 1),
    _ApQosType_Type()
)
apQosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQosType.setStatus("current")


class _ApQosSubType_Type(Integer32):
    """Custom type apQosSubType based on Integer32"""
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
        *(("best-effort", 1),
          ("realAudio-2-14400", 2),
          ("realAudio-2-28800", 3),
          ("realAudio-3-28800", 4),
          ("realAudio-3-28800-stereo", 5),
          ("realAudio-3-dual-isdn", 7),
          ("realAudio-3-isdn", 6))
    )


_ApQosSubType_Type.__name__ = "Integer32"
_ApQosSubType_Object = MibTableColumn
apQosSubType = _ApQosSubType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 2),
    _ApQosSubType_Type()
)
apQosSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQosSubType.setStatus("current")


class _ApQosName_Type(DisplayString):
    """Custom type apQosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApQosName_Type.__name__ = "DisplayString"
_ApQosName_Object = MibTableColumn
apQosName = _ApQosName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 3),
    _ApQosName_Type()
)
apQosName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apQosName.setStatus("current")


class _ApQosClass_Type(Integer32):
    """Custom type apQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ApQosClass_Type.__name__ = "Integer32"
_ApQosClass_Object = MibTableColumn
apQosClass = _ApQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 4),
    _ApQosClass_Type()
)
apQosClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQosClass.setStatus("current")
_ApQosHopLatency_Type = Integer32
_ApQosHopLatency_Object = MibTableColumn
apQosHopLatency = _ApQosHopLatency_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 5),
    _ApQosHopLatency_Type()
)
apQosHopLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQosHopLatency.setStatus("current")
_ApQosSampleRate_Type = Integer32
_ApQosSampleRate_Object = MibTableColumn
apQosSampleRate = _ApQosSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 6),
    _ApQosSampleRate_Type()
)
apQosSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQosSampleRate.setStatus("current")
_ApQosBitsPerSample_Type = Integer32
_ApQosBitsPerSample_Object = MibTableColumn
apQosBitsPerSample = _ApQosBitsPerSample_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 7),
    _ApQosBitsPerSample_Type()
)
apQosBitsPerSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQosBitsPerSample.setStatus("current")
_ApQosAvgBw_Type = Integer32
_ApQosAvgBw_Object = MibTableColumn
apQosAvgBw = _ApQosAvgBw_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 8),
    _ApQosAvgBw_Type()
)
apQosAvgBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQosAvgBw.setStatus("current")
_ApQosSampleSize_Type = Integer32
_ApQosSampleSize_Object = MibTableColumn
apQosSampleSize = _ApQosSampleSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 9),
    _ApQosSampleSize_Type()
)
apQosSampleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQosSampleSize.setStatus("current")
_ApQosSilenceTime_Type = Integer32
_ApQosSilenceTime_Object = MibTableColumn
apQosSilenceTime = _ApQosSilenceTime_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 10),
    _ApQosSilenceTime_Type()
)
apQosSilenceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQosSilenceTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QOSEXT-MIB",
    **{"apQosExtMib": apQosExtMib,
       "apQosTable": apQosTable,
       "apQosEntry": apQosEntry,
       "apQosType": apQosType,
       "apQosSubType": apQosSubType,
       "apQosName": apQosName,
       "apQosClass": apQosClass,
       "apQosHopLatency": apQosHopLatency,
       "apQosSampleRate": apQosSampleRate,
       "apQosBitsPerSample": apQosBitsPerSample,
       "apQosAvgBw": apQosAvgBw,
       "apQosSampleSize": apQosSampleSize,
       "apQosSilenceTime": apQosSilenceTime}
)
