# SNMP MIB module (HPN-ICF-MP-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MP-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:08 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

hpnicfMultilinkPPPV2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140)
)
hpnicfMultilinkPPPV2.setRevisions(
        ("2013-07-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfMpObjectsV2_ObjectIdentity = ObjectIdentity
hpnicfMpObjectsV2 = _HpnicfMpObjectsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1)
)
_HpnicfMpMultilinkV2Table_Object = MibTable
hpnicfMpMultilinkV2Table = _HpnicfMpMultilinkV2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfMpMultilinkV2Table.setStatus("current")
_HpnicfMpMultilinkV2Entry_Object = MibTableRow
hpnicfMpMultilinkV2Entry = _HpnicfMpMultilinkV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1)
)
hpnicfMpMultilinkV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMpMultilinkV2Entry.setStatus("current")


class _HpnicfMpMultilinkDescrV2_Type(DisplayString):
    """Custom type hpnicfMpMultilinkDescrV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfMpMultilinkDescrV2_Type.__name__ = "DisplayString"
_HpnicfMpMultilinkDescrV2_Object = MibTableColumn
hpnicfMpMultilinkDescrV2 = _HpnicfMpMultilinkDescrV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 1),
    _HpnicfMpMultilinkDescrV2_Type()
)
hpnicfMpMultilinkDescrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpMultilinkDescrV2.setStatus("current")


class _HpnicfMpBundleNameV2_Type(DisplayString):
    """Custom type hpnicfMpBundleNameV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfMpBundleNameV2_Type.__name__ = "DisplayString"
_HpnicfMpBundleNameV2_Object = MibTableColumn
hpnicfMpBundleNameV2 = _HpnicfMpBundleNameV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 2),
    _HpnicfMpBundleNameV2_Type()
)
hpnicfMpBundleNameV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpBundleNameV2.setStatus("current")
_HpnicfMpBundledSlotV2_Type = Integer32
_HpnicfMpBundledSlotV2_Object = MibTableColumn
hpnicfMpBundledSlotV2 = _HpnicfMpBundledSlotV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 3),
    _HpnicfMpBundledSlotV2_Type()
)
hpnicfMpBundledSlotV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpBundledSlotV2.setStatus("current")
_HpnicfMpBundledMemberCntV2_Type = Integer32
_HpnicfMpBundledMemberCntV2_Object = MibTableColumn
hpnicfMpBundledMemberCntV2 = _HpnicfMpBundledMemberCntV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 4),
    _HpnicfMpBundledMemberCntV2_Type()
)
hpnicfMpBundledMemberCntV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpBundledMemberCntV2.setStatus("current")
_HpnicfMpLostFragmentsV2_Type = Counter32
_HpnicfMpLostFragmentsV2_Object = MibTableColumn
hpnicfMpLostFragmentsV2 = _HpnicfMpLostFragmentsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 5),
    _HpnicfMpLostFragmentsV2_Type()
)
hpnicfMpLostFragmentsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpLostFragmentsV2.setStatus("current")
_HpnicfMpReorderedPktsV2_Type = Counter32
_HpnicfMpReorderedPktsV2_Object = MibTableColumn
hpnicfMpReorderedPktsV2 = _HpnicfMpReorderedPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 6),
    _HpnicfMpReorderedPktsV2_Type()
)
hpnicfMpReorderedPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpReorderedPktsV2.setStatus("current")
_HpnicfMpUnassignedPktsV2_Type = Counter32
_HpnicfMpUnassignedPktsV2_Object = MibTableColumn
hpnicfMpUnassignedPktsV2 = _HpnicfMpUnassignedPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 7),
    _HpnicfMpUnassignedPktsV2_Type()
)
hpnicfMpUnassignedPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpUnassignedPktsV2.setStatus("current")
_HpnicfMpInterleavedPktsV2_Type = Counter32
_HpnicfMpInterleavedPktsV2_Object = MibTableColumn
hpnicfMpInterleavedPktsV2 = _HpnicfMpInterleavedPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 8),
    _HpnicfMpInterleavedPktsV2_Type()
)
hpnicfMpInterleavedPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpInterleavedPktsV2.setStatus("current")
_HpnicfMpRcvdSequenceV2_Type = Integer32
_HpnicfMpRcvdSequenceV2_Object = MibTableColumn
hpnicfMpRcvdSequenceV2 = _HpnicfMpRcvdSequenceV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 9),
    _HpnicfMpRcvdSequenceV2_Type()
)
hpnicfMpRcvdSequenceV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpRcvdSequenceV2.setStatus("current")
_HpnicfMpSentSequenceV2_Type = Integer32
_HpnicfMpSentSequenceV2_Object = MibTableColumn
hpnicfMpSentSequenceV2 = _HpnicfMpSentSequenceV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 10),
    _HpnicfMpSentSequenceV2_Type()
)
hpnicfMpSentSequenceV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpSentSequenceV2.setStatus("current")
_HpnicfMpMemberlinkV2Table_Object = MibTable
hpnicfMpMemberlinkV2Table = _HpnicfMpMemberlinkV2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkV2Table.setStatus("current")
_HpnicfMpMemberlinkV2Entry_Object = MibTableRow
hpnicfMpMemberlinkV2Entry = _HpnicfMpMemberlinkV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2, 1)
)
hpnicfMpMemberlinkV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-MP-V2-MIB", "hpnicfMpMemberlinkSeqNumberV2"),
)
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkV2Entry.setStatus("current")


class _HpnicfMpMemberlinkSeqNumberV2_Type(Integer32):
    """Custom type hpnicfMpMemberlinkSeqNumberV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HpnicfMpMemberlinkSeqNumberV2_Type.__name__ = "Integer32"
_HpnicfMpMemberlinkSeqNumberV2_Object = MibTableColumn
hpnicfMpMemberlinkSeqNumberV2 = _HpnicfMpMemberlinkSeqNumberV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2, 1, 1),
    _HpnicfMpMemberlinkSeqNumberV2_Type()
)
hpnicfMpMemberlinkSeqNumberV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkSeqNumberV2.setStatus("current")
_HpnicfMpMemberlinkIfIndexV2_Type = Integer32
_HpnicfMpMemberlinkIfIndexV2_Object = MibTableColumn
hpnicfMpMemberlinkIfIndexV2 = _HpnicfMpMemberlinkIfIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2, 1, 2),
    _HpnicfMpMemberlinkIfIndexV2_Type()
)
hpnicfMpMemberlinkIfIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkIfIndexV2.setStatus("current")


class _HpnicfMpMemberlinkDescrV2_Type(DisplayString):
    """Custom type hpnicfMpMemberlinkDescrV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfMpMemberlinkDescrV2_Type.__name__ = "DisplayString"
_HpnicfMpMemberlinkDescrV2_Object = MibTableColumn
hpnicfMpMemberlinkDescrV2 = _HpnicfMpMemberlinkDescrV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2, 1, 3),
    _HpnicfMpMemberlinkDescrV2_Type()
)
hpnicfMpMemberlinkDescrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkDescrV2.setStatus("current")


class _HpnicfMpMemberlinkMpStatusV2_Type(Integer32):
    """Custom type hpnicfMpMemberlinkMpStatusV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HpnicfMpMemberlinkMpStatusV2_Type.__name__ = "Integer32"
_HpnicfMpMemberlinkMpStatusV2_Object = MibTableColumn
hpnicfMpMemberlinkMpStatusV2 = _HpnicfMpMemberlinkMpStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2, 1, 4),
    _HpnicfMpMemberlinkMpStatusV2_Type()
)
hpnicfMpMemberlinkMpStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkMpStatusV2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MP-V2-MIB",
    **{"hpnicfMultilinkPPPV2": hpnicfMultilinkPPPV2,
       "hpnicfMpObjectsV2": hpnicfMpObjectsV2,
       "hpnicfMpMultilinkV2Table": hpnicfMpMultilinkV2Table,
       "hpnicfMpMultilinkV2Entry": hpnicfMpMultilinkV2Entry,
       "hpnicfMpMultilinkDescrV2": hpnicfMpMultilinkDescrV2,
       "hpnicfMpBundleNameV2": hpnicfMpBundleNameV2,
       "hpnicfMpBundledSlotV2": hpnicfMpBundledSlotV2,
       "hpnicfMpBundledMemberCntV2": hpnicfMpBundledMemberCntV2,
       "hpnicfMpLostFragmentsV2": hpnicfMpLostFragmentsV2,
       "hpnicfMpReorderedPktsV2": hpnicfMpReorderedPktsV2,
       "hpnicfMpUnassignedPktsV2": hpnicfMpUnassignedPktsV2,
       "hpnicfMpInterleavedPktsV2": hpnicfMpInterleavedPktsV2,
       "hpnicfMpRcvdSequenceV2": hpnicfMpRcvdSequenceV2,
       "hpnicfMpSentSequenceV2": hpnicfMpSentSequenceV2,
       "hpnicfMpMemberlinkV2Table": hpnicfMpMemberlinkV2Table,
       "hpnicfMpMemberlinkV2Entry": hpnicfMpMemberlinkV2Entry,
       "hpnicfMpMemberlinkSeqNumberV2": hpnicfMpMemberlinkSeqNumberV2,
       "hpnicfMpMemberlinkIfIndexV2": hpnicfMpMemberlinkIfIndexV2,
       "hpnicfMpMemberlinkDescrV2": hpnicfMpMemberlinkDescrV2,
       "hpnicfMpMemberlinkMpStatusV2": hpnicfMpMemberlinkMpStatusV2}
)
