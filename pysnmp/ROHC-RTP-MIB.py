# SNMP MIB module (ROHC-RTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ROHC-RTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:10 2024
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

(rohcChannelID,
 rohcContextCID) = mibBuilder.importSymbols(
    "ROHC-MIB",
    "rohcChannelID",
    "rohcContextCID")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rohcRtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 114)
)
rohcRtpMIB.setRevisions(
        ("2004-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RohcRtpObjects_ObjectIdentity = ObjectIdentity
rohcRtpObjects = _RohcRtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 114, 1)
)
_RohcRtpContextTable_Object = MibTable
rohcRtpContextTable = _RohcRtpContextTable_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1)
)
if mibBuilder.loadTexts:
    rohcRtpContextTable.setStatus("current")
_RohcRtpContextEntry_Object = MibTableRow
rohcRtpContextEntry = _RohcRtpContextEntry_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1)
)
rohcRtpContextEntry.setIndexNames(
    (0, "ROHC-MIB", "rohcChannelID"),
    (0, "ROHC-MIB", "rohcContextCID"),
)
if mibBuilder.loadTexts:
    rohcRtpContextEntry.setStatus("current")


class _RohcRtpContextState_Type(Integer32):
    """Custom type rohcRtpContextState based on Integer32"""
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
        *(("firstOrder", 2),
          ("fullContext", 6),
          ("initAndRefresh", 1),
          ("noContext", 4),
          ("secondOrder", 3),
          ("staticContext", 5))
    )


_RohcRtpContextState_Type.__name__ = "Integer32"
_RohcRtpContextState_Object = MibTableColumn
rohcRtpContextState = _RohcRtpContextState_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 3),
    _RohcRtpContextState_Type()
)
rohcRtpContextState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextState.setStatus("current")


class _RohcRtpContextMode_Type(Integer32):
    """Custom type rohcRtpContextMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("optimistic", 2),
          ("reliable", 3),
          ("unidirectional", 1))
    )


_RohcRtpContextMode_Type.__name__ = "Integer32"
_RohcRtpContextMode_Object = MibTableColumn
rohcRtpContextMode = _RohcRtpContextMode_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 4),
    _RohcRtpContextMode_Type()
)
rohcRtpContextMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextMode.setStatus("current")


class _RohcRtpContextAlwaysPad_Type(TruthValue):
    """Custom type rohcRtpContextAlwaysPad based on TruthValue"""


_RohcRtpContextAlwaysPad_Object = MibTableColumn
rohcRtpContextAlwaysPad = _RohcRtpContextAlwaysPad_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 5),
    _RohcRtpContextAlwaysPad_Type()
)
rohcRtpContextAlwaysPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextAlwaysPad.setStatus("current")


class _RohcRtpContextLargePktsAllowed_Type(TruthValue):
    """Custom type rohcRtpContextLargePktsAllowed based on TruthValue"""


_RohcRtpContextLargePktsAllowed_Object = MibTableColumn
rohcRtpContextLargePktsAllowed = _RohcRtpContextLargePktsAllowed_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 6),
    _RohcRtpContextLargePktsAllowed_Type()
)
rohcRtpContextLargePktsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextLargePktsAllowed.setStatus("current")


class _RohcRtpContextVerifyPeriod_Type(Unsigned32):
    """Custom type rohcRtpContextVerifyPeriod based on Unsigned32"""
    defaultValue = 0


_RohcRtpContextVerifyPeriod_Object = MibTableColumn
rohcRtpContextVerifyPeriod = _RohcRtpContextVerifyPeriod_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 7),
    _RohcRtpContextVerifyPeriod_Type()
)
rohcRtpContextVerifyPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextVerifyPeriod.setStatus("current")


class _RohcRtpContextSizesAllowed_Type(Unsigned32):
    """Custom type rohcRtpContextSizesAllowed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RohcRtpContextSizesAllowed_Type.__name__ = "Unsigned32"
_RohcRtpContextSizesAllowed_Object = MibTableColumn
rohcRtpContextSizesAllowed = _RohcRtpContextSizesAllowed_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 8),
    _RohcRtpContextSizesAllowed_Type()
)
rohcRtpContextSizesAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextSizesAllowed.setStatus("current")


class _RohcRtpContextSizesUsed_Type(Unsigned32):
    """Custom type rohcRtpContextSizesUsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RohcRtpContextSizesUsed_Type.__name__ = "Unsigned32"
_RohcRtpContextSizesUsed_Object = MibTableColumn
rohcRtpContextSizesUsed = _RohcRtpContextSizesUsed_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 9),
    _RohcRtpContextSizesUsed_Type()
)
rohcRtpContextSizesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextSizesUsed.setStatus("current")
_RohcRtpContextACKs_Type = Counter32
_RohcRtpContextACKs_Object = MibTableColumn
rohcRtpContextACKs = _RohcRtpContextACKs_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 10),
    _RohcRtpContextACKs_Type()
)
rohcRtpContextACKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextACKs.setStatus("current")
_RohcRtpContextNACKs_Type = Counter32
_RohcRtpContextNACKs_Object = MibTableColumn
rohcRtpContextNACKs = _RohcRtpContextNACKs_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 11),
    _RohcRtpContextNACKs_Type()
)
rohcRtpContextNACKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextNACKs.setStatus("current")
_RohcRtpContextSNACKs_Type = Counter32
_RohcRtpContextSNACKs_Object = MibTableColumn
rohcRtpContextSNACKs = _RohcRtpContextSNACKs_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 12),
    _RohcRtpContextSNACKs_Type()
)
rohcRtpContextSNACKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextSNACKs.setStatus("current")
_RohcRtpContextNHPs_Type = Counter32
_RohcRtpContextNHPs_Object = MibTableColumn
rohcRtpContextNHPs = _RohcRtpContextNHPs_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 13),
    _RohcRtpContextNHPs_Type()
)
rohcRtpContextNHPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextNHPs.setStatus("current")
_RohcRtpContextCSPs_Type = Counter32
_RohcRtpContextCSPs_Object = MibTableColumn
rohcRtpContextCSPs = _RohcRtpContextCSPs_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 14),
    _RohcRtpContextCSPs_Type()
)
rohcRtpContextCSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextCSPs.setStatus("current")
_RohcRtpContextCCPs_Type = Counter32
_RohcRtpContextCCPs_Object = MibTableColumn
rohcRtpContextCCPs = _RohcRtpContextCCPs_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 15),
    _RohcRtpContextCCPs_Type()
)
rohcRtpContextCCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextCCPs.setStatus("current")
_RohcRtpContextPktsLostPhysical_Type = Counter32
_RohcRtpContextPktsLostPhysical_Object = MibTableColumn
rohcRtpContextPktsLostPhysical = _RohcRtpContextPktsLostPhysical_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 16),
    _RohcRtpContextPktsLostPhysical_Type()
)
rohcRtpContextPktsLostPhysical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextPktsLostPhysical.setStatus("current")
_RohcRtpContextPktsLostPreLink_Type = Counter32
_RohcRtpContextPktsLostPreLink_Object = MibTableColumn
rohcRtpContextPktsLostPreLink = _RohcRtpContextPktsLostPreLink_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 17),
    _RohcRtpContextPktsLostPreLink_Type()
)
rohcRtpContextPktsLostPreLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpContextPktsLostPreLink.setStatus("current")
_RohcRtpPacketSizeTable_Object = MibTable
rohcRtpPacketSizeTable = _RohcRtpPacketSizeTable_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 2)
)
if mibBuilder.loadTexts:
    rohcRtpPacketSizeTable.setStatus("current")
_RohcRtpPacketSizeEntry_Object = MibTableRow
rohcRtpPacketSizeEntry = _RohcRtpPacketSizeEntry_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 2, 1)
)
rohcRtpPacketSizeEntry.setIndexNames(
    (0, "ROHC-MIB", "rohcChannelID"),
    (0, "ROHC-MIB", "rohcContextCID"),
    (0, "ROHC-RTP-MIB", "rohcRtpPacketSize"),
)
if mibBuilder.loadTexts:
    rohcRtpPacketSizeEntry.setStatus("current")


class _RohcRtpPacketSize_Type(Unsigned32):
    """Custom type rohcRtpPacketSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RohcRtpPacketSize_Type.__name__ = "Unsigned32"
_RohcRtpPacketSize_Object = MibTableColumn
rohcRtpPacketSize = _RohcRtpPacketSize_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 2, 1, 3),
    _RohcRtpPacketSize_Type()
)
rohcRtpPacketSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rohcRtpPacketSize.setStatus("current")
_RohcRtpPacketSizePreferred_Type = TruthValue
_RohcRtpPacketSizePreferred_Object = MibTableColumn
rohcRtpPacketSizePreferred = _RohcRtpPacketSizePreferred_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 2, 1, 4),
    _RohcRtpPacketSizePreferred_Type()
)
rohcRtpPacketSizePreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpPacketSizePreferred.setStatus("current")
_RohcRtpPacketSizeUsed_Type = TruthValue
_RohcRtpPacketSizeUsed_Object = MibTableColumn
rohcRtpPacketSizeUsed = _RohcRtpPacketSizeUsed_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 2, 1, 5),
    _RohcRtpPacketSizeUsed_Type()
)
rohcRtpPacketSizeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpPacketSizeUsed.setStatus("current")


class _RohcRtpPacketSizeRestrictedType_Type(Integer32):
    """Custom type rohcRtpPacketSizeRestrictedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nhpOnly", 1),
          ("noRestrictions", 3),
          ("rhpOnly", 2))
    )


_RohcRtpPacketSizeRestrictedType_Type.__name__ = "Integer32"
_RohcRtpPacketSizeRestrictedType_Object = MibTableColumn
rohcRtpPacketSizeRestrictedType = _RohcRtpPacketSizeRestrictedType_Object(
    (1, 3, 6, 1, 2, 1, 114, 1, 2, 1, 6),
    _RohcRtpPacketSizeRestrictedType_Type()
)
rohcRtpPacketSizeRestrictedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcRtpPacketSizeRestrictedType.setStatus("current")
_RohcRtpConformance_ObjectIdentity = ObjectIdentity
rohcRtpConformance = _RohcRtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 114, 2)
)
_RohcRtpCompliances_ObjectIdentity = ObjectIdentity
rohcRtpCompliances = _RohcRtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 114, 2, 1)
)
_RohcRtpGroups_ObjectIdentity = ObjectIdentity
rohcRtpGroups = _RohcRtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 114, 2, 2)
)

# Managed Objects groups

rohcRtpContextGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 114, 2, 2, 1)
)
rohcRtpContextGroup.setObjects(
      *(("ROHC-RTP-MIB", "rohcRtpContextState"),
        ("ROHC-RTP-MIB", "rohcRtpContextMode"),
        ("ROHC-RTP-MIB", "rohcRtpContextAlwaysPad"),
        ("ROHC-RTP-MIB", "rohcRtpContextLargePktsAllowed"),
        ("ROHC-RTP-MIB", "rohcRtpContextVerifyPeriod"))
)
if mibBuilder.loadTexts:
    rohcRtpContextGroup.setStatus("current")

rohcRtpPacketSizesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 114, 2, 2, 2)
)
rohcRtpPacketSizesGroup.setObjects(
      *(("ROHC-RTP-MIB", "rohcRtpContextSizesAllowed"),
        ("ROHC-RTP-MIB", "rohcRtpContextSizesUsed"),
        ("ROHC-RTP-MIB", "rohcRtpPacketSizePreferred"),
        ("ROHC-RTP-MIB", "rohcRtpPacketSizeUsed"),
        ("ROHC-RTP-MIB", "rohcRtpPacketSizeRestrictedType"))
)
if mibBuilder.loadTexts:
    rohcRtpPacketSizesGroup.setStatus("current")

rohcRtpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 114, 2, 2, 3)
)
rohcRtpStatisticsGroup.setObjects(
      *(("ROHC-RTP-MIB", "rohcRtpContextACKs"),
        ("ROHC-RTP-MIB", "rohcRtpContextNACKs"),
        ("ROHC-RTP-MIB", "rohcRtpContextSNACKs"),
        ("ROHC-RTP-MIB", "rohcRtpContextNHPs"),
        ("ROHC-RTP-MIB", "rohcRtpContextCSPs"),
        ("ROHC-RTP-MIB", "rohcRtpContextCCPs"),
        ("ROHC-RTP-MIB", "rohcRtpContextPktsLostPhysical"),
        ("ROHC-RTP-MIB", "rohcRtpContextPktsLostPreLink"))
)
if mibBuilder.loadTexts:
    rohcRtpStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rohcRtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 114, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rohcRtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROHC-RTP-MIB",
    **{"rohcRtpMIB": rohcRtpMIB,
       "rohcRtpObjects": rohcRtpObjects,
       "rohcRtpContextTable": rohcRtpContextTable,
       "rohcRtpContextEntry": rohcRtpContextEntry,
       "rohcRtpContextState": rohcRtpContextState,
       "rohcRtpContextMode": rohcRtpContextMode,
       "rohcRtpContextAlwaysPad": rohcRtpContextAlwaysPad,
       "rohcRtpContextLargePktsAllowed": rohcRtpContextLargePktsAllowed,
       "rohcRtpContextVerifyPeriod": rohcRtpContextVerifyPeriod,
       "rohcRtpContextSizesAllowed": rohcRtpContextSizesAllowed,
       "rohcRtpContextSizesUsed": rohcRtpContextSizesUsed,
       "rohcRtpContextACKs": rohcRtpContextACKs,
       "rohcRtpContextNACKs": rohcRtpContextNACKs,
       "rohcRtpContextSNACKs": rohcRtpContextSNACKs,
       "rohcRtpContextNHPs": rohcRtpContextNHPs,
       "rohcRtpContextCSPs": rohcRtpContextCSPs,
       "rohcRtpContextCCPs": rohcRtpContextCCPs,
       "rohcRtpContextPktsLostPhysical": rohcRtpContextPktsLostPhysical,
       "rohcRtpContextPktsLostPreLink": rohcRtpContextPktsLostPreLink,
       "rohcRtpPacketSizeTable": rohcRtpPacketSizeTable,
       "rohcRtpPacketSizeEntry": rohcRtpPacketSizeEntry,
       "rohcRtpPacketSize": rohcRtpPacketSize,
       "rohcRtpPacketSizePreferred": rohcRtpPacketSizePreferred,
       "rohcRtpPacketSizeUsed": rohcRtpPacketSizeUsed,
       "rohcRtpPacketSizeRestrictedType": rohcRtpPacketSizeRestrictedType,
       "rohcRtpConformance": rohcRtpConformance,
       "rohcRtpCompliances": rohcRtpCompliances,
       "rohcRtpCompliance": rohcRtpCompliance,
       "rohcRtpGroups": rohcRtpGroups,
       "rohcRtpContextGroup": rohcRtpContextGroup,
       "rohcRtpPacketSizesGroup": rohcRtpPacketSizesGroup,
       "rohcRtpStatisticsGroup": rohcRtpStatisticsGroup}
)
