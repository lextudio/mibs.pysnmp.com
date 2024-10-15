# SNMP MIB module (BUNDLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BUNDLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:58 2024
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

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

nnbundleMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13)
)
nnbundleMib.setRevisions(
        ("1999-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnbundleTable_Object = MibTable
nnbundleTable = _NnbundleTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    nnbundleTable.setStatus("current")
_NnbundleTableEntry_Object = MibTableRow
nnbundleTableEntry = _NnbundleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1)
)
nnbundleTableEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
)
if mibBuilder.loadTexts:
    nnbundleTableEntry.setStatus("current")
_NnbundleId_Type = Integer32
_NnbundleId_Object = MibTableColumn
nnbundleId = _NnbundleId_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 1),
    _NnbundleId_Type()
)
nnbundleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnbundleId.setStatus("current")


class _NnbundleName_Type(DisplayString):
    """Custom type nnbundleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NnbundleName_Type.__name__ = "DisplayString"
_NnbundleName_Object = MibTableColumn
nnbundleName = _NnbundleName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 2),
    _NnbundleName_Type()
)
nnbundleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleName.setStatus("current")


class _NnbundleContact_Type(DisplayString):
    """Custom type nnbundleContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_NnbundleContact_Type.__name__ = "DisplayString"
_NnbundleContact_Object = MibTableColumn
nnbundleContact = _NnbundleContact_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 3),
    _NnbundleContact_Type()
)
nnbundleContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleContact.setStatus("current")


class _NnbundleDescr_Type(DisplayString):
    """Custom type nnbundleDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 76),
    )


_NnbundleDescr_Type.__name__ = "DisplayString"
_NnbundleDescr_Object = MibTableColumn
nnbundleDescr = _NnbundleDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 4),
    _NnbundleDescr_Type()
)
nnbundleDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDescr.setStatus("current")


class _NnbundleEncapsulation_Type(Integer32):
    """Custom type nnbundleEncapsulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 4),
          ("hdlc", 3),
          ("noEncap", 1),
          ("ppp", 2))
    )


_NnbundleEncapsulation_Type.__name__ = "Integer32"
_NnbundleEncapsulation_Object = MibTableColumn
nnbundleEncapsulation = _NnbundleEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 5),
    _NnbundleEncapsulation_Type()
)
nnbundleEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleEncapsulation.setStatus("current")


class _NnbundleDropEs_Type(Integer32):
    """Custom type nnbundleDropEs based on Integer32"""
    defaultValue = 0


_NnbundleDropEs_Object = MibTableColumn
nnbundleDropEs = _NnbundleDropEs_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 6),
    _NnbundleDropEs_Type()
)
nnbundleDropEs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropEs.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropEs.setUnits("seconds")


class _NnbundleDropSes_Type(Integer32):
    """Custom type nnbundleDropSes based on Integer32"""
    defaultValue = 0


_NnbundleDropSes_Object = MibTableColumn
nnbundleDropSes = _NnbundleDropSes_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 7),
    _NnbundleDropSes_Type()
)
nnbundleDropSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropSes.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropSes.setUnits("seconds")


class _NnbundleDropUas_Type(Integer32):
    """Custom type nnbundleDropUas based on Integer32"""
    defaultValue = 0


_NnbundleDropUas_Object = MibTableColumn
nnbundleDropUas = _NnbundleDropUas_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 8),
    _NnbundleDropUas_Type()
)
nnbundleDropUas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropUas.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropUas.setUnits("seconds")


class _NnbundleDropEev_Type(Integer32):
    """Custom type nnbundleDropEev based on Integer32"""
    defaultValue = 0


_NnbundleDropEev_Object = MibTableColumn
nnbundleDropEev = _NnbundleDropEev_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 9),
    _NnbundleDropEev_Type()
)
nnbundleDropEev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropEev.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropEev.setUnits("seconds")


class _NnbundleDropBes_Type(Integer32):
    """Custom type nnbundleDropBes based on Integer32"""
    defaultValue = 0


_NnbundleDropBes_Object = MibTableColumn
nnbundleDropBes = _NnbundleDropBes_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 10),
    _NnbundleDropBes_Type()
)
nnbundleDropBes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropBes.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropBes.setUnits("seconds")


class _NnbundleDropBbe_Type(Integer32):
    """Custom type nnbundleDropBbe based on Integer32"""
    defaultValue = 0


_NnbundleDropBbe_Object = MibTableColumn
nnbundleDropBbe = _NnbundleDropBbe_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 11),
    _NnbundleDropBbe_Type()
)
nnbundleDropBbe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropBbe.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropBbe.setUnits("seconds")


class _NnbundleDropLofc_Type(Integer32):
    """Custom type nnbundleDropLofc based on Integer32"""
    defaultValue = 0


_NnbundleDropLofc_Object = MibTableColumn
nnbundleDropLofc = _NnbundleDropLofc_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 12),
    _NnbundleDropLofc_Type()
)
nnbundleDropLofc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropLofc.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropLofc.setUnits("seconds")


class _NnbundleDropBpv_Type(Integer32):
    """Custom type nnbundleDropBpv based on Integer32"""
    defaultValue = 0


_NnbundleDropBpv_Object = MibTableColumn
nnbundleDropBpv = _NnbundleDropBpv_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 13),
    _NnbundleDropBpv_Type()
)
nnbundleDropBpv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropBpv.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropBpv.setUnits("seconds")


class _NnbundleDropCss_Type(Integer32):
    """Custom type nnbundleDropCss based on Integer32"""
    defaultValue = 0


_NnbundleDropCss_Object = MibTableColumn
nnbundleDropCss = _NnbundleDropCss_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 14),
    _NnbundleDropCss_Type()
)
nnbundleDropCss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropCss.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropCss.setUnits("seconds")


class _NnbundleDropOof_Type(Integer32):
    """Custom type nnbundleDropOof based on Integer32"""
    defaultValue = 0


_NnbundleDropOof_Object = MibTableColumn
nnbundleDropOof = _NnbundleDropOof_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 15),
    _NnbundleDropOof_Type()
)
nnbundleDropOof.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropOof.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropOof.setUnits("seconds")


class _NnbundleDropCrc_Type(Integer32):
    """Custom type nnbundleDropCrc based on Integer32"""
    defaultValue = 0


_NnbundleDropCrc_Object = MibTableColumn
nnbundleDropCrc = _NnbundleDropCrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 16),
    _NnbundleDropCrc_Type()
)
nnbundleDropCrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDropCrc.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleDropCrc.setUnits("seconds")


class _NnbundleIpAddr_Type(IpAddress):
    """Custom type nnbundleIpAddr based on IpAddress"""
    defaultValue = 0


_NnbundleIpAddr_Object = MibTableColumn
nnbundleIpAddr = _NnbundleIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 17),
    _NnbundleIpAddr_Type()
)
nnbundleIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleIpAddr.setStatus("current")


class _NnbundleSubnetMask_Type(IpAddress):
    """Custom type nnbundleSubnetMask based on IpAddress"""
    defaultValue = 0


_NnbundleSubnetMask_Object = MibTableColumn
nnbundleSubnetMask = _NnbundleSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 18),
    _NnbundleSubnetMask_Type()
)
nnbundleSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleSubnetMask.setStatus("current")


class _NnbundleSrcForwardingAddrPrimary_Type(IpAddress):
    """Custom type nnbundleSrcForwardingAddrPrimary based on IpAddress"""
    defaultValue = 0


_NnbundleSrcForwardingAddrPrimary_Object = MibTableColumn
nnbundleSrcForwardingAddrPrimary = _NnbundleSrcForwardingAddrPrimary_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 19),
    _NnbundleSrcForwardingAddrPrimary_Type()
)
nnbundleSrcForwardingAddrPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleSrcForwardingAddrPrimary.setStatus("current")


class _NnbundleSrcForwardingAddrSecondary_Type(IpAddress):
    """Custom type nnbundleSrcForwardingAddrSecondary based on IpAddress"""
    defaultValue = 0


_NnbundleSrcForwardingAddrSecondary_Object = MibTableColumn
nnbundleSrcForwardingAddrSecondary = _NnbundleSrcForwardingAddrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 20),
    _NnbundleSrcForwardingAddrSecondary_Type()
)
nnbundleSrcForwardingAddrSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleSrcForwardingAddrSecondary.setStatus("current")


class _NnbundleRestoreMethod_Type(Integer32):
    """Custom type nnbundleRestoreMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )


_NnbundleRestoreMethod_Type.__name__ = "Integer32"
_NnbundleRestoreMethod_Object = MibTableColumn
nnbundleRestoreMethod = _NnbundleRestoreMethod_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 21),
    _NnbundleRestoreMethod_Type()
)
nnbundleRestoreMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnbundleRestoreMethod.setStatus("current")


class _NnbundleLinkRestoralTime_Type(Integer32):
    """Custom type nnbundleLinkRestoralTime based on Integer32"""
    defaultValue = 120


_NnbundleLinkRestoralTime_Object = MibTableColumn
nnbundleLinkRestoralTime = _NnbundleLinkRestoralTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 22),
    _NnbundleLinkRestoralTime_Type()
)
nnbundleLinkRestoralTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleLinkRestoralTime.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleLinkRestoralTime.setUnits("seconds")


class _NnbundleStatus_Type(Integer32):
    """Custom type nnbundleStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NnbundleStatus_Type.__name__ = "Integer32"
_NnbundleStatus_Object = MibTableColumn
nnbundleStatus = _NnbundleStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 23),
    _NnbundleStatus_Type()
)
nnbundleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnbundleStatus.setStatus("current")


class _NnbundleLinkRestore_Type(OctetString):
    """Custom type nnbundleLinkRestore based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NnbundleLinkRestore_Type.__name__ = "OctetString"
_NnbundleLinkRestore_Object = MibTableColumn
nnbundleLinkRestore = _NnbundleLinkRestore_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 24),
    _NnbundleLinkRestore_Type()
)
nnbundleLinkRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnbundleLinkRestore.setStatus("current")
_NnbundleNoOfLinks_Type = Integer32
_NnbundleNoOfLinks_Object = MibTableColumn
nnbundleNoOfLinks = _NnbundleNoOfLinks_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 25),
    _NnbundleNoOfLinks_Type()
)
nnbundleNoOfLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnbundleNoOfLinks.setStatus("current")
_NnbundleTotalBw_Type = Integer32
_NnbundleTotalBw_Object = MibTableColumn
nnbundleTotalBw = _NnbundleTotalBw_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 26),
    _NnbundleTotalBw_Type()
)
nnbundleTotalBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnbundleTotalBw.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleTotalBw.setUnits("kbps")
_NnbundleRowStatus_Type = RowStatus
_NnbundleRowStatus_Object = MibTableColumn
nnbundleRowStatus = _NnbundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 27),
    _NnbundleRowStatus_Type()
)
nnbundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleRowStatus.setStatus("current")


class _NnbundleIpUnnumbered_Type(DisplayString):
    """Custom type nnbundleIpUnnumbered based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NnbundleIpUnnumbered_Type.__name__ = "DisplayString"
_NnbundleIpUnnumbered_Object = MibTableColumn
nnbundleIpUnnumbered = _NnbundleIpUnnumbered_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 28),
    _NnbundleIpUnnumbered_Type()
)
nnbundleIpUnnumbered.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleIpUnnumbered.setStatus("current")


class _NnbundleIpMulticast_Type(Integer32):
    """Custom type nnbundleIpMulticast based on Integer32"""
    defaultValue = 0

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
        *(("block", 2),
          ("noMcast", 0),
          ("ospfrip2", 3),
          ("pass", 1))
    )


_NnbundleIpMulticast_Type.__name__ = "Integer32"
_NnbundleIpMulticast_Object = MibTableColumn
nnbundleIpMulticast = _NnbundleIpMulticast_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 29),
    _NnbundleIpMulticast_Type()
)
nnbundleIpMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleIpMulticast.setStatus("current")


class _NnbundleDirectedBcast_Type(Integer32):
    """Custom type nnbundleDirectedBcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NnbundleDirectedBcast_Type.__name__ = "Integer32"
_NnbundleDirectedBcast_Object = MibTableColumn
nnbundleDirectedBcast = _NnbundleDirectedBcast_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 30),
    _NnbundleDirectedBcast_Type()
)
nnbundleDirectedBcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleDirectedBcast.setStatus("current")


class _NnbundleIcmpUnreachable_Type(Integer32):
    """Custom type nnbundleIcmpUnreachable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NnbundleIcmpUnreachable_Type.__name__ = "Integer32"
_NnbundleIcmpUnreachable_Object = MibTableColumn
nnbundleIcmpUnreachable = _NnbundleIcmpUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 31),
    _NnbundleIcmpUnreachable_Type()
)
nnbundleIcmpUnreachable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleIcmpUnreachable.setStatus("current")


class _NnbundleIcmpRedirect_Type(Integer32):
    """Custom type nnbundleIcmpRedirect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NnbundleIcmpRedirect_Type.__name__ = "Integer32"
_NnbundleIcmpRedirect_Object = MibTableColumn
nnbundleIcmpRedirect = _NnbundleIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 32),
    _NnbundleIcmpRedirect_Type()
)
nnbundleIcmpRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleIcmpRedirect.setStatus("current")
_NnbundleClearCounters_Type = Integer32
_NnbundleClearCounters_Object = MibTableColumn
nnbundleClearCounters = _NnbundleClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 33),
    _NnbundleClearCounters_Type()
)
nnbundleClearCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleClearCounters.setStatus("current")


class _NnbundleTrackHoldDownTimer_Type(Integer32):
    """Custom type nnbundleTrackHoldDownTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NnbundleTrackHoldDownTimer_Type.__name__ = "Integer32"
_NnbundleTrackHoldDownTimer_Object = MibTableColumn
nnbundleTrackHoldDownTimer = _NnbundleTrackHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 34),
    _NnbundleTrackHoldDownTimer_Type()
)
nnbundleTrackHoldDownTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleTrackHoldDownTimer.setStatus("current")
_NnbundleDropPackets_Type = Counter32
_NnbundleDropPackets_Object = MibTableColumn
nnbundleDropPackets = _NnbundleDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 1, 1, 35),
    _NnbundleDropPackets_Type()
)
nnbundleDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnbundleDropPackets.setStatus("current")
_NnbundleLinkTable_Object = MibTable
nnbundleLinkTable = _NnbundleLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2)
)
if mibBuilder.loadTexts:
    nnbundleLinkTable.setStatus("current")
_NnbundleLinkEntry_Object = MibTableRow
nnbundleLinkEntry = _NnbundleLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1)
)
nnbundleLinkEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
    (0, "BUNDLE-MIB", "nnbundleLinkT1Num"),
)
if mibBuilder.loadTexts:
    nnbundleLinkEntry.setStatus("current")
_NnbundleLinkT1Num_Type = Integer32
_NnbundleLinkT1Num_Object = MibTableColumn
nnbundleLinkT1Num = _NnbundleLinkT1Num_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1, 1),
    _NnbundleLinkT1Num_Type()
)
nnbundleLinkT1Num.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnbundleLinkT1Num.setStatus("current")


class _NnbundleLinkTimeSlots_Type(OctetString):
    """Custom type nnbundleLinkTimeSlots based on OctetString"""
    defaultValue = OctetString("00ffffff")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NnbundleLinkTimeSlots_Type.__name__ = "OctetString"
_NnbundleLinkTimeSlots_Object = MibTableColumn
nnbundleLinkTimeSlots = _NnbundleLinkTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1, 2),
    _NnbundleLinkTimeSlots_Type()
)
nnbundleLinkTimeSlots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleLinkTimeSlots.setStatus("current")


class _NnbundleLinkType_Type(Integer32):
    """Custom type nnbundleLinkType based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ct3", 1),
          ("e1", 3),
          ("fe1", 8),
          ("ft1", 7),
          ("hssi", 4),
          ("s232", 13),
          ("s449", 12),
          ("s530", 10),
          ("s530A", 11),
          ("t1", 2),
          ("t3", 5),
          ("v35", 6),
          ("x21", 9))
    )


_NnbundleLinkType_Type.__name__ = "Integer32"
_NnbundleLinkType_Object = MibTableColumn
nnbundleLinkType = _NnbundleLinkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1, 3),
    _NnbundleLinkType_Type()
)
nnbundleLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleLinkType.setStatus("current")


class _NnbundleLinkSpeed_Type(Integer32):
    """Custom type nnbundleLinkSpeed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps56", 1),
          ("kbps64", 2),
          ("notApplicable", 3))
    )


_NnbundleLinkSpeed_Type.__name__ = "Integer32"
_NnbundleLinkSpeed_Object = MibTableColumn
nnbundleLinkSpeed = _NnbundleLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1, 4),
    _NnbundleLinkSpeed_Type()
)
nnbundleLinkSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleLinkSpeed.setStatus("current")


class _NnbundleLinkInvertedData_Type(TruthValue):
    """Custom type nnbundleLinkInvertedData based on TruthValue"""


_NnbundleLinkInvertedData_Object = MibTableColumn
nnbundleLinkInvertedData = _NnbundleLinkInvertedData_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1, 5),
    _NnbundleLinkInvertedData_Type()
)
nnbundleLinkInvertedData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleLinkInvertedData.setStatus("current")


class _NnbundleLinkPhysIfNum_Type(Integer32):
    """Custom type nnbundleLinkPhysIfNum based on Integer32"""
    defaultValue = 0


_NnbundleLinkPhysIfNum_Object = MibTableColumn
nnbundleLinkPhysIfNum = _NnbundleLinkPhysIfNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1, 6),
    _NnbundleLinkPhysIfNum_Type()
)
nnbundleLinkPhysIfNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleLinkPhysIfNum.setStatus("current")
_NnbundleLinkDiffDelay_Type = Integer32
_NnbundleLinkDiffDelay_Object = MibTableColumn
nnbundleLinkDiffDelay = _NnbundleLinkDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1, 7),
    _NnbundleLinkDiffDelay_Type()
)
nnbundleLinkDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnbundleLinkDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleLinkDiffDelay.setUnits("milli-seconds")
_NnbundleLinkBw_Type = Integer32
_NnbundleLinkBw_Object = MibTableColumn
nnbundleLinkBw = _NnbundleLinkBw_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1, 8),
    _NnbundleLinkBw_Type()
)
nnbundleLinkBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnbundleLinkBw.setStatus("current")
if mibBuilder.loadTexts:
    nnbundleLinkBw.setUnits("kbps")


class _NnbundleLinkStatus_Type(Integer32):
    """Custom type nnbundleLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_NnbundleLinkStatus_Type.__name__ = "Integer32"
_NnbundleLinkStatus_Object = MibTableColumn
nnbundleLinkStatus = _NnbundleLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1, 9),
    _NnbundleLinkStatus_Type()
)
nnbundleLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnbundleLinkStatus.setStatus("current")
_NnbundleLinkRowStatus_Type = RowStatus
_NnbundleLinkRowStatus_Object = MibTableColumn
nnbundleLinkRowStatus = _NnbundleLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 2, 1, 10),
    _NnbundleLinkRowStatus_Type()
)
nnbundleLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnbundleLinkRowStatus.setStatus("current")
_NnbundleTrackTable_Object = MibTable
nnbundleTrackTable = _NnbundleTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 3)
)
if mibBuilder.loadTexts:
    nnbundleTrackTable.setStatus("current")
_NnbundleTrackEntry_Object = MibTableRow
nnbundleTrackEntry = _NnbundleTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 3, 1)
)
nnbundleTrackEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
    (0, "BUNDLE-MIB", "nntrackIntfId"),
)
if mibBuilder.loadTexts:
    nnbundleTrackEntry.setStatus("current")
_NntrackIntfId_Type = Integer32
_NntrackIntfId_Object = MibTableColumn
nntrackIntfId = _NntrackIntfId_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 3, 1, 1),
    _NntrackIntfId_Type()
)
nntrackIntfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nntrackIntfId.setStatus("current")


class _NntrackIntfName_Type(DisplayString):
    """Custom type nntrackIntfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NntrackIntfName_Type.__name__ = "DisplayString"
_NntrackIntfName_Object = MibTableColumn
nntrackIntfName = _NntrackIntfName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 3, 1, 2),
    _NntrackIntfName_Type()
)
nntrackIntfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nntrackIntfName.setStatus("current")


class _NntrackIntfStatus_Type(Integer32):
    """Custom type nntrackIntfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_NntrackIntfStatus_Type.__name__ = "Integer32"
_NntrackIntfStatus_Object = MibTableColumn
nntrackIntfStatus = _NntrackIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 3, 1, 3),
    _NntrackIntfStatus_Type()
)
nntrackIntfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntrackIntfStatus.setStatus("current")
_NntrackIntfRowStatus_Type = RowStatus
_NntrackIntfRowStatus_Object = MibTableColumn
nntrackIntfRowStatus = _NntrackIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 3, 1, 4),
    _NntrackIntfRowStatus_Type()
)
nntrackIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nntrackIntfRowStatus.setStatus("current")
_NnloopbackIfTable_Object = MibTable
nnloopbackIfTable = _NnloopbackIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 4)
)
if mibBuilder.loadTexts:
    nnloopbackIfTable.setStatus("current")
_NnloopbackIfTableEntry_Object = MibTableRow
nnloopbackIfTableEntry = _NnloopbackIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 4, 1)
)
nnloopbackIfTableEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnloopbackIfId"),
)
if mibBuilder.loadTexts:
    nnloopbackIfTableEntry.setStatus("current")
_NnloopbackIfId_Type = Integer32
_NnloopbackIfId_Object = MibTableColumn
nnloopbackIfId = _NnloopbackIfId_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 4, 1, 1),
    _NnloopbackIfId_Type()
)
nnloopbackIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnloopbackIfId.setStatus("current")


class _NnloopbackIfName_Type(DisplayString):
    """Custom type nnloopbackIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NnloopbackIfName_Type.__name__ = "DisplayString"
_NnloopbackIfName_Object = MibTableColumn
nnloopbackIfName = _NnloopbackIfName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 4, 1, 2),
    _NnloopbackIfName_Type()
)
nnloopbackIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnloopbackIfName.setStatus("current")


class _NnloopbackIfIpAddr_Type(IpAddress):
    """Custom type nnloopbackIfIpAddr based on IpAddress"""
    defaultValue = 0


_NnloopbackIfIpAddr_Object = MibTableColumn
nnloopbackIfIpAddr = _NnloopbackIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 4, 1, 3),
    _NnloopbackIfIpAddr_Type()
)
nnloopbackIfIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnloopbackIfIpAddr.setStatus("current")


class _NnloopbackIfSubnetMask_Type(IpAddress):
    """Custom type nnloopbackIfSubnetMask based on IpAddress"""
    defaultValue = 0


_NnloopbackIfSubnetMask_Object = MibTableColumn
nnloopbackIfSubnetMask = _NnloopbackIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 4, 1, 4),
    _NnloopbackIfSubnetMask_Type()
)
nnloopbackIfSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnloopbackIfSubnetMask.setStatus("current")


class _NnloopbackIfStatus_Type(Integer32):
    """Custom type nnloopbackIfStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_NnloopbackIfStatus_Type.__name__ = "Integer32"
_NnloopbackIfStatus_Object = MibTableColumn
nnloopbackIfStatus = _NnloopbackIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 4, 1, 5),
    _NnloopbackIfStatus_Type()
)
nnloopbackIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnloopbackIfStatus.setStatus("current")
_NnloopbackIfRowStatus_Type = RowStatus
_NnloopbackIfRowStatus_Object = MibTableColumn
nnloopbackIfRowStatus = _NnloopbackIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 4, 1, 6),
    _NnloopbackIfRowStatus_Type()
)
nnloopbackIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnloopbackIfRowStatus.setStatus("current")
_NnbundleTraps_ObjectIdentity = ObjectIdentity
nnbundleTraps = _NnbundleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5)
)
_NnbundleNotifications_ObjectIdentity = ObjectIdentity
nnbundleNotifications = _NnbundleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 0)
)
_NnbundleTrapVariables_ObjectIdentity = ObjectIdentity
nnbundleTrapVariables = _NnbundleTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1)
)


class _NnbundleNameStr_Type(DisplayString):
    """Custom type nnbundleNameStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NnbundleNameStr_Type.__name__ = "DisplayString"
_NnbundleNameStr_Object = MibScalar
nnbundleNameStr = _NnbundleNameStr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 1),
    _NnbundleNameStr_Type()
)
nnbundleNameStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnbundleNameStr.setStatus("current")


class _NnbundleDownCause_Type(Integer32):
    """Custom type nnbundleDownCause based on Integer32"""
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
        *(("admin-delete", 1),
          ("admin-down", 2),
          ("bcp-negotiation-fail", 5),
          ("bundle-track-down", 7),
          ("l1-failures", 3),
          ("l2-negotiation-fail", 4),
          ("l3-negotiation-fail", 6))
    )


_NnbundleDownCause_Type.__name__ = "Integer32"
_NnbundleDownCause_Object = MibScalar
nnbundleDownCause = _NnbundleDownCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 2),
    _NnbundleDownCause_Type()
)
nnbundleDownCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnbundleDownCause.setStatus("current")


class _NnbundleContactInfo_Type(DisplayString):
    """Custom type nnbundleContactInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_NnbundleContactInfo_Type.__name__ = "DisplayString"
_NnbundleContactInfo_Object = MibScalar
nnbundleContactInfo = _NnbundleContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 3),
    _NnbundleContactInfo_Type()
)
nnbundleContactInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnbundleContactInfo.setStatus("current")


class _NnbundleDescrInfo_Type(DisplayString):
    """Custom type nnbundleDescrInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_NnbundleDescrInfo_Type.__name__ = "DisplayString"
_NnbundleDescrInfo_Object = MibScalar
nnbundleDescrInfo = _NnbundleDescrInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 4),
    _NnbundleDescrInfo_Type()
)
nnbundleDescrInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnbundleDescrInfo.setStatus("current")


class _NnlinkNum_Type(DisplayString):
    """Custom type nnlinkNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_NnlinkNum_Type.__name__ = "DisplayString"
_NnlinkNum_Object = MibScalar
nnlinkNum = _NnlinkNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 5),
    _NnlinkNum_Type()
)
nnlinkNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnlinkNum.setStatus("current")


class _NnlinkType_Type(Integer32):
    """Custom type nnlinkType based on Integer32"""
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
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("e1", 3),
          ("e1-within-ce3", 4),
          ("fe1", 9),
          ("ft1", 8),
          ("hssi", 6),
          ("s232", 14),
          ("s449", 13),
          ("s530", 11),
          ("s530A", 12),
          ("t1", 1),
          ("t1-within-ct3", 2),
          ("t3", 5),
          ("v35", 7),
          ("x21", 10))
    )


_NnlinkType_Type.__name__ = "Integer32"
_NnlinkType_Object = MibScalar
nnlinkType = _NnlinkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 6),
    _NnlinkType_Type()
)
nnlinkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnlinkType.setStatus("current")


class _NnlinkCt3Num_Type(DisplayString):
    """Custom type nnlinkCt3Num based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_NnlinkCt3Num_Type.__name__ = "DisplayString"
_NnlinkCt3Num_Object = MibScalar
nnlinkCt3Num = _NnlinkCt3Num_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 7),
    _NnlinkCt3Num_Type()
)
nnlinkCt3Num.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnlinkCt3Num.setStatus("current")


class _NnlinkDownCause_Type(Integer32):
    """Custom type nnlinkDownCause based on Integer32"""
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
        *(("admin-delete", 1),
          ("admin-down", 2),
          ("diffdelay", 4),
          ("drop-config", 3),
          ("l1-failures", 5))
    )


_NnlinkDownCause_Type.__name__ = "Integer32"
_NnlinkDownCause_Object = MibScalar
nnlinkDownCause = _NnlinkDownCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 8),
    _NnlinkDownCause_Type()
)
nnlinkDownCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnlinkDownCause.setStatus("current")


class _NnlinkBundleName_Type(DisplayString):
    """Custom type nnlinkBundleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NnlinkBundleName_Type.__name__ = "DisplayString"
_NnlinkBundleName_Object = MibScalar
nnlinkBundleName = _NnlinkBundleName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 9),
    _NnlinkBundleName_Type()
)
nnlinkBundleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnlinkBundleName.setStatus("current")


class _NnlinkCircuitId_Type(DisplayString):
    """Custom type nnlinkCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnlinkCircuitId_Type.__name__ = "DisplayString"
_NnlinkCircuitId_Object = MibScalar
nnlinkCircuitId = _NnlinkCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 10),
    _NnlinkCircuitId_Type()
)
nnlinkCircuitId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnlinkCircuitId.setStatus("current")


class _NnlinkContactInfo_Type(DisplayString):
    """Custom type nnlinkContactInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnlinkContactInfo_Type.__name__ = "DisplayString"
_NnlinkContactInfo_Object = MibScalar
nnlinkContactInfo = _NnlinkContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 11),
    _NnlinkContactInfo_Type()
)
nnlinkContactInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnlinkContactInfo.setStatus("current")


class _NnlinkNameInfo_Type(DisplayString):
    """Custom type nnlinkNameInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NnlinkNameInfo_Type.__name__ = "DisplayString"
_NnlinkNameInfo_Object = MibScalar
nnlinkNameInfo = _NnlinkNameInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 12),
    _NnlinkNameInfo_Type()
)
nnlinkNameInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnlinkNameInfo.setStatus("current")


class _NnlinkDescrInfo_Type(DisplayString):
    """Custom type nnlinkDescrInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_NnlinkDescrInfo_Type.__name__ = "DisplayString"
_NnlinkDescrInfo_Object = MibScalar
nnlinkDescrInfo = _NnlinkDescrInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 1, 13),
    _NnlinkDescrInfo_Type()
)
nnlinkDescrInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnlinkDescrInfo.setStatus("current")


class _NnenableBundleUpDownNotification_Type(TruthValue):
    """Custom type nnenableBundleUpDownNotification based on TruthValue"""


_NnenableBundleUpDownNotification_Object = MibScalar
nnenableBundleUpDownNotification = _NnenableBundleUpDownNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 2),
    _NnenableBundleUpDownNotification_Type()
)
nnenableBundleUpDownNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableBundleUpDownNotification.setStatus("current")


class _NnenableLinkUpDownNotification_Type(TruthValue):
    """Custom type nnenableLinkUpDownNotification based on TruthValue"""


_NnenableLinkUpDownNotification_Object = MibScalar
nnenableLinkUpDownNotification = _NnenableLinkUpDownNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 3),
    _NnenableLinkUpDownNotification_Type()
)
nnenableLinkUpDownNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableLinkUpDownNotification.setStatus("current")

# Managed Objects groups


# Notification objects

nnbundleDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 0, 1)
)
nnbundleDownTrap.setObjects(
      *(("BUNDLE-MIB", "nnbundleNameStr"),
        ("BUNDLE-MIB", "nnbundleDownCause"),
        ("BUNDLE-MIB", "nnbundleContactInfo"),
        ("BUNDLE-MIB", "nnbundleDescrInfo"))
)
if mibBuilder.loadTexts:
    nnbundleDownTrap.setStatus(
        "current"
    )

nnbundleUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 0, 2)
)
nnbundleUpTrap.setObjects(
      *(("BUNDLE-MIB", "nnbundleNameStr"),
        ("BUNDLE-MIB", "nnbundleContactInfo"),
        ("BUNDLE-MIB", "nnbundleDescrInfo"))
)
if mibBuilder.loadTexts:
    nnbundleUpTrap.setStatus(
        "current"
    )

nnlinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 0, 3)
)
nnlinkDownTrap.setObjects(
      *(("BUNDLE-MIB", "nnlinkNum"),
        ("BUNDLE-MIB", "nnlinkType"),
        ("BUNDLE-MIB", "nnlinkCt3Num"),
        ("BUNDLE-MIB", "nnlinkDownCause"),
        ("BUNDLE-MIB", "nnlinkBundleName"),
        ("BUNDLE-MIB", "nnlinkCircuitId"),
        ("BUNDLE-MIB", "nnlinkContactInfo"),
        ("BUNDLE-MIB", "nnlinkNameInfo"),
        ("BUNDLE-MIB", "nnlinkDescrInfo"))
)
if mibBuilder.loadTexts:
    nnlinkDownTrap.setStatus(
        "current"
    )

nnlinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 5, 0, 4)
)
nnlinkUpTrap.setObjects(
      *(("BUNDLE-MIB", "nnlinkNum"),
        ("BUNDLE-MIB", "nnlinkType"),
        ("BUNDLE-MIB", "nnlinkCt3Num"),
        ("BUNDLE-MIB", "nnlinkBundleName"),
        ("BUNDLE-MIB", "nnlinkCircuitId"),
        ("BUNDLE-MIB", "nnlinkContactInfo"),
        ("BUNDLE-MIB", "nnlinkNameInfo"),
        ("BUNDLE-MIB", "nnlinkDescrInfo"))
)
if mibBuilder.loadTexts:
    nnlinkUpTrap.setStatus(
        "current"
    )


# Notifications groups

nnbundleNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 13, 6)
)
nnbundleNotificationGroup.setObjects(
      *(("BUNDLE-MIB", "nnbundleDownTrap"),
        ("BUNDLE-MIB", "nnbundleUpTrap"),
        ("BUNDLE-MIB", "nnlinkDownTrap"),
        ("BUNDLE-MIB", "nnlinkUpTrap"))
)
if mibBuilder.loadTexts:
    nnbundleNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BUNDLE-MIB",
    **{"nnbundleMib": nnbundleMib,
       "nnbundleTable": nnbundleTable,
       "nnbundleTableEntry": nnbundleTableEntry,
       "nnbundleId": nnbundleId,
       "nnbundleName": nnbundleName,
       "nnbundleContact": nnbundleContact,
       "nnbundleDescr": nnbundleDescr,
       "nnbundleEncapsulation": nnbundleEncapsulation,
       "nnbundleDropEs": nnbundleDropEs,
       "nnbundleDropSes": nnbundleDropSes,
       "nnbundleDropUas": nnbundleDropUas,
       "nnbundleDropEev": nnbundleDropEev,
       "nnbundleDropBes": nnbundleDropBes,
       "nnbundleDropBbe": nnbundleDropBbe,
       "nnbundleDropLofc": nnbundleDropLofc,
       "nnbundleDropBpv": nnbundleDropBpv,
       "nnbundleDropCss": nnbundleDropCss,
       "nnbundleDropOof": nnbundleDropOof,
       "nnbundleDropCrc": nnbundleDropCrc,
       "nnbundleIpAddr": nnbundleIpAddr,
       "nnbundleSubnetMask": nnbundleSubnetMask,
       "nnbundleSrcForwardingAddrPrimary": nnbundleSrcForwardingAddrPrimary,
       "nnbundleSrcForwardingAddrSecondary": nnbundleSrcForwardingAddrSecondary,
       "nnbundleRestoreMethod": nnbundleRestoreMethod,
       "nnbundleLinkRestoralTime": nnbundleLinkRestoralTime,
       "nnbundleStatus": nnbundleStatus,
       "nnbundleLinkRestore": nnbundleLinkRestore,
       "nnbundleNoOfLinks": nnbundleNoOfLinks,
       "nnbundleTotalBw": nnbundleTotalBw,
       "nnbundleRowStatus": nnbundleRowStatus,
       "nnbundleIpUnnumbered": nnbundleIpUnnumbered,
       "nnbundleIpMulticast": nnbundleIpMulticast,
       "nnbundleDirectedBcast": nnbundleDirectedBcast,
       "nnbundleIcmpUnreachable": nnbundleIcmpUnreachable,
       "nnbundleIcmpRedirect": nnbundleIcmpRedirect,
       "nnbundleClearCounters": nnbundleClearCounters,
       "nnbundleTrackHoldDownTimer": nnbundleTrackHoldDownTimer,
       "nnbundleDropPackets": nnbundleDropPackets,
       "nnbundleLinkTable": nnbundleLinkTable,
       "nnbundleLinkEntry": nnbundleLinkEntry,
       "nnbundleLinkT1Num": nnbundleLinkT1Num,
       "nnbundleLinkTimeSlots": nnbundleLinkTimeSlots,
       "nnbundleLinkType": nnbundleLinkType,
       "nnbundleLinkSpeed": nnbundleLinkSpeed,
       "nnbundleLinkInvertedData": nnbundleLinkInvertedData,
       "nnbundleLinkPhysIfNum": nnbundleLinkPhysIfNum,
       "nnbundleLinkDiffDelay": nnbundleLinkDiffDelay,
       "nnbundleLinkBw": nnbundleLinkBw,
       "nnbundleLinkStatus": nnbundleLinkStatus,
       "nnbundleLinkRowStatus": nnbundleLinkRowStatus,
       "nnbundleTrackTable": nnbundleTrackTable,
       "nnbundleTrackEntry": nnbundleTrackEntry,
       "nntrackIntfId": nntrackIntfId,
       "nntrackIntfName": nntrackIntfName,
       "nntrackIntfStatus": nntrackIntfStatus,
       "nntrackIntfRowStatus": nntrackIntfRowStatus,
       "nnloopbackIfTable": nnloopbackIfTable,
       "nnloopbackIfTableEntry": nnloopbackIfTableEntry,
       "nnloopbackIfId": nnloopbackIfId,
       "nnloopbackIfName": nnloopbackIfName,
       "nnloopbackIfIpAddr": nnloopbackIfIpAddr,
       "nnloopbackIfSubnetMask": nnloopbackIfSubnetMask,
       "nnloopbackIfStatus": nnloopbackIfStatus,
       "nnloopbackIfRowStatus": nnloopbackIfRowStatus,
       "nnbundleTraps": nnbundleTraps,
       "nnbundleNotifications": nnbundleNotifications,
       "nnbundleDownTrap": nnbundleDownTrap,
       "nnbundleUpTrap": nnbundleUpTrap,
       "nnlinkDownTrap": nnlinkDownTrap,
       "nnlinkUpTrap": nnlinkUpTrap,
       "nnbundleTrapVariables": nnbundleTrapVariables,
       "nnbundleNameStr": nnbundleNameStr,
       "nnbundleDownCause": nnbundleDownCause,
       "nnbundleContactInfo": nnbundleContactInfo,
       "nnbundleDescrInfo": nnbundleDescrInfo,
       "nnlinkNum": nnlinkNum,
       "nnlinkType": nnlinkType,
       "nnlinkCt3Num": nnlinkCt3Num,
       "nnlinkDownCause": nnlinkDownCause,
       "nnlinkBundleName": nnlinkBundleName,
       "nnlinkCircuitId": nnlinkCircuitId,
       "nnlinkContactInfo": nnlinkContactInfo,
       "nnlinkNameInfo": nnlinkNameInfo,
       "nnlinkDescrInfo": nnlinkDescrInfo,
       "nnenableBundleUpDownNotification": nnenableBundleUpDownNotification,
       "nnenableLinkUpDownNotification": nnenableLinkUpDownNotification,
       "nnbundleNotificationGroup": nnbundleNotificationGroup}
)
