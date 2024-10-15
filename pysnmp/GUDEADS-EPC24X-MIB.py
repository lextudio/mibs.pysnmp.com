# SNMP MIB module (GUDEADS-EPC24X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GUDEADS-EPC24X-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:18 2024
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

gudeads = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28507)
)
gudeads.setRevisions(
        ("2007-03-05 13:56",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsEPC24_ObjectIdentity = ObjectIdentity
gadsEPC24 = _GadsEPC24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 5)
)
_Epc24Objects_ObjectIdentity = ObjectIdentity
epc24Objects = _Epc24Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1)
)
_Epc24powerports_ObjectIdentity = ObjectIdentity
epc24powerports = _Epc24powerports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1)
)


class _Epc24portNumber_Type(Integer32):
    """Custom type epc24portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Epc24portNumber_Type.__name__ = "Integer32"
_Epc24portNumber_Object = MibScalar
epc24portNumber = _Epc24portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1, 1),
    _Epc24portNumber_Type()
)
epc24portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc24portNumber.setStatus("current")
_Epc24portTable_Object = MibTable
epc24portTable = _Epc24portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    epc24portTable.setStatus("current")
_Epc24portEntry_Object = MibTableRow
epc24portEntry = _Epc24portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1, 2, 1)
)
epc24portEntry.setIndexNames(
    (0, "GUDEADS-EPC24X-MIB", "epc24PortIndex"),
)
if mibBuilder.loadTexts:
    epc24portEntry.setStatus("current")


class _Epc24PortIndex_Type(Integer32):
    """Custom type epc24PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Epc24PortIndex_Type.__name__ = "Integer32"
_Epc24PortIndex_Object = MibTableColumn
epc24PortIndex = _Epc24PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1, 2, 1, 1),
    _Epc24PortIndex_Type()
)
epc24PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    epc24PortIndex.setStatus("current")


class _Epc24PortName_Type(OctetString):
    """Custom type epc24PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Epc24PortName_Type.__name__ = "OctetString"
_Epc24PortName_Object = MibTableColumn
epc24PortName = _Epc24PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1, 2, 1, 2),
    _Epc24PortName_Type()
)
epc24PortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc24PortName.setStatus("current")


class _Epc24PortState_Type(Integer32):
    """Custom type epc24PortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Epc24PortState_Type.__name__ = "Integer32"
_Epc24PortState_Object = MibTableColumn
epc24PortState = _Epc24PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1, 2, 1, 3),
    _Epc24PortState_Type()
)
epc24PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc24PortState.setStatus("current")
_Epc24PortSwitchCount_Type = Counter32
_Epc24PortSwitchCount_Object = MibTableColumn
epc24PortSwitchCount = _Epc24PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1, 2, 1, 4),
    _Epc24PortSwitchCount_Type()
)
epc24PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc24PortSwitchCount.setStatus("current")


class _Epc24Fuse1_Type(Integer32):
    """Custom type epc24Fuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc24Fuse1_Type.__name__ = "Integer32"
_Epc24Fuse1_Object = MibScalar
epc24Fuse1 = _Epc24Fuse1_Object(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1, 3),
    _Epc24Fuse1_Type()
)
epc24Fuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc24Fuse1.setStatus("current")


class _Epc24Fuse2_Type(Integer32):
    """Custom type epc24Fuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc24Fuse2_Type.__name__ = "Integer32"
_Epc24Fuse2_Object = MibScalar
epc24Fuse2 = _Epc24Fuse2_Object(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1, 4),
    _Epc24Fuse2_Type()
)
epc24Fuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc24Fuse2.setStatus("current")


class _Epc24Fuse3_Type(Integer32):
    """Custom type epc24Fuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc24Fuse3_Type.__name__ = "Integer32"
_Epc24Fuse3_Object = MibScalar
epc24Fuse3 = _Epc24Fuse3_Object(
    (1, 3, 6, 1, 4, 1, 28507, 5, 1, 1, 5),
    _Epc24Fuse3_Type()
)
epc24Fuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc24Fuse3.setStatus("current")
_Epc24Events_ObjectIdentity = ObjectIdentity
epc24Events = _Epc24Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 5, 2)
)
_Epc24Conf_ObjectIdentity = ObjectIdentity
epc24Conf = _Epc24Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 5, 3)
)
_Epc24Groups_ObjectIdentity = ObjectIdentity
epc24Groups = _Epc24Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 5, 3, 1)
)
_Epc24Compls_ObjectIdentity = ObjectIdentity
epc24Compls = _Epc24Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 5, 3, 2)
)

# Managed Objects groups

epc24BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 5, 3, 1, 1)
)
epc24BasicGroup.setObjects(
      *(("GUDEADS-EPC24X-MIB", "epc24portNumber"),
        ("GUDEADS-EPC24X-MIB", "epc24PortName"),
        ("GUDEADS-EPC24X-MIB", "epc24PortState"),
        ("GUDEADS-EPC24X-MIB", "epc24PortSwitchCount"),
        ("GUDEADS-EPC24X-MIB", "epc24Fuse1"),
        ("GUDEADS-EPC24X-MIB", "epc24Fuse2"),
        ("GUDEADS-EPC24X-MIB", "epc24Fuse3"))
)
if mibBuilder.loadTexts:
    epc24BasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EPC24X-MIB",
    **{"gudeads": gudeads,
       "gadsEPC24": gadsEPC24,
       "epc24Objects": epc24Objects,
       "epc24powerports": epc24powerports,
       "epc24portNumber": epc24portNumber,
       "epc24portTable": epc24portTable,
       "epc24portEntry": epc24portEntry,
       "epc24PortIndex": epc24PortIndex,
       "epc24PortName": epc24PortName,
       "epc24PortState": epc24PortState,
       "epc24PortSwitchCount": epc24PortSwitchCount,
       "epc24Fuse1": epc24Fuse1,
       "epc24Fuse2": epc24Fuse2,
       "epc24Fuse3": epc24Fuse3,
       "epc24Events": epc24Events,
       "epc24Conf": epc24Conf,
       "epc24Groups": epc24Groups,
       "epc24BasicGroup": epc24BasicGroup,
       "epc24Compls": epc24Compls}
)
