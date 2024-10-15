# SNMP MIB module (SAMSUNG-CLONING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAMSUNG-CLONING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:37 2024
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

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

(samsungCommonMIB,) = mibBuilder.importSymbols(
    "SAMSUNG-COMMON-MIB",
    "samsungCommonMIB")

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

scmCloningMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ScmCloning_ObjectIdentity = ObjectIdentity
scmCloning = _ScmCloning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1)
)
_ScmCloningTable_Object = MibTable
scmCloningTable = _ScmCloningTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1)
)
if mibBuilder.loadTexts:
    scmCloningTable.setStatus("current")
_ScmCloningEntry_Object = MibTableRow
scmCloningEntry = _ScmCloningEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1)
)
scmCloningEntry.setIndexNames(
    (0, "SAMSUNG-CLONING-MIB", "scmCloningIndex"),
)
if mibBuilder.loadTexts:
    scmCloningEntry.setStatus("current")
_ScmCloningIndex_Type = Integer32
_ScmCloningIndex_Object = MibTableColumn
scmCloningIndex = _ScmCloningIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 1),
    _ScmCloningIndex_Type()
)
scmCloningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmCloningIndex.setStatus("current")
_ScmCloningIPAddress_Type = IpAddress
_ScmCloningIPAddress_Object = MibTableColumn
scmCloningIPAddress = _ScmCloningIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 2),
    _ScmCloningIPAddress_Type()
)
scmCloningIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmCloningIPAddress.setStatus("current")


class _ScmCloningResult_Type(Integer32):
    """Custom type scmCloningResult based on Integer32"""
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
        *(("busy", 6),
          ("completed", 1),
          ("invalidFile", 3),
          ("notSupportedCloning", 5),
          ("processing", 2),
          ("versionMismatch", 4))
    )


_ScmCloningResult_Type.__name__ = "Integer32"
_ScmCloningResult_Object = MibTableColumn
scmCloningResult = _ScmCloningResult_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 3),
    _ScmCloningResult_Type()
)
scmCloningResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmCloningResult.setStatus("current")
_ScmCloningDate_Type = OctetString
_ScmCloningDate_Object = MibTableColumn
scmCloningDate = _ScmCloningDate_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 4),
    _ScmCloningDate_Type()
)
scmCloningDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmCloningDate.setStatus("current")
_ScmCloningSimple_ObjectIdentity = ObjectIdentity
scmCloningSimple = _ScmCloningSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2)
)
_ScmCloningLastIPAddress_Type = IpAddress
_ScmCloningLastIPAddress_Object = MibScalar
scmCloningLastIPAddress = _ScmCloningLastIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 1),
    _ScmCloningLastIPAddress_Type()
)
scmCloningLastIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmCloningLastIPAddress.setStatus("current")


class _ScmCloningLastResult_Type(Integer32):
    """Custom type scmCloningLastResult based on Integer32"""
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
        *(("busy", 6),
          ("completed", 1),
          ("invalidFile", 3),
          ("notSupportedCloning", 5),
          ("processing", 2),
          ("versionMismatch", 4))
    )


_ScmCloningLastResult_Type.__name__ = "Integer32"
_ScmCloningLastResult_Object = MibScalar
scmCloningLastResult = _ScmCloningLastResult_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 2),
    _ScmCloningLastResult_Type()
)
scmCloningLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmCloningLastResult.setStatus("current")
_ScmCloningLastDate_Type = OctetString
_ScmCloningLastDate_Object = MibScalar
scmCloningLastDate = _ScmCloningLastDate_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 3),
    _ScmCloningLastDate_Type()
)
scmCloningLastDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmCloningLastDate.setStatus("current")


class _ScmCloningSupported_Type(Integer32):
    """Custom type scmCloningSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_ScmCloningSupported_Type.__name__ = "Integer32"
_ScmCloningSupported_Object = MibScalar
scmCloningSupported = _ScmCloningSupported_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 4),
    _ScmCloningSupported_Type()
)
scmCloningSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmCloningSupported.setStatus("current")
_ScmCloningTrap_ObjectIdentity = ObjectIdentity
scmCloningTrap = _ScmCloningTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 3)
)
if mibBuilder.loadTexts:
    scmCloningTrap.setStatus("current")
_ScmCloningTrapSimple_ObjectIdentity = ObjectIdentity
scmCloningTrapSimple = _ScmCloningTrapSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 3, 1)
)

# Managed Objects groups


# Notification objects

scmCloningTrapResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 3, 1, 1)
)
scmCloningTrapResult.setObjects(
      *(("SAMSUNG-CLONING-MIB", "scmCloningLastIPAddress"),
        ("SAMSUNG-CLONING-MIB", "scmCloningLastResult"))
)
if mibBuilder.loadTexts:
    scmCloningTrapResult.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAMSUNG-CLONING-MIB",
    **{"scmCloningMIB": scmCloningMIB,
       "scmCloning": scmCloning,
       "scmCloningTable": scmCloningTable,
       "scmCloningEntry": scmCloningEntry,
       "scmCloningIndex": scmCloningIndex,
       "scmCloningIPAddress": scmCloningIPAddress,
       "scmCloningResult": scmCloningResult,
       "scmCloningDate": scmCloningDate,
       "scmCloningSimple": scmCloningSimple,
       "scmCloningLastIPAddress": scmCloningLastIPAddress,
       "scmCloningLastResult": scmCloningLastResult,
       "scmCloningLastDate": scmCloningLastDate,
       "scmCloningSupported": scmCloningSupported,
       "scmCloningTrap": scmCloningTrap,
       "scmCloningTrapSimple": scmCloningTrapSimple,
       "scmCloningTrapResult": scmCloningTrapResult}
)
