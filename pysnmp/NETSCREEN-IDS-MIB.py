# SNMP MIB module (NETSCREEN-IDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-IDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:44 2024
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

(netscreenIDS,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenIDS")

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

nsIdsProtect = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1)
)
nsIdsProtect.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2002-04-26 00:00",
         "2001-09-28 00:00",
         "2001-01-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsIdsProtectSetTable_Object = MibTable
nsIdsProtectSetTable = _NsIdsProtectSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nsIdsProtectSetTable.setStatus("current")
_NsIdsProtectSetEntry_Object = MibTableRow
nsIdsProtectSetEntry = _NsIdsProtectSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1)
)
nsIdsProtectSetEntry.setIndexNames(
    (0, "NETSCREEN-IDS-MIB", "nsIdsProtectZoneIdx"),
)
if mibBuilder.loadTexts:
    nsIdsProtectSetEntry.setStatus("current")


class _NsIdsProtectZoneIdx_Type(Integer32):
    """Custom type nsIdsProtectZoneIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIdsProtectZoneIdx_Type.__name__ = "Integer32"
_NsIdsProtectZoneIdx_Object = MibTableColumn
nsIdsProtectZoneIdx = _NsIdsProtectZoneIdx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 1),
    _NsIdsProtectZoneIdx_Type()
)
nsIdsProtectZoneIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsProtectZoneIdx.setStatus("current")


class _NsIdsDetectPingOfDeath_Type(Integer32):
    """Custom type nsIdsDetectPingOfDeath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectPingOfDeath_Type.__name__ = "Integer32"
_NsIdsDetectPingOfDeath_Object = MibTableColumn
nsIdsDetectPingOfDeath = _NsIdsDetectPingOfDeath_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 2),
    _NsIdsDetectPingOfDeath_Type()
)
nsIdsDetectPingOfDeath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectPingOfDeath.setStatus("current")


class _NsIdsDetectTearDrop_Type(Integer32):
    """Custom type nsIdsDetectTearDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectTearDrop_Type.__name__ = "Integer32"
_NsIdsDetectTearDrop_Object = MibTableColumn
nsIdsDetectTearDrop = _NsIdsDetectTearDrop_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 3),
    _NsIdsDetectTearDrop_Type()
)
nsIdsDetectTearDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectTearDrop.setStatus("current")


class _NsIdsDetectWinNuke_Type(Integer32):
    """Custom type nsIdsDetectWinNuke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectWinNuke_Type.__name__ = "Integer32"
_NsIdsDetectWinNuke_Object = MibTableColumn
nsIdsDetectWinNuke = _NsIdsDetectWinNuke_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 4),
    _NsIdsDetectWinNuke_Type()
)
nsIdsDetectWinNuke.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectWinNuke.setStatus("current")


class _NsIdsFilterIpSrcRoute_Type(Integer32):
    """Custom type nsIdsFilterIpSrcRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsFilterIpSrcRoute_Type.__name__ = "Integer32"
_NsIdsFilterIpSrcRoute_Object = MibTableColumn
nsIdsFilterIpSrcRoute = _NsIdsFilterIpSrcRoute_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 5),
    _NsIdsFilterIpSrcRoute_Type()
)
nsIdsFilterIpSrcRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsFilterIpSrcRoute.setStatus("current")


class _NsIdsDetectPortScan_Type(Integer32):
    """Custom type nsIdsDetectPortScan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectPortScan_Type.__name__ = "Integer32"
_NsIdsDetectPortScan_Object = MibTableColumn
nsIdsDetectPortScan = _NsIdsDetectPortScan_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 6),
    _NsIdsDetectPortScan_Type()
)
nsIdsDetectPortScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectPortScan.setStatus("current")


class _NsIdsDetectAddrSweep_Type(Integer32):
    """Custom type nsIdsDetectAddrSweep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectAddrSweep_Type.__name__ = "Integer32"
_NsIdsDetectAddrSweep_Object = MibTableColumn
nsIdsDetectAddrSweep = _NsIdsDetectAddrSweep_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 7),
    _NsIdsDetectAddrSweep_Type()
)
nsIdsDetectAddrSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectAddrSweep.setStatus("current")


class _NsIdsDetectLand_Type(Integer32):
    """Custom type nsIdsDetectLand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectLand_Type.__name__ = "Integer32"
_NsIdsDetectLand_Object = MibTableColumn
nsIdsDetectLand = _NsIdsDetectLand_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 8),
    _NsIdsDetectLand_Type()
)
nsIdsDetectLand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectLand.setStatus("current")


class _NsIdsBlockComponent_Type(Integer32):
    """Custom type nsIdsBlockComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsBlockComponent_Type.__name__ = "Integer32"
_NsIdsBlockComponent_Object = MibTableColumn
nsIdsBlockComponent = _NsIdsBlockComponent_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 9),
    _NsIdsBlockComponent_Type()
)
nsIdsBlockComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsBlockComponent.setStatus("current")


class _NsIdsDetectIpSpoof_Type(Integer32):
    """Custom type nsIdsDetectIpSpoof based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIpSpoof_Type.__name__ = "Integer32"
_NsIdsDetectIpSpoof_Object = MibTableColumn
nsIdsDetectIpSpoof = _NsIdsDetectIpSpoof_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 10),
    _NsIdsDetectIpSpoof_Type()
)
nsIdsDetectIpSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIpSpoof.setStatus("current")


class _NsIdsDetectSyn_Type(Integer32):
    """Custom type nsIdsDetectSyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectSyn_Type.__name__ = "Integer32"
_NsIdsDetectSyn_Object = MibTableColumn
nsIdsDetectSyn = _NsIdsDetectSyn_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 11),
    _NsIdsDetectSyn_Type()
)
nsIdsDetectSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectSyn.setStatus("current")


class _NsIdsDetectIcmpFlood_Type(Integer32):
    """Custom type nsIdsDetectIcmpFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIcmpFlood_Type.__name__ = "Integer32"
_NsIdsDetectIcmpFlood_Object = MibTableColumn
nsIdsDetectIcmpFlood = _NsIdsDetectIcmpFlood_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 12),
    _NsIdsDetectIcmpFlood_Type()
)
nsIdsDetectIcmpFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIcmpFlood.setStatus("current")


class _NsIdsDetectUdpFlood_Type(Integer32):
    """Custom type nsIdsDetectUdpFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectUdpFlood_Type.__name__ = "Integer32"
_NsIdsDetectUdpFlood_Object = MibTableColumn
nsIdsDetectUdpFlood = _NsIdsDetectUdpFlood_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 13),
    _NsIdsDetectUdpFlood_Type()
)
nsIdsDetectUdpFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectUdpFlood.setStatus("current")


class _NsIdsDetectSynFrag_Type(Integer32):
    """Custom type nsIdsDetectSynFrag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectSynFrag_Type.__name__ = "Integer32"
_NsIdsDetectSynFrag_Object = MibTableColumn
nsIdsDetectSynFrag = _NsIdsDetectSynFrag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 14),
    _NsIdsDetectSynFrag_Type()
)
nsIdsDetectSynFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectSynFrag.setStatus("current")


class _NsIdsDetectTcpNoFlag_Type(Integer32):
    """Custom type nsIdsDetectTcpNoFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectTcpNoFlag_Type.__name__ = "Integer32"
_NsIdsDetectTcpNoFlag_Object = MibTableColumn
nsIdsDetectTcpNoFlag = _NsIdsDetectTcpNoFlag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 15),
    _NsIdsDetectTcpNoFlag_Type()
)
nsIdsDetectTcpNoFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectTcpNoFlag.setStatus("current")


class _NsIdsDetectIpUnknownProt_Type(Integer32):
    """Custom type nsIdsDetectIpUnknownProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIpUnknownProt_Type.__name__ = "Integer32"
_NsIdsDetectIpUnknownProt_Object = MibTableColumn
nsIdsDetectIpUnknownProt = _NsIdsDetectIpUnknownProt_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 16),
    _NsIdsDetectIpUnknownProt_Type()
)
nsIdsDetectIpUnknownProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIpUnknownProt.setStatus("current")


class _NsIdsDetectIpOptBad_Type(Integer32):
    """Custom type nsIdsDetectIpOptBad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIpOptBad_Type.__name__ = "Integer32"
_NsIdsDetectIpOptBad_Object = MibTableColumn
nsIdsDetectIpOptBad = _NsIdsDetectIpOptBad_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 17),
    _NsIdsDetectIpOptBad_Type()
)
nsIdsDetectIpOptBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIpOptBad.setStatus("current")


class _NsIdsDetectIpOptRecord_Type(Integer32):
    """Custom type nsIdsDetectIpOptRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIpOptRecord_Type.__name__ = "Integer32"
_NsIdsDetectIpOptRecord_Object = MibTableColumn
nsIdsDetectIpOptRecord = _NsIdsDetectIpOptRecord_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 18),
    _NsIdsDetectIpOptRecord_Type()
)
nsIdsDetectIpOptRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIpOptRecord.setStatus("current")


class _NsIdsDetectIpOptTimestamp_Type(Integer32):
    """Custom type nsIdsDetectIpOptTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIpOptTimestamp_Type.__name__ = "Integer32"
_NsIdsDetectIpOptTimestamp_Object = MibTableColumn
nsIdsDetectIpOptTimestamp = _NsIdsDetectIpOptTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 19),
    _NsIdsDetectIpOptTimestamp_Type()
)
nsIdsDetectIpOptTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIpOptTimestamp.setStatus("current")


class _NsIdsDetectIpOptSCHT_Type(Integer32):
    """Custom type nsIdsDetectIpOptSCHT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIpOptSCHT_Type.__name__ = "Integer32"
_NsIdsDetectIpOptSCHT_Object = MibTableColumn
nsIdsDetectIpOptSCHT = _NsIdsDetectIpOptSCHT_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 20),
    _NsIdsDetectIpOptSCHT_Type()
)
nsIdsDetectIpOptSCHT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIpOptSCHT.setStatus("current")


class _NsIdsDetectIpOptLSR_Type(Integer32):
    """Custom type nsIdsDetectIpOptLSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIpOptLSR_Type.__name__ = "Integer32"
_NsIdsDetectIpOptLSR_Object = MibTableColumn
nsIdsDetectIpOptLSR = _NsIdsDetectIpOptLSR_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 21),
    _NsIdsDetectIpOptLSR_Type()
)
nsIdsDetectIpOptLSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIpOptLSR.setStatus("current")


class _NsIdsDetectIpOptSSR_Type(Integer32):
    """Custom type nsIdsDetectIpOptSSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIpOptSSR_Type.__name__ = "Integer32"
_NsIdsDetectIpOptSSR_Object = MibTableColumn
nsIdsDetectIpOptSSR = _NsIdsDetectIpOptSSR_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 22),
    _NsIdsDetectIpOptSSR_Type()
)
nsIdsDetectIpOptSSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIpOptSSR.setStatus("current")


class _NsIdsDetectIpOptStream_Type(Integer32):
    """Custom type nsIdsDetectIpOptStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIpOptStream_Type.__name__ = "Integer32"
_NsIdsDetectIpOptStream_Object = MibTableColumn
nsIdsDetectIpOptStream = _NsIdsDetectIpOptStream_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 23),
    _NsIdsDetectIpOptStream_Type()
)
nsIdsDetectIpOptStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIpOptStream.setStatus("current")


class _NsIdsDetectIcmpFrag_Type(Integer32):
    """Custom type nsIdsDetectIcmpFrag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIcmpFrag_Type.__name__ = "Integer32"
_NsIdsDetectIcmpFrag_Object = MibTableColumn
nsIdsDetectIcmpFrag = _NsIdsDetectIcmpFrag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 24),
    _NsIdsDetectIcmpFrag_Type()
)
nsIdsDetectIcmpFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIcmpFrag.setStatus("current")


class _NsIdsDetectIcmpLarge_Type(Integer32):
    """Custom type nsIdsDetectIcmpLarge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIcmpLarge_Type.__name__ = "Integer32"
_NsIdsDetectIcmpLarge_Object = MibTableColumn
nsIdsDetectIcmpLarge = _NsIdsDetectIcmpLarge_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 25),
    _NsIdsDetectIcmpLarge_Type()
)
nsIdsDetectIcmpLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIcmpLarge.setStatus("current")


class _NsIdsDetectTcpSynFin_Type(Integer32):
    """Custom type nsIdsDetectTcpSynFin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectTcpSynFin_Type.__name__ = "Integer32"
_NsIdsDetectTcpSynFin_Object = MibTableColumn
nsIdsDetectTcpSynFin = _NsIdsDetectTcpSynFin_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 26),
    _NsIdsDetectTcpSynFin_Type()
)
nsIdsDetectTcpSynFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectTcpSynFin.setStatus("current")


class _NsIdsDetectTcpFinNoAck_Type(Integer32):
    """Custom type nsIdsDetectTcpFinNoAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectTcpFinNoAck_Type.__name__ = "Integer32"
_NsIdsDetectTcpFinNoAck_Object = MibTableColumn
nsIdsDetectTcpFinNoAck = _NsIdsDetectTcpFinNoAck_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 27),
    _NsIdsDetectTcpFinNoAck_Type()
)
nsIdsDetectTcpFinNoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectTcpFinNoAck.setStatus("current")


class _NsIdsHttpMalUrl_Type(Integer32):
    """Custom type nsIdsHttpMalUrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsHttpMalUrl_Type.__name__ = "Integer32"
_NsIdsHttpMalUrl_Object = MibTableColumn
nsIdsHttpMalUrl = _NsIdsHttpMalUrl_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 28),
    _NsIdsHttpMalUrl_Type()
)
nsIdsHttpMalUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsHttpMalUrl.setStatus("current")


class _NsIdsSessMalNum_Type(Integer32):
    """Custom type nsIdsSessMalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsSessMalNum_Type.__name__ = "Integer32"
_NsIdsSessMalNum_Object = MibTableColumn
nsIdsSessMalNum = _NsIdsSessMalNum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 29),
    _NsIdsSessMalNum_Type()
)
nsIdsSessMalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsSessMalNum.setStatus("current")


class _NsIdsDetectSynAckAck_Type(Integer32):
    """Custom type nsIdsDetectSynAckAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectSynAckAck_Type.__name__ = "Integer32"
_NsIdsDetectSynAckAck_Object = MibTableColumn
nsIdsDetectSynAckAck = _NsIdsDetectSynAckAck_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 30),
    _NsIdsDetectSynAckAck_Type()
)
nsIdsDetectSynAckAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectSynAckAck.setStatus("current")


class _NsIdsDetectIpFrag_Type(Integer32):
    """Custom type nsIdsDetectIpFrag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIdsDetectIpFrag_Type.__name__ = "Integer32"
_NsIdsDetectIpFrag_Object = MibTableColumn
nsIdsDetectIpFrag = _NsIdsDetectIpFrag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 1, 1, 31),
    _NsIdsDetectIpFrag_Type()
)
nsIdsDetectIpFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsDetectIpFrag.setStatus("current")
_NsIdsProtectThreshTable_Object = MibTable
nsIdsProtectThreshTable = _NsIdsProtectThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2)
)
if mibBuilder.loadTexts:
    nsIdsProtectThreshTable.setStatus("current")
_NsIdsProtectThreshEntry_Object = MibTableRow
nsIdsProtectThreshEntry = _NsIdsProtectThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1)
)
nsIdsProtectThreshEntry.setIndexNames(
    (0, "NETSCREEN-IDS-MIB", "nsIdsProtectThreshZoneIdx"),
)
if mibBuilder.loadTexts:
    nsIdsProtectThreshEntry.setStatus("current")


class _NsIdsProtectThreshZoneIdx_Type(Integer32):
    """Custom type nsIdsProtectThreshZoneIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIdsProtectThreshZoneIdx_Type.__name__ = "Integer32"
_NsIdsProtectThreshZoneIdx_Object = MibTableColumn
nsIdsProtectThreshZoneIdx = _NsIdsProtectThreshZoneIdx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 1),
    _NsIdsProtectThreshZoneIdx_Type()
)
nsIdsProtectThreshZoneIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsProtectThreshZoneIdx.setStatus("current")
_NsIdsSynAttackThresh_Type = Integer32
_NsIdsSynAttackThresh_Object = MibTableColumn
nsIdsSynAttackThresh = _NsIdsSynAttackThresh_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 2),
    _NsIdsSynAttackThresh_Type()
)
nsIdsSynAttackThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsSynAttackThresh.setStatus("current")
_NsIdsSynAttackTimeout_Type = Integer32
_NsIdsSynAttackTimeout_Object = MibTableColumn
nsIdsSynAttackTimeout = _NsIdsSynAttackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 3),
    _NsIdsSynAttackTimeout_Type()
)
nsIdsSynAttackTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsSynAttackTimeout.setStatus("current")
_NsIdsSynAttackAlmTh_Type = Integer32
_NsIdsSynAttackAlmTh_Object = MibTableColumn
nsIdsSynAttackAlmTh = _NsIdsSynAttackAlmTh_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 4),
    _NsIdsSynAttackAlmTh_Type()
)
nsIdsSynAttackAlmTh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsSynAttackAlmTh.setStatus("current")
_NsIdsSynAttackQueSize_Type = Integer32
_NsIdsSynAttackQueSize_Object = MibTableColumn
nsIdsSynAttackQueSize = _NsIdsSynAttackQueSize_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 5),
    _NsIdsSynAttackQueSize_Type()
)
nsIdsSynAttackQueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsSynAttackQueSize.setStatus("current")
_NsIdsSynAttackAgeTime_Type = Integer32
_NsIdsSynAttackAgeTime_Object = MibTableColumn
nsIdsSynAttackAgeTime = _NsIdsSynAttackAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 6),
    _NsIdsSynAttackAgeTime_Type()
)
nsIdsSynAttackAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsSynAttackAgeTime.setStatus("current")
_NsIdsIcmpFloodThresh_Type = Integer32
_NsIdsIcmpFloodThresh_Object = MibTableColumn
nsIdsIcmpFloodThresh = _NsIdsIcmpFloodThresh_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 7),
    _NsIdsIcmpFloodThresh_Type()
)
nsIdsIcmpFloodThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsIcmpFloodThresh.setStatus("current")
_NsIdsUdpFloodThresh_Type = Integer32
_NsIdsUdpFloodThresh_Object = MibTableColumn
nsIdsUdpFloodThresh = _NsIdsUdpFloodThresh_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 8),
    _NsIdsUdpFloodThresh_Type()
)
nsIdsUdpFloodThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsUdpFloodThresh.setStatus("current")
_NsIdsPortScanThresh_Type = Integer32
_NsIdsPortScanThresh_Object = MibTableColumn
nsIdsPortScanThresh = _NsIdsPortScanThresh_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 9),
    _NsIdsPortScanThresh_Type()
)
nsIdsPortScanThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsPortScanThresh.setStatus("current")
_NsIdsIpSweepThresh_Type = Integer32
_NsIdsIpSweepThresh_Object = MibTableColumn
nsIdsIpSweepThresh = _NsIdsIpSweepThresh_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 10),
    _NsIdsIpSweepThresh_Type()
)
nsIdsIpSweepThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsIpSweepThresh.setStatus("current")
_NsIdsSynAckAckThres_Type = Integer32
_NsIdsSynAckAckThres_Object = MibTableColumn
nsIdsSynAckAckThres = _NsIdsSynAckAckThres_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 1, 2, 1, 11),
    _NsIdsSynAckAckThres_Type()
)
nsIdsSynAckAckThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsSynAckAckThres.setStatus("current")
_NsIdsAttkMonTable_Object = MibTable
nsIdsAttkMonTable = _NsIdsAttkMonTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2)
)
if mibBuilder.loadTexts:
    nsIdsAttkMonTable.setStatus("current")
_NsIdsAttkMonEntry_Object = MibTableRow
nsIdsAttkMonEntry = _NsIdsAttkMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1)
)
nsIdsAttkMonEntry.setIndexNames(
    (0, "NETSCREEN-IDS-MIB", "nsIdsAttkMonIfIdx"),
)
if mibBuilder.loadTexts:
    nsIdsAttkMonEntry.setStatus("current")


class _NsIdsAttkMonIfIdx_Type(Integer32):
    """Custom type nsIdsAttkMonIfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIdsAttkMonIfIdx_Type.__name__ = "Integer32"
_NsIdsAttkMonIfIdx_Object = MibTableColumn
nsIdsAttkMonIfIdx = _NsIdsAttkMonIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 1),
    _NsIdsAttkMonIfIdx_Type()
)
nsIdsAttkMonIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonIfIdx.setStatus("current")
_NsIdsAttkMonVsys_Type = Integer32
_NsIdsAttkMonVsys_Object = MibTableColumn
nsIdsAttkMonVsys = _NsIdsAttkMonVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 2),
    _NsIdsAttkMonVsys_Type()
)
nsIdsAttkMonVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonVsys.setStatus("current")
_NsIdsAttkMonSynAttk_Type = Counter32
_NsIdsAttkMonSynAttk_Object = MibTableColumn
nsIdsAttkMonSynAttk = _NsIdsAttkMonSynAttk_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 3),
    _NsIdsAttkMonSynAttk_Type()
)
nsIdsAttkMonSynAttk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonSynAttk.setStatus("current")
_NsIdsAttkMonTearDrop_Type = Counter32
_NsIdsAttkMonTearDrop_Object = MibTableColumn
nsIdsAttkMonTearDrop = _NsIdsAttkMonTearDrop_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 4),
    _NsIdsAttkMonTearDrop_Type()
)
nsIdsAttkMonTearDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonTearDrop.setStatus("current")
_NsIdsAttkMonSrcRoute_Type = Counter32
_NsIdsAttkMonSrcRoute_Object = MibTableColumn
nsIdsAttkMonSrcRoute = _NsIdsAttkMonSrcRoute_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 5),
    _NsIdsAttkMonSrcRoute_Type()
)
nsIdsAttkMonSrcRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonSrcRoute.setStatus("current")
_NsIdsAttkMonPingDeath_Type = Counter32
_NsIdsAttkMonPingDeath_Object = MibTableColumn
nsIdsAttkMonPingDeath = _NsIdsAttkMonPingDeath_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 6),
    _NsIdsAttkMonPingDeath_Type()
)
nsIdsAttkMonPingDeath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonPingDeath.setStatus("current")
_NsIdsAttkMonAddrSpoof_Type = Counter32
_NsIdsAttkMonAddrSpoof_Object = MibTableColumn
nsIdsAttkMonAddrSpoof = _NsIdsAttkMonAddrSpoof_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 7),
    _NsIdsAttkMonAddrSpoof_Type()
)
nsIdsAttkMonAddrSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonAddrSpoof.setStatus("current")
_NsIdsAttkMonLand_Type = Counter32
_NsIdsAttkMonLand_Object = MibTableColumn
nsIdsAttkMonLand = _NsIdsAttkMonLand_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 8),
    _NsIdsAttkMonLand_Type()
)
nsIdsAttkMonLand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonLand.setStatus("current")
_NsIdsAttkMonIcmpFlood_Type = Counter32
_NsIdsAttkMonIcmpFlood_Object = MibTableColumn
nsIdsAttkMonIcmpFlood = _NsIdsAttkMonIcmpFlood_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 9),
    _NsIdsAttkMonIcmpFlood_Type()
)
nsIdsAttkMonIcmpFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonIcmpFlood.setStatus("current")
_NsIdsAttkMonUdpFlood_Type = Counter32
_NsIdsAttkMonUdpFlood_Object = MibTableColumn
nsIdsAttkMonUdpFlood = _NsIdsAttkMonUdpFlood_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 10),
    _NsIdsAttkMonUdpFlood_Type()
)
nsIdsAttkMonUdpFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonUdpFlood.setStatus("current")
_NsIdsAttkMonWinnuke_Type = Counter32
_NsIdsAttkMonWinnuke_Object = MibTableColumn
nsIdsAttkMonWinnuke = _NsIdsAttkMonWinnuke_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 11),
    _NsIdsAttkMonWinnuke_Type()
)
nsIdsAttkMonWinnuke.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonWinnuke.setStatus("current")
_NsIdsAttkMonPortScan_Type = Counter32
_NsIdsAttkMonPortScan_Object = MibTableColumn
nsIdsAttkMonPortScan = _NsIdsAttkMonPortScan_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 12),
    _NsIdsAttkMonPortScan_Type()
)
nsIdsAttkMonPortScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonPortScan.setStatus("current")
_NsIdsAttkMonIpSweep_Type = Counter32
_NsIdsAttkMonIpSweep_Object = MibTableColumn
nsIdsAttkMonIpSweep = _NsIdsAttkMonIpSweep_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 13),
    _NsIdsAttkMonIpSweep_Type()
)
nsIdsAttkMonIpSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonIpSweep.setStatus("current")
_NsAttkMonSynFrag_Type = Counter32
_NsAttkMonSynFrag_Object = MibTableColumn
nsAttkMonSynFrag = _NsAttkMonSynFrag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 14),
    _NsAttkMonSynFrag_Type()
)
nsAttkMonSynFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonSynFrag.setStatus("current")
_NsAttkMonTcpNoFlag_Type = Counter32
_NsAttkMonTcpNoFlag_Object = MibTableColumn
nsAttkMonTcpNoFlag = _NsAttkMonTcpNoFlag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 15),
    _NsAttkMonTcpNoFlag_Type()
)
nsAttkMonTcpNoFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonTcpNoFlag.setStatus("current")
_NsAttkMonIpUnknownProt_Type = Counter32
_NsAttkMonIpUnknownProt_Object = MibTableColumn
nsAttkMonIpUnknownProt = _NsAttkMonIpUnknownProt_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 16),
    _NsAttkMonIpUnknownProt_Type()
)
nsAttkMonIpUnknownProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIpUnknownProt.setStatus("current")
_NsAttkMonIpOptBad_Type = Counter32
_NsAttkMonIpOptBad_Object = MibTableColumn
nsAttkMonIpOptBad = _NsAttkMonIpOptBad_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 17),
    _NsAttkMonIpOptBad_Type()
)
nsAttkMonIpOptBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIpOptBad.setStatus("current")
_NsAttkMonIpOptRecord_Type = Counter32
_NsAttkMonIpOptRecord_Object = MibTableColumn
nsAttkMonIpOptRecord = _NsAttkMonIpOptRecord_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 18),
    _NsAttkMonIpOptRecord_Type()
)
nsAttkMonIpOptRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIpOptRecord.setStatus("current")
_NsAttkMonIpOptTimestamp_Type = Counter32
_NsAttkMonIpOptTimestamp_Object = MibTableColumn
nsAttkMonIpOptTimestamp = _NsAttkMonIpOptTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 19),
    _NsAttkMonIpOptTimestamp_Type()
)
nsAttkMonIpOptTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIpOptTimestamp.setStatus("current")
_NsAttkMonIpOptSCHT_Type = Counter32
_NsAttkMonIpOptSCHT_Object = MibTableColumn
nsAttkMonIpOptSCHT = _NsAttkMonIpOptSCHT_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 20),
    _NsAttkMonIpOptSCHT_Type()
)
nsAttkMonIpOptSCHT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIpOptSCHT.setStatus("current")
_NsAttkMonIpOptLSR_Type = Counter32
_NsAttkMonIpOptLSR_Object = MibTableColumn
nsAttkMonIpOptLSR = _NsAttkMonIpOptLSR_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 21),
    _NsAttkMonIpOptLSR_Type()
)
nsAttkMonIpOptLSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIpOptLSR.setStatus("current")
_NsAttkMonIpOptSSR_Type = Counter32
_NsAttkMonIpOptSSR_Object = MibTableColumn
nsAttkMonIpOptSSR = _NsAttkMonIpOptSSR_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 22),
    _NsAttkMonIpOptSSR_Type()
)
nsAttkMonIpOptSSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIpOptSSR.setStatus("current")
_NsAttkMonIpOptStream_Type = Counter32
_NsAttkMonIpOptStream_Object = MibTableColumn
nsAttkMonIpOptStream = _NsAttkMonIpOptStream_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 23),
    _NsAttkMonIpOptStream_Type()
)
nsAttkMonIpOptStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIpOptStream.setStatus("current")
_NsAttkMonIcmpFrag_Type = Counter32
_NsAttkMonIcmpFrag_Object = MibTableColumn
nsAttkMonIcmpFrag = _NsAttkMonIcmpFrag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 24),
    _NsAttkMonIcmpFrag_Type()
)
nsAttkMonIcmpFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIcmpFrag.setStatus("current")
_NsAttkMonIcmpLarge_Type = Counter32
_NsAttkMonIcmpLarge_Object = MibTableColumn
nsAttkMonIcmpLarge = _NsAttkMonIcmpLarge_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 25),
    _NsAttkMonIcmpLarge_Type()
)
nsAttkMonIcmpLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIcmpLarge.setStatus("current")
_NsAttkMonTcpSynFin_Type = Counter32
_NsAttkMonTcpSynFin_Object = MibTableColumn
nsAttkMonTcpSynFin = _NsAttkMonTcpSynFin_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 26),
    _NsAttkMonTcpSynFin_Type()
)
nsAttkMonTcpSynFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonTcpSynFin.setStatus("current")
_NsAttkMonTcpFinNoAck_Type = Counter32
_NsAttkMonTcpFinNoAck_Object = MibTableColumn
nsAttkMonTcpFinNoAck = _NsAttkMonTcpFinNoAck_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 27),
    _NsAttkMonTcpFinNoAck_Type()
)
nsAttkMonTcpFinNoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonTcpFinNoAck.setStatus("current")
_NsAttkMonHttpMalUrl_Type = Counter32
_NsAttkMonHttpMalUrl_Object = MibTableColumn
nsAttkMonHttpMalUrl = _NsAttkMonHttpMalUrl_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 28),
    _NsAttkMonHttpMalUrl_Type()
)
nsAttkMonHttpMalUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonHttpMalUrl.setStatus("current")
_NsAttkMonSessMalNum_Type = Counter32
_NsAttkMonSessMalNum_Object = MibTableColumn
nsAttkMonSessMalNum = _NsAttkMonSessMalNum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 29),
    _NsAttkMonSessMalNum_Type()
)
nsAttkMonSessMalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonSessMalNum.setStatus("current")
_NsAttkMonSynAckAck_Type = Counter32
_NsAttkMonSynAckAck_Object = MibTableColumn
nsAttkMonSynAckAck = _NsAttkMonSynAckAck_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 30),
    _NsAttkMonSynAckAck_Type()
)
nsAttkMonSynAckAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonSynAckAck.setStatus("current")
_NsAttkMonIpFrag_Type = Counter32
_NsAttkMonIpFrag_Object = MibTableColumn
nsAttkMonIpFrag = _NsAttkMonIpFrag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 31),
    _NsAttkMonIpFrag_Type()
)
nsAttkMonIpFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAttkMonIpFrag.setStatus("current")


class _NsIdsAttkMonIfInfo_Type(Integer32):
    """Custom type nsIdsAttkMonIfInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIdsAttkMonIfInfo_Type.__name__ = "Integer32"
_NsIdsAttkMonIfInfo_Object = MibTableColumn
nsIdsAttkMonIfInfo = _NsIdsAttkMonIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 3, 2, 1, 32),
    _NsIdsAttkMonIfInfo_Type()
)
nsIdsAttkMonIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIdsAttkMonIfInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-IDS-MIB",
    **{"nsIdsProtect": nsIdsProtect,
       "nsIdsProtectSetTable": nsIdsProtectSetTable,
       "nsIdsProtectSetEntry": nsIdsProtectSetEntry,
       "nsIdsProtectZoneIdx": nsIdsProtectZoneIdx,
       "nsIdsDetectPingOfDeath": nsIdsDetectPingOfDeath,
       "nsIdsDetectTearDrop": nsIdsDetectTearDrop,
       "nsIdsDetectWinNuke": nsIdsDetectWinNuke,
       "nsIdsFilterIpSrcRoute": nsIdsFilterIpSrcRoute,
       "nsIdsDetectPortScan": nsIdsDetectPortScan,
       "nsIdsDetectAddrSweep": nsIdsDetectAddrSweep,
       "nsIdsDetectLand": nsIdsDetectLand,
       "nsIdsBlockComponent": nsIdsBlockComponent,
       "nsIdsDetectIpSpoof": nsIdsDetectIpSpoof,
       "nsIdsDetectSyn": nsIdsDetectSyn,
       "nsIdsDetectIcmpFlood": nsIdsDetectIcmpFlood,
       "nsIdsDetectUdpFlood": nsIdsDetectUdpFlood,
       "nsIdsDetectSynFrag": nsIdsDetectSynFrag,
       "nsIdsDetectTcpNoFlag": nsIdsDetectTcpNoFlag,
       "nsIdsDetectIpUnknownProt": nsIdsDetectIpUnknownProt,
       "nsIdsDetectIpOptBad": nsIdsDetectIpOptBad,
       "nsIdsDetectIpOptRecord": nsIdsDetectIpOptRecord,
       "nsIdsDetectIpOptTimestamp": nsIdsDetectIpOptTimestamp,
       "nsIdsDetectIpOptSCHT": nsIdsDetectIpOptSCHT,
       "nsIdsDetectIpOptLSR": nsIdsDetectIpOptLSR,
       "nsIdsDetectIpOptSSR": nsIdsDetectIpOptSSR,
       "nsIdsDetectIpOptStream": nsIdsDetectIpOptStream,
       "nsIdsDetectIcmpFrag": nsIdsDetectIcmpFrag,
       "nsIdsDetectIcmpLarge": nsIdsDetectIcmpLarge,
       "nsIdsDetectTcpSynFin": nsIdsDetectTcpSynFin,
       "nsIdsDetectTcpFinNoAck": nsIdsDetectTcpFinNoAck,
       "nsIdsHttpMalUrl": nsIdsHttpMalUrl,
       "nsIdsSessMalNum": nsIdsSessMalNum,
       "nsIdsDetectSynAckAck": nsIdsDetectSynAckAck,
       "nsIdsDetectIpFrag": nsIdsDetectIpFrag,
       "nsIdsProtectThreshTable": nsIdsProtectThreshTable,
       "nsIdsProtectThreshEntry": nsIdsProtectThreshEntry,
       "nsIdsProtectThreshZoneIdx": nsIdsProtectThreshZoneIdx,
       "nsIdsSynAttackThresh": nsIdsSynAttackThresh,
       "nsIdsSynAttackTimeout": nsIdsSynAttackTimeout,
       "nsIdsSynAttackAlmTh": nsIdsSynAttackAlmTh,
       "nsIdsSynAttackQueSize": nsIdsSynAttackQueSize,
       "nsIdsSynAttackAgeTime": nsIdsSynAttackAgeTime,
       "nsIdsIcmpFloodThresh": nsIdsIcmpFloodThresh,
       "nsIdsUdpFloodThresh": nsIdsUdpFloodThresh,
       "nsIdsPortScanThresh": nsIdsPortScanThresh,
       "nsIdsIpSweepThresh": nsIdsIpSweepThresh,
       "nsIdsSynAckAckThres": nsIdsSynAckAckThres,
       "nsIdsAttkMonTable": nsIdsAttkMonTable,
       "nsIdsAttkMonEntry": nsIdsAttkMonEntry,
       "nsIdsAttkMonIfIdx": nsIdsAttkMonIfIdx,
       "nsIdsAttkMonVsys": nsIdsAttkMonVsys,
       "nsIdsAttkMonSynAttk": nsIdsAttkMonSynAttk,
       "nsIdsAttkMonTearDrop": nsIdsAttkMonTearDrop,
       "nsIdsAttkMonSrcRoute": nsIdsAttkMonSrcRoute,
       "nsIdsAttkMonPingDeath": nsIdsAttkMonPingDeath,
       "nsIdsAttkMonAddrSpoof": nsIdsAttkMonAddrSpoof,
       "nsIdsAttkMonLand": nsIdsAttkMonLand,
       "nsIdsAttkMonIcmpFlood": nsIdsAttkMonIcmpFlood,
       "nsIdsAttkMonUdpFlood": nsIdsAttkMonUdpFlood,
       "nsIdsAttkMonWinnuke": nsIdsAttkMonWinnuke,
       "nsIdsAttkMonPortScan": nsIdsAttkMonPortScan,
       "nsIdsAttkMonIpSweep": nsIdsAttkMonIpSweep,
       "nsAttkMonSynFrag": nsAttkMonSynFrag,
       "nsAttkMonTcpNoFlag": nsAttkMonTcpNoFlag,
       "nsAttkMonIpUnknownProt": nsAttkMonIpUnknownProt,
       "nsAttkMonIpOptBad": nsAttkMonIpOptBad,
       "nsAttkMonIpOptRecord": nsAttkMonIpOptRecord,
       "nsAttkMonIpOptTimestamp": nsAttkMonIpOptTimestamp,
       "nsAttkMonIpOptSCHT": nsAttkMonIpOptSCHT,
       "nsAttkMonIpOptLSR": nsAttkMonIpOptLSR,
       "nsAttkMonIpOptSSR": nsAttkMonIpOptSSR,
       "nsAttkMonIpOptStream": nsAttkMonIpOptStream,
       "nsAttkMonIcmpFrag": nsAttkMonIcmpFrag,
       "nsAttkMonIcmpLarge": nsAttkMonIcmpLarge,
       "nsAttkMonTcpSynFin": nsAttkMonTcpSynFin,
       "nsAttkMonTcpFinNoAck": nsAttkMonTcpFinNoAck,
       "nsAttkMonHttpMalUrl": nsAttkMonHttpMalUrl,
       "nsAttkMonSessMalNum": nsAttkMonSessMalNum,
       "nsAttkMonSynAckAck": nsAttkMonSynAckAck,
       "nsAttkMonIpFrag": nsAttkMonIpFrag,
       "nsIdsAttkMonIfInfo": nsIdsAttkMonIfInfo}
)
