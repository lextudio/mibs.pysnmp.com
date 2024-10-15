# SNMP MIB module (FOUNDRY-CAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-CAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:42 2024
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

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

snCAR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16)
)
snCAR.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PacketSource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("input", 0),
          ("output", 1))
    )



class RateLimitType(Integer32, TextualConvention):
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
        *(("all", 3),
          ("quickAcc", 2),
          ("standardAcc", 1))
    )



class RateLimitAction(Integer32, TextualConvention):
    status = "current"
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
        *(("continue", 1),
          ("drop", 2),
          ("precedCont", 3),
          ("precedXmit", 4),
          ("xmit", 5))
    )



# MIB Managed Objects in the order of their OIDs

_SnPortCARs_ObjectIdentity = ObjectIdentity
snPortCARs = _SnPortCARs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1)
)
_SnPortCARTable_Object = MibTable
snPortCARTable = _SnPortCARTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1)
)
if mibBuilder.loadTexts:
    snPortCARTable.setStatus("current")
_SnPortCAREntry_Object = MibTableRow
snPortCAREntry = _SnPortCAREntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1)
)
snPortCAREntry.setIndexNames(
    (0, "FOUNDRY-CAR-MIB", "snPortCARifIndex"),
    (0, "FOUNDRY-CAR-MIB", "snPortCARDirection"),
    (0, "FOUNDRY-CAR-MIB", "snPortCARRowIndex"),
)
if mibBuilder.loadTexts:
    snPortCAREntry.setStatus("current")
_SnPortCARifIndex_Type = InterfaceIndex
_SnPortCARifIndex_Object = MibTableColumn
snPortCARifIndex = _SnPortCARifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 1),
    _SnPortCARifIndex_Type()
)
snPortCARifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARifIndex.setStatus("current")
_SnPortCARDirection_Type = PacketSource
_SnPortCARDirection_Object = MibTableColumn
snPortCARDirection = _SnPortCARDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 2),
    _SnPortCARDirection_Type()
)
snPortCARDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARDirection.setStatus("current")


class _SnPortCARRowIndex_Type(Integer32):
    """Custom type snPortCARRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnPortCARRowIndex_Type.__name__ = "Integer32"
_SnPortCARRowIndex_Object = MibTableColumn
snPortCARRowIndex = _SnPortCARRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 3),
    _SnPortCARRowIndex_Type()
)
snPortCARRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARRowIndex.setStatus("current")
_SnPortCARType_Type = RateLimitType
_SnPortCARType_Object = MibTableColumn
snPortCARType = _SnPortCARType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 4),
    _SnPortCARType_Type()
)
snPortCARType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARType.setStatus("current")
_SnPortCARAccIdx_Type = Integer32
_SnPortCARAccIdx_Object = MibTableColumn
snPortCARAccIdx = _SnPortCARAccIdx_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 5),
    _SnPortCARAccIdx_Type()
)
snPortCARAccIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARAccIdx.setStatus("current")
_SnPortCARRate_Type = Integer32
_SnPortCARRate_Object = MibTableColumn
snPortCARRate = _SnPortCARRate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 6),
    _SnPortCARRate_Type()
)
snPortCARRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARRate.setStatus("current")
_SnPortCARLimit_Type = Integer32
_SnPortCARLimit_Object = MibTableColumn
snPortCARLimit = _SnPortCARLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 7),
    _SnPortCARLimit_Type()
)
snPortCARLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARLimit.setStatus("current")
_SnPortCARExtLimit_Type = Integer32
_SnPortCARExtLimit_Object = MibTableColumn
snPortCARExtLimit = _SnPortCARExtLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 8),
    _SnPortCARExtLimit_Type()
)
snPortCARExtLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARExtLimit.setStatus("current")
_SnPortCARConformAction_Type = RateLimitAction
_SnPortCARConformAction_Object = MibTableColumn
snPortCARConformAction = _SnPortCARConformAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 9),
    _SnPortCARConformAction_Type()
)
snPortCARConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARConformAction.setStatus("current")
_SnPortCARExceedAction_Type = RateLimitAction
_SnPortCARExceedAction_Object = MibTableColumn
snPortCARExceedAction = _SnPortCARExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 10),
    _SnPortCARExceedAction_Type()
)
snPortCARExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARExceedAction.setStatus("current")
_SnPortCARStatSwitchedPkts_Type = Counter64
_SnPortCARStatSwitchedPkts_Object = MibTableColumn
snPortCARStatSwitchedPkts = _SnPortCARStatSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 11),
    _SnPortCARStatSwitchedPkts_Type()
)
snPortCARStatSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARStatSwitchedPkts.setStatus("current")
_SnPortCARStatSwitchedBytes_Type = Counter64
_SnPortCARStatSwitchedBytes_Object = MibTableColumn
snPortCARStatSwitchedBytes = _SnPortCARStatSwitchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 12),
    _SnPortCARStatSwitchedBytes_Type()
)
snPortCARStatSwitchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARStatSwitchedBytes.setStatus("current")
_SnPortCARStatFilteredPkts_Type = Counter64
_SnPortCARStatFilteredPkts_Object = MibTableColumn
snPortCARStatFilteredPkts = _SnPortCARStatFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 13),
    _SnPortCARStatFilteredPkts_Type()
)
snPortCARStatFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARStatFilteredPkts.setStatus("current")
_SnPortCARStatFilteredBytes_Type = Counter64
_SnPortCARStatFilteredBytes_Object = MibTableColumn
snPortCARStatFilteredBytes = _SnPortCARStatFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 14),
    _SnPortCARStatFilteredBytes_Type()
)
snPortCARStatFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARStatFilteredBytes.setStatus("current")
_SnPortCARStatCurBurst_Type = Gauge32
_SnPortCARStatCurBurst_Object = MibTableColumn
snPortCARStatCurBurst = _SnPortCARStatCurBurst_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 15),
    _SnPortCARStatCurBurst_Type()
)
snPortCARStatCurBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARStatCurBurst.setStatus("current")
_AgRateLimitCounterTable_Object = MibTable
agRateLimitCounterTable = _AgRateLimitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2)
)
if mibBuilder.loadTexts:
    agRateLimitCounterTable.setStatus("current")
_AgRateLimitCounterEntry_Object = MibTableRow
agRateLimitCounterEntry = _AgRateLimitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1)
)
agRateLimitCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FOUNDRY-CAR-MIB", "snPortCARRowIndex"),
)
if mibBuilder.loadTexts:
    agRateLimitCounterEntry.setStatus("current")
_AgRateLimitCounterFwdedOctets_Type = Counter64
_AgRateLimitCounterFwdedOctets_Object = MibTableColumn
agRateLimitCounterFwdedOctets = _AgRateLimitCounterFwdedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 1),
    _AgRateLimitCounterFwdedOctets_Type()
)
agRateLimitCounterFwdedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterFwdedOctets.setStatus("current")
_AgRateLimitCounterDroppedOctets_Type = Counter64
_AgRateLimitCounterDroppedOctets_Object = MibTableColumn
agRateLimitCounterDroppedOctets = _AgRateLimitCounterDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 2),
    _AgRateLimitCounterDroppedOctets_Type()
)
agRateLimitCounterDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterDroppedOctets.setStatus("current")
_AgRateLimitCounterReMarkedOctets_Type = Counter64
_AgRateLimitCounterReMarkedOctets_Object = MibTableColumn
agRateLimitCounterReMarkedOctets = _AgRateLimitCounterReMarkedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 3),
    _AgRateLimitCounterReMarkedOctets_Type()
)
agRateLimitCounterReMarkedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterReMarkedOctets.setStatus("current")
_AgRateLimitCounterTotalOctets_Type = Counter64
_AgRateLimitCounterTotalOctets_Object = MibTableColumn
agRateLimitCounterTotalOctets = _AgRateLimitCounterTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 4),
    _AgRateLimitCounterTotalOctets_Type()
)
agRateLimitCounterTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterTotalOctets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-CAR-MIB",
    **{"PacketSource": PacketSource,
       "RateLimitType": RateLimitType,
       "RateLimitAction": RateLimitAction,
       "snCAR": snCAR,
       "snPortCARs": snPortCARs,
       "snPortCARTable": snPortCARTable,
       "snPortCAREntry": snPortCAREntry,
       "snPortCARifIndex": snPortCARifIndex,
       "snPortCARDirection": snPortCARDirection,
       "snPortCARRowIndex": snPortCARRowIndex,
       "snPortCARType": snPortCARType,
       "snPortCARAccIdx": snPortCARAccIdx,
       "snPortCARRate": snPortCARRate,
       "snPortCARLimit": snPortCARLimit,
       "snPortCARExtLimit": snPortCARExtLimit,
       "snPortCARConformAction": snPortCARConformAction,
       "snPortCARExceedAction": snPortCARExceedAction,
       "snPortCARStatSwitchedPkts": snPortCARStatSwitchedPkts,
       "snPortCARStatSwitchedBytes": snPortCARStatSwitchedBytes,
       "snPortCARStatFilteredPkts": snPortCARStatFilteredPkts,
       "snPortCARStatFilteredBytes": snPortCARStatFilteredBytes,
       "snPortCARStatCurBurst": snPortCARStatCurBurst,
       "agRateLimitCounterTable": agRateLimitCounterTable,
       "agRateLimitCounterEntry": agRateLimitCounterEntry,
       "agRateLimitCounterFwdedOctets": agRateLimitCounterFwdedOctets,
       "agRateLimitCounterDroppedOctets": agRateLimitCounterDroppedOctets,
       "agRateLimitCounterReMarkedOctets": agRateLimitCounterReMarkedOctets,
       "agRateLimitCounterTotalOctets": agRateLimitCounterTotalOctets}
)
