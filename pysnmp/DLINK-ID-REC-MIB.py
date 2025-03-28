# SNMP MIB module (DLINK-ID-REC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-ID-REC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:26 2024
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



class AgentNotifyLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 4),
          ("critical", 0),
          ("debug", 7),
          ("emergency", 3),
          ("error", 5),
          ("information", 2),
          ("notice", 6),
          ("warning", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Dlink_products_ObjectIdentity = ObjectIdentity
dlink_products = _Dlink_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10)
)
_Dlink_mgmt_ObjectIdentity = ObjectIdentity
dlink_mgmt = _Dlink_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11)
)
_Dlink_common_mgmt_ObjectIdentity = ObjectIdentity
dlink_common_mgmt = _Dlink_common_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12)
)
_Dlink_broadband_products_ObjectIdentity = ObjectIdentity
dlink_broadband_products = _Dlink_broadband_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 30)
)
_Dlink_broadband_mgmt_ObjectIdentity = ObjectIdentity
dlink_broadband_mgmt = _Dlink_broadband_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 31)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-ID-REC-MIB",
    **{"AgentNotifyLevel": AgentNotifyLevel,
       "dlink": dlink,
       "dlink-products": dlink_products,
       "dlink-mgmt": dlink_mgmt,
       "dlink-common-mgmt": dlink_common_mgmt,
       "dlink-broadband-products": dlink_broadband_products,
       "dlink-broadband-mgmt": dlink_broadband_mgmt}
)
