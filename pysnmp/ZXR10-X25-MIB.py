# SNMP MIB module (ZXR10-X25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-X25-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:13 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10X25_ObjectIdentity = ObjectIdentity
zxr10X25 = _Zxr10X25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4000)
)
_Zxr10X25OprTable_Object = MibTable
zxr10X25OprTable = _Zxr10X25OprTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1)
)
if mibBuilder.loadTexts:
    zxr10X25OprTable.setStatus("current")
_Zxr10X25OprEntry_Object = MibTableRow
zxr10X25OprEntry = _Zxr10X25OprEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1)
)
zxr10X25OprEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxr10X25OprEntry.setStatus("current")


class _Zxr10X25OprXconnenctIfName_Type(DisplayString):
    """Custom type zxr10X25OprXconnenctIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10X25OprXconnenctIfName_Type.__name__ = "DisplayString"
_Zxr10X25OprXconnenctIfName_Object = MibTableColumn
zxr10X25OprXconnenctIfName = _Zxr10X25OprXconnenctIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 1),
    _Zxr10X25OprXconnenctIfName_Type()
)
zxr10X25OprXconnenctIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10X25OprXconnenctIfName.setStatus("current")


class _Zxr10X25OprLocalswitchIfName_Type(DisplayString):
    """Custom type zxr10X25OprLocalswitchIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10X25OprLocalswitchIfName_Type.__name__ = "DisplayString"
_Zxr10X25OprLocalswitchIfName_Object = MibTableColumn
zxr10X25OprLocalswitchIfName = _Zxr10X25OprLocalswitchIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 2),
    _Zxr10X25OprLocalswitchIfName_Type()
)
zxr10X25OprLocalswitchIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10X25OprLocalswitchIfName.setStatus("current")
_Zxr10X25OprDLCI_Type = Integer32
_Zxr10X25OprDLCI_Object = MibTableColumn
zxr10X25OprDLCI = _Zxr10X25OprDLCI_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 3),
    _Zxr10X25OprDLCI_Type()
)
zxr10X25OprDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10X25OprDLCI.setStatus("current")


class _Zxr10X25OprType_Type(Integer32):
    """Custom type zxr10X25OprType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("localswitch", 1),
          ("xconnect", 2))
    )


_Zxr10X25OprType_Type.__name__ = "Integer32"
_Zxr10X25OprType_Object = MibTableColumn
zxr10X25OprType = _Zxr10X25OprType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 4),
    _Zxr10X25OprType_Type()
)
zxr10X25OprType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10X25OprType.setStatus("current")
_Zxr10X25OprStatus_Type = RowStatus
_Zxr10X25OprStatus_Object = MibTableColumn
zxr10X25OprStatus = _Zxr10X25OprStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 5),
    _Zxr10X25OprStatus_Type()
)
zxr10X25OprStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10X25OprStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-X25-MIB",
    **{"DisplayString": DisplayString,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10X25": zxr10X25,
       "zxr10X25OprTable": zxr10X25OprTable,
       "zxr10X25OprEntry": zxr10X25OprEntry,
       "zxr10X25OprXconnenctIfName": zxr10X25OprXconnenctIfName,
       "zxr10X25OprLocalswitchIfName": zxr10X25OprLocalswitchIfName,
       "zxr10X25OprDLCI": zxr10X25OprDLCI,
       "zxr10X25OprType": zxr10X25OprType,
       "zxr10X25OprStatus": zxr10X25OprStatus}
)
