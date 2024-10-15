# SNMP MIB module (ONEACCESS-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:57 2024
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

(ifAdminStatus,
 ifAlias,
 ifDescr,
 ifIndex,
 ifName,
 ifOperStatus,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifAlias",
    "ifDescr",
    "ifIndex",
    "ifName",
    "ifOperStatus",
    "ifType")

(oacEventText,) = mibBuilder.importSymbols(
    "ONEACCESS-EVENTS-MIB",
    "oacEventText")

(oacExpIMIsdn,
 oacExpIMIsdnNotifications,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIsdn",
    "oacExpIMIsdnNotifications",
    "oacMIBModules")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

oacIsdnMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 674)
)
oacIsdnMIBModule.setRevisions(
        ("2011-10-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

dialDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 7, 0, 3)
)
dialDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    dialDown.setStatus(
        "current"
    )

dialUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 7, 0, 4)
)
dialUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    dialUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-ISDN-MIB",
    **{"oacIsdnMIBModule": oacIsdnMIBModule,
       "dialDown": dialDown,
       "dialUp": dialUp}
)
