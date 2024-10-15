# SNMP MIB module (SALIX-DS0-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-DS0-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:22 2024
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

(dsx0ConfigEntry,) = mibBuilder.importSymbols(
    "DS0-MIB",
    "dsx0ConfigEntry")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(platform1,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "platform1")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

salixDsx0MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SalixDsx0MIBObjects_ObjectIdentity = ObjectIdentity
salixDsx0MIBObjects = _SalixDsx0MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1)
)
_SalixDsx0CrossConnectTable_Object = MibTable
salixDsx0CrossConnectTable = _SalixDsx0CrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    salixDsx0CrossConnectTable.setStatus("current")
_SalixDsx0CrossConnectEntry_Object = MibTableRow
salixDsx0CrossConnectEntry = _SalixDsx0CrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 1, 1)
)
salixDsx0CrossConnectEntry.setIndexNames(
    (0, "SALIX-DS0-MIB", "salixDsx0CrossConnectHighInterface"),
    (0, "SALIX-DS0-MIB", "salixDsx0CrossConnectLowInterface"),
)
if mibBuilder.loadTexts:
    salixDsx0CrossConnectEntry.setStatus("current")
_SalixDsx0CrossConnectHighInterface_Type = InterfaceIndex
_SalixDsx0CrossConnectHighInterface_Object = MibTableColumn
salixDsx0CrossConnectHighInterface = _SalixDsx0CrossConnectHighInterface_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 1, 1, 1),
    _SalixDsx0CrossConnectHighInterface_Type()
)
salixDsx0CrossConnectHighInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixDsx0CrossConnectHighInterface.setStatus("current")
_SalixDsx0CrossConnectLowInterface_Type = InterfaceIndex
_SalixDsx0CrossConnectLowInterface_Object = MibTableColumn
salixDsx0CrossConnectLowInterface = _SalixDsx0CrossConnectLowInterface_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 1, 1, 2),
    _SalixDsx0CrossConnectLowInterface_Type()
)
salixDsx0CrossConnectLowInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixDsx0CrossConnectLowInterface.setStatus("current")


class _SalixDsx0CrossConnectDirection_Type(Integer32):
    """Custom type salixDsx0CrossConnectDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("high2low", 1),
          ("low2high", 2))
    )


_SalixDsx0CrossConnectDirection_Type.__name__ = "Integer32"
_SalixDsx0CrossConnectDirection_Object = MibTableColumn
salixDsx0CrossConnectDirection = _SalixDsx0CrossConnectDirection_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 1, 1, 3),
    _SalixDsx0CrossConnectDirection_Type()
)
salixDsx0CrossConnectDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixDsx0CrossConnectDirection.setStatus("current")


class _SalixDsx0CrossConnectOperStatus_Type(Integer32):
    """Custom type salixDsx0CrossConnectOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_SalixDsx0CrossConnectOperStatus_Type.__name__ = "Integer32"
_SalixDsx0CrossConnectOperStatus_Object = MibTableColumn
salixDsx0CrossConnectOperStatus = _SalixDsx0CrossConnectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 1, 1, 4),
    _SalixDsx0CrossConnectOperStatus_Type()
)
salixDsx0CrossConnectOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixDsx0CrossConnectOperStatus.setStatus("current")
_SalixDsx0CrossConnectStartTime_Type = TimeStamp
_SalixDsx0CrossConnectStartTime_Object = MibTableColumn
salixDsx0CrossConnectStartTime = _SalixDsx0CrossConnectStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 1, 1, 5),
    _SalixDsx0CrossConnectStartTime_Type()
)
salixDsx0CrossConnectStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixDsx0CrossConnectStartTime.setStatus("current")
_SalixDsx0CrossConnectRowStatus_Type = RowStatus
_SalixDsx0CrossConnectRowStatus_Object = MibTableColumn
salixDsx0CrossConnectRowStatus = _SalixDsx0CrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 1, 1, 6),
    _SalixDsx0CrossConnectRowStatus_Type()
)
salixDsx0CrossConnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixDsx0CrossConnectRowStatus.setStatus("current")
_SalixDsx0ConfigTable_Object = MibTable
salixDsx0ConfigTable = _SalixDsx0ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    salixDsx0ConfigTable.setStatus("current")
_SalixDsx0ConfigEntry_Object = MibTableRow
salixDsx0ConfigEntry = _SalixDsx0ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    salixDsx0ConfigEntry.setStatus("current")


class _SalixDsx0Status_Type(Integer32):
    """Custom type salixDsx0Status based on Integer32"""
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
        *(("crossconnect", 2),
          ("loopback", 4),
          ("notused", 1),
          ("rtpconnect", 3),
          ("test", 5),
          ("unknown", 6))
    )


_SalixDsx0Status_Type.__name__ = "Integer32"
_SalixDsx0Status_Object = MibTableColumn
salixDsx0Status = _SalixDsx0Status_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 1, 2, 1, 1),
    _SalixDsx0Status_Type()
)
salixDsx0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixDsx0Status.setStatus("current")
_SalixDsx0MIBTraps_ObjectIdentity = ObjectIdentity
salixDsx0MIBTraps = _SalixDsx0MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 2)
)
_SalixDsx0MIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixDsx0MIBTrapPrefix = _SalixDsx0MIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 2, 0)
)
_SalixDsx0MIBCompliance_ObjectIdentity = ObjectIdentity
salixDsx0MIBCompliance = _SalixDsx0MIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 3)
)
_SalixDsx0Groups_ObjectIdentity = ObjectIdentity
salixDsx0Groups = _SalixDsx0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 3, 1)
)
_SalixDsx0Compliances_ObjectIdentity = ObjectIdentity
salixDsx0Compliances = _SalixDsx0Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 3, 2)
)
dsx0ConfigEntry.registerAugmentions(
    ("SALIX-DS0-MIB",
     "salixDsx0ConfigEntry")
)
salixDsx0ConfigEntry.setIndexNames(*dsx0ConfigEntry.getIndexNames())

# Managed Objects groups

salixDsx0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 3, 1, 1)
)
salixDsx0Group.setObjects(
      *(("SALIX-DS0-MIB", "salixDsx0CrossConnectDirection"),
        ("SALIX-DS0-MIB", "salixDsx0CrossConnectOperStatus"),
        ("SALIX-DS0-MIB", "salixDsx0CrossConnectStartTime"),
        ("SALIX-DS0-MIB", "salixDsx0CrossConnectRowStatus"),
        ("SALIX-DS0-MIB", "salixDsx0Status"))
)
if mibBuilder.loadTexts:
    salixDsx0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

salixDsx0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    salixDsx0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-DS0-MIB",
    **{"salixDsx0MIB": salixDsx0MIB,
       "salixDsx0MIBObjects": salixDsx0MIBObjects,
       "salixDsx0CrossConnectTable": salixDsx0CrossConnectTable,
       "salixDsx0CrossConnectEntry": salixDsx0CrossConnectEntry,
       "salixDsx0CrossConnectHighInterface": salixDsx0CrossConnectHighInterface,
       "salixDsx0CrossConnectLowInterface": salixDsx0CrossConnectLowInterface,
       "salixDsx0CrossConnectDirection": salixDsx0CrossConnectDirection,
       "salixDsx0CrossConnectOperStatus": salixDsx0CrossConnectOperStatus,
       "salixDsx0CrossConnectStartTime": salixDsx0CrossConnectStartTime,
       "salixDsx0CrossConnectRowStatus": salixDsx0CrossConnectRowStatus,
       "salixDsx0ConfigTable": salixDsx0ConfigTable,
       "salixDsx0ConfigEntry": salixDsx0ConfigEntry,
       "salixDsx0Status": salixDsx0Status,
       "salixDsx0MIBTraps": salixDsx0MIBTraps,
       "salixDsx0MIBTrapPrefix": salixDsx0MIBTrapPrefix,
       "salixDsx0MIBCompliance": salixDsx0MIBCompliance,
       "salixDsx0Groups": salixDsx0Groups,
       "salixDsx0Group": salixDsx0Group,
       "salixDsx0Compliances": salixDsx0Compliances,
       "salixDsx0Compliance": salixDsx0Compliance}
)
