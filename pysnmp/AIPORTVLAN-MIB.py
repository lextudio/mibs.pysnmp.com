# SNMP MIB module (AIPORTVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIPORTVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:13 2024
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

(PositiveInteger,) = mibBuilder.importSymbols(
    "AISYSTEM-MIB",
    "PositiveInteger")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aiPortVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSystemOID_ObjectIdentity = ObjectIdentity
aiSystemOID = _AiSystemOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2)
)
_AiPortVlanCnf_ObjectIdentity = ObjectIdentity
aiPortVlanCnf = _AiPortVlanCnf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 29, 1)
)
_PortVlanCnfTable_Object = MibTable
portVlanCnfTable = _PortVlanCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 29, 1, 1)
)
if mibBuilder.loadTexts:
    portVlanCnfTable.setStatus("current")
_PortVlanCnfEntry_Object = MibTableRow
portVlanCnfEntry = _PortVlanCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 29, 1, 1, 1)
)
portVlanCnfEntry.setIndexNames(
    (0, "AIPORTVLAN-MIB", "portVlanIndex"),
)
if mibBuilder.loadTexts:
    portVlanCnfEntry.setStatus("current")


class _PortVlanIndex_Type(Integer32):
    """Custom type portVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PortVlanIndex_Type.__name__ = "Integer32"
_PortVlanIndex_Object = MibTableColumn
portVlanIndex = _PortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 29, 1, 1, 1, 1),
    _PortVlanIndex_Type()
)
portVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVlanIndex.setStatus("current")


class _PortVlanName_Type(DisplayString):
    """Custom type portVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_PortVlanName_Type.__name__ = "DisplayString"
_PortVlanName_Object = MibTableColumn
portVlanName = _PortVlanName_Object(
    (1, 3, 6, 1, 4, 1, 539, 29, 1, 1, 1, 2),
    _PortVlanName_Type()
)
portVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVlanName.setStatus("current")


class _PortVlanOverlap_Type(Integer32):
    """Custom type portVlanOverlap based on Integer32"""
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


_PortVlanOverlap_Type.__name__ = "Integer32"
_PortVlanOverlap_Object = MibTableColumn
portVlanOverlap = _PortVlanOverlap_Object(
    (1, 3, 6, 1, 4, 1, 539, 29, 1, 1, 1, 3),
    _PortVlanOverlap_Type()
)
portVlanOverlap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVlanOverlap.setStatus("current")
_PortVlanMembershipTable_Object = MibTable
portVlanMembershipTable = _PortVlanMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 29, 1, 2)
)
if mibBuilder.loadTexts:
    portVlanMembershipTable.setStatus("current")
_PortVlanMembershipEntry_Object = MibTableRow
portVlanMembershipEntry = _PortVlanMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 29, 1, 2, 1)
)
portVlanMembershipEntry.setIndexNames(
    (0, "AIPORTVLAN-MIB", "portVlanMembershipVlanIndex"),
    (0, "AIPORTVLAN-MIB", "portVlanMembershipPortIndex"),
)
if mibBuilder.loadTexts:
    portVlanMembershipEntry.setStatus("current")


class _PortVlanMembershipVlanIndex_Type(Integer32):
    """Custom type portVlanMembershipVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PortVlanMembershipVlanIndex_Type.__name__ = "Integer32"
_PortVlanMembershipVlanIndex_Object = MibTableColumn
portVlanMembershipVlanIndex = _PortVlanMembershipVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 29, 1, 2, 1, 1),
    _PortVlanMembershipVlanIndex_Type()
)
portVlanMembershipVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVlanMembershipVlanIndex.setStatus("current")


class _PortVlanMembershipPortIndex_Type(Integer32):
    """Custom type portVlanMembershipPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PortVlanMembershipPortIndex_Type.__name__ = "Integer32"
_PortVlanMembershipPortIndex_Object = MibTableColumn
portVlanMembershipPortIndex = _PortVlanMembershipPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 29, 1, 2, 1, 2),
    _PortVlanMembershipPortIndex_Type()
)
portVlanMembershipPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVlanMembershipPortIndex.setStatus("current")


class _PortVlanMembershipStatus_Type(Integer32):
    """Custom type portVlanMembershipStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("member", 1),
          ("nonmember", 2))
    )


_PortVlanMembershipStatus_Type.__name__ = "Integer32"
_PortVlanMembershipStatus_Object = MibTableColumn
portVlanMembershipStatus = _PortVlanMembershipStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 29, 1, 2, 1, 3),
    _PortVlanMembershipStatus_Type()
)
portVlanMembershipStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVlanMembershipStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIPORTVLAN-MIB",
    **{"aii": aii,
       "aiSystemOID": aiSystemOID,
       "aiPortVlan": aiPortVlan,
       "aiPortVlanCnf": aiPortVlanCnf,
       "portVlanCnfTable": portVlanCnfTable,
       "portVlanCnfEntry": portVlanCnfEntry,
       "portVlanIndex": portVlanIndex,
       "portVlanName": portVlanName,
       "portVlanOverlap": portVlanOverlap,
       "portVlanMembershipTable": portVlanMembershipTable,
       "portVlanMembershipEntry": portVlanMembershipEntry,
       "portVlanMembershipVlanIndex": portVlanMembershipVlanIndex,
       "portVlanMembershipPortIndex": portVlanMembershipPortIndex,
       "portVlanMembershipStatus": portVlanMembershipStatus}
)
