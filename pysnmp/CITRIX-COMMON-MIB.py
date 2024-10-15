# SNMP MIB module (CITRIX-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CITRIX-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:26 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Citrix_ObjectIdentity = ObjectIdentity
citrix = _Citrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 3)
)
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 3, 1)
)
_Metaframe_ObjectIdentity = ObjectIdentity
metaframe = _Metaframe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 3, 1, 1)
)
_ManagementUtilities_ObjectIdentity = ObjectIdentity
managementUtilities = _ManagementUtilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 3, 2)
)
_MetaframeManager_ObjectIdentity = ObjectIdentity
metaframeManager = _MetaframeManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 3, 2, 1)
)
_ProductManagementGroup_ObjectIdentity = ObjectIdentity
productManagementGroup = _ProductManagementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 3, 3)
)
_Rm_ObjectIdentity = ObjectIdentity
rm = _Rm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 3, 3, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CITRIX-COMMON-MIB",
    **{"citrix": citrix,
       "product": product,
       "server": server,
       "metaframe": metaframe,
       "managementUtilities": managementUtilities,
       "metaframeManager": metaframeManager,
       "productManagementGroup": productManagementGroup,
       "rm": rm}
)
