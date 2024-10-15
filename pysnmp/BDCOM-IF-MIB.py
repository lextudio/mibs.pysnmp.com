# SNMP MIB module (BDCOM-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:33 2024
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

(bdMgmt,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdMgmt")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

bdIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BdIfObjects_ObjectIdentity = ObjectIdentity
bdIfObjects = _BdIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1)
)
_VifTable_Object = MibTable
vifTable = _VifTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1)
)
if mibBuilder.loadTexts:
    vifTable.setStatus("mandatory")
_VifEntry_Object = MibTableRow
vifEntry = _VifEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1)
)
vifEntry.setIndexNames(
    (0, "BDCOM-IF-MIB", "vifIndex"),
)
if mibBuilder.loadTexts:
    vifEntry.setStatus("mandatory")
_VifIndex_Type = Integer32
_VifIndex_Object = MibTableColumn
vifIndex = _VifIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 1),
    _VifIndex_Type()
)
vifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifIndex.setStatus("mandatory")


class _VifDescr_Type(DisplayString):
    """Custom type vifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VifDescr_Type.__name__ = "DisplayString"
_VifDescr_Object = MibTableColumn
vifDescr = _VifDescr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 2),
    _VifDescr_Type()
)
vifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifDescr.setStatus("mandatory")


class _VifType_Type(Integer32):
    """Custom type vifType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("voiceEM", 100),
          ("voiceFXO", 101),
          ("voiceFXS", 102))
    )


_VifType_Type.__name__ = "Integer32"
_VifType_Object = MibTableColumn
vifType = _VifType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 3),
    _VifType_Type()
)
vifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifType.setStatus("mandatory")
_VifMtu_Type = Integer32
_VifMtu_Object = MibTableColumn
vifMtu = _VifMtu_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 4),
    _VifMtu_Type()
)
vifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifMtu.setStatus("mandatory")
_VifSpeed_Type = Gauge32
_VifSpeed_Object = MibTableColumn
vifSpeed = _VifSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 5),
    _VifSpeed_Type()
)
vifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifSpeed.setStatus("mandatory")
_VifPhysAddress_Type = PhysAddress
_VifPhysAddress_Object = MibTableColumn
vifPhysAddress = _VifPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 6),
    _VifPhysAddress_Type()
)
vifPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifPhysAddress.setStatus("mandatory")


class _VifAdminStatus_Type(Integer32):
    """Custom type vifAdminStatus based on Integer32"""
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
          ("testing", 3),
          ("up", 1))
    )


_VifAdminStatus_Type.__name__ = "Integer32"
_VifAdminStatus_Object = MibTableColumn
vifAdminStatus = _VifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 7),
    _VifAdminStatus_Type()
)
vifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vifAdminStatus.setStatus("mandatory")


class _VifOperStatus_Type(Integer32):
    """Custom type vifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_VifOperStatus_Type.__name__ = "Integer32"
_VifOperStatus_Object = MibTableColumn
vifOperStatus = _VifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 8),
    _VifOperStatus_Type()
)
vifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifOperStatus.setStatus("mandatory")
_VifLastChange_Type = TimeTicks
_VifLastChange_Object = MibTableColumn
vifLastChange = _VifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 9),
    _VifLastChange_Type()
)
vifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLastChange.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-IF-MIB",
    **{"bdIfMIB": bdIfMIB,
       "bdIfObjects": bdIfObjects,
       "vifTable": vifTable,
       "vifEntry": vifEntry,
       "vifIndex": vifIndex,
       "vifDescr": vifDescr,
       "vifType": vifType,
       "vifMtu": vifMtu,
       "vifSpeed": vifSpeed,
       "vifPhysAddress": vifPhysAddress,
       "vifAdminStatus": vifAdminStatus,
       "vifOperStatus": vifOperStatus,
       "vifLastChange": vifLastChange}
)
