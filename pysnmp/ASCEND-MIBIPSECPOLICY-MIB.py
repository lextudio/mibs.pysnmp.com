# SNMP MIB module (ASCEND-MIBIPSECPOLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIPSECPOLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:45 2024
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

_MibmibProfIpsecPolicy_ObjectIdentity = ObjectIdentity
mibmibProfIpsecPolicy = _MibmibProfIpsecPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 167)
)
_MibmibProfIpsecPolicyTable_Object = MibTable
mibmibProfIpsecPolicyTable = _MibmibProfIpsecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 167, 1)
)
if mibBuilder.loadTexts:
    mibmibProfIpsecPolicyTable.setStatus("mandatory")
_MibmibProfIpsecPolicyEntry_Object = MibTableRow
mibmibProfIpsecPolicyEntry = _MibmibProfIpsecPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1)
)
mibmibProfIpsecPolicyEntry.setIndexNames(
    (0, "ASCEND-MIBIPSECPOLICY-MIB", "mibProfIpsecPolicy-PolicyName"),
)
if mibBuilder.loadTexts:
    mibmibProfIpsecPolicyEntry.setStatus("mandatory")
_MibProfIpsecPolicy_PolicyName_Type = DisplayString
_MibProfIpsecPolicy_PolicyName_Object = MibScalar
mibProfIpsecPolicy_PolicyName = _MibProfIpsecPolicy_PolicyName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 1),
    _MibProfIpsecPolicy_PolicyName_Type()
)
mibProfIpsecPolicy_PolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfIpsecPolicy_PolicyName.setStatus("mandatory")
_MibProfIpsecPolicy_FilterName_Type = DisplayString
_MibProfIpsecPolicy_FilterName_Object = MibScalar
mibProfIpsecPolicy_FilterName = _MibProfIpsecPolicy_FilterName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 2),
    _MibProfIpsecPolicy_FilterName_Type()
)
mibProfIpsecPolicy_FilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsecPolicy_FilterName.setStatus("mandatory")


class _MibProfIpsecPolicy_KeyManagement_Type(Integer32):
    """Custom type mibProfIpsecPolicy_KeyManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ike", 2),
          ("manual", 1))
    )


_MibProfIpsecPolicy_KeyManagement_Type.__name__ = "Integer32"
_MibProfIpsecPolicy_KeyManagement_Object = MibScalar
mibProfIpsecPolicy_KeyManagement = _MibProfIpsecPolicy_KeyManagement_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 3),
    _MibProfIpsecPolicy_KeyManagement_Type()
)
mibProfIpsecPolicy_KeyManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsecPolicy_KeyManagement.setStatus("mandatory")
_MibProfIpsecPolicy_IpsecProposals_Type = DisplayString
_MibProfIpsecPolicy_IpsecProposals_Object = MibScalar
mibProfIpsecPolicy_IpsecProposals = _MibProfIpsecPolicy_IpsecProposals_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 4),
    _MibProfIpsecPolicy_IpsecProposals_Type()
)
mibProfIpsecPolicy_IpsecProposals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsecPolicy_IpsecProposals.setStatus("mandatory")
_MibProfIpsecPolicy_PrimaryTunnelAddress_Type = IpAddress
_MibProfIpsecPolicy_PrimaryTunnelAddress_Object = MibScalar
mibProfIpsecPolicy_PrimaryTunnelAddress = _MibProfIpsecPolicy_PrimaryTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 5),
    _MibProfIpsecPolicy_PrimaryTunnelAddress_Type()
)
mibProfIpsecPolicy_PrimaryTunnelAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsecPolicy_PrimaryTunnelAddress.setStatus("mandatory")
_MibProfIpsecPolicy_SecondaryTunnelAddress_Type = IpAddress
_MibProfIpsecPolicy_SecondaryTunnelAddress_Object = MibScalar
mibProfIpsecPolicy_SecondaryTunnelAddress = _MibProfIpsecPolicy_SecondaryTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 6),
    _MibProfIpsecPolicy_SecondaryTunnelAddress_Type()
)
mibProfIpsecPolicy_SecondaryTunnelAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsecPolicy_SecondaryTunnelAddress.setStatus("mandatory")


class _MibProfIpsecPolicy_Action_o_Type(Integer32):
    """Custom type mibProfIpsecPolicy_Action_o based on Integer32"""
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


_MibProfIpsecPolicy_Action_o_Type.__name__ = "Integer32"
_MibProfIpsecPolicy_Action_o_Object = MibScalar
mibProfIpsecPolicy_Action_o = _MibProfIpsecPolicy_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 7),
    _MibProfIpsecPolicy_Action_o_Type()
)
mibProfIpsecPolicy_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsecPolicy_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIPSECPOLICY-MIB",
    **{"DisplayString": DisplayString,
       "mibmibProfIpsecPolicy": mibmibProfIpsecPolicy,
       "mibmibProfIpsecPolicyTable": mibmibProfIpsecPolicyTable,
       "mibmibProfIpsecPolicyEntry": mibmibProfIpsecPolicyEntry,
       "mibProfIpsecPolicy-PolicyName": mibProfIpsecPolicy_PolicyName,
       "mibProfIpsecPolicy-FilterName": mibProfIpsecPolicy_FilterName,
       "mibProfIpsecPolicy-KeyManagement": mibProfIpsecPolicy_KeyManagement,
       "mibProfIpsecPolicy-IpsecProposals": mibProfIpsecPolicy_IpsecProposals,
       "mibProfIpsecPolicy-PrimaryTunnelAddress": mibProfIpsecPolicy_PrimaryTunnelAddress,
       "mibProfIpsecPolicy-SecondaryTunnelAddress": mibProfIpsecPolicy_SecondaryTunnelAddress,
       "mibProfIpsecPolicy-Action-o": mibProfIpsecPolicy_Action_o}
)
