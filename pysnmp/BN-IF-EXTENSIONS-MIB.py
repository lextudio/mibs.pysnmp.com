# SNMP MIB module (BN-IF-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BN-IF-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:28 2024
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

(s5IfExt,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5IfExt")

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

bnIfExtensionsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 2)
)
bnIfExtensionsMib.setRevisions(
        ("2013-07-26 00:00",
         "2011-10-05 00:00",
         "2011-09-16 00:00",
         "2004-07-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BnIfExtensions_ObjectIdentity = ObjectIdentity
bnIfExtensions = _BnIfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1)
)
_BnIfExtnTable_Object = MibTable
bnIfExtnTable = _BnIfExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1)
)
if mibBuilder.loadTexts:
    bnIfExtnTable.setStatus("current")
_BnIfExtnEntry_Object = MibTableRow
bnIfExtnEntry = _BnIfExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1)
)
bnIfExtnEntry.setIndexNames(
    (0, "BN-IF-EXTENSIONS-MIB", "bnIfExtnIndex"),
)
if mibBuilder.loadTexts:
    bnIfExtnEntry.setStatus("current")
_BnIfExtnIndex_Type = Integer32
_BnIfExtnIndex_Object = MibTableColumn
bnIfExtnIndex = _BnIfExtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 1),
    _BnIfExtnIndex_Type()
)
bnIfExtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnIfExtnIndex.setStatus("current")
_BnIfExtnSlot_Type = Integer32
_BnIfExtnSlot_Object = MibTableColumn
bnIfExtnSlot = _BnIfExtnSlot_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 2),
    _BnIfExtnSlot_Type()
)
bnIfExtnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnIfExtnSlot.setStatus("current")
_BnIfExtnPort_Type = Integer32
_BnIfExtnPort_Object = MibTableColumn
bnIfExtnPort = _BnIfExtnPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 3),
    _BnIfExtnPort_Type()
)
bnIfExtnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnIfExtnPort.setStatus("current")


class _BnIfExtnIsPortShared_Type(Integer32):
    """Custom type bnIfExtnIsPortShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portNotShared", 2),
          ("portShared", 1))
    )


_BnIfExtnIsPortShared_Type.__name__ = "Integer32"
_BnIfExtnIsPortShared_Object = MibTableColumn
bnIfExtnIsPortShared = _BnIfExtnIsPortShared_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 4),
    _BnIfExtnIsPortShared_Type()
)
bnIfExtnIsPortShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnIfExtnIsPortShared.setStatus("current")


class _BnIfExtnPortActiveComponent_Type(Integer32):
    """Custom type bnIfExtnPortActiveComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixedPort", 1),
          ("gbicPort", 2),
          ("mdaPort", 3))
    )


_BnIfExtnPortActiveComponent_Type.__name__ = "Integer32"
_BnIfExtnPortActiveComponent_Object = MibTableColumn
bnIfExtnPortActiveComponent = _BnIfExtnPortActiveComponent_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 5),
    _BnIfExtnPortActiveComponent_Type()
)
bnIfExtnPortActiveComponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnIfExtnPortActiveComponent.setStatus("current")


class _BnIfExtnPoweredDeviceDetectType_Type(Integer32):
    """Custom type bnIfExtnPoweredDeviceDetectType based on Integer32"""
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
        *(("compliantWith802dot3af", 1),
          ("compliantWith802dot3afAndLegacySupport", 2),
          ("compliantWith802dot3at", 3),
          ("compliantWith802dot3atAndLegacySupport", 4))
    )


_BnIfExtnPoweredDeviceDetectType_Type.__name__ = "Integer32"
_BnIfExtnPoweredDeviceDetectType_Object = MibTableColumn
bnIfExtnPoweredDeviceDetectType = _BnIfExtnPoweredDeviceDetectType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 6),
    _BnIfExtnPoweredDeviceDetectType_Type()
)
bnIfExtnPoweredDeviceDetectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnIfExtnPoweredDeviceDetectType.setStatus("current")


class _BnIfExtnAutoNegotiationExtAdv_Type(Bits):
    """Custom type bnIfExtnAutoNegotiationExtAdv based on Bits"""
    namedValues = NamedValues(
        *(("advertise10000Full", 8),
          ("advertise1000Full", 5),
          ("advertise1000Half", 4),
          ("advertise100Full", 3),
          ("advertise100Half", 2),
          ("advertise10Full", 1),
          ("advertise10Half", 0),
          ("advertise40000Full", 9),
          ("advertiseAsymmPauseFrame", 7),
          ("advertisePauseFrame", 6))
    )

_BnIfExtnAutoNegotiationExtAdv_Type.__name__ = "Bits"
_BnIfExtnAutoNegotiationExtAdv_Object = MibTableColumn
bnIfExtnAutoNegotiationExtAdv = _BnIfExtnAutoNegotiationExtAdv_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 7),
    _BnIfExtnAutoNegotiationExtAdv_Type()
)
bnIfExtnAutoNegotiationExtAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnIfExtnAutoNegotiationExtAdv.setStatus("current")


class _BnIfExtnExtHwAdvCapability_Type(Bits):
    """Custom type bnIfExtnExtHwAdvCapability based on Bits"""
    namedValues = NamedValues(
        *(("advertise10000Full", 8),
          ("advertise1000Full", 5),
          ("advertise1000Half", 4),
          ("advertise100Full", 3),
          ("advertise100Half", 2),
          ("advertise10Full", 1),
          ("advertise10Half", 0),
          ("advertise40000Full", 9),
          ("advertiseAsymmPauseFrame", 7),
          ("advertisePauseFrame", 6))
    )

_BnIfExtnExtHwAdvCapability_Type.__name__ = "Bits"
_BnIfExtnExtHwAdvCapability_Object = MibTableColumn
bnIfExtnExtHwAdvCapability = _BnIfExtnExtHwAdvCapability_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 8),
    _BnIfExtnExtHwAdvCapability_Type()
)
bnIfExtnExtHwAdvCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnIfExtnExtHwAdvCapability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BN-IF-EXTENSIONS-MIB",
    **{"bnIfExtensions": bnIfExtensions,
       "bnIfExtnTable": bnIfExtnTable,
       "bnIfExtnEntry": bnIfExtnEntry,
       "bnIfExtnIndex": bnIfExtnIndex,
       "bnIfExtnSlot": bnIfExtnSlot,
       "bnIfExtnPort": bnIfExtnPort,
       "bnIfExtnIsPortShared": bnIfExtnIsPortShared,
       "bnIfExtnPortActiveComponent": bnIfExtnPortActiveComponent,
       "bnIfExtnPoweredDeviceDetectType": bnIfExtnPoweredDeviceDetectType,
       "bnIfExtnAutoNegotiationExtAdv": bnIfExtnAutoNegotiationExtAdv,
       "bnIfExtnExtHwAdvCapability": bnIfExtnExtHwAdvCapability,
       "bnIfExtensionsMib": bnIfExtensionsMib}
)
