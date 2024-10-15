# SNMP MIB module (DES3810-52-SWITCH-RESOURCE-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DES3810-52-SWITCH-RESOURCE-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:25:49 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(des3810_52,) = mibBuilder.importSymbols(
    "SW3810PRIMGMT-MIB",
    "des3810-52")


# MODULE-IDENTITY

swSwitchResourceMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSwitchResourceMgmtMIBObjects_ObjectIdentity = ObjectIdentity
swSwitchResourceMgmtMIBObjects = _SwSwitchResourceMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1)
)


class _SwSwitchResourceMgmtSRMMode_Type(Integer32):
    """Custom type swSwitchResourceMgmtSRMMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("routing", 1),
          ("vpws", 2))
    )


_SwSwitchResourceMgmtSRMMode_Type.__name__ = "Integer32"
_SwSwitchResourceMgmtSRMMode_Object = MibScalar
swSwitchResourceMgmtSRMMode = _SwSwitchResourceMgmtSRMMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1, 2),
    _SwSwitchResourceMgmtSRMMode_Type()
)
swSwitchResourceMgmtSRMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSwitchResourceMgmtSRMMode.setStatus("current")


class _SwSwitchResourceMgmtSRMCurrentMode_Type(Integer32):
    """Custom type swSwitchResourceMgmtSRMCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("routing", 1),
          ("vpws", 2))
    )


_SwSwitchResourceMgmtSRMCurrentMode_Type.__name__ = "Integer32"
_SwSwitchResourceMgmtSRMCurrentMode_Object = MibScalar
swSwitchResourceMgmtSRMCurrentMode = _SwSwitchResourceMgmtSRMCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1, 3),
    _SwSwitchResourceMgmtSRMCurrentMode_Type()
)
swSwitchResourceMgmtSRMCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSwitchResourceMgmtSRMCurrentMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES3810-52-SWITCH-RESOURCE-MGMT-MIB",
    **{"swSwitchResourceMgmtMIB": swSwitchResourceMgmtMIB,
       "swSwitchResourceMgmtMIBObjects": swSwitchResourceMgmtMIBObjects,
       "swSwitchResourceMgmtSRMMode": swSwitchResourceMgmtSRMMode,
       "swSwitchResourceMgmtSRMCurrentMode": swSwitchResourceMgmtSRMCurrentMode}
)
