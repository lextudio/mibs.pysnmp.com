# SNMP MIB module (XYLAN-SRTB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-SRTB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:16 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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

(xylanSrtbArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanSrtbArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanSRTB_ObjectIdentity = ObjectIdentity
xylanSRTB = _XylanSRTB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1)
)
_SrtbConfigTable_Object = MibTable
srtbConfigTable = _SrtbConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    srtbConfigTable.setStatus("mandatory")
_SrtbConfigEntry_Object = MibTableRow
srtbConfigEntry = _SrtbConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1, 1)
)
srtbConfigEntry.setIndexNames(
    (0, "XYLAN-SRTB-MIB", "srtbGroupID"),
)
if mibBuilder.loadTexts:
    srtbConfigEntry.setStatus("mandatory")


class _SrtbGroupID_Type(Integer32):
    """Custom type srtbGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SrtbGroupID_Type.__name__ = "Integer32"
_SrtbGroupID_Object = MibTableColumn
srtbGroupID = _SrtbGroupID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1, 1, 1),
    _SrtbGroupID_Type()
)
srtbGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtbGroupID.setStatus("mandatory")


class _SrtbOperStatus_Type(Integer32):
    """Custom type srtbOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SrtbOperStatus_Type.__name__ = "Integer32"
_SrtbOperStatus_Object = MibTableColumn
srtbOperStatus = _SrtbOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1, 1, 2),
    _SrtbOperStatus_Type()
)
srtbOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtbOperStatus.setStatus("mandatory")


class _SrtbEthernetRingId_Type(Integer32):
    """Custom type srtbEthernetRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SrtbEthernetRingId_Type.__name__ = "Integer32"
_SrtbEthernetRingId_Object = MibTableColumn
srtbEthernetRingId = _SrtbEthernetRingId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1, 1, 3),
    _SrtbEthernetRingId_Type()
)
srtbEthernetRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtbEthernetRingId.setStatus("mandatory")


class _SrtbExplorerTypeToSend_Type(Integer32):
    """Custom type srtbExplorerTypeToSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 3),
          ("typeARE", 1),
          ("typeSTE", 2))
    )


_SrtbExplorerTypeToSend_Type.__name__ = "Integer32"
_SrtbExplorerTypeToSend_Object = MibTableColumn
srtbExplorerTypeToSend = _SrtbExplorerTypeToSend_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1, 1, 4),
    _SrtbExplorerTypeToSend_Type()
)
srtbExplorerTypeToSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtbExplorerTypeToSend.setStatus("mandatory")
_SrtbRIFTable_Object = MibTable
srtbRIFTable = _SrtbRIFTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2)
)
if mibBuilder.loadTexts:
    srtbRIFTable.setStatus("mandatory")
_SrtbRIFEntry_Object = MibTableRow
srtbRIFEntry = _SrtbRIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2, 1)
)
srtbRIFEntry.setIndexNames(
    (0, "XYLAN-SRTB-MIB", "srtbRIFMac"),
    (0, "XYLAN-SRTB-MIB", "srtbRIFGroupID"),
)
if mibBuilder.loadTexts:
    srtbRIFEntry.setStatus("mandatory")
_SrtbRIFMac_Type = MacAddress
_SrtbRIFMac_Object = MibTableColumn
srtbRIFMac = _SrtbRIFMac_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2, 1, 1),
    _SrtbRIFMac_Type()
)
srtbRIFMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtbRIFMac.setStatus("mandatory")


class _SrtbRIFGroupID_Type(Integer32):
    """Custom type srtbRIFGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SrtbRIFGroupID_Type.__name__ = "Integer32"
_SrtbRIFGroupID_Object = MibTableColumn
srtbRIFGroupID = _SrtbRIFGroupID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2, 1, 2),
    _SrtbRIFGroupID_Type()
)
srtbRIFGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtbRIFGroupID.setStatus("mandatory")
_SrtbRIFString_Type = OctetString
_SrtbRIFString_Object = MibTableColumn
srtbRIFString = _SrtbRIFString_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2, 1, 3),
    _SrtbRIFString_Type()
)
srtbRIFString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtbRIFString.setStatus("mandatory")


class _SrtbRIFPurge_Type(Integer32):
    """Custom type srtbRIFPurge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("purgeRif", 2))
    )


_SrtbRIFPurge_Type.__name__ = "Integer32"
_SrtbRIFPurge_Object = MibTableColumn
srtbRIFPurge = _SrtbRIFPurge_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2, 1, 4),
    _SrtbRIFPurge_Type()
)
srtbRIFPurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtbRIFPurge.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-SRTB-MIB",
    **{"xylanSRTB": xylanSRTB,
       "srtbConfigTable": srtbConfigTable,
       "srtbConfigEntry": srtbConfigEntry,
       "srtbGroupID": srtbGroupID,
       "srtbOperStatus": srtbOperStatus,
       "srtbEthernetRingId": srtbEthernetRingId,
       "srtbExplorerTypeToSend": srtbExplorerTypeToSend,
       "srtbRIFTable": srtbRIFTable,
       "srtbRIFEntry": srtbRIFEntry,
       "srtbRIFMac": srtbRIFMac,
       "srtbRIFGroupID": srtbRIFGroupID,
       "srtbRIFString": srtbRIFString,
       "srtbRIFPurge": srtbRIFPurge}
)
