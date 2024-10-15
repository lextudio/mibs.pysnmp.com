# SNMP MIB module (Hub-rptr-prvt-sec) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Hub-rptr-prvt-sec
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:55 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 internet,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "internet",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Fibronics_ObjectIdentity = ObjectIdentity
fibronics = _Fibronics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101)
)
_Mibseth_rptrs_ObjectIdentity = ObjectIdentity
mibseth_rptrs = _Mibseth_rptrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 8)
)
_RptrSecurityInfo_ObjectIdentity = ObjectIdentity
rptrSecurityInfo = _RptrSecurityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5)
)
_PrptrSecurityGroupTable_Object = MibTable
prptrSecurityGroupTable = _PrptrSecurityGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1)
)
if mibBuilder.loadTexts:
    prptrSecurityGroupTable.setStatus("mandatory")
_PrptrSecurityGroupEntry_Object = MibTableRow
prptrSecurityGroupEntry = _PrptrSecurityGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1)
)
prptrSecurityGroupEntry.setIndexNames(
    (0, "Hub-rptr-prvt-sec", "prptrSecurityGroupIndex"),
)
if mibBuilder.loadTexts:
    prptrSecurityGroupEntry.setStatus("mandatory")


class _PrptrSecurityGroupIndex_Type(Integer32):
    """Custom type prptrSecurityGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PrptrSecurityGroupIndex_Type.__name__ = "Integer32"
_PrptrSecurityGroupIndex_Object = MibTableColumn
prptrSecurityGroupIndex = _PrptrSecurityGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 1),
    _PrptrSecurityGroupIndex_Type()
)
prptrSecurityGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prptrSecurityGroupIndex.setStatus("mandatory")


class _PrptrSecurityGroupAdminState_Type(Integer32):
    """Custom type prptrSecurityGroupAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityGroupAdminState_Type.__name__ = "Integer32"
_PrptrSecurityGroupAdminState_Object = MibTableColumn
prptrSecurityGroupAdminState = _PrptrSecurityGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 2),
    _PrptrSecurityGroupAdminState_Type()
)
prptrSecurityGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityGroupAdminState.setStatus("mandatory")


class _PrptrSecurityGroupAutoLearnMode_Type(Integer32):
    """Custom type prptrSecurityGroupAutoLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityGroupAutoLearnMode_Type.__name__ = "Integer32"
_PrptrSecurityGroupAutoLearnMode_Object = MibTableColumn
prptrSecurityGroupAutoLearnMode = _PrptrSecurityGroupAutoLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 3),
    _PrptrSecurityGroupAutoLearnMode_Type()
)
prptrSecurityGroupAutoLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityGroupAutoLearnMode.setStatus("mandatory")


class _PrptrSecurityGroupBroadcastMode_Type(Integer32):
    """Custom type prptrSecurityGroupBroadcastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("other", 1),
          ("reject", 3))
    )


_PrptrSecurityGroupBroadcastMode_Type.__name__ = "Integer32"
_PrptrSecurityGroupBroadcastMode_Object = MibTableColumn
prptrSecurityGroupBroadcastMode = _PrptrSecurityGroupBroadcastMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 4),
    _PrptrSecurityGroupBroadcastMode_Type()
)
prptrSecurityGroupBroadcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityGroupBroadcastMode.setStatus("mandatory")


class _PrptrSecurityGroupMulticastMode_Type(Integer32):
    """Custom type prptrSecurityGroupMulticastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("other", 1),
          ("reject", 3))
    )


_PrptrSecurityGroupMulticastMode_Type.__name__ = "Integer32"
_PrptrSecurityGroupMulticastMode_Object = MibTableColumn
prptrSecurityGroupMulticastMode = _PrptrSecurityGroupMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 5),
    _PrptrSecurityGroupMulticastMode_Type()
)
prptrSecurityGroupMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityGroupMulticastMode.setStatus("mandatory")


class _PrptrSecurityGroupDisPortMode_Type(Integer32):
    """Custom type prptrSecurityGroupDisPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityGroupDisPortMode_Type.__name__ = "Integer32"
_PrptrSecurityGroupDisPortMode_Object = MibTableColumn
prptrSecurityGroupDisPortMode = _PrptrSecurityGroupDisPortMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 6),
    _PrptrSecurityGroupDisPortMode_Type()
)
prptrSecurityGroupDisPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityGroupDisPortMode.setStatus("mandatory")


class _PrptrSecurityGroupRandomMode_Type(Integer32):
    """Custom type prptrSecurityGroupRandomMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityGroupRandomMode_Type.__name__ = "Integer32"
_PrptrSecurityGroupRandomMode_Object = MibTableColumn
prptrSecurityGroupRandomMode = _PrptrSecurityGroupRandomMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 7),
    _PrptrSecurityGroupRandomMode_Type()
)
prptrSecurityGroupRandomMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityGroupRandomMode.setStatus("mandatory")


class _PrptrSecurityGroupDAMismatch_Type(Integer32):
    """Custom type prptrSecurityGroupDAMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityGroupDAMismatch_Type.__name__ = "Integer32"
_PrptrSecurityGroupDAMismatch_Object = MibTableColumn
prptrSecurityGroupDAMismatch = _PrptrSecurityGroupDAMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 8),
    _PrptrSecurityGroupDAMismatch_Type()
)
prptrSecurityGroupDAMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityGroupDAMismatch.setStatus("mandatory")


class _PrptrSecurityGroupSAMismatch_Type(Integer32):
    """Custom type prptrSecurityGroupSAMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityGroupSAMismatch_Type.__name__ = "Integer32"
_PrptrSecurityGroupSAMismatch_Object = MibTableColumn
prptrSecurityGroupSAMismatch = _PrptrSecurityGroupSAMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 9),
    _PrptrSecurityGroupSAMismatch_Type()
)
prptrSecurityGroupSAMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityGroupSAMismatch.setStatus("mandatory")


class _PrptrSecurityAutoRplaceMode_Type(Integer32):
    """Custom type prptrSecurityAutoRplaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityAutoRplaceMode_Type.__name__ = "Integer32"
_PrptrSecurityAutoRplaceMode_Object = MibTableColumn
prptrSecurityAutoRplaceMode = _PrptrSecurityAutoRplaceMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 10),
    _PrptrSecurityAutoRplaceMode_Type()
)
prptrSecurityAutoRplaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityAutoRplaceMode.setStatus("mandatory")


class _PrptrSecurityAllPortsAdmin_Type(Integer32):
    """Custom type prptrSecurityAllPortsAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityAllPortsAdmin_Type.__name__ = "Integer32"
_PrptrSecurityAllPortsAdmin_Object = MibTableColumn
prptrSecurityAllPortsAdmin = _PrptrSecurityAllPortsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 1, 1, 11),
    _PrptrSecurityAllPortsAdmin_Type()
)
prptrSecurityAllPortsAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityAllPortsAdmin.setStatus("mandatory")
_RptrSecurityGroupTable_Object = MibTable
rptrSecurityGroupTable = _RptrSecurityGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 2)
)
if mibBuilder.loadTexts:
    rptrSecurityGroupTable.setStatus("mandatory")
_RptrSecurityGroupEntry_Object = MibTableRow
rptrSecurityGroupEntry = _RptrSecurityGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 2, 1)
)
rptrSecurityGroupEntry.setIndexNames(
    (0, "Hub-rptr-prvt-sec", "rptrSecurityGroupIndex"),
)
if mibBuilder.loadTexts:
    rptrSecurityGroupEntry.setStatus("mandatory")


class _RptrSecurityGroupIndex_Type(Integer32):
    """Custom type rptrSecurityGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrSecurityGroupIndex_Type.__name__ = "Integer32"
_RptrSecurityGroupIndex_Object = MibTableColumn
rptrSecurityGroupIndex = _RptrSecurityGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 2, 1, 1),
    _RptrSecurityGroupIndex_Type()
)
rptrSecurityGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityGroupIndex.setStatus("mandatory")


class _RptrSecurityGroupOperState_Type(Integer32):
    """Custom type rptrSecurityGroupOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_RptrSecurityGroupOperState_Type.__name__ = "Integer32"
_RptrSecurityGroupOperState_Object = MibTableColumn
rptrSecurityGroupOperState = _RptrSecurityGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 2, 1, 2),
    _RptrSecurityGroupOperState_Type()
)
rptrSecurityGroupOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityGroupOperState.setStatus("mandatory")


class _RptrSecurityGroupAutoLearnMode_Type(Integer32):
    """Custom type rptrSecurityGroupAutoLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_RptrSecurityGroupAutoLearnMode_Type.__name__ = "Integer32"
_RptrSecurityGroupAutoLearnMode_Object = MibTableColumn
rptrSecurityGroupAutoLearnMode = _RptrSecurityGroupAutoLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 2, 1, 3),
    _RptrSecurityGroupAutoLearnMode_Type()
)
rptrSecurityGroupAutoLearnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityGroupAutoLearnMode.setStatus("mandatory")


class _RptrSecurityGroupDisPortMode_Type(Integer32):
    """Custom type rptrSecurityGroupDisPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_RptrSecurityGroupDisPortMode_Type.__name__ = "Integer32"
_RptrSecurityGroupDisPortMode_Object = MibTableColumn
rptrSecurityGroupDisPortMode = _RptrSecurityGroupDisPortMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 2, 1, 4),
    _RptrSecurityGroupDisPortMode_Type()
)
rptrSecurityGroupDisPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityGroupDisPortMode.setStatus("mandatory")


class _RptrSecurityGroupRandomMode_Type(Integer32):
    """Custom type rptrSecurityGroupRandomMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_RptrSecurityGroupRandomMode_Type.__name__ = "Integer32"
_RptrSecurityGroupRandomMode_Object = MibTableColumn
rptrSecurityGroupRandomMode = _RptrSecurityGroupRandomMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 5, 2, 1, 5),
    _RptrSecurityGroupRandomMode_Type()
)
rptrSecurityGroupRandomMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityGroupRandomMode.setStatus("mandatory")
_RptrSecurityPortInfo_ObjectIdentity = ObjectIdentity
rptrSecurityPortInfo = _RptrSecurityPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6)
)
_PrptrSecurityPortTable_Object = MibTable
prptrSecurityPortTable = _PrptrSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1)
)
if mibBuilder.loadTexts:
    prptrSecurityPortTable.setStatus("mandatory")
_PrptrSecurityPortEntry_Object = MibTableRow
prptrSecurityPortEntry = _PrptrSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1)
)
prptrSecurityPortEntry.setIndexNames(
    (0, "Hub-rptr-prvt-sec", "prptrSecurityPortGroupIndex"),
    (0, "Hub-rptr-prvt-sec", "prptrSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    prptrSecurityPortEntry.setStatus("mandatory")


class _PrptrSecurityPortGroupIndex_Type(Integer32):
    """Custom type prptrSecurityPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PrptrSecurityPortGroupIndex_Type.__name__ = "Integer32"
_PrptrSecurityPortGroupIndex_Object = MibTableColumn
prptrSecurityPortGroupIndex = _PrptrSecurityPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 1),
    _PrptrSecurityPortGroupIndex_Type()
)
prptrSecurityPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prptrSecurityPortGroupIndex.setStatus("mandatory")


class _PrptrSecurityPortIndex_Type(Integer32):
    """Custom type prptrSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PrptrSecurityPortIndex_Type.__name__ = "Integer32"
_PrptrSecurityPortIndex_Object = MibTableColumn
prptrSecurityPortIndex = _PrptrSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 2),
    _PrptrSecurityPortIndex_Type()
)
prptrSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prptrSecurityPortIndex.setStatus("mandatory")


class _PrptrSecurityPortAdminState_Type(Integer32):
    """Custom type prptrSecurityPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityPortAdminState_Type.__name__ = "Integer32"
_PrptrSecurityPortAdminState_Object = MibTableColumn
prptrSecurityPortAdminState = _PrptrSecurityPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 3),
    _PrptrSecurityPortAdminState_Type()
)
prptrSecurityPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortAdminState.setStatus("mandatory")


class _PrptrSecurityPortAutoLearnMode_Type(Integer32):
    """Custom type prptrSecurityPortAutoLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityPortAutoLearnMode_Type.__name__ = "Integer32"
_PrptrSecurityPortAutoLearnMode_Object = MibTableColumn
prptrSecurityPortAutoLearnMode = _PrptrSecurityPortAutoLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 4),
    _PrptrSecurityPortAutoLearnMode_Type()
)
prptrSecurityPortAutoLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortAutoLearnMode.setStatus("mandatory")


class _PrptrSecurityPortBroadcastMode_Type(Integer32):
    """Custom type prptrSecurityPortBroadcastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("other", 1),
          ("reject", 3))
    )


_PrptrSecurityPortBroadcastMode_Type.__name__ = "Integer32"
_PrptrSecurityPortBroadcastMode_Object = MibTableColumn
prptrSecurityPortBroadcastMode = _PrptrSecurityPortBroadcastMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 5),
    _PrptrSecurityPortBroadcastMode_Type()
)
prptrSecurityPortBroadcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortBroadcastMode.setStatus("mandatory")


class _PrptrSecurityPortMulticastMode_Type(Integer32):
    """Custom type prptrSecurityPortMulticastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("other", 1),
          ("reject", 3))
    )


_PrptrSecurityPortMulticastMode_Type.__name__ = "Integer32"
_PrptrSecurityPortMulticastMode_Object = MibTableColumn
prptrSecurityPortMulticastMode = _PrptrSecurityPortMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 6),
    _PrptrSecurityPortMulticastMode_Type()
)
prptrSecurityPortMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortMulticastMode.setStatus("mandatory")


class _PrptrSecurityPortSAMismatch_Type(Integer32):
    """Custom type prptrSecurityPortSAMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityPortSAMismatch_Type.__name__ = "Integer32"
_PrptrSecurityPortSAMismatch_Object = MibTableColumn
prptrSecurityPortSAMismatch = _PrptrSecurityPortSAMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 7),
    _PrptrSecurityPortSAMismatch_Type()
)
prptrSecurityPortSAMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortSAMismatch.setStatus("mandatory")


class _PrptrSecurityPortDAMismatch_Type(Integer32):
    """Custom type prptrSecurityPortDAMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityPortDAMismatch_Type.__name__ = "Integer32"
_PrptrSecurityPortDAMismatch_Object = MibTableColumn
prptrSecurityPortDAMismatch = _PrptrSecurityPortDAMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 8),
    _PrptrSecurityPortDAMismatch_Type()
)
prptrSecurityPortDAMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortDAMismatch.setStatus("mandatory")


class _PrptrSecurityPortMAC1state_Type(Integer32):
    """Custom type prptrSecurityPortMAC1state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", 3),
          ("other", 1),
          ("valid", 2))
    )


_PrptrSecurityPortMAC1state_Type.__name__ = "Integer32"
_PrptrSecurityPortMAC1state_Object = MibTableColumn
prptrSecurityPortMAC1state = _PrptrSecurityPortMAC1state_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 9),
    _PrptrSecurityPortMAC1state_Type()
)
prptrSecurityPortMAC1state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortMAC1state.setStatus("mandatory")
_PrptrSecurityPortMAC1Address_Type = PhysAddress
_PrptrSecurityPortMAC1Address_Object = MibTableColumn
prptrSecurityPortMAC1Address = _PrptrSecurityPortMAC1Address_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 10),
    _PrptrSecurityPortMAC1Address_Type()
)
prptrSecurityPortMAC1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortMAC1Address.setStatus("mandatory")


class _PrptrSecurityPortMAC2state_Type(Integer32):
    """Custom type prptrSecurityPortMAC2state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", 3),
          ("other", 1),
          ("valid", 2))
    )


_PrptrSecurityPortMAC2state_Type.__name__ = "Integer32"
_PrptrSecurityPortMAC2state_Object = MibTableColumn
prptrSecurityPortMAC2state = _PrptrSecurityPortMAC2state_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 11),
    _PrptrSecurityPortMAC2state_Type()
)
prptrSecurityPortMAC2state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortMAC2state.setStatus("mandatory")
_PrptrSecurityPortMAC2Address_Type = PhysAddress
_PrptrSecurityPortMAC2Address_Object = MibTableColumn
prptrSecurityPortMAC2Address = _PrptrSecurityPortMAC2Address_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 12),
    _PrptrSecurityPortMAC2Address_Type()
)
prptrSecurityPortMAC2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortMAC2Address.setStatus("mandatory")


class _PrptrSecurityPortAutoRplaceMode_Type(Integer32):
    """Custom type prptrSecurityPortAutoRplaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_PrptrSecurityPortAutoRplaceMode_Type.__name__ = "Integer32"
_PrptrSecurityPortAutoRplaceMode_Object = MibTableColumn
prptrSecurityPortAutoRplaceMode = _PrptrSecurityPortAutoRplaceMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 1, 1, 13),
    _PrptrSecurityPortAutoRplaceMode_Type()
)
prptrSecurityPortAutoRplaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityPortAutoRplaceMode.setStatus("mandatory")
_RptrSecurityPortTable_Object = MibTable
rptrSecurityPortTable = _RptrSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2)
)
if mibBuilder.loadTexts:
    rptrSecurityPortTable.setStatus("mandatory")
_RptrSecurityPortEntry_Object = MibTableRow
rptrSecurityPortEntry = _RptrSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1)
)
rptrSecurityPortEntry.setIndexNames(
    (0, "Hub-rptr-prvt-sec", "rptrSecurityPortGroupIndex"),
    (0, "Hub-rptr-prvt-sec", "rptrSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    rptrSecurityPortEntry.setStatus("mandatory")


class _RptrSecurityPortGroupIndex_Type(Integer32):
    """Custom type rptrSecurityPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrSecurityPortGroupIndex_Type.__name__ = "Integer32"
_RptrSecurityPortGroupIndex_Object = MibTableColumn
rptrSecurityPortGroupIndex = _RptrSecurityPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 1),
    _RptrSecurityPortGroupIndex_Type()
)
rptrSecurityPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortGroupIndex.setStatus("mandatory")


class _RptrSecurityPortIndex_Type(Integer32):
    """Custom type rptrSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrSecurityPortIndex_Type.__name__ = "Integer32"
_RptrSecurityPortIndex_Object = MibTableColumn
rptrSecurityPortIndex = _RptrSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 2),
    _RptrSecurityPortIndex_Type()
)
rptrSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortIndex.setStatus("mandatory")


class _RptrSecurityPortOperState_Type(Integer32):
    """Custom type rptrSecurityPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_RptrSecurityPortOperState_Type.__name__ = "Integer32"
_RptrSecurityPortOperState_Object = MibTableColumn
rptrSecurityPortOperState = _RptrSecurityPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 3),
    _RptrSecurityPortOperState_Type()
)
rptrSecurityPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortOperState.setStatus("mandatory")


class _RptrSecurityPortAutoLearnMode_Type(Integer32):
    """Custom type rptrSecurityPortAutoLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_RptrSecurityPortAutoLearnMode_Type.__name__ = "Integer32"
_RptrSecurityPortAutoLearnMode_Object = MibTableColumn
rptrSecurityPortAutoLearnMode = _RptrSecurityPortAutoLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 4),
    _RptrSecurityPortAutoLearnMode_Type()
)
rptrSecurityPortAutoLearnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortAutoLearnMode.setStatus("mandatory")


class _RptrSecurityPortBroadcastMode_Type(Integer32):
    """Custom type rptrSecurityPortBroadcastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("other", 1),
          ("reject", 3))
    )


_RptrSecurityPortBroadcastMode_Type.__name__ = "Integer32"
_RptrSecurityPortBroadcastMode_Object = MibTableColumn
rptrSecurityPortBroadcastMode = _RptrSecurityPortBroadcastMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 5),
    _RptrSecurityPortBroadcastMode_Type()
)
rptrSecurityPortBroadcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortBroadcastMode.setStatus("mandatory")


class _RptrSecurityPortMulticastMode_Type(Integer32):
    """Custom type rptrSecurityPortMulticastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("other", 1),
          ("reject", 3))
    )


_RptrSecurityPortMulticastMode_Type.__name__ = "Integer32"
_RptrSecurityPortMulticastMode_Object = MibTableColumn
rptrSecurityPortMulticastMode = _RptrSecurityPortMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 6),
    _RptrSecurityPortMulticastMode_Type()
)
rptrSecurityPortMulticastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortMulticastMode.setStatus("mandatory")


class _RptrSecurityPortSAMismatch_Type(Integer32):
    """Custom type rptrSecurityPortSAMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_RptrSecurityPortSAMismatch_Type.__name__ = "Integer32"
_RptrSecurityPortSAMismatch_Object = MibTableColumn
rptrSecurityPortSAMismatch = _RptrSecurityPortSAMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 7),
    _RptrSecurityPortSAMismatch_Type()
)
rptrSecurityPortSAMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortSAMismatch.setStatus("mandatory")


class _RptrSecurityPortDAMismatch_Type(Integer32):
    """Custom type rptrSecurityPortDAMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_RptrSecurityPortDAMismatch_Type.__name__ = "Integer32"
_RptrSecurityPortDAMismatch_Object = MibTableColumn
rptrSecurityPortDAMismatch = _RptrSecurityPortDAMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 8),
    _RptrSecurityPortDAMismatch_Type()
)
rptrSecurityPortDAMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortDAMismatch.setStatus("mandatory")
_RptrSecurityPortSAMismatches_Type = Counter32
_RptrSecurityPortSAMismatches_Object = MibTableColumn
rptrSecurityPortSAMismatches = _RptrSecurityPortSAMismatches_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 9),
    _RptrSecurityPortSAMismatches_Type()
)
rptrSecurityPortSAMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortSAMismatches.setStatus("mandatory")
_RptrSecurityPortLastSAMismatch_Type = PhysAddress
_RptrSecurityPortLastSAMismatch_Object = MibTableColumn
rptrSecurityPortLastSAMismatch = _RptrSecurityPortLastSAMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 10),
    _RptrSecurityPortLastSAMismatch_Type()
)
rptrSecurityPortLastSAMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortLastSAMismatch.setStatus("mandatory")


class _RptrSecurityPortMAC1state_Type(Integer32):
    """Custom type rptrSecurityPortMAC1state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", 3),
          ("other", 1),
          ("valid", 2))
    )


_RptrSecurityPortMAC1state_Type.__name__ = "Integer32"
_RptrSecurityPortMAC1state_Object = MibTableColumn
rptrSecurityPortMAC1state = _RptrSecurityPortMAC1state_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 11),
    _RptrSecurityPortMAC1state_Type()
)
rptrSecurityPortMAC1state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortMAC1state.setStatus("mandatory")
_RptrSecurityPortMAC1Address_Type = PhysAddress
_RptrSecurityPortMAC1Address_Object = MibTableColumn
rptrSecurityPortMAC1Address = _RptrSecurityPortMAC1Address_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 12),
    _RptrSecurityPortMAC1Address_Type()
)
rptrSecurityPortMAC1Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortMAC1Address.setStatus("mandatory")


class _RptrSecurityPortMAC2state_Type(Integer32):
    """Custom type rptrSecurityPortMAC2state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", 3),
          ("other", 1),
          ("valid", 2))
    )


_RptrSecurityPortMAC2state_Type.__name__ = "Integer32"
_RptrSecurityPortMAC2state_Object = MibTableColumn
rptrSecurityPortMAC2state = _RptrSecurityPortMAC2state_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 13),
    _RptrSecurityPortMAC2state_Type()
)
rptrSecurityPortMAC2state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortMAC2state.setStatus("mandatory")
_RptrSecurityPortMAC2Address_Type = PhysAddress
_RptrSecurityPortMAC2Address_Object = MibTableColumn
rptrSecurityPortMAC2Address = _RptrSecurityPortMAC2Address_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 6, 2, 1, 14),
    _RptrSecurityPortMAC2Address_Type()
)
rptrSecurityPortMAC2Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityPortMAC2Address.setStatus("mandatory")
_RptrSecurityMACInfo_ObjectIdentity = ObjectIdentity
rptrSecurityMACInfo = _RptrSecurityMACInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7)
)
_PrptrSecurityMACTable_Object = MibTable
prptrSecurityMACTable = _PrptrSecurityMACTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 1)
)
if mibBuilder.loadTexts:
    prptrSecurityMACTable.setStatus("mandatory")
_PrptrSecurityMACEntry_Object = MibTableRow
prptrSecurityMACEntry = _PrptrSecurityMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 1, 1)
)
prptrSecurityMACEntry.setIndexNames(
    (0, "Hub-rptr-prvt-sec", "prptrSecurityMACGroupIndex"),
    (0, "Hub-rptr-prvt-sec", "prptrSecurityMACEntryIndex"),
)
if mibBuilder.loadTexts:
    prptrSecurityMACEntry.setStatus("mandatory")


class _PrptrSecurityMACGroupIndex_Type(Integer32):
    """Custom type prptrSecurityMACGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PrptrSecurityMACGroupIndex_Type.__name__ = "Integer32"
_PrptrSecurityMACGroupIndex_Object = MibTableColumn
prptrSecurityMACGroupIndex = _PrptrSecurityMACGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 1, 1, 1),
    _PrptrSecurityMACGroupIndex_Type()
)
prptrSecurityMACGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prptrSecurityMACGroupIndex.setStatus("mandatory")


class _PrptrSecurityMACEntryIndex_Type(Integer32):
    """Custom type prptrSecurityMACEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PrptrSecurityMACEntryIndex_Type.__name__ = "Integer32"
_PrptrSecurityMACEntryIndex_Object = MibTableColumn
prptrSecurityMACEntryIndex = _PrptrSecurityMACEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 1, 1, 2),
    _PrptrSecurityMACEntryIndex_Type()
)
prptrSecurityMACEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prptrSecurityMACEntryIndex.setStatus("mandatory")
_PrptrSecurityMACPhysicalAddress_Type = PhysAddress
_PrptrSecurityMACPhysicalAddress_Object = MibTableColumn
prptrSecurityMACPhysicalAddress = _PrptrSecurityMACPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 1, 1, 3),
    _PrptrSecurityMACPhysicalAddress_Type()
)
prptrSecurityMACPhysicalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityMACPhysicalAddress.setStatus("mandatory")


class _PrptrSecurityMACState_Type(Integer32):
    """Custom type prptrSecurityMACState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", 3),
          ("other", 1),
          ("valid", 2))
    )


_PrptrSecurityMACState_Type.__name__ = "Integer32"
_PrptrSecurityMACState_Object = MibTableColumn
prptrSecurityMACState = _PrptrSecurityMACState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 1, 1, 4),
    _PrptrSecurityMACState_Type()
)
prptrSecurityMACState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityMACState.setStatus("mandatory")


class _PrptrSecurityMACPortMap_Type(Integer32):
    """Custom type prptrSecurityMACPortMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_PrptrSecurityMACPortMap_Type.__name__ = "Integer32"
_PrptrSecurityMACPortMap_Object = MibTableColumn
prptrSecurityMACPortMap = _PrptrSecurityMACPortMap_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 1, 1, 5),
    _PrptrSecurityMACPortMap_Type()
)
prptrSecurityMACPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prptrSecurityMACPortMap.setStatus("mandatory")
_RptrSecurityMACTable_Object = MibTable
rptrSecurityMACTable = _RptrSecurityMACTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 2)
)
if mibBuilder.loadTexts:
    rptrSecurityMACTable.setStatus("mandatory")
_RptrSecurityMACEntry_Object = MibTableRow
rptrSecurityMACEntry = _RptrSecurityMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 2, 1)
)
rptrSecurityMACEntry.setIndexNames(
    (0, "Hub-rptr-prvt-sec", "rptrSecurityMACGroupIndex"),
    (0, "Hub-rptr-prvt-sec", "rptrSecurityMACEntryIndex"),
)
if mibBuilder.loadTexts:
    rptrSecurityMACEntry.setStatus("mandatory")


class _RptrSecurityMACGroupIndex_Type(Integer32):
    """Custom type rptrSecurityMACGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrSecurityMACGroupIndex_Type.__name__ = "Integer32"
_RptrSecurityMACGroupIndex_Object = MibTableColumn
rptrSecurityMACGroupIndex = _RptrSecurityMACGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 2, 1, 1),
    _RptrSecurityMACGroupIndex_Type()
)
rptrSecurityMACGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityMACGroupIndex.setStatus("mandatory")


class _RptrSecurityMACEntryIndex_Type(Integer32):
    """Custom type rptrSecurityMACEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RptrSecurityMACEntryIndex_Type.__name__ = "Integer32"
_RptrSecurityMACEntryIndex_Object = MibTableColumn
rptrSecurityMACEntryIndex = _RptrSecurityMACEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 2, 1, 2),
    _RptrSecurityMACEntryIndex_Type()
)
rptrSecurityMACEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityMACEntryIndex.setStatus("mandatory")
_RptrSecurityMACPhysicalAddress_Type = PhysAddress
_RptrSecurityMACPhysicalAddress_Object = MibTableColumn
rptrSecurityMACPhysicalAddress = _RptrSecurityMACPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 2, 1, 3),
    _RptrSecurityMACPhysicalAddress_Type()
)
rptrSecurityMACPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityMACPhysicalAddress.setStatus("mandatory")


class _RptrSecurityMACState_Type(Integer32):
    """Custom type rptrSecurityMACState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", 3),
          ("other", 1),
          ("valid", 2))
    )


_RptrSecurityMACState_Type.__name__ = "Integer32"
_RptrSecurityMACState_Object = MibTableColumn
rptrSecurityMACState = _RptrSecurityMACState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 2, 1, 4),
    _RptrSecurityMACState_Type()
)
rptrSecurityMACState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityMACState.setStatus("mandatory")


class _RptrSecurityMACPortMap_Type(Integer32):
    """Custom type rptrSecurityMACPortMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_RptrSecurityMACPortMap_Type.__name__ = "Integer32"
_RptrSecurityMACPortMap_Object = MibTableColumn
rptrSecurityMACPortMap = _RptrSecurityMACPortMap_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 7, 2, 1, 5),
    _RptrSecurityMACPortMap_Type()
)
rptrSecurityMACPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecurityMACPortMap.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rptrSecuritySAMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 101, 8, 0, 15)
)
rptrSecuritySAMismatch.setObjects(
      *(("Hub-rptr-prvt-sec", "rptrSecurityPortGroupIndex"),
        ("Hub-rptr-prvt-sec", "rptrSecurityPortIndex"),
        ("Hub-rptr-prvt-sec", "rptrSecurityPortSAMismatches"),
        ("Hub-rptr-prvt-sec", "rptrSecurityPortLastSAMismatch"))
)
if mibBuilder.loadTexts:
    rptrSecuritySAMismatch.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Hub-rptr-prvt-sec",
    **{"private": private,
       "enterprises": enterprises,
       "fibronics": fibronics,
       "mibs": mibs,
       "mibseth-rptrs": mibseth_rptrs,
       "rptrSecuritySAMismatch": rptrSecuritySAMismatch,
       "rptrSecurityInfo": rptrSecurityInfo,
       "prptrSecurityGroupTable": prptrSecurityGroupTable,
       "prptrSecurityGroupEntry": prptrSecurityGroupEntry,
       "prptrSecurityGroupIndex": prptrSecurityGroupIndex,
       "prptrSecurityGroupAdminState": prptrSecurityGroupAdminState,
       "prptrSecurityGroupAutoLearnMode": prptrSecurityGroupAutoLearnMode,
       "prptrSecurityGroupBroadcastMode": prptrSecurityGroupBroadcastMode,
       "prptrSecurityGroupMulticastMode": prptrSecurityGroupMulticastMode,
       "prptrSecurityGroupDisPortMode": prptrSecurityGroupDisPortMode,
       "prptrSecurityGroupRandomMode": prptrSecurityGroupRandomMode,
       "prptrSecurityGroupDAMismatch": prptrSecurityGroupDAMismatch,
       "prptrSecurityGroupSAMismatch": prptrSecurityGroupSAMismatch,
       "prptrSecurityAutoRplaceMode": prptrSecurityAutoRplaceMode,
       "prptrSecurityAllPortsAdmin": prptrSecurityAllPortsAdmin,
       "rptrSecurityGroupTable": rptrSecurityGroupTable,
       "rptrSecurityGroupEntry": rptrSecurityGroupEntry,
       "rptrSecurityGroupIndex": rptrSecurityGroupIndex,
       "rptrSecurityGroupOperState": rptrSecurityGroupOperState,
       "rptrSecurityGroupAutoLearnMode": rptrSecurityGroupAutoLearnMode,
       "rptrSecurityGroupDisPortMode": rptrSecurityGroupDisPortMode,
       "rptrSecurityGroupRandomMode": rptrSecurityGroupRandomMode,
       "rptrSecurityPortInfo": rptrSecurityPortInfo,
       "prptrSecurityPortTable": prptrSecurityPortTable,
       "prptrSecurityPortEntry": prptrSecurityPortEntry,
       "prptrSecurityPortGroupIndex": prptrSecurityPortGroupIndex,
       "prptrSecurityPortIndex": prptrSecurityPortIndex,
       "prptrSecurityPortAdminState": prptrSecurityPortAdminState,
       "prptrSecurityPortAutoLearnMode": prptrSecurityPortAutoLearnMode,
       "prptrSecurityPortBroadcastMode": prptrSecurityPortBroadcastMode,
       "prptrSecurityPortMulticastMode": prptrSecurityPortMulticastMode,
       "prptrSecurityPortSAMismatch": prptrSecurityPortSAMismatch,
       "prptrSecurityPortDAMismatch": prptrSecurityPortDAMismatch,
       "prptrSecurityPortMAC1state": prptrSecurityPortMAC1state,
       "prptrSecurityPortMAC1Address": prptrSecurityPortMAC1Address,
       "prptrSecurityPortMAC2state": prptrSecurityPortMAC2state,
       "prptrSecurityPortMAC2Address": prptrSecurityPortMAC2Address,
       "prptrSecurityPortAutoRplaceMode": prptrSecurityPortAutoRplaceMode,
       "rptrSecurityPortTable": rptrSecurityPortTable,
       "rptrSecurityPortEntry": rptrSecurityPortEntry,
       "rptrSecurityPortGroupIndex": rptrSecurityPortGroupIndex,
       "rptrSecurityPortIndex": rptrSecurityPortIndex,
       "rptrSecurityPortOperState": rptrSecurityPortOperState,
       "rptrSecurityPortAutoLearnMode": rptrSecurityPortAutoLearnMode,
       "rptrSecurityPortBroadcastMode": rptrSecurityPortBroadcastMode,
       "rptrSecurityPortMulticastMode": rptrSecurityPortMulticastMode,
       "rptrSecurityPortSAMismatch": rptrSecurityPortSAMismatch,
       "rptrSecurityPortDAMismatch": rptrSecurityPortDAMismatch,
       "rptrSecurityPortSAMismatches": rptrSecurityPortSAMismatches,
       "rptrSecurityPortLastSAMismatch": rptrSecurityPortLastSAMismatch,
       "rptrSecurityPortMAC1state": rptrSecurityPortMAC1state,
       "rptrSecurityPortMAC1Address": rptrSecurityPortMAC1Address,
       "rptrSecurityPortMAC2state": rptrSecurityPortMAC2state,
       "rptrSecurityPortMAC2Address": rptrSecurityPortMAC2Address,
       "rptrSecurityMACInfo": rptrSecurityMACInfo,
       "prptrSecurityMACTable": prptrSecurityMACTable,
       "prptrSecurityMACEntry": prptrSecurityMACEntry,
       "prptrSecurityMACGroupIndex": prptrSecurityMACGroupIndex,
       "prptrSecurityMACEntryIndex": prptrSecurityMACEntryIndex,
       "prptrSecurityMACPhysicalAddress": prptrSecurityMACPhysicalAddress,
       "prptrSecurityMACState": prptrSecurityMACState,
       "prptrSecurityMACPortMap": prptrSecurityMACPortMap,
       "rptrSecurityMACTable": rptrSecurityMACTable,
       "rptrSecurityMACEntry": rptrSecurityMACEntry,
       "rptrSecurityMACGroupIndex": rptrSecurityMACGroupIndex,
       "rptrSecurityMACEntryIndex": rptrSecurityMACEntryIndex,
       "rptrSecurityMACPhysicalAddress": rptrSecurityMACPhysicalAddress,
       "rptrSecurityMACState": rptrSecurityMACState,
       "rptrSecurityMACPortMap": rptrSecurityMACPortMap}
)
