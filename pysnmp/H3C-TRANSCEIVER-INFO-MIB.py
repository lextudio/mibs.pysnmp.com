# SNMP MIB module (H3C-TRANSCEIVER-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-TRANSCEIVER-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:33 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
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

h3cTransceiver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cTransceiverInfoAdm_ObjectIdentity = ObjectIdentity
h3cTransceiverInfoAdm = _H3cTransceiverInfoAdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1)
)
_H3cTransceiverInfoTable_Object = MibTable
h3cTransceiverInfoTable = _H3cTransceiverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1)
)
if mibBuilder.loadTexts:
    h3cTransceiverInfoTable.setStatus("current")
_H3cTransceiverInfoEntry_Object = MibTableRow
h3cTransceiverInfoEntry = _H3cTransceiverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1)
)
h3cTransceiverInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cTransceiverInfoEntry.setStatus("current")
_H3cTransceiverHardwareType_Type = OctetString
_H3cTransceiverHardwareType_Object = MibTableColumn
h3cTransceiverHardwareType = _H3cTransceiverHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 1),
    _H3cTransceiverHardwareType_Type()
)
h3cTransceiverHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTransceiverHardwareType.setStatus("current")
_H3cTransceiverType_Type = OctetString
_H3cTransceiverType_Object = MibTableColumn
h3cTransceiverType = _H3cTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 2),
    _H3cTransceiverType_Type()
)
h3cTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTransceiverType.setStatus("current")
_H3cTransceiverWaveLength_Type = Integer32
_H3cTransceiverWaveLength_Object = MibTableColumn
h3cTransceiverWaveLength = _H3cTransceiverWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 3),
    _H3cTransceiverWaveLength_Type()
)
h3cTransceiverWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTransceiverWaveLength.setStatus("current")
_H3cTransceiverVendorName_Type = OctetString
_H3cTransceiverVendorName_Object = MibTableColumn
h3cTransceiverVendorName = _H3cTransceiverVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 4),
    _H3cTransceiverVendorName_Type()
)
h3cTransceiverVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTransceiverVendorName.setStatus("current")
_H3cTransceiverSerialNumber_Type = OctetString
_H3cTransceiverSerialNumber_Object = MibTableColumn
h3cTransceiverSerialNumber = _H3cTransceiverSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 5),
    _H3cTransceiverSerialNumber_Type()
)
h3cTransceiverSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTransceiverSerialNumber.setStatus("current")


class _H3cTransceiverFiberDiameterType_Type(Integer32):
    """Custom type h3cTransceiverFiberDiameterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("copper", 4),
          ("fiber50", 2),
          ("fiber625", 3),
          ("fiber9", 1))
    )


_H3cTransceiverFiberDiameterType_Type.__name__ = "Integer32"
_H3cTransceiverFiberDiameterType_Object = MibTableColumn
h3cTransceiverFiberDiameterType = _H3cTransceiverFiberDiameterType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 6),
    _H3cTransceiverFiberDiameterType_Type()
)
h3cTransceiverFiberDiameterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTransceiverFiberDiameterType.setStatus("current")
_H3cTransceiverTransferDistance_Type = Integer32
_H3cTransceiverTransferDistance_Object = MibTableColumn
h3cTransceiverTransferDistance = _H3cTransceiverTransferDistance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 7),
    _H3cTransceiverTransferDistance_Type()
)
h3cTransceiverTransferDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTransceiverTransferDistance.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-TRANSCEIVER-INFO-MIB",
    **{"h3cTransceiver": h3cTransceiver,
       "h3cTransceiverInfoAdm": h3cTransceiverInfoAdm,
       "h3cTransceiverInfoTable": h3cTransceiverInfoTable,
       "h3cTransceiverInfoEntry": h3cTransceiverInfoEntry,
       "h3cTransceiverHardwareType": h3cTransceiverHardwareType,
       "h3cTransceiverType": h3cTransceiverType,
       "h3cTransceiverWaveLength": h3cTransceiverWaveLength,
       "h3cTransceiverVendorName": h3cTransceiverVendorName,
       "h3cTransceiverSerialNumber": h3cTransceiverSerialNumber,
       "h3cTransceiverFiberDiameterType": h3cTransceiverFiberDiameterType,
       "h3cTransceiverTransferDistance": h3cTransceiverTransferDistance}
)
