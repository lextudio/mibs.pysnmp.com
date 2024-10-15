# SNMP MIB module (CISCO-MGX82XX-PXM-CLOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGX82XX-PXM-CLOCK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:34 2024
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

(cardSpecific,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cardSpecific")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoMgx82xxPxmClockMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 72)
)
ciscoMgx82xxPxmClockMIB.setRevisions(
        ("2003-05-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CmpClockConnectorType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rj45Type", 1),
          ("smbType", 2))
    )



class CmpClockSourceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("pxmBottomSRMClock", 7),
          ("pxmExternalClock", 4),
          ("pxmExternalClock2", 9),
          ("pxmInbandClock1", 1),
          ("pxmInbandClock2", 5),
          ("pxmInternalOscillator", 8),
          ("pxmServiceModuleClock1", 2),
          ("pxmServiceModuleClock2", 6),
          ("pxmTopSRMClock", 3))
    )



class CmpCurrentClock(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("intOscillator", 3),
          ("primary", 1),
          ("secondary", 2))
    )



class CmpClockExistence(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clkNotPresent", 1),
          ("clkPresent", 2))
    )



class CmpClockImpedance(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ohms100", 2),
          ("ohms120", 3),
          ("ohms75", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PxmClockConfig_ObjectIdentity = ObjectIdentity
pxmClockConfig = _PxmClockConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16)
)
_PxmPrimaryMuxClockSource_Type = CmpClockSourceType
_PxmPrimaryMuxClockSource_Object = MibScalar
pxmPrimaryMuxClockSource = _PxmPrimaryMuxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 1),
    _PxmPrimaryMuxClockSource_Type()
)
pxmPrimaryMuxClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPrimaryMuxClockSource.setStatus("current")


class _PxmPrimaryInbandClockSourceLineNumber_Type(Integer32):
    """Custom type pxmPrimaryInbandClockSourceLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_PxmPrimaryInbandClockSourceLineNumber_Type.__name__ = "Integer32"
_PxmPrimaryInbandClockSourceLineNumber_Object = MibScalar
pxmPrimaryInbandClockSourceLineNumber = _PxmPrimaryInbandClockSourceLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 2),
    _PxmPrimaryInbandClockSourceLineNumber_Type()
)
pxmPrimaryInbandClockSourceLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPrimaryInbandClockSourceLineNumber.setStatus("current")


class _PxmPrimarySMClockSourceSlotNumber_Type(Integer32):
    """Custom type pxmPrimarySMClockSourceSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PxmPrimarySMClockSourceSlotNumber_Type.__name__ = "Integer32"
_PxmPrimarySMClockSourceSlotNumber_Object = MibScalar
pxmPrimarySMClockSourceSlotNumber = _PxmPrimarySMClockSourceSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 3),
    _PxmPrimarySMClockSourceSlotNumber_Type()
)
pxmPrimarySMClockSourceSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPrimarySMClockSourceSlotNumber.setStatus("current")
_PxmSecondaryMuxClockSource_Type = CmpClockSourceType
_PxmSecondaryMuxClockSource_Object = MibScalar
pxmSecondaryMuxClockSource = _PxmSecondaryMuxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 4),
    _PxmSecondaryMuxClockSource_Type()
)
pxmSecondaryMuxClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmSecondaryMuxClockSource.setStatus("current")


class _PxmSecondaryInbandClockSourceLineNumber_Type(Integer32):
    """Custom type pxmSecondaryInbandClockSourceLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_PxmSecondaryInbandClockSourceLineNumber_Type.__name__ = "Integer32"
_PxmSecondaryInbandClockSourceLineNumber_Object = MibScalar
pxmSecondaryInbandClockSourceLineNumber = _PxmSecondaryInbandClockSourceLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 5),
    _PxmSecondaryInbandClockSourceLineNumber_Type()
)
pxmSecondaryInbandClockSourceLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmSecondaryInbandClockSourceLineNumber.setStatus("current")


class _PxmSecondarySMClockSourceSlotNumber_Type(Integer32):
    """Custom type pxmSecondarySMClockSourceSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PxmSecondarySMClockSourceSlotNumber_Type.__name__ = "Integer32"
_PxmSecondarySMClockSourceSlotNumber_Object = MibScalar
pxmSecondarySMClockSourceSlotNumber = _PxmSecondarySMClockSourceSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 6),
    _PxmSecondarySMClockSourceSlotNumber_Type()
)
pxmSecondarySMClockSourceSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmSecondarySMClockSourceSlotNumber.setStatus("current")
_PxmCurrentClock_Type = CmpCurrentClock
_PxmCurrentClock_Object = MibScalar
pxmCurrentClock = _PxmCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 7),
    _PxmCurrentClock_Type()
)
pxmCurrentClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmCurrentClock.setStatus("current")
_PxmPreviousClock_Type = CmpCurrentClock
_PxmPreviousClock_Object = MibScalar
pxmPreviousClock = _PxmPreviousClock_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 8),
    _PxmPreviousClock_Type()
)
pxmPreviousClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPreviousClock.setStatus("current")
_PxmExtClockPresent_Type = CmpClockExistence
_PxmExtClockPresent_Object = MibScalar
pxmExtClockPresent = _PxmExtClockPresent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 9),
    _PxmExtClockPresent_Type()
)
pxmExtClockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmExtClockPresent.setStatus("current")
_PxmExtClkSrcImpedance_Type = CmpClockImpedance
_PxmExtClkSrcImpedance_Object = MibScalar
pxmExtClkSrcImpedance = _PxmExtClkSrcImpedance_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 10),
    _PxmExtClkSrcImpedance_Type()
)
pxmExtClkSrcImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmExtClkSrcImpedance.setStatus("current")
_PxmExtClkConnectorType_Type = CmpClockConnectorType
_PxmExtClkConnectorType_Object = MibScalar
pxmExtClkConnectorType = _PxmExtClkConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 11),
    _PxmExtClkConnectorType_Type()
)
pxmExtClkConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmExtClkConnectorType.setStatus("current")


class _PxmClkStratumLevel_Type(Integer32):
    """Custom type pxmClkStratumLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("stratumLevel1", 2),
          ("stratumLevel2", 3),
          ("stratumLevel3", 5),
          ("stratumLevel3E", 4),
          ("stratumLevel4", 6),
          ("stratumLevel4E", 7),
          ("stratumUnknown", 1))
    )


_PxmClkStratumLevel_Type.__name__ = "Integer32"
_PxmClkStratumLevel_Object = MibScalar
pxmClkStratumLevel = _PxmClkStratumLevel_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 12),
    _PxmClkStratumLevel_Type()
)
pxmClkStratumLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmClkStratumLevel.setStatus("current")


class _PxmClkErrReason_Type(Integer32):
    """Custom type pxmClkErrReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("excessiveJitter", 6),
          ("freqTooHigh", 4),
          ("freqTooLow", 5),
          ("goodClk", 1),
          ("missingCard", 7),
          ("missingLogicalIf", 8),
          ("noClkSignal", 3),
          ("noClock", 9),
          ("unknownReason", 2))
    )


_PxmClkErrReason_Type.__name__ = "Integer32"
_PxmClkErrReason_Object = MibScalar
pxmClkErrReason = _PxmClkErrReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 13),
    _PxmClkErrReason_Type()
)
pxmClkErrReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmClkErrReason.setStatus("current")
_PxmExtClock2Present_Type = CmpClockExistence
_PxmExtClock2Present_Object = MibScalar
pxmExtClock2Present = _PxmExtClock2Present_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 14),
    _PxmExtClock2Present_Type()
)
pxmExtClock2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmExtClock2Present.setStatus("current")
_PxmExtClk2SrcImpedance_Type = CmpClockImpedance
_PxmExtClk2SrcImpedance_Object = MibScalar
pxmExtClk2SrcImpedance = _PxmExtClk2SrcImpedance_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 15),
    _PxmExtClk2SrcImpedance_Type()
)
pxmExtClk2SrcImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmExtClk2SrcImpedance.setStatus("current")
_PxmExtClk2ConnectorType_Type = CmpClockConnectorType
_PxmExtClk2ConnectorType_Object = MibScalar
pxmExtClk2ConnectorType = _PxmExtClk2ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 16),
    _PxmExtClk2ConnectorType_Type()
)
pxmExtClk2ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmExtClk2ConnectorType.setStatus("current")
_CmpClockMIBConformance_ObjectIdentity = ObjectIdentity
cmpClockMIBConformance = _CmpClockMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 72, 2)
)
_CmpClockMIBGroups_ObjectIdentity = ObjectIdentity
cmpClockMIBGroups = _CmpClockMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1)
)
_CmpClockMIBCompliances_ObjectIdentity = ObjectIdentity
cmpClockMIBCompliances = _CmpClockMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 2)
)

# Managed Objects groups

cmpClockInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 1)
)
cmpClockInfoGroup.setObjects(
      *(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmCurrentClock"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPreviousClock"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmClkStratumLevel"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmClkErrReason"))
)
if mibBuilder.loadTexts:
    cmpClockInfoGroup.setStatus("current")

cmpPrimaryClockInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 2)
)
cmpPrimaryClockInfoGroup.setObjects(
      *(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPrimaryMuxClockSource"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPrimaryInbandClockSourceLineNumber"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPrimarySMClockSourceSlotNumber"))
)
if mibBuilder.loadTexts:
    cmpPrimaryClockInfoGroup.setStatus("current")

cmpSecondaryClockInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 3)
)
cmpSecondaryClockInfoGroup.setObjects(
      *(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmSecondaryMuxClockSource"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmSecondaryInbandClockSourceLineNumber"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmSecondarySMClockSourceSlotNumber"))
)
if mibBuilder.loadTexts:
    cmpSecondaryClockInfoGroup.setStatus("current")

cmpExtClockInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 4)
)
cmpExtClockInfoGroup.setObjects(
      *(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClockPresent"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClkSrcImpedance"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClkConnectorType"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClock2Present"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClk2SrcImpedance"),
        ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClk2ConnectorType"))
)
if mibBuilder.loadTexts:
    cmpExtClockInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmpClockCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cmpClockCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-PXM-CLOCK-MIB",
    **{"CmpClockConnectorType": CmpClockConnectorType,
       "CmpClockSourceType": CmpClockSourceType,
       "CmpCurrentClock": CmpCurrentClock,
       "CmpClockExistence": CmpClockExistence,
       "CmpClockImpedance": CmpClockImpedance,
       "pxmClockConfig": pxmClockConfig,
       "pxmPrimaryMuxClockSource": pxmPrimaryMuxClockSource,
       "pxmPrimaryInbandClockSourceLineNumber": pxmPrimaryInbandClockSourceLineNumber,
       "pxmPrimarySMClockSourceSlotNumber": pxmPrimarySMClockSourceSlotNumber,
       "pxmSecondaryMuxClockSource": pxmSecondaryMuxClockSource,
       "pxmSecondaryInbandClockSourceLineNumber": pxmSecondaryInbandClockSourceLineNumber,
       "pxmSecondarySMClockSourceSlotNumber": pxmSecondarySMClockSourceSlotNumber,
       "pxmCurrentClock": pxmCurrentClock,
       "pxmPreviousClock": pxmPreviousClock,
       "pxmExtClockPresent": pxmExtClockPresent,
       "pxmExtClkSrcImpedance": pxmExtClkSrcImpedance,
       "pxmExtClkConnectorType": pxmExtClkConnectorType,
       "pxmClkStratumLevel": pxmClkStratumLevel,
       "pxmClkErrReason": pxmClkErrReason,
       "pxmExtClock2Present": pxmExtClock2Present,
       "pxmExtClk2SrcImpedance": pxmExtClk2SrcImpedance,
       "pxmExtClk2ConnectorType": pxmExtClk2ConnectorType,
       "ciscoMgx82xxPxmClockMIB": ciscoMgx82xxPxmClockMIB,
       "cmpClockMIBConformance": cmpClockMIBConformance,
       "cmpClockMIBGroups": cmpClockMIBGroups,
       "cmpClockInfoGroup": cmpClockInfoGroup,
       "cmpPrimaryClockInfoGroup": cmpPrimaryClockInfoGroup,
       "cmpSecondaryClockInfoGroup": cmpSecondaryClockInfoGroup,
       "cmpExtClockInfoGroup": cmpExtClockInfoGroup,
       "cmpClockMIBCompliances": cmpClockMIBCompliances,
       "cmpClockCompliance": cmpClockCompliance}
)
