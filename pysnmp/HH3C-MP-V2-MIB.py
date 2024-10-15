# SNMP MIB module (HH3C-MP-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MP-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:09 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cMultilinkPPPV2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140)
)
hh3cMultilinkPPPV2.setRevisions(
        ("2013-07-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cMpObjectsV2_ObjectIdentity = ObjectIdentity
hh3cMpObjectsV2 = _Hh3cMpObjectsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1)
)
_Hh3cMpMultilinkV2Table_Object = MibTable
hh3cMpMultilinkV2Table = _Hh3cMpMultilinkV2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cMpMultilinkV2Table.setStatus("current")
_Hh3cMpMultilinkV2Entry_Object = MibTableRow
hh3cMpMultilinkV2Entry = _Hh3cMpMultilinkV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1)
)
hh3cMpMultilinkV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cMpMultilinkV2Entry.setStatus("current")


class _Hh3cMpMultilinkDescrV2_Type(DisplayString):
    """Custom type hh3cMpMultilinkDescrV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cMpMultilinkDescrV2_Type.__name__ = "DisplayString"
_Hh3cMpMultilinkDescrV2_Object = MibTableColumn
hh3cMpMultilinkDescrV2 = _Hh3cMpMultilinkDescrV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1, 1),
    _Hh3cMpMultilinkDescrV2_Type()
)
hh3cMpMultilinkDescrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpMultilinkDescrV2.setStatus("current")


class _Hh3cMpBundleNameV2_Type(DisplayString):
    """Custom type hh3cMpBundleNameV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cMpBundleNameV2_Type.__name__ = "DisplayString"
_Hh3cMpBundleNameV2_Object = MibTableColumn
hh3cMpBundleNameV2 = _Hh3cMpBundleNameV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1, 2),
    _Hh3cMpBundleNameV2_Type()
)
hh3cMpBundleNameV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpBundleNameV2.setStatus("current")
_Hh3cMpBundledSlotV2_Type = Integer32
_Hh3cMpBundledSlotV2_Object = MibTableColumn
hh3cMpBundledSlotV2 = _Hh3cMpBundledSlotV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1, 3),
    _Hh3cMpBundledSlotV2_Type()
)
hh3cMpBundledSlotV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpBundledSlotV2.setStatus("current")
_Hh3cMpBundledMemberCntV2_Type = Integer32
_Hh3cMpBundledMemberCntV2_Object = MibTableColumn
hh3cMpBundledMemberCntV2 = _Hh3cMpBundledMemberCntV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1, 4),
    _Hh3cMpBundledMemberCntV2_Type()
)
hh3cMpBundledMemberCntV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpBundledMemberCntV2.setStatus("current")
_Hh3cMpLostFragmentsV2_Type = Counter32
_Hh3cMpLostFragmentsV2_Object = MibTableColumn
hh3cMpLostFragmentsV2 = _Hh3cMpLostFragmentsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1, 5),
    _Hh3cMpLostFragmentsV2_Type()
)
hh3cMpLostFragmentsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpLostFragmentsV2.setStatus("current")
_Hh3cMpReorderedPktsV2_Type = Counter32
_Hh3cMpReorderedPktsV2_Object = MibTableColumn
hh3cMpReorderedPktsV2 = _Hh3cMpReorderedPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1, 6),
    _Hh3cMpReorderedPktsV2_Type()
)
hh3cMpReorderedPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpReorderedPktsV2.setStatus("current")
_Hh3cMpUnassignedPktsV2_Type = Counter32
_Hh3cMpUnassignedPktsV2_Object = MibTableColumn
hh3cMpUnassignedPktsV2 = _Hh3cMpUnassignedPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1, 7),
    _Hh3cMpUnassignedPktsV2_Type()
)
hh3cMpUnassignedPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpUnassignedPktsV2.setStatus("current")
_Hh3cMpInterleavedPktsV2_Type = Counter32
_Hh3cMpInterleavedPktsV2_Object = MibTableColumn
hh3cMpInterleavedPktsV2 = _Hh3cMpInterleavedPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1, 8),
    _Hh3cMpInterleavedPktsV2_Type()
)
hh3cMpInterleavedPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpInterleavedPktsV2.setStatus("current")
_Hh3cMpRcvdSequenceV2_Type = Integer32
_Hh3cMpRcvdSequenceV2_Object = MibTableColumn
hh3cMpRcvdSequenceV2 = _Hh3cMpRcvdSequenceV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1, 9),
    _Hh3cMpRcvdSequenceV2_Type()
)
hh3cMpRcvdSequenceV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpRcvdSequenceV2.setStatus("current")
_Hh3cMpSentSequenceV2_Type = Integer32
_Hh3cMpSentSequenceV2_Object = MibTableColumn
hh3cMpSentSequenceV2 = _Hh3cMpSentSequenceV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 1, 1, 10),
    _Hh3cMpSentSequenceV2_Type()
)
hh3cMpSentSequenceV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpSentSequenceV2.setStatus("current")
_Hh3cMpMemberlinkV2Table_Object = MibTable
hh3cMpMemberlinkV2Table = _Hh3cMpMemberlinkV2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cMpMemberlinkV2Table.setStatus("current")
_Hh3cMpMemberlinkV2Entry_Object = MibTableRow
hh3cMpMemberlinkV2Entry = _Hh3cMpMemberlinkV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 2, 1)
)
hh3cMpMemberlinkV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-MP-V2-MIB", "hh3cMpMemberlinkSeqNumberV2"),
)
if mibBuilder.loadTexts:
    hh3cMpMemberlinkV2Entry.setStatus("current")


class _Hh3cMpMemberlinkSeqNumberV2_Type(Integer32):
    """Custom type hh3cMpMemberlinkSeqNumberV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hh3cMpMemberlinkSeqNumberV2_Type.__name__ = "Integer32"
_Hh3cMpMemberlinkSeqNumberV2_Object = MibTableColumn
hh3cMpMemberlinkSeqNumberV2 = _Hh3cMpMemberlinkSeqNumberV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 2, 1, 1),
    _Hh3cMpMemberlinkSeqNumberV2_Type()
)
hh3cMpMemberlinkSeqNumberV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpMemberlinkSeqNumberV2.setStatus("current")
_Hh3cMpMemberlinkIfIndexV2_Type = Integer32
_Hh3cMpMemberlinkIfIndexV2_Object = MibTableColumn
hh3cMpMemberlinkIfIndexV2 = _Hh3cMpMemberlinkIfIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 2, 1, 2),
    _Hh3cMpMemberlinkIfIndexV2_Type()
)
hh3cMpMemberlinkIfIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpMemberlinkIfIndexV2.setStatus("current")


class _Hh3cMpMemberlinkDescrV2_Type(DisplayString):
    """Custom type hh3cMpMemberlinkDescrV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cMpMemberlinkDescrV2_Type.__name__ = "DisplayString"
_Hh3cMpMemberlinkDescrV2_Object = MibTableColumn
hh3cMpMemberlinkDescrV2 = _Hh3cMpMemberlinkDescrV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 2, 1, 3),
    _Hh3cMpMemberlinkDescrV2_Type()
)
hh3cMpMemberlinkDescrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpMemberlinkDescrV2.setStatus("current")


class _Hh3cMpMemberlinkMpStatusV2_Type(Integer32):
    """Custom type hh3cMpMemberlinkMpStatusV2 based on Integer32"""
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


_Hh3cMpMemberlinkMpStatusV2_Type.__name__ = "Integer32"
_Hh3cMpMemberlinkMpStatusV2_Object = MibTableColumn
hh3cMpMemberlinkMpStatusV2 = _Hh3cMpMemberlinkMpStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140, 1, 2, 1, 4),
    _Hh3cMpMemberlinkMpStatusV2_Type()
)
hh3cMpMemberlinkMpStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpMemberlinkMpStatusV2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MP-V2-MIB",
    **{"hh3cMultilinkPPPV2": hh3cMultilinkPPPV2,
       "hh3cMpObjectsV2": hh3cMpObjectsV2,
       "hh3cMpMultilinkV2Table": hh3cMpMultilinkV2Table,
       "hh3cMpMultilinkV2Entry": hh3cMpMultilinkV2Entry,
       "hh3cMpMultilinkDescrV2": hh3cMpMultilinkDescrV2,
       "hh3cMpBundleNameV2": hh3cMpBundleNameV2,
       "hh3cMpBundledSlotV2": hh3cMpBundledSlotV2,
       "hh3cMpBundledMemberCntV2": hh3cMpBundledMemberCntV2,
       "hh3cMpLostFragmentsV2": hh3cMpLostFragmentsV2,
       "hh3cMpReorderedPktsV2": hh3cMpReorderedPktsV2,
       "hh3cMpUnassignedPktsV2": hh3cMpUnassignedPktsV2,
       "hh3cMpInterleavedPktsV2": hh3cMpInterleavedPktsV2,
       "hh3cMpRcvdSequenceV2": hh3cMpRcvdSequenceV2,
       "hh3cMpSentSequenceV2": hh3cMpSentSequenceV2,
       "hh3cMpMemberlinkV2Table": hh3cMpMemberlinkV2Table,
       "hh3cMpMemberlinkV2Entry": hh3cMpMemberlinkV2Entry,
       "hh3cMpMemberlinkSeqNumberV2": hh3cMpMemberlinkSeqNumberV2,
       "hh3cMpMemberlinkIfIndexV2": hh3cMpMemberlinkIfIndexV2,
       "hh3cMpMemberlinkDescrV2": hh3cMpMemberlinkDescrV2,
       "hh3cMpMemberlinkMpStatusV2": hh3cMpMemberlinkMpStatusV2}
)
