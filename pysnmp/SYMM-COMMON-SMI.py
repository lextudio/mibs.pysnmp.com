# SNMP MIB module (SYMM-COMMON-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMM-COMMON-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:41 2024
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

symmetricom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070)
)
symmetricom.setRevisions(
        ("2018-08-23 08:22",)
)


# Types definitions



class EnableValue(Integer32):
    """Custom type EnableValue based on Integer32"""
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





class TP5000MODULEID(Integer32):
    """Custom type TP5000MODULEID based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("exp0", 6),
          ("exp1", 7),
          ("exp2", 8),
          ("exp3", 9),
          ("exp4", 10),
          ("exp5", 11),
          ("exp6", 12),
          ("exp7", 13),
          ("exp8", 14),
          ("exp9", 15),
          ("imc", 2),
          ("io", 5),
          ("ioc1", 3),
          ("ioc2", 4),
          ("sys", 1))
    )





class ONVALUETYPE(Integer32):
    """Custom type ONVALUETYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )





class ACTIONONLY(Integer32):
    """Custom type ACTIONONLY based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("nonapply", 2))
    )





class OPMODETYPE(Integer32):
    """Custom type OPMODETYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )





class ACTIVEVALUETYPE(Integer32):
    """Custom type ACTIVEVALUETYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )





class YESVALUETYPE(Integer32):
    """Custom type YESVALUETYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )





class OKVALUETYPE(Integer32):
    """Custom type OKVALUETYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("ok", 1))
    )





class VALIDTYPE(Integer32):
    """Custom type VALIDTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("nurture", 3),
          ("valid", 1))
    )





class GNSSHealthStatus(Integer32):
    """Custom type GNSSHealthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("healthy", 1),
          ("unhealthy", 2))
    )





class GNSSReceiverMode(Integer32):
    """Custom type GNSSReceiverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              128)
        )
    )
    namedValues = NamedValues(
        *(("beidou", 1),
          ("gnssBeidou", 24),
          ("gnssBeidouGPS", 25),
          ("gnssBeidouGalileo", 28),
          ("gnssBeidouGalileoGPS", 29),
          ("gnssBeidouGalileoGlonassGPSReserved", 31),
          ("gnssBeidouGalileoGlonassReserved", 30),
          ("gnssBeidouGlonass", 26),
          ("gnssBeidouGlonassGPSReserved", 27),
          ("gnssGPS", 17),
          ("gnssGPSGalileo", 21),
          ("gnssGPSGlonass", 19),
          ("gnssGPSGlonassGalileo", 23),
          ("gnssGalileo", 20),
          ("gnssGlonass", 18),
          ("gnssGlonassGalileo", 22),
          ("gps", 2),
          ("notApplicable", 128),
          ("priorityBeidou", 4),
          ("priorityGps", 5))
    )





class GNSSPositionMode(Integer32):
    """Custom type GNSSPositionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SymmNetworkManagement_ObjectIdentity = ObjectIdentity
symmNetworkManagement = _SymmNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1)
)
if mibBuilder.loadTexts:
    symmNetworkManagement.setStatus("current")
_SymmCmipManagement_ObjectIdentity = ObjectIdentity
symmCmipManagement = _SymmCmipManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 1)
)
if mibBuilder.loadTexts:
    symmCmipManagement.setStatus("current")
_SymmSnmpManagement_ObjectIdentity = ObjectIdentity
symmSnmpManagement = _SymmSnmpManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2)
)
if mibBuilder.loadTexts:
    symmSnmpManagement.setStatus("current")
_SymmTimePictra_ObjectIdentity = ObjectIdentity
symmTimePictra = _SymmTimePictra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 1)
)
if mibBuilder.loadTexts:
    symmTimePictra.setStatus("current")
_SymmBroadband_ObjectIdentity = ObjectIdentity
symmBroadband = _SymmBroadband_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 2)
)
if mibBuilder.loadTexts:
    symmBroadband.setStatus("current")
_SymmTTM_ObjectIdentity = ObjectIdentity
symmTTM = _SymmTTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3)
)
if mibBuilder.loadTexts:
    symmTTM.setStatus("current")
_SymmTSD_ObjectIdentity = ObjectIdentity
symmTSD = _SymmTSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 4)
)
if mibBuilder.loadTexts:
    symmTSD.setStatus("current")
_SymmCommonModelV1_ObjectIdentity = ObjectIdentity
symmCommonModelV1 = _SymmCommonModelV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5)
)
if mibBuilder.loadTexts:
    symmCommonModelV1.setStatus("current")
_SymmPacketService_ObjectIdentity = ObjectIdentity
symmPacketService = _SymmPacketService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    symmPacketService.setStatus("current")
_SymmPhysicalSignal_ObjectIdentity = ObjectIdentity
symmPhysicalSignal = _SymmPhysicalSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    symmPhysicalSignal.setStatus("current")
_SymmClock_ObjectIdentity = ObjectIdentity
symmClock = _SymmClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    symmClock.setStatus("current")
_SymmNetwork_ObjectIdentity = ObjectIdentity
symmNetwork = _SymmNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    symmNetwork.setStatus("current")
_SymmEntPhysicalExtension_ObjectIdentity = ObjectIdentity
symmEntPhysicalExtension = _SymmEntPhysicalExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    symmEntPhysicalExtension.setStatus("current")
_SymmInterfaceExtension_ObjectIdentity = ObjectIdentity
symmInterfaceExtension = _SymmInterfaceExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6)
)
if mibBuilder.loadTexts:
    symmInterfaceExtension.setStatus("current")
_SymmDeviceDependent_ObjectIdentity = ObjectIdentity
symmDeviceDependent = _SymmDeviceDependent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7)
)
if mibBuilder.loadTexts:
    symmDeviceDependent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMM-COMMON-SMI",
    **{"EnableValue": EnableValue,
       "TP5000MODULEID": TP5000MODULEID,
       "ONVALUETYPE": ONVALUETYPE,
       "ACTIONONLY": ACTIONONLY,
       "OPMODETYPE": OPMODETYPE,
       "ACTIVEVALUETYPE": ACTIVEVALUETYPE,
       "YESVALUETYPE": YESVALUETYPE,
       "OKVALUETYPE": OKVALUETYPE,
       "VALIDTYPE": VALIDTYPE,
       "GNSSHealthStatus": GNSSHealthStatus,
       "GNSSReceiverMode": GNSSReceiverMode,
       "GNSSPositionMode": GNSSPositionMode,
       "symmetricom": symmetricom,
       "symmNetworkManagement": symmNetworkManagement,
       "symmCmipManagement": symmCmipManagement,
       "symmSnmpManagement": symmSnmpManagement,
       "symmTimePictra": symmTimePictra,
       "symmBroadband": symmBroadband,
       "symmTTM": symmTTM,
       "symmTSD": symmTSD,
       "symmCommonModelV1": symmCommonModelV1,
       "symmPacketService": symmPacketService,
       "symmPhysicalSignal": symmPhysicalSignal,
       "symmClock": symmClock,
       "symmNetwork": symmNetwork,
       "symmEntPhysicalExtension": symmEntPhysicalExtension,
       "symmInterfaceExtension": symmInterfaceExtension,
       "symmDeviceDependent": symmDeviceDependent}
)
