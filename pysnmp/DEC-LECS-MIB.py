# SNMP MIB module (DEC-LECS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEC-LECS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:36 2024
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

(decMIBextension,) = mibBuilder.importSymbols(
    "DECATM-MIB",
    "decMIBextension")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DecLecsMIB_ObjectIdentity = ObjectIdentity
decLecsMIB = _DecLecsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31)
)
_DecElanAdminGroup_ObjectIdentity = ObjectIdentity
decElanAdminGroup = _DecElanAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 1)
)
_DecElanAdminPolicyVal_ObjectIdentity = ObjectIdentity
decElanAdminPolicyVal = _DecElanAdminPolicyVal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 1, 1)
)
_AssignByAtmAddr_ObjectIdentity = ObjectIdentity
assignByAtmAddr = _AssignByAtmAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 1, 1, 1)
)
_AssignByMacAddr_ObjectIdentity = ObjectIdentity
assignByMacAddr = _AssignByMacAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 1, 1, 2)
)
_AssignByRouteDescriptor_ObjectIdentity = ObjectIdentity
assignByRouteDescriptor = _AssignByRouteDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 1, 1, 3)
)
_AssignByElanName_ObjectIdentity = ObjectIdentity
assignByElanName = _AssignByElanName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 1, 1, 4)
)
_AssignByCompatibility_ObjectIdentity = ObjectIdentity
assignByCompatibility = _AssignByCompatibility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 1, 1, 5)
)
_DecElanConfGroup_ObjectIdentity = ObjectIdentity
decElanConfGroup = _DecElanConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2)
)
_DecElanConfNextId_Type = Integer32
_DecElanConfNextId_Object = MibScalar
decElanConfNextId = _DecElanConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 1),
    _DecElanConfNextId_Type()
)
decElanConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decElanConfNextId.setStatus("mandatory")
_DecElanConfTable_Object = MibTable
decElanConfTable = _DecElanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 2)
)
if mibBuilder.loadTexts:
    decElanConfTable.setStatus("mandatory")
_DecElanConfEntry_Object = MibTableRow
decElanConfEntry = _DecElanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 2, 1)
)
decElanConfEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decElanConfIndex"),
)
if mibBuilder.loadTexts:
    decElanConfEntry.setStatus("mandatory")
_DecElanConfIndex_Type = Integer32
_DecElanConfIndex_Object = MibTableColumn
decElanConfIndex = _DecElanConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 2, 1, 1),
    _DecElanConfIndex_Type()
)
decElanConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decElanConfIndex.setStatus("mandatory")


class _DecElanConfName_Type(OctetString):
    """Custom type decElanConfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DecElanConfName_Type.__name__ = "OctetString"
_DecElanConfName_Object = MibTableColumn
decElanConfName = _DecElanConfName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 2, 1, 2),
    _DecElanConfName_Type()
)
decElanConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanConfName.setStatus("mandatory")
_DecElanConfTlvIndex_Type = Integer32
_DecElanConfTlvIndex_Object = MibTableColumn
decElanConfTlvIndex = _DecElanConfTlvIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 2, 1, 3),
    _DecElanConfTlvIndex_Type()
)
decElanConfTlvIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanConfTlvIndex.setStatus("mandatory")


class _DecElanConfLanType_Type(Integer32):
    """Custom type decElanConfLanType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("s8023", 2),
          ("s8025", 3))
    )


_DecElanConfLanType_Type.__name__ = "Integer32"
_DecElanConfLanType_Object = MibTableColumn
decElanConfLanType = _DecElanConfLanType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 2, 1, 4),
    _DecElanConfLanType_Type()
)
decElanConfLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanConfLanType.setStatus("mandatory")


class _DecElanConfMaxFrameSize_Type(Integer32):
    """Custom type decElanConfMaxFrameSize based on Integer32"""
    defaultValue = 1

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
        *(("max1516", 2),
          ("max18190", 5),
          ("max4544", 3),
          ("max9234", 4),
          ("unspecified", 1))
    )


_DecElanConfMaxFrameSize_Type.__name__ = "Integer32"
_DecElanConfMaxFrameSize_Object = MibTableColumn
decElanConfMaxFrameSize = _DecElanConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 2, 1, 5),
    _DecElanConfMaxFrameSize_Type()
)
decElanConfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanConfMaxFrameSize.setStatus("mandatory")


class _DecElanConfAdminStatus_Type(Integer32):
    """Custom type decElanConfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DecElanConfAdminStatus_Type.__name__ = "Integer32"
_DecElanConfAdminStatus_Object = MibTableColumn
decElanConfAdminStatus = _DecElanConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 2, 1, 6),
    _DecElanConfAdminStatus_Type()
)
decElanConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanConfAdminStatus.setStatus("mandatory")


class _DecElanConfDefaultElan_Type(Integer32):
    """Custom type decElanConfDefaultElan based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_DecElanConfDefaultElan_Type.__name__ = "Integer32"
_DecElanConfDefaultElan_Object = MibTableColumn
decElanConfDefaultElan = _DecElanConfDefaultElan_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 2, 1, 7),
    _DecElanConfDefaultElan_Type()
)
decElanConfDefaultElan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanConfDefaultElan.setStatus("mandatory")


class _DecElanConfRowStatus_Type(Integer32):
    """Custom type decElanConfRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecElanConfRowStatus_Type.__name__ = "Integer32"
_DecElanConfRowStatus_Object = MibTableColumn
decElanConfRowStatus = _DecElanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 2, 1, 8),
    _DecElanConfRowStatus_Type()
)
decElanConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanConfRowStatus.setStatus("mandatory")
_DecElanLesTable_Object = MibTable
decElanLesTable = _DecElanLesTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 3)
)
if mibBuilder.loadTexts:
    decElanLesTable.setStatus("mandatory")
_DecElanLesEntry_Object = MibTableRow
decElanLesEntry = _DecElanLesEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 3, 1)
)
decElanLesEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decElanConfIndex"),
    (0, "DEC-LECS-MIB", "decElanLesIndex"),
)
if mibBuilder.loadTexts:
    decElanLesEntry.setStatus("mandatory")
_DecElanLesIndex_Type = Integer32
_DecElanLesIndex_Object = MibTableColumn
decElanLesIndex = _DecElanLesIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 3, 1, 1),
    _DecElanLesIndex_Type()
)
decElanLesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decElanLesIndex.setStatus("mandatory")


class _DecElanLesAtmAddress_Type(OctetString):
    """Custom type decElanLesAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecElanLesAtmAddress_Type.__name__ = "OctetString"
_DecElanLesAtmAddress_Object = MibTableColumn
decElanLesAtmAddress = _DecElanLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 3, 1, 2),
    _DecElanLesAtmAddress_Type()
)
decElanLesAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanLesAtmAddress.setStatus("mandatory")


class _DecElanLesRowStatus_Type(Integer32):
    """Custom type decElanLesRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecElanLesRowStatus_Type.__name__ = "Integer32"
_DecElanLesRowStatus_Object = MibTableColumn
decElanLesRowStatus = _DecElanLesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 3, 1, 3),
    _DecElanLesRowStatus_Type()
)
decElanLesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanLesRowStatus.setStatus("mandatory")
_DecElanPolicyTable_Object = MibTable
decElanPolicyTable = _DecElanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 4)
)
if mibBuilder.loadTexts:
    decElanPolicyTable.setStatus("mandatory")
_DecElanPolicyEntry_Object = MibTableRow
decElanPolicyEntry = _DecElanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 4, 1)
)
decElanPolicyEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decElanPolicySelectorIndex"),
    (0, "DEC-LECS-MIB", "decElanPolicyIndex"),
)
if mibBuilder.loadTexts:
    decElanPolicyEntry.setStatus("mandatory")
_DecElanPolicySelectorIndex_Type = Integer32
_DecElanPolicySelectorIndex_Object = MibTableColumn
decElanPolicySelectorIndex = _DecElanPolicySelectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 4, 1, 1),
    _DecElanPolicySelectorIndex_Type()
)
decElanPolicySelectorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decElanPolicySelectorIndex.setStatus("mandatory")


class _DecElanPolicyIndex_Type(Integer32):
    """Custom type decElanPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_DecElanPolicyIndex_Type.__name__ = "Integer32"
_DecElanPolicyIndex_Object = MibTableColumn
decElanPolicyIndex = _DecElanPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 4, 1, 2),
    _DecElanPolicyIndex_Type()
)
decElanPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decElanPolicyIndex.setStatus("mandatory")


class _DecElanPolicyPriority_Type(Integer32):
    """Custom type decElanPolicyPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_DecElanPolicyPriority_Type.__name__ = "Integer32"
_DecElanPolicyPriority_Object = MibTableColumn
decElanPolicyPriority = _DecElanPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 4, 1, 3),
    _DecElanPolicyPriority_Type()
)
decElanPolicyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanPolicyPriority.setStatus("mandatory")
_DecElanPolicyType_Type = ObjectIdentifier
_DecElanPolicyType_Object = MibTableColumn
decElanPolicyType = _DecElanPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 4, 1, 4),
    _DecElanPolicyType_Type()
)
decElanPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanPolicyType.setStatus("mandatory")


class _DecElanPolicyRowStatus_Type(Integer32):
    """Custom type decElanPolicyRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecElanPolicyRowStatus_Type.__name__ = "Integer32"
_DecElanPolicyRowStatus_Object = MibTableColumn
decElanPolicyRowStatus = _DecElanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 4, 1, 5),
    _DecElanPolicyRowStatus_Type()
)
decElanPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanPolicyRowStatus.setStatus("mandatory")
_DecElanLecAtmAddrTable_Object = MibTable
decElanLecAtmAddrTable = _DecElanLecAtmAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 5)
)
if mibBuilder.loadTexts:
    decElanLecAtmAddrTable.setStatus("mandatory")
_DecElanLecAtmAddrEntry_Object = MibTableRow
decElanLecAtmAddrEntry = _DecElanLecAtmAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 5, 1)
)
decElanLecAtmAddrEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decElanConfIndex"),
    (0, "DEC-LECS-MIB", "decElanLesIndex"),
    (0, "DEC-LECS-MIB", "decElanLecAtmAddress"),
    (0, "DEC-LECS-MIB", "decElanLecAtmMask"),
)
if mibBuilder.loadTexts:
    decElanLecAtmAddrEntry.setStatus("mandatory")


class _DecElanLecAtmAddress_Type(OctetString):
    """Custom type decElanLecAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecElanLecAtmAddress_Type.__name__ = "OctetString"
_DecElanLecAtmAddress_Object = MibTableColumn
decElanLecAtmAddress = _DecElanLecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 5, 1, 1),
    _DecElanLecAtmAddress_Type()
)
decElanLecAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decElanLecAtmAddress.setStatus("mandatory")


class _DecElanLecAtmMask_Type(OctetString):
    """Custom type decElanLecAtmMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecElanLecAtmMask_Type.__name__ = "OctetString"
_DecElanLecAtmMask_Object = MibTableColumn
decElanLecAtmMask = _DecElanLecAtmMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 5, 1, 2),
    _DecElanLecAtmMask_Type()
)
decElanLecAtmMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decElanLecAtmMask.setStatus("mandatory")


class _DecElanLecAtmRowStatus_Type(Integer32):
    """Custom type decElanLecAtmRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecElanLecAtmRowStatus_Type.__name__ = "Integer32"
_DecElanLecAtmRowStatus_Object = MibTableColumn
decElanLecAtmRowStatus = _DecElanLecAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 5, 1, 3),
    _DecElanLecAtmRowStatus_Type()
)
decElanLecAtmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanLecAtmRowStatus.setStatus("mandatory")
_DecElanLecMacAddrTable_Object = MibTable
decElanLecMacAddrTable = _DecElanLecMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 6)
)
if mibBuilder.loadTexts:
    decElanLecMacAddrTable.setStatus("mandatory")
_DecElanLecMacAddrEntry_Object = MibTableRow
decElanLecMacAddrEntry = _DecElanLecMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 6, 1)
)
decElanLecMacAddrEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decElanConfIndex"),
    (0, "DEC-LECS-MIB", "decElanLesIndex"),
    (0, "DEC-LECS-MIB", "decElanLecMacAddress"),
)
if mibBuilder.loadTexts:
    decElanLecMacAddrEntry.setStatus("mandatory")


class _DecElanLecMacAddress_Type(OctetString):
    """Custom type decElanLecMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DecElanLecMacAddress_Type.__name__ = "OctetString"
_DecElanLecMacAddress_Object = MibTableColumn
decElanLecMacAddress = _DecElanLecMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 6, 1, 1),
    _DecElanLecMacAddress_Type()
)
decElanLecMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decElanLecMacAddress.setStatus("mandatory")


class _DecElanLecMacRowStatus_Type(Integer32):
    """Custom type decElanLecMacRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecElanLecMacRowStatus_Type.__name__ = "Integer32"
_DecElanLecMacRowStatus_Object = MibTableColumn
decElanLecMacRowStatus = _DecElanLecMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 6, 1, 2),
    _DecElanLecMacRowStatus_Type()
)
decElanLecMacRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanLecMacRowStatus.setStatus("mandatory")
_DecElanLecRdTable_Object = MibTable
decElanLecRdTable = _DecElanLecRdTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 7)
)
if mibBuilder.loadTexts:
    decElanLecRdTable.setStatus("mandatory")
_DecElanLecRdEntry_Object = MibTableRow
decElanLecRdEntry = _DecElanLecRdEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 7, 1)
)
decElanLecRdEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decElanConfIndex"),
    (0, "DEC-LECS-MIB", "decElanLesIndex"),
    (0, "DEC-LECS-MIB", "decElanLecRdSegId"),
    (0, "DEC-LECS-MIB", "decElanLecRdBridgeNum"),
)
if mibBuilder.loadTexts:
    decElanLecRdEntry.setStatus("mandatory")


class _DecElanLecRdSegId_Type(Integer32):
    """Custom type decElanLecRdSegId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_DecElanLecRdSegId_Type.__name__ = "Integer32"
_DecElanLecRdSegId_Object = MibTableColumn
decElanLecRdSegId = _DecElanLecRdSegId_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 7, 1, 1),
    _DecElanLecRdSegId_Type()
)
decElanLecRdSegId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decElanLecRdSegId.setStatus("mandatory")


class _DecElanLecRdBridgeNum_Type(Integer32):
    """Custom type decElanLecRdBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DecElanLecRdBridgeNum_Type.__name__ = "Integer32"
_DecElanLecRdBridgeNum_Object = MibTableColumn
decElanLecRdBridgeNum = _DecElanLecRdBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 7, 1, 2),
    _DecElanLecRdBridgeNum_Type()
)
decElanLecRdBridgeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decElanLecRdBridgeNum.setStatus("mandatory")


class _DecElanLecRdRowStatus_Type(Integer32):
    """Custom type decElanLecRdRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecElanLecRdRowStatus_Type.__name__ = "Integer32"
_DecElanLecRdRowStatus_Object = MibTableColumn
decElanLecRdRowStatus = _DecElanLecRdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 2, 7, 1, 3),
    _DecElanLecRdRowStatus_Type()
)
decElanLecRdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decElanLecRdRowStatus.setStatus("mandatory")
_DecElanLecsGroup_ObjectIdentity = ObjectIdentity
decElanLecsGroup = _DecElanLecsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3)
)
_DecElanLecsConfGroup_ObjectIdentity = ObjectIdentity
decElanLecsConfGroup = _DecElanLecsConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1)
)
_DecLecsConfNextId_Type = Integer32
_DecLecsConfNextId_Object = MibScalar
decLecsConfNextId = _DecLecsConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 1),
    _DecLecsConfNextId_Type()
)
decLecsConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsConfNextId.setStatus("mandatory")
_DecLecsConfTable_Object = MibTable
decLecsConfTable = _DecLecsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2)
)
if mibBuilder.loadTexts:
    decLecsConfTable.setStatus("mandatory")
_DecLecsConfEntry_Object = MibTableRow
decLecsConfEntry = _DecLecsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1)
)
decLecsConfEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decLecsConfIndex"),
)
if mibBuilder.loadTexts:
    decLecsConfEntry.setStatus("mandatory")
_DecLecsConfIndex_Type = Integer32
_DecLecsConfIndex_Object = MibTableColumn
decLecsConfIndex = _DecLecsConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1, 1),
    _DecLecsConfIndex_Type()
)
decLecsConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsConfIndex.setStatus("mandatory")


class _DecLecsAtmIfIndex_Type(Integer32):
    """Custom type decLecsAtmIfIndex based on Integer32"""
    defaultHexValue = 0


_DecLecsAtmIfIndex_Object = MibTableColumn
decLecsAtmIfIndex = _DecLecsAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1, 2),
    _DecLecsAtmIfIndex_Type()
)
decLecsAtmIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLecsAtmIfIndex.setStatus("mandatory")


class _DecLecsAtmAddrSpec_Type(OctetString):
    """Custom type decLecsAtmAddrSpec based on OctetString"""
    defaultHexValue = "4700790000000000000000000000A03E00000100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLecsAtmAddrSpec_Type.__name__ = "OctetString"
_DecLecsAtmAddrSpec_Object = MibTableColumn
decLecsAtmAddrSpec = _DecLecsAtmAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1, 3),
    _DecLecsAtmAddrSpec_Type()
)
decLecsAtmAddrSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLecsAtmAddrSpec.setStatus("mandatory")


class _DecLecsAtmAddrMask_Type(OctetString):
    """Custom type decLecsAtmAddrMask based on OctetString"""
    defaultHexValue = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_DecLecsAtmAddrMask_Type.__name__ = "OctetString"
_DecLecsAtmAddrMask_Object = MibTableColumn
decLecsAtmAddrMask = _DecLecsAtmAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1, 4),
    _DecLecsAtmAddrMask_Type()
)
decLecsAtmAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLecsAtmAddrMask.setStatus("mandatory")


class _DecLecsAtmAddrActual_Type(OctetString):
    """Custom type decLecsAtmAddrActual based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLecsAtmAddrActual_Type.__name__ = "OctetString"
_DecLecsAtmAddrActual_Object = MibTableColumn
decLecsAtmAddrActual = _DecLecsAtmAddrActual_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1, 5),
    _DecLecsAtmAddrActual_Type()
)
decLecsAtmAddrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsAtmAddrActual.setStatus("mandatory")
_DecLecsPolicySelIndex_Type = Integer32
_DecLecsPolicySelIndex_Object = MibTableColumn
decLecsPolicySelIndex = _DecLecsPolicySelIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1, 6),
    _DecLecsPolicySelIndex_Type()
)
decLecsPolicySelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsPolicySelIndex.setStatus("mandatory")
_DecLecsLastInitialized_Type = TimeTicks
_DecLecsLastInitialized_Object = MibTableColumn
decLecsLastInitialized = _DecLecsLastInitialized_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1, 7),
    _DecLecsLastInitialized_Type()
)
decLecsLastInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsLastInitialized.setStatus("mandatory")


class _DecLecsOperStatus_Type(Integer32):
    """Custom type decLecsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_DecLecsOperStatus_Type.__name__ = "Integer32"
_DecLecsOperStatus_Object = MibTableColumn
decLecsOperStatus = _DecLecsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1, 8),
    _DecLecsOperStatus_Type()
)
decLecsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsOperStatus.setStatus("mandatory")


class _DecLecsAdminStatus_Type(Integer32):
    """Custom type decLecsAdminStatus based on Integer32"""
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


_DecLecsAdminStatus_Type.__name__ = "Integer32"
_DecLecsAdminStatus_Object = MibTableColumn
decLecsAdminStatus = _DecLecsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1, 9),
    _DecLecsAdminStatus_Type()
)
decLecsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLecsAdminStatus.setStatus("mandatory")


class _DecLecsRowStatus_Type(Integer32):
    """Custom type decLecsRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecLecsRowStatus_Type.__name__ = "Integer32"
_DecLecsRowStatus_Object = MibTableColumn
decLecsRowStatus = _DecLecsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 2, 1, 10),
    _DecLecsRowStatus_Type()
)
decLecsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLecsRowStatus.setStatus("mandatory")
_DecLecsTlvTable_Object = MibTable
decLecsTlvTable = _DecLecsTlvTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 4)
)
if mibBuilder.loadTexts:
    decLecsTlvTable.setStatus("mandatory")
_DecLecsTlvEntry_Object = MibTableRow
decLecsTlvEntry = _DecLecsTlvEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 4, 1)
)
decLecsTlvEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decLecsTlvSelectorIndex"),
    (0, "DEC-LECS-MIB", "decLecsTlvTag"),
    (0, "DEC-LECS-MIB", "decLecsTlvIndex"),
)
if mibBuilder.loadTexts:
    decLecsTlvEntry.setStatus("mandatory")
_DecLecsTlvSelectorIndex_Type = Integer32
_DecLecsTlvSelectorIndex_Object = MibTableColumn
decLecsTlvSelectorIndex = _DecLecsTlvSelectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 4, 1, 1),
    _DecLecsTlvSelectorIndex_Type()
)
decLecsTlvSelectorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsTlvSelectorIndex.setStatus("mandatory")


class _DecLecsTlvTag_Type(OctetString):
    """Custom type decLecsTlvTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DecLecsTlvTag_Type.__name__ = "OctetString"
_DecLecsTlvTag_Object = MibTableColumn
decLecsTlvTag = _DecLecsTlvTag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 4, 1, 2),
    _DecLecsTlvTag_Type()
)
decLecsTlvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsTlvTag.setStatus("mandatory")


class _DecLecsTlvIndex_Type(Integer32):
    """Custom type decLecsTlvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DecLecsTlvIndex_Type.__name__ = "Integer32"
_DecLecsTlvIndex_Object = MibTableColumn
decLecsTlvIndex = _DecLecsTlvIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 4, 1, 3),
    _DecLecsTlvIndex_Type()
)
decLecsTlvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsTlvIndex.setStatus("mandatory")


class _DecLecsTlvVal_Type(OctetString):
    """Custom type decLecsTlvVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_DecLecsTlvVal_Type.__name__ = "OctetString"
_DecLecsTlvVal_Object = MibTableColumn
decLecsTlvVal = _DecLecsTlvVal_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 4, 1, 4),
    _DecLecsTlvVal_Type()
)
decLecsTlvVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLecsTlvVal.setStatus("mandatory")


class _DecLecsTlvRowStatus_Type(Integer32):
    """Custom type decLecsTlvRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecLecsTlvRowStatus_Type.__name__ = "Integer32"
_DecLecsTlvRowStatus_Object = MibTableColumn
decLecsTlvRowStatus = _DecLecsTlvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 1, 4, 1, 5),
    _DecLecsTlvRowStatus_Type()
)
decLecsTlvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLecsTlvRowStatus.setStatus("mandatory")
_DecElanLecsFaultGroup_ObjectIdentity = ObjectIdentity
decElanLecsFaultGroup = _DecElanLecsFaultGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2)
)
_DecLecsErrCtlTable_Object = MibTable
decLecsErrCtlTable = _DecLecsErrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 1)
)
if mibBuilder.loadTexts:
    decLecsErrCtlTable.setStatus("mandatory")
_DecLecsErrCtlEntry_Object = MibTableRow
decLecsErrCtlEntry = _DecLecsErrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 1, 1)
)
decLecsErrCtlEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decLecsConfIndex"),
)
if mibBuilder.loadTexts:
    decLecsErrCtlEntry.setStatus("mandatory")


class _DecLecsErrCtlAdminStatus_Type(Integer32):
    """Custom type decLecsErrCtlAdminStatus based on Integer32"""
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


_DecLecsErrCtlAdminStatus_Type.__name__ = "Integer32"
_DecLecsErrCtlAdminStatus_Object = MibTableColumn
decLecsErrCtlAdminStatus = _DecLecsErrCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 1, 1, 1),
    _DecLecsErrCtlAdminStatus_Type()
)
decLecsErrCtlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLecsErrCtlAdminStatus.setStatus("mandatory")


class _DecLecsErrCtlOperStatus_Type(Integer32):
    """Custom type decLecsErrCtlOperStatus based on Integer32"""
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
        *(("active", 2),
          ("failed", 4),
          ("other", 1),
          ("outOfRes", 3))
    )


_DecLecsErrCtlOperStatus_Type.__name__ = "Integer32"
_DecLecsErrCtlOperStatus_Object = MibTableColumn
decLecsErrCtlOperStatus = _DecLecsErrCtlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 1, 1, 2),
    _DecLecsErrCtlOperStatus_Type()
)
decLecsErrCtlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsErrCtlOperStatus.setStatus("mandatory")


class _DecLecsErrCtlClearLog_Type(Integer32):
    """Custom type decLecsErrCtlClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noOp", 1))
    )


_DecLecsErrCtlClearLog_Type.__name__ = "Integer32"
_DecLecsErrCtlClearLog_Object = MibTableColumn
decLecsErrCtlClearLog = _DecLecsErrCtlClearLog_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 1, 1, 3),
    _DecLecsErrCtlClearLog_Type()
)
decLecsErrCtlClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLecsErrCtlClearLog.setStatus("mandatory")


class _DecLecsErrCtlMaxEntries_Type(Integer32):
    """Custom type decLecsErrCtlMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DecLecsErrCtlMaxEntries_Type.__name__ = "Integer32"
_DecLecsErrCtlMaxEntries_Object = MibTableColumn
decLecsErrCtlMaxEntries = _DecLecsErrCtlMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 1, 1, 4),
    _DecLecsErrCtlMaxEntries_Type()
)
decLecsErrCtlMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsErrCtlMaxEntries.setStatus("mandatory")
_DecLecsErrCtlLastEntry_Type = Integer32
_DecLecsErrCtlLastEntry_Object = MibTableColumn
decLecsErrCtlLastEntry = _DecLecsErrCtlLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 1, 1, 5),
    _DecLecsErrCtlLastEntry_Type()
)
decLecsErrCtlLastEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLecsErrCtlLastEntry.setStatus("mandatory")
_DecLecsErrLogTable_Object = MibTable
decLecsErrLogTable = _DecLecsErrLogTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 2)
)
if mibBuilder.loadTexts:
    decLecsErrLogTable.setStatus("mandatory")
_DecLecsErrLogEntry_Object = MibTableRow
decLecsErrLogEntry = _DecLecsErrLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 2, 1)
)
decLecsErrLogEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decLecsConfIndex"),
    (0, "DEC-LECS-MIB", "decLecsErrLogIndex"),
)
if mibBuilder.loadTexts:
    decLecsErrLogEntry.setStatus("mandatory")
_DecLecsErrLogIndex_Type = Integer32
_DecLecsErrLogIndex_Object = MibTableColumn
decLecsErrLogIndex = _DecLecsErrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 2, 1, 1),
    _DecLecsErrLogIndex_Type()
)
decLecsErrLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsErrLogIndex.setStatus("mandatory")


class _DecLecsErrLogAtmAddr_Type(OctetString):
    """Custom type decLecsErrLogAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLecsErrLogAtmAddr_Type.__name__ = "OctetString"
_DecLecsErrLogAtmAddr_Object = MibTableColumn
decLecsErrLogAtmAddr = _DecLecsErrLogAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 2, 1, 2),
    _DecLecsErrLogAtmAddr_Type()
)
decLecsErrLogAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsErrLogAtmAddr.setStatus("mandatory")


class _DecLecsErrLogErrCode_Type(Integer32):
    """Custom type decLecsErrLogErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22),
    )


_DecLecsErrLogErrCode_Type.__name__ = "Integer32"
_DecLecsErrLogErrCode_Object = MibTableColumn
decLecsErrLogErrCode = _DecLecsErrLogErrCode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 2, 1, 3),
    _DecLecsErrLogErrCode_Type()
)
decLecsErrLogErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsErrLogErrCode.setStatus("mandatory")
_DecLecsErrLogTime_Type = TimeTicks
_DecLecsErrLogTime_Object = MibTableColumn
decLecsErrLogTime = _DecLecsErrLogTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 2, 2, 1, 4),
    _DecLecsErrLogTime_Type()
)
decLecsErrLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsErrLogTime.setStatus("mandatory")
_DecElanLecsStatGroup_ObjectIdentity = ObjectIdentity
decElanLecsStatGroup = _DecElanLecsStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3)
)
_DecLecsStatsTable_Object = MibTable
decLecsStatsTable = _DecLecsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1)
)
if mibBuilder.loadTexts:
    decLecsStatsTable.setStatus("mandatory")
_DecLecsStatsEntry_Object = MibTableRow
decLecsStatsEntry = _DecLecsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1)
)
decLecsStatsEntry.setIndexNames(
    (0, "DEC-LECS-MIB", "decLecsConfIndex"),
)
if mibBuilder.loadTexts:
    decLecsStatsEntry.setStatus("mandatory")
_DecLecsStatSuccessful_Type = Counter32
_DecLecsStatSuccessful_Object = MibTableColumn
decLecsStatSuccessful = _DecLecsStatSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 1),
    _DecLecsStatSuccessful_Type()
)
decLecsStatSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatSuccessful.setStatus("mandatory")
_DecLecsStatInBadFrames_Type = Counter32
_DecLecsStatInBadFrames_Object = MibTableColumn
decLecsStatInBadFrames = _DecLecsStatInBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 2),
    _DecLecsStatInBadFrames_Type()
)
decLecsStatInBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatInBadFrames.setStatus("mandatory")
_DecLecsStatInvalidParam_Type = Counter32
_DecLecsStatInvalidParam_Object = MibTableColumn
decLecsStatInvalidParam = _DecLecsStatInvalidParam_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 3),
    _DecLecsStatInvalidParam_Type()
)
decLecsStatInvalidParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatInvalidParam.setStatus("mandatory")
_DecLecsStatInsufRes_Type = Counter32
_DecLecsStatInsufRes_Object = MibTableColumn
decLecsStatInsufRes = _DecLecsStatInsufRes_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 4),
    _DecLecsStatInsufRes_Type()
)
decLecsStatInsufRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatInsufRes.setStatus("mandatory")
_DecLecsStatAccDenied_Type = Counter32
_DecLecsStatAccDenied_Object = MibTableColumn
decLecsStatAccDenied = _DecLecsStatAccDenied_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 5),
    _DecLecsStatAccDenied_Type()
)
decLecsStatAccDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatAccDenied.setStatus("mandatory")
_DecLecsStatInvalidReq_Type = Counter32
_DecLecsStatInvalidReq_Object = MibTableColumn
decLecsStatInvalidReq = _DecLecsStatInvalidReq_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 6),
    _DecLecsStatInvalidReq_Type()
)
decLecsStatInvalidReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatInvalidReq.setStatus("mandatory")
_DecLecsStatInvalidDest_Type = Counter32
_DecLecsStatInvalidDest_Object = MibTableColumn
decLecsStatInvalidDest = _DecLecsStatInvalidDest_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 7),
    _DecLecsStatInvalidDest_Type()
)
decLecsStatInvalidDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatInvalidDest.setStatus("mandatory")
_DecLecsStatInvalidAddr_Type = Counter32
_DecLecsStatInvalidAddr_Object = MibTableColumn
decLecsStatInvalidAddr = _DecLecsStatInvalidAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 8),
    _DecLecsStatInvalidAddr_Type()
)
decLecsStatInvalidAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatInvalidAddr.setStatus("mandatory")
_DecLecsStatNoConf_Type = Counter32
_DecLecsStatNoConf_Object = MibTableColumn
decLecsStatNoConf = _DecLecsStatNoConf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 9),
    _DecLecsStatNoConf_Type()
)
decLecsStatNoConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatNoConf.setStatus("mandatory")
_DecLecsStatConfError_Type = Counter32
_DecLecsStatConfError_Object = MibTableColumn
decLecsStatConfError = _DecLecsStatConfError_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 10),
    _DecLecsStatConfError_Type()
)
decLecsStatConfError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatConfError.setStatus("mandatory")
_DecLecsStatInsufInfo_Type = Counter32
_DecLecsStatInsufInfo_Object = MibTableColumn
decLecsStatInsufInfo = _DecLecsStatInsufInfo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 3, 3, 1, 1, 11),
    _DecLecsStatInsufInfo_Type()
)
decLecsStatInsufInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLecsStatInsufInfo.setStatus("mandatory")
_DecLecsMIBConformance_ObjectIdentity = ObjectIdentity
decLecsMIBConformance = _DecLecsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4)
)
_DecLecsMIBGroups_ObjectIdentity = ObjectIdentity
decLecsMIBGroups = _DecLecsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4, 1)
)
_DecElanCConfGroup_ObjectIdentity = ObjectIdentity
decElanCConfGroup = _DecElanCConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4, 1, 1)
)
_DecElanLecAssignByAtmGroup_ObjectIdentity = ObjectIdentity
decElanLecAssignByAtmGroup = _DecElanLecAssignByAtmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4, 1, 2)
)
_DecElanLecAssignByMacGroup_ObjectIdentity = ObjectIdentity
decElanLecAssignByMacGroup = _DecElanLecAssignByMacGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4, 1, 3)
)
_DecElanLecAssignByRdGroup_ObjectIdentity = ObjectIdentity
decElanLecAssignByRdGroup = _DecElanLecAssignByRdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4, 1, 4)
)
_DecLecsCStatGroup_ObjectIdentity = ObjectIdentity
decLecsCStatGroup = _DecLecsCStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4, 1, 5)
)
_DecLecsCGroup_ObjectIdentity = ObjectIdentity
decLecsCGroup = _DecLecsCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4, 1, 6)
)
_DecLecsCFaultGroup_ObjectIdentity = ObjectIdentity
decLecsCFaultGroup = _DecLecsCFaultGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4, 1, 7)
)
_DecLecsMIBCompliances_ObjectIdentity = ObjectIdentity
decLecsMIBCompliances = _DecLecsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4, 2)
)
_DecLecsMIBCompliance_ObjectIdentity = ObjectIdentity
decLecsMIBCompliance = _DecLecsMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 31, 4, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEC-LECS-MIB",
    **{"decLecsMIB": decLecsMIB,
       "decElanAdminGroup": decElanAdminGroup,
       "decElanAdminPolicyVal": decElanAdminPolicyVal,
       "assignByAtmAddr": assignByAtmAddr,
       "assignByMacAddr": assignByMacAddr,
       "assignByRouteDescriptor": assignByRouteDescriptor,
       "assignByElanName": assignByElanName,
       "assignByCompatibility": assignByCompatibility,
       "decElanConfGroup": decElanConfGroup,
       "decElanConfNextId": decElanConfNextId,
       "decElanConfTable": decElanConfTable,
       "decElanConfEntry": decElanConfEntry,
       "decElanConfIndex": decElanConfIndex,
       "decElanConfName": decElanConfName,
       "decElanConfTlvIndex": decElanConfTlvIndex,
       "decElanConfLanType": decElanConfLanType,
       "decElanConfMaxFrameSize": decElanConfMaxFrameSize,
       "decElanConfAdminStatus": decElanConfAdminStatus,
       "decElanConfDefaultElan": decElanConfDefaultElan,
       "decElanConfRowStatus": decElanConfRowStatus,
       "decElanLesTable": decElanLesTable,
       "decElanLesEntry": decElanLesEntry,
       "decElanLesIndex": decElanLesIndex,
       "decElanLesAtmAddress": decElanLesAtmAddress,
       "decElanLesRowStatus": decElanLesRowStatus,
       "decElanPolicyTable": decElanPolicyTable,
       "decElanPolicyEntry": decElanPolicyEntry,
       "decElanPolicySelectorIndex": decElanPolicySelectorIndex,
       "decElanPolicyIndex": decElanPolicyIndex,
       "decElanPolicyPriority": decElanPolicyPriority,
       "decElanPolicyType": decElanPolicyType,
       "decElanPolicyRowStatus": decElanPolicyRowStatus,
       "decElanLecAtmAddrTable": decElanLecAtmAddrTable,
       "decElanLecAtmAddrEntry": decElanLecAtmAddrEntry,
       "decElanLecAtmAddress": decElanLecAtmAddress,
       "decElanLecAtmMask": decElanLecAtmMask,
       "decElanLecAtmRowStatus": decElanLecAtmRowStatus,
       "decElanLecMacAddrTable": decElanLecMacAddrTable,
       "decElanLecMacAddrEntry": decElanLecMacAddrEntry,
       "decElanLecMacAddress": decElanLecMacAddress,
       "decElanLecMacRowStatus": decElanLecMacRowStatus,
       "decElanLecRdTable": decElanLecRdTable,
       "decElanLecRdEntry": decElanLecRdEntry,
       "decElanLecRdSegId": decElanLecRdSegId,
       "decElanLecRdBridgeNum": decElanLecRdBridgeNum,
       "decElanLecRdRowStatus": decElanLecRdRowStatus,
       "decElanLecsGroup": decElanLecsGroup,
       "decElanLecsConfGroup": decElanLecsConfGroup,
       "decLecsConfNextId": decLecsConfNextId,
       "decLecsConfTable": decLecsConfTable,
       "decLecsConfEntry": decLecsConfEntry,
       "decLecsConfIndex": decLecsConfIndex,
       "decLecsAtmIfIndex": decLecsAtmIfIndex,
       "decLecsAtmAddrSpec": decLecsAtmAddrSpec,
       "decLecsAtmAddrMask": decLecsAtmAddrMask,
       "decLecsAtmAddrActual": decLecsAtmAddrActual,
       "decLecsPolicySelIndex": decLecsPolicySelIndex,
       "decLecsLastInitialized": decLecsLastInitialized,
       "decLecsOperStatus": decLecsOperStatus,
       "decLecsAdminStatus": decLecsAdminStatus,
       "decLecsRowStatus": decLecsRowStatus,
       "decLecsTlvTable": decLecsTlvTable,
       "decLecsTlvEntry": decLecsTlvEntry,
       "decLecsTlvSelectorIndex": decLecsTlvSelectorIndex,
       "decLecsTlvTag": decLecsTlvTag,
       "decLecsTlvIndex": decLecsTlvIndex,
       "decLecsTlvVal": decLecsTlvVal,
       "decLecsTlvRowStatus": decLecsTlvRowStatus,
       "decElanLecsFaultGroup": decElanLecsFaultGroup,
       "decLecsErrCtlTable": decLecsErrCtlTable,
       "decLecsErrCtlEntry": decLecsErrCtlEntry,
       "decLecsErrCtlAdminStatus": decLecsErrCtlAdminStatus,
       "decLecsErrCtlOperStatus": decLecsErrCtlOperStatus,
       "decLecsErrCtlClearLog": decLecsErrCtlClearLog,
       "decLecsErrCtlMaxEntries": decLecsErrCtlMaxEntries,
       "decLecsErrCtlLastEntry": decLecsErrCtlLastEntry,
       "decLecsErrLogTable": decLecsErrLogTable,
       "decLecsErrLogEntry": decLecsErrLogEntry,
       "decLecsErrLogIndex": decLecsErrLogIndex,
       "decLecsErrLogAtmAddr": decLecsErrLogAtmAddr,
       "decLecsErrLogErrCode": decLecsErrLogErrCode,
       "decLecsErrLogTime": decLecsErrLogTime,
       "decElanLecsStatGroup": decElanLecsStatGroup,
       "decLecsStatsTable": decLecsStatsTable,
       "decLecsStatsEntry": decLecsStatsEntry,
       "decLecsStatSuccessful": decLecsStatSuccessful,
       "decLecsStatInBadFrames": decLecsStatInBadFrames,
       "decLecsStatInvalidParam": decLecsStatInvalidParam,
       "decLecsStatInsufRes": decLecsStatInsufRes,
       "decLecsStatAccDenied": decLecsStatAccDenied,
       "decLecsStatInvalidReq": decLecsStatInvalidReq,
       "decLecsStatInvalidDest": decLecsStatInvalidDest,
       "decLecsStatInvalidAddr": decLecsStatInvalidAddr,
       "decLecsStatNoConf": decLecsStatNoConf,
       "decLecsStatConfError": decLecsStatConfError,
       "decLecsStatInsufInfo": decLecsStatInsufInfo,
       "decLecsMIBConformance": decLecsMIBConformance,
       "decLecsMIBGroups": decLecsMIBGroups,
       "decElanCConfGroup": decElanCConfGroup,
       "decElanLecAssignByAtmGroup": decElanLecAssignByAtmGroup,
       "decElanLecAssignByMacGroup": decElanLecAssignByMacGroup,
       "decElanLecAssignByRdGroup": decElanLecAssignByRdGroup,
       "decLecsCStatGroup": decLecsCStatGroup,
       "decLecsCGroup": decLecsCGroup,
       "decLecsCFaultGroup": decLecsCFaultGroup,
       "decLecsMIBCompliances": decLecsMIBCompliances,
       "decLecsMIBCompliance": decLecsMIBCompliance}
)
