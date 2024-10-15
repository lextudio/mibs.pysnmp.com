# SNMP MIB module (XEDIA-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:00 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xpimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XpimMIBObjects_ObjectIdentity = ObjectIdentity
xpimMIBObjects = _XpimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 31, 1)
)
_Xpim_ObjectIdentity = ObjectIdentity
xpim = _Xpim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 31, 1, 1)
)


class _XpimVersion_Type(Integer32):
    """Custom type xpimVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XpimVersion_Type.__name__ = "Integer32"
_XpimVersion_Object = MibScalar
xpimVersion = _XpimVersion_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 31, 1, 1, 1),
    _XpimVersion_Type()
)
xpimVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpimVersion.setStatus("current")
_XpimInterfaceTable_Object = MibTable
xpimInterfaceTable = _XpimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 31, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xpimInterfaceTable.setStatus("current")
_XpimInterfaceEntry_Object = MibTableRow
xpimInterfaceEntry = _XpimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 31, 1, 1, 2, 1)
)
xpimInterfaceEntry.setIndexNames(
    (0, "XEDIA-PIM-MIB", "xpimInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    xpimInterfaceEntry.setStatus("current")
_XpimInterfaceIfIndex_Type = Integer32
_XpimInterfaceIfIndex_Object = MibTableColumn
xpimInterfaceIfIndex = _XpimInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 31, 1, 1, 2, 1, 1),
    _XpimInterfaceIfIndex_Type()
)
xpimInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xpimInterfaceIfIndex.setStatus("current")


class _XpimInterfaceAdminStatus_Type(Integer32):
    """Custom type xpimInterfaceAdminStatus based on Integer32"""
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


_XpimInterfaceAdminStatus_Type.__name__ = "Integer32"
_XpimInterfaceAdminStatus_Object = MibTableColumn
xpimInterfaceAdminStatus = _XpimInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 31, 1, 1, 2, 1, 2),
    _XpimInterfaceAdminStatus_Type()
)
xpimInterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpimInterfaceAdminStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-PIM-MIB",
    **{"xpimMIB": xpimMIB,
       "xpimMIBObjects": xpimMIBObjects,
       "xpim": xpim,
       "xpimVersion": xpimVersion,
       "xpimInterfaceTable": xpimInterfaceTable,
       "xpimInterfaceEntry": xpimInterfaceEntry,
       "xpimInterfaceIfIndex": xpimInterfaceIfIndex,
       "xpimInterfaceAdminStatus": xpimInterfaceAdminStatus}
)
