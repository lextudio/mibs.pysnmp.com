# SNMP MIB module (ASCEND-MIBDIALMOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDIALMOD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:28 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibdialModifierProfile_ObjectIdentity = ObjectIdentity
mibdialModifierProfile = _MibdialModifierProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 74)
)
_MibdialModifierProfileTable_Object = MibTable
mibdialModifierProfileTable = _MibdialModifierProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1)
)
if mibBuilder.loadTexts:
    mibdialModifierProfileTable.setStatus("mandatory")
_MibdialModifierProfileEntry_Object = MibTableRow
mibdialModifierProfileEntry = _MibdialModifierProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1)
)
mibdialModifierProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDIALMOD-MIB", "dialModifierProfile-Name"),
)
if mibBuilder.loadTexts:
    mibdialModifierProfileEntry.setStatus("mandatory")
_DialModifierProfile_Name_Type = DisplayString
_DialModifierProfile_Name_Object = MibScalar
dialModifierProfile_Name = _DialModifierProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 1),
    _DialModifierProfile_Name_Type()
)
dialModifierProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialModifierProfile_Name.setStatus("mandatory")


class _DialModifierProfile_Active_Type(Integer32):
    """Custom type dialModifierProfile_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DialModifierProfile_Active_Type.__name__ = "Integer32"
_DialModifierProfile_Active_Object = MibScalar
dialModifierProfile_Active = _DialModifierProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 2),
    _DialModifierProfile_Active_Type()
)
dialModifierProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialModifierProfile_Active.setStatus("mandatory")


class _DialModifierProfile_UserSuppliedTg_Type(Integer32):
    """Custom type dialModifierProfile_UserSuppliedTg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DialModifierProfile_UserSuppliedTg_Type.__name__ = "Integer32"
_DialModifierProfile_UserSuppliedTg_Object = MibScalar
dialModifierProfile_UserSuppliedTg = _DialModifierProfile_UserSuppliedTg_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 3),
    _DialModifierProfile_UserSuppliedTg_Type()
)
dialModifierProfile_UserSuppliedTg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialModifierProfile_UserSuppliedTg.setStatus("mandatory")
_DialModifierProfile_TrunkGroupFilter_Type = Integer32
_DialModifierProfile_TrunkGroupFilter_Object = MibScalar
dialModifierProfile_TrunkGroupFilter = _DialModifierProfile_TrunkGroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 4),
    _DialModifierProfile_TrunkGroupFilter_Type()
)
dialModifierProfile_TrunkGroupFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialModifierProfile_TrunkGroupFilter.setStatus("mandatory")
_DialModifierProfile_SlotFilter_Type = Integer32
_DialModifierProfile_SlotFilter_Object = MibScalar
dialModifierProfile_SlotFilter = _DialModifierProfile_SlotFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 5),
    _DialModifierProfile_SlotFilter_Type()
)
dialModifierProfile_SlotFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialModifierProfile_SlotFilter.setStatus("mandatory")


class _DialModifierProfile_PortTypeFilter_Type(Integer32):
    """Custom type dialModifierProfile_PortTypeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("maxpots", 2))
    )


_DialModifierProfile_PortTypeFilter_Type.__name__ = "Integer32"
_DialModifierProfile_PortTypeFilter_Object = MibScalar
dialModifierProfile_PortTypeFilter = _DialModifierProfile_PortTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 6),
    _DialModifierProfile_PortTypeFilter_Type()
)
dialModifierProfile_PortTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialModifierProfile_PortTypeFilter.setStatus("mandatory")
_DialModifierProfile_PrefixFilter_Type = DisplayString
_DialModifierProfile_PrefixFilter_Object = MibScalar
dialModifierProfile_PrefixFilter = _DialModifierProfile_PrefixFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 7),
    _DialModifierProfile_PrefixFilter_Type()
)
dialModifierProfile_PrefixFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialModifierProfile_PrefixFilter.setStatus("mandatory")
_DialModifierProfile_LengthFilter_Type = Integer32
_DialModifierProfile_LengthFilter_Object = MibScalar
dialModifierProfile_LengthFilter = _DialModifierProfile_LengthFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 8),
    _DialModifierProfile_LengthFilter_Type()
)
dialModifierProfile_LengthFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialModifierProfile_LengthFilter.setStatus("mandatory")
_DialModifierProfile_DialPlan_Type = Integer32
_DialModifierProfile_DialPlan_Object = MibScalar
dialModifierProfile_DialPlan = _DialModifierProfile_DialPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 9),
    _DialModifierProfile_DialPlan_Type()
)
dialModifierProfile_DialPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialModifierProfile_DialPlan.setStatus("mandatory")
_DialModifierProfile_NewTrunkGroup_Type = Integer32
_DialModifierProfile_NewTrunkGroup_Object = MibScalar
dialModifierProfile_NewTrunkGroup = _DialModifierProfile_NewTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 10),
    _DialModifierProfile_NewTrunkGroup_Type()
)
dialModifierProfile_NewTrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialModifierProfile_NewTrunkGroup.setStatus("mandatory")


class _DialModifierProfile_Action_o_Type(Integer32):
    """Custom type dialModifierProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_DialModifierProfile_Action_o_Type.__name__ = "Integer32"
_DialModifierProfile_Action_o_Object = MibScalar
dialModifierProfile_Action_o = _DialModifierProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 74, 1, 1, 11),
    _DialModifierProfile_Action_o_Type()
)
dialModifierProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialModifierProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDIALMOD-MIB",
    **{"DisplayString": DisplayString,
       "mibdialModifierProfile": mibdialModifierProfile,
       "mibdialModifierProfileTable": mibdialModifierProfileTable,
       "mibdialModifierProfileEntry": mibdialModifierProfileEntry,
       "dialModifierProfile-Name": dialModifierProfile_Name,
       "dialModifierProfile-Active": dialModifierProfile_Active,
       "dialModifierProfile-UserSuppliedTg": dialModifierProfile_UserSuppliedTg,
       "dialModifierProfile-TrunkGroupFilter": dialModifierProfile_TrunkGroupFilter,
       "dialModifierProfile-SlotFilter": dialModifierProfile_SlotFilter,
       "dialModifierProfile-PortTypeFilter": dialModifierProfile_PortTypeFilter,
       "dialModifierProfile-PrefixFilter": dialModifierProfile_PrefixFilter,
       "dialModifierProfile-LengthFilter": dialModifierProfile_LengthFilter,
       "dialModifierProfile-DialPlan": dialModifierProfile_DialPlan,
       "dialModifierProfile-NewTrunkGroup": dialModifierProfile_NewTrunkGroup,
       "dialModifierProfile-Action-o": dialModifierProfile_Action_o}
)
