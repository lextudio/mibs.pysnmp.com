# SNMP MIB module (CHIPCOMMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHIPCOMMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:45 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Chipcom_ObjectIdentity = ObjectIdentity
chipcom = _Chipcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49)
)
_Chipmib02_ObjectIdentity = ObjectIdentity
chipmib02 = _Chipmib02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2)
)
_ChipGen_ObjectIdentity = ObjectIdentity
chipGen = _ChipGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 1)
)


class _ChipGenProduct_Type(Integer32):
    """Custom type chipGenProduct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("product-4112H-MTP", 8),
          ("product-5100M-MGT", 1),
          ("product-5102B-EE", 2),
          ("product-5112H-UTP", 4),
          ("product-5200M-MGT", 7),
          ("product-5300M-MGT", 5),
          ("product-6100M-MGT", 12),
          ("product-8383B", 3))
    )


_ChipGenProduct_Type.__name__ = "Integer32"
_ChipGenProduct_Object = MibScalar
chipGenProduct = _ChipGenProduct_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 1),
    _ChipGenProduct_Type()
)
chipGenProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenProduct.setStatus("mandatory")


class _ChipGenServiceDate_Type(DisplayString):
    """Custom type chipGenServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ChipGenServiceDate_Type.__name__ = "DisplayString"
_ChipGenServiceDate_Object = MibScalar
chipGenServiceDate = _ChipGenServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 2),
    _ChipGenServiceDate_Type()
)
chipGenServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenServiceDate.setStatus("mandatory")
_ChipGenNetman_Type = IpAddress
_ChipGenNetman_Object = MibScalar
chipGenNetman = _ChipGenNetman_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 3),
    _ChipGenNetman_Type()
)
chipGenNetman.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenNetman.setStatus("mandatory")


class _ChipGenDiagnostics_Type(Integer32):
    """Custom type chipGenDiagnostics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("passed", 1))
    )


_ChipGenDiagnostics_Type.__name__ = "Integer32"
_ChipGenDiagnostics_Object = MibScalar
chipGenDiagnostics = _ChipGenDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 4),
    _ChipGenDiagnostics_Type()
)
chipGenDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenDiagnostics.setStatus("mandatory")


class _ChipGenSerial_Type(DisplayString):
    """Custom type chipGenSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ChipGenSerial_Type.__name__ = "DisplayString"
_ChipGenSerial_Object = MibScalar
chipGenSerial = _ChipGenSerial_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 5),
    _ChipGenSerial_Type()
)
chipGenSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenSerial.setStatus("mandatory")
_ChipGenID_Type = Integer32
_ChipGenID_Object = MibScalar
chipGenID = _ChipGenID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 6),
    _ChipGenID_Type()
)
chipGenID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipGenID.setStatus("mandatory")


class _ChipGenVers_Type(DisplayString):
    """Custom type chipGenVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ChipGenVers_Type.__name__ = "DisplayString"
_ChipGenVers_Object = MibScalar
chipGenVers = _ChipGenVers_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 7),
    _ChipGenVers_Type()
)
chipGenVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenVers.setStatus("mandatory")
_ChipGenAuthFailureAddr_Type = IpAddress
_ChipGenAuthFailureAddr_Object = MibScalar
chipGenAuthFailureAddr = _ChipGenAuthFailureAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 8),
    _ChipGenAuthFailureAddr_Type()
)
chipGenAuthFailureAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenAuthFailureAddr.setStatus("mandatory")
_ChipGenTimeLastChanged_Type = TimeTicks
_ChipGenTimeLastChanged_Object = MibScalar
chipGenTimeLastChanged = _ChipGenTimeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 9),
    _ChipGenTimeLastChanged_Type()
)
chipGenTimeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenTimeLastChanged.setStatus("mandatory")
_ChipEcho_ObjectIdentity = ObjectIdentity
chipEcho = _ChipEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 2)
)


class _ChipEchoStart_Type(Integer32):
    """Custom type chipEchoStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noEcho", 1),
          ("startEcho", 2))
    )


_ChipEchoStart_Type.__name__ = "Integer32"
_ChipEchoStart_Object = MibScalar
chipEchoStart = _ChipEchoStart_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 1),
    _ChipEchoStart_Type()
)
chipEchoStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipEchoStart.setStatus("mandatory")
_ChipEchoAddr_Type = IpAddress
_ChipEchoAddr_Object = MibScalar
chipEchoAddr = _ChipEchoAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 2),
    _ChipEchoAddr_Type()
)
chipEchoAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipEchoAddr.setStatus("mandatory")


class _ChipEchoPattern_Type(Integer32):
    """Custom type chipEchoPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 3),
          ("ones", 2),
          ("zeroes", 1))
    )


_ChipEchoPattern_Type.__name__ = "Integer32"
_ChipEchoPattern_Object = MibScalar
chipEchoPattern = _ChipEchoPattern_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 3),
    _ChipEchoPattern_Type()
)
chipEchoPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipEchoPattern.setStatus("mandatory")


class _ChipEchoNumber_Type(Integer32):
    """Custom type chipEchoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChipEchoNumber_Type.__name__ = "Integer32"
_ChipEchoNumber_Object = MibScalar
chipEchoNumber = _ChipEchoNumber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 4),
    _ChipEchoNumber_Type()
)
chipEchoNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipEchoNumber.setStatus("mandatory")


class _ChipEchoSize_Type(Integer32):
    """Custom type chipEchoSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_ChipEchoSize_Type.__name__ = "Integer32"
_ChipEchoSize_Object = MibScalar
chipEchoSize = _ChipEchoSize_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 5),
    _ChipEchoSize_Type()
)
chipEchoSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipEchoSize.setStatus("mandatory")
_ChipEchoResponseCounts_Type = Counter32
_ChipEchoResponseCounts_Object = MibScalar
chipEchoResponseCounts = _ChipEchoResponseCounts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 6),
    _ChipEchoResponseCounts_Type()
)
chipEchoResponseCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipEchoResponseCounts.setStatus("mandatory")
_ChipProducts_ObjectIdentity = ObjectIdentity
chipProducts = _ChipProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3)
)
_Online_ObjectIdentity = ObjectIdentity
online = _Online_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1)
)
_OlAgents_ObjectIdentity = ObjectIdentity
olAgents = _OlAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1)
)
_OlAgentsMySlot_Type = Integer32
_OlAgentsMySlot_Object = MibScalar
olAgentsMySlot = _OlAgentsMySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 1),
    _OlAgentsMySlot_Type()
)
olAgentsMySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olAgentsMySlot.setStatus("mandatory")


class _OlAgentsMasterReset_Type(Integer32):
    """Custom type olAgentsMasterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_OlAgentsMasterReset_Type.__name__ = "Integer32"
_OlAgentsMasterReset_Object = MibScalar
olAgentsMasterReset = _OlAgentsMasterReset_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 2),
    _OlAgentsMasterReset_Type()
)
olAgentsMasterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olAgentsMasterReset.setStatus("mandatory")
_OlAgentsTable_Object = MibTable
olAgentsTable = _OlAgentsTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    olAgentsTable.setStatus("mandatory")
_OlAgentsEntry_Object = MibTableRow
olAgentsEntry = _OlAgentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1)
)
olAgentsEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olAgentsSlotIndex"),
)
if mibBuilder.loadTexts:
    olAgentsEntry.setStatus("mandatory")
_OlAgentsSlotIndex_Type = Integer32
_OlAgentsSlotIndex_Object = MibTableColumn
olAgentsSlotIndex = _OlAgentsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 1),
    _OlAgentsSlotIndex_Type()
)
olAgentsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olAgentsSlotIndex.setStatus("mandatory")


class _OlAgentsStationAddr_Type(OctetString):
    """Custom type olAgentsStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlAgentsStationAddr_Type.__name__ = "OctetString"
_OlAgentsStationAddr_Object = MibTableColumn
olAgentsStationAddr = _OlAgentsStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 2),
    _OlAgentsStationAddr_Type()
)
olAgentsStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olAgentsStationAddr.setStatus("mandatory")
_OlAgentsIpAddress_Type = IpAddress
_OlAgentsIpAddress_Object = MibTableColumn
olAgentsIpAddress = _OlAgentsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 3),
    _OlAgentsIpAddress_Type()
)
olAgentsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olAgentsIpAddress.setStatus("mandatory")


class _OlAgentsMasterStatus_Type(Integer32):
    """Custom type olAgentsMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("electing", 3),
          ("master", 1),
          ("non-master", 2))
    )


_OlAgentsMasterStatus_Type.__name__ = "Integer32"
_OlAgentsMasterStatus_Object = MibTableColumn
olAgentsMasterStatus = _OlAgentsMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 4),
    _OlAgentsMasterStatus_Type()
)
olAgentsMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olAgentsMasterStatus.setStatus("mandatory")


class _OlAgentsMasterPriority_Type(Integer32):
    """Custom type olAgentsMasterPriority based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("never", 11),
          ("nine", 9),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("ten", 10),
          ("three", 3),
          ("two", 2))
    )


_OlAgentsMasterPriority_Type.__name__ = "Integer32"
_OlAgentsMasterPriority_Object = MibTableColumn
olAgentsMasterPriority = _OlAgentsMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 5),
    _OlAgentsMasterPriority_Type()
)
olAgentsMasterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olAgentsMasterPriority.setStatus("mandatory")
_OcAgentsSubSlot_Type = Integer32
_OcAgentsSubSlot_Object = MibTableColumn
ocAgentsSubSlot = _OcAgentsSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 6),
    _OcAgentsSubSlot_Type()
)
ocAgentsSubSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocAgentsSubSlot.setStatus("mandatory")
_OlConc_ObjectIdentity = ObjectIdentity
olConc = _OlConc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2)
)


class _OlConcType_Type(Integer32):
    """Custom type olConcType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("hub-4112-HMTP", 7),
          ("hub-5006C", 2),
          ("hub-5006C-FT", 3),
          ("hub-5006C-HC", 4),
          ("hub-5006C-HC-FT", 5),
          ("hub-5017C", 1),
          ("hub-5017C-LS", 9),
          ("hub-6017C-A", 6))
    )


_OlConcType_Type.__name__ = "Integer32"
_OlConcType_Object = MibScalar
olConcType = _OlConcType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2, 1),
    _OlConcType_Type()
)
olConcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olConcType.setStatus("mandatory")


class _OlConcReset_Type(Integer32):
    """Custom type olConcReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_OlConcReset_Type.__name__ = "Integer32"
_OlConcReset_Object = MibScalar
olConcReset = _OlConcReset_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2, 2),
    _OlConcReset_Type()
)
olConcReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olConcReset.setStatus("mandatory")
_OlConcNumSlots_Type = Integer32
_OlConcNumSlots_Object = MibScalar
olConcNumSlots = _OlConcNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2, 3),
    _OlConcNumSlots_Type()
)
olConcNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olConcNumSlots.setStatus("mandatory")


class _OlConcProfile_Type(OctetString):
    """Custom type olConcProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_OlConcProfile_Type.__name__ = "OctetString"
_OlConcProfile_Object = MibScalar
olConcProfile = _OlConcProfile_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2, 4),
    _OlConcProfile_Type()
)
olConcProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olConcProfile.setStatus("mandatory")
_OlEnv_ObjectIdentity = ObjectIdentity
olEnv = _OlEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3)
)


class _OlEnvTempStatus_Type(Integer32):
    """Custom type olEnvTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1),
          ("warning", 3))
    )


_OlEnvTempStatus_Type.__name__ = "Integer32"
_OlEnvTempStatus_Object = MibScalar
olEnvTempStatus = _OlEnvTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 1),
    _OlEnvTempStatus_Type()
)
olEnvTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvTempStatus.setStatus("mandatory")
_OlEnvPSCapacity_Type = Integer32
_OlEnvPSCapacity_Object = MibScalar
olEnvPSCapacity = _OlEnvPSCapacity_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 2),
    _OlEnvPSCapacity_Type()
)
olEnvPSCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvPSCapacity.setStatus("mandatory")
_OlEnvPSTable_Object = MibTable
olEnvPSTable = _OlEnvPSTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    olEnvPSTable.setStatus("mandatory")
_OlEnvPSEntry_Object = MibTableRow
olEnvPSEntry = _OlEnvPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 3, 1)
)
olEnvPSEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olEnvPSIndex"),
)
if mibBuilder.loadTexts:
    olEnvPSEntry.setStatus("mandatory")
_OlEnvPSIndex_Type = Integer32
_OlEnvPSIndex_Object = MibTableColumn
olEnvPSIndex = _OlEnvPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 3, 1, 1),
    _OlEnvPSIndex_Type()
)
olEnvPSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvPSIndex.setStatus("mandatory")


class _OlEnvPSAdminState_Type(Integer32):
    """Custom type olEnvPSAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("standby", 2))
    )


_OlEnvPSAdminState_Type.__name__ = "Integer32"
_OlEnvPSAdminState_Object = MibTableColumn
olEnvPSAdminState = _OlEnvPSAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 3, 1, 2),
    _OlEnvPSAdminState_Type()
)
olEnvPSAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olEnvPSAdminState.setStatus("mandatory")


class _OlEnvPSOperStatus_Type(Integer32):
    """Custom type olEnvPSOperStatus based on Integer32"""
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
        *(("active", 1),
          ("faulty", 3),
          ("not-installed", 4),
          ("standby", 2))
    )


_OlEnvPSOperStatus_Type.__name__ = "Integer32"
_OlEnvPSOperStatus_Object = MibTableColumn
olEnvPSOperStatus = _OlEnvPSOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 3, 1, 3),
    _OlEnvPSOperStatus_Type()
)
olEnvPSOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvPSOperStatus.setStatus("mandatory")


class _OlEnvFanStatus_Type(Integer32):
    """Custom type olEnvFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("not-installed", 4),
          ("okay", 1),
          ("unknown", 5))
    )


_OlEnvFanStatus_Type.__name__ = "Integer32"
_OlEnvFanStatus_Object = MibScalar
olEnvFanStatus = _OlEnvFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 4),
    _OlEnvFanStatus_Type()
)
olEnvFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvFanStatus.setStatus("mandatory")
_OlEnvTable_Object = MibTable
olEnvTable = _OlEnvTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    olEnvTable.setStatus("mandatory")
_OlEnvEntry_Object = MibTableRow
olEnvEntry = _OlEnvEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 5, 1)
)
olEnvEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olEnvType"),
)
if mibBuilder.loadTexts:
    olEnvEntry.setStatus("mandatory")


class _OlEnvType_Type(Integer32):
    """Custom type olEnvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ls-pdb", 1)
    )


_OlEnvType_Type.__name__ = "Integer32"
_OlEnvType_Object = MibTableColumn
olEnvType = _OlEnvType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 5, 1, 1),
    _OlEnvType_Type()
)
olEnvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvType.setStatus("mandatory")


class _OlEnvStatus_Type(Integer32):
    """Custom type olEnvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1))
    )


_OlEnvStatus_Type.__name__ = "Integer32"
_OlEnvStatus_Object = MibTableColumn
olEnvStatus = _OlEnvStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 5, 1, 2),
    _OlEnvStatus_Type()
)
olEnvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvStatus.setStatus("mandatory")
_OlModules_ObjectIdentity = ObjectIdentity
olModules = _OlModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4)
)
_OlModTable_Object = MibTable
olModTable = _OlModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    olModTable.setStatus("mandatory")
_OlModEntry_Object = MibTableRow
olModEntry = _OlModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1)
)
olModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olModSlotIndex"),
)
if mibBuilder.loadTexts:
    olModEntry.setStatus("mandatory")
_OlModSlotIndex_Type = Integer32
_OlModSlotIndex_Object = MibTableColumn
olModSlotIndex = _OlModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 1),
    _OlModSlotIndex_Type()
)
olModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModSlotIndex.setStatus("mandatory")


class _OlModType_Type(Integer32):
    """Custom type olModType based on Integer32"""
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
              15,
              16,
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
              32,
              33,
              35,
              43,
              45,
              46,
              47,
              48,
              50,
              51,
              52,
              53,
              62,
              65)
        )
    )
    namedValues = NamedValues(
        *(("module-41nnH-ETP", 53),
          ("module-41nnH-MTP", 52),
          ("module-50nnM-CTL", 3),
          ("module-50nnM-HCTL", 33),
          ("module-50nnM-RCLS", 51),
          ("module-50nnM-RCTL", 23),
          ("module-51nnB-EE", 9),
          ("module-51nnI-x", 31),
          ("module-51nnM-AUIF", 12),
          ("module-51nnM-AUIM", 13),
          ("module-51nnM-BNC", 8),
          ("module-51nnM-FB", 24),
          ("module-51nnM-FBP", 16),
          ("module-51nnM-FIB", 5),
          ("module-51nnM-FL", 22),
          ("module-51nnM-FP", 15),
          ("module-51nnM-MGT", 4),
          ("module-51nnM-TP", 7),
          ("module-51nnM-TPCL", 29),
          ("module-51nnM-TPL", 17),
          ("module-51nnM-TPLS", 48),
          ("module-51nnM-TPPL", 18),
          ("module-51nnM-TS", 21),
          ("module-51nnM-UTP", 6),
          ("module-51nnR-EE", 11),
          ("module-51nnR-ES", 10),
          ("module-5208M-TP", 14),
          ("module-52nnB-TT", 30),
          ("module-52nnM-EC", 62),
          ("module-52nnM-FR", 20),
          ("module-52nnM-MGT", 32),
          ("module-52nnM-TP", 19),
          ("module-53nnM-FBMIC", 26),
          ("module-53nnM-FIBST", 27),
          ("module-53nnM-MGT", 25),
          ("module-53nnM-STP", 28),
          ("module-53nnM-TDDI", 65),
          ("module-60nnM-MGT", 43),
          ("module-60nnM-RCTL", 50),
          ("module-61nnD-MGT", 45),
          ("module-61nnM-CAR", 35),
          ("module-61nnM-FBP", 46),
          ("module-61nnM-TPL", 47),
          ("module-unknown", 2),
          ("module-unmanageable", 1))
    )


_OlModType_Type.__name__ = "Integer32"
_OlModType_Object = MibTableColumn
olModType = _OlModType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 2),
    _OlModType_Type()
)
olModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModType.setStatus("mandatory")


class _OlModClass_Type(Integer32):
    """Custom type olModClass based on Integer32"""
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
              15,
              17,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("controller", 1),
          ("ethernet-carrier", 14),
          ("ethernet-connswitching-media", 10),
          ("ethernet-interconnect", 4),
          ("ethernet-media", 3),
          ("ethernet-media-extended", 19),
          ("ethernet-portswitching-media", 5),
          ("fddi-media", 8),
          ("fddi-mgmt", 12),
          ("mgmt", 2),
          ("oncore-download", 17),
          ("oncore-oem-specials", 15),
          ("oncore-token-ring-media", 13),
          ("online-token-ring-mod-interconnect", 20),
          ("terminal-server", 7),
          ("token-ring-interconnect", 11),
          ("token-ring-media", 6),
          ("token-ring-mgmt", 9))
    )


_OlModClass_Type.__name__ = "Integer32"
_OlModClass_Object = MibTableColumn
olModClass = _OlModClass_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 3),
    _OlModClass_Type()
)
olModClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModClass.setStatus("mandatory")


class _OlModDescr_Type(DisplayString):
    """Custom type olModDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OlModDescr_Type.__name__ = "DisplayString"
_OlModDescr_Object = MibTableColumn
olModDescr = _OlModDescr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 4),
    _OlModDescr_Type()
)
olModDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModDescr.setStatus("mandatory")


class _OlModVersion_Type(DisplayString):
    """Custom type olModVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OlModVersion_Type.__name__ = "DisplayString"
_OlModVersion_Object = MibTableColumn
olModVersion = _OlModVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 5),
    _OlModVersion_Type()
)
olModVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModVersion.setStatus("mandatory")


class _OlModVendor_Type(Integer32):
    """Custom type olModVendor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("chipcom", 1),
          ("cisco", 2),
          ("datability", 5),
          ("ibm", 6),
          ("intellicom", 9),
          ("pilkington", 3),
          ("raycom", 7),
          ("retix", 8))
    )


_OlModVendor_Type.__name__ = "Integer32"
_OlModVendor_Object = MibTableColumn
olModVendor = _OlModVendor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 6),
    _OlModVendor_Type()
)
olModVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModVendor.setStatus("mandatory")


class _OlModResetModule_Type(Integer32):
    """Custom type olModResetModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_OlModResetModule_Type.__name__ = "Integer32"
_OlModResetModule_Object = MibTableColumn
olModResetModule = _OlModResetModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 7),
    _OlModResetModule_Type()
)
olModResetModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olModResetModule.setStatus("mandatory")


class _OlModConfigToDips_Type(Integer32):
    """Custom type olModConfigToDips based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configure", 2),
          ("noConfigure", 1))
    )


_OlModConfigToDips_Type.__name__ = "Integer32"
_OlModConfigToDips_Object = MibTableColumn
olModConfigToDips = _OlModConfigToDips_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 8),
    _OlModConfigToDips_Type()
)
olModConfigToDips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olModConfigToDips.setStatus("mandatory")


class _OlModConfigured_Type(Integer32):
    """Custom type olModConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("notConfigured", 1))
    )


_OlModConfigured_Type.__name__ = "Integer32"
_OlModConfigured_Object = MibTableColumn
olModConfigured = _OlModConfigured_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 9),
    _OlModConfigured_Type()
)
olModConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModConfigured.setStatus("mandatory")


class _OlModNetwork_Type(Integer32):
    """Custom type olModNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
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
              15,
              16,
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
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36),
          ("fddi-1", 16),
          ("fddi-2", 17),
          ("fddi-3", 18),
          ("fddi-4", 19),
          ("front-panel", 5),
          ("isolated", 2),
          ("isolated-1", 21),
          ("isolated-10", 30),
          ("isolated-11", 31),
          ("isolated-2", 22),
          ("isolated-3", 23),
          ("isolated-4", 24),
          ("isolated-5", 25),
          ("isolated-6", 26),
          ("isolated-7", 27),
          ("isolated-8", 28),
          ("isolated-9", 29),
          ("other", 1),
          ("per-connector", 20),
          ("port-switching", 3),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlModNetwork_Type.__name__ = "Integer32"
_OlModNetwork_Object = MibTableColumn
olModNetwork = _OlModNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 10),
    _OlModNetwork_Type()
)
olModNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olModNetwork.setStatus("mandatory")


class _OlModNetworkType_Type(Integer32):
    """Custom type olModNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 5),
          ("fddi", 7),
          ("other", 1),
          ("port-switching", 3),
          ("serial", 8),
          ("token-ring", 6))
    )


_OlModNetworkType_Type.__name__ = "Integer32"
_OlModNetworkType_Object = MibTableColumn
olModNetworkType = _OlModNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 11),
    _OlModNetworkType_Type()
)
olModNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModNetworkType.setStatus("mandatory")


class _OlModStatus_Type(Integer32):
    """Custom type olModStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("booting", 20),
          ("fatalError", 10),
          ("okay", 1),
          ("partial-failure", 21))
    )


_OlModStatus_Type.__name__ = "Integer32"
_OlModStatus_Object = MibTableColumn
olModStatus = _OlModStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 12),
    _OlModStatus_Type()
)
olModStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModStatus.setStatus("mandatory")
_OlModNumPorts_Type = Integer32
_OlModNumPorts_Object = MibTableColumn
olModNumPorts = _OlModNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 13),
    _OlModNumPorts_Type()
)
olModNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModNumPorts.setStatus("mandatory")
_OlModNumTrunks_Type = Integer32
_OlModNumTrunks_Object = MibTableColumn
olModNumTrunks = _OlModNumTrunks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 14),
    _OlModNumTrunks_Type()
)
olModNumTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModNumTrunks.setStatus("mandatory")
_OlPortTable_Object = MibTable
olPortTable = _OlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    olPortTable.setStatus("mandatory")
_OlPortEntry_Object = MibTableRow
olPortEntry = _OlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1)
)
olPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olPortSlotIndex"),
    (0, "CHIPCOMMIB", "olPortIndex"),
)
if mibBuilder.loadTexts:
    olPortEntry.setStatus("mandatory")
_OlPortSlotIndex_Type = Integer32
_OlPortSlotIndex_Object = MibTableColumn
olPortSlotIndex = _OlPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 1),
    _OlPortSlotIndex_Type()
)
olPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortSlotIndex.setStatus("mandatory")
_OlPortIndex_Type = Integer32
_OlPortIndex_Object = MibTableColumn
olPortIndex = _OlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 2),
    _OlPortIndex_Type()
)
olPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortIndex.setStatus("mandatory")


class _OlPortType_Type(Integer32):
    """Custom type olPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("logical", 1),
          ("media", 2),
          ("virtual", 5))
    )


_OlPortType_Type.__name__ = "Integer32"
_OlPortType_Object = MibTableColumn
olPortType = _OlPortType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 3),
    _OlPortType_Type()
)
olPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortType.setStatus("mandatory")


class _OlPortConnector_Type(Integer32):
    """Custom type olPortConnector based on Integer32"""
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
              15,
              17,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("backPlane", 1),
          ("bnc", 2),
          ("db-25", 15),
          ("db-50", 6),
          ("db-9", 10),
          ("ethernet-fc", 23),
          ("ethernet-sma", 17),
          ("ethernet-st", 24),
          ("faui", 3),
          ("fddi-lc", 12),
          ("fddi-mic", 14),
          ("fddi-st", 13),
          ("fiber", 5),
          ("maui", 4),
          ("rj45", 8),
          ("rj45S", 9),
          ("telco", 7),
          ("virtual", 11))
    )


_OlPortConnector_Type.__name__ = "Integer32"
_OlPortConnector_Object = MibTableColumn
olPortConnector = _OlPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 4),
    _OlPortConnector_Type()
)
olPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortConnector.setStatus("mandatory")


class _OlPortStatus_Type(Integer32):
    """Custom type olPortStatus based on Integer32"""
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
              15,
              19,
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
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("attach3174To32-3299", 34),
          ("attach3174To8-3299", 33),
          ("attach3174ToDirect", 35),
          ("attach3174Unavailable", 36),
          ("attach3174Unknown", 32),
          ("backup-link", 24),
          ("beacon", 27),
          ("connecting", 23),
          ("fatalError", 10),
          ("fifoOverrun", 8),
          ("fifoUnderrun", 9),
          ("invalidData", 6),
          ("jabber", 3),
          ("linkFailure", 2),
          ("lowLight", 7),
          ("macRemoved", 29),
          ("mjlp", 12),
          ("noCable", 13),
          ("noPhantom", 15),
          ("noSquelch", 14),
          ("notInserted", 30),
          ("off", 22),
          ("okay", 1),
          ("okay-standby", 19),
          ("partition", 11),
          ("remoteJabber", 5),
          ("remoteLinkFailure", 4),
          ("security-breach", 25),
          ("speedMismatch", 31),
          ("transientError", 37),
          ("unknownStatus", 26),
          ("wireFault", 28))
    )


_OlPortStatus_Type.__name__ = "Integer32"
_OlPortStatus_Object = MibTableColumn
olPortStatus = _OlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 5),
    _OlPortStatus_Type()
)
olPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortStatus.setStatus("mandatory")


class _OlPortAdminState_Type(Integer32):
    """Custom type olPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("local", 6),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("redundant-rfs", 5),
          ("remote", 7),
          ("remote-diagnostics", 8),
          ("unknown", 9))
    )


_OlPortAdminState_Type.__name__ = "Integer32"
_OlPortAdminState_Object = MibTableColumn
olPortAdminState = _OlPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 6),
    _OlPortAdminState_Type()
)
olPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olPortAdminState.setStatus("mandatory")


class _OlPortNetwork_Type(Integer32):
    """Custom type olPortNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
              15,
              16,
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
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36),
          ("fddi-1", 16),
          ("fddi-2", 17),
          ("fddi-3", 18),
          ("fddi-4", 19),
          ("front-panel", 5),
          ("isolated", 2),
          ("isolated-1", 21),
          ("isolated-10", 30),
          ("isolated-11", 31),
          ("isolated-2", 22),
          ("isolated-3", 23),
          ("isolated-4", 24),
          ("isolated-5", 25),
          ("isolated-6", 26),
          ("isolated-7", 27),
          ("isolated-8", 28),
          ("isolated-9", 29),
          ("other", 1),
          ("per-connector", 20),
          ("per-module", 4),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlPortNetwork_Type.__name__ = "Integer32"
_OlPortNetwork_Object = MibTableColumn
olPortNetwork = _OlPortNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 7),
    _OlPortNetwork_Type()
)
olPortNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olPortNetwork.setStatus("mandatory")


class _OlPortNetworkType_Type(Integer32):
    """Custom type olPortNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 5),
          ("fddi", 7),
          ("other", 1),
          ("serial", 8))
    )


_OlPortNetworkType_Type.__name__ = "Integer32"
_OlPortNetworkType_Object = MibTableColumn
olPortNetworkType = _OlPortNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 8),
    _OlPortNetworkType_Type()
)
olPortNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortNetworkType.setStatus("mandatory")


class _OlPortAlertFilter_Type(Integer32):
    """Custom type olPortAlertFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("other", 3))
    )


_OlPortAlertFilter_Type.__name__ = "Integer32"
_OlPortAlertFilter_Object = MibTableColumn
olPortAlertFilter = _OlPortAlertFilter_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 9),
    _OlPortAlertFilter_Type()
)
olPortAlertFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olPortAlertFilter.setStatus("mandatory")
_OlTrunkTable_Object = MibTable
olTrunkTable = _OlTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    olTrunkTable.setStatus("mandatory")
_OlTrunkEntry_Object = MibTableRow
olTrunkEntry = _OlTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1)
)
olTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "olTrunkIndex"),
)
if mibBuilder.loadTexts:
    olTrunkEntry.setStatus("mandatory")
_OlTrunkSlotIndex_Type = Integer32
_OlTrunkSlotIndex_Object = MibTableColumn
olTrunkSlotIndex = _OlTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 1),
    _OlTrunkSlotIndex_Type()
)
olTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkSlotIndex.setStatus("mandatory")
_OlTrunkIndex_Type = Integer32
_OlTrunkIndex_Object = MibTableColumn
olTrunkIndex = _OlTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 2),
    _OlTrunkIndex_Type()
)
olTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkIndex.setStatus("mandatory")


class _OlTrunkType_Type(Integer32):
    """Custom type olTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("backplaneIn", 6),
          ("backplaneOut", 7),
          ("other", 1),
          ("ringIn", 3),
          ("ringOut", 4))
    )


_OlTrunkType_Type.__name__ = "Integer32"
_OlTrunkType_Object = MibTableColumn
olTrunkType = _OlTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 3),
    _OlTrunkType_Type()
)
olTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkType.setStatus("mandatory")


class _OlTrunkConnector_Type(Integer32):
    """Custom type olTrunkConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 1),
          ("fiber", 5),
          ("rj45S", 9))
    )


_OlTrunkConnector_Type.__name__ = "Integer32"
_OlTrunkConnector_Object = MibTableColumn
olTrunkConnector = _OlTrunkConnector_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 4),
    _OlTrunkConnector_Type()
)
olTrunkConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkConnector.setStatus("mandatory")


class _OlTrunkStatus_Type(Integer32):
    """Custom type olTrunkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              13,
              14,
              16,
              17,
              18,
              19,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("beacon", 27),
          ("fatalError", 10),
          ("invalidConfig", 18),
          ("linkFailure", 2),
          ("lostLock", 16),
          ("noCable", 13),
          ("noSquelch", 14),
          ("okay", 1),
          ("okay-standby", 19),
          ("upstreamNeighborLost", 17),
          ("wireFault", 28))
    )


_OlTrunkStatus_Type.__name__ = "Integer32"
_OlTrunkStatus_Object = MibTableColumn
olTrunkStatus = _OlTrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 5),
    _OlTrunkStatus_Type()
)
olTrunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkStatus.setStatus("mandatory")


class _OlTrunkAdminState_Type(Integer32):
    """Custom type olTrunkAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_OlTrunkAdminState_Type.__name__ = "Integer32"
_OlTrunkAdminState_Object = MibTableColumn
olTrunkAdminState = _OlTrunkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 6),
    _OlTrunkAdminState_Type()
)
olTrunkAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTrunkAdminState.setStatus("mandatory")


class _OlTrunkWrapState_Type(Integer32):
    """Custom type olTrunkWrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unwrapped", 2),
          ("wrapped", 1))
    )


_OlTrunkWrapState_Type.__name__ = "Integer32"
_OlTrunkWrapState_Object = MibTableColumn
olTrunkWrapState = _OlTrunkWrapState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 7),
    _OlTrunkWrapState_Type()
)
olTrunkWrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkWrapState.setStatus("mandatory")


class _OlTrunkNeighbor_Type(Integer32):
    """Custom type olTrunkNeighbor based on Integer32"""
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
              15,
              16,
              17,
              256)
        )
    )
    namedValues = NamedValues(
        *(("external", 256),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_OlTrunkNeighbor_Type.__name__ = "Integer32"
_OlTrunkNeighbor_Object = MibTableColumn
olTrunkNeighbor = _OlTrunkNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 8),
    _OlTrunkNeighbor_Type()
)
olTrunkNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkNeighbor.setStatus("mandatory")
_OlSpecMods_ObjectIdentity = ObjectIdentity
olSpecMods = _OlSpecMods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4)
)
_Ol50nnMCTL_ObjectIdentity = ObjectIdentity
ol50nnMCTL = _Ol50nnMCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3)
)
_Ol50nnMCTLModTable_Object = MibTable
ol50nnMCTLModTable = _Ol50nnMCTLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ol50nnMCTLModTable.setStatus("mandatory")
_Ol50nnMCTLModEntry_Object = MibTableRow
ol50nnMCTLModEntry = _Ol50nnMCTLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3, 1, 1)
)
ol50nnMCTLModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol50nnMCTLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol50nnMCTLModEntry.setStatus("mandatory")
_Ol50nnMCTLModSlotIndex_Type = Integer32
_Ol50nnMCTLModSlotIndex_Object = MibTableColumn
ol50nnMCTLModSlotIndex = _Ol50nnMCTLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3, 1, 1, 1),
    _Ol50nnMCTLModSlotIndex_Type()
)
ol50nnMCTLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMCTLModSlotIndex.setStatus("mandatory")


class _Ol50nnMCTLModTempStatus_Type(Integer32):
    """Custom type ol50nnMCTLModTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1))
    )


_Ol50nnMCTLModTempStatus_Type.__name__ = "Integer32"
_Ol50nnMCTLModTempStatus_Object = MibTableColumn
ol50nnMCTLModTempStatus = _Ol50nnMCTLModTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3, 1, 1, 2),
    _Ol50nnMCTLModTempStatus_Type()
)
ol50nnMCTLModTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMCTLModTempStatus.setStatus("mandatory")
_Ol51nnMMGT_ObjectIdentity = ObjectIdentity
ol51nnMMGT = _Ol51nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4)
)
_Ol51nnMMGTModTable_Object = MibTable
ol51nnMMGTModTable = _Ol51nnMMGTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1)
)
if mibBuilder.loadTexts:
    ol51nnMMGTModTable.setStatus("mandatory")
_Ol51nnMMGTModEntry_Object = MibTableRow
ol51nnMMGTModEntry = _Ol51nnMMGTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1, 1)
)
ol51nnMMGTModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMMGTModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMMGTModEntry.setStatus("mandatory")
_Ol51nnMMGTModSlotIndex_Type = Integer32
_Ol51nnMMGTModSlotIndex_Object = MibTableColumn
ol51nnMMGTModSlotIndex = _Ol51nnMMGTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1, 1, 1),
    _Ol51nnMMGTModSlotIndex_Type()
)
ol51nnMMGTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTModSlotIndex.setStatus("mandatory")


class _Ol51nnMMGTModMasterPriority_Type(Integer32):
    """Custom type ol51nnMMGTModMasterPriority based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("nine", 9),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("ten", 10),
          ("three", 3),
          ("two", 2))
    )


_Ol51nnMMGTModMasterPriority_Type.__name__ = "Integer32"
_Ol51nnMMGTModMasterPriority_Object = MibTableColumn
ol51nnMMGTModMasterPriority = _Ol51nnMMGTModMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1, 1, 2),
    _Ol51nnMMGTModMasterPriority_Type()
)
ol51nnMMGTModMasterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMMGTModMasterPriority.setStatus("mandatory")


class _Ol51nnMMGTModMasterStatus_Type(Integer32):
    """Custom type ol51nnMMGTModMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("electing", 3),
          ("master", 1),
          ("non-master", 2))
    )


_Ol51nnMMGTModMasterStatus_Type.__name__ = "Integer32"
_Ol51nnMMGTModMasterStatus_Object = MibTableColumn
ol51nnMMGTModMasterStatus = _Ol51nnMMGTModMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1, 1, 3),
    _Ol51nnMMGTModMasterStatus_Type()
)
ol51nnMMGTModMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTModMasterStatus.setStatus("mandatory")


class _Ol51nnMMGTModStationAddr_Type(OctetString):
    """Custom type ol51nnMMGTModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnMMGTModStationAddr_Type.__name__ = "OctetString"
_Ol51nnMMGTModStationAddr_Object = MibTableColumn
ol51nnMMGTModStationAddr = _Ol51nnMMGTModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1, 1, 4),
    _Ol51nnMMGTModStationAddr_Type()
)
ol51nnMMGTModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTModStationAddr.setStatus("mandatory")
_Ol51nnMMGTPortTable_Object = MibTable
ol51nnMMGTPortTable = _Ol51nnMMGTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 2)
)
if mibBuilder.loadTexts:
    ol51nnMMGTPortTable.setStatus("mandatory")
_Ol51nnMMGTPortEntry_Object = MibTableRow
ol51nnMMGTPortEntry = _Ol51nnMMGTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 2, 1)
)
ol51nnMMGTPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMMGTPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMMGTPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMMGTPortEntry.setStatus("mandatory")
_Ol51nnMMGTPortSlotIndex_Type = Integer32
_Ol51nnMMGTPortSlotIndex_Object = MibTableColumn
ol51nnMMGTPortSlotIndex = _Ol51nnMMGTPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 2, 1, 1),
    _Ol51nnMMGTPortSlotIndex_Type()
)
ol51nnMMGTPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTPortSlotIndex.setStatus("mandatory")
_Ol51nnMMGTPortIndex_Type = Integer32
_Ol51nnMMGTPortIndex_Object = MibTableColumn
ol51nnMMGTPortIndex = _Ol51nnMMGTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 2, 1, 2),
    _Ol51nnMMGTPortIndex_Type()
)
ol51nnMMGTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTPortIndex.setStatus("mandatory")
_Ol51nnMMGTIpAddress_Type = IpAddress
_Ol51nnMMGTIpAddress_Object = MibTableColumn
ol51nnMMGTIpAddress = _Ol51nnMMGTIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 2, 1, 3),
    _Ol51nnMMGTIpAddress_Type()
)
ol51nnMMGTIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTIpAddress.setStatus("mandatory")
_Ol51nnMFIB_ObjectIdentity = ObjectIdentity
ol51nnMFIB = _Ol51nnMFIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5)
)
_Ol51nnMFIBModTable_Object = MibTable
ol51nnMFIBModTable = _Ol51nnMFIBModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ol51nnMFIBModTable.setStatus("mandatory")
_Ol51nnMFIBModEntry_Object = MibTableRow
ol51nnMFIBModEntry = _Ol51nnMFIBModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1, 1)
)
ol51nnMFIBModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMFIBModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFIBModEntry.setStatus("mandatory")
_Ol51nnMFIBModSlotIndex_Type = Integer32
_Ol51nnMFIBModSlotIndex_Object = MibTableColumn
ol51nnMFIBModSlotIndex = _Ol51nnMFIBModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1, 1, 1),
    _Ol51nnMFIBModSlotIndex_Type()
)
ol51nnMFIBModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBModSlotIndex.setStatus("mandatory")


class _Ol51nnMFIBModDipNetwork_Type(Integer32):
    """Custom type ol51nnMFIBModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMFIBModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMFIBModDipNetwork_Object = MibTableColumn
ol51nnMFIBModDipNetwork = _Ol51nnMFIBModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1, 1, 2),
    _Ol51nnMFIBModDipNetwork_Type()
)
ol51nnMFIBModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBModDipNetwork.setStatus("mandatory")


class _Ol51nnMFIBModLLW_Type(Integer32):
    """Custom type ol51nnMFIBModLLW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFIBModLLW_Type.__name__ = "Integer32"
_Ol51nnMFIBModLLW_Object = MibTableColumn
ol51nnMFIBModLLW = _Ol51nnMFIBModLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1, 1, 3),
    _Ol51nnMFIBModLLW_Type()
)
ol51nnMFIBModLLW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFIBModLLW.setStatus("mandatory")


class _Ol51nnMFIBModDipLLW_Type(Integer32):
    """Custom type ol51nnMFIBModDipLLW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFIBModDipLLW_Type.__name__ = "Integer32"
_Ol51nnMFIBModDipLLW_Object = MibTableColumn
ol51nnMFIBModDipLLW = _Ol51nnMFIBModDipLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1, 1, 4),
    _Ol51nnMFIBModDipLLW_Type()
)
ol51nnMFIBModDipLLW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBModDipLLW.setStatus("mandatory")
_Ol51nnMFIBPortTable_Object = MibTable
ol51nnMFIBPortTable = _Ol51nnMFIBPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2)
)
if mibBuilder.loadTexts:
    ol51nnMFIBPortTable.setStatus("mandatory")
_Ol51nnMFIBPortEntry_Object = MibTableRow
ol51nnMFIBPortEntry = _Ol51nnMFIBPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1)
)
ol51nnMFIBPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMFIBPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMFIBPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFIBPortEntry.setStatus("mandatory")
_Ol51nnMFIBPortSlotIndex_Type = Integer32
_Ol51nnMFIBPortSlotIndex_Object = MibTableColumn
ol51nnMFIBPortSlotIndex = _Ol51nnMFIBPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 1),
    _Ol51nnMFIBPortSlotIndex_Type()
)
ol51nnMFIBPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBPortSlotIndex.setStatus("mandatory")
_Ol51nnMFIBPortIndex_Type = Integer32
_Ol51nnMFIBPortIndex_Object = MibTableColumn
ol51nnMFIBPortIndex = _Ol51nnMFIBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 2),
    _Ol51nnMFIBPortIndex_Type()
)
ol51nnMFIBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBPortIndex.setStatus("mandatory")


class _Ol51nnMFIBPortAdminState_Type(Integer32):
    """Custom type ol51nnMFIBPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFIBPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMFIBPortAdminState_Object = MibTableColumn
ol51nnMFIBPortAdminState = _Ol51nnMFIBPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 3),
    _Ol51nnMFIBPortAdminState_Type()
)
ol51nnMFIBPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFIBPortAdminState.setStatus("mandatory")
_Ol51nnMFIBPortBuddySlot_Type = Integer32
_Ol51nnMFIBPortBuddySlot_Object = MibTableColumn
ol51nnMFIBPortBuddySlot = _Ol51nnMFIBPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 4),
    _Ol51nnMFIBPortBuddySlot_Type()
)
ol51nnMFIBPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFIBPortBuddySlot.setStatus("mandatory")
_Ol51nnMFIBPortBuddyPort_Type = Integer32
_Ol51nnMFIBPortBuddyPort_Object = MibTableColumn
ol51nnMFIBPortBuddyPort = _Ol51nnMFIBPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 5),
    _Ol51nnMFIBPortBuddyPort_Type()
)
ol51nnMFIBPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFIBPortBuddyPort.setStatus("mandatory")


class _Ol51nnMFIBPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMFIBPortDipAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFIBPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMFIBPortDipAdminState_Object = MibTableColumn
ol51nnMFIBPortDipAdminState = _Ol51nnMFIBPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 6),
    _Ol51nnMFIBPortDipAdminState_Type()
)
ol51nnMFIBPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBPortDipAdminState.setStatus("mandatory")
_Ol51nnMUTP_ObjectIdentity = ObjectIdentity
ol51nnMUTP = _Ol51nnMUTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6)
)
_Ol51nnMUTPModTable_Object = MibTable
ol51nnMUTPModTable = _Ol51nnMUTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1)
)
if mibBuilder.loadTexts:
    ol51nnMUTPModTable.setStatus("mandatory")
_Ol51nnMUTPModEntry_Object = MibTableRow
ol51nnMUTPModEntry = _Ol51nnMUTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1)
)
ol51nnMUTPModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMUTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMUTPModEntry.setStatus("mandatory")
_Ol51nnMUTPModSlotIndex_Type = Integer32
_Ol51nnMUTPModSlotIndex_Object = MibTableColumn
ol51nnMUTPModSlotIndex = _Ol51nnMUTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 1),
    _Ol51nnMUTPModSlotIndex_Type()
)
ol51nnMUTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPModSlotIndex.setStatus("mandatory")


class _Ol51nnMUTPModDipNetwork_Type(Integer32):
    """Custom type ol51nnMUTPModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMUTPModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMUTPModDipNetwork_Object = MibTableColumn
ol51nnMUTPModDipNetwork = _Ol51nnMUTPModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 2),
    _Ol51nnMUTPModDipNetwork_Type()
)
ol51nnMUTPModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPModDipNetwork.setStatus("mandatory")


class _Ol51nnMUTPModCrossover_Type(Integer32):
    """Custom type ol51nnMUTPModCrossover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 1),
          ("uncrossed", 2))
    )


_Ol51nnMUTPModCrossover_Type.__name__ = "Integer32"
_Ol51nnMUTPModCrossover_Object = MibTableColumn
ol51nnMUTPModCrossover = _Ol51nnMUTPModCrossover_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 3),
    _Ol51nnMUTPModCrossover_Type()
)
ol51nnMUTPModCrossover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPModCrossover.setStatus("mandatory")


class _Ol51nnMUTPModDipCrossover_Type(Integer32):
    """Custom type ol51nnMUTPModDipCrossover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 1),
          ("uncrossed", 2))
    )


_Ol51nnMUTPModDipCrossover_Type.__name__ = "Integer32"
_Ol51nnMUTPModDipCrossover_Object = MibTableColumn
ol51nnMUTPModDipCrossover = _Ol51nnMUTPModDipCrossover_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 4),
    _Ol51nnMUTPModDipCrossover_Type()
)
ol51nnMUTPModDipCrossover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPModDipCrossover.setStatus("mandatory")


class _Ol51nnMUTPModFFL_Type(Integer32):
    """Custom type ol51nnMUTPModFFL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eight-bits", 1),
          ("seven-bits", 2))
    )


_Ol51nnMUTPModFFL_Type.__name__ = "Integer32"
_Ol51nnMUTPModFFL_Object = MibTableColumn
ol51nnMUTPModFFL = _Ol51nnMUTPModFFL_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 5),
    _Ol51nnMUTPModFFL_Type()
)
ol51nnMUTPModFFL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPModFFL.setStatus("mandatory")


class _Ol51nnMUTPModDipFFL_Type(Integer32):
    """Custom type ol51nnMUTPModDipFFL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eight-bits", 1),
          ("seven-bits", 2))
    )


_Ol51nnMUTPModDipFFL_Type.__name__ = "Integer32"
_Ol51nnMUTPModDipFFL_Object = MibTableColumn
ol51nnMUTPModDipFFL = _Ol51nnMUTPModDipFFL_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 6),
    _Ol51nnMUTPModDipFFL_Type()
)
ol51nnMUTPModDipFFL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPModDipFFL.setStatus("mandatory")
_Ol51nnMUTPPortTable_Object = MibTable
ol51nnMUTPPortTable = _Ol51nnMUTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2)
)
if mibBuilder.loadTexts:
    ol51nnMUTPPortTable.setStatus("mandatory")
_Ol51nnMUTPPortEntry_Object = MibTableRow
ol51nnMUTPPortEntry = _Ol51nnMUTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1)
)
ol51nnMUTPPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMUTPPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMUTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMUTPPortEntry.setStatus("mandatory")
_Ol51nnMUTPPortSlotIndex_Type = Integer32
_Ol51nnMUTPPortSlotIndex_Object = MibTableColumn
ol51nnMUTPPortSlotIndex = _Ol51nnMUTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 1),
    _Ol51nnMUTPPortSlotIndex_Type()
)
ol51nnMUTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPPortSlotIndex.setStatus("mandatory")
_Ol51nnMUTPPortIndex_Type = Integer32
_Ol51nnMUTPPortIndex_Object = MibTableColumn
ol51nnMUTPPortIndex = _Ol51nnMUTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 2),
    _Ol51nnMUTPPortIndex_Type()
)
ol51nnMUTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPPortIndex.setStatus("mandatory")


class _Ol51nnMUTPPortAdminState_Type(Integer32):
    """Custom type ol51nnMUTPPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMUTPPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMUTPPortAdminState_Object = MibTableColumn
ol51nnMUTPPortAdminState = _Ol51nnMUTPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 3),
    _Ol51nnMUTPPortAdminState_Type()
)
ol51nnMUTPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPPortAdminState.setStatus("mandatory")
_Ol51nnMUTPPortBuddySlot_Type = Integer32
_Ol51nnMUTPPortBuddySlot_Object = MibTableColumn
ol51nnMUTPPortBuddySlot = _Ol51nnMUTPPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 4),
    _Ol51nnMUTPPortBuddySlot_Type()
)
ol51nnMUTPPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPPortBuddySlot.setStatus("mandatory")
_Ol51nnMUTPPortBuddyPort_Type = Integer32
_Ol51nnMUTPPortBuddyPort_Object = MibTableColumn
ol51nnMUTPPortBuddyPort = _Ol51nnMUTPPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 5),
    _Ol51nnMUTPPortBuddyPort_Type()
)
ol51nnMUTPPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPPortBuddyPort.setStatus("mandatory")


class _Ol51nnMUTPPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMUTPPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMUTPPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMUTPPortDipAdminState_Object = MibTableColumn
ol51nnMUTPPortDipAdminState = _Ol51nnMUTPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 6),
    _Ol51nnMUTPPortDipAdminState_Type()
)
ol51nnMUTPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPPortDipAdminState.setStatus("mandatory")


class _Ol51nnMUTPPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMUTPPortLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMUTPPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMUTPPortLinkInteg_Object = MibTableColumn
ol51nnMUTPPortLinkInteg = _Ol51nnMUTPPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 7),
    _Ol51nnMUTPPortLinkInteg_Type()
)
ol51nnMUTPPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPPortLinkInteg.setStatus("mandatory")


class _Ol51nnMUTPPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMUTPPortDipLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMUTPPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMUTPPortDipLinkInteg_Object = MibTableColumn
ol51nnMUTPPortDipLinkInteg = _Ol51nnMUTPPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 8),
    _Ol51nnMUTPPortDipLinkInteg_Type()
)
ol51nnMUTPPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPPortDipLinkInteg.setStatus("mandatory")


class _Ol51nnMUTPPortSquelch_Type(Integer32):
    """Custom type ol51nnMUTPPortSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMUTPPortSquelch_Type.__name__ = "Integer32"
_Ol51nnMUTPPortSquelch_Object = MibTableColumn
ol51nnMUTPPortSquelch = _Ol51nnMUTPPortSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 9),
    _Ol51nnMUTPPortSquelch_Type()
)
ol51nnMUTPPortSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPPortSquelch.setStatus("mandatory")


class _Ol51nnMUTPPortDipSquelch_Type(Integer32):
    """Custom type ol51nnMUTPPortDipSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMUTPPortDipSquelch_Type.__name__ = "Integer32"
_Ol51nnMUTPPortDipSquelch_Object = MibTableColumn
ol51nnMUTPPortDipSquelch = _Ol51nnMUTPPortDipSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 10),
    _Ol51nnMUTPPortDipSquelch_Type()
)
ol51nnMUTPPortDipSquelch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPPortDipSquelch.setStatus("mandatory")
_Ol51nnMTP_ObjectIdentity = ObjectIdentity
ol51nnMTP = _Ol51nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7)
)
_Ol51nnMTPModTable_Object = MibTable
ol51nnMTPModTable = _Ol51nnMTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTPModTable.setStatus("mandatory")
_Ol51nnMTPModEntry_Object = MibTableRow
ol51nnMTPModEntry = _Ol51nnMTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1, 1)
)
ol51nnMTPModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPModEntry.setStatus("mandatory")
_Ol51nnMTPModSlotIndex_Type = Integer32
_Ol51nnMTPModSlotIndex_Object = MibTableColumn
ol51nnMTPModSlotIndex = _Ol51nnMTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1, 1, 1),
    _Ol51nnMTPModSlotIndex_Type()
)
ol51nnMTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPModSlotIndex.setStatus("mandatory")


class _Ol51nnMTPModDipNetwork_Type(Integer32):
    """Custom type ol51nnMTPModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMTPModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPModDipNetwork_Object = MibTableColumn
ol51nnMTPModDipNetwork = _Ol51nnMTPModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1, 1, 2),
    _Ol51nnMTPModDipNetwork_Type()
)
ol51nnMTPModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPModDipNetwork.setStatus("mandatory")


class _Ol51nnMTPModCrossover_Type(Integer32):
    """Custom type ol51nnMTPModCrossover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 1),
          ("uncrossed", 2))
    )


_Ol51nnMTPModCrossover_Type.__name__ = "Integer32"
_Ol51nnMTPModCrossover_Object = MibTableColumn
ol51nnMTPModCrossover = _Ol51nnMTPModCrossover_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1, 1, 3),
    _Ol51nnMTPModCrossover_Type()
)
ol51nnMTPModCrossover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPModCrossover.setStatus("mandatory")


class _Ol51nnMTPModDipCrossover_Type(Integer32):
    """Custom type ol51nnMTPModDipCrossover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 1),
          ("uncrossed", 2))
    )


_Ol51nnMTPModDipCrossover_Type.__name__ = "Integer32"
_Ol51nnMTPModDipCrossover_Object = MibTableColumn
ol51nnMTPModDipCrossover = _Ol51nnMTPModDipCrossover_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1, 1, 4),
    _Ol51nnMTPModDipCrossover_Type()
)
ol51nnMTPModDipCrossover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPModDipCrossover.setStatus("mandatory")
_Ol51nnMTPPortTable_Object = MibTable
ol51nnMTPPortTable = _Ol51nnMTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTPPortTable.setStatus("mandatory")
_Ol51nnMTPPortEntry_Object = MibTableRow
ol51nnMTPPortEntry = _Ol51nnMTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1)
)
ol51nnMTPPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTPPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPPortEntry.setStatus("mandatory")
_Ol51nnMTPPortSlotIndex_Type = Integer32
_Ol51nnMTPPortSlotIndex_Object = MibTableColumn
ol51nnMTPPortSlotIndex = _Ol51nnMTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 1),
    _Ol51nnMTPPortSlotIndex_Type()
)
ol51nnMTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPortSlotIndex.setStatus("mandatory")
_Ol51nnMTPPortIndex_Type = Integer32
_Ol51nnMTPPortIndex_Object = MibTableColumn
ol51nnMTPPortIndex = _Ol51nnMTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 2),
    _Ol51nnMTPPortIndex_Type()
)
ol51nnMTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPortIndex.setStatus("mandatory")


class _Ol51nnMTPPortAdminState_Type(Integer32):
    """Custom type ol51nnMTPPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMTPPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPPortAdminState_Object = MibTableColumn
ol51nnMTPPortAdminState = _Ol51nnMTPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 3),
    _Ol51nnMTPPortAdminState_Type()
)
ol51nnMTPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPortAdminState.setStatus("mandatory")
_Ol51nnMTPPortBuddySlot_Type = Integer32
_Ol51nnMTPPortBuddySlot_Object = MibTableColumn
ol51nnMTPPortBuddySlot = _Ol51nnMTPPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 4),
    _Ol51nnMTPPortBuddySlot_Type()
)
ol51nnMTPPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPortBuddySlot.setStatus("mandatory")
_Ol51nnMTPPortBuddyPort_Type = Integer32
_Ol51nnMTPPortBuddyPort_Object = MibTableColumn
ol51nnMTPPortBuddyPort = _Ol51nnMTPPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 5),
    _Ol51nnMTPPortBuddyPort_Type()
)
ol51nnMTPPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPortBuddyPort.setStatus("mandatory")


class _Ol51nnMTPPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMTPPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPPortDipAdminState_Object = MibTableColumn
ol51nnMTPPortDipAdminState = _Ol51nnMTPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 6),
    _Ol51nnMTPPortDipAdminState_Type()
)
ol51nnMTPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPortDipAdminState.setStatus("mandatory")


class _Ol51nnMTPPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPPortLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPPortLinkInteg_Object = MibTableColumn
ol51nnMTPPortLinkInteg = _Ol51nnMTPPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 7),
    _Ol51nnMTPPortLinkInteg_Type()
)
ol51nnMTPPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPortLinkInteg.setStatus("mandatory")


class _Ol51nnMTPPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPPortDipLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPPortDipLinkInteg_Object = MibTableColumn
ol51nnMTPPortDipLinkInteg = _Ol51nnMTPPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 8),
    _Ol51nnMTPPortDipLinkInteg_Type()
)
ol51nnMTPPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPortDipLinkInteg.setStatus("mandatory")


class _Ol51nnMTPPortSquelch_Type(Integer32):
    """Custom type ol51nnMTPPortSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMTPPortSquelch_Type.__name__ = "Integer32"
_Ol51nnMTPPortSquelch_Object = MibTableColumn
ol51nnMTPPortSquelch = _Ol51nnMTPPortSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 9),
    _Ol51nnMTPPortSquelch_Type()
)
ol51nnMTPPortSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPortSquelch.setStatus("mandatory")


class _Ol51nnMTPPortDipSquelch_Type(Integer32):
    """Custom type ol51nnMTPPortDipSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMTPPortDipSquelch_Type.__name__ = "Integer32"
_Ol51nnMTPPortDipSquelch_Object = MibTableColumn
ol51nnMTPPortDipSquelch = _Ol51nnMTPPortDipSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 10),
    _Ol51nnMTPPortDipSquelch_Type()
)
ol51nnMTPPortDipSquelch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPortDipSquelch.setStatus("mandatory")
_Ol51nnMBNC_ObjectIdentity = ObjectIdentity
ol51nnMBNC = _Ol51nnMBNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8)
)
_Ol51nnMBNCModTable_Object = MibTable
ol51nnMBNCModTable = _Ol51nnMBNCModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 1)
)
if mibBuilder.loadTexts:
    ol51nnMBNCModTable.setStatus("mandatory")
_Ol51nnMBNCModEntry_Object = MibTableRow
ol51nnMBNCModEntry = _Ol51nnMBNCModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 1, 1)
)
ol51nnMBNCModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMBNCModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMBNCModEntry.setStatus("mandatory")
_Ol51nnMBNCModSlotIndex_Type = Integer32
_Ol51nnMBNCModSlotIndex_Object = MibTableColumn
ol51nnMBNCModSlotIndex = _Ol51nnMBNCModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 1, 1, 1),
    _Ol51nnMBNCModSlotIndex_Type()
)
ol51nnMBNCModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCModSlotIndex.setStatus("mandatory")


class _Ol51nnMBNCModDipNetwork_Type(Integer32):
    """Custom type ol51nnMBNCModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMBNCModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMBNCModDipNetwork_Object = MibTableColumn
ol51nnMBNCModDipNetwork = _Ol51nnMBNCModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 1, 1, 2),
    _Ol51nnMBNCModDipNetwork_Type()
)
ol51nnMBNCModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCModDipNetwork.setStatus("mandatory")
_Ol51nnMBNCPortTable_Object = MibTable
ol51nnMBNCPortTable = _Ol51nnMBNCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2)
)
if mibBuilder.loadTexts:
    ol51nnMBNCPortTable.setStatus("mandatory")
_Ol51nnMBNCPortEntry_Object = MibTableRow
ol51nnMBNCPortEntry = _Ol51nnMBNCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1)
)
ol51nnMBNCPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMBNCPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMBNCPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMBNCPortEntry.setStatus("mandatory")
_Ol51nnMBNCPortSlotIndex_Type = Integer32
_Ol51nnMBNCPortSlotIndex_Object = MibTableColumn
ol51nnMBNCPortSlotIndex = _Ol51nnMBNCPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1, 1),
    _Ol51nnMBNCPortSlotIndex_Type()
)
ol51nnMBNCPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCPortSlotIndex.setStatus("mandatory")
_Ol51nnMBNCPortIndex_Type = Integer32
_Ol51nnMBNCPortIndex_Object = MibTableColumn
ol51nnMBNCPortIndex = _Ol51nnMBNCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1, 2),
    _Ol51nnMBNCPortIndex_Type()
)
ol51nnMBNCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCPortIndex.setStatus("mandatory")


class _Ol51nnMBNCPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMBNCPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMBNCPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMBNCPortDipAdminState_Object = MibTableColumn
ol51nnMBNCPortDipAdminState = _Ol51nnMBNCPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1, 3),
    _Ol51nnMBNCPortDipAdminState_Type()
)
ol51nnMBNCPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCPortDipAdminState.setStatus("mandatory")


class _Ol51nnMBNCPortDipTermination_Type(Integer32):
    """Custom type ol51nnMBNCPortDipTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-terminated", 2),
          ("terminated", 1))
    )


_Ol51nnMBNCPortDipTermination_Type.__name__ = "Integer32"
_Ol51nnMBNCPortDipTermination_Object = MibTableColumn
ol51nnMBNCPortDipTermination = _Ol51nnMBNCPortDipTermination_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1, 4),
    _Ol51nnMBNCPortDipTermination_Type()
)
ol51nnMBNCPortDipTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCPortDipTermination.setStatus("mandatory")


class _Ol51nnMBNCPortDipGround_Type(Integer32):
    """Custom type ol51nnMBNCPortDipGround based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("grounded", 1),
          ("not-grounded", 2))
    )


_Ol51nnMBNCPortDipGround_Type.__name__ = "Integer32"
_Ol51nnMBNCPortDipGround_Object = MibTableColumn
ol51nnMBNCPortDipGround = _Ol51nnMBNCPortDipGround_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1, 5),
    _Ol51nnMBNCPortDipGround_Type()
)
ol51nnMBNCPortDipGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCPortDipGround.setStatus("mandatory")
_Ol51nnBEE_ObjectIdentity = ObjectIdentity
ol51nnBEE = _Ol51nnBEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9)
)
_Ol51nnBEEModTable_Object = MibTable
ol51nnBEEModTable = _Ol51nnBEEModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 1)
)
if mibBuilder.loadTexts:
    ol51nnBEEModTable.setStatus("mandatory")
_Ol51nnBEEModEntry_Object = MibTableRow
ol51nnBEEModEntry = _Ol51nnBEEModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 1, 1)
)
ol51nnBEEModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnBEEModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnBEEModEntry.setStatus("mandatory")
_Ol51nnBEEModSlotIndex_Type = Integer32
_Ol51nnBEEModSlotIndex_Object = MibTableColumn
ol51nnBEEModSlotIndex = _Ol51nnBEEModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 1, 1, 1),
    _Ol51nnBEEModSlotIndex_Type()
)
ol51nnBEEModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEModSlotIndex.setStatus("mandatory")


class _Ol51nnBEEModStationAddr_Type(OctetString):
    """Custom type ol51nnBEEModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnBEEModStationAddr_Type.__name__ = "OctetString"
_Ol51nnBEEModStationAddr_Object = MibTableColumn
ol51nnBEEModStationAddr = _Ol51nnBEEModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 1, 1, 2),
    _Ol51nnBEEModStationAddr_Type()
)
ol51nnBEEModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEModStationAddr.setStatus("mandatory")
_Ol51nnBEEModProtocols_Type = DisplayString
_Ol51nnBEEModProtocols_Object = MibTableColumn
ol51nnBEEModProtocols = _Ol51nnBEEModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 1, 1, 3),
    _Ol51nnBEEModProtocols_Type()
)
ol51nnBEEModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEModProtocols.setStatus("mandatory")
_Ol51nnBEEPortTable_Object = MibTable
ol51nnBEEPortTable = _Ol51nnBEEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2)
)
if mibBuilder.loadTexts:
    ol51nnBEEPortTable.setStatus("mandatory")
_Ol51nnBEEPortEntry_Object = MibTableRow
ol51nnBEEPortEntry = _Ol51nnBEEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1)
)
ol51nnBEEPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnBEEPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnBEEPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnBEEPortEntry.setStatus("mandatory")
_Ol51nnBEEPortSlotIndex_Type = Integer32
_Ol51nnBEEPortSlotIndex_Object = MibTableColumn
ol51nnBEEPortSlotIndex = _Ol51nnBEEPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1, 1),
    _Ol51nnBEEPortSlotIndex_Type()
)
ol51nnBEEPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEPortSlotIndex.setStatus("mandatory")
_Ol51nnBEEPortIndex_Type = Integer32
_Ol51nnBEEPortIndex_Object = MibTableColumn
ol51nnBEEPortIndex = _Ol51nnBEEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1, 2),
    _Ol51nnBEEPortIndex_Type()
)
ol51nnBEEPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEPortIndex.setStatus("mandatory")
_Ol51nnBEEPortIpAddress_Type = IpAddress
_Ol51nnBEEPortIpAddress_Object = MibTableColumn
ol51nnBEEPortIpAddress = _Ol51nnBEEPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1, 3),
    _Ol51nnBEEPortIpAddress_Type()
)
ol51nnBEEPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEPortIpAddress.setStatus("mandatory")


class _Ol51nnBEEPortDipNetwork_Type(Integer32):
    """Custom type ol51nnBEEPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnBEEPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnBEEPortDipNetwork_Object = MibTableColumn
ol51nnBEEPortDipNetwork = _Ol51nnBEEPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1, 4),
    _Ol51nnBEEPortDipNetwork_Type()
)
ol51nnBEEPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEPortDipNetwork.setStatus("mandatory")


class _Ol51nnBEEPortDefNetwork_Type(Integer32):
    """Custom type ol51nnBEEPortDefNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnBEEPortDefNetwork_Type.__name__ = "Integer32"
_Ol51nnBEEPortDefNetwork_Object = MibTableColumn
ol51nnBEEPortDefNetwork = _Ol51nnBEEPortDefNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1, 5),
    _Ol51nnBEEPortDefNetwork_Type()
)
ol51nnBEEPortDefNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEPortDefNetwork.setStatus("mandatory")
_Ol51nnRES_ObjectIdentity = ObjectIdentity
ol51nnRES = _Ol51nnRES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10)
)
_Ol51nnRESModTable_Object = MibTable
ol51nnRESModTable = _Ol51nnRESModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 1)
)
if mibBuilder.loadTexts:
    ol51nnRESModTable.setStatus("mandatory")
_Ol51nnRESModEntry_Object = MibTableRow
ol51nnRESModEntry = _Ol51nnRESModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 1, 1)
)
ol51nnRESModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnRESModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnRESModEntry.setStatus("mandatory")
_Ol51nnRESModSlotIndex_Type = Integer32
_Ol51nnRESModSlotIndex_Object = MibTableColumn
ol51nnRESModSlotIndex = _Ol51nnRESModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 1, 1, 1),
    _Ol51nnRESModSlotIndex_Type()
)
ol51nnRESModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESModSlotIndex.setStatus("mandatory")


class _Ol51nnRESModStationAddr_Type(OctetString):
    """Custom type ol51nnRESModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnRESModStationAddr_Type.__name__ = "OctetString"
_Ol51nnRESModStationAddr_Object = MibTableColumn
ol51nnRESModStationAddr = _Ol51nnRESModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 1, 1, 2),
    _Ol51nnRESModStationAddr_Type()
)
ol51nnRESModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESModStationAddr.setStatus("mandatory")
_Ol51nnRESModProtocols_Type = DisplayString
_Ol51nnRESModProtocols_Object = MibTableColumn
ol51nnRESModProtocols = _Ol51nnRESModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 1, 1, 3),
    _Ol51nnRESModProtocols_Type()
)
ol51nnRESModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESModProtocols.setStatus("mandatory")
_Ol51nnRESPortTable_Object = MibTable
ol51nnRESPortTable = _Ol51nnRESPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2)
)
if mibBuilder.loadTexts:
    ol51nnRESPortTable.setStatus("mandatory")
_Ol51nnRESPortEntry_Object = MibTableRow
ol51nnRESPortEntry = _Ol51nnRESPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1)
)
ol51nnRESPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnRESPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnRESPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnRESPortEntry.setStatus("mandatory")
_Ol51nnRESPortSlotIndex_Type = Integer32
_Ol51nnRESPortSlotIndex_Object = MibTableColumn
ol51nnRESPortSlotIndex = _Ol51nnRESPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1, 1),
    _Ol51nnRESPortSlotIndex_Type()
)
ol51nnRESPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESPortSlotIndex.setStatus("mandatory")
_Ol51nnRESPortIndex_Type = Integer32
_Ol51nnRESPortIndex_Object = MibTableColumn
ol51nnRESPortIndex = _Ol51nnRESPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1, 2),
    _Ol51nnRESPortIndex_Type()
)
ol51nnRESPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESPortIndex.setStatus("mandatory")
_Ol51nnRESPortIpAddress_Type = IpAddress
_Ol51nnRESPortIpAddress_Object = MibTableColumn
ol51nnRESPortIpAddress = _Ol51nnRESPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1, 3),
    _Ol51nnRESPortIpAddress_Type()
)
ol51nnRESPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESPortIpAddress.setStatus("mandatory")


class _Ol51nnRESPortDipNetwork_Type(Integer32):
    """Custom type ol51nnRESPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnRESPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnRESPortDipNetwork_Object = MibTableColumn
ol51nnRESPortDipNetwork = _Ol51nnRESPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1, 4),
    _Ol51nnRESPortDipNetwork_Type()
)
ol51nnRESPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESPortDipNetwork.setStatus("mandatory")


class _Ol51nnRESPortDefNetwork_Type(Integer32):
    """Custom type ol51nnRESPortDefNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnRESPortDefNetwork_Type.__name__ = "Integer32"
_Ol51nnRESPortDefNetwork_Object = MibTableColumn
ol51nnRESPortDefNetwork = _Ol51nnRESPortDefNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1, 5),
    _Ol51nnRESPortDefNetwork_Type()
)
ol51nnRESPortDefNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESPortDefNetwork.setStatus("mandatory")
_Ol51nnREE_ObjectIdentity = ObjectIdentity
ol51nnREE = _Ol51nnREE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11)
)
_Ol51nnREEModTable_Object = MibTable
ol51nnREEModTable = _Ol51nnREEModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 1)
)
if mibBuilder.loadTexts:
    ol51nnREEModTable.setStatus("mandatory")
_Ol51nnREEModEntry_Object = MibTableRow
ol51nnREEModEntry = _Ol51nnREEModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 1, 1)
)
ol51nnREEModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnREEModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnREEModEntry.setStatus("mandatory")
_Ol51nnREEModSlotIndex_Type = Integer32
_Ol51nnREEModSlotIndex_Object = MibTableColumn
ol51nnREEModSlotIndex = _Ol51nnREEModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 1, 1, 1),
    _Ol51nnREEModSlotIndex_Type()
)
ol51nnREEModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEModSlotIndex.setStatus("mandatory")


class _Ol51nnREEModStationAddr_Type(OctetString):
    """Custom type ol51nnREEModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnREEModStationAddr_Type.__name__ = "OctetString"
_Ol51nnREEModStationAddr_Object = MibTableColumn
ol51nnREEModStationAddr = _Ol51nnREEModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 1, 1, 2),
    _Ol51nnREEModStationAddr_Type()
)
ol51nnREEModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEModStationAddr.setStatus("mandatory")
_Ol51nnREEModProtocols_Type = DisplayString
_Ol51nnREEModProtocols_Object = MibTableColumn
ol51nnREEModProtocols = _Ol51nnREEModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 1, 1, 3),
    _Ol51nnREEModProtocols_Type()
)
ol51nnREEModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEModProtocols.setStatus("mandatory")
_Ol51nnREEPortTable_Object = MibTable
ol51nnREEPortTable = _Ol51nnREEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2)
)
if mibBuilder.loadTexts:
    ol51nnREEPortTable.setStatus("mandatory")
_Ol51nnREEPortEntry_Object = MibTableRow
ol51nnREEPortEntry = _Ol51nnREEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1)
)
ol51nnREEPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnREEPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnREEPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnREEPortEntry.setStatus("mandatory")
_Ol51nnREEPortSlotIndex_Type = Integer32
_Ol51nnREEPortSlotIndex_Object = MibTableColumn
ol51nnREEPortSlotIndex = _Ol51nnREEPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1, 1),
    _Ol51nnREEPortSlotIndex_Type()
)
ol51nnREEPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEPortSlotIndex.setStatus("mandatory")
_Ol51nnREEPortIndex_Type = Integer32
_Ol51nnREEPortIndex_Object = MibTableColumn
ol51nnREEPortIndex = _Ol51nnREEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1, 2),
    _Ol51nnREEPortIndex_Type()
)
ol51nnREEPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEPortIndex.setStatus("mandatory")
_Ol51nnREEPortIpAddress_Type = IpAddress
_Ol51nnREEPortIpAddress_Object = MibTableColumn
ol51nnREEPortIpAddress = _Ol51nnREEPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1, 3),
    _Ol51nnREEPortIpAddress_Type()
)
ol51nnREEPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEPortIpAddress.setStatus("mandatory")


class _Ol51nnREEPortDipNetwork_Type(Integer32):
    """Custom type ol51nnREEPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnREEPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnREEPortDipNetwork_Object = MibTableColumn
ol51nnREEPortDipNetwork = _Ol51nnREEPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1, 4),
    _Ol51nnREEPortDipNetwork_Type()
)
ol51nnREEPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEPortDipNetwork.setStatus("mandatory")


class _Ol51nnREEPortDefNetwork_Type(Integer32):
    """Custom type ol51nnREEPortDefNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnREEPortDefNetwork_Type.__name__ = "Integer32"
_Ol51nnREEPortDefNetwork_Object = MibTableColumn
ol51nnREEPortDefNetwork = _Ol51nnREEPortDefNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1, 5),
    _Ol51nnREEPortDefNetwork_Type()
)
ol51nnREEPortDefNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEPortDefNetwork.setStatus("mandatory")
_Ol51nnMAUIF_ObjectIdentity = ObjectIdentity
ol51nnMAUIF = _Ol51nnMAUIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12)
)
_Ol51nnMAUIFModTable_Object = MibTable
ol51nnMAUIFModTable = _Ol51nnMAUIFModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 1)
)
if mibBuilder.loadTexts:
    ol51nnMAUIFModTable.setStatus("mandatory")
_Ol51nnMAUIFModEntry_Object = MibTableRow
ol51nnMAUIFModEntry = _Ol51nnMAUIFModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 1, 1)
)
ol51nnMAUIFModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMAUIFModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMAUIFModEntry.setStatus("mandatory")
_Ol51nnMAUIFModSlotIndex_Type = Integer32
_Ol51nnMAUIFModSlotIndex_Object = MibTableColumn
ol51nnMAUIFModSlotIndex = _Ol51nnMAUIFModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 1, 1, 1),
    _Ol51nnMAUIFModSlotIndex_Type()
)
ol51nnMAUIFModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIFModSlotIndex.setStatus("mandatory")
_Ol51nnMAUIFPortTable_Object = MibTable
ol51nnMAUIFPortTable = _Ol51nnMAUIFPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2)
)
if mibBuilder.loadTexts:
    ol51nnMAUIFPortTable.setStatus("mandatory")
_Ol51nnMAUIFPortEntry_Object = MibTableRow
ol51nnMAUIFPortEntry = _Ol51nnMAUIFPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1)
)
ol51nnMAUIFPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMAUIFPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMAUIFPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMAUIFPortEntry.setStatus("mandatory")
_Ol51nnMAUIFPortSlotIndex_Type = Integer32
_Ol51nnMAUIFPortSlotIndex_Object = MibTableColumn
ol51nnMAUIFPortSlotIndex = _Ol51nnMAUIFPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 1),
    _Ol51nnMAUIFPortSlotIndex_Type()
)
ol51nnMAUIFPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortSlotIndex.setStatus("mandatory")
_Ol51nnMAUIFPortIndex_Type = Integer32
_Ol51nnMAUIFPortIndex_Object = MibTableColumn
ol51nnMAUIFPortIndex = _Ol51nnMAUIFPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 2),
    _Ol51nnMAUIFPortIndex_Type()
)
ol51nnMAUIFPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortIndex.setStatus("mandatory")


class _Ol51nnMAUIFPortAdminState_Type(Integer32):
    """Custom type ol51nnMAUIFPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMAUIFPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMAUIFPortAdminState_Object = MibTableColumn
ol51nnMAUIFPortAdminState = _Ol51nnMAUIFPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 3),
    _Ol51nnMAUIFPortAdminState_Type()
)
ol51nnMAUIFPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortAdminState.setStatus("mandatory")
_Ol51nnMAUIFPortBuddySlot_Type = Integer32
_Ol51nnMAUIFPortBuddySlot_Object = MibTableColumn
ol51nnMAUIFPortBuddySlot = _Ol51nnMAUIFPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 4),
    _Ol51nnMAUIFPortBuddySlot_Type()
)
ol51nnMAUIFPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortBuddySlot.setStatus("mandatory")
_Ol51nnMAUIFPortBuddyPort_Type = Integer32
_Ol51nnMAUIFPortBuddyPort_Object = MibTableColumn
ol51nnMAUIFPortBuddyPort = _Ol51nnMAUIFPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 5),
    _Ol51nnMAUIFPortBuddyPort_Type()
)
ol51nnMAUIFPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortBuddyPort.setStatus("mandatory")


class _Ol51nnMAUIFPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMAUIFPortDipAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMAUIFPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMAUIFPortDipAdminState_Object = MibTableColumn
ol51nnMAUIFPortDipAdminState = _Ol51nnMAUIFPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 6),
    _Ol51nnMAUIFPortDipAdminState_Type()
)
ol51nnMAUIFPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortDipAdminState.setStatus("mandatory")


class _Ol51nnMAUIFPortDipNetwork_Type(Integer32):
    """Custom type ol51nnMAUIFPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMAUIFPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMAUIFPortDipNetwork_Object = MibTableColumn
ol51nnMAUIFPortDipNetwork = _Ol51nnMAUIFPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 7),
    _Ol51nnMAUIFPortDipNetwork_Type()
)
ol51nnMAUIFPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortDipNetwork.setStatus("mandatory")
_Ol51nnMAUIM_ObjectIdentity = ObjectIdentity
ol51nnMAUIM = _Ol51nnMAUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13)
)
_Ol51nnMAUIMModTable_Object = MibTable
ol51nnMAUIMModTable = _Ol51nnMAUIMModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 1)
)
if mibBuilder.loadTexts:
    ol51nnMAUIMModTable.setStatus("mandatory")
_Ol51nnMAUIMModEntry_Object = MibTableRow
ol51nnMAUIMModEntry = _Ol51nnMAUIMModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 1, 1)
)
ol51nnMAUIMModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMAUIMModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMAUIMModEntry.setStatus("mandatory")
_Ol51nnMAUIMModSlotIndex_Type = Integer32
_Ol51nnMAUIMModSlotIndex_Object = MibTableColumn
ol51nnMAUIMModSlotIndex = _Ol51nnMAUIMModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 1, 1, 1),
    _Ol51nnMAUIMModSlotIndex_Type()
)
ol51nnMAUIMModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMModSlotIndex.setStatus("mandatory")
_Ol51nnMAUIMPortTable_Object = MibTable
ol51nnMAUIMPortTable = _Ol51nnMAUIMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2)
)
if mibBuilder.loadTexts:
    ol51nnMAUIMPortTable.setStatus("mandatory")
_Ol51nnMAUIMPortEntry_Object = MibTableRow
ol51nnMAUIMPortEntry = _Ol51nnMAUIMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1)
)
ol51nnMAUIMPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMAUIMPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMAUIMPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMAUIMPortEntry.setStatus("mandatory")
_Ol51nnMAUIMPortSlotIndex_Type = Integer32
_Ol51nnMAUIMPortSlotIndex_Object = MibTableColumn
ol51nnMAUIMPortSlotIndex = _Ol51nnMAUIMPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 1),
    _Ol51nnMAUIMPortSlotIndex_Type()
)
ol51nnMAUIMPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortSlotIndex.setStatus("mandatory")
_Ol51nnMAUIMPortIndex_Type = Integer32
_Ol51nnMAUIMPortIndex_Object = MibTableColumn
ol51nnMAUIMPortIndex = _Ol51nnMAUIMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 2),
    _Ol51nnMAUIMPortIndex_Type()
)
ol51nnMAUIMPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortIndex.setStatus("mandatory")


class _Ol51nnMAUIMPortAdminState_Type(Integer32):
    """Custom type ol51nnMAUIMPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMAUIMPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortAdminState_Object = MibTableColumn
ol51nnMAUIMPortAdminState = _Ol51nnMAUIMPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 3),
    _Ol51nnMAUIMPortAdminState_Type()
)
ol51nnMAUIMPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortAdminState.setStatus("mandatory")
_Ol51nnMAUIMPortBuddySlot_Type = Integer32
_Ol51nnMAUIMPortBuddySlot_Object = MibTableColumn
ol51nnMAUIMPortBuddySlot = _Ol51nnMAUIMPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 4),
    _Ol51nnMAUIMPortBuddySlot_Type()
)
ol51nnMAUIMPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortBuddySlot.setStatus("mandatory")
_Ol51nnMAUIMPortBuddyPort_Type = Integer32
_Ol51nnMAUIMPortBuddyPort_Object = MibTableColumn
ol51nnMAUIMPortBuddyPort = _Ol51nnMAUIMPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 5),
    _Ol51nnMAUIMPortBuddyPort_Type()
)
ol51nnMAUIMPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortBuddyPort.setStatus("mandatory")


class _Ol51nnMAUIMPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMAUIMPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMAUIMPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortDipAdminState_Object = MibTableColumn
ol51nnMAUIMPortDipAdminState = _Ol51nnMAUIMPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 6),
    _Ol51nnMAUIMPortDipAdminState_Type()
)
ol51nnMAUIMPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortDipAdminState.setStatus("mandatory")


class _Ol51nnMAUIMPortDipNetwork_Type(Integer32):
    """Custom type ol51nnMAUIMPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMAUIMPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortDipNetwork_Object = MibTableColumn
ol51nnMAUIMPortDipNetwork = _Ol51nnMAUIMPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 7),
    _Ol51nnMAUIMPortDipNetwork_Type()
)
ol51nnMAUIMPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortDipNetwork.setStatus("mandatory")


class _Ol51nnMAUIMPortSQETest_Type(Integer32):
    """Custom type ol51nnMAUIMPortSQETest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMAUIMPortSQETest_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortSQETest_Object = MibTableColumn
ol51nnMAUIMPortSQETest = _Ol51nnMAUIMPortSQETest_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 8),
    _Ol51nnMAUIMPortSQETest_Type()
)
ol51nnMAUIMPortSQETest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortSQETest.setStatus("mandatory")


class _Ol51nnMAUIMPortDipSQETest_Type(Integer32):
    """Custom type ol51nnMAUIMPortDipSQETest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMAUIMPortDipSQETest_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortDipSQETest_Object = MibTableColumn
ol51nnMAUIMPortDipSQETest = _Ol51nnMAUIMPortDipSQETest_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 9),
    _Ol51nnMAUIMPortDipSQETest_Type()
)
ol51nnMAUIMPortDipSQETest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortDipSQETest.setStatus("mandatory")


class _Ol51nnMAUIMPortCollision_Type(Integer32):
    """Custom type ol51nnMAUIMPortCollision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("normal", 1))
    )


_Ol51nnMAUIMPortCollision_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortCollision_Object = MibTableColumn
ol51nnMAUIMPortCollision = _Ol51nnMAUIMPortCollision_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 10),
    _Ol51nnMAUIMPortCollision_Type()
)
ol51nnMAUIMPortCollision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortCollision.setStatus("mandatory")


class _Ol51nnMAUIMPortDipCollision_Type(Integer32):
    """Custom type ol51nnMAUIMPortDipCollision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("normal", 1))
    )


_Ol51nnMAUIMPortDipCollision_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortDipCollision_Object = MibTableColumn
ol51nnMAUIMPortDipCollision = _Ol51nnMAUIMPortDipCollision_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 11),
    _Ol51nnMAUIMPortDipCollision_Type()
)
ol51nnMAUIMPortDipCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortDipCollision.setStatus("mandatory")


class _Ol51nnMAUIMPortHalfStep_Type(Integer32):
    """Custom type ol51nnMAUIMPortHalfStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMAUIMPortHalfStep_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortHalfStep_Object = MibTableColumn
ol51nnMAUIMPortHalfStep = _Ol51nnMAUIMPortHalfStep_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 12),
    _Ol51nnMAUIMPortHalfStep_Type()
)
ol51nnMAUIMPortHalfStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortHalfStep.setStatus("mandatory")


class _Ol51nnMAUIMPortDipHalfStep_Type(Integer32):
    """Custom type ol51nnMAUIMPortDipHalfStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMAUIMPortDipHalfStep_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortDipHalfStep_Object = MibTableColumn
ol51nnMAUIMPortDipHalfStep = _Ol51nnMAUIMPortDipHalfStep_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 13),
    _Ol51nnMAUIMPortDipHalfStep_Type()
)
ol51nnMAUIMPortDipHalfStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortDipHalfStep.setStatus("mandatory")
_Ol5208MTP_ObjectIdentity = ObjectIdentity
ol5208MTP = _Ol5208MTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14)
)
_Ol5208MTPModTable_Object = MibTable
ol5208MTPModTable = _Ol5208MTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1)
)
if mibBuilder.loadTexts:
    ol5208MTPModTable.setStatus("mandatory")
_Ol5208MTPModEntry_Object = MibTableRow
ol5208MTPModEntry = _Ol5208MTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1, 1)
)
ol5208MTPModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol5208MTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol5208MTPModEntry.setStatus("mandatory")
_Ol5208MTPModSlotIndex_Type = Integer32
_Ol5208MTPModSlotIndex_Object = MibTableColumn
ol5208MTPModSlotIndex = _Ol5208MTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1, 1, 1),
    _Ol5208MTPModSlotIndex_Type()
)
ol5208MTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPModSlotIndex.setStatus("mandatory")


class _Ol5208MTPModBypsAdminState_Type(Integer32):
    """Custom type ol5208MTPModBypsAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("insert", 1))
    )


_Ol5208MTPModBypsAdminState_Type.__name__ = "Integer32"
_Ol5208MTPModBypsAdminState_Object = MibTableColumn
ol5208MTPModBypsAdminState = _Ol5208MTPModBypsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1, 1, 2),
    _Ol5208MTPModBypsAdminState_Type()
)
ol5208MTPModBypsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol5208MTPModBypsAdminState.setStatus("mandatory")


class _Ol5208MTPModBypsOperState_Type(Integer32):
    """Custom type ol5208MTPModBypsOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("insert", 1))
    )


_Ol5208MTPModBypsOperState_Type.__name__ = "Integer32"
_Ol5208MTPModBypsOperState_Object = MibTableColumn
ol5208MTPModBypsOperState = _Ol5208MTPModBypsOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1, 1, 3),
    _Ol5208MTPModBypsOperState_Type()
)
ol5208MTPModBypsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPModBypsOperState.setStatus("mandatory")


class _Ol5208MTPModDipCableImp_Type(Integer32):
    """Custom type ol5208MTPModDipCableImp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ohm100", 1),
          ("ohm150", 2))
    )


_Ol5208MTPModDipCableImp_Type.__name__ = "Integer32"
_Ol5208MTPModDipCableImp_Object = MibTableColumn
ol5208MTPModDipCableImp = _Ol5208MTPModDipCableImp_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1, 1, 4),
    _Ol5208MTPModDipCableImp_Type()
)
ol5208MTPModDipCableImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPModDipCableImp.setStatus("mandatory")
_Ol5208MTPPortTable_Object = MibTable
ol5208MTPPortTable = _Ol5208MTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2)
)
if mibBuilder.loadTexts:
    ol5208MTPPortTable.setStatus("mandatory")
_Ol5208MTPPortEntry_Object = MibTableRow
ol5208MTPPortEntry = _Ol5208MTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2, 1)
)
ol5208MTPPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol5208MTPPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol5208MTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol5208MTPPortEntry.setStatus("mandatory")
_Ol5208MTPPortSlotIndex_Type = Integer32
_Ol5208MTPPortSlotIndex_Object = MibTableColumn
ol5208MTPPortSlotIndex = _Ol5208MTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2, 1, 1),
    _Ol5208MTPPortSlotIndex_Type()
)
ol5208MTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPPortSlotIndex.setStatus("mandatory")
_Ol5208MTPPortIndex_Type = Integer32
_Ol5208MTPPortIndex_Object = MibTableColumn
ol5208MTPPortIndex = _Ol5208MTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2, 1, 2),
    _Ol5208MTPPortIndex_Type()
)
ol5208MTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPPortIndex.setStatus("mandatory")


class _Ol5208MTPPortDipAdminState_Type(Integer32):
    """Custom type ol5208MTPPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol5208MTPPortDipAdminState_Type.__name__ = "Integer32"
_Ol5208MTPPortDipAdminState_Object = MibTableColumn
ol5208MTPPortDipAdminState = _Ol5208MTPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2, 1, 3),
    _Ol5208MTPPortDipAdminState_Type()
)
ol5208MTPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPPortDipAdminState.setStatus("mandatory")


class _Ol5208MTPPortStationType_Type(Integer32):
    """Custom type ol5208MTPPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac-not-present", 2),
          ("mac-present", 1))
    )


_Ol5208MTPPortStationType_Type.__name__ = "Integer32"
_Ol5208MTPPortStationType_Object = MibTableColumn
ol5208MTPPortStationType = _Ol5208MTPPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2, 1, 4),
    _Ol5208MTPPortStationType_Type()
)
ol5208MTPPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol5208MTPPortStationType.setStatus("mandatory")
_Ol5208MTPTrunkTable_Object = MibTable
ol5208MTPTrunkTable = _Ol5208MTPTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3)
)
if mibBuilder.loadTexts:
    ol5208MTPTrunkTable.setStatus("mandatory")
_Ol5208MTPTrunkEntry_Object = MibTableRow
ol5208MTPTrunkEntry = _Ol5208MTPTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1)
)
ol5208MTPTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol5208MTPTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol5208MTPTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol5208MTPTrunkEntry.setStatus("mandatory")
_Ol5208MTPTrunkSlotIndex_Type = Integer32
_Ol5208MTPTrunkSlotIndex_Object = MibTableColumn
ol5208MTPTrunkSlotIndex = _Ol5208MTPTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 1),
    _Ol5208MTPTrunkSlotIndex_Type()
)
ol5208MTPTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPTrunkSlotIndex.setStatus("mandatory")
_Ol5208MTPTrunkIndex_Type = Integer32
_Ol5208MTPTrunkIndex_Object = MibTableColumn
ol5208MTPTrunkIndex = _Ol5208MTPTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 2),
    _Ol5208MTPTrunkIndex_Type()
)
ol5208MTPTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPTrunkIndex.setStatus("mandatory")


class _Ol5208MTPTrunkDipAdminState_Type(Integer32):
    """Custom type ol5208MTPTrunkDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol5208MTPTrunkDipAdminState_Type.__name__ = "Integer32"
_Ol5208MTPTrunkDipAdminState_Object = MibTableColumn
ol5208MTPTrunkDipAdminState = _Ol5208MTPTrunkDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 3),
    _Ol5208MTPTrunkDipAdminState_Type()
)
ol5208MTPTrunkDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPTrunkDipAdminState.setStatus("mandatory")


class _Ol5208MTPTrunkCableMon_Type(Integer32):
    """Custom type ol5208MTPTrunkCableMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol5208MTPTrunkCableMon_Type.__name__ = "Integer32"
_Ol5208MTPTrunkCableMon_Object = MibTableColumn
ol5208MTPTrunkCableMon = _Ol5208MTPTrunkCableMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 4),
    _Ol5208MTPTrunkCableMon_Type()
)
ol5208MTPTrunkCableMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol5208MTPTrunkCableMon.setStatus("mandatory")


class _Ol5208MTPTrunkDipCableMon_Type(Integer32):
    """Custom type ol5208MTPTrunkDipCableMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol5208MTPTrunkDipCableMon_Type.__name__ = "Integer32"
_Ol5208MTPTrunkDipCableMon_Object = MibTableColumn
ol5208MTPTrunkDipCableMon = _Ol5208MTPTrunkDipCableMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 5),
    _Ol5208MTPTrunkDipCableMon_Type()
)
ol5208MTPTrunkDipCableMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPTrunkDipCableMon.setStatus("mandatory")


class _Ol5208MTPTrunkNetMapState_Type(Integer32):
    """Custom type ol5208MTPTrunkNetMapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("notApplicable", 1))
    )


_Ol5208MTPTrunkNetMapState_Type.__name__ = "Integer32"
_Ol5208MTPTrunkNetMapState_Object = MibTableColumn
ol5208MTPTrunkNetMapState = _Ol5208MTPTrunkNetMapState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 6),
    _Ol5208MTPTrunkNetMapState_Type()
)
ol5208MTPTrunkNetMapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol5208MTPTrunkNetMapState.setStatus("mandatory")


class _Ol5208MTPTrunkExtBcnRecovery_Type(Integer32):
    """Custom type ol5208MTPTrunkExtBcnRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exists", 1),
          ("nonExists", 2),
          ("notApplicable", 3))
    )


_Ol5208MTPTrunkExtBcnRecovery_Type.__name__ = "Integer32"
_Ol5208MTPTrunkExtBcnRecovery_Object = MibTableColumn
ol5208MTPTrunkExtBcnRecovery = _Ol5208MTPTrunkExtBcnRecovery_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 7),
    _Ol5208MTPTrunkExtBcnRecovery_Type()
)
ol5208MTPTrunkExtBcnRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol5208MTPTrunkExtBcnRecovery.setStatus("mandatory")
_Ol51nnMFP_ObjectIdentity = ObjectIdentity
ol51nnMFP = _Ol51nnMFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15)
)
_Ol51nnMFPModTable_Object = MibTable
ol51nnMFPModTable = _Ol51nnMFPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 1)
)
if mibBuilder.loadTexts:
    ol51nnMFPModTable.setStatus("mandatory")
_Ol51nnMFPModEntry_Object = MibTableRow
ol51nnMFPModEntry = _Ol51nnMFPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 1, 1)
)
ol51nnMFPModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMFPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFPModEntry.setStatus("mandatory")
_Ol51nnMFPModSlotIndex_Type = Integer32
_Ol51nnMFPModSlotIndex_Object = MibTableColumn
ol51nnMFPModSlotIndex = _Ol51nnMFPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 1, 1, 1),
    _Ol51nnMFPModSlotIndex_Type()
)
ol51nnMFPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPModSlotIndex.setStatus("mandatory")
_Ol51nnMFPPortTable_Object = MibTable
ol51nnMFPPortTable = _Ol51nnMFPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2)
)
if mibBuilder.loadTexts:
    ol51nnMFPPortTable.setStatus("mandatory")
_Ol51nnMFPPortEntry_Object = MibTableRow
ol51nnMFPPortEntry = _Ol51nnMFPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1)
)
ol51nnMFPPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMFPPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMFPPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFPPortEntry.setStatus("mandatory")
_Ol51nnMFPPortSlotIndex_Type = Integer32
_Ol51nnMFPPortSlotIndex_Object = MibTableColumn
ol51nnMFPPortSlotIndex = _Ol51nnMFPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 1),
    _Ol51nnMFPPortSlotIndex_Type()
)
ol51nnMFPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortSlotIndex.setStatus("mandatory")
_Ol51nnMFPPortIndex_Type = Integer32
_Ol51nnMFPPortIndex_Object = MibTableColumn
ol51nnMFPPortIndex = _Ol51nnMFPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 2),
    _Ol51nnMFPPortIndex_Type()
)
ol51nnMFPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortIndex.setStatus("mandatory")


class _Ol51nnMFPPortAdminState_Type(Integer32):
    """Custom type ol51nnMFPPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFPPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMFPPortAdminState_Object = MibTableColumn
ol51nnMFPPortAdminState = _Ol51nnMFPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 3),
    _Ol51nnMFPPortAdminState_Type()
)
ol51nnMFPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFPPortAdminState.setStatus("mandatory")
_Ol51nnMFPPortBuddySlot_Type = Integer32
_Ol51nnMFPPortBuddySlot_Object = MibTableColumn
ol51nnMFPPortBuddySlot = _Ol51nnMFPPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 4),
    _Ol51nnMFPPortBuddySlot_Type()
)
ol51nnMFPPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFPPortBuddySlot.setStatus("mandatory")
_Ol51nnMFPPortBuddyPort_Type = Integer32
_Ol51nnMFPPortBuddyPort_Object = MibTableColumn
ol51nnMFPPortBuddyPort = _Ol51nnMFPPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 5),
    _Ol51nnMFPPortBuddyPort_Type()
)
ol51nnMFPPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFPPortBuddyPort.setStatus("mandatory")


class _Ol51nnMFPPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMFPPortDipAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFPPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMFPPortDipAdminState_Object = MibTableColumn
ol51nnMFPPortDipAdminState = _Ol51nnMFPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 6),
    _Ol51nnMFPPortDipAdminState_Type()
)
ol51nnMFPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortDipAdminState.setStatus("mandatory")


class _Ol51nnMFPPortDipNetwork_Type(Integer32):
    """Custom type ol51nnMFPPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMFPPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMFPPortDipNetwork_Object = MibTableColumn
ol51nnMFPPortDipNetwork = _Ol51nnMFPPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 7),
    _Ol51nnMFPPortDipNetwork_Type()
)
ol51nnMFPPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortDipNetwork.setStatus("mandatory")


class _Ol51nnMFPPortLLW_Type(Integer32):
    """Custom type ol51nnMFPPortLLW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFPPortLLW_Type.__name__ = "Integer32"
_Ol51nnMFPPortLLW_Object = MibTableColumn
ol51nnMFPPortLLW = _Ol51nnMFPPortLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 8),
    _Ol51nnMFPPortLLW_Type()
)
ol51nnMFPPortLLW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFPPortLLW.setStatus("mandatory")


class _Ol51nnMFPPortDipLLW_Type(Integer32):
    """Custom type ol51nnMFPPortDipLLW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFPPortDipLLW_Type.__name__ = "Integer32"
_Ol51nnMFPPortDipLLW_Object = MibTableColumn
ol51nnMFPPortDipLLW = _Ol51nnMFPPortDipLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 9),
    _Ol51nnMFPPortDipLLW_Type()
)
ol51nnMFPPortDipLLW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortDipLLW.setStatus("mandatory")


class _Ol51nnMFPPortHipwr_Type(Integer32):
    """Custom type ol51nnMFPPortHipwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFPPortHipwr_Type.__name__ = "Integer32"
_Ol51nnMFPPortHipwr_Object = MibTableColumn
ol51nnMFPPortHipwr = _Ol51nnMFPPortHipwr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 10),
    _Ol51nnMFPPortHipwr_Type()
)
ol51nnMFPPortHipwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFPPortHipwr.setStatus("mandatory")


class _Ol51nnMFPPortDipHipwr_Type(Integer32):
    """Custom type ol51nnMFPPortDipHipwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFPPortDipHipwr_Type.__name__ = "Integer32"
_Ol51nnMFPPortDipHipwr_Object = MibTableColumn
ol51nnMFPPortDipHipwr = _Ol51nnMFPPortDipHipwr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 11),
    _Ol51nnMFPPortDipHipwr_Type()
)
ol51nnMFPPortDipHipwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortDipHipwr.setStatus("mandatory")
_Ol51nnMFBP_ObjectIdentity = ObjectIdentity
ol51nnMFBP = _Ol51nnMFBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16)
)
_Ol51nnMFBPModTable_Object = MibTable
ol51nnMFBPModTable = _Ol51nnMFBPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 1)
)
if mibBuilder.loadTexts:
    ol51nnMFBPModTable.setStatus("mandatory")
_Ol51nnMFBPModEntry_Object = MibTableRow
ol51nnMFBPModEntry = _Ol51nnMFBPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 1, 1)
)
ol51nnMFBPModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMFBPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFBPModEntry.setStatus("mandatory")
_Ol51nnMFBPModSlotIndex_Type = Integer32
_Ol51nnMFBPModSlotIndex_Object = MibTableColumn
ol51nnMFBPModSlotIndex = _Ol51nnMFBPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 1, 1, 1),
    _Ol51nnMFBPModSlotIndex_Type()
)
ol51nnMFBPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPModSlotIndex.setStatus("mandatory")
_Ol51nnMFBPPortTable_Object = MibTable
ol51nnMFBPPortTable = _Ol51nnMFBPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2)
)
if mibBuilder.loadTexts:
    ol51nnMFBPPortTable.setStatus("mandatory")
_Ol51nnMFBPPortEntry_Object = MibTableRow
ol51nnMFBPPortEntry = _Ol51nnMFBPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1)
)
ol51nnMFBPPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMFBPPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMFBPPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFBPPortEntry.setStatus("mandatory")
_Ol51nnMFBPPortSlotIndex_Type = Integer32
_Ol51nnMFBPPortSlotIndex_Object = MibTableColumn
ol51nnMFBPPortSlotIndex = _Ol51nnMFBPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 1),
    _Ol51nnMFBPPortSlotIndex_Type()
)
ol51nnMFBPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortSlotIndex.setStatus("mandatory")
_Ol51nnMFBPPortIndex_Type = Integer32
_Ol51nnMFBPPortIndex_Object = MibTableColumn
ol51nnMFBPPortIndex = _Ol51nnMFBPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 2),
    _Ol51nnMFBPPortIndex_Type()
)
ol51nnMFBPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortIndex.setStatus("mandatory")


class _Ol51nnMFBPPortAdminState_Type(Integer32):
    """Custom type ol51nnMFBPPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFBPPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMFBPPortAdminState_Object = MibTableColumn
ol51nnMFBPPortAdminState = _Ol51nnMFBPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 3),
    _Ol51nnMFBPPortAdminState_Type()
)
ol51nnMFBPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPPortAdminState.setStatus("mandatory")
_Ol51nnMFBPPortBuddySlot_Type = Integer32
_Ol51nnMFBPPortBuddySlot_Object = MibTableColumn
ol51nnMFBPPortBuddySlot = _Ol51nnMFBPPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 4),
    _Ol51nnMFBPPortBuddySlot_Type()
)
ol51nnMFBPPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPPortBuddySlot.setStatus("mandatory")
_Ol51nnMFBPPortBuddyPort_Type = Integer32
_Ol51nnMFBPPortBuddyPort_Object = MibTableColumn
ol51nnMFBPPortBuddyPort = _Ol51nnMFBPPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 5),
    _Ol51nnMFBPPortBuddyPort_Type()
)
ol51nnMFBPPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPPortBuddyPort.setStatus("mandatory")


class _Ol51nnMFBPPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMFBPPortDipAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFBPPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMFBPPortDipAdminState_Object = MibTableColumn
ol51nnMFBPPortDipAdminState = _Ol51nnMFBPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 6),
    _Ol51nnMFBPPortDipAdminState_Type()
)
ol51nnMFBPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortDipAdminState.setStatus("mandatory")


class _Ol51nnMFBPPortDipNetwork_Type(Integer32):
    """Custom type ol51nnMFBPPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMFBPPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMFBPPortDipNetwork_Object = MibTableColumn
ol51nnMFBPPortDipNetwork = _Ol51nnMFBPPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 7),
    _Ol51nnMFBPPortDipNetwork_Type()
)
ol51nnMFBPPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortDipNetwork.setStatus("mandatory")


class _Ol51nnMFBPPortLLW_Type(Integer32):
    """Custom type ol51nnMFBPPortLLW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFBPPortLLW_Type.__name__ = "Integer32"
_Ol51nnMFBPPortLLW_Object = MibTableColumn
ol51nnMFBPPortLLW = _Ol51nnMFBPPortLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 8),
    _Ol51nnMFBPPortLLW_Type()
)
ol51nnMFBPPortLLW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPPortLLW.setStatus("mandatory")


class _Ol51nnMFBPPortDipLLW_Type(Integer32):
    """Custom type ol51nnMFBPPortDipLLW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFBPPortDipLLW_Type.__name__ = "Integer32"
_Ol51nnMFBPPortDipLLW_Object = MibTableColumn
ol51nnMFBPPortDipLLW = _Ol51nnMFBPPortDipLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 9),
    _Ol51nnMFBPPortDipLLW_Type()
)
ol51nnMFBPPortDipLLW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortDipLLW.setStatus("mandatory")


class _Ol51nnMFBPPortHipwr_Type(Integer32):
    """Custom type ol51nnMFBPPortHipwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFBPPortHipwr_Type.__name__ = "Integer32"
_Ol51nnMFBPPortHipwr_Object = MibTableColumn
ol51nnMFBPPortHipwr = _Ol51nnMFBPPortHipwr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 10),
    _Ol51nnMFBPPortHipwr_Type()
)
ol51nnMFBPPortHipwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPPortHipwr.setStatus("mandatory")


class _Ol51nnMFBPPortDipHipwr_Type(Integer32):
    """Custom type ol51nnMFBPPortDipHipwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFBPPortDipHipwr_Type.__name__ = "Integer32"
_Ol51nnMFBPPortDipHipwr_Object = MibTableColumn
ol51nnMFBPPortDipHipwr = _Ol51nnMFBPPortDipHipwr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 11),
    _Ol51nnMFBPPortDipHipwr_Type()
)
ol51nnMFBPPortDipHipwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortDipHipwr.setStatus("mandatory")
_Ol51nnMTPL_ObjectIdentity = ObjectIdentity
ol51nnMTPL = _Ol51nnMTPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17)
)
_Ol51nnMTPLModTable_Object = MibTable
ol51nnMTPLModTable = _Ol51nnMTPLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTPLModTable.setStatus("mandatory")
_Ol51nnMTPLModEntry_Object = MibTableRow
ol51nnMTPLModEntry = _Ol51nnMTPLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 1, 1)
)
ol51nnMTPLModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTPLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPLModEntry.setStatus("mandatory")
_Ol51nnMTPLModSlotIndex_Type = Integer32
_Ol51nnMTPLModSlotIndex_Object = MibTableColumn
ol51nnMTPLModSlotIndex = _Ol51nnMTPLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 1, 1, 1),
    _Ol51nnMTPLModSlotIndex_Type()
)
ol51nnMTPLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLModSlotIndex.setStatus("mandatory")


class _Ol51nnMTPLModDipNetwork_Type(Integer32):
    """Custom type ol51nnMTPLModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMTPLModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPLModDipNetwork_Object = MibTableColumn
ol51nnMTPLModDipNetwork = _Ol51nnMTPLModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 1, 1, 2),
    _Ol51nnMTPLModDipNetwork_Type()
)
ol51nnMTPLModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLModDipNetwork.setStatus("mandatory")
_Ol51nnMTPLPortTable_Object = MibTable
ol51nnMTPLPortTable = _Ol51nnMTPLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTPLPortTable.setStatus("mandatory")
_Ol51nnMTPLPortEntry_Object = MibTableRow
ol51nnMTPLPortEntry = _Ol51nnMTPLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1)
)
ol51nnMTPLPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTPLPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMTPLPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPLPortEntry.setStatus("mandatory")
_Ol51nnMTPLPortSlotIndex_Type = Integer32
_Ol51nnMTPLPortSlotIndex_Object = MibTableColumn
ol51nnMTPLPortSlotIndex = _Ol51nnMTPLPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 1),
    _Ol51nnMTPLPortSlotIndex_Type()
)
ol51nnMTPLPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLPortSlotIndex.setStatus("mandatory")
_Ol51nnMTPLPortIndex_Type = Integer32
_Ol51nnMTPLPortIndex_Object = MibTableColumn
ol51nnMTPLPortIndex = _Ol51nnMTPLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 2),
    _Ol51nnMTPLPortIndex_Type()
)
ol51nnMTPLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLPortIndex.setStatus("mandatory")


class _Ol51nnMTPLPortAdminState_Type(Integer32):
    """Custom type ol51nnMTPLPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("remote-diagnostics", 8))
    )


_Ol51nnMTPLPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPLPortAdminState_Object = MibTableColumn
ol51nnMTPLPortAdminState = _Ol51nnMTPLPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 3),
    _Ol51nnMTPLPortAdminState_Type()
)
ol51nnMTPLPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortAdminState.setStatus("mandatory")
_Ol51nnMTPLPortBuddySlot_Type = Integer32
_Ol51nnMTPLPortBuddySlot_Object = MibTableColumn
ol51nnMTPLPortBuddySlot = _Ol51nnMTPLPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 4),
    _Ol51nnMTPLPortBuddySlot_Type()
)
ol51nnMTPLPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortBuddySlot.setStatus("mandatory")
_Ol51nnMTPLPortBuddyPort_Type = Integer32
_Ol51nnMTPLPortBuddyPort_Object = MibTableColumn
ol51nnMTPLPortBuddyPort = _Ol51nnMTPLPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 5),
    _Ol51nnMTPLPortBuddyPort_Type()
)
ol51nnMTPLPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortBuddyPort.setStatus("mandatory")


class _Ol51nnMTPLPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMTPLPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPLPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPLPortDipAdminState_Object = MibTableColumn
ol51nnMTPLPortDipAdminState = _Ol51nnMTPLPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 6),
    _Ol51nnMTPLPortDipAdminState_Type()
)
ol51nnMTPLPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLPortDipAdminState.setStatus("mandatory")


class _Ol51nnMTPLPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPLPortLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPLPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPLPortLinkInteg_Object = MibTableColumn
ol51nnMTPLPortLinkInteg = _Ol51nnMTPLPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 7),
    _Ol51nnMTPLPortLinkInteg_Type()
)
ol51nnMTPLPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortLinkInteg.setStatus("mandatory")


class _Ol51nnMTPLPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPLPortDipLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPLPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPLPortDipLinkInteg_Object = MibTableColumn
ol51nnMTPLPortDipLinkInteg = _Ol51nnMTPLPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 8),
    _Ol51nnMTPLPortDipLinkInteg_Type()
)
ol51nnMTPLPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLPortDipLinkInteg.setStatus("mandatory")


class _Ol51nnMTPLPortSquelch_Type(Integer32):
    """Custom type ol51nnMTPLPortSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMTPLPortSquelch_Type.__name__ = "Integer32"
_Ol51nnMTPLPortSquelch_Object = MibTableColumn
ol51nnMTPLPortSquelch = _Ol51nnMTPLPortSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 9),
    _Ol51nnMTPLPortSquelch_Type()
)
ol51nnMTPLPortSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortSquelch.setStatus("mandatory")


class _Ol51nnMTPLPortJabber_Type(Integer32):
    """Custom type ol51nnMTPLPortJabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPLPortJabber_Type.__name__ = "Integer32"
_Ol51nnMTPLPortJabber_Object = MibTableColumn
ol51nnMTPLPortJabber = _Ol51nnMTPLPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 10),
    _Ol51nnMTPLPortJabber_Type()
)
ol51nnMTPLPortJabber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortJabber.setStatus("mandatory")


class _Ol51nnMTPLPortDipJabber_Type(Integer32):
    """Custom type ol51nnMTPLPortDipJabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPLPortDipJabber_Type.__name__ = "Integer32"
_Ol51nnMTPLPortDipJabber_Object = MibTableColumn
ol51nnMTPLPortDipJabber = _Ol51nnMTPLPortDipJabber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 11),
    _Ol51nnMTPLPortDipJabber_Type()
)
ol51nnMTPLPortDipJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLPortDipJabber.setStatus("mandatory")
_Ol51nnMTPPL_ObjectIdentity = ObjectIdentity
ol51nnMTPPL = _Ol51nnMTPPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18)
)
_Ol51nnMTPPLModTable_Object = MibTable
ol51nnMTPPLModTable = _Ol51nnMTPPLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTPPLModTable.setStatus("mandatory")
_Ol51nnMTPPLModEntry_Object = MibTableRow
ol51nnMTPPLModEntry = _Ol51nnMTPPLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 1, 1)
)
ol51nnMTPPLModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTPPLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPPLModEntry.setStatus("mandatory")
_Ol51nnMTPPLModSlotIndex_Type = Integer32
_Ol51nnMTPPLModSlotIndex_Object = MibTableColumn
ol51nnMTPPLModSlotIndex = _Ol51nnMTPPLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 1, 1, 1),
    _Ol51nnMTPPLModSlotIndex_Type()
)
ol51nnMTPPLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLModSlotIndex.setStatus("mandatory")
_Ol51nnMTPPLPortTable_Object = MibTable
ol51nnMTPPLPortTable = _Ol51nnMTPPLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTPPLPortTable.setStatus("mandatory")
_Ol51nnMTPPLPortEntry_Object = MibTableRow
ol51nnMTPPLPortEntry = _Ol51nnMTPPLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1)
)
ol51nnMTPPLPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTPPLPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMTPPLPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPPLPortEntry.setStatus("mandatory")
_Ol51nnMTPPLPortSlotIndex_Type = Integer32
_Ol51nnMTPPLPortSlotIndex_Object = MibTableColumn
ol51nnMTPPLPortSlotIndex = _Ol51nnMTPPLPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 1),
    _Ol51nnMTPPLPortSlotIndex_Type()
)
ol51nnMTPPLPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortSlotIndex.setStatus("mandatory")
_Ol51nnMTPPLPortIndex_Type = Integer32
_Ol51nnMTPPLPortIndex_Object = MibTableColumn
ol51nnMTPPLPortIndex = _Ol51nnMTPPLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 2),
    _Ol51nnMTPPLPortIndex_Type()
)
ol51nnMTPPLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortIndex.setStatus("mandatory")


class _Ol51nnMTPPLPortAdminState_Type(Integer32):
    """Custom type ol51nnMTPPLPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("remote-diagnostics", 8))
    )


_Ol51nnMTPPLPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortAdminState_Object = MibTableColumn
ol51nnMTPPLPortAdminState = _Ol51nnMTPPLPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 3),
    _Ol51nnMTPPLPortAdminState_Type()
)
ol51nnMTPPLPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortAdminState.setStatus("mandatory")
_Ol51nnMTPPLPortBuddySlot_Type = Integer32
_Ol51nnMTPPLPortBuddySlot_Object = MibTableColumn
ol51nnMTPPLPortBuddySlot = _Ol51nnMTPPLPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 4),
    _Ol51nnMTPPLPortBuddySlot_Type()
)
ol51nnMTPPLPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortBuddySlot.setStatus("mandatory")
_Ol51nnMTPPLPortBuddyPort_Type = Integer32
_Ol51nnMTPPLPortBuddyPort_Object = MibTableColumn
ol51nnMTPPLPortBuddyPort = _Ol51nnMTPPLPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 5),
    _Ol51nnMTPPLPortBuddyPort_Type()
)
ol51nnMTPPLPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortBuddyPort.setStatus("mandatory")


class _Ol51nnMTPPLPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMTPPLPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPPLPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortDipAdminState_Object = MibTableColumn
ol51nnMTPPLPortDipAdminState = _Ol51nnMTPPLPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 6),
    _Ol51nnMTPPLPortDipAdminState_Type()
)
ol51nnMTPPLPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortDipAdminState.setStatus("mandatory")


class _Ol51nnMTPPLPortDipNetwork_Type(Integer32):
    """Custom type ol51nnMTPPLPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMTPPLPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortDipNetwork_Object = MibTableColumn
ol51nnMTPPLPortDipNetwork = _Ol51nnMTPPLPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 7),
    _Ol51nnMTPPLPortDipNetwork_Type()
)
ol51nnMTPPLPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortDipNetwork.setStatus("mandatory")


class _Ol51nnMTPPLPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPPLPortLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPPLPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortLinkInteg_Object = MibTableColumn
ol51nnMTPPLPortLinkInteg = _Ol51nnMTPPLPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 8),
    _Ol51nnMTPPLPortLinkInteg_Type()
)
ol51nnMTPPLPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortLinkInteg.setStatus("mandatory")


class _Ol51nnMTPPLPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPPLPortDipLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPPLPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortDipLinkInteg_Object = MibTableColumn
ol51nnMTPPLPortDipLinkInteg = _Ol51nnMTPPLPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 9),
    _Ol51nnMTPPLPortDipLinkInteg_Type()
)
ol51nnMTPPLPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortDipLinkInteg.setStatus("mandatory")


class _Ol51nnMTPPLPortSquelch_Type(Integer32):
    """Custom type ol51nnMTPPLPortSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMTPPLPortSquelch_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortSquelch_Object = MibTableColumn
ol51nnMTPPLPortSquelch = _Ol51nnMTPPLPortSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 10),
    _Ol51nnMTPPLPortSquelch_Type()
)
ol51nnMTPPLPortSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortSquelch.setStatus("mandatory")


class _Ol51nnMTPPLPortJabber_Type(Integer32):
    """Custom type ol51nnMTPPLPortJabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPPLPortJabber_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortJabber_Object = MibTableColumn
ol51nnMTPPLPortJabber = _Ol51nnMTPPLPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 11),
    _Ol51nnMTPPLPortJabber_Type()
)
ol51nnMTPPLPortJabber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortJabber.setStatus("mandatory")


class _Ol51nnMTPPLPortDipJabber_Type(Integer32):
    """Custom type ol51nnMTPPLPortDipJabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPPLPortDipJabber_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortDipJabber_Object = MibTableColumn
ol51nnMTPPLPortDipJabber = _Ol51nnMTPPLPortDipJabber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 12),
    _Ol51nnMTPPLPortDipJabber_Type()
)
ol51nnMTPPLPortDipJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortDipJabber.setStatus("mandatory")
_Ol52nnMTP_ObjectIdentity = ObjectIdentity
ol52nnMTP = _Ol52nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19)
)
_Ol52nnMTPModTable_Object = MibTable
ol52nnMTPModTable = _Ol52nnMTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1)
)
if mibBuilder.loadTexts:
    ol52nnMTPModTable.setStatus("mandatory")
_Ol52nnMTPModEntry_Object = MibTableRow
ol52nnMTPModEntry = _Ol52nnMTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1)
)
ol52nnMTPModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMTPModEntry.setStatus("mandatory")
_Ol52nnMTPModSlotIndex_Type = Integer32
_Ol52nnMTPModSlotIndex_Object = MibTableColumn
ol52nnMTPModSlotIndex = _Ol52nnMTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1, 1),
    _Ol52nnMTPModSlotIndex_Type()
)
ol52nnMTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPModSlotIndex.setStatus("mandatory")


class _Ol52nnMTPModRingSpeed_Type(Integer32):
    """Custom type ol52nnMTPModRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMTPModRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMTPModRingSpeed_Object = MibTableColumn
ol52nnMTPModRingSpeed = _Ol52nnMTPModRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1, 2),
    _Ol52nnMTPModRingSpeed_Type()
)
ol52nnMTPModRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMTPModRingSpeed.setStatus("mandatory")


class _Ol52nnMTPModDipRingSpeed_Type(Integer32):
    """Custom type ol52nnMTPModDipRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMTPModDipRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMTPModDipRingSpeed_Object = MibTableColumn
ol52nnMTPModDipRingSpeed = _Ol52nnMTPModDipRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1, 3),
    _Ol52nnMTPModDipRingSpeed_Type()
)
ol52nnMTPModDipRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPModDipRingSpeed.setStatus("mandatory")


class _Ol52nnMTPModCableImp_Type(Integer32):
    """Custom type ol52nnMTPModCableImp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ohm100", 1),
          ("ohm150", 2))
    )


_Ol52nnMTPModCableImp_Type.__name__ = "Integer32"
_Ol52nnMTPModCableImp_Object = MibTableColumn
ol52nnMTPModCableImp = _Ol52nnMTPModCableImp_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1, 4),
    _Ol52nnMTPModCableImp_Type()
)
ol52nnMTPModCableImp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMTPModCableImp.setStatus("mandatory")


class _Ol52nnMTPModDipCableImp_Type(Integer32):
    """Custom type ol52nnMTPModDipCableImp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ohm100", 1),
          ("ohm150", 2))
    )


_Ol52nnMTPModDipCableImp_Type.__name__ = "Integer32"
_Ol52nnMTPModDipCableImp_Object = MibTableColumn
ol52nnMTPModDipCableImp = _Ol52nnMTPModDipCableImp_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1, 5),
    _Ol52nnMTPModDipCableImp_Type()
)
ol52nnMTPModDipCableImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPModDipCableImp.setStatus("mandatory")
_Ol52nnMTPPortTable_Object = MibTable
ol52nnMTPPortTable = _Ol52nnMTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2)
)
if mibBuilder.loadTexts:
    ol52nnMTPPortTable.setStatus("mandatory")
_Ol52nnMTPPortEntry_Object = MibTableRow
ol52nnMTPPortEntry = _Ol52nnMTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2, 1)
)
ol52nnMTPPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMTPPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol52nnMTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMTPPortEntry.setStatus("mandatory")
_Ol52nnMTPPortSlotIndex_Type = Integer32
_Ol52nnMTPPortSlotIndex_Object = MibTableColumn
ol52nnMTPPortSlotIndex = _Ol52nnMTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2, 1, 1),
    _Ol52nnMTPPortSlotIndex_Type()
)
ol52nnMTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPPortSlotIndex.setStatus("mandatory")
_Ol52nnMTPPortIndex_Type = Integer32
_Ol52nnMTPPortIndex_Object = MibTableColumn
ol52nnMTPPortIndex = _Ol52nnMTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2, 1, 2),
    _Ol52nnMTPPortIndex_Type()
)
ol52nnMTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPPortIndex.setStatus("mandatory")


class _Ol52nnMTPPortDipAdminState_Type(Integer32):
    """Custom type ol52nnMTPPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol52nnMTPPortDipAdminState_Type.__name__ = "Integer32"
_Ol52nnMTPPortDipAdminState_Object = MibTableColumn
ol52nnMTPPortDipAdminState = _Ol52nnMTPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2, 1, 3),
    _Ol52nnMTPPortDipAdminState_Type()
)
ol52nnMTPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPPortDipAdminState.setStatus("mandatory")


class _Ol52nnMTPPortStationType_Type(Integer32):
    """Custom type ol52nnMTPPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac-not-present", 2),
          ("mac-present", 1))
    )


_Ol52nnMTPPortStationType_Type.__name__ = "Integer32"
_Ol52nnMTPPortStationType_Object = MibTableColumn
ol52nnMTPPortStationType = _Ol52nnMTPPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2, 1, 4),
    _Ol52nnMTPPortStationType_Type()
)
ol52nnMTPPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMTPPortStationType.setStatus("mandatory")
_Ol52nnMTPTrunkTable_Object = MibTable
ol52nnMTPTrunkTable = _Ol52nnMTPTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 3)
)
if mibBuilder.loadTexts:
    ol52nnMTPTrunkTable.setStatus("mandatory")
_Ol52nnMTPTrunkEntry_Object = MibTableRow
ol52nnMTPTrunkEntry = _Ol52nnMTPTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 3, 1)
)
ol52nnMTPTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMTPTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol52nnMTPTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMTPTrunkEntry.setStatus("mandatory")
_Ol52nnMTPTrunkSlotIndex_Type = Integer32
_Ol52nnMTPTrunkSlotIndex_Object = MibTableColumn
ol52nnMTPTrunkSlotIndex = _Ol52nnMTPTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 3, 1, 1),
    _Ol52nnMTPTrunkSlotIndex_Type()
)
ol52nnMTPTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPTrunkSlotIndex.setStatus("mandatory")
_Ol52nnMTPTrunkIndex_Type = Integer32
_Ol52nnMTPTrunkIndex_Object = MibTableColumn
ol52nnMTPTrunkIndex = _Ol52nnMTPTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 3, 1, 2),
    _Ol52nnMTPTrunkIndex_Type()
)
ol52nnMTPTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPTrunkIndex.setStatus("mandatory")


class _Ol52nnMTPTrunkDipAdminState_Type(Integer32):
    """Custom type ol52nnMTPTrunkDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol52nnMTPTrunkDipAdminState_Type.__name__ = "Integer32"
_Ol52nnMTPTrunkDipAdminState_Object = MibTableColumn
ol52nnMTPTrunkDipAdminState = _Ol52nnMTPTrunkDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 3, 1, 3),
    _Ol52nnMTPTrunkDipAdminState_Type()
)
ol52nnMTPTrunkDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPTrunkDipAdminState.setStatus("mandatory")
_Ol52nnMFR_ObjectIdentity = ObjectIdentity
ol52nnMFR = _Ol52nnMFR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20)
)
_Ol52nnMFRModTable_Object = MibTable
ol52nnMFRModTable = _Ol52nnMFRModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 1)
)
if mibBuilder.loadTexts:
    ol52nnMFRModTable.setStatus("mandatory")
_Ol52nnMFRModEntry_Object = MibTableRow
ol52nnMFRModEntry = _Ol52nnMFRModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 1, 1)
)
ol52nnMFRModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMFRModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMFRModEntry.setStatus("mandatory")
_Ol52nnMFRModSlotIndex_Type = Integer32
_Ol52nnMFRModSlotIndex_Object = MibTableColumn
ol52nnMFRModSlotIndex = _Ol52nnMFRModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 1, 1, 1),
    _Ol52nnMFRModSlotIndex_Type()
)
ol52nnMFRModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRModSlotIndex.setStatus("mandatory")


class _Ol52nnMFRModRingSpeed_Type(Integer32):
    """Custom type ol52nnMFRModRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMFRModRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMFRModRingSpeed_Object = MibTableColumn
ol52nnMFRModRingSpeed = _Ol52nnMFRModRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 1, 1, 2),
    _Ol52nnMFRModRingSpeed_Type()
)
ol52nnMFRModRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRModRingSpeed.setStatus("mandatory")


class _Ol52nnMFRModDipRingSpeed_Type(Integer32):
    """Custom type ol52nnMFRModDipRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMFRModDipRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMFRModDipRingSpeed_Object = MibTableColumn
ol52nnMFRModDipRingSpeed = _Ol52nnMFRModDipRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 1, 1, 3),
    _Ol52nnMFRModDipRingSpeed_Type()
)
ol52nnMFRModDipRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRModDipRingSpeed.setStatus("mandatory")
_Ol52nnMFRPortTable_Object = MibTable
ol52nnMFRPortTable = _Ol52nnMFRPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2)
)
if mibBuilder.loadTexts:
    ol52nnMFRPortTable.setStatus("mandatory")
_Ol52nnMFRPortEntry_Object = MibTableRow
ol52nnMFRPortEntry = _Ol52nnMFRPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1)
)
ol52nnMFRPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMFRPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol52nnMFRPortIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMFRPortEntry.setStatus("mandatory")
_Ol52nnMFRPortSlotIndex_Type = Integer32
_Ol52nnMFRPortSlotIndex_Object = MibTableColumn
ol52nnMFRPortSlotIndex = _Ol52nnMFRPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1, 1),
    _Ol52nnMFRPortSlotIndex_Type()
)
ol52nnMFRPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRPortSlotIndex.setStatus("mandatory")
_Ol52nnMFRPortIndex_Type = Integer32
_Ol52nnMFRPortIndex_Object = MibTableColumn
ol52nnMFRPortIndex = _Ol52nnMFRPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1, 2),
    _Ol52nnMFRPortIndex_Type()
)
ol52nnMFRPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRPortIndex.setStatus("mandatory")


class _Ol52nnMFRPortDipAdminState_Type(Integer32):
    """Custom type ol52nnMFRPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol52nnMFRPortDipAdminState_Type.__name__ = "Integer32"
_Ol52nnMFRPortDipAdminState_Object = MibTableColumn
ol52nnMFRPortDipAdminState = _Ol52nnMFRPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1, 3),
    _Ol52nnMFRPortDipAdminState_Type()
)
ol52nnMFRPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRPortDipAdminState.setStatus("mandatory")


class _Ol52nnMFRPortCableImp_Type(Integer32):
    """Custom type ol52nnMFRPortCableImp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ohm100", 1),
          ("ohm150", 2))
    )


_Ol52nnMFRPortCableImp_Type.__name__ = "Integer32"
_Ol52nnMFRPortCableImp_Object = MibTableColumn
ol52nnMFRPortCableImp = _Ol52nnMFRPortCableImp_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1, 4),
    _Ol52nnMFRPortCableImp_Type()
)
ol52nnMFRPortCableImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRPortCableImp.setStatus("mandatory")


class _Ol52nnMFRPortStationType_Type(Integer32):
    """Custom type ol52nnMFRPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac-not-present", 2),
          ("mac-present", 1))
    )


_Ol52nnMFRPortStationType_Type.__name__ = "Integer32"
_Ol52nnMFRPortStationType_Object = MibTableColumn
ol52nnMFRPortStationType = _Ol52nnMFRPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1, 5),
    _Ol52nnMFRPortStationType_Type()
)
ol52nnMFRPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRPortStationType.setStatus("mandatory")
_Ol52nnMFRTrunkTable_Object = MibTable
ol52nnMFRTrunkTable = _Ol52nnMFRTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3)
)
if mibBuilder.loadTexts:
    ol52nnMFRTrunkTable.setStatus("mandatory")
_Ol52nnMFRTrunkEntry_Object = MibTableRow
ol52nnMFRTrunkEntry = _Ol52nnMFRTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1)
)
ol52nnMFRTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMFRTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol52nnMFRTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMFRTrunkEntry.setStatus("mandatory")
_Ol52nnMFRTrunkSlotIndex_Type = Integer32
_Ol52nnMFRTrunkSlotIndex_Object = MibTableColumn
ol52nnMFRTrunkSlotIndex = _Ol52nnMFRTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 1),
    _Ol52nnMFRTrunkSlotIndex_Type()
)
ol52nnMFRTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkSlotIndex.setStatus("mandatory")
_Ol52nnMFRTrunkIndex_Type = Integer32
_Ol52nnMFRTrunkIndex_Object = MibTableColumn
ol52nnMFRTrunkIndex = _Ol52nnMFRTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 2),
    _Ol52nnMFRTrunkIndex_Type()
)
ol52nnMFRTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkIndex.setStatus("mandatory")


class _Ol52nnMFRTrunkDipAdminState_Type(Integer32):
    """Custom type ol52nnMFRTrunkDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol52nnMFRTrunkDipAdminState_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkDipAdminState_Object = MibTableColumn
ol52nnMFRTrunkDipAdminState = _Ol52nnMFRTrunkDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 3),
    _Ol52nnMFRTrunkDipAdminState_Type()
)
ol52nnMFRTrunkDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkDipAdminState.setStatus("mandatory")


class _Ol52nnMFRTrunkCableMon_Type(Integer32):
    """Custom type ol52nnMFRTrunkCableMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol52nnMFRTrunkCableMon_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkCableMon_Object = MibTableColumn
ol52nnMFRTrunkCableMon = _Ol52nnMFRTrunkCableMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 4),
    _Ol52nnMFRTrunkCableMon_Type()
)
ol52nnMFRTrunkCableMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkCableMon.setStatus("mandatory")


class _Ol52nnMFRTrunkDipCableMon_Type(Integer32):
    """Custom type ol52nnMFRTrunkDipCableMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol52nnMFRTrunkDipCableMon_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkDipCableMon_Object = MibTableColumn
ol52nnMFRTrunkDipCableMon = _Ol52nnMFRTrunkDipCableMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 5),
    _Ol52nnMFRTrunkDipCableMon_Type()
)
ol52nnMFRTrunkDipCableMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkDipCableMon.setStatus("mandatory")


class _Ol52nnMFRTrunkCompMode_Type(Integer32):
    """Custom type ol52nnMFRTrunkCompMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol52nnMFRTrunkCompMode_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkCompMode_Object = MibTableColumn
ol52nnMFRTrunkCompMode = _Ol52nnMFRTrunkCompMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 6),
    _Ol52nnMFRTrunkCompMode_Type()
)
ol52nnMFRTrunkCompMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkCompMode.setStatus("mandatory")


class _Ol52nnMFRTrunkDipCompMode_Type(Integer32):
    """Custom type ol52nnMFRTrunkDipCompMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol52nnMFRTrunkDipCompMode_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkDipCompMode_Object = MibTableColumn
ol52nnMFRTrunkDipCompMode = _Ol52nnMFRTrunkDipCompMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 7),
    _Ol52nnMFRTrunkDipCompMode_Type()
)
ol52nnMFRTrunkDipCompMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkDipCompMode.setStatus("mandatory")


class _Ol52nnMFRTrunkNetMapState_Type(Integer32):
    """Custom type ol52nnMFRTrunkNetMapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("notApplicable", 1))
    )


_Ol52nnMFRTrunkNetMapState_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkNetMapState_Object = MibTableColumn
ol52nnMFRTrunkNetMapState = _Ol52nnMFRTrunkNetMapState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 8),
    _Ol52nnMFRTrunkNetMapState_Type()
)
ol52nnMFRTrunkNetMapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkNetMapState.setStatus("mandatory")


class _Ol52nnMFRTrunkExtBcnRecovery_Type(Integer32):
    """Custom type ol52nnMFRTrunkExtBcnRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exists", 1),
          ("nonExists", 2),
          ("notApplicable", 3))
    )


_Ol52nnMFRTrunkExtBcnRecovery_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkExtBcnRecovery_Object = MibTableColumn
ol52nnMFRTrunkExtBcnRecovery = _Ol52nnMFRTrunkExtBcnRecovery_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 9),
    _Ol52nnMFRTrunkExtBcnRecovery_Type()
)
ol52nnMFRTrunkExtBcnRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkExtBcnRecovery.setStatus("mandatory")
_Ol52nnMFRTrunkBuddySlot_Type = Integer32
_Ol52nnMFRTrunkBuddySlot_Object = MibTableColumn
ol52nnMFRTrunkBuddySlot = _Ol52nnMFRTrunkBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 10),
    _Ol52nnMFRTrunkBuddySlot_Type()
)
ol52nnMFRTrunkBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkBuddySlot.setStatus("mandatory")


class _Ol52nnMFRTrunkAdminState_Type(Integer32):
    """Custom type ol52nnMFRTrunkAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-primary", 3),
          ("redundant-standby", 4))
    )


_Ol52nnMFRTrunkAdminState_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkAdminState_Object = MibTableColumn
ol52nnMFRTrunkAdminState = _Ol52nnMFRTrunkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 11),
    _Ol52nnMFRTrunkAdminState_Type()
)
ol52nnMFRTrunkAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkAdminState.setStatus("mandatory")
_Ol51nnMTS_ObjectIdentity = ObjectIdentity
ol51nnMTS = _Ol51nnMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21)
)
_Ol51nnMTSModTable_Object = MibTable
ol51nnMTSModTable = _Ol51nnMTSModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTSModTable.setStatus("mandatory")
_Ol51nnMTSModEntry_Object = MibTableRow
ol51nnMTSModEntry = _Ol51nnMTSModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1)
)
ol51nnMTSModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTSModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTSModEntry.setStatus("mandatory")
_Ol51nnMTSModSlotIndex_Type = Integer32
_Ol51nnMTSModSlotIndex_Object = MibTableColumn
ol51nnMTSModSlotIndex = _Ol51nnMTSModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 1),
    _Ol51nnMTSModSlotIndex_Type()
)
ol51nnMTSModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModSlotIndex.setStatus("mandatory")
_Ol51nnMTSModProtocols_Type = DisplayString
_Ol51nnMTSModProtocols_Object = MibTableColumn
ol51nnMTSModProtocols = _Ol51nnMTSModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 2),
    _Ol51nnMTSModProtocols_Type()
)
ol51nnMTSModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModProtocols.setStatus("mandatory")
_Ol51nnMTSModIpAddress_Type = IpAddress
_Ol51nnMTSModIpAddress_Object = MibTableColumn
ol51nnMTSModIpAddress = _Ol51nnMTSModIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 3),
    _Ol51nnMTSModIpAddress_Type()
)
ol51nnMTSModIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModIpAddress.setStatus("mandatory")
_Ol51nnMTSModTCPPort_Type = Integer32
_Ol51nnMTSModTCPPort_Object = MibTableColumn
ol51nnMTSModTCPPort = _Ol51nnMTSModTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 4),
    _Ol51nnMTSModTCPPort_Type()
)
ol51nnMTSModTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModTCPPort.setStatus("mandatory")


class _Ol51nnMTSModStationAddr_Type(OctetString):
    """Custom type ol51nnMTSModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnMTSModStationAddr_Type.__name__ = "OctetString"
_Ol51nnMTSModStationAddr_Object = MibTableColumn
ol51nnMTSModStationAddr = _Ol51nnMTSModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 5),
    _Ol51nnMTSModStationAddr_Type()
)
ol51nnMTSModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModStationAddr.setStatus("mandatory")


class _Ol51nnMTSModDipNetwork_Type(Integer32):
    """Custom type ol51nnMTSModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMTSModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTSModDipNetwork_Object = MibTableColumn
ol51nnMTSModDipNetwork = _Ol51nnMTSModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 6),
    _Ol51nnMTSModDipNetwork_Type()
)
ol51nnMTSModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModDipNetwork.setStatus("mandatory")


class _Ol51nnMTSModCPURev_Type(DisplayString):
    """Custom type ol51nnMTSModCPURev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Ol51nnMTSModCPURev_Type.__name__ = "DisplayString"
_Ol51nnMTSModCPURev_Object = MibTableColumn
ol51nnMTSModCPURev = _Ol51nnMTSModCPURev_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 7),
    _Ol51nnMTSModCPURev_Type()
)
ol51nnMTSModCPURev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModCPURev.setStatus("mandatory")
_Ol51nnMTSPortTable_Object = MibTable
ol51nnMTSPortTable = _Ol51nnMTSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTSPortTable.setStatus("mandatory")
_Ol51nnMTSPortEntry_Object = MibTableRow
ol51nnMTSPortEntry = _Ol51nnMTSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2, 1)
)
ol51nnMTSPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTSPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMTSPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTSPortEntry.setStatus("mandatory")
_Ol51nnMTSPortSlotIndex_Type = Integer32
_Ol51nnMTSPortSlotIndex_Object = MibTableColumn
ol51nnMTSPortSlotIndex = _Ol51nnMTSPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2, 1, 1),
    _Ol51nnMTSPortSlotIndex_Type()
)
ol51nnMTSPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSPortSlotIndex.setStatus("mandatory")
_Ol51nnMTSPortIndex_Type = Integer32
_Ol51nnMTSPortIndex_Object = MibTableColumn
ol51nnMTSPortIndex = _Ol51nnMTSPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2, 1, 2),
    _Ol51nnMTSPortIndex_Type()
)
ol51nnMTSPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSPortIndex.setStatus("mandatory")


class _Ol51nnMTSPortAdminState_Type(Integer32):
    """Custom type ol51nnMTSPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("local", 6),
          ("remote", 7))
    )


_Ol51nnMTSPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTSPortAdminState_Object = MibTableColumn
ol51nnMTSPortAdminState = _Ol51nnMTSPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2, 1, 3),
    _Ol51nnMTSPortAdminState_Type()
)
ol51nnMTSPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTSPortAdminState.setStatus("mandatory")


class _Ol51nnMTSPortOperState_Type(Integer32):
    """Custom type ol51nnMTSPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("idle", 1),
          ("local", 2))
    )


_Ol51nnMTSPortOperState_Type.__name__ = "Integer32"
_Ol51nnMTSPortOperState_Object = MibTableColumn
ol51nnMTSPortOperState = _Ol51nnMTSPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2, 1, 4),
    _Ol51nnMTSPortOperState_Type()
)
ol51nnMTSPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSPortOperState.setStatus("mandatory")
_Ol51nnMFL_ObjectIdentity = ObjectIdentity
ol51nnMFL = _Ol51nnMFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22)
)
_Ol51nnMFLModTable_Object = MibTable
ol51nnMFLModTable = _Ol51nnMFLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 1)
)
if mibBuilder.loadTexts:
    ol51nnMFLModTable.setStatus("mandatory")
_Ol51nnMFLModEntry_Object = MibTableRow
ol51nnMFLModEntry = _Ol51nnMFLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 1, 1)
)
ol51nnMFLModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMFLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFLModEntry.setStatus("mandatory")
_Ol51nnMFLModSlotIndex_Type = Integer32
_Ol51nnMFLModSlotIndex_Object = MibTableColumn
ol51nnMFLModSlotIndex = _Ol51nnMFLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 1, 1, 1),
    _Ol51nnMFLModSlotIndex_Type()
)
ol51nnMFLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFLModSlotIndex.setStatus("mandatory")


class _Ol51nnMFLModDipNetwork_Type(Integer32):
    """Custom type ol51nnMFLModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMFLModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMFLModDipNetwork_Object = MibTableColumn
ol51nnMFLModDipNetwork = _Ol51nnMFLModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 1, 1, 2),
    _Ol51nnMFLModDipNetwork_Type()
)
ol51nnMFLModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFLModDipNetwork.setStatus("mandatory")
_Ol51nnMFLPortTable_Object = MibTable
ol51nnMFLPortTable = _Ol51nnMFLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2)
)
if mibBuilder.loadTexts:
    ol51nnMFLPortTable.setStatus("mandatory")
_Ol51nnMFLPortEntry_Object = MibTableRow
ol51nnMFLPortEntry = _Ol51nnMFLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1)
)
ol51nnMFLPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMFLPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMFLPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFLPortEntry.setStatus("mandatory")
_Ol51nnMFLPortSlotIndex_Type = Integer32
_Ol51nnMFLPortSlotIndex_Object = MibTableColumn
ol51nnMFLPortSlotIndex = _Ol51nnMFLPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 1),
    _Ol51nnMFLPortSlotIndex_Type()
)
ol51nnMFLPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFLPortSlotIndex.setStatus("mandatory")
_Ol51nnMFLPortIndex_Type = Integer32
_Ol51nnMFLPortIndex_Object = MibTableColumn
ol51nnMFLPortIndex = _Ol51nnMFLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 2),
    _Ol51nnMFLPortIndex_Type()
)
ol51nnMFLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFLPortIndex.setStatus("mandatory")


class _Ol51nnMFLPortAdminState_Type(Integer32):
    """Custom type ol51nnMFLPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("redundant-rfs", 5))
    )


_Ol51nnMFLPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMFLPortAdminState_Object = MibTableColumn
ol51nnMFLPortAdminState = _Ol51nnMFLPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 3),
    _Ol51nnMFLPortAdminState_Type()
)
ol51nnMFLPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFLPortAdminState.setStatus("mandatory")
_Ol51nnMFLPortBuddySlot_Type = Integer32
_Ol51nnMFLPortBuddySlot_Object = MibTableColumn
ol51nnMFLPortBuddySlot = _Ol51nnMFLPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 4),
    _Ol51nnMFLPortBuddySlot_Type()
)
ol51nnMFLPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFLPortBuddySlot.setStatus("mandatory")
_Ol51nnMFLPortBuddyPort_Type = Integer32
_Ol51nnMFLPortBuddyPort_Object = MibTableColumn
ol51nnMFLPortBuddyPort = _Ol51nnMFLPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 5),
    _Ol51nnMFLPortBuddyPort_Type()
)
ol51nnMFLPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFLPortBuddyPort.setStatus("mandatory")


class _Ol51nnMFLPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMFLPortDipAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("redundant-rfs", 5))
    )


_Ol51nnMFLPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMFLPortDipAdminState_Object = MibTableColumn
ol51nnMFLPortDipAdminState = _Ol51nnMFLPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 6),
    _Ol51nnMFLPortDipAdminState_Type()
)
ol51nnMFLPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFLPortDipAdminState.setStatus("mandatory")
_Ol50nnMRCTL_ObjectIdentity = ObjectIdentity
ol50nnMRCTL = _Ol50nnMRCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23)
)
_Ol50nnMRCTLModTable_Object = MibTable
ol50nnMRCTLModTable = _Ol50nnMRCTLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1)
)
if mibBuilder.loadTexts:
    ol50nnMRCTLModTable.setStatus("mandatory")
_Ol50nnMRCTLModEntry_Object = MibTableRow
ol50nnMRCTLModEntry = _Ol50nnMRCTLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1, 1)
)
ol50nnMRCTLModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol50nnMRCTLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol50nnMRCTLModEntry.setStatus("mandatory")
_Ol50nnMRCTLModSlotIndex_Type = Integer32
_Ol50nnMRCTLModSlotIndex_Object = MibTableColumn
ol50nnMRCTLModSlotIndex = _Ol50nnMRCTLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1, 1, 1),
    _Ol50nnMRCTLModSlotIndex_Type()
)
ol50nnMRCTLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCTLModSlotIndex.setStatus("mandatory")


class _Ol50nnMRCTLModOperState_Type(Integer32):
    """Custom type ol50nnMRCTLModOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_Ol50nnMRCTLModOperState_Type.__name__ = "Integer32"
_Ol50nnMRCTLModOperState_Object = MibTableColumn
ol50nnMRCTLModOperState = _Ol50nnMRCTLModOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1, 1, 2),
    _Ol50nnMRCTLModOperState_Type()
)
ol50nnMRCTLModOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCTLModOperState.setStatus("mandatory")


class _Ol50nnMRCTLModClockStatus_Type(Integer32):
    """Custom type ol50nnMRCTLModClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1))
    )


_Ol50nnMRCTLModClockStatus_Type.__name__ = "Integer32"
_Ol50nnMRCTLModClockStatus_Object = MibTableColumn
ol50nnMRCTLModClockStatus = _Ol50nnMRCTLModClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1, 1, 3),
    _Ol50nnMRCTLModClockStatus_Type()
)
ol50nnMRCTLModClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCTLModClockStatus.setStatus("mandatory")


class _Ol50nnMRCTLModTempStatus_Type(Integer32):
    """Custom type ol50nnMRCTLModTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1))
    )


_Ol50nnMRCTLModTempStatus_Type.__name__ = "Integer32"
_Ol50nnMRCTLModTempStatus_Object = MibTableColumn
ol50nnMRCTLModTempStatus = _Ol50nnMRCTLModTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1, 1, 4),
    _Ol50nnMRCTLModTempStatus_Type()
)
ol50nnMRCTLModTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCTLModTempStatus.setStatus("mandatory")
_Ol51nnMFB_ObjectIdentity = ObjectIdentity
ol51nnMFB = _Ol51nnMFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24)
)
_Ol51nnMFBModTable_Object = MibTable
ol51nnMFBModTable = _Ol51nnMFBModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1)
)
if mibBuilder.loadTexts:
    ol51nnMFBModTable.setStatus("mandatory")
_Ol51nnMFBModEntry_Object = MibTableRow
ol51nnMFBModEntry = _Ol51nnMFBModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1, 1)
)
ol51nnMFBModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMFBModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFBModEntry.setStatus("mandatory")
_Ol51nnMFBModSlotIndex_Type = Integer32
_Ol51nnMFBModSlotIndex_Object = MibTableColumn
ol51nnMFBModSlotIndex = _Ol51nnMFBModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1, 1, 1),
    _Ol51nnMFBModSlotIndex_Type()
)
ol51nnMFBModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBModSlotIndex.setStatus("mandatory")


class _Ol51nnMFBModDipNetwork_Type(Integer32):
    """Custom type ol51nnMFBModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMFBModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMFBModDipNetwork_Object = MibTableColumn
ol51nnMFBModDipNetwork = _Ol51nnMFBModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1, 1, 2),
    _Ol51nnMFBModDipNetwork_Type()
)
ol51nnMFBModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBModDipNetwork.setStatus("mandatory")


class _Ol51nnMFBModLLW_Type(Integer32):
    """Custom type ol51nnMFBModLLW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFBModLLW_Type.__name__ = "Integer32"
_Ol51nnMFBModLLW_Object = MibTableColumn
ol51nnMFBModLLW = _Ol51nnMFBModLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1, 1, 3),
    _Ol51nnMFBModLLW_Type()
)
ol51nnMFBModLLW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBModLLW.setStatus("mandatory")


class _Ol51nnMFBModDipLLW_Type(Integer32):
    """Custom type ol51nnMFBModDipLLW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFBModDipLLW_Type.__name__ = "Integer32"
_Ol51nnMFBModDipLLW_Object = MibTableColumn
ol51nnMFBModDipLLW = _Ol51nnMFBModDipLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1, 1, 4),
    _Ol51nnMFBModDipLLW_Type()
)
ol51nnMFBModDipLLW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBModDipLLW.setStatus("mandatory")
_Ol51nnMFBPortTable_Object = MibTable
ol51nnMFBPortTable = _Ol51nnMFBPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2)
)
if mibBuilder.loadTexts:
    ol51nnMFBPortTable.setStatus("mandatory")
_Ol51nnMFBPortEntry_Object = MibTableRow
ol51nnMFBPortEntry = _Ol51nnMFBPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1)
)
ol51nnMFBPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMFBPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMFBPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFBPortEntry.setStatus("mandatory")
_Ol51nnMFBPortSlotIndex_Type = Integer32
_Ol51nnMFBPortSlotIndex_Object = MibTableColumn
ol51nnMFBPortSlotIndex = _Ol51nnMFBPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 1),
    _Ol51nnMFBPortSlotIndex_Type()
)
ol51nnMFBPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPortSlotIndex.setStatus("mandatory")
_Ol51nnMFBPortIndex_Type = Integer32
_Ol51nnMFBPortIndex_Object = MibTableColumn
ol51nnMFBPortIndex = _Ol51nnMFBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 2),
    _Ol51nnMFBPortIndex_Type()
)
ol51nnMFBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPortIndex.setStatus("mandatory")


class _Ol51nnMFBPortAdminState_Type(Integer32):
    """Custom type ol51nnMFBPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFBPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMFBPortAdminState_Object = MibTableColumn
ol51nnMFBPortAdminState = _Ol51nnMFBPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 3),
    _Ol51nnMFBPortAdminState_Type()
)
ol51nnMFBPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPortAdminState.setStatus("mandatory")
_Ol51nnMFBPortBuddySlot_Type = Integer32
_Ol51nnMFBPortBuddySlot_Object = MibTableColumn
ol51nnMFBPortBuddySlot = _Ol51nnMFBPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 4),
    _Ol51nnMFBPortBuddySlot_Type()
)
ol51nnMFBPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPortBuddySlot.setStatus("mandatory")
_Ol51nnMFBPortBuddyPort_Type = Integer32
_Ol51nnMFBPortBuddyPort_Object = MibTableColumn
ol51nnMFBPortBuddyPort = _Ol51nnMFBPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 5),
    _Ol51nnMFBPortBuddyPort_Type()
)
ol51nnMFBPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPortBuddyPort.setStatus("mandatory")


class _Ol51nnMFBPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMFBPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMFBPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMFBPortDipAdminState_Object = MibTableColumn
ol51nnMFBPortDipAdminState = _Ol51nnMFBPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 6),
    _Ol51nnMFBPortDipAdminState_Type()
)
ol51nnMFBPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPortDipAdminState.setStatus("mandatory")
_Ol53nnMMGT_ObjectIdentity = ObjectIdentity
ol53nnMMGT = _Ol53nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25)
)
_Ol53nnMMGTModTable_Object = MibTable
ol53nnMMGTModTable = _Ol53nnMMGTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1)
)
if mibBuilder.loadTexts:
    ol53nnMMGTModTable.setStatus("mandatory")
_Ol53nnMMGTModEntry_Object = MibTableRow
ol53nnMMGTModEntry = _Ol53nnMMGTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1)
)
ol53nnMMGTModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMMGTModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMMGTModEntry.setStatus("mandatory")
_Ol53nnMMGTModSlotIndex_Type = Integer32
_Ol53nnMMGTModSlotIndex_Object = MibTableColumn
ol53nnMMGTModSlotIndex = _Ol53nnMMGTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 1),
    _Ol53nnMMGTModSlotIndex_Type()
)
ol53nnMMGTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModSlotIndex.setStatus("mandatory")


class _Ol53nnMMGTModMasterPriority_Type(Integer32):
    """Custom type ol53nnMMGTModMasterPriority based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("nine", 9),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("ten", 10),
          ("three", 3),
          ("two", 2))
    )


_Ol53nnMMGTModMasterPriority_Type.__name__ = "Integer32"
_Ol53nnMMGTModMasterPriority_Object = MibTableColumn
ol53nnMMGTModMasterPriority = _Ol53nnMMGTModMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 2),
    _Ol53nnMMGTModMasterPriority_Type()
)
ol53nnMMGTModMasterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMMGTModMasterPriority.setStatus("mandatory")


class _Ol53nnMMGTModMasterStatus_Type(Integer32):
    """Custom type ol53nnMMGTModMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("electing", 3),
          ("master", 1),
          ("non-master", 2))
    )


_Ol53nnMMGTModMasterStatus_Type.__name__ = "Integer32"
_Ol53nnMMGTModMasterStatus_Object = MibTableColumn
ol53nnMMGTModMasterStatus = _Ol53nnMMGTModMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 3),
    _Ol53nnMMGTModMasterStatus_Type()
)
ol53nnMMGTModMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModMasterStatus.setStatus("mandatory")


class _Ol53nnMMGTModStationAddr_Type(OctetString):
    """Custom type ol53nnMMGTModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol53nnMMGTModStationAddr_Type.__name__ = "OctetString"
_Ol53nnMMGTModStationAddr_Object = MibTableColumn
ol53nnMMGTModStationAddr = _Ol53nnMMGTModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 4),
    _Ol53nnMMGTModStationAddr_Type()
)
ol53nnMMGTModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModStationAddr.setStatus("mandatory")
_Ol53nnMMGTModIpAddress_Type = IpAddress
_Ol53nnMMGTModIpAddress_Object = MibTableColumn
ol53nnMMGTModIpAddress = _Ol53nnMMGTModIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 5),
    _Ol53nnMMGTModIpAddress_Type()
)
ol53nnMMGTModIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModIpAddress.setStatus("mandatory")


class _Ol53nnMMGTModDownStreamMAC_Type(OctetString):
    """Custom type ol53nnMMGTModDownStreamMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol53nnMMGTModDownStreamMAC_Type.__name__ = "OctetString"
_Ol53nnMMGTModDownStreamMAC_Object = MibTableColumn
ol53nnMMGTModDownStreamMAC = _Ol53nnMMGTModDownStreamMAC_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 6),
    _Ol53nnMMGTModDownStreamMAC_Type()
)
ol53nnMMGTModDownStreamMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModDownStreamMAC.setStatus("mandatory")


class _Ol53nnMMGTModUpStreamMAC_Type(OctetString):
    """Custom type ol53nnMMGTModUpStreamMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol53nnMMGTModUpStreamMAC_Type.__name__ = "OctetString"
_Ol53nnMMGTModUpStreamMAC_Object = MibTableColumn
ol53nnMMGTModUpStreamMAC = _Ol53nnMMGTModUpStreamMAC_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 7),
    _Ol53nnMMGTModUpStreamMAC_Type()
)
ol53nnMMGTModUpStreamMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModUpStreamMAC.setStatus("mandatory")


class _Ol53nnMMGTModfddiMACPath_Type(Integer32):
    """Custom type ol53nnMMGTModfddiMACPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_Ol53nnMMGTModfddiMACPath_Type.__name__ = "Integer32"
_Ol53nnMMGTModfddiMACPath_Object = MibTableColumn
ol53nnMMGTModfddiMACPath = _Ol53nnMMGTModfddiMACPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 8),
    _Ol53nnMMGTModfddiMACPath_Type()
)
ol53nnMMGTModfddiMACPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMMGTModfddiMACPath.setStatus("mandatory")


class _Ol53nnMMGTModDownStreamModule_Type(Integer32):
    """Custom type ol53nnMMGTModDownStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMMGTModDownStreamModule_Type.__name__ = "Integer32"
_Ol53nnMMGTModDownStreamModule_Object = MibTableColumn
ol53nnMMGTModDownStreamModule = _Ol53nnMMGTModDownStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 9),
    _Ol53nnMMGTModDownStreamModule_Type()
)
ol53nnMMGTModDownStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModDownStreamModule.setStatus("mandatory")


class _Ol53nnMMGTModUpStreamModule_Type(Integer32):
    """Custom type ol53nnMMGTModUpStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMMGTModUpStreamModule_Type.__name__ = "Integer32"
_Ol53nnMMGTModUpStreamModule_Object = MibTableColumn
ol53nnMMGTModUpStreamModule = _Ol53nnMMGTModUpStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 10),
    _Ol53nnMMGTModUpStreamModule_Type()
)
ol53nnMMGTModUpStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModUpStreamModule.setStatus("mandatory")


class _Ol53nnMMGTModDownStreamOperPath_Type(Integer32):
    """Custom type ol53nnMMGTModDownStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMMGTModDownStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMMGTModDownStreamOperPath_Object = MibTableColumn
ol53nnMMGTModDownStreamOperPath = _Ol53nnMMGTModDownStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 11),
    _Ol53nnMMGTModDownStreamOperPath_Type()
)
ol53nnMMGTModDownStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModDownStreamOperPath.setStatus("mandatory")


class _Ol53nnMMGTModUpStreamOperPath_Type(Integer32):
    """Custom type ol53nnMMGTModUpStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMMGTModUpStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMMGTModUpStreamOperPath_Object = MibTableColumn
ol53nnMMGTModUpStreamOperPath = _Ol53nnMMGTModUpStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 12),
    _Ol53nnMMGTModUpStreamOperPath_Type()
)
ol53nnMMGTModUpStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModUpStreamOperPath.setStatus("mandatory")


class _Ol53nnMMGTModRingInfo_Type(OctetString):
    """Custom type ol53nnMMGTModRingInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ol53nnMMGTModRingInfo_Type.__name__ = "OctetString"
_Ol53nnMMGTModRingInfo_Object = MibTableColumn
ol53nnMMGTModRingInfo = _Ol53nnMMGTModRingInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 13),
    _Ol53nnMMGTModRingInfo_Type()
)
ol53nnMMGTModRingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModRingInfo.setStatus("mandatory")
_Ol53nnMMGTPortTable_Object = MibTable
ol53nnMMGTPortTable = _Ol53nnMMGTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2)
)
if mibBuilder.loadTexts:
    ol53nnMMGTPortTable.setStatus("mandatory")
_Ol53nnMMGTPortEntry_Object = MibTableRow
ol53nnMMGTPortEntry = _Ol53nnMMGTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1)
)
ol53nnMMGTPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMMGTPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol53nnMMGTPortIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMMGTPortEntry.setStatus("mandatory")
_Ol53nnMMGTPortSlotIndex_Type = Integer32
_Ol53nnMMGTPortSlotIndex_Object = MibTableColumn
ol53nnMMGTPortSlotIndex = _Ol53nnMMGTPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 1),
    _Ol53nnMMGTPortSlotIndex_Type()
)
ol53nnMMGTPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortSlotIndex.setStatus("mandatory")
_Ol53nnMMGTPortIndex_Type = Integer32
_Ol53nnMMGTPortIndex_Object = MibTableColumn
ol53nnMMGTPortIndex = _Ol53nnMMGTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 2),
    _Ol53nnMMGTPortIndex_Type()
)
ol53nnMMGTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortIndex.setStatus("mandatory")


class _Ol53nnMMGTPortConfig_Type(Integer32):
    """Custom type ol53nnMMGTPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_Ol53nnMMGTPortConfig_Type.__name__ = "Integer32"
_Ol53nnMMGTPortConfig_Object = MibTableColumn
ol53nnMMGTPortConfig = _Ol53nnMMGTPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 3),
    _Ol53nnMMGTPortConfig_Type()
)
ol53nnMMGTPortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortConfig.setStatus("mandatory")


class _Ol53nnMMGTPortPcmState_Type(Integer32):
    """Custom type ol53nnMMGTPortPcmState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("pc0", 1),
          ("pc1", 2),
          ("pc2", 3),
          ("pc3", 4),
          ("pc4", 5),
          ("pc5", 6),
          ("pc6", 7),
          ("pc7", 8),
          ("pc8", 9),
          ("pc9", 10))
    )


_Ol53nnMMGTPortPcmState_Type.__name__ = "Integer32"
_Ol53nnMMGTPortPcmState_Object = MibTableColumn
ol53nnMMGTPortPcmState = _Ol53nnMMGTPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 4),
    _Ol53nnMMGTPortPcmState_Type()
)
ol53nnMMGTPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortPcmState.setStatus("mandatory")


class _Ol53nnMMGTPortConnectState_Type(Integer32):
    """Custom type ol53nnMMGTPortConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_Ol53nnMMGTPortConnectState_Type.__name__ = "Integer32"
_Ol53nnMMGTPortConnectState_Object = MibTableColumn
ol53nnMMGTPortConnectState = _Ol53nnMMGTPortConnectState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 5),
    _Ol53nnMMGTPortConnectState_Type()
)
ol53nnMMGTPortConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortConnectState.setStatus("mandatory")


class _Ol53nnMMGTPortNeighbor_Type(Integer32):
    """Custom type ol53nnMMGTPortNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("master", 4),
          ("slave", 3),
          ("unknown", 5))
    )


_Ol53nnMMGTPortNeighbor_Type.__name__ = "Integer32"
_Ol53nnMMGTPortNeighbor_Object = MibTableColumn
ol53nnMMGTPortNeighbor = _Ol53nnMMGTPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 6),
    _Ol53nnMMGTPortNeighbor_Type()
)
ol53nnMMGTPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortNeighbor.setStatus("mandatory")


class _Ol53nnMMGTPortRemoteMACIndicated_Type(Integer32):
    """Custom type ol53nnMMGTPortRemoteMACIndicated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol53nnMMGTPortRemoteMACIndicated_Type.__name__ = "Integer32"
_Ol53nnMMGTPortRemoteMACIndicated_Object = MibTableColumn
ol53nnMMGTPortRemoteMACIndicated = _Ol53nnMMGTPortRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 7),
    _Ol53nnMMGTPortRemoteMACIndicated_Type()
)
ol53nnMMGTPortRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortRemoteMACIndicated.setStatus("mandatory")


class _Ol53nnMMGTPortBSFlag_Type(Integer32):
    """Custom type ol53nnMMGTPortBSFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol53nnMMGTPortBSFlag_Type.__name__ = "Integer32"
_Ol53nnMMGTPortBSFlag_Object = MibTableColumn
ol53nnMMGTPortBSFlag = _Ol53nnMMGTPortBSFlag_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 8),
    _Ol53nnMMGTPortBSFlag_Type()
)
ol53nnMMGTPortBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortBSFlag.setStatus("mandatory")


class _Ol53nnMMGTPortPCWithhold_Type(Integer32):
    """Custom type ol53nnMMGTPortPCWithhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-m", 2),
          ("none", 1),
          ("other", 3))
    )


_Ol53nnMMGTPortPCWithhold_Type.__name__ = "Integer32"
_Ol53nnMMGTPortPCWithhold_Object = MibTableColumn
ol53nnMMGTPortPCWithhold = _Ol53nnMMGTPortPCWithhold_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 9),
    _Ol53nnMMGTPortPCWithhold_Type()
)
ol53nnMMGTPortPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortPCWithhold.setStatus("mandatory")


class _Ol53nnMMGTPortLerCondition_Type(Integer32):
    """Custom type ol53nnMMGTPortLerCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("okay", 2))
    )


_Ol53nnMMGTPortLerCondition_Type.__name__ = "Integer32"
_Ol53nnMMGTPortLerCondition_Object = MibTableColumn
ol53nnMMGTPortLerCondition = _Ol53nnMMGTPortLerCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 10),
    _Ol53nnMMGTPortLerCondition_Type()
)
ol53nnMMGTPortLerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortLerCondition.setStatus("mandatory")
_Ol53nnMMGTTrunkTable_Object = MibTable
ol53nnMMGTTrunkTable = _Ol53nnMMGTTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 3)
)
if mibBuilder.loadTexts:
    ol53nnMMGTTrunkTable.setStatus("mandatory")
_Ol53nnMMGTTrunkEntry_Object = MibTableRow
ol53nnMMGTTrunkEntry = _Ol53nnMMGTTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 3, 1)
)
ol53nnMMGTTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMMGTTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol53nnMMGTTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMMGTTrunkEntry.setStatus("mandatory")
_Ol53nnMMGTTrunkSlotIndex_Type = Integer32
_Ol53nnMMGTTrunkSlotIndex_Object = MibTableColumn
ol53nnMMGTTrunkSlotIndex = _Ol53nnMMGTTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 3, 1, 1),
    _Ol53nnMMGTTrunkSlotIndex_Type()
)
ol53nnMMGTTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTTrunkSlotIndex.setStatus("mandatory")
_Ol53nnMMGTTrunkIndex_Type = Integer32
_Ol53nnMMGTTrunkIndex_Object = MibTableColumn
ol53nnMMGTTrunkIndex = _Ol53nnMMGTTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 3, 1, 2),
    _Ol53nnMMGTTrunkIndex_Type()
)
ol53nnMMGTTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTTrunkIndex.setStatus("mandatory")
_Ol53nnMFBMIC_ObjectIdentity = ObjectIdentity
ol53nnMFBMIC = _Ol53nnMFBMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26)
)
_Ol53nnMFBMICModTable_Object = MibTable
ol53nnMFBMICModTable = _Ol53nnMFBMICModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1)
)
if mibBuilder.loadTexts:
    ol53nnMFBMICModTable.setStatus("mandatory")
_Ol53nnMFBMICModEntry_Object = MibTableRow
ol53nnMFBMICModEntry = _Ol53nnMFBMICModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1)
)
ol53nnMFBMICModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMFBMICModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFBMICModEntry.setStatus("mandatory")
_Ol53nnMFBMICModSlotIndex_Type = Integer32
_Ol53nnMFBMICModSlotIndex_Object = MibTableColumn
ol53nnMFBMICModSlotIndex = _Ol53nnMFBMICModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 1),
    _Ol53nnMFBMICModSlotIndex_Type()
)
ol53nnMFBMICModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModSlotIndex.setStatus("mandatory")


class _Ol53nnMFBMICModDownStreamModule_Type(Integer32):
    """Custom type ol53nnMFBMICModDownStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMFBMICModDownStreamModule_Type.__name__ = "Integer32"
_Ol53nnMFBMICModDownStreamModule_Object = MibTableColumn
ol53nnMFBMICModDownStreamModule = _Ol53nnMFBMICModDownStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 2),
    _Ol53nnMFBMICModDownStreamModule_Type()
)
ol53nnMFBMICModDownStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModDownStreamModule.setStatus("mandatory")


class _Ol53nnMFBMICModUpStreamModule_Type(Integer32):
    """Custom type ol53nnMFBMICModUpStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMFBMICModUpStreamModule_Type.__name__ = "Integer32"
_Ol53nnMFBMICModUpStreamModule_Object = MibTableColumn
ol53nnMFBMICModUpStreamModule = _Ol53nnMFBMICModUpStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 3),
    _Ol53nnMFBMICModUpStreamModule_Type()
)
ol53nnMFBMICModUpStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModUpStreamModule.setStatus("mandatory")


class _Ol53nnMFBMICModDownStreamOperPath_Type(Integer32):
    """Custom type ol53nnMFBMICModDownStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMFBMICModDownStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMFBMICModDownStreamOperPath_Object = MibTableColumn
ol53nnMFBMICModDownStreamOperPath = _Ol53nnMFBMICModDownStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 4),
    _Ol53nnMFBMICModDownStreamOperPath_Type()
)
ol53nnMFBMICModDownStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModDownStreamOperPath.setStatus("mandatory")


class _Ol53nnMFBMICModUpStreamOperPath_Type(Integer32):
    """Custom type ol53nnMFBMICModUpStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMFBMICModUpStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMFBMICModUpStreamOperPath_Object = MibTableColumn
ol53nnMFBMICModUpStreamOperPath = _Ol53nnMFBMICModUpStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 5),
    _Ol53nnMFBMICModUpStreamOperPath_Type()
)
ol53nnMFBMICModUpStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModUpStreamOperPath.setStatus("mandatory")


class _Ol53nnMFBMICModRingInfo_Type(OctetString):
    """Custom type ol53nnMFBMICModRingInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ol53nnMFBMICModRingInfo_Type.__name__ = "OctetString"
_Ol53nnMFBMICModRingInfo_Object = MibTableColumn
ol53nnMFBMICModRingInfo = _Ol53nnMFBMICModRingInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 6),
    _Ol53nnMFBMICModRingInfo_Type()
)
ol53nnMFBMICModRingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModRingInfo.setStatus("mandatory")
_Ol53nnMFBMICPortTable_Object = MibTable
ol53nnMFBMICPortTable = _Ol53nnMFBMICPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2)
)
if mibBuilder.loadTexts:
    ol53nnMFBMICPortTable.setStatus("mandatory")
_Ol53nnMFBMICPortEntry_Object = MibTableRow
ol53nnMFBMICPortEntry = _Ol53nnMFBMICPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1)
)
ol53nnMFBMICPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMFBMICPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol53nnMFBMICPortIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFBMICPortEntry.setStatus("mandatory")
_Ol53nnMFBMICPortSlotIndex_Type = Integer32
_Ol53nnMFBMICPortSlotIndex_Object = MibTableColumn
ol53nnMFBMICPortSlotIndex = _Ol53nnMFBMICPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 1),
    _Ol53nnMFBMICPortSlotIndex_Type()
)
ol53nnMFBMICPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortSlotIndex.setStatus("mandatory")
_Ol53nnMFBMICPortIndex_Type = Integer32
_Ol53nnMFBMICPortIndex_Object = MibTableColumn
ol53nnMFBMICPortIndex = _Ol53nnMFBMICPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 2),
    _Ol53nnMFBMICPortIndex_Type()
)
ol53nnMFBMICPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortIndex.setStatus("mandatory")


class _Ol53nnMFBMICPortConfig_Type(Integer32):
    """Custom type ol53nnMFBMICPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("master", 4),
          ("slave", 3))
    )


_Ol53nnMFBMICPortConfig_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortConfig_Object = MibTableColumn
ol53nnMFBMICPortConfig = _Ol53nnMFBMICPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 3),
    _Ol53nnMFBMICPortConfig_Type()
)
ol53nnMFBMICPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortConfig.setStatus("mandatory")


class _Ol53nnMFBMICPortPcmState_Type(Integer32):
    """Custom type ol53nnMFBMICPortPcmState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("pc0", 1),
          ("pc1", 2),
          ("pc2", 3),
          ("pc3", 4),
          ("pc4", 5),
          ("pc5", 6),
          ("pc6", 7),
          ("pc7", 8),
          ("pc8", 9),
          ("pc9", 10))
    )


_Ol53nnMFBMICPortPcmState_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortPcmState_Object = MibTableColumn
ol53nnMFBMICPortPcmState = _Ol53nnMFBMICPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 4),
    _Ol53nnMFBMICPortPcmState_Type()
)
ol53nnMFBMICPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortPcmState.setStatus("mandatory")


class _Ol53nnMFBMICPortConnectState_Type(Integer32):
    """Custom type ol53nnMFBMICPortConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_Ol53nnMFBMICPortConnectState_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortConnectState_Object = MibTableColumn
ol53nnMFBMICPortConnectState = _Ol53nnMFBMICPortConnectState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 5),
    _Ol53nnMFBMICPortConnectState_Type()
)
ol53nnMFBMICPortConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortConnectState.setStatus("mandatory")


class _Ol53nnMFBMICPortNeighbor_Type(Integer32):
    """Custom type ol53nnMFBMICPortNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("master", 4),
          ("slave", 3),
          ("unknown", 5))
    )


_Ol53nnMFBMICPortNeighbor_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortNeighbor_Object = MibTableColumn
ol53nnMFBMICPortNeighbor = _Ol53nnMFBMICPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 6),
    _Ol53nnMFBMICPortNeighbor_Type()
)
ol53nnMFBMICPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortNeighbor.setStatus("mandatory")


class _Ol53nnMFBMICPortRemoteMACIndicated_Type(Integer32):
    """Custom type ol53nnMFBMICPortRemoteMACIndicated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol53nnMFBMICPortRemoteMACIndicated_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortRemoteMACIndicated_Object = MibTableColumn
ol53nnMFBMICPortRemoteMACIndicated = _Ol53nnMFBMICPortRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 7),
    _Ol53nnMFBMICPortRemoteMACIndicated_Type()
)
ol53nnMFBMICPortRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortRemoteMACIndicated.setStatus("mandatory")


class _Ol53nnMFBMICPortBSFlag_Type(Integer32):
    """Custom type ol53nnMFBMICPortBSFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol53nnMFBMICPortBSFlag_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortBSFlag_Object = MibTableColumn
ol53nnMFBMICPortBSFlag = _Ol53nnMFBMICPortBSFlag_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 8),
    _Ol53nnMFBMICPortBSFlag_Type()
)
ol53nnMFBMICPortBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortBSFlag.setStatus("mandatory")


class _Ol53nnMFBMICPortPCWithhold_Type(Integer32):
    """Custom type ol53nnMFBMICPortPCWithhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-m", 2),
          ("none", 1),
          ("other", 3))
    )


_Ol53nnMFBMICPortPCWithhold_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortPCWithhold_Object = MibTableColumn
ol53nnMFBMICPortPCWithhold = _Ol53nnMFBMICPortPCWithhold_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 9),
    _Ol53nnMFBMICPortPCWithhold_Type()
)
ol53nnMFBMICPortPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortPCWithhold.setStatus("mandatory")


class _Ol53nnMFBMICPortLerCondition_Type(Integer32):
    """Custom type ol53nnMFBMICPortLerCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("okay", 2))
    )


_Ol53nnMFBMICPortLerCondition_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortLerCondition_Object = MibTableColumn
ol53nnMFBMICPortLerCondition = _Ol53nnMFBMICPortLerCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 10),
    _Ol53nnMFBMICPortLerCondition_Type()
)
ol53nnMFBMICPortLerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortLerCondition.setStatus("mandatory")
_Ol53nnMFBMICTrunkTable_Object = MibTable
ol53nnMFBMICTrunkTable = _Ol53nnMFBMICTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 3)
)
if mibBuilder.loadTexts:
    ol53nnMFBMICTrunkTable.setStatus("mandatory")
_Ol53nnMFBMICTrunkEntry_Object = MibTableRow
ol53nnMFBMICTrunkEntry = _Ol53nnMFBMICTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 3, 1)
)
ol53nnMFBMICTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMFBMICTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol53nnMFBMICTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFBMICTrunkEntry.setStatus("mandatory")
_Ol53nnMFBMICTrunkSlotIndex_Type = Integer32
_Ol53nnMFBMICTrunkSlotIndex_Object = MibTableColumn
ol53nnMFBMICTrunkSlotIndex = _Ol53nnMFBMICTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 3, 1, 1),
    _Ol53nnMFBMICTrunkSlotIndex_Type()
)
ol53nnMFBMICTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICTrunkSlotIndex.setStatus("mandatory")
_Ol53nnMFBMICTrunkIndex_Type = Integer32
_Ol53nnMFBMICTrunkIndex_Object = MibTableColumn
ol53nnMFBMICTrunkIndex = _Ol53nnMFBMICTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 3, 1, 2),
    _Ol53nnMFBMICTrunkIndex_Type()
)
ol53nnMFBMICTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICTrunkIndex.setStatus("mandatory")
_Ol53nnMFIBST_ObjectIdentity = ObjectIdentity
ol53nnMFIBST = _Ol53nnMFIBST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27)
)
_Ol53nnMFIBSTModTable_Object = MibTable
ol53nnMFIBSTModTable = _Ol53nnMFIBSTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1)
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTModTable.setStatus("mandatory")
_Ol53nnMFIBSTModEntry_Object = MibTableRow
ol53nnMFIBSTModEntry = _Ol53nnMFIBSTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1)
)
ol53nnMFIBSTModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMFIBSTModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTModEntry.setStatus("mandatory")
_Ol53nnMFIBSTModSlotIndex_Type = Integer32
_Ol53nnMFIBSTModSlotIndex_Object = MibTableColumn
ol53nnMFIBSTModSlotIndex = _Ol53nnMFIBSTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 1),
    _Ol53nnMFIBSTModSlotIndex_Type()
)
ol53nnMFIBSTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModSlotIndex.setStatus("mandatory")


class _Ol53nnMFIBSTModDownStreamModule_Type(Integer32):
    """Custom type ol53nnMFIBSTModDownStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMFIBSTModDownStreamModule_Type.__name__ = "Integer32"
_Ol53nnMFIBSTModDownStreamModule_Object = MibTableColumn
ol53nnMFIBSTModDownStreamModule = _Ol53nnMFIBSTModDownStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 2),
    _Ol53nnMFIBSTModDownStreamModule_Type()
)
ol53nnMFIBSTModDownStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModDownStreamModule.setStatus("mandatory")


class _Ol53nnMFIBSTModUpStreamModule_Type(Integer32):
    """Custom type ol53nnMFIBSTModUpStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMFIBSTModUpStreamModule_Type.__name__ = "Integer32"
_Ol53nnMFIBSTModUpStreamModule_Object = MibTableColumn
ol53nnMFIBSTModUpStreamModule = _Ol53nnMFIBSTModUpStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 3),
    _Ol53nnMFIBSTModUpStreamModule_Type()
)
ol53nnMFIBSTModUpStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModUpStreamModule.setStatus("mandatory")


class _Ol53nnMFIBSTModDownStreamOperPath_Type(Integer32):
    """Custom type ol53nnMFIBSTModDownStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMFIBSTModDownStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMFIBSTModDownStreamOperPath_Object = MibTableColumn
ol53nnMFIBSTModDownStreamOperPath = _Ol53nnMFIBSTModDownStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 4),
    _Ol53nnMFIBSTModDownStreamOperPath_Type()
)
ol53nnMFIBSTModDownStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModDownStreamOperPath.setStatus("mandatory")


class _Ol53nnMFIBSTModUpStreamOperPath_Type(Integer32):
    """Custom type ol53nnMFIBSTModUpStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMFIBSTModUpStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMFIBSTModUpStreamOperPath_Object = MibTableColumn
ol53nnMFIBSTModUpStreamOperPath = _Ol53nnMFIBSTModUpStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 5),
    _Ol53nnMFIBSTModUpStreamOperPath_Type()
)
ol53nnMFIBSTModUpStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModUpStreamOperPath.setStatus("mandatory")


class _Ol53nnMFIBSTModRingInfo_Type(OctetString):
    """Custom type ol53nnMFIBSTModRingInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ol53nnMFIBSTModRingInfo_Type.__name__ = "OctetString"
_Ol53nnMFIBSTModRingInfo_Object = MibTableColumn
ol53nnMFIBSTModRingInfo = _Ol53nnMFIBSTModRingInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 6),
    _Ol53nnMFIBSTModRingInfo_Type()
)
ol53nnMFIBSTModRingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModRingInfo.setStatus("mandatory")
_Ol53nnMFIBSTPortTable_Object = MibTable
ol53nnMFIBSTPortTable = _Ol53nnMFIBSTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2)
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortTable.setStatus("mandatory")
_Ol53nnMFIBSTPortEntry_Object = MibTableRow
ol53nnMFIBSTPortEntry = _Ol53nnMFIBSTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1)
)
ol53nnMFIBSTPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMFIBSTPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol53nnMFIBSTPortIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortEntry.setStatus("mandatory")
_Ol53nnMFIBSTPortSlotIndex_Type = Integer32
_Ol53nnMFIBSTPortSlotIndex_Object = MibTableColumn
ol53nnMFIBSTPortSlotIndex = _Ol53nnMFIBSTPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 1),
    _Ol53nnMFIBSTPortSlotIndex_Type()
)
ol53nnMFIBSTPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortSlotIndex.setStatus("mandatory")
_Ol53nnMFIBSTPortIndex_Type = Integer32
_Ol53nnMFIBSTPortIndex_Object = MibTableColumn
ol53nnMFIBSTPortIndex = _Ol53nnMFIBSTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 2),
    _Ol53nnMFIBSTPortIndex_Type()
)
ol53nnMFIBSTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortIndex.setStatus("mandatory")


class _Ol53nnMFIBSTPortConfig_Type(Integer32):
    """Custom type ol53nnMFIBSTPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("master", 4),
          ("slave", 3))
    )


_Ol53nnMFIBSTPortConfig_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortConfig_Object = MibTableColumn
ol53nnMFIBSTPortConfig = _Ol53nnMFIBSTPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 3),
    _Ol53nnMFIBSTPortConfig_Type()
)
ol53nnMFIBSTPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortConfig.setStatus("mandatory")


class _Ol53nnMFIBSTPortPcmState_Type(Integer32):
    """Custom type ol53nnMFIBSTPortPcmState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("pc0", 1),
          ("pc1", 2),
          ("pc2", 3),
          ("pc3", 4),
          ("pc4", 5),
          ("pc5", 6),
          ("pc6", 7),
          ("pc7", 8),
          ("pc8", 9),
          ("pc9", 10))
    )


_Ol53nnMFIBSTPortPcmState_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortPcmState_Object = MibTableColumn
ol53nnMFIBSTPortPcmState = _Ol53nnMFIBSTPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 4),
    _Ol53nnMFIBSTPortPcmState_Type()
)
ol53nnMFIBSTPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortPcmState.setStatus("mandatory")


class _Ol53nnMFIBSTPortConnectState_Type(Integer32):
    """Custom type ol53nnMFIBSTPortConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_Ol53nnMFIBSTPortConnectState_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortConnectState_Object = MibTableColumn
ol53nnMFIBSTPortConnectState = _Ol53nnMFIBSTPortConnectState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 5),
    _Ol53nnMFIBSTPortConnectState_Type()
)
ol53nnMFIBSTPortConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortConnectState.setStatus("mandatory")


class _Ol53nnMFIBSTPortNeighbor_Type(Integer32):
    """Custom type ol53nnMFIBSTPortNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("master", 4),
          ("slave", 3),
          ("unknown", 5))
    )


_Ol53nnMFIBSTPortNeighbor_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortNeighbor_Object = MibTableColumn
ol53nnMFIBSTPortNeighbor = _Ol53nnMFIBSTPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 6),
    _Ol53nnMFIBSTPortNeighbor_Type()
)
ol53nnMFIBSTPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortNeighbor.setStatus("mandatory")


class _Ol53nnMFIBSTPortRemoteMACIndicated_Type(Integer32):
    """Custom type ol53nnMFIBSTPortRemoteMACIndicated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol53nnMFIBSTPortRemoteMACIndicated_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortRemoteMACIndicated_Object = MibTableColumn
ol53nnMFIBSTPortRemoteMACIndicated = _Ol53nnMFIBSTPortRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 7),
    _Ol53nnMFIBSTPortRemoteMACIndicated_Type()
)
ol53nnMFIBSTPortRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortRemoteMACIndicated.setStatus("mandatory")


class _Ol53nnMFIBSTPortBSFlag_Type(Integer32):
    """Custom type ol53nnMFIBSTPortBSFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol53nnMFIBSTPortBSFlag_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortBSFlag_Object = MibTableColumn
ol53nnMFIBSTPortBSFlag = _Ol53nnMFIBSTPortBSFlag_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 8),
    _Ol53nnMFIBSTPortBSFlag_Type()
)
ol53nnMFIBSTPortBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortBSFlag.setStatus("mandatory")


class _Ol53nnMFIBSTPortPCWithhold_Type(Integer32):
    """Custom type ol53nnMFIBSTPortPCWithhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-m", 2),
          ("none", 1),
          ("other", 3))
    )


_Ol53nnMFIBSTPortPCWithhold_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortPCWithhold_Object = MibTableColumn
ol53nnMFIBSTPortPCWithhold = _Ol53nnMFIBSTPortPCWithhold_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 9),
    _Ol53nnMFIBSTPortPCWithhold_Type()
)
ol53nnMFIBSTPortPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortPCWithhold.setStatus("mandatory")


class _Ol53nnMFIBSTPortLerCondition_Type(Integer32):
    """Custom type ol53nnMFIBSTPortLerCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("okay", 2))
    )


_Ol53nnMFIBSTPortLerCondition_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortLerCondition_Object = MibTableColumn
ol53nnMFIBSTPortLerCondition = _Ol53nnMFIBSTPortLerCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 10),
    _Ol53nnMFIBSTPortLerCondition_Type()
)
ol53nnMFIBSTPortLerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortLerCondition.setStatus("mandatory")
_Ol53nnMFIBSTTrunkTable_Object = MibTable
ol53nnMFIBSTTrunkTable = _Ol53nnMFIBSTTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 3)
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTTrunkTable.setStatus("mandatory")
_Ol53nnMFIBSTTrunkEntry_Object = MibTableRow
ol53nnMFIBSTTrunkEntry = _Ol53nnMFIBSTTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 3, 1)
)
ol53nnMFIBSTTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMFIBSTTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol53nnMFIBSTTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTTrunkEntry.setStatus("mandatory")
_Ol53nnMFIBSTTrunkSlotIndex_Type = Integer32
_Ol53nnMFIBSTTrunkSlotIndex_Object = MibTableColumn
ol53nnMFIBSTTrunkSlotIndex = _Ol53nnMFIBSTTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 3, 1, 1),
    _Ol53nnMFIBSTTrunkSlotIndex_Type()
)
ol53nnMFIBSTTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTTrunkSlotIndex.setStatus("mandatory")
_Ol53nnMFIBSTTrunkIndex_Type = Integer32
_Ol53nnMFIBSTTrunkIndex_Object = MibTableColumn
ol53nnMFIBSTTrunkIndex = _Ol53nnMFIBSTTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 3, 1, 2),
    _Ol53nnMFIBSTTrunkIndex_Type()
)
ol53nnMFIBSTTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTTrunkIndex.setStatus("mandatory")
_Ol53nnMSTP_ObjectIdentity = ObjectIdentity
ol53nnMSTP = _Ol53nnMSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28)
)
_Ol53nnMSTPModTable_Object = MibTable
ol53nnMSTPModTable = _Ol53nnMSTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1)
)
if mibBuilder.loadTexts:
    ol53nnMSTPModTable.setStatus("mandatory")
_Ol53nnMSTPModEntry_Object = MibTableRow
ol53nnMSTPModEntry = _Ol53nnMSTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1)
)
ol53nnMSTPModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMSTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMSTPModEntry.setStatus("mandatory")
_Ol53nnMSTPModSlotIndex_Type = Integer32
_Ol53nnMSTPModSlotIndex_Object = MibTableColumn
ol53nnMSTPModSlotIndex = _Ol53nnMSTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 1),
    _Ol53nnMSTPModSlotIndex_Type()
)
ol53nnMSTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModSlotIndex.setStatus("mandatory")


class _Ol53nnMSTPModDownStreamModule_Type(Integer32):
    """Custom type ol53nnMSTPModDownStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMSTPModDownStreamModule_Type.__name__ = "Integer32"
_Ol53nnMSTPModDownStreamModule_Object = MibTableColumn
ol53nnMSTPModDownStreamModule = _Ol53nnMSTPModDownStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 2),
    _Ol53nnMSTPModDownStreamModule_Type()
)
ol53nnMSTPModDownStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModDownStreamModule.setStatus("mandatory")


class _Ol53nnMSTPModUpStreamModule_Type(Integer32):
    """Custom type ol53nnMSTPModUpStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMSTPModUpStreamModule_Type.__name__ = "Integer32"
_Ol53nnMSTPModUpStreamModule_Object = MibTableColumn
ol53nnMSTPModUpStreamModule = _Ol53nnMSTPModUpStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 3),
    _Ol53nnMSTPModUpStreamModule_Type()
)
ol53nnMSTPModUpStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModUpStreamModule.setStatus("mandatory")


class _Ol53nnMSTPModDownStreamOperPath_Type(Integer32):
    """Custom type ol53nnMSTPModDownStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMSTPModDownStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMSTPModDownStreamOperPath_Object = MibTableColumn
ol53nnMSTPModDownStreamOperPath = _Ol53nnMSTPModDownStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 4),
    _Ol53nnMSTPModDownStreamOperPath_Type()
)
ol53nnMSTPModDownStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModDownStreamOperPath.setStatus("mandatory")


class _Ol53nnMSTPModUpStreamOperPath_Type(Integer32):
    """Custom type ol53nnMSTPModUpStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMSTPModUpStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMSTPModUpStreamOperPath_Object = MibTableColumn
ol53nnMSTPModUpStreamOperPath = _Ol53nnMSTPModUpStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 5),
    _Ol53nnMSTPModUpStreamOperPath_Type()
)
ol53nnMSTPModUpStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModUpStreamOperPath.setStatus("mandatory")


class _Ol53nnMSTPModRingInfo_Type(OctetString):
    """Custom type ol53nnMSTPModRingInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ol53nnMSTPModRingInfo_Type.__name__ = "OctetString"
_Ol53nnMSTPModRingInfo_Object = MibTableColumn
ol53nnMSTPModRingInfo = _Ol53nnMSTPModRingInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 6),
    _Ol53nnMSTPModRingInfo_Type()
)
ol53nnMSTPModRingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModRingInfo.setStatus("mandatory")
_Ol53nnMSTPPortTable_Object = MibTable
ol53nnMSTPPortTable = _Ol53nnMSTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2)
)
if mibBuilder.loadTexts:
    ol53nnMSTPPortTable.setStatus("mandatory")
_Ol53nnMSTPPortEntry_Object = MibTableRow
ol53nnMSTPPortEntry = _Ol53nnMSTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1)
)
ol53nnMSTPPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMSTPPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol53nnMSTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMSTPPortEntry.setStatus("mandatory")
_Ol53nnMSTPPortSlotIndex_Type = Integer32
_Ol53nnMSTPPortSlotIndex_Object = MibTableColumn
ol53nnMSTPPortSlotIndex = _Ol53nnMSTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 1),
    _Ol53nnMSTPPortSlotIndex_Type()
)
ol53nnMSTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortSlotIndex.setStatus("mandatory")
_Ol53nnMSTPPortIndex_Type = Integer32
_Ol53nnMSTPPortIndex_Object = MibTableColumn
ol53nnMSTPPortIndex = _Ol53nnMSTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 2),
    _Ol53nnMSTPPortIndex_Type()
)
ol53nnMSTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortIndex.setStatus("mandatory")


class _Ol53nnMSTPPortConfig_Type(Integer32):
    """Custom type ol53nnMSTPPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("master", 4),
          ("slave", 3))
    )


_Ol53nnMSTPPortConfig_Type.__name__ = "Integer32"
_Ol53nnMSTPPortConfig_Object = MibTableColumn
ol53nnMSTPPortConfig = _Ol53nnMSTPPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 3),
    _Ol53nnMSTPPortConfig_Type()
)
ol53nnMSTPPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMSTPPortConfig.setStatus("mandatory")


class _Ol53nnMSTPPortPcmState_Type(Integer32):
    """Custom type ol53nnMSTPPortPcmState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("pc0", 1),
          ("pc1", 2),
          ("pc2", 3),
          ("pc3", 4),
          ("pc4", 5),
          ("pc5", 6),
          ("pc6", 7),
          ("pc7", 8),
          ("pc8", 9),
          ("pc9", 10))
    )


_Ol53nnMSTPPortPcmState_Type.__name__ = "Integer32"
_Ol53nnMSTPPortPcmState_Object = MibTableColumn
ol53nnMSTPPortPcmState = _Ol53nnMSTPPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 4),
    _Ol53nnMSTPPortPcmState_Type()
)
ol53nnMSTPPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortPcmState.setStatus("mandatory")


class _Ol53nnMSTPPortConnectState_Type(Integer32):
    """Custom type ol53nnMSTPPortConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_Ol53nnMSTPPortConnectState_Type.__name__ = "Integer32"
_Ol53nnMSTPPortConnectState_Object = MibTableColumn
ol53nnMSTPPortConnectState = _Ol53nnMSTPPortConnectState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 5),
    _Ol53nnMSTPPortConnectState_Type()
)
ol53nnMSTPPortConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortConnectState.setStatus("mandatory")


class _Ol53nnMSTPPortNeighbor_Type(Integer32):
    """Custom type ol53nnMSTPPortNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("master", 4),
          ("slave", 3),
          ("unknown", 5))
    )


_Ol53nnMSTPPortNeighbor_Type.__name__ = "Integer32"
_Ol53nnMSTPPortNeighbor_Object = MibTableColumn
ol53nnMSTPPortNeighbor = _Ol53nnMSTPPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 6),
    _Ol53nnMSTPPortNeighbor_Type()
)
ol53nnMSTPPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortNeighbor.setStatus("mandatory")


class _Ol53nnMSTPPortRemoteMACIndicated_Type(Integer32):
    """Custom type ol53nnMSTPPortRemoteMACIndicated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol53nnMSTPPortRemoteMACIndicated_Type.__name__ = "Integer32"
_Ol53nnMSTPPortRemoteMACIndicated_Object = MibTableColumn
ol53nnMSTPPortRemoteMACIndicated = _Ol53nnMSTPPortRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 7),
    _Ol53nnMSTPPortRemoteMACIndicated_Type()
)
ol53nnMSTPPortRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortRemoteMACIndicated.setStatus("mandatory")


class _Ol53nnMSTPPortBSFlag_Type(Integer32):
    """Custom type ol53nnMSTPPortBSFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol53nnMSTPPortBSFlag_Type.__name__ = "Integer32"
_Ol53nnMSTPPortBSFlag_Object = MibTableColumn
ol53nnMSTPPortBSFlag = _Ol53nnMSTPPortBSFlag_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 8),
    _Ol53nnMSTPPortBSFlag_Type()
)
ol53nnMSTPPortBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortBSFlag.setStatus("mandatory")


class _Ol53nnMSTPPortPCWithhold_Type(Integer32):
    """Custom type ol53nnMSTPPortPCWithhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-m", 2),
          ("none", 1),
          ("other", 3))
    )


_Ol53nnMSTPPortPCWithhold_Type.__name__ = "Integer32"
_Ol53nnMSTPPortPCWithhold_Object = MibTableColumn
ol53nnMSTPPortPCWithhold = _Ol53nnMSTPPortPCWithhold_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 9),
    _Ol53nnMSTPPortPCWithhold_Type()
)
ol53nnMSTPPortPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortPCWithhold.setStatus("mandatory")


class _Ol53nnMSTPPortLerCondition_Type(Integer32):
    """Custom type ol53nnMSTPPortLerCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("okay", 2))
    )


_Ol53nnMSTPPortLerCondition_Type.__name__ = "Integer32"
_Ol53nnMSTPPortLerCondition_Object = MibTableColumn
ol53nnMSTPPortLerCondition = _Ol53nnMSTPPortLerCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 10),
    _Ol53nnMSTPPortLerCondition_Type()
)
ol53nnMSTPPortLerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortLerCondition.setStatus("mandatory")


class _Ol53nnMSTPPortPersonality_Type(Integer32):
    """Custom type ol53nnMSTPPortPersonality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sddi", 1),
          ("tpddi", 2))
    )


_Ol53nnMSTPPortPersonality_Type.__name__ = "Integer32"
_Ol53nnMSTPPortPersonality_Object = MibTableColumn
ol53nnMSTPPortPersonality = _Ol53nnMSTPPortPersonality_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 11),
    _Ol53nnMSTPPortPersonality_Type()
)
ol53nnMSTPPortPersonality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMSTPPortPersonality.setStatus("mandatory")
_Ol53nnMSTPTrunkTable_Object = MibTable
ol53nnMSTPTrunkTable = _Ol53nnMSTPTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 3)
)
if mibBuilder.loadTexts:
    ol53nnMSTPTrunkTable.setStatus("mandatory")
_Ol53nnMSTPTrunkEntry_Object = MibTableRow
ol53nnMSTPTrunkEntry = _Ol53nnMSTPTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 3, 1)
)
ol53nnMSTPTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMSTPTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol53nnMSTPTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMSTPTrunkEntry.setStatus("mandatory")
_Ol53nnMSTPTrunkSlotIndex_Type = Integer32
_Ol53nnMSTPTrunkSlotIndex_Object = MibTableColumn
ol53nnMSTPTrunkSlotIndex = _Ol53nnMSTPTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 3, 1, 1),
    _Ol53nnMSTPTrunkSlotIndex_Type()
)
ol53nnMSTPTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPTrunkSlotIndex.setStatus("mandatory")
_Ol53nnMSTPTrunkIndex_Type = Integer32
_Ol53nnMSTPTrunkIndex_Object = MibTableColumn
ol53nnMSTPTrunkIndex = _Ol53nnMSTPTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 3, 1, 2),
    _Ol53nnMSTPTrunkIndex_Type()
)
ol53nnMSTPTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPTrunkIndex.setStatus("mandatory")
_Ol51nnMTPCL_ObjectIdentity = ObjectIdentity
ol51nnMTPCL = _Ol51nnMTPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29)
)
_Ol51nnMTPCLModTable_Object = MibTable
ol51nnMTPCLModTable = _Ol51nnMTPCLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTPCLModTable.setStatus("mandatory")
_Ol51nnMTPCLModEntry_Object = MibTableRow
ol51nnMTPCLModEntry = _Ol51nnMTPCLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1)
)
ol51nnMTPCLModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTPCLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPCLModEntry.setStatus("mandatory")
_Ol51nnMTPCLModSlotIndex_Type = Integer32
_Ol51nnMTPCLModSlotIndex_Object = MibTableColumn
ol51nnMTPCLModSlotIndex = _Ol51nnMTPCLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 1),
    _Ol51nnMTPCLModSlotIndex_Type()
)
ol51nnMTPCLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLModSlotIndex.setStatus("mandatory")


class _Ol51nnMTPCLModMonitorConn_Type(Integer32):
    """Custom type ol51nnMTPCLModMonitorConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connector-1", 1),
          ("connector-2", 2))
    )


_Ol51nnMTPCLModMonitorConn_Type.__name__ = "Integer32"
_Ol51nnMTPCLModMonitorConn_Object = MibTableColumn
ol51nnMTPCLModMonitorConn = _Ol51nnMTPCLModMonitorConn_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 2),
    _Ol51nnMTPCLModMonitorConn_Type()
)
ol51nnMTPCLModMonitorConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLModMonitorConn.setStatus("mandatory")


class _Ol51nnMTPCLModConn1Network_Type(Integer32):
    """Custom type ol51nnMTPCLModConn1Network based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated-1", 21),
          ("isolated-2", 22))
    )


_Ol51nnMTPCLModConn1Network_Type.__name__ = "Integer32"
_Ol51nnMTPCLModConn1Network_Object = MibTableColumn
ol51nnMTPCLModConn1Network = _Ol51nnMTPCLModConn1Network_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 3),
    _Ol51nnMTPCLModConn1Network_Type()
)
ol51nnMTPCLModConn1Network.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLModConn1Network.setStatus("mandatory")


class _Ol51nnMTPCLModConn2Network_Type(Integer32):
    """Custom type ol51nnMTPCLModConn2Network based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated-1", 21),
          ("isolated-2", 22))
    )


_Ol51nnMTPCLModConn2Network_Type.__name__ = "Integer32"
_Ol51nnMTPCLModConn2Network_Object = MibTableColumn
ol51nnMTPCLModConn2Network = _Ol51nnMTPCLModConn2Network_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 4),
    _Ol51nnMTPCLModConn2Network_Type()
)
ol51nnMTPCLModConn2Network.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLModConn2Network.setStatus("mandatory")


class _Ol51nnMTPCLModConn1DipNetwork_Type(Integer32):
    """Custom type ol51nnMTPCLModConn1DipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated-1", 21),
          ("isolated-2", 22))
    )


_Ol51nnMTPCLModConn1DipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPCLModConn1DipNetwork_Object = MibTableColumn
ol51nnMTPCLModConn1DipNetwork = _Ol51nnMTPCLModConn1DipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 5),
    _Ol51nnMTPCLModConn1DipNetwork_Type()
)
ol51nnMTPCLModConn1DipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLModConn1DipNetwork.setStatus("mandatory")


class _Ol51nnMTPCLModConn2DipNetwork_Type(Integer32):
    """Custom type ol51nnMTPCLModConn2DipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated-1", 21),
          ("isolated-2", 22))
    )


_Ol51nnMTPCLModConn2DipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPCLModConn2DipNetwork_Object = MibTableColumn
ol51nnMTPCLModConn2DipNetwork = _Ol51nnMTPCLModConn2DipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 6),
    _Ol51nnMTPCLModConn2DipNetwork_Type()
)
ol51nnMTPCLModConn2DipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLModConn2DipNetwork.setStatus("mandatory")


class _Ol51nnMTPCLModAutoPartition_Type(Integer32):
    """Custom type ol51nnMTPCLModAutoPartition based on Integer32"""
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
        *(("collisions-127", 3),
          ("collisions-255", 4),
          ("collisions-31", 1),
          ("collisions-63", 2))
    )


_Ol51nnMTPCLModAutoPartition_Type.__name__ = "Integer32"
_Ol51nnMTPCLModAutoPartition_Object = MibTableColumn
ol51nnMTPCLModAutoPartition = _Ol51nnMTPCLModAutoPartition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 7),
    _Ol51nnMTPCLModAutoPartition_Type()
)
ol51nnMTPCLModAutoPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLModAutoPartition.setStatus("mandatory")
_Ol51nnMTPCLPortTable_Object = MibTable
ol51nnMTPCLPortTable = _Ol51nnMTPCLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTPCLPortTable.setStatus("mandatory")
_Ol51nnMTPCLPortEntry_Object = MibTableRow
ol51nnMTPCLPortEntry = _Ol51nnMTPCLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1)
)
ol51nnMTPCLPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTPCLPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMTPCLPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPCLPortEntry.setStatus("mandatory")
_Ol51nnMTPCLPortSlotIndex_Type = Integer32
_Ol51nnMTPCLPortSlotIndex_Object = MibTableColumn
ol51nnMTPCLPortSlotIndex = _Ol51nnMTPCLPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 1),
    _Ol51nnMTPCLPortSlotIndex_Type()
)
ol51nnMTPCLPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortSlotIndex.setStatus("mandatory")
_Ol51nnMTPCLPortIndex_Type = Integer32
_Ol51nnMTPCLPortIndex_Object = MibTableColumn
ol51nnMTPCLPortIndex = _Ol51nnMTPCLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 2),
    _Ol51nnMTPCLPortIndex_Type()
)
ol51nnMTPCLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortIndex.setStatus("mandatory")


class _Ol51nnMTPCLPortAdminState_Type(Integer32):
    """Custom type ol51nnMTPCLPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("remote-diagnostics", 8))
    )


_Ol51nnMTPCLPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPCLPortAdminState_Object = MibTableColumn
ol51nnMTPCLPortAdminState = _Ol51nnMTPCLPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 3),
    _Ol51nnMTPCLPortAdminState_Type()
)
ol51nnMTPCLPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortAdminState.setStatus("mandatory")
_Ol51nnMTPCLPortBuddySlot_Type = Integer32
_Ol51nnMTPCLPortBuddySlot_Object = MibTableColumn
ol51nnMTPCLPortBuddySlot = _Ol51nnMTPCLPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 4),
    _Ol51nnMTPCLPortBuddySlot_Type()
)
ol51nnMTPCLPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortBuddySlot.setStatus("mandatory")
_Ol51nnMTPCLPortBuddyPort_Type = Integer32
_Ol51nnMTPCLPortBuddyPort_Object = MibTableColumn
ol51nnMTPCLPortBuddyPort = _Ol51nnMTPCLPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 5),
    _Ol51nnMTPCLPortBuddyPort_Type()
)
ol51nnMTPCLPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortBuddyPort.setStatus("mandatory")


class _Ol51nnMTPCLPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMTPCLPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPCLPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPCLPortDipAdminState_Object = MibTableColumn
ol51nnMTPCLPortDipAdminState = _Ol51nnMTPCLPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 6),
    _Ol51nnMTPCLPortDipAdminState_Type()
)
ol51nnMTPCLPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortDipAdminState.setStatus("mandatory")


class _Ol51nnMTPCLPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPCLPortLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPCLPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPCLPortLinkInteg_Object = MibTableColumn
ol51nnMTPCLPortLinkInteg = _Ol51nnMTPCLPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 7),
    _Ol51nnMTPCLPortLinkInteg_Type()
)
ol51nnMTPCLPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortLinkInteg.setStatus("mandatory")


class _Ol51nnMTPCLPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPCLPortDipLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPCLPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPCLPortDipLinkInteg_Object = MibTableColumn
ol51nnMTPCLPortDipLinkInteg = _Ol51nnMTPCLPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 8),
    _Ol51nnMTPCLPortDipLinkInteg_Type()
)
ol51nnMTPCLPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortDipLinkInteg.setStatus("mandatory")
_Ol52nnBTT_ObjectIdentity = ObjectIdentity
ol52nnBTT = _Ol52nnBTT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30)
)
_Ol52nnBTTModTable_Object = MibTable
ol52nnBTTModTable = _Ol52nnBTTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1)
)
if mibBuilder.loadTexts:
    ol52nnBTTModTable.setStatus("mandatory")
_Ol52nnBTTModEntry_Object = MibTableRow
ol52nnBTTModEntry = _Ol52nnBTTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1)
)
ol52nnBTTModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnBTTModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol52nnBTTModEntry.setStatus("mandatory")
_Ol52nnBTTModSlotIndex_Type = Integer32
_Ol52nnBTTModSlotIndex_Object = MibTableColumn
ol52nnBTTModSlotIndex = _Ol52nnBTTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1, 1),
    _Ol52nnBTTModSlotIndex_Type()
)
ol52nnBTTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTModSlotIndex.setStatus("mandatory")


class _Ol52nnBTTModBridgeType_Type(Integer32):
    """Custom type ol52nnBTTModBridgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge-type-sr", 1),
          ("bridge-type-srt", 2))
    )


_Ol52nnBTTModBridgeType_Type.__name__ = "Integer32"
_Ol52nnBTTModBridgeType_Object = MibTableColumn
ol52nnBTTModBridgeType = _Ol52nnBTTModBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1, 2),
    _Ol52nnBTTModBridgeType_Type()
)
ol52nnBTTModBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTModBridgeType.setStatus("mandatory")


class _Ol52nnBTTModSoftwareVersion_Type(DisplayString):
    """Custom type ol52nnBTTModSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Ol52nnBTTModSoftwareVersion_Type.__name__ = "DisplayString"
_Ol52nnBTTModSoftwareVersion_Object = MibTableColumn
ol52nnBTTModSoftwareVersion = _Ol52nnBTTModSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1, 3),
    _Ol52nnBTTModSoftwareVersion_Type()
)
ol52nnBTTModSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTModSoftwareVersion.setStatus("mandatory")
_Ol52nnBTTModSRBridgeNo_Type = Integer32
_Ol52nnBTTModSRBridgeNo_Object = MibTableColumn
ol52nnBTTModSRBridgeNo = _Ol52nnBTTModSRBridgeNo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1, 4),
    _Ol52nnBTTModSRBridgeNo_Type()
)
ol52nnBTTModSRBridgeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTModSRBridgeNo.setStatus("mandatory")


class _Ol52nnBTTModNetworkStatus_Type(Integer32):
    """Custom type ol52nnBTTModNetworkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("beaconing", 3),
          ("closed", 2),
          ("okay", 1))
    )


_Ol52nnBTTModNetworkStatus_Type.__name__ = "Integer32"
_Ol52nnBTTModNetworkStatus_Object = MibTableColumn
ol52nnBTTModNetworkStatus = _Ol52nnBTTModNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1, 5),
    _Ol52nnBTTModNetworkStatus_Type()
)
ol52nnBTTModNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTModNetworkStatus.setStatus("mandatory")
_Ol52nnBTTPortTable_Object = MibTable
ol52nnBTTPortTable = _Ol52nnBTTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2)
)
if mibBuilder.loadTexts:
    ol52nnBTTPortTable.setStatus("mandatory")
_Ol52nnBTTPortEntry_Object = MibTableRow
ol52nnBTTPortEntry = _Ol52nnBTTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1)
)
ol52nnBTTPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnBTTPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol52nnBTTPortIndex"),
)
if mibBuilder.loadTexts:
    ol52nnBTTPortEntry.setStatus("mandatory")
_Ol52nnBTTPortSlotIndex_Type = Integer32
_Ol52nnBTTPortSlotIndex_Object = MibTableColumn
ol52nnBTTPortSlotIndex = _Ol52nnBTTPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 1),
    _Ol52nnBTTPortSlotIndex_Type()
)
ol52nnBTTPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortSlotIndex.setStatus("mandatory")
_Ol52nnBTTPortIndex_Type = Integer32
_Ol52nnBTTPortIndex_Object = MibTableColumn
ol52nnBTTPortIndex = _Ol52nnBTTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 2),
    _Ol52nnBTTPortIndex_Type()
)
ol52nnBTTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortIndex.setStatus("mandatory")


class _Ol52nnBTTPortConnector_Type(Integer32):
    """Custom type ol52nnBTTPortConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("backPlane", 1),
          ("db-9", 10),
          ("rj45", 8))
    )


_Ol52nnBTTPortConnector_Type.__name__ = "Integer32"
_Ol52nnBTTPortConnector_Object = MibTableColumn
ol52nnBTTPortConnector = _Ol52nnBTTPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 3),
    _Ol52nnBTTPortConnector_Type()
)
ol52nnBTTPortConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnBTTPortConnector.setStatus("mandatory")


class _Ol52nnBTTPortSTAPState_Type(Integer32):
    """Custom type ol52nnBTTPortSTAPState based on Integer32"""
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
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3),
          ("off", 6))
    )


_Ol52nnBTTPortSTAPState_Type.__name__ = "Integer32"
_Ol52nnBTTPortSTAPState_Object = MibTableColumn
ol52nnBTTPortSTAPState = _Ol52nnBTTPortSTAPState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 4),
    _Ol52nnBTTPortSTAPState_Type()
)
ol52nnBTTPortSTAPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortSTAPState.setStatus("mandatory")
_Ol52nnBTTPortIpAddress_Type = IpAddress
_Ol52nnBTTPortIpAddress_Object = MibTableColumn
ol52nnBTTPortIpAddress = _Ol52nnBTTPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 5),
    _Ol52nnBTTPortIpAddress_Type()
)
ol52nnBTTPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortIpAddress.setStatus("mandatory")


class _Ol52nnBTTPortMACAddress_Type(OctetString):
    """Custom type ol52nnBTTPortMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol52nnBTTPortMACAddress_Type.__name__ = "OctetString"
_Ol52nnBTTPortMACAddress_Object = MibTableColumn
ol52nnBTTPortMACAddress = _Ol52nnBTTPortMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 6),
    _Ol52nnBTTPortMACAddress_Type()
)
ol52nnBTTPortMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortMACAddress.setStatus("mandatory")
_Ol52nnBTTPortThroughput_Type = Gauge32
_Ol52nnBTTPortThroughput_Object = MibTableColumn
ol52nnBTTPortThroughput = _Ol52nnBTTPortThroughput_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 7),
    _Ol52nnBTTPortThroughput_Type()
)
ol52nnBTTPortThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortThroughput.setStatus("mandatory")
_Ol52nnBTTPortForwarding_Type = Gauge32
_Ol52nnBTTPortForwarding_Object = MibTableColumn
ol52nnBTTPortForwarding = _Ol52nnBTTPortForwarding_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 8),
    _Ol52nnBTTPortForwarding_Type()
)
ol52nnBTTPortForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortForwarding.setStatus("mandatory")
_Ol52nnBTTPortSRRingNo_Type = Integer32
_Ol52nnBTTPortSRRingNo_Object = MibTableColumn
ol52nnBTTPortSRRingNo = _Ol52nnBTTPortSRRingNo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 9),
    _Ol52nnBTTPortSRRingNo_Type()
)
ol52nnBTTPortSRRingNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortSRRingNo.setStatus("mandatory")


class _Ol52nnBTTPortRingSpeed_Type(Integer32):
    """Custom type ol52nnBTTPortRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnBTTPortRingSpeed_Type.__name__ = "Integer32"
_Ol52nnBTTPortRingSpeed_Object = MibTableColumn
ol52nnBTTPortRingSpeed = _Ol52nnBTTPortRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 10),
    _Ol52nnBTTPortRingSpeed_Type()
)
ol52nnBTTPortRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnBTTPortRingSpeed.setStatus("mandatory")
_Ol52nnBTTTrunkTable_Object = MibTable
ol52nnBTTTrunkTable = _Ol52nnBTTTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 3)
)
if mibBuilder.loadTexts:
    ol52nnBTTTrunkTable.setStatus("mandatory")
_Ol52nnBTTTrunkEntry_Object = MibTableRow
ol52nnBTTTrunkEntry = _Ol52nnBTTTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 3, 1)
)
ol52nnBTTTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnBTTTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol52nnBTTTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol52nnBTTTrunkEntry.setStatus("mandatory")
_Ol52nnBTTTrunkSlotIndex_Type = Integer32
_Ol52nnBTTTrunkSlotIndex_Object = MibTableColumn
ol52nnBTTTrunkSlotIndex = _Ol52nnBTTTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 3, 1, 1),
    _Ol52nnBTTTrunkSlotIndex_Type()
)
ol52nnBTTTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTTrunkSlotIndex.setStatus("mandatory")
_Ol52nnBTTTrunkIndex_Type = Integer32
_Ol52nnBTTTrunkIndex_Object = MibTableColumn
ol52nnBTTTrunkIndex = _Ol52nnBTTTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 3, 1, 2),
    _Ol52nnBTTTrunkIndex_Type()
)
ol52nnBTTTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTTrunkIndex.setStatus("mandatory")
_Ol51nnIx_ObjectIdentity = ObjectIdentity
ol51nnIx = _Ol51nnIx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31)
)
_Ol51nnIxModTable_Object = MibTable
ol51nnIxModTable = _Ol51nnIxModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1)
)
if mibBuilder.loadTexts:
    ol51nnIxModTable.setStatus("mandatory")
_Ol51nnIxModEntry_Object = MibTableRow
ol51nnIxModEntry = _Ol51nnIxModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1)
)
ol51nnIxModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnIxModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnIxModEntry.setStatus("mandatory")
_Ol51nnIxModSlotIndex_Type = Integer32
_Ol51nnIxModSlotIndex_Object = MibTableColumn
ol51nnIxModSlotIndex = _Ol51nnIxModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1, 1),
    _Ol51nnIxModSlotIndex_Type()
)
ol51nnIxModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxModSlotIndex.setStatus("mandatory")


class _Ol51nnIxModSwType_Type(Integer32):
    """Custom type ol51nnIxModSwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("router", 3),
          ("switch", 2))
    )


_Ol51nnIxModSwType_Type.__name__ = "Integer32"
_Ol51nnIxModSwType_Object = MibTableColumn
ol51nnIxModSwType = _Ol51nnIxModSwType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1, 2),
    _Ol51nnIxModSwType_Type()
)
ol51nnIxModSwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxModSwType.setStatus("mandatory")


class _Ol51nnIxModStationAddr_Type(OctetString):
    """Custom type ol51nnIxModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnIxModStationAddr_Type.__name__ = "OctetString"
_Ol51nnIxModStationAddr_Object = MibTableColumn
ol51nnIxModStationAddr = _Ol51nnIxModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1, 3),
    _Ol51nnIxModStationAddr_Type()
)
ol51nnIxModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxModStationAddr.setStatus("mandatory")


class _Ol51nnIxModDipPromDefaults_Type(Integer32):
    """Custom type ol51nnIxModDipPromDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol51nnIxModDipPromDefaults_Type.__name__ = "Integer32"
_Ol51nnIxModDipPromDefaults_Object = MibTableColumn
ol51nnIxModDipPromDefaults = _Ol51nnIxModDipPromDefaults_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1, 4),
    _Ol51nnIxModDipPromDefaults_Type()
)
ol51nnIxModDipPromDefaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxModDipPromDefaults.setStatus("mandatory")
_Ol51nnIxModProtocols_Type = DisplayString
_Ol51nnIxModProtocols_Object = MibTableColumn
ol51nnIxModProtocols = _Ol51nnIxModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1, 5),
    _Ol51nnIxModProtocols_Type()
)
ol51nnIxModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxModProtocols.setStatus("mandatory")
_Ol51nnIxPortTable_Object = MibTable
ol51nnIxPortTable = _Ol51nnIxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2)
)
if mibBuilder.loadTexts:
    ol51nnIxPortTable.setStatus("mandatory")
_Ol51nnIxPortEntry_Object = MibTableRow
ol51nnIxPortEntry = _Ol51nnIxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1)
)
ol51nnIxPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnIxPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnIxPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnIxPortEntry.setStatus("mandatory")
_Ol51nnIxPortSlotIndex_Type = Integer32
_Ol51nnIxPortSlotIndex_Object = MibTableColumn
ol51nnIxPortSlotIndex = _Ol51nnIxPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 1),
    _Ol51nnIxPortSlotIndex_Type()
)
ol51nnIxPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortSlotIndex.setStatus("mandatory")
_Ol51nnIxPortIndex_Type = Integer32
_Ol51nnIxPortIndex_Object = MibTableColumn
ol51nnIxPortIndex = _Ol51nnIxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 2),
    _Ol51nnIxPortIndex_Type()
)
ol51nnIxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortIndex.setStatus("mandatory")


class _Ol51nnIxPortDipAdminState_Type(Integer32):
    """Custom type ol51nnIxPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnIxPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnIxPortDipAdminState_Object = MibTableColumn
ol51nnIxPortDipAdminState = _Ol51nnIxPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 3),
    _Ol51nnIxPortDipAdminState_Type()
)
ol51nnIxPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortDipAdminState.setStatus("mandatory")


class _Ol51nnIxPortSTAPState_Type(Integer32):
    """Custom type ol51nnIxPortSTAPState based on Integer32"""
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
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3),
          ("off", 6),
          ("unknown", 7))
    )


_Ol51nnIxPortSTAPState_Type.__name__ = "Integer32"
_Ol51nnIxPortSTAPState_Object = MibTableColumn
ol51nnIxPortSTAPState = _Ol51nnIxPortSTAPState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 4),
    _Ol51nnIxPortSTAPState_Type()
)
ol51nnIxPortSTAPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortSTAPState.setStatus("mandatory")
_Ol51nnIxPortIpAddress_Type = IpAddress
_Ol51nnIxPortIpAddress_Object = MibTableColumn
ol51nnIxPortIpAddress = _Ol51nnIxPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 5),
    _Ol51nnIxPortIpAddress_Type()
)
ol51nnIxPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortIpAddress.setStatus("mandatory")


class _Ol51nnIxPortDipNetwork_Type(Integer32):
    """Custom type ol51nnIxPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnIxPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnIxPortDipNetwork_Object = MibTableColumn
ol51nnIxPortDipNetwork = _Ol51nnIxPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 6),
    _Ol51nnIxPortDipNetwork_Type()
)
ol51nnIxPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortDipNetwork.setStatus("mandatory")


class _Ol51nnIxPortDefNetwork_Type(Integer32):
    """Custom type ol51nnIxPortDefNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnIxPortDefNetwork_Type.__name__ = "Integer32"
_Ol51nnIxPortDefNetwork_Object = MibTableColumn
ol51nnIxPortDefNetwork = _Ol51nnIxPortDefNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 7),
    _Ol51nnIxPortDefNetwork_Type()
)
ol51nnIxPortDefNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortDefNetwork.setStatus("mandatory")
_Ol52nnMMGT_ObjectIdentity = ObjectIdentity
ol52nnMMGT = _Ol52nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32)
)
_Ol52nnMMGTModTable_Object = MibTable
ol52nnMMGTModTable = _Ol52nnMMGTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1)
)
if mibBuilder.loadTexts:
    ol52nnMMGTModTable.setStatus("mandatory")
_Ol52nnMMGTModEntry_Object = MibTableRow
ol52nnMMGTModEntry = _Ol52nnMMGTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1)
)
ol52nnMMGTModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMMGTModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMMGTModEntry.setStatus("mandatory")
_Ol52nnMMGTModSlotIndex_Type = Integer32
_Ol52nnMMGTModSlotIndex_Object = MibTableColumn
ol52nnMMGTModSlotIndex = _Ol52nnMMGTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 1),
    _Ol52nnMMGTModSlotIndex_Type()
)
ol52nnMMGTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTModSlotIndex.setStatus("mandatory")


class _Ol52nnMMGTModMasterPriority_Type(Integer32):
    """Custom type ol52nnMMGTModMasterPriority based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("nine", 9),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("ten", 10),
          ("three", 3),
          ("two", 2))
    )


_Ol52nnMMGTModMasterPriority_Type.__name__ = "Integer32"
_Ol52nnMMGTModMasterPriority_Object = MibTableColumn
ol52nnMMGTModMasterPriority = _Ol52nnMMGTModMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 2),
    _Ol52nnMMGTModMasterPriority_Type()
)
ol52nnMMGTModMasterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTModMasterPriority.setStatus("mandatory")


class _Ol52nnMMGTModMasterStatus_Type(Integer32):
    """Custom type ol52nnMMGTModMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("electing", 3),
          ("master", 1),
          ("non-master", 2))
    )


_Ol52nnMMGTModMasterStatus_Type.__name__ = "Integer32"
_Ol52nnMMGTModMasterStatus_Object = MibTableColumn
ol52nnMMGTModMasterStatus = _Ol52nnMMGTModMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 3),
    _Ol52nnMMGTModMasterStatus_Type()
)
ol52nnMMGTModMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTModMasterStatus.setStatus("mandatory")
_Ol52nnMMGTModStationAddr_Type = OctetString
_Ol52nnMMGTModStationAddr_Object = MibTableColumn
ol52nnMMGTModStationAddr = _Ol52nnMMGTModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 4),
    _Ol52nnMMGTModStationAddr_Type()
)
ol52nnMMGTModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTModStationAddr.setStatus("mandatory")


class _Ol52nnMMGTModRingSpeed_Type(Integer32):
    """Custom type ol52nnMMGTModRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMMGTModRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMMGTModRingSpeed_Object = MibTableColumn
ol52nnMMGTModRingSpeed = _Ol52nnMMGTModRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 5),
    _Ol52nnMMGTModRingSpeed_Type()
)
ol52nnMMGTModRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTModRingSpeed.setStatus("mandatory")


class _Ol52nnMMGTModNetworkStatus_Type(Integer32):
    """Custom type ol52nnMMGTModNetworkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("beaconing", 3),
          ("closed", 2),
          ("okay", 1))
    )


_Ol52nnMMGTModNetworkStatus_Type.__name__ = "Integer32"
_Ol52nnMMGTModNetworkStatus_Object = MibTableColumn
ol52nnMMGTModNetworkStatus = _Ol52nnMMGTModNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 6),
    _Ol52nnMMGTModNetworkStatus_Type()
)
ol52nnMMGTModNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTModNetworkStatus.setStatus("mandatory")


class _Ol52nnMMGTModMasterNetwork_Type(Integer32):
    """Custom type ol52nnMMGTModMasterNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              25)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("no-change", 25),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_Ol52nnMMGTModMasterNetwork_Type.__name__ = "Integer32"
_Ol52nnMMGTModMasterNetwork_Object = MibTableColumn
ol52nnMMGTModMasterNetwork = _Ol52nnMMGTModMasterNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 7),
    _Ol52nnMMGTModMasterNetwork_Type()
)
ol52nnMMGTModMasterNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTModMasterNetwork.setStatus("mandatory")
_Ol52nnMMGTModLocalMACAddress_Type = MacAddress
_Ol52nnMMGTModLocalMACAddress_Object = MibTableColumn
ol52nnMMGTModLocalMACAddress = _Ol52nnMMGTModLocalMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 8),
    _Ol52nnMMGTModLocalMACAddress_Type()
)
ol52nnMMGTModLocalMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTModLocalMACAddress.setStatus("mandatory")


class _Ol52nnMMGTModMACAddressType_Type(Integer32):
    """Custom type ol52nnMMGTModMACAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("burned-in", 1),
          ("locally-administered", 2))
    )


_Ol52nnMMGTModMACAddressType_Type.__name__ = "Integer32"
_Ol52nnMMGTModMACAddressType_Object = MibTableColumn
ol52nnMMGTModMACAddressType = _Ol52nnMMGTModMACAddressType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 9),
    _Ol52nnMMGTModMACAddressType_Type()
)
ol52nnMMGTModMACAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTModMACAddressType.setStatus("mandatory")
_Ol52nnMMGTModActiveMACAddress_Type = MacAddress
_Ol52nnMMGTModActiveMACAddress_Object = MibTableColumn
ol52nnMMGTModActiveMACAddress = _Ol52nnMMGTModActiveMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 10),
    _Ol52nnMMGTModActiveMACAddress_Type()
)
ol52nnMMGTModActiveMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTModActiveMACAddress.setStatus("mandatory")
_Ol52nnMMGTPortTable_Object = MibTable
ol52nnMMGTPortTable = _Ol52nnMMGTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 2)
)
if mibBuilder.loadTexts:
    ol52nnMMGTPortTable.setStatus("mandatory")
_Ol52nnMMGTPortEntry_Object = MibTableRow
ol52nnMMGTPortEntry = _Ol52nnMMGTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 2, 1)
)
ol52nnMMGTPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMMGTPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol52nnMMGTPortIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMMGTPortEntry.setStatus("mandatory")
_Ol52nnMMGTPortSlotIndex_Type = Integer32
_Ol52nnMMGTPortSlotIndex_Object = MibTableColumn
ol52nnMMGTPortSlotIndex = _Ol52nnMMGTPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 2, 1, 1),
    _Ol52nnMMGTPortSlotIndex_Type()
)
ol52nnMMGTPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTPortSlotIndex.setStatus("mandatory")
_Ol52nnMMGTPortIndex_Type = Integer32
_Ol52nnMMGTPortIndex_Object = MibTableColumn
ol52nnMMGTPortIndex = _Ol52nnMMGTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 2, 1, 2),
    _Ol52nnMMGTPortIndex_Type()
)
ol52nnMMGTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTPortIndex.setStatus("mandatory")
_Ol52nnMMGTPortIpAddress_Type = IpAddress
_Ol52nnMMGTPortIpAddress_Object = MibTableColumn
ol52nnMMGTPortIpAddress = _Ol52nnMMGTPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 2, 1, 3),
    _Ol52nnMMGTPortIpAddress_Type()
)
ol52nnMMGTPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTPortIpAddress.setStatus("mandatory")
_Ol52nnMMGTTrunkTable_Object = MibTable
ol52nnMMGTTrunkTable = _Ol52nnMMGTTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3)
)
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkTable.setStatus("mandatory")
_Ol52nnMMGTTrunkEntry_Object = MibTableRow
ol52nnMMGTTrunkEntry = _Ol52nnMMGTTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1)
)
ol52nnMMGTTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMMGTTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol52nnMMGTTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkEntry.setStatus("mandatory")
_Ol52nnMMGTTrunkSlotIndex_Type = Integer32
_Ol52nnMMGTTrunkSlotIndex_Object = MibTableColumn
ol52nnMMGTTrunkSlotIndex = _Ol52nnMMGTTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1, 1),
    _Ol52nnMMGTTrunkSlotIndex_Type()
)
ol52nnMMGTTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkSlotIndex.setStatus("mandatory")
_Ol52nnMMGTTrunkIndex_Type = Integer32
_Ol52nnMMGTTrunkIndex_Object = MibTableColumn
ol52nnMMGTTrunkIndex = _Ol52nnMMGTTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1, 2),
    _Ol52nnMMGTTrunkIndex_Type()
)
ol52nnMMGTTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkIndex.setStatus("mandatory")


class _Ol52nnMMGTTrunkCableMon_Type(Integer32):
    """Custom type ol52nnMMGTTrunkCableMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notApplicable", 3))
    )


_Ol52nnMMGTTrunkCableMon_Type.__name__ = "Integer32"
_Ol52nnMMGTTrunkCableMon_Object = MibTableColumn
ol52nnMMGTTrunkCableMon = _Ol52nnMMGTTrunkCableMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1, 3),
    _Ol52nnMMGTTrunkCableMon_Type()
)
ol52nnMMGTTrunkCableMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkCableMon.setStatus("mandatory")


class _Ol52nnMMGTTrunkNetMapState_Type(Integer32):
    """Custom type ol52nnMMGTTrunkNetMapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("notApplicable", 1))
    )


_Ol52nnMMGTTrunkNetMapState_Type.__name__ = "Integer32"
_Ol52nnMMGTTrunkNetMapState_Object = MibTableColumn
ol52nnMMGTTrunkNetMapState = _Ol52nnMMGTTrunkNetMapState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1, 4),
    _Ol52nnMMGTTrunkNetMapState_Type()
)
ol52nnMMGTTrunkNetMapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkNetMapState.setStatus("mandatory")


class _Ol52nnMMGTTrunkExtBcnRecovery_Type(Integer32):
    """Custom type ol52nnMMGTTrunkExtBcnRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exists", 1),
          ("nonExists", 2),
          ("notApplicable", 3))
    )


_Ol52nnMMGTTrunkExtBcnRecovery_Type.__name__ = "Integer32"
_Ol52nnMMGTTrunkExtBcnRecovery_Object = MibTableColumn
ol52nnMMGTTrunkExtBcnRecovery = _Ol52nnMMGTTrunkExtBcnRecovery_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1, 5),
    _Ol52nnMMGTTrunkExtBcnRecovery_Type()
)
ol52nnMMGTTrunkExtBcnRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkExtBcnRecovery.setStatus("mandatory")
_Ol50nnMHCTL_ObjectIdentity = ObjectIdentity
ol50nnMHCTL = _Ol50nnMHCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33)
)
_Ol50nnMHCTLModTable_Object = MibTable
ol50nnMHCTLModTable = _Ol50nnMHCTLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1)
)
if mibBuilder.loadTexts:
    ol50nnMHCTLModTable.setStatus("mandatory")
_Ol50nnMHCTLModEntry_Object = MibTableRow
ol50nnMHCTLModEntry = _Ol50nnMHCTLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1)
)
ol50nnMHCTLModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol50nnMHCTLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol50nnMHCTLModEntry.setStatus("mandatory")
_Ol50nnMHCTLModSlotIndex_Type = Integer32
_Ol50nnMHCTLModSlotIndex_Object = MibTableColumn
ol50nnMHCTLModSlotIndex = _Ol50nnMHCTLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 1),
    _Ol50nnMHCTLModSlotIndex_Type()
)
ol50nnMHCTLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModSlotIndex.setStatus("mandatory")


class _Ol50nnMHCTLModOperState_Type(Integer32):
    """Custom type ol50nnMHCTLModOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_Ol50nnMHCTLModOperState_Type.__name__ = "Integer32"
_Ol50nnMHCTLModOperState_Object = MibTableColumn
ol50nnMHCTLModOperState = _Ol50nnMHCTLModOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 2),
    _Ol50nnMHCTLModOperState_Type()
)
ol50nnMHCTLModOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModOperState.setStatus("mandatory")


class _Ol50nnMHCTLModClockStatus_Type(Integer32):
    """Custom type ol50nnMHCTLModClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1))
    )


_Ol50nnMHCTLModClockStatus_Type.__name__ = "Integer32"
_Ol50nnMHCTLModClockStatus_Object = MibTableColumn
ol50nnMHCTLModClockStatus = _Ol50nnMHCTLModClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 3),
    _Ol50nnMHCTLModClockStatus_Type()
)
ol50nnMHCTLModClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModClockStatus.setStatus("mandatory")


class _Ol50nnMHCTLModTempStatus_Type(Integer32):
    """Custom type ol50nnMHCTLModTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1))
    )


_Ol50nnMHCTLModTempStatus_Type.__name__ = "Integer32"
_Ol50nnMHCTLModTempStatus_Object = MibTableColumn
ol50nnMHCTLModTempStatus = _Ol50nnMHCTLModTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 4),
    _Ol50nnMHCTLModTempStatus_Type()
)
ol50nnMHCTLModTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModTempStatus.setStatus("mandatory")


class _Ol50nnMHCTLModPDBStatus_Type(Integer32):
    """Custom type ol50nnMHCTLModPDBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_Ol50nnMHCTLModPDBStatus_Type.__name__ = "Integer32"
_Ol50nnMHCTLModPDBStatus_Object = MibTableColumn
ol50nnMHCTLModPDBStatus = _Ol50nnMHCTLModPDBStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 5),
    _Ol50nnMHCTLModPDBStatus_Type()
)
ol50nnMHCTLModPDBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModPDBStatus.setStatus("mandatory")


class _Ol50nnMHCTLModDipCh1ActCol_Type(Integer32):
    """Custom type ol50nnMHCTLModDipCh1ActCol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol50nnMHCTLModDipCh1ActCol_Type.__name__ = "Integer32"
_Ol50nnMHCTLModDipCh1ActCol_Object = MibTableColumn
ol50nnMHCTLModDipCh1ActCol = _Ol50nnMHCTLModDipCh1ActCol_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 6),
    _Ol50nnMHCTLModDipCh1ActCol_Type()
)
ol50nnMHCTLModDipCh1ActCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModDipCh1ActCol.setStatus("mandatory")


class _Ol50nnMHCTLModDipCh2ActCol_Type(Integer32):
    """Custom type ol50nnMHCTLModDipCh2ActCol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol50nnMHCTLModDipCh2ActCol_Type.__name__ = "Integer32"
_Ol50nnMHCTLModDipCh2ActCol_Object = MibTableColumn
ol50nnMHCTLModDipCh2ActCol = _Ol50nnMHCTLModDipCh2ActCol_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 7),
    _Ol50nnMHCTLModDipCh2ActCol_Type()
)
ol50nnMHCTLModDipCh2ActCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModDipCh2ActCol.setStatus("mandatory")


class _Ol50nnMHCTLModDipCh3ActCol_Type(Integer32):
    """Custom type ol50nnMHCTLModDipCh3ActCol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol50nnMHCTLModDipCh3ActCol_Type.__name__ = "Integer32"
_Ol50nnMHCTLModDipCh3ActCol_Object = MibTableColumn
ol50nnMHCTLModDipCh3ActCol = _Ol50nnMHCTLModDipCh3ActCol_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 8),
    _Ol50nnMHCTLModDipCh3ActCol_Type()
)
ol50nnMHCTLModDipCh3ActCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModDipCh3ActCol.setStatus("mandatory")
_Oc61nnMCAR_ObjectIdentity = ObjectIdentity
oc61nnMCAR = _Oc61nnMCAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 35)
)
_Oc61nnMCARModTable_Object = MibTable
oc61nnMCARModTable = _Oc61nnMCARModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 35, 6)
)
if mibBuilder.loadTexts:
    oc61nnMCARModTable.setStatus("mandatory")
_Oc61nnMCARModEntry_Object = MibTableRow
oc61nnMCARModEntry = _Oc61nnMCARModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 35, 6, 1)
)
oc61nnMCARModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "oc61nnMCARModSlotIndex"),
    (0, "CHIPCOMMIB", "oc61nnMCARModSubSlotIndex"),
)
if mibBuilder.loadTexts:
    oc61nnMCARModEntry.setStatus("mandatory")
_Oc61nnMCARModSlotIndex_Type = Integer32
_Oc61nnMCARModSlotIndex_Object = MibTableColumn
oc61nnMCARModSlotIndex = _Oc61nnMCARModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 35, 6, 1, 1),
    _Oc61nnMCARModSlotIndex_Type()
)
oc61nnMCARModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMCARModSlotIndex.setStatus("mandatory")
_Oc61nnMCARModSubSlotIndex_Type = Integer32
_Oc61nnMCARModSubSlotIndex_Object = MibTableColumn
oc61nnMCARModSubSlotIndex = _Oc61nnMCARModSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 35, 6, 1, 2),
    _Oc61nnMCARModSubSlotIndex_Type()
)
oc61nnMCARModSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMCARModSubSlotIndex.setStatus("mandatory")


class _Oc61nnMCARModBootVersion_Type(DisplayString):
    """Custom type oc61nnMCARModBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Oc61nnMCARModBootVersion_Type.__name__ = "DisplayString"
_Oc61nnMCARModBootVersion_Object = MibTableColumn
oc61nnMCARModBootVersion = _Oc61nnMCARModBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 35, 6, 1, 3),
    _Oc61nnMCARModBootVersion_Type()
)
oc61nnMCARModBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMCARModBootVersion.setStatus("mandatory")
_Oc60nnMMGT_ObjectIdentity = ObjectIdentity
oc60nnMMGT = _Oc60nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 43)
)
_Oc60nnMMGTModTable_Object = MibTable
oc60nnMMGTModTable = _Oc60nnMMGTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 43, 6)
)
if mibBuilder.loadTexts:
    oc60nnMMGTModTable.setStatus("mandatory")
_Oc60nnMMGTModEntry_Object = MibTableRow
oc60nnMMGTModEntry = _Oc60nnMMGTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 43, 6, 1)
)
oc60nnMMGTModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "oc60nnMMGTModSlotIndex"),
    (0, "CHIPCOMMIB", "oc60nnMMGTModSubSlotIndex"),
)
if mibBuilder.loadTexts:
    oc60nnMMGTModEntry.setStatus("mandatory")
_Oc60nnMMGTModSlotIndex_Type = Integer32
_Oc60nnMMGTModSlotIndex_Object = MibTableColumn
oc60nnMMGTModSlotIndex = _Oc60nnMMGTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 43, 6, 1, 1),
    _Oc60nnMMGTModSlotIndex_Type()
)
oc60nnMMGTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMMGTModSlotIndex.setStatus("mandatory")
_Oc60nnMMGTModSubSlotIndex_Type = Integer32
_Oc60nnMMGTModSubSlotIndex_Object = MibTableColumn
oc60nnMMGTModSubSlotIndex = _Oc60nnMMGTModSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 43, 6, 1, 2),
    _Oc60nnMMGTModSubSlotIndex_Type()
)
oc60nnMMGTModSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMMGTModSubSlotIndex.setStatus("mandatory")


class _Oc60nnMMGTModBootVersion_Type(DisplayString):
    """Custom type oc60nnMMGTModBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Oc60nnMMGTModBootVersion_Type.__name__ = "DisplayString"
_Oc60nnMMGTModBootVersion_Object = MibTableColumn
oc60nnMMGTModBootVersion = _Oc60nnMMGTModBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 43, 6, 1, 3),
    _Oc60nnMMGTModBootVersion_Type()
)
oc60nnMMGTModBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMMGTModBootVersion.setStatus("mandatory")


class _Oc60nnMMGTModMasterPriority_Type(Integer32):
    """Custom type oc60nnMMGTModMasterPriority based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("nine", 9),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("ten", 10),
          ("three", 3),
          ("two", 2))
    )


_Oc60nnMMGTModMasterPriority_Type.__name__ = "Integer32"
_Oc60nnMMGTModMasterPriority_Object = MibTableColumn
oc60nnMMGTModMasterPriority = _Oc60nnMMGTModMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 43, 6, 1, 4),
    _Oc60nnMMGTModMasterPriority_Type()
)
oc60nnMMGTModMasterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc60nnMMGTModMasterPriority.setStatus("mandatory")


class _Oc60nnMMGTModMasterStatus_Type(Integer32):
    """Custom type oc60nnMMGTModMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("electing", 3),
          ("master", 1),
          ("non-master", 2))
    )


_Oc60nnMMGTModMasterStatus_Type.__name__ = "Integer32"
_Oc60nnMMGTModMasterStatus_Object = MibTableColumn
oc60nnMMGTModMasterStatus = _Oc60nnMMGTModMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 43, 6, 1, 5),
    _Oc60nnMMGTModMasterStatus_Type()
)
oc60nnMMGTModMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMMGTModMasterStatus.setStatus("mandatory")
_Oc60nnMMGTModHubSerial_Type = DisplayString
_Oc60nnMMGTModHubSerial_Object = MibTableColumn
oc60nnMMGTModHubSerial = _Oc60nnMMGTModHubSerial_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 43, 6, 1, 6),
    _Oc60nnMMGTModHubSerial_Type()
)
oc60nnMMGTModHubSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMMGTModHubSerial.setStatus("mandatory")
_Oc61nnDMGT_ObjectIdentity = ObjectIdentity
oc61nnDMGT = _Oc61nnDMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45)
)
_Oc61nnDMGTModTable_Object = MibTable
oc61nnDMGTModTable = _Oc61nnDMGTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6)
)
if mibBuilder.loadTexts:
    oc61nnDMGTModTable.setStatus("mandatory")
_Oc61nnDMGTModEntry_Object = MibTableRow
oc61nnDMGTModEntry = _Oc61nnDMGTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6, 1)
)
oc61nnDMGTModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "oc61nnDMGTModSlotIndex"),
    (0, "CHIPCOMMIB", "oc61nnDMGTModSubSlotIndex"),
)
if mibBuilder.loadTexts:
    oc61nnDMGTModEntry.setStatus("mandatory")
_Oc61nnDMGTModSlotIndex_Type = Integer32
_Oc61nnDMGTModSlotIndex_Object = MibTableColumn
oc61nnDMGTModSlotIndex = _Oc61nnDMGTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6, 1, 1),
    _Oc61nnDMGTModSlotIndex_Type()
)
oc61nnDMGTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnDMGTModSlotIndex.setStatus("mandatory")
_Oc61nnDMGTModSubSlotIndex_Type = Integer32
_Oc61nnDMGTModSubSlotIndex_Object = MibTableColumn
oc61nnDMGTModSubSlotIndex = _Oc61nnDMGTModSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6, 1, 2),
    _Oc61nnDMGTModSubSlotIndex_Type()
)
oc61nnDMGTModSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnDMGTModSubSlotIndex.setStatus("mandatory")


class _Oc61nnDMGTModBootVersion_Type(DisplayString):
    """Custom type oc61nnDMGTModBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Oc61nnDMGTModBootVersion_Type.__name__ = "DisplayString"
_Oc61nnDMGTModBootVersion_Object = MibTableColumn
oc61nnDMGTModBootVersion = _Oc61nnDMGTModBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6, 1, 3),
    _Oc61nnDMGTModBootVersion_Type()
)
oc61nnDMGTModBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnDMGTModBootVersion.setStatus("mandatory")
_Oc61nnDMGTModIpAddress_Type = IpAddress
_Oc61nnDMGTModIpAddress_Object = MibTableColumn
oc61nnDMGTModIpAddress = _Oc61nnDMGTModIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6, 1, 4),
    _Oc61nnDMGTModIpAddress_Type()
)
oc61nnDMGTModIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnDMGTModIpAddress.setStatus("mandatory")
_Oc61nnDMGTModSubnetMask_Type = IpAddress
_Oc61nnDMGTModSubnetMask_Object = MibTableColumn
oc61nnDMGTModSubnetMask = _Oc61nnDMGTModSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6, 1, 5),
    _Oc61nnDMGTModSubnetMask_Type()
)
oc61nnDMGTModSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnDMGTModSubnetMask.setStatus("mandatory")
_Oc61nnDMGTModDefaultGateway_Type = IpAddress
_Oc61nnDMGTModDefaultGateway_Object = MibTableColumn
oc61nnDMGTModDefaultGateway = _Oc61nnDMGTModDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6, 1, 6),
    _Oc61nnDMGTModDefaultGateway_Type()
)
oc61nnDMGTModDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnDMGTModDefaultGateway.setStatus("mandatory")
_Oc61nnDMGTModStationAddr_Type = MacAddress
_Oc61nnDMGTModStationAddr_Object = MibTableColumn
oc61nnDMGTModStationAddr = _Oc61nnDMGTModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6, 1, 7),
    _Oc61nnDMGTModStationAddr_Type()
)
oc61nnDMGTModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnDMGTModStationAddr.setStatus("mandatory")


class _Oc61nnDMGTModInterfaceMode_Type(Integer32):
    """Custom type oc61nnDMGTModInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("standby", 3))
    )


_Oc61nnDMGTModInterfaceMode_Type.__name__ = "Integer32"
_Oc61nnDMGTModInterfaceMode_Object = MibTableColumn
oc61nnDMGTModInterfaceMode = _Oc61nnDMGTModInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6, 1, 8),
    _Oc61nnDMGTModInterfaceMode_Type()
)
oc61nnDMGTModInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnDMGTModInterfaceMode.setStatus("mandatory")


class _Oc61nnDMGTModRMONHostStatsMode_Type(Integer32):
    """Custom type oc61nnDMGTModRMONHostStatsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Oc61nnDMGTModRMONHostStatsMode_Type.__name__ = "Integer32"
_Oc61nnDMGTModRMONHostStatsMode_Object = MibTableColumn
oc61nnDMGTModRMONHostStatsMode = _Oc61nnDMGTModRMONHostStatsMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 45, 6, 1, 9),
    _Oc61nnDMGTModRMONHostStatsMode_Type()
)
oc61nnDMGTModRMONHostStatsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnDMGTModRMONHostStatsMode.setStatus("mandatory")
_Oc61nnMFBP_ObjectIdentity = ObjectIdentity
oc61nnMFBP = _Oc61nnMFBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46)
)
_Oc61nnMFBPPortTable_Object = MibTable
oc61nnMFBPPortTable = _Oc61nnMFBPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 2)
)
if mibBuilder.loadTexts:
    oc61nnMFBPPortTable.setStatus("mandatory")
_Oc61nnMFBPPortEntry_Object = MibTableRow
oc61nnMFBPPortEntry = _Oc61nnMFBPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 2, 1)
)
oc61nnMFBPPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "oc61nnMFBPPortSlotIndex"),
    (0, "CHIPCOMMIB", "oc61nnMFBPPortIndex"),
)
if mibBuilder.loadTexts:
    oc61nnMFBPPortEntry.setStatus("mandatory")
_Oc61nnMFBPPortSlotIndex_Type = Integer32
_Oc61nnMFBPPortSlotIndex_Object = MibTableColumn
oc61nnMFBPPortSlotIndex = _Oc61nnMFBPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 2, 1, 1),
    _Oc61nnMFBPPortSlotIndex_Type()
)
oc61nnMFBPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMFBPPortSlotIndex.setStatus("mandatory")
_Oc61nnMFBPPortIndex_Type = Integer32
_Oc61nnMFBPPortIndex_Object = MibTableColumn
oc61nnMFBPPortIndex = _Oc61nnMFBPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 2, 1, 2),
    _Oc61nnMFBPPortIndex_Type()
)
oc61nnMFBPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMFBPPortIndex.setStatus("mandatory")


class _Oc61nnMFBPPortAdminState_Type(Integer32):
    """Custom type oc61nnMFBPPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Oc61nnMFBPPortAdminState_Type.__name__ = "Integer32"
_Oc61nnMFBPPortAdminState_Object = MibTableColumn
oc61nnMFBPPortAdminState = _Oc61nnMFBPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 2, 1, 3),
    _Oc61nnMFBPPortAdminState_Type()
)
oc61nnMFBPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnMFBPPortAdminState.setStatus("mandatory")
_Oc61nnMFBPPortBuddySlot_Type = Integer32
_Oc61nnMFBPPortBuddySlot_Object = MibTableColumn
oc61nnMFBPPortBuddySlot = _Oc61nnMFBPPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 2, 1, 4),
    _Oc61nnMFBPPortBuddySlot_Type()
)
oc61nnMFBPPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnMFBPPortBuddySlot.setStatus("mandatory")
_Oc61nnMFBPPortBuddyPort_Type = Integer32
_Oc61nnMFBPPortBuddyPort_Object = MibTableColumn
oc61nnMFBPPortBuddyPort = _Oc61nnMFBPPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 2, 1, 5),
    _Oc61nnMFBPPortBuddyPort_Type()
)
oc61nnMFBPPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnMFBPPortBuddyPort.setStatus("mandatory")


class _Oc61nnMFBPPortDipNetwork_Type(Integer32):
    """Custom type oc61nnMFBPPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              21,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36),
          ("isolated-1", 21))
    )


_Oc61nnMFBPPortDipNetwork_Type.__name__ = "Integer32"
_Oc61nnMFBPPortDipNetwork_Object = MibTableColumn
oc61nnMFBPPortDipNetwork = _Oc61nnMFBPPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 2, 1, 6),
    _Oc61nnMFBPPortDipNetwork_Type()
)
oc61nnMFBPPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMFBPPortDipNetwork.setStatus("mandatory")


class _Oc61nnMFBPPortHipwr_Type(Integer32):
    """Custom type oc61nnMFBPPortHipwr based on Integer32"""
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


_Oc61nnMFBPPortHipwr_Type.__name__ = "Integer32"
_Oc61nnMFBPPortHipwr_Object = MibTableColumn
oc61nnMFBPPortHipwr = _Oc61nnMFBPPortHipwr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 2, 1, 7),
    _Oc61nnMFBPPortHipwr_Type()
)
oc61nnMFBPPortHipwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnMFBPPortHipwr.setStatus("mandatory")
_Oc61nnMFBPModTable_Object = MibTable
oc61nnMFBPModTable = _Oc61nnMFBPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 6)
)
if mibBuilder.loadTexts:
    oc61nnMFBPModTable.setStatus("mandatory")
_Oc61nnMFBPModEntry_Object = MibTableRow
oc61nnMFBPModEntry = _Oc61nnMFBPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 6, 1)
)
oc61nnMFBPModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "oc61nnMFBPModSlotIndex"),
    (0, "CHIPCOMMIB", "oc61nnMFBPModSubSlotIndex"),
)
if mibBuilder.loadTexts:
    oc61nnMFBPModEntry.setStatus("mandatory")
_Oc61nnMFBPModSlotIndex_Type = Integer32
_Oc61nnMFBPModSlotIndex_Object = MibTableColumn
oc61nnMFBPModSlotIndex = _Oc61nnMFBPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 6, 1, 1),
    _Oc61nnMFBPModSlotIndex_Type()
)
oc61nnMFBPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMFBPModSlotIndex.setStatus("mandatory")
_Oc61nnMFBPModSubSlotIndex_Type = Integer32
_Oc61nnMFBPModSubSlotIndex_Object = MibTableColumn
oc61nnMFBPModSubSlotIndex = _Oc61nnMFBPModSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 6, 1, 2),
    _Oc61nnMFBPModSubSlotIndex_Type()
)
oc61nnMFBPModSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMFBPModSubSlotIndex.setStatus("mandatory")


class _Oc61nnMFBPModBootVersion_Type(DisplayString):
    """Custom type oc61nnMFBPModBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Oc61nnMFBPModBootVersion_Type.__name__ = "DisplayString"
_Oc61nnMFBPModBootVersion_Object = MibTableColumn
oc61nnMFBPModBootVersion = _Oc61nnMFBPModBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 6, 1, 3),
    _Oc61nnMFBPModBootVersion_Type()
)
oc61nnMFBPModBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMFBPModBootVersion.setStatus("mandatory")


class _Oc61nnMFBPModDipNVRam_Type(Integer32):
    """Custom type oc61nnMFBPModDipNVRam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Oc61nnMFBPModDipNVRam_Type.__name__ = "Integer32"
_Oc61nnMFBPModDipNVRam_Object = MibTableColumn
oc61nnMFBPModDipNVRam = _Oc61nnMFBPModDipNVRam_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 46, 6, 1, 4),
    _Oc61nnMFBPModDipNVRam_Type()
)
oc61nnMFBPModDipNVRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMFBPModDipNVRam.setStatus("mandatory")
_Oc61nnMTPL_ObjectIdentity = ObjectIdentity
oc61nnMTPL = _Oc61nnMTPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47)
)
_Oc61nnMTPLPortTable_Object = MibTable
oc61nnMTPLPortTable = _Oc61nnMTPLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 2)
)
if mibBuilder.loadTexts:
    oc61nnMTPLPortTable.setStatus("mandatory")
_Oc61nnMTPLPortEntry_Object = MibTableRow
oc61nnMTPLPortEntry = _Oc61nnMTPLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 2, 1)
)
oc61nnMTPLPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "oc61nnMTPLPortSlotIndex"),
    (0, "CHIPCOMMIB", "oc61nnMTPLPortIndex"),
)
if mibBuilder.loadTexts:
    oc61nnMTPLPortEntry.setStatus("mandatory")
_Oc61nnMTPLPortSlotIndex_Type = Integer32
_Oc61nnMTPLPortSlotIndex_Object = MibTableColumn
oc61nnMTPLPortSlotIndex = _Oc61nnMTPLPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 2, 1, 1),
    _Oc61nnMTPLPortSlotIndex_Type()
)
oc61nnMTPLPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMTPLPortSlotIndex.setStatus("mandatory")
_Oc61nnMTPLPortIndex_Type = Integer32
_Oc61nnMTPLPortIndex_Object = MibTableColumn
oc61nnMTPLPortIndex = _Oc61nnMTPLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 2, 1, 2),
    _Oc61nnMTPLPortIndex_Type()
)
oc61nnMTPLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMTPLPortIndex.setStatus("mandatory")


class _Oc61nnMTPLPortAdminState_Type(Integer32):
    """Custom type oc61nnMTPLPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("remote-diagnostics", 8))
    )


_Oc61nnMTPLPortAdminState_Type.__name__ = "Integer32"
_Oc61nnMTPLPortAdminState_Object = MibTableColumn
oc61nnMTPLPortAdminState = _Oc61nnMTPLPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 2, 1, 3),
    _Oc61nnMTPLPortAdminState_Type()
)
oc61nnMTPLPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnMTPLPortAdminState.setStatus("mandatory")
_Oc61nnMTPLPortBuddySlot_Type = Integer32
_Oc61nnMTPLPortBuddySlot_Object = MibTableColumn
oc61nnMTPLPortBuddySlot = _Oc61nnMTPLPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 2, 1, 4),
    _Oc61nnMTPLPortBuddySlot_Type()
)
oc61nnMTPLPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnMTPLPortBuddySlot.setStatus("mandatory")
_Oc61nnMTPLPortBuddyPort_Type = Integer32
_Oc61nnMTPLPortBuddyPort_Object = MibTableColumn
oc61nnMTPLPortBuddyPort = _Oc61nnMTPLPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 2, 1, 5),
    _Oc61nnMTPLPortBuddyPort_Type()
)
oc61nnMTPLPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnMTPLPortBuddyPort.setStatus("mandatory")


class _Oc61nnMTPLPortDipNetwork_Type(Integer32):
    """Custom type oc61nnMTPLPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              21,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36),
          ("isolated-1", 21))
    )


_Oc61nnMTPLPortDipNetwork_Type.__name__ = "Integer32"
_Oc61nnMTPLPortDipNetwork_Object = MibTableColumn
oc61nnMTPLPortDipNetwork = _Oc61nnMTPLPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 2, 1, 6),
    _Oc61nnMTPLPortDipNetwork_Type()
)
oc61nnMTPLPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMTPLPortDipNetwork.setStatus("mandatory")


class _Oc61nnMTPLPortLinkInteg_Type(Integer32):
    """Custom type oc61nnMTPLPortLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Oc61nnMTPLPortLinkInteg_Type.__name__ = "Integer32"
_Oc61nnMTPLPortLinkInteg_Object = MibTableColumn
oc61nnMTPLPortLinkInteg = _Oc61nnMTPLPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 2, 1, 7),
    _Oc61nnMTPLPortLinkInteg_Type()
)
oc61nnMTPLPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnMTPLPortLinkInteg.setStatus("mandatory")


class _Oc61nnMTPLPortAutoPolarity_Type(Integer32):
    """Custom type oc61nnMTPLPortAutoPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Oc61nnMTPLPortAutoPolarity_Type.__name__ = "Integer32"
_Oc61nnMTPLPortAutoPolarity_Object = MibTableColumn
oc61nnMTPLPortAutoPolarity = _Oc61nnMTPLPortAutoPolarity_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 2, 1, 8),
    _Oc61nnMTPLPortAutoPolarity_Type()
)
oc61nnMTPLPortAutoPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc61nnMTPLPortAutoPolarity.setStatus("mandatory")
_Oc61nnMTPLModTable_Object = MibTable
oc61nnMTPLModTable = _Oc61nnMTPLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 6)
)
if mibBuilder.loadTexts:
    oc61nnMTPLModTable.setStatus("mandatory")
_Oc61nnMTPLModEntry_Object = MibTableRow
oc61nnMTPLModEntry = _Oc61nnMTPLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 6, 1)
)
oc61nnMTPLModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "oc61nnMTPLModSlotIndex"),
    (0, "CHIPCOMMIB", "oc61nnMTPLModSubSlotIndex"),
)
if mibBuilder.loadTexts:
    oc61nnMTPLModEntry.setStatus("mandatory")
_Oc61nnMTPLModSlotIndex_Type = Integer32
_Oc61nnMTPLModSlotIndex_Object = MibTableColumn
oc61nnMTPLModSlotIndex = _Oc61nnMTPLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 6, 1, 1),
    _Oc61nnMTPLModSlotIndex_Type()
)
oc61nnMTPLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMTPLModSlotIndex.setStatus("mandatory")
_Oc61nnMTPLModSubSlotIndex_Type = Integer32
_Oc61nnMTPLModSubSlotIndex_Object = MibTableColumn
oc61nnMTPLModSubSlotIndex = _Oc61nnMTPLModSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 6, 1, 2),
    _Oc61nnMTPLModSubSlotIndex_Type()
)
oc61nnMTPLModSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMTPLModSubSlotIndex.setStatus("mandatory")


class _Oc61nnMTPLModBootVersion_Type(DisplayString):
    """Custom type oc61nnMTPLModBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Oc61nnMTPLModBootVersion_Type.__name__ = "DisplayString"
_Oc61nnMTPLModBootVersion_Object = MibTableColumn
oc61nnMTPLModBootVersion = _Oc61nnMTPLModBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 6, 1, 3),
    _Oc61nnMTPLModBootVersion_Type()
)
oc61nnMTPLModBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMTPLModBootVersion.setStatus("mandatory")


class _Oc61nnMTPLModDipNVRam_Type(Integer32):
    """Custom type oc61nnMTPLModDipNVRam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Oc61nnMTPLModDipNVRam_Type.__name__ = "Integer32"
_Oc61nnMTPLModDipNVRam_Object = MibTableColumn
oc61nnMTPLModDipNVRam = _Oc61nnMTPLModDipNVRam_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 47, 6, 1, 4),
    _Oc61nnMTPLModDipNVRam_Type()
)
oc61nnMTPLModDipNVRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc61nnMTPLModDipNVRam.setStatus("mandatory")
_Ol51nnMTPLS_ObjectIdentity = ObjectIdentity
ol51nnMTPLS = _Ol51nnMTPLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48)
)
_Ol51nnMTPLSModTable_Object = MibTable
ol51nnMTPLSModTable = _Ol51nnMTPLSModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTPLSModTable.setStatus("mandatory")
_Ol51nnMTPLSModEntry_Object = MibTableRow
ol51nnMTPLSModEntry = _Ol51nnMTPLSModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 1, 1)
)
ol51nnMTPLSModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTPLSModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPLSModEntry.setStatus("mandatory")
_Ol51nnMTPLSModSlotIndex_Type = Integer32
_Ol51nnMTPLSModSlotIndex_Object = MibTableColumn
ol51nnMTPLSModSlotIndex = _Ol51nnMTPLSModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 1, 1, 1),
    _Ol51nnMTPLSModSlotIndex_Type()
)
ol51nnMTPLSModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLSModSlotIndex.setStatus("mandatory")


class _Ol51nnMTPLSModDipNetwork_Type(Integer32):
    """Custom type ol51nnMTPLSModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMTPLSModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPLSModDipNetwork_Object = MibTableColumn
ol51nnMTPLSModDipNetwork = _Ol51nnMTPLSModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 1, 1, 2),
    _Ol51nnMTPLSModDipNetwork_Type()
)
ol51nnMTPLSModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLSModDipNetwork.setStatus("mandatory")


class _Ol51nnMTPLSModAutoPartition_Type(Integer32):
    """Custom type ol51nnMTPLSModAutoPartition based on Integer32"""
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
        *(("collisions-127", 3),
          ("collisions-255", 4),
          ("collisions-31", 1),
          ("collisions-63", 2))
    )


_Ol51nnMTPLSModAutoPartition_Type.__name__ = "Integer32"
_Ol51nnMTPLSModAutoPartition_Object = MibTableColumn
ol51nnMTPLSModAutoPartition = _Ol51nnMTPLSModAutoPartition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 1, 1, 3),
    _Ol51nnMTPLSModAutoPartition_Type()
)
ol51nnMTPLSModAutoPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLSModAutoPartition.setStatus("mandatory")
_Ol51nnMTPLSPortTable_Object = MibTable
ol51nnMTPLSPortTable = _Ol51nnMTPLSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTPLSPortTable.setStatus("mandatory")
_Ol51nnMTPLSPortEntry_Object = MibTableRow
ol51nnMTPLSPortEntry = _Ol51nnMTPLSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2, 1)
)
ol51nnMTPLSPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol51nnMTPLSPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol51nnMTPLSPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPLSPortEntry.setStatus("mandatory")
_Ol51nnMTPLSPortSlotIndex_Type = Integer32
_Ol51nnMTPLSPortSlotIndex_Object = MibTableColumn
ol51nnMTPLSPortSlotIndex = _Ol51nnMTPLSPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2, 1, 1),
    _Ol51nnMTPLSPortSlotIndex_Type()
)
ol51nnMTPLSPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLSPortSlotIndex.setStatus("mandatory")
_Ol51nnMTPLSPortIndex_Type = Integer32
_Ol51nnMTPLSPortIndex_Object = MibTableColumn
ol51nnMTPLSPortIndex = _Ol51nnMTPLSPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2, 1, 2),
    _Ol51nnMTPLSPortIndex_Type()
)
ol51nnMTPLSPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLSPortIndex.setStatus("mandatory")


class _Ol51nnMTPLSPortAdminState_Type(Integer32):
    """Custom type ol51nnMTPLSPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("remote-diagnostics", 8))
    )


_Ol51nnMTPLSPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPLSPortAdminState_Object = MibTableColumn
ol51nnMTPLSPortAdminState = _Ol51nnMTPLSPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2, 1, 3),
    _Ol51nnMTPLSPortAdminState_Type()
)
ol51nnMTPLSPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLSPortAdminState.setStatus("mandatory")


class _Ol51nnMTPLSPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMTPLSPortDipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPLSPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPLSPortDipAdminState_Object = MibTableColumn
ol51nnMTPLSPortDipAdminState = _Ol51nnMTPLSPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2, 1, 4),
    _Ol51nnMTPLSPortDipAdminState_Type()
)
ol51nnMTPLSPortDipAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLSPortDipAdminState.setStatus("mandatory")


class _Ol51nnMTPLSPortDipSecurity_Type(Integer32):
    """Custom type ol51nnMTPLSPortDipSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPLSPortDipSecurity_Type.__name__ = "Integer32"
_Ol51nnMTPLSPortDipSecurity_Object = MibTableColumn
ol51nnMTPLSPortDipSecurity = _Ol51nnMTPLSPortDipSecurity_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2, 1, 5),
    _Ol51nnMTPLSPortDipSecurity_Type()
)
ol51nnMTPLSPortDipSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLSPortDipSecurity.setStatus("mandatory")
_Ol51nnMTPLSPortBuddySlot_Type = Integer32
_Ol51nnMTPLSPortBuddySlot_Object = MibTableColumn
ol51nnMTPLSPortBuddySlot = _Ol51nnMTPLSPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2, 1, 6),
    _Ol51nnMTPLSPortBuddySlot_Type()
)
ol51nnMTPLSPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLSPortBuddySlot.setStatus("mandatory")
_Ol51nnMTPLSPortBuddyPort_Type = Integer32
_Ol51nnMTPLSPortBuddyPort_Object = MibTableColumn
ol51nnMTPLSPortBuddyPort = _Ol51nnMTPLSPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2, 1, 7),
    _Ol51nnMTPLSPortBuddyPort_Type()
)
ol51nnMTPLSPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLSPortBuddyPort.setStatus("mandatory")


class _Ol51nnMTPLSPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPLSPortLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPLSPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPLSPortLinkInteg_Object = MibTableColumn
ol51nnMTPLSPortLinkInteg = _Ol51nnMTPLSPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2, 1, 8),
    _Ol51nnMTPLSPortLinkInteg_Type()
)
ol51nnMTPLSPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLSPortLinkInteg.setStatus("mandatory")


class _Ol51nnMTPLSPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPLSPortDipLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol51nnMTPLSPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPLSPortDipLinkInteg_Object = MibTableColumn
ol51nnMTPLSPortDipLinkInteg = _Ol51nnMTPLSPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 48, 2, 1, 9),
    _Ol51nnMTPLSPortDipLinkInteg_Type()
)
ol51nnMTPLSPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLSPortDipLinkInteg.setStatus("mandatory")
_Oc60nnMRCTL_ObjectIdentity = ObjectIdentity
oc60nnMRCTL = _Oc60nnMRCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50)
)
_Ol60nnMRCTLModTable_Object = MibTable
ol60nnMRCTLModTable = _Ol60nnMRCTLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 1)
)
if mibBuilder.loadTexts:
    ol60nnMRCTLModTable.setStatus("mandatory")
_Ol60nnMRCTLModEntry_Object = MibTableRow
ol60nnMRCTLModEntry = _Ol60nnMRCTLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 1, 1)
)
ol60nnMRCTLModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol60nnMRCTLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol60nnMRCTLModEntry.setStatus("mandatory")
_Ol60nnMRCTLModSlotIndex_Type = Integer32
_Ol60nnMRCTLModSlotIndex_Object = MibTableColumn
ol60nnMRCTLModSlotIndex = _Ol60nnMRCTLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 1, 1, 1),
    _Ol60nnMRCTLModSlotIndex_Type()
)
ol60nnMRCTLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol60nnMRCTLModSlotIndex.setStatus("mandatory")


class _Ol60nnMRCTLModOperState_Type(Integer32):
    """Custom type ol60nnMRCTLModOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_Ol60nnMRCTLModOperState_Type.__name__ = "Integer32"
_Ol60nnMRCTLModOperState_Object = MibTableColumn
ol60nnMRCTLModOperState = _Ol60nnMRCTLModOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 1, 1, 2),
    _Ol60nnMRCTLModOperState_Type()
)
ol60nnMRCTLModOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol60nnMRCTLModOperState.setStatus("mandatory")


class _Ol60nnMRCTLModClockStatus_Type(Integer32):
    """Custom type ol60nnMRCTLModClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1))
    )


_Ol60nnMRCTLModClockStatus_Type.__name__ = "Integer32"
_Ol60nnMRCTLModClockStatus_Object = MibTableColumn
ol60nnMRCTLModClockStatus = _Ol60nnMRCTLModClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 1, 1, 3),
    _Ol60nnMRCTLModClockStatus_Type()
)
ol60nnMRCTLModClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol60nnMRCTLModClockStatus.setStatus("mandatory")


class _Ol60nnMRCTLModTempStatus_Type(Integer32):
    """Custom type ol60nnMRCTLModTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1))
    )


_Ol60nnMRCTLModTempStatus_Type.__name__ = "Integer32"
_Ol60nnMRCTLModTempStatus_Object = MibTableColumn
ol60nnMRCTLModTempStatus = _Ol60nnMRCTLModTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 1, 1, 4),
    _Ol60nnMRCTLModTempStatus_Type()
)
ol60nnMRCTLModTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol60nnMRCTLModTempStatus.setStatus("mandatory")
_Oc60nnMRCTLModTable_Object = MibTable
oc60nnMRCTLModTable = _Oc60nnMRCTLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6)
)
if mibBuilder.loadTexts:
    oc60nnMRCTLModTable.setStatus("mandatory")
_Oc60nnMRCTLModEntry_Object = MibTableRow
oc60nnMRCTLModEntry = _Oc60nnMRCTLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1)
)
oc60nnMRCTLModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "oc60nnMRCTLModSlotIndex"),
    (0, "CHIPCOMMIB", "oc60nnMRCTLModSubSlotIndex"),
)
if mibBuilder.loadTexts:
    oc60nnMRCTLModEntry.setStatus("mandatory")
_Oc60nnMRCTLModSlotIndex_Type = Integer32
_Oc60nnMRCTLModSlotIndex_Object = MibTableColumn
oc60nnMRCTLModSlotIndex = _Oc60nnMRCTLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 1),
    _Oc60nnMRCTLModSlotIndex_Type()
)
oc60nnMRCTLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModSlotIndex.setStatus("mandatory")
_Oc60nnMRCTLModSubSlotIndex_Type = Integer32
_Oc60nnMRCTLModSubSlotIndex_Object = MibTableColumn
oc60nnMRCTLModSubSlotIndex = _Oc60nnMRCTLModSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 2),
    _Oc60nnMRCTLModSubSlotIndex_Type()
)
oc60nnMRCTLModSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModSubSlotIndex.setStatus("mandatory")


class _Oc60nnMRCTLModBootVersion_Type(DisplayString):
    """Custom type oc60nnMRCTLModBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Oc60nnMRCTLModBootVersion_Type.__name__ = "DisplayString"
_Oc60nnMRCTLModBootVersion_Object = MibTableColumn
oc60nnMRCTLModBootVersion = _Oc60nnMRCTLModBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 3),
    _Oc60nnMRCTLModBootVersion_Type()
)
oc60nnMRCTLModBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModBootVersion.setStatus("mandatory")


class _Oc60nnMRCTLModOperState_Type(Integer32):
    """Custom type oc60nnMRCTLModOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_Oc60nnMRCTLModOperState_Type.__name__ = "Integer32"
_Oc60nnMRCTLModOperState_Object = MibTableColumn
oc60nnMRCTLModOperState = _Oc60nnMRCTLModOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 4),
    _Oc60nnMRCTLModOperState_Type()
)
oc60nnMRCTLModOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModOperState.setStatus("mandatory")


class _Oc60nnMRCTLModClockStatus_Type(Integer32):
    """Custom type oc60nnMRCTLModClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1))
    )


_Oc60nnMRCTLModClockStatus_Type.__name__ = "Integer32"
_Oc60nnMRCTLModClockStatus_Object = MibTableColumn
oc60nnMRCTLModClockStatus = _Oc60nnMRCTLModClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 5),
    _Oc60nnMRCTLModClockStatus_Type()
)
oc60nnMRCTLModClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModClockStatus.setStatus("mandatory")


class _Oc60nnMRCTLModTempStatus_Type(Integer32):
    """Custom type oc60nnMRCTLModTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1))
    )


_Oc60nnMRCTLModTempStatus_Type.__name__ = "Integer32"
_Oc60nnMRCTLModTempStatus_Object = MibTableColumn
oc60nnMRCTLModTempStatus = _Oc60nnMRCTLModTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 6),
    _Oc60nnMRCTLModTempStatus_Type()
)
oc60nnMRCTLModTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModTempStatus.setStatus("mandatory")


class _Oc60nnMRCTLModAtoDConverterStatus_Type(Integer32):
    """Custom type oc60nnMRCTLModAtoDConverterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1))
    )


_Oc60nnMRCTLModAtoDConverterStatus_Type.__name__ = "Integer32"
_Oc60nnMRCTLModAtoDConverterStatus_Object = MibTableColumn
oc60nnMRCTLModAtoDConverterStatus = _Oc60nnMRCTLModAtoDConverterStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 7),
    _Oc60nnMRCTLModAtoDConverterStatus_Type()
)
oc60nnMRCTLModAtoDConverterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModAtoDConverterStatus.setStatus("mandatory")


class _Oc60nnMRCTLModPS1Status_Type(Integer32):
    """Custom type oc60nnMRCTLModPS1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("faulty", 3),
          ("not-installed", 4))
    )


_Oc60nnMRCTLModPS1Status_Type.__name__ = "Integer32"
_Oc60nnMRCTLModPS1Status_Object = MibTableColumn
oc60nnMRCTLModPS1Status = _Oc60nnMRCTLModPS1Status_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 8),
    _Oc60nnMRCTLModPS1Status_Type()
)
oc60nnMRCTLModPS1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModPS1Status.setStatus("mandatory")


class _Oc60nnMRCTLModPS2Status_Type(Integer32):
    """Custom type oc60nnMRCTLModPS2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("faulty", 3),
          ("not-installed", 4))
    )


_Oc60nnMRCTLModPS2Status_Type.__name__ = "Integer32"
_Oc60nnMRCTLModPS2Status_Object = MibTableColumn
oc60nnMRCTLModPS2Status = _Oc60nnMRCTLModPS2Status_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 9),
    _Oc60nnMRCTLModPS2Status_Type()
)
oc60nnMRCTLModPS2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModPS2Status.setStatus("mandatory")


class _Oc60nnMRCTLModPS3Status_Type(Integer32):
    """Custom type oc60nnMRCTLModPS3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("faulty", 3),
          ("not-installed", 4))
    )


_Oc60nnMRCTLModPS3Status_Type.__name__ = "Integer32"
_Oc60nnMRCTLModPS3Status_Object = MibTableColumn
oc60nnMRCTLModPS3Status = _Oc60nnMRCTLModPS3Status_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 10),
    _Oc60nnMRCTLModPS3Status_Type()
)
oc60nnMRCTLModPS3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModPS3Status.setStatus("mandatory")


class _Oc60nnMRCTLModPS4Status_Type(Integer32):
    """Custom type oc60nnMRCTLModPS4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("faulty", 3),
          ("not-installed", 4))
    )


_Oc60nnMRCTLModPS4Status_Type.__name__ = "Integer32"
_Oc60nnMRCTLModPS4Status_Object = MibTableColumn
oc60nnMRCTLModPS4Status = _Oc60nnMRCTLModPS4Status_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 50, 6, 1, 11),
    _Oc60nnMRCTLModPS4Status_Type()
)
oc60nnMRCTLModPS4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc60nnMRCTLModPS4Status.setStatus("mandatory")
_Ol50nnMRCLS_ObjectIdentity = ObjectIdentity
ol50nnMRCLS = _Ol50nnMRCLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 51)
)
_Ol50nnMRCLSModTable_Object = MibTable
ol50nnMRCLSModTable = _Ol50nnMRCLSModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 51, 1)
)
if mibBuilder.loadTexts:
    ol50nnMRCLSModTable.setStatus("mandatory")
_Ol50nnMRCLSModEntry_Object = MibTableRow
ol50nnMRCLSModEntry = _Ol50nnMRCLSModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 51, 1, 1)
)
ol50nnMRCLSModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol50nnMRCLSModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol50nnMRCLSModEntry.setStatus("mandatory")
_Ol50nnMRCLSModSlotIndex_Type = Integer32
_Ol50nnMRCLSModSlotIndex_Object = MibTableColumn
ol50nnMRCLSModSlotIndex = _Ol50nnMRCLSModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 51, 1, 1, 1),
    _Ol50nnMRCLSModSlotIndex_Type()
)
ol50nnMRCLSModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCLSModSlotIndex.setStatus("mandatory")


class _Ol50nnMRCLSModOperState_Type(Integer32):
    """Custom type ol50nnMRCLSModOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_Ol50nnMRCLSModOperState_Type.__name__ = "Integer32"
_Ol50nnMRCLSModOperState_Object = MibTableColumn
ol50nnMRCLSModOperState = _Ol50nnMRCLSModOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 51, 1, 1, 2),
    _Ol50nnMRCLSModOperState_Type()
)
ol50nnMRCLSModOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCLSModOperState.setStatus("mandatory")


class _Ol50nnMRCLSModClockStatus_Type(Integer32):
    """Custom type ol50nnMRCLSModClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1))
    )


_Ol50nnMRCLSModClockStatus_Type.__name__ = "Integer32"
_Ol50nnMRCLSModClockStatus_Object = MibTableColumn
ol50nnMRCLSModClockStatus = _Ol50nnMRCLSModClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 51, 1, 1, 3),
    _Ol50nnMRCLSModClockStatus_Type()
)
ol50nnMRCLSModClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCLSModClockStatus.setStatus("mandatory")


class _Ol50nnMRCLSModTempStatus_Type(Integer32):
    """Custom type ol50nnMRCLSModTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1))
    )


_Ol50nnMRCLSModTempStatus_Type.__name__ = "Integer32"
_Ol50nnMRCLSModTempStatus_Object = MibTableColumn
ol50nnMRCLSModTempStatus = _Ol50nnMRCLSModTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 51, 1, 1, 4),
    _Ol50nnMRCLSModTempStatus_Type()
)
ol50nnMRCLSModTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCLSModTempStatus.setStatus("mandatory")
_Ol41nnHMTP_ObjectIdentity = ObjectIdentity
ol41nnHMTP = _Ol41nnHMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52)
)
_Ol41nnHMTPModTable_Object = MibTable
ol41nnHMTPModTable = _Ol41nnHMTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 1)
)
if mibBuilder.loadTexts:
    ol41nnHMTPModTable.setStatus("mandatory")
_Ol41nnHMTPModEntry_Object = MibTableRow
ol41nnHMTPModEntry = _Ol41nnHMTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 1, 1)
)
ol41nnHMTPModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol41nnHMTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol41nnHMTPModEntry.setStatus("mandatory")
_Ol41nnHMTPModSlotIndex_Type = Integer32
_Ol41nnHMTPModSlotIndex_Object = MibTableColumn
ol41nnHMTPModSlotIndex = _Ol41nnHMTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 1, 1, 1),
    _Ol41nnHMTPModSlotIndex_Type()
)
ol41nnHMTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol41nnHMTPModSlotIndex.setStatus("mandatory")
_Ol41nnHMTPModSerialNo_Type = DisplayString
_Ol41nnHMTPModSerialNo_Object = MibTableColumn
ol41nnHMTPModSerialNo = _Ol41nnHMTPModSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 1, 1, 2),
    _Ol41nnHMTPModSerialNo_Type()
)
ol41nnHMTPModSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol41nnHMTPModSerialNo.setStatus("mandatory")
_Ol41nnHMTPModProtocols_Type = DisplayString
_Ol41nnHMTPModProtocols_Object = MibTableColumn
ol41nnHMTPModProtocols = _Ol41nnHMTPModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 1, 1, 3),
    _Ol41nnHMTPModProtocols_Type()
)
ol41nnHMTPModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol41nnHMTPModProtocols.setStatus("mandatory")
_Ol41nnHMTPModIpAddress_Type = IpAddress
_Ol41nnHMTPModIpAddress_Object = MibTableColumn
ol41nnHMTPModIpAddress = _Ol41nnHMTPModIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 1, 1, 4),
    _Ol41nnHMTPModIpAddress_Type()
)
ol41nnHMTPModIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol41nnHMTPModIpAddress.setStatus("mandatory")
_Ol41nnHMTPPortTable_Object = MibTable
ol41nnHMTPPortTable = _Ol41nnHMTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 2)
)
if mibBuilder.loadTexts:
    ol41nnHMTPPortTable.setStatus("mandatory")
_Ol41nnHMTPPortEntry_Object = MibTableRow
ol41nnHMTPPortEntry = _Ol41nnHMTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 2, 1)
)
ol41nnHMTPPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol41nnHMTPPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol41nnHMTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol41nnHMTPPortEntry.setStatus("mandatory")
_Ol41nnHMTPPortSlotIndex_Type = Integer32
_Ol41nnHMTPPortSlotIndex_Object = MibTableColumn
ol41nnHMTPPortSlotIndex = _Ol41nnHMTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 2, 1, 1),
    _Ol41nnHMTPPortSlotIndex_Type()
)
ol41nnHMTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol41nnHMTPPortSlotIndex.setStatus("mandatory")
_Ol41nnHMTPPortIndex_Type = Integer32
_Ol41nnHMTPPortIndex_Object = MibTableColumn
ol41nnHMTPPortIndex = _Ol41nnHMTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 2, 1, 2),
    _Ol41nnHMTPPortIndex_Type()
)
ol41nnHMTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol41nnHMTPPortIndex.setStatus("mandatory")


class _Ol41nnHMTPPortReset_Type(Integer32):
    """Custom type ol41nnHMTPPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_Ol41nnHMTPPortReset_Type.__name__ = "Integer32"
_Ol41nnHMTPPortReset_Object = MibTableColumn
ol41nnHMTPPortReset = _Ol41nnHMTPPortReset_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 2, 1, 3),
    _Ol41nnHMTPPortReset_Type()
)
ol41nnHMTPPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol41nnHMTPPortReset.setStatus("mandatory")


class _Ol41nnHMTPPortLinkInteg_Type(Integer32):
    """Custom type ol41nnHMTPPortLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol41nnHMTPPortLinkInteg_Type.__name__ = "Integer32"
_Ol41nnHMTPPortLinkInteg_Object = MibTableColumn
ol41nnHMTPPortLinkInteg = _Ol41nnHMTPPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 52, 2, 1, 4),
    _Ol41nnHMTPPortLinkInteg_Type()
)
ol41nnHMTPPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol41nnHMTPPortLinkInteg.setStatus("mandatory")
_Ol41nnHETP_ObjectIdentity = ObjectIdentity
ol41nnHETP = _Ol41nnHETP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53)
)
_Ol41nnHETPModTable_Object = MibTable
ol41nnHETPModTable = _Ol41nnHETPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53, 1)
)
if mibBuilder.loadTexts:
    ol41nnHETPModTable.setStatus("mandatory")
_Ol41nnHETPModEntry_Object = MibTableRow
ol41nnHETPModEntry = _Ol41nnHETPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53, 1, 1)
)
ol41nnHETPModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol41nnHETPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol41nnHETPModEntry.setStatus("mandatory")
_Ol41nnHETPModSlotIndex_Type = Integer32
_Ol41nnHETPModSlotIndex_Object = MibTableColumn
ol41nnHETPModSlotIndex = _Ol41nnHETPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53, 1, 1, 1),
    _Ol41nnHETPModSlotIndex_Type()
)
ol41nnHETPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol41nnHETPModSlotIndex.setStatus("mandatory")
_Ol41nnHETPModSerialNo_Type = DisplayString
_Ol41nnHETPModSerialNo_Object = MibTableColumn
ol41nnHETPModSerialNo = _Ol41nnHETPModSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53, 1, 1, 2),
    _Ol41nnHETPModSerialNo_Type()
)
ol41nnHETPModSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol41nnHETPModSerialNo.setStatus("mandatory")
_Ol41nnHETPPortTable_Object = MibTable
ol41nnHETPPortTable = _Ol41nnHETPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53, 2)
)
if mibBuilder.loadTexts:
    ol41nnHETPPortTable.setStatus("mandatory")
_Ol41nnHETPPortEntry_Object = MibTableRow
ol41nnHETPPortEntry = _Ol41nnHETPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53, 2, 1)
)
ol41nnHETPPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol41nnHETPPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol41nnHETPPortIndex"),
)
if mibBuilder.loadTexts:
    ol41nnHETPPortEntry.setStatus("mandatory")
_Ol41nnHETPPortSlotIndex_Type = Integer32
_Ol41nnHETPPortSlotIndex_Object = MibTableColumn
ol41nnHETPPortSlotIndex = _Ol41nnHETPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53, 2, 1, 1),
    _Ol41nnHETPPortSlotIndex_Type()
)
ol41nnHETPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol41nnHETPPortSlotIndex.setStatus("mandatory")
_Ol41nnHETPPortIndex_Type = Integer32
_Ol41nnHETPPortIndex_Object = MibTableColumn
ol41nnHETPPortIndex = _Ol41nnHETPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53, 2, 1, 2),
    _Ol41nnHETPPortIndex_Type()
)
ol41nnHETPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol41nnHETPPortIndex.setStatus("mandatory")


class _Ol41nnHETPPortReset_Type(Integer32):
    """Custom type ol41nnHETPPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("reset", 2))
    )


_Ol41nnHETPPortReset_Type.__name__ = "Integer32"
_Ol41nnHETPPortReset_Object = MibTableColumn
ol41nnHETPPortReset = _Ol41nnHETPPortReset_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53, 2, 1, 3),
    _Ol41nnHETPPortReset_Type()
)
ol41nnHETPPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol41nnHETPPortReset.setStatus("mandatory")


class _Ol41nnHETPPortLinkInteg_Type(Integer32):
    """Custom type ol41nnHETPPortLinkInteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ol41nnHETPPortLinkInteg_Type.__name__ = "Integer32"
_Ol41nnHETPPortLinkInteg_Object = MibTableColumn
ol41nnHETPPortLinkInteg = _Ol41nnHETPPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 53, 2, 1, 4),
    _Ol41nnHETPPortLinkInteg_Type()
)
ol41nnHETPPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol41nnHETPPortLinkInteg.setStatus("mandatory")
_Ol52nnMEC_ObjectIdentity = ObjectIdentity
ol52nnMEC = _Ol52nnMEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62)
)
_Ol52nnMECModTable_Object = MibTable
ol52nnMECModTable = _Ol52nnMECModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 1)
)
if mibBuilder.loadTexts:
    ol52nnMECModTable.setStatus("mandatory")
_Ol52nnMECModEntry_Object = MibTableRow
ol52nnMECModEntry = _Ol52nnMECModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 1, 1)
)
ol52nnMECModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMECModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMECModEntry.setStatus("mandatory")
_Ol52nnMECModSlotIndex_Type = Integer32
_Ol52nnMECModSlotIndex_Object = MibTableColumn
ol52nnMECModSlotIndex = _Ol52nnMECModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 1, 1, 1),
    _Ol52nnMECModSlotIndex_Type()
)
ol52nnMECModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMECModSlotIndex.setStatus("mandatory")


class _Ol52nnMECModSoftwareVersion_Type(DisplayString):
    """Custom type ol52nnMECModSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Ol52nnMECModSoftwareVersion_Type.__name__ = "DisplayString"
_Ol52nnMECModSoftwareVersion_Object = MibTableColumn
ol52nnMECModSoftwareVersion = _Ol52nnMECModSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 1, 1, 2),
    _Ol52nnMECModSoftwareVersion_Type()
)
ol52nnMECModSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMECModSoftwareVersion.setStatus("mandatory")


class _Ol52nnMECModSystemStatusCode_Type(DisplayString):
    """Custom type ol52nnMECModSystemStatusCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(43, 43),
    )


_Ol52nnMECModSystemStatusCode_Type.__name__ = "DisplayString"
_Ol52nnMECModSystemStatusCode_Object = MibTableColumn
ol52nnMECModSystemStatusCode = _Ol52nnMECModSystemStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 1, 1, 3),
    _Ol52nnMECModSystemStatusCode_Type()
)
ol52nnMECModSystemStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMECModSystemStatusCode.setStatus("mandatory")


class _Ol52nnMECModRingSpeed_Type(Integer32):
    """Custom type ol52nnMECModRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMECModRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMECModRingSpeed_Object = MibTableColumn
ol52nnMECModRingSpeed = _Ol52nnMECModRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 1, 1, 4),
    _Ol52nnMECModRingSpeed_Type()
)
ol52nnMECModRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMECModRingSpeed.setStatus("mandatory")


class _Ol52nnMECModNetworkStatus_Type(Integer32):
    """Custom type ol52nnMECModNetworkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("beaconing", 3),
          ("closed", 2),
          ("okay", 1))
    )


_Ol52nnMECModNetworkStatus_Type.__name__ = "Integer32"
_Ol52nnMECModNetworkStatus_Object = MibTableColumn
ol52nnMECModNetworkStatus = _Ol52nnMECModNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 1, 1, 5),
    _Ol52nnMECModNetworkStatus_Type()
)
ol52nnMECModNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMECModNetworkStatus.setStatus("mandatory")
_Ol52nnMECModIpAddress_Type = IpAddress
_Ol52nnMECModIpAddress_Object = MibTableColumn
ol52nnMECModIpAddress = _Ol52nnMECModIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 1, 1, 6),
    _Ol52nnMECModIpAddress_Type()
)
ol52nnMECModIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMECModIpAddress.setStatus("mandatory")
_Ol52nnMECModMACStationAddr_Type = OctetString
_Ol52nnMECModMACStationAddr_Object = MibTableColumn
ol52nnMECModMACStationAddr = _Ol52nnMECModMACStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 1, 1, 7),
    _Ol52nnMECModMACStationAddr_Type()
)
ol52nnMECModMACStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMECModMACStationAddr.setStatus("mandatory")
_Ol52nnMECPortTable_Object = MibTable
ol52nnMECPortTable = _Ol52nnMECPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 2)
)
if mibBuilder.loadTexts:
    ol52nnMECPortTable.setStatus("mandatory")
_Ol52nnMECPortEntry_Object = MibTableRow
ol52nnMECPortEntry = _Ol52nnMECPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 2, 1)
)
ol52nnMECPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMECPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol52nnMECPortIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMECPortEntry.setStatus("mandatory")
_Ol52nnMECPortSlotIndex_Type = Integer32
_Ol52nnMECPortSlotIndex_Object = MibTableColumn
ol52nnMECPortSlotIndex = _Ol52nnMECPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 2, 1, 1),
    _Ol52nnMECPortSlotIndex_Type()
)
ol52nnMECPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMECPortSlotIndex.setStatus("mandatory")
_Ol52nnMECPortIndex_Type = Integer32
_Ol52nnMECPortIndex_Object = MibTableColumn
ol52nnMECPortIndex = _Ol52nnMECPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 2, 1, 2),
    _Ol52nnMECPortIndex_Type()
)
ol52nnMECPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMECPortIndex.setStatus("mandatory")
_Ol52nnMECTrunkTable_Object = MibTable
ol52nnMECTrunkTable = _Ol52nnMECTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 3)
)
if mibBuilder.loadTexts:
    ol52nnMECTrunkTable.setStatus("mandatory")
_Ol52nnMECTrunkEntry_Object = MibTableRow
ol52nnMECTrunkEntry = _Ol52nnMECTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 3, 1)
)
ol52nnMECTrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol52nnMECTrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol52nnMECTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMECTrunkEntry.setStatus("mandatory")
_Ol52nnMECTrunkSlotIndex_Type = Integer32
_Ol52nnMECTrunkSlotIndex_Object = MibTableColumn
ol52nnMECTrunkSlotIndex = _Ol52nnMECTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 3, 1, 1),
    _Ol52nnMECTrunkSlotIndex_Type()
)
ol52nnMECTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMECTrunkSlotIndex.setStatus("mandatory")
_Ol52nnMECTrunkIndex_Type = Integer32
_Ol52nnMECTrunkIndex_Object = MibTableColumn
ol52nnMECTrunkIndex = _Ol52nnMECTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 62, 3, 1, 2),
    _Ol52nnMECTrunkIndex_Type()
)
ol52nnMECTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMECTrunkIndex.setStatus("mandatory")
_Ol53nnMTDDI_ObjectIdentity = ObjectIdentity
ol53nnMTDDI = _Ol53nnMTDDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65)
)
_Ol53nnMTDDIModTable_Object = MibTable
ol53nnMTDDIModTable = _Ol53nnMTDDIModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 1)
)
if mibBuilder.loadTexts:
    ol53nnMTDDIModTable.setStatus("mandatory")
_Ol53nnMTDDIModEntry_Object = MibTableRow
ol53nnMTDDIModEntry = _Ol53nnMTDDIModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 1, 1)
)
ol53nnMTDDIModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMTDDIModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMTDDIModEntry.setStatus("mandatory")
_Ol53nnMTDDIModSlotIndex_Type = Integer32
_Ol53nnMTDDIModSlotIndex_Object = MibTableColumn
ol53nnMTDDIModSlotIndex = _Ol53nnMTDDIModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 1, 1, 1),
    _Ol53nnMTDDIModSlotIndex_Type()
)
ol53nnMTDDIModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIModSlotIndex.setStatus("mandatory")


class _Ol53nnMTDDIModDownStreamModule_Type(Integer32):
    """Custom type ol53nnMTDDIModDownStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMTDDIModDownStreamModule_Type.__name__ = "Integer32"
_Ol53nnMTDDIModDownStreamModule_Object = MibTableColumn
ol53nnMTDDIModDownStreamModule = _Ol53nnMTDDIModDownStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 1, 1, 2),
    _Ol53nnMTDDIModDownStreamModule_Type()
)
ol53nnMTDDIModDownStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIModDownStreamModule.setStatus("mandatory")


class _Ol53nnMTDDIModUpStreamModule_Type(Integer32):
    """Custom type ol53nnMTDDIModUpStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMTDDIModUpStreamModule_Type.__name__ = "Integer32"
_Ol53nnMTDDIModUpStreamModule_Object = MibTableColumn
ol53nnMTDDIModUpStreamModule = _Ol53nnMTDDIModUpStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 1, 1, 3),
    _Ol53nnMTDDIModUpStreamModule_Type()
)
ol53nnMTDDIModUpStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIModUpStreamModule.setStatus("mandatory")


class _Ol53nnMTDDIModDownStreamOperPath_Type(Integer32):
    """Custom type ol53nnMTDDIModDownStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMTDDIModDownStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMTDDIModDownStreamOperPath_Object = MibTableColumn
ol53nnMTDDIModDownStreamOperPath = _Ol53nnMTDDIModDownStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 1, 1, 4),
    _Ol53nnMTDDIModDownStreamOperPath_Type()
)
ol53nnMTDDIModDownStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIModDownStreamOperPath.setStatus("mandatory")


class _Ol53nnMTDDIModUpStreamOperPath_Type(Integer32):
    """Custom type ol53nnMTDDIModUpStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMTDDIModUpStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMTDDIModUpStreamOperPath_Object = MibTableColumn
ol53nnMTDDIModUpStreamOperPath = _Ol53nnMTDDIModUpStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 1, 1, 5),
    _Ol53nnMTDDIModUpStreamOperPath_Type()
)
ol53nnMTDDIModUpStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIModUpStreamOperPath.setStatus("mandatory")


class _Ol53nnMTDDIModRingInfo_Type(OctetString):
    """Custom type ol53nnMTDDIModRingInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ol53nnMTDDIModRingInfo_Type.__name__ = "OctetString"
_Ol53nnMTDDIModRingInfo_Object = MibTableColumn
ol53nnMTDDIModRingInfo = _Ol53nnMTDDIModRingInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 1, 1, 6),
    _Ol53nnMTDDIModRingInfo_Type()
)
ol53nnMTDDIModRingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIModRingInfo.setStatus("mandatory")
_Ol53nnMTDDIPortTable_Object = MibTable
ol53nnMTDDIPortTable = _Ol53nnMTDDIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2)
)
if mibBuilder.loadTexts:
    ol53nnMTDDIPortTable.setStatus("mandatory")
_Ol53nnMTDDIPortEntry_Object = MibTableRow
ol53nnMTDDIPortEntry = _Ol53nnMTDDIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1)
)
ol53nnMTDDIPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMTDDIPortSlotIndex"),
    (0, "CHIPCOMMIB", "ol53nnMTDDIPortIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMTDDIPortEntry.setStatus("mandatory")
_Ol53nnMTDDIPortSlotIndex_Type = Integer32
_Ol53nnMTDDIPortSlotIndex_Object = MibTableColumn
ol53nnMTDDIPortSlotIndex = _Ol53nnMTDDIPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1, 1),
    _Ol53nnMTDDIPortSlotIndex_Type()
)
ol53nnMTDDIPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIPortSlotIndex.setStatus("mandatory")
_Ol53nnMTDDIPortIndex_Type = Integer32
_Ol53nnMTDDIPortIndex_Object = MibTableColumn
ol53nnMTDDIPortIndex = _Ol53nnMTDDIPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1, 2),
    _Ol53nnMTDDIPortIndex_Type()
)
ol53nnMTDDIPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIPortIndex.setStatus("mandatory")


class _Ol53nnMTDDIPortConfig_Type(Integer32):
    """Custom type ol53nnMTDDIPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("master", 4),
          ("slave", 3))
    )


_Ol53nnMTDDIPortConfig_Type.__name__ = "Integer32"
_Ol53nnMTDDIPortConfig_Object = MibTableColumn
ol53nnMTDDIPortConfig = _Ol53nnMTDDIPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1, 3),
    _Ol53nnMTDDIPortConfig_Type()
)
ol53nnMTDDIPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMTDDIPortConfig.setStatus("mandatory")


class _Ol53nnMTDDIPortPcmState_Type(Integer32):
    """Custom type ol53nnMTDDIPortPcmState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("pc0", 1),
          ("pc1", 2),
          ("pc2", 3),
          ("pc3", 4),
          ("pc4", 5),
          ("pc5", 6),
          ("pc6", 7),
          ("pc7", 8),
          ("pc8", 9),
          ("pc9", 10))
    )


_Ol53nnMTDDIPortPcmState_Type.__name__ = "Integer32"
_Ol53nnMTDDIPortPcmState_Object = MibTableColumn
ol53nnMTDDIPortPcmState = _Ol53nnMTDDIPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1, 4),
    _Ol53nnMTDDIPortPcmState_Type()
)
ol53nnMTDDIPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIPortPcmState.setStatus("mandatory")


class _Ol53nnMTDDIPortConnectState_Type(Integer32):
    """Custom type ol53nnMTDDIPortConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_Ol53nnMTDDIPortConnectState_Type.__name__ = "Integer32"
_Ol53nnMTDDIPortConnectState_Object = MibTableColumn
ol53nnMTDDIPortConnectState = _Ol53nnMTDDIPortConnectState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1, 5),
    _Ol53nnMTDDIPortConnectState_Type()
)
ol53nnMTDDIPortConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIPortConnectState.setStatus("mandatory")


class _Ol53nnMTDDIPortNeighbor_Type(Integer32):
    """Custom type ol53nnMTDDIPortNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("master", 4),
          ("slave", 3),
          ("unknown", 5))
    )


_Ol53nnMTDDIPortNeighbor_Type.__name__ = "Integer32"
_Ol53nnMTDDIPortNeighbor_Object = MibTableColumn
ol53nnMTDDIPortNeighbor = _Ol53nnMTDDIPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1, 6),
    _Ol53nnMTDDIPortNeighbor_Type()
)
ol53nnMTDDIPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIPortNeighbor.setStatus("mandatory")


class _Ol53nnMTDDIPortRemoteMACIndicated_Type(Integer32):
    """Custom type ol53nnMTDDIPortRemoteMACIndicated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol53nnMTDDIPortRemoteMACIndicated_Type.__name__ = "Integer32"
_Ol53nnMTDDIPortRemoteMACIndicated_Object = MibTableColumn
ol53nnMTDDIPortRemoteMACIndicated = _Ol53nnMTDDIPortRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1, 7),
    _Ol53nnMTDDIPortRemoteMACIndicated_Type()
)
ol53nnMTDDIPortRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIPortRemoteMACIndicated.setStatus("mandatory")


class _Ol53nnMTDDIPortBSFlag_Type(Integer32):
    """Custom type ol53nnMTDDIPortBSFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Ol53nnMTDDIPortBSFlag_Type.__name__ = "Integer32"
_Ol53nnMTDDIPortBSFlag_Object = MibTableColumn
ol53nnMTDDIPortBSFlag = _Ol53nnMTDDIPortBSFlag_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1, 8),
    _Ol53nnMTDDIPortBSFlag_Type()
)
ol53nnMTDDIPortBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIPortBSFlag.setStatus("mandatory")


class _Ol53nnMTDDIPortPCWithhold_Type(Integer32):
    """Custom type ol53nnMTDDIPortPCWithhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-m", 2),
          ("none", 1),
          ("other", 3))
    )


_Ol53nnMTDDIPortPCWithhold_Type.__name__ = "Integer32"
_Ol53nnMTDDIPortPCWithhold_Object = MibTableColumn
ol53nnMTDDIPortPCWithhold = _Ol53nnMTDDIPortPCWithhold_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1, 9),
    _Ol53nnMTDDIPortPCWithhold_Type()
)
ol53nnMTDDIPortPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIPortPCWithhold.setStatus("mandatory")


class _Ol53nnMTDDIPortLerCondition_Type(Integer32):
    """Custom type ol53nnMTDDIPortLerCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("okay", 2))
    )


_Ol53nnMTDDIPortLerCondition_Type.__name__ = "Integer32"
_Ol53nnMTDDIPortLerCondition_Object = MibTableColumn
ol53nnMTDDIPortLerCondition = _Ol53nnMTDDIPortLerCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 2, 1, 10),
    _Ol53nnMTDDIPortLerCondition_Type()
)
ol53nnMTDDIPortLerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDIPortLerCondition.setStatus("mandatory")
_Ol53nnMTDDITrunkTable_Object = MibTable
ol53nnMTDDITrunkTable = _Ol53nnMTDDITrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 3)
)
if mibBuilder.loadTexts:
    ol53nnMTDDITrunkTable.setStatus("mandatory")
_Ol53nnMTDDITrunkEntry_Object = MibTableRow
ol53nnMTDDITrunkEntry = _Ol53nnMTDDITrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 3, 1)
)
ol53nnMTDDITrunkEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ol53nnMTDDITrunkSlotIndex"),
    (0, "CHIPCOMMIB", "ol53nnMTDDITrunkIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMTDDITrunkEntry.setStatus("mandatory")
_Ol53nnMTDDITrunkSlotIndex_Type = Integer32
_Ol53nnMTDDITrunkSlotIndex_Object = MibTableColumn
ol53nnMTDDITrunkSlotIndex = _Ol53nnMTDDITrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 3, 1, 1),
    _Ol53nnMTDDITrunkSlotIndex_Type()
)
ol53nnMTDDITrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDITrunkSlotIndex.setStatus("mandatory")
_Ol53nnMTDDITrunkIndex_Type = Integer32
_Ol53nnMTDDITrunkIndex_Object = MibTableColumn
ol53nnMTDDITrunkIndex = _Ol53nnMTDDITrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 65, 3, 1, 2),
    _Ol53nnMTDDITrunkIndex_Type()
)
ol53nnMTDDITrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMTDDITrunkIndex.setStatus("mandatory")
_OlModSummaryTable_Object = MibTable
olModSummaryTable = _OlModSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 5)
)
if mibBuilder.loadTexts:
    olModSummaryTable.setStatus("mandatory")
_OlModSummaryEntry_Object = MibTableRow
olModSummaryEntry = _OlModSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 5, 1)
)
olModSummaryEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olModSummarySlotIndex"),
)
if mibBuilder.loadTexts:
    olModSummaryEntry.setStatus("mandatory")
_OlModSummarySlotIndex_Type = Integer32
_OlModSummarySlotIndex_Object = MibTableColumn
olModSummarySlotIndex = _OlModSummarySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 5, 1, 1),
    _OlModSummarySlotIndex_Type()
)
olModSummarySlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModSummarySlotIndex.setStatus("mandatory")


class _OlModSummaryInfo_Type(OctetString):
    """Custom type olModSummaryInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_OlModSummaryInfo_Type.__name__ = "OctetString"
_OlModSummaryInfo_Object = MibTableColumn
olModSummaryInfo = _OlModSummaryInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 5, 1, 2),
    _OlModSummaryInfo_Type()
)
olModSummaryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModSummaryInfo.setStatus("mandatory")
_OcModTable_Object = MibTable
ocModTable = _OcModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6)
)
if mibBuilder.loadTexts:
    ocModTable.setStatus("mandatory")
_OcModEntry_Object = MibTableRow
ocModEntry = _OcModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1)
)
ocModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ocModSlotIndex"),
    (0, "CHIPCOMMIB", "ocModSubSlotIndex"),
)
if mibBuilder.loadTexts:
    ocModEntry.setStatus("mandatory")
_OcModSlotIndex_Type = Integer32
_OcModSlotIndex_Object = MibTableColumn
ocModSlotIndex = _OcModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 1),
    _OcModSlotIndex_Type()
)
ocModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModSlotIndex.setStatus("mandatory")
_OcModSubSlotIndex_Type = Integer32
_OcModSubSlotIndex_Object = MibTableColumn
ocModSubSlotIndex = _OcModSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 2),
    _OcModSubSlotIndex_Type()
)
ocModSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModSubSlotIndex.setStatus("mandatory")


class _OcModType_Type(Integer32):
    """Custom type ocModType based on Integer32"""
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
              15,
              16,
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
              32,
              33,
              35,
              43,
              45,
              46,
              47,
              48,
              50,
              51,
              52,
              53,
              62,
              65)
        )
    )
    namedValues = NamedValues(
        *(("module-41nnH-ETP", 53),
          ("module-41nnH-MTP", 52),
          ("module-50nnM-CTL", 3),
          ("module-50nnM-HCTL", 33),
          ("module-50nnM-RCLS", 51),
          ("module-50nnM-RCTL", 23),
          ("module-51nnB-EE", 9),
          ("module-51nnI-x", 31),
          ("module-51nnM-AUIF", 12),
          ("module-51nnM-AUIM", 13),
          ("module-51nnM-BNC", 8),
          ("module-51nnM-FB", 24),
          ("module-51nnM-FBP", 16),
          ("module-51nnM-FIB", 5),
          ("module-51nnM-FL", 22),
          ("module-51nnM-FP", 15),
          ("module-51nnM-MGT", 4),
          ("module-51nnM-TP", 7),
          ("module-51nnM-TPCL", 29),
          ("module-51nnM-TPL", 17),
          ("module-51nnM-TPLS", 48),
          ("module-51nnM-TPPL", 18),
          ("module-51nnM-TS", 21),
          ("module-51nnM-UTP", 6),
          ("module-51nnR-EE", 11),
          ("module-51nnR-ES", 10),
          ("module-5208M-TP", 14),
          ("module-52nnB-TT", 30),
          ("module-52nnM-EC", 62),
          ("module-52nnM-FR", 20),
          ("module-52nnM-MGT", 32),
          ("module-52nnM-TP", 19),
          ("module-53nnM-FBMIC", 26),
          ("module-53nnM-FIBST", 27),
          ("module-53nnM-MGT", 25),
          ("module-53nnM-STP", 28),
          ("module-53nnM-TDDI", 65),
          ("module-60nnM-MGT", 43),
          ("module-60nnM-RCTL", 50),
          ("module-61nnD-MGT", 45),
          ("module-61nnM-CAR", 35),
          ("module-61nnM-FBP", 46),
          ("module-61nnM-TPL", 47),
          ("module-unknown", 2),
          ("module-unmanageable", 1))
    )


_OcModType_Type.__name__ = "Integer32"
_OcModType_Object = MibTableColumn
ocModType = _OcModType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 3),
    _OcModType_Type()
)
ocModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModType.setStatus("mandatory")


class _OcModClass_Type(Integer32):
    """Custom type ocModClass based on Integer32"""
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
              15,
              16,
              17,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("controller", 1),
          ("ethernet-carrier", 14),
          ("ethernet-connswitching-media", 10),
          ("ethernet-interconnect", 4),
          ("ethernet-media", 3),
          ("ethernet-media-extended", 19),
          ("ethernet-portswitching-media", 5),
          ("fddi-media", 8),
          ("fddi-mgmt", 12),
          ("mgmt", 2),
          ("network-monitor", 16),
          ("oncore-download", 17),
          ("oncore-oem-specials", 15),
          ("oncore-token-ring-media", 13),
          ("online-token-ring-mod-interconnect", 20),
          ("terminal-server", 7),
          ("token-ring-interconnect", 11),
          ("token-ring-media", 6),
          ("token-ring-mgmt", 9))
    )


_OcModClass_Type.__name__ = "Integer32"
_OcModClass_Object = MibTableColumn
ocModClass = _OcModClass_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 4),
    _OcModClass_Type()
)
ocModClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModClass.setStatus("mandatory")


class _OcModDescr_Type(DisplayString):
    """Custom type ocModDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OcModDescr_Type.__name__ = "DisplayString"
_OcModDescr_Object = MibTableColumn
ocModDescr = _OcModDescr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 5),
    _OcModDescr_Type()
)
ocModDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModDescr.setStatus("mandatory")


class _OcModVersion_Type(DisplayString):
    """Custom type ocModVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcModVersion_Type.__name__ = "DisplayString"
_OcModVersion_Object = MibTableColumn
ocModVersion = _OcModVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 6),
    _OcModVersion_Type()
)
ocModVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModVersion.setStatus("mandatory")


class _OcModVendor_Type(Integer32):
    """Custom type ocModVendor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("chipcom", 1),
          ("cisco", 2),
          ("datability", 5),
          ("ibm", 6),
          ("intellicom", 9),
          ("pilkington", 3),
          ("raycom", 7),
          ("retix", 8))
    )


_OcModVendor_Type.__name__ = "Integer32"
_OcModVendor_Object = MibTableColumn
ocModVendor = _OcModVendor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 7),
    _OcModVendor_Type()
)
ocModVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModVendor.setStatus("mandatory")


class _OcModResetModule_Type(Integer32):
    """Custom type ocModResetModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_OcModResetModule_Type.__name__ = "Integer32"
_OcModResetModule_Object = MibTableColumn
ocModResetModule = _OcModResetModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 8),
    _OcModResetModule_Type()
)
ocModResetModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocModResetModule.setStatus("mandatory")


class _OcModConfigToDips_Type(Integer32):
    """Custom type ocModConfigToDips based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configure", 2),
          ("noConfigure", 1))
    )


_OcModConfigToDips_Type.__name__ = "Integer32"
_OcModConfigToDips_Object = MibTableColumn
ocModConfigToDips = _OcModConfigToDips_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 9),
    _OcModConfigToDips_Type()
)
ocModConfigToDips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocModConfigToDips.setStatus("mandatory")


class _OcModConfigured_Type(Integer32):
    """Custom type ocModConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("notConfigured", 1))
    )


_OcModConfigured_Type.__name__ = "Integer32"
_OcModConfigured_Object = MibTableColumn
ocModConfigured = _OcModConfigured_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 10),
    _OcModConfigured_Type()
)
ocModConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModConfigured.setStatus("mandatory")


class _OcModNetwork_Type(Integer32):
    """Custom type ocModNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
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
              15,
              16,
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
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36),
          ("fddi-1", 16),
          ("fddi-2", 17),
          ("fddi-3", 18),
          ("fddi-4", 19),
          ("front-panel", 5),
          ("isolated", 2),
          ("isolated-1", 21),
          ("isolated-10", 30),
          ("isolated-11", 31),
          ("isolated-2", 22),
          ("isolated-3", 23),
          ("isolated-4", 24),
          ("isolated-5", 25),
          ("isolated-6", 26),
          ("isolated-7", 27),
          ("isolated-8", 28),
          ("isolated-9", 29),
          ("other", 1),
          ("per-connector", 20),
          ("port-switching", 3),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OcModNetwork_Type.__name__ = "Integer32"
_OcModNetwork_Object = MibTableColumn
ocModNetwork = _OcModNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 11),
    _OcModNetwork_Type()
)
ocModNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocModNetwork.setStatus("mandatory")


class _OcModNetworkType_Type(Integer32):
    """Custom type ocModNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 5),
          ("fddi", 7),
          ("other", 1),
          ("port-switching", 3),
          ("serial", 8),
          ("token-ring", 6))
    )


_OcModNetworkType_Type.__name__ = "Integer32"
_OcModNetworkType_Object = MibTableColumn
ocModNetworkType = _OcModNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 12),
    _OcModNetworkType_Type()
)
ocModNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModNetworkType.setStatus("mandatory")


class _OcModStatus_Type(Integer32):
    """Custom type ocModStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20,
              21,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("booting", 20),
          ("fatalError", 10),
          ("notInserted", 30),
          ("okay", 1),
          ("partial-failure", 21),
          ("speedMismatch", 31))
    )


_OcModStatus_Type.__name__ = "Integer32"
_OcModStatus_Object = MibTableColumn
ocModStatus = _OcModStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 13),
    _OcModStatus_Type()
)
ocModStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModStatus.setStatus("mandatory")
_OcModNumPorts_Type = Integer32
_OcModNumPorts_Object = MibTableColumn
ocModNumPorts = _OcModNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 14),
    _OcModNumPorts_Type()
)
ocModNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModNumPorts.setStatus("mandatory")
_OcModNumTrunks_Type = Integer32
_OcModNumTrunks_Object = MibTableColumn
ocModNumTrunks = _OcModNumTrunks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 15),
    _OcModNumTrunks_Type()
)
ocModNumTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModNumTrunks.setStatus("mandatory")
_OcModNumSubSlots_Type = Integer32
_OcModNumSubSlots_Object = MibTableColumn
ocModNumSubSlots = _OcModNumSubSlots_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 6, 1, 16),
    _OcModNumSubSlots_Type()
)
ocModNumSubSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocModNumSubSlots.setStatus("mandatory")
_OlNets_ObjectIdentity = ObjectIdentity
olNets = _OlNets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5)
)
_OlNet_ObjectIdentity = ObjectIdentity
olNet = _OlNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1)
)
_OlNetDPTable_Object = MibTable
olNetDPTable = _OlNetDPTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    olNetDPTable.setStatus("mandatory")
_OlNetDPEntry_Object = MibTableRow
olNetDPEntry = _OlNetDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 1, 1)
)
olNetDPEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olNetDPDataPath"),
)
if mibBuilder.loadTexts:
    olNetDPEntry.setStatus("mandatory")


class _OlNetDPDataPath_Type(Integer32):
    """Custom type olNetDPDataPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
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
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-path-1", 6),
          ("ethernet-path-2", 7),
          ("ethernet-path-3", 8),
          ("ethernet-path-4", 32),
          ("ethernet-path-5", 33),
          ("ethernet-path-6", 34),
          ("ethernet-path-7", 35),
          ("ethernet-path-8", 36),
          ("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("token-ring-path-1", 9),
          ("token-ring-path-10", 18),
          ("token-ring-path-11", 19),
          ("token-ring-path-12", 20),
          ("token-ring-path-13", 21),
          ("token-ring-path-14", 22),
          ("token-ring-path-15", 23),
          ("token-ring-path-2", 10),
          ("token-ring-path-3", 11),
          ("token-ring-path-4", 12),
          ("token-ring-path-5", 13),
          ("token-ring-path-6", 14),
          ("token-ring-path-7", 15),
          ("token-ring-path-8", 16),
          ("token-ring-path-9", 17))
    )


_OlNetDPDataPath_Type.__name__ = "Integer32"
_OlNetDPDataPath_Object = MibTableColumn
olNetDPDataPath = _OlNetDPDataPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 1, 1, 1),
    _OlNetDPDataPath_Type()
)
olNetDPDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetDPDataPath.setStatus("mandatory")


class _OlNetDPNetID_Type(Integer32):
    """Custom type olNetDPNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("fddi-1", 16),
          ("fddi-2", 17),
          ("fddi-3", 18),
          ("fddi-4", 19),
          ("notUsed", 1),
          ("otherProto", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlNetDPNetID_Type.__name__ = "Integer32"
_OlNetDPNetID_Object = MibTableColumn
olNetDPNetID = _OlNetDPNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 1, 1, 2),
    _OlNetDPNetID_Type()
)
olNetDPNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetDPNetID.setStatus("mandatory")
_OlNetSecurityMACTable_Object = MibTable
olNetSecurityMACTable = _OlNetSecurityMACTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    olNetSecurityMACTable.setStatus("mandatory")
_OlNetSecurityMACEntry_Object = MibTableRow
olNetSecurityMACEntry = _OlNetSecurityMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 2, 1)
)
olNetSecurityMACEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olNetSecurityMACSlotIndex"),
    (0, "CHIPCOMMIB", "olNetSecurityMACPortIndex"),
    (0, "CHIPCOMMIB", "olNetSecurityMACAddress"),
)
if mibBuilder.loadTexts:
    olNetSecurityMACEntry.setStatus("mandatory")
_OlNetSecurityMACSlotIndex_Type = Integer32
_OlNetSecurityMACSlotIndex_Object = MibTableColumn
olNetSecurityMACSlotIndex = _OlNetSecurityMACSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 2, 1, 1),
    _OlNetSecurityMACSlotIndex_Type()
)
olNetSecurityMACSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetSecurityMACSlotIndex.setStatus("mandatory")
_OlNetSecurityMACPortIndex_Type = Integer32
_OlNetSecurityMACPortIndex_Object = MibTableColumn
olNetSecurityMACPortIndex = _OlNetSecurityMACPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 2, 1, 2),
    _OlNetSecurityMACPortIndex_Type()
)
olNetSecurityMACPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetSecurityMACPortIndex.setStatus("mandatory")
_OlNetSecurityMACAddress_Type = MacAddress
_OlNetSecurityMACAddress_Object = MibTableColumn
olNetSecurityMACAddress = _OlNetSecurityMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 2, 1, 3),
    _OlNetSecurityMACAddress_Type()
)
olNetSecurityMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetSecurityMACAddress.setStatus("mandatory")


class _OlNetSecurityMACMode_Type(Integer32):
    """Custom type olNetSecurityMACMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OlNetSecurityMACMode_Type.__name__ = "Integer32"
_OlNetSecurityMACMode_Object = MibTableColumn
olNetSecurityMACMode = _OlNetSecurityMACMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 2, 1, 4),
    _OlNetSecurityMACMode_Type()
)
olNetSecurityMACMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetSecurityMACMode.setStatus("mandatory")


class _OlNetSecurityMACStatus_Type(Integer32):
    """Custom type olNetSecurityMACStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_OlNetSecurityMACStatus_Type.__name__ = "Integer32"
_OlNetSecurityMACStatus_Object = MibTableColumn
olNetSecurityMACStatus = _OlNetSecurityMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 2, 1, 5),
    _OlNetSecurityMACStatus_Type()
)
olNetSecurityMACStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetSecurityMACStatus.setStatus("mandatory")
_OlNetOlSec_ObjectIdentity = ObjectIdentity
olNetOlSec = _OlNetOlSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3)
)
_OlNetOlSecAddrTable_Object = MibTable
olNetOlSecAddrTable = _OlNetOlSecAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    olNetOlSecAddrTable.setStatus("mandatory")
_OlNetOlSecAddrEntry_Object = MibTableRow
olNetOlSecAddrEntry = _OlNetOlSecAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 1, 1)
)
olNetOlSecAddrEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olNetOlSecAddrSlotIndex"),
    (0, "CHIPCOMMIB", "olNetOlSecAddrPortIndex"),
    (0, "CHIPCOMMIB", "olNetOlSecAddrAddress"),
)
if mibBuilder.loadTexts:
    olNetOlSecAddrEntry.setStatus("mandatory")
_OlNetOlSecAddrSlotIndex_Type = Integer32
_OlNetOlSecAddrSlotIndex_Object = MibTableColumn
olNetOlSecAddrSlotIndex = _OlNetOlSecAddrSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 1, 1, 1),
    _OlNetOlSecAddrSlotIndex_Type()
)
olNetOlSecAddrSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecAddrSlotIndex.setStatus("mandatory")
_OlNetOlSecAddrPortIndex_Type = Integer32
_OlNetOlSecAddrPortIndex_Object = MibTableColumn
olNetOlSecAddrPortIndex = _OlNetOlSecAddrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 1, 1, 2),
    _OlNetOlSecAddrPortIndex_Type()
)
olNetOlSecAddrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecAddrPortIndex.setStatus("mandatory")
_OlNetOlSecAddrAddress_Type = MacAddress
_OlNetOlSecAddrAddress_Object = MibTableColumn
olNetOlSecAddrAddress = _OlNetOlSecAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 1, 1, 3),
    _OlNetOlSecAddrAddress_Type()
)
olNetOlSecAddrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecAddrAddress.setStatus("mandatory")


class _OlNetOlSecAddrStatus_Type(Integer32):
    """Custom type olNetOlSecAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_OlNetOlSecAddrStatus_Type.__name__ = "Integer32"
_OlNetOlSecAddrStatus_Object = MibTableColumn
olNetOlSecAddrStatus = _OlNetOlSecAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 1, 1, 4),
    _OlNetOlSecAddrStatus_Type()
)
olNetOlSecAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecAddrStatus.setStatus("mandatory")
_OlNetOlSecControlTable_Object = MibTable
olNetOlSecControlTable = _OlNetOlSecControlTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    olNetOlSecControlTable.setStatus("mandatory")
_OlNetOlSecControlEntry_Object = MibTableRow
olNetOlSecControlEntry = _OlNetOlSecControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 2, 1)
)
olNetOlSecControlEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olNetOlSecControlSlotIndex"),
    (0, "CHIPCOMMIB", "olNetOlSecControlPortIndex"),
)
if mibBuilder.loadTexts:
    olNetOlSecControlEntry.setStatus("mandatory")
_OlNetOlSecControlSlotIndex_Type = Integer32
_OlNetOlSecControlSlotIndex_Object = MibTableColumn
olNetOlSecControlSlotIndex = _OlNetOlSecControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 2, 1, 1),
    _OlNetOlSecControlSlotIndex_Type()
)
olNetOlSecControlSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecControlSlotIndex.setStatus("mandatory")
_OlNetOlSecControlPortIndex_Type = Integer32
_OlNetOlSecControlPortIndex_Object = MibTableColumn
olNetOlSecControlPortIndex = _OlNetOlSecControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 2, 1, 2),
    _OlNetOlSecControlPortIndex_Type()
)
olNetOlSecControlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecControlPortIndex.setStatus("mandatory")


class _OlNetOlSecControlMode_Type(Integer32):
    """Custom type olNetOlSecControlMode based on Integer32"""
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


_OlNetOlSecControlMode_Type.__name__ = "Integer32"
_OlNetOlSecControlMode_Object = MibTableColumn
olNetOlSecControlMode = _OlNetOlSecControlMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 2, 1, 3),
    _OlNetOlSecControlMode_Type()
)
olNetOlSecControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecControlMode.setStatus("mandatory")


class _OlNetOlSecControlSecType_Type(Integer32):
    """Custom type olNetOlSecControlSecType based on Integer32"""
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
        *(("eavesdropping-only", 3),
          ("full", 1),
          ("intrusion-only", 2),
          ("no-security", 4))
    )


_OlNetOlSecControlSecType_Type.__name__ = "Integer32"
_OlNetOlSecControlSecType_Object = MibTableColumn
olNetOlSecControlSecType = _OlNetOlSecControlSecType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 2, 1, 4),
    _OlNetOlSecControlSecType_Type()
)
olNetOlSecControlSecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecControlSecType.setStatus("mandatory")


class _OlNetOlSecControlActOnIntr_Type(Integer32):
    """Custom type olNetOlSecControlActOnIntr based on Integer32"""
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
        *(("disable-and-trap", 1),
          ("disable-only", 2),
          ("no-action", 4),
          ("trap-only", 3))
    )


_OlNetOlSecControlActOnIntr_Type.__name__ = "Integer32"
_OlNetOlSecControlActOnIntr_Object = MibTableColumn
olNetOlSecControlActOnIntr = _OlNetOlSecControlActOnIntr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 2, 1, 5),
    _OlNetOlSecControlActOnIntr_Type()
)
olNetOlSecControlActOnIntr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecControlActOnIntr.setStatus("mandatory")


class _OlNetOlSecControlClearAddrs_Type(Integer32):
    """Custom type olNetOlSecControlClearAddrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear-all-addrs", 1),
          ("not-clear", 2))
    )


_OlNetOlSecControlClearAddrs_Type.__name__ = "Integer32"
_OlNetOlSecControlClearAddrs_Object = MibTableColumn
olNetOlSecControlClearAddrs = _OlNetOlSecControlClearAddrs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 2, 1, 6),
    _OlNetOlSecControlClearAddrs_Type()
)
olNetOlSecControlClearAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecControlClearAddrs.setStatus("mandatory")


class _OlNetOlSecControlAutolearnMask_Type(Integer32):
    """Custom type olNetOlSecControlAutolearnMask based on Integer32"""
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


_OlNetOlSecControlAutolearnMask_Type.__name__ = "Integer32"
_OlNetOlSecControlAutolearnMask_Object = MibTableColumn
olNetOlSecControlAutolearnMask = _OlNetOlSecControlAutolearnMask_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 2, 1, 7),
    _OlNetOlSecControlAutolearnMask_Type()
)
olNetOlSecControlAutolearnMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecControlAutolearnMask.setStatus("mandatory")
_OlNetOlSecAutolearn_ObjectIdentity = ObjectIdentity
olNetOlSecAutolearn = _OlNetOlSecAutolearn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 3)
)


class _OlNetOlSecAutolearnTrigger_Type(Integer32):
    """Custom type olNetOlSecAutolearnTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autolearn", 1),
          ("no-autolearn", 2))
    )


_OlNetOlSecAutolearnTrigger_Type.__name__ = "Integer32"
_OlNetOlSecAutolearnTrigger_Object = MibScalar
olNetOlSecAutolearnTrigger = _OlNetOlSecAutolearnTrigger_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 3, 1),
    _OlNetOlSecAutolearnTrigger_Type()
)
olNetOlSecAutolearnTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecAutolearnTrigger.setStatus("mandatory")


class _OlNetOlSecAutolearnDownload_Type(Integer32):
    """Custom type olNetOlSecAutolearnDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download-addresses", 1),
          ("no-download", 2))
    )


_OlNetOlSecAutolearnDownload_Type.__name__ = "Integer32"
_OlNetOlSecAutolearnDownload_Object = MibScalar
olNetOlSecAutolearnDownload = _OlNetOlSecAutolearnDownload_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 3, 2),
    _OlNetOlSecAutolearnDownload_Type()
)
olNetOlSecAutolearnDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecAutolearnDownload.setStatus("mandatory")
_OlNetOlSecLearnTable_Object = MibTable
olNetOlSecLearnTable = _OlNetOlSecLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 4)
)
if mibBuilder.loadTexts:
    olNetOlSecLearnTable.setStatus("mandatory")
_OlNetOlSecLearnEntry_Object = MibTableRow
olNetOlSecLearnEntry = _OlNetOlSecLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 4, 1)
)
olNetOlSecLearnEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olNetOlSecLearnSlotIndex"),
    (0, "CHIPCOMMIB", "olNetOlSecLearnPortIndex"),
    (0, "CHIPCOMMIB", "olNetOlSecLearnAddress"),
)
if mibBuilder.loadTexts:
    olNetOlSecLearnEntry.setStatus("mandatory")
_OlNetOlSecLearnSlotIndex_Type = Integer32
_OlNetOlSecLearnSlotIndex_Object = MibTableColumn
olNetOlSecLearnSlotIndex = _OlNetOlSecLearnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 4, 1, 1),
    _OlNetOlSecLearnSlotIndex_Type()
)
olNetOlSecLearnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecLearnSlotIndex.setStatus("mandatory")
_OlNetOlSecLearnPortIndex_Type = Integer32
_OlNetOlSecLearnPortIndex_Object = MibTableColumn
olNetOlSecLearnPortIndex = _OlNetOlSecLearnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 4, 1, 2),
    _OlNetOlSecLearnPortIndex_Type()
)
olNetOlSecLearnPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecLearnPortIndex.setStatus("mandatory")
_OlNetOlSecLearnAddress_Type = MacAddress
_OlNetOlSecLearnAddress_Object = MibTableColumn
olNetOlSecLearnAddress = _OlNetOlSecLearnAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 4, 1, 3),
    _OlNetOlSecLearnAddress_Type()
)
olNetOlSecLearnAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecLearnAddress.setStatus("mandatory")


class _OlNetOlSecLearnStatus_Type(Integer32):
    """Custom type olNetOlSecLearnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_OlNetOlSecLearnStatus_Type.__name__ = "Integer32"
_OlNetOlSecLearnStatus_Object = MibTableColumn
olNetOlSecLearnStatus = _OlNetOlSecLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 4, 1, 4),
    _OlNetOlSecLearnStatus_Type()
)
olNetOlSecLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olNetOlSecLearnStatus.setStatus("mandatory")
_OlNetOlSecIntruderTable_Object = MibTable
olNetOlSecIntruderTable = _OlNetOlSecIntruderTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 5)
)
if mibBuilder.loadTexts:
    olNetOlSecIntruderTable.setStatus("mandatory")
_OlNetOlSecIntruderEntry_Object = MibTableRow
olNetOlSecIntruderEntry = _OlNetOlSecIntruderEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 5, 1)
)
olNetOlSecIntruderEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olNetOlSecIntruderChronIndex"),
)
if mibBuilder.loadTexts:
    olNetOlSecIntruderEntry.setStatus("mandatory")
_OlNetOlSecIntruderChronIndex_Type = Integer32
_OlNetOlSecIntruderChronIndex_Object = MibTableColumn
olNetOlSecIntruderChronIndex = _OlNetOlSecIntruderChronIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 5, 1, 1),
    _OlNetOlSecIntruderChronIndex_Type()
)
olNetOlSecIntruderChronIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecIntruderChronIndex.setStatus("mandatory")
_OlNetOlSecIntruderSlot_Type = Integer32
_OlNetOlSecIntruderSlot_Object = MibTableColumn
olNetOlSecIntruderSlot = _OlNetOlSecIntruderSlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 5, 1, 2),
    _OlNetOlSecIntruderSlot_Type()
)
olNetOlSecIntruderSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecIntruderSlot.setStatus("mandatory")
_OlNetOlSecIntruderPort_Type = Integer32
_OlNetOlSecIntruderPort_Object = MibTableColumn
olNetOlSecIntruderPort = _OlNetOlSecIntruderPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 5, 1, 3),
    _OlNetOlSecIntruderPort_Type()
)
olNetOlSecIntruderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecIntruderPort.setStatus("mandatory")
_OlNetOlSecIntruderAddress_Type = MacAddress
_OlNetOlSecIntruderAddress_Object = MibTableColumn
olNetOlSecIntruderAddress = _OlNetOlSecIntruderAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 5, 1, 4),
    _OlNetOlSecIntruderAddress_Type()
)
olNetOlSecIntruderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecIntruderAddress.setStatus("mandatory")
_OlNetOlSecIntruderTimeSince_Type = TimeTicks
_OlNetOlSecIntruderTimeSince_Object = MibTableColumn
olNetOlSecIntruderTimeSince = _OlNetOlSecIntruderTimeSince_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 5, 1, 5),
    _OlNetOlSecIntruderTimeSince_Type()
)
olNetOlSecIntruderTimeSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecIntruderTimeSince.setStatus("mandatory")


class _OlNetOlSecIntruderDisabled_Type(Integer32):
    """Custom type olNetOlSecIntruderDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto-disabled", 1),
          ("not-auto-disabled", 2))
    )


_OlNetOlSecIntruderDisabled_Type.__name__ = "Integer32"
_OlNetOlSecIntruderDisabled_Object = MibTableColumn
olNetOlSecIntruderDisabled = _OlNetOlSecIntruderDisabled_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 5, 1, 6),
    _OlNetOlSecIntruderDisabled_Type()
)
olNetOlSecIntruderDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecIntruderDisabled.setStatus("mandatory")
_OlNetOlSecPortIntrTable_Object = MibTable
olNetOlSecPortIntrTable = _OlNetOlSecPortIntrTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 6)
)
if mibBuilder.loadTexts:
    olNetOlSecPortIntrTable.setStatus("mandatory")
_OlNetOlSecPortIntrEntry_Object = MibTableRow
olNetOlSecPortIntrEntry = _OlNetOlSecPortIntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 6, 1)
)
olNetOlSecPortIntrEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olNetOlSecPortIntrSlotIndex"),
    (0, "CHIPCOMMIB", "olNetOlSecPortIntrPortIndex"),
    (0, "CHIPCOMMIB", "olNetOlSecPortIntrChronIndex"),
)
if mibBuilder.loadTexts:
    olNetOlSecPortIntrEntry.setStatus("mandatory")
_OlNetOlSecPortIntrSlotIndex_Type = Integer32
_OlNetOlSecPortIntrSlotIndex_Object = MibTableColumn
olNetOlSecPortIntrSlotIndex = _OlNetOlSecPortIntrSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 6, 1, 1),
    _OlNetOlSecPortIntrSlotIndex_Type()
)
olNetOlSecPortIntrSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecPortIntrSlotIndex.setStatus("mandatory")
_OlNetOlSecPortIntrPortIndex_Type = Integer32
_OlNetOlSecPortIntrPortIndex_Object = MibTableColumn
olNetOlSecPortIntrPortIndex = _OlNetOlSecPortIntrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 6, 1, 2),
    _OlNetOlSecPortIntrPortIndex_Type()
)
olNetOlSecPortIntrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecPortIntrPortIndex.setStatus("mandatory")
_OlNetOlSecPortIntrChronIndex_Type = Integer32
_OlNetOlSecPortIntrChronIndex_Object = MibTableColumn
olNetOlSecPortIntrChronIndex = _OlNetOlSecPortIntrChronIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 6, 1, 3),
    _OlNetOlSecPortIntrChronIndex_Type()
)
olNetOlSecPortIntrChronIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecPortIntrChronIndex.setStatus("mandatory")
_OlNetOlSecPortIntrAddress_Type = MacAddress
_OlNetOlSecPortIntrAddress_Object = MibTableColumn
olNetOlSecPortIntrAddress = _OlNetOlSecPortIntrAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 6, 1, 4),
    _OlNetOlSecPortIntrAddress_Type()
)
olNetOlSecPortIntrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecPortIntrAddress.setStatus("mandatory")
_OlNetOlSecPortIntrTimeSince_Type = TimeTicks
_OlNetOlSecPortIntrTimeSince_Object = MibTableColumn
olNetOlSecPortIntrTimeSince = _OlNetOlSecPortIntrTimeSince_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 6, 1, 5),
    _OlNetOlSecPortIntrTimeSince_Type()
)
olNetOlSecPortIntrTimeSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecPortIntrTimeSince.setStatus("mandatory")


class _OlNetOlSecPortIntrDisabled_Type(Integer32):
    """Custom type olNetOlSecPortIntrDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto-disabled", 1),
          ("not-auto-disabled", 2))
    )


_OlNetOlSecPortIntrDisabled_Type.__name__ = "Integer32"
_OlNetOlSecPortIntrDisabled_Object = MibTableColumn
olNetOlSecPortIntrDisabled = _OlNetOlSecPortIntrDisabled_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 6, 1, 6),
    _OlNetOlSecPortIntrDisabled_Type()
)
olNetOlSecPortIntrDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecPortIntrDisabled.setStatus("mandatory")
_OlNetOlSecTrap_ObjectIdentity = ObjectIdentity
olNetOlSecTrap = _OlNetOlSecTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 7)
)


class _OlNetOlSecTrapReason_Type(Integer32):
    """Custom type olNetOlSecTrapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intrusion-attempt", 2),
          ("not-applicable", 1))
    )


_OlNetOlSecTrapReason_Type.__name__ = "Integer32"
_OlNetOlSecTrapReason_Object = MibScalar
olNetOlSecTrapReason = _OlNetOlSecTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1, 3, 7, 1),
    _OlNetOlSecTrapReason_Type()
)
olNetOlSecTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olNetOlSecTrapReason.setStatus("mandatory")
_OlEnet_ObjectIdentity = ObjectIdentity
olEnet = _OlEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2)
)
_OlEnetStatsTable_Object = MibTable
olEnetStatsTable = _OlEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    olEnetStatsTable.setStatus("mandatory")
_OlEnetStatsEntry_Object = MibTableRow
olEnetStatsEntry = _OlEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1)
)
olEnetStatsEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olEnetStatsNetID"),
)
if mibBuilder.loadTexts:
    olEnetStatsEntry.setStatus("mandatory")


class _OlEnetStatsNetID_Type(Integer32):
    """Custom type olEnetStatsNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36))
    )


_OlEnetStatsNetID_Type.__name__ = "Integer32"
_OlEnetStatsNetID_Object = MibTableColumn
olEnetStatsNetID = _OlEnetStatsNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 1),
    _OlEnetStatsNetID_Type()
)
olEnetStatsNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsNetID.setStatus("mandatory")
_OlEnetStatsFramesRcvdOks_Type = Counter32
_OlEnetStatsFramesRcvdOks_Object = MibTableColumn
olEnetStatsFramesRcvdOks = _OlEnetStatsFramesRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 2),
    _OlEnetStatsFramesRcvdOks_Type()
)
olEnetStatsFramesRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsFramesRcvdOks.setStatus("mandatory")
_OlEnetStatsOctetsRcvdOks_Type = Counter32
_OlEnetStatsOctetsRcvdOks_Object = MibTableColumn
olEnetStatsOctetsRcvdOks = _OlEnetStatsOctetsRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 3),
    _OlEnetStatsOctetsRcvdOks_Type()
)
olEnetStatsOctetsRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsOctetsRcvdOks.setStatus("mandatory")
_OlEnetStatsMcastRcvdOks_Type = Counter32
_OlEnetStatsMcastRcvdOks_Object = MibTableColumn
olEnetStatsMcastRcvdOks = _OlEnetStatsMcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 4),
    _OlEnetStatsMcastRcvdOks_Type()
)
olEnetStatsMcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsMcastRcvdOks.setStatus("mandatory")
_OlEnetStatsBcastRcvdOks_Type = Counter32
_OlEnetStatsBcastRcvdOks_Object = MibTableColumn
olEnetStatsBcastRcvdOks = _OlEnetStatsBcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 5),
    _OlEnetStatsBcastRcvdOks_Type()
)
olEnetStatsBcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsBcastRcvdOks.setStatus("mandatory")
_OlEnetStatsFrameTooLongs_Type = Counter32
_OlEnetStatsFrameTooLongs_Object = MibTableColumn
olEnetStatsFrameTooLongs = _OlEnetStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 6),
    _OlEnetStatsFrameTooLongs_Type()
)
olEnetStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsFrameTooLongs.setStatus("mandatory")
_OlEnetStatsAlignmentErrors_Type = Counter32
_OlEnetStatsAlignmentErrors_Object = MibTableColumn
olEnetStatsAlignmentErrors = _OlEnetStatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 7),
    _OlEnetStatsAlignmentErrors_Type()
)
olEnetStatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsAlignmentErrors.setStatus("mandatory")
_OlEnetStatsFCSErrors_Type = Counter32
_OlEnetStatsFCSErrors_Object = MibTableColumn
olEnetStatsFCSErrors = _OlEnetStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 8),
    _OlEnetStatsFCSErrors_Type()
)
olEnetStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsFCSErrors.setStatus("mandatory")
_OlEnetStatsRunts_Type = Counter32
_OlEnetStatsRunts_Object = MibTableColumn
olEnetStatsRunts = _OlEnetStatsRunts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 9),
    _OlEnetStatsRunts_Type()
)
olEnetStatsRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsRunts.setStatus("mandatory")
_OlEnetStatsLocalColls_Type = Counter32
_OlEnetStatsLocalColls_Object = MibTableColumn
olEnetStatsLocalColls = _OlEnetStatsLocalColls_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 10),
    _OlEnetStatsLocalColls_Type()
)
olEnetStatsLocalColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsLocalColls.setStatus("mandatory")
_OlEnetStatsDropEvents_Type = Counter32
_OlEnetStatsDropEvents_Object = MibTableColumn
olEnetStatsDropEvents = _OlEnetStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 11),
    _OlEnetStatsDropEvents_Type()
)
olEnetStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsDropEvents.setStatus("mandatory")
_OlEnetStatsModTable_Object = MibTable
olEnetStatsModTable = _OlEnetStatsModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    olEnetStatsModTable.setStatus("mandatory")
_OlEnetStatsModEntry_Object = MibTableRow
olEnetStatsModEntry = _OlEnetStatsModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1)
)
olEnetStatsModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olEnetStatsModNetID"),
    (0, "CHIPCOMMIB", "olEnetStatsModSlotIndex"),
)
if mibBuilder.loadTexts:
    olEnetStatsModEntry.setStatus("mandatory")


class _OlEnetStatsModNetID_Type(Integer32):
    """Custom type olEnetStatsModNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8))
    )


_OlEnetStatsModNetID_Type.__name__ = "Integer32"
_OlEnetStatsModNetID_Object = MibTableColumn
olEnetStatsModNetID = _OlEnetStatsModNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 1),
    _OlEnetStatsModNetID_Type()
)
olEnetStatsModNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModNetID.setStatus("mandatory")
_OlEnetStatsModSlotIndex_Type = Integer32
_OlEnetStatsModSlotIndex_Object = MibTableColumn
olEnetStatsModSlotIndex = _OlEnetStatsModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 2),
    _OlEnetStatsModSlotIndex_Type()
)
olEnetStatsModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModSlotIndex.setStatus("mandatory")
_OlEnetStatsModFramesRcvdOks_Type = Counter32
_OlEnetStatsModFramesRcvdOks_Object = MibTableColumn
olEnetStatsModFramesRcvdOks = _OlEnetStatsModFramesRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 3),
    _OlEnetStatsModFramesRcvdOks_Type()
)
olEnetStatsModFramesRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModFramesRcvdOks.setStatus("mandatory")
_OlEnetStatsModOctetsRcvdOks_Type = Counter32
_OlEnetStatsModOctetsRcvdOks_Object = MibTableColumn
olEnetStatsModOctetsRcvdOks = _OlEnetStatsModOctetsRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 4),
    _OlEnetStatsModOctetsRcvdOks_Type()
)
olEnetStatsModOctetsRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModOctetsRcvdOks.setStatus("mandatory")
_OlEnetStatsModMcastRcvdOks_Type = Counter32
_OlEnetStatsModMcastRcvdOks_Object = MibTableColumn
olEnetStatsModMcastRcvdOks = _OlEnetStatsModMcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 5),
    _OlEnetStatsModMcastRcvdOks_Type()
)
olEnetStatsModMcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModMcastRcvdOks.setStatus("mandatory")
_OlEnetStatsModBcastRcvdOks_Type = Counter32
_OlEnetStatsModBcastRcvdOks_Object = MibTableColumn
olEnetStatsModBcastRcvdOks = _OlEnetStatsModBcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 6),
    _OlEnetStatsModBcastRcvdOks_Type()
)
olEnetStatsModBcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModBcastRcvdOks.setStatus("mandatory")
_OlEnetStatsModFrameTooLongs_Type = Counter32
_OlEnetStatsModFrameTooLongs_Object = MibTableColumn
olEnetStatsModFrameTooLongs = _OlEnetStatsModFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 7),
    _OlEnetStatsModFrameTooLongs_Type()
)
olEnetStatsModFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModFrameTooLongs.setStatus("mandatory")
_OlEnetStatsModAlignmentErrors_Type = Counter32
_OlEnetStatsModAlignmentErrors_Object = MibTableColumn
olEnetStatsModAlignmentErrors = _OlEnetStatsModAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 8),
    _OlEnetStatsModAlignmentErrors_Type()
)
olEnetStatsModAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModAlignmentErrors.setStatus("mandatory")
_OlEnetStatsModFCSErrors_Type = Counter32
_OlEnetStatsModFCSErrors_Object = MibTableColumn
olEnetStatsModFCSErrors = _OlEnetStatsModFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 9),
    _OlEnetStatsModFCSErrors_Type()
)
olEnetStatsModFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModFCSErrors.setStatus("mandatory")
_OlEnetStatsModRunts_Type = Counter32
_OlEnetStatsModRunts_Object = MibTableColumn
olEnetStatsModRunts = _OlEnetStatsModRunts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 10),
    _OlEnetStatsModRunts_Type()
)
olEnetStatsModRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModRunts.setStatus("mandatory")
_OlEnetStatsPortTable_Object = MibTable
olEnetStatsPortTable = _OlEnetStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    olEnetStatsPortTable.setStatus("mandatory")
_OlEnetStatsPortEntry_Object = MibTableRow
olEnetStatsPortEntry = _OlEnetStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1)
)
olEnetStatsPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olEnetStatsPortSlotIndex"),
    (0, "CHIPCOMMIB", "olEnetStatsPortIndex"),
)
if mibBuilder.loadTexts:
    olEnetStatsPortEntry.setStatus("mandatory")


class _OlEnetStatsPortNetID_Type(Integer32):
    """Custom type olEnetStatsPortNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36))
    )


_OlEnetStatsPortNetID_Type.__name__ = "Integer32"
_OlEnetStatsPortNetID_Object = MibTableColumn
olEnetStatsPortNetID = _OlEnetStatsPortNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 1),
    _OlEnetStatsPortNetID_Type()
)
olEnetStatsPortNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortNetID.setStatus("mandatory")
_OlEnetStatsPortSlotIndex_Type = Integer32
_OlEnetStatsPortSlotIndex_Object = MibTableColumn
olEnetStatsPortSlotIndex = _OlEnetStatsPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 2),
    _OlEnetStatsPortSlotIndex_Type()
)
olEnetStatsPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortSlotIndex.setStatus("mandatory")
_OlEnetStatsPortIndex_Type = Integer32
_OlEnetStatsPortIndex_Object = MibTableColumn
olEnetStatsPortIndex = _OlEnetStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 3),
    _OlEnetStatsPortIndex_Type()
)
olEnetStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortIndex.setStatus("mandatory")
_OlEnetStatsPortFramesRcvdOks_Type = Counter32
_OlEnetStatsPortFramesRcvdOks_Object = MibTableColumn
olEnetStatsPortFramesRcvdOks = _OlEnetStatsPortFramesRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 4),
    _OlEnetStatsPortFramesRcvdOks_Type()
)
olEnetStatsPortFramesRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortFramesRcvdOks.setStatus("mandatory")
_OlEnetStatsPortOctetsRcvdOks_Type = Counter32
_OlEnetStatsPortOctetsRcvdOks_Object = MibTableColumn
olEnetStatsPortOctetsRcvdOks = _OlEnetStatsPortOctetsRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 5),
    _OlEnetStatsPortOctetsRcvdOks_Type()
)
olEnetStatsPortOctetsRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortOctetsRcvdOks.setStatus("mandatory")
_OlEnetStatsPortMcastRcvdOks_Type = Counter32
_OlEnetStatsPortMcastRcvdOks_Object = MibTableColumn
olEnetStatsPortMcastRcvdOks = _OlEnetStatsPortMcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 6),
    _OlEnetStatsPortMcastRcvdOks_Type()
)
olEnetStatsPortMcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortMcastRcvdOks.setStatus("mandatory")
_OlEnetStatsPortBcastRcvdOks_Type = Counter32
_OlEnetStatsPortBcastRcvdOks_Object = MibTableColumn
olEnetStatsPortBcastRcvdOks = _OlEnetStatsPortBcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 7),
    _OlEnetStatsPortBcastRcvdOks_Type()
)
olEnetStatsPortBcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortBcastRcvdOks.setStatus("mandatory")
_OlEnetStatsPortFrameTooLongs_Type = Counter32
_OlEnetStatsPortFrameTooLongs_Object = MibTableColumn
olEnetStatsPortFrameTooLongs = _OlEnetStatsPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 8),
    _OlEnetStatsPortFrameTooLongs_Type()
)
olEnetStatsPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortFrameTooLongs.setStatus("mandatory")
_OlEnetStatsPortAlignmentErrors_Type = Counter32
_OlEnetStatsPortAlignmentErrors_Object = MibTableColumn
olEnetStatsPortAlignmentErrors = _OlEnetStatsPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 9),
    _OlEnetStatsPortAlignmentErrors_Type()
)
olEnetStatsPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortAlignmentErrors.setStatus("mandatory")
_OlEnetStatsPortFCSErrors_Type = Counter32
_OlEnetStatsPortFCSErrors_Object = MibTableColumn
olEnetStatsPortFCSErrors = _OlEnetStatsPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 10),
    _OlEnetStatsPortFCSErrors_Type()
)
olEnetStatsPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortFCSErrors.setStatus("mandatory")
_OlEnetStatsPortRunts_Type = Counter32
_OlEnetStatsPortRunts_Object = MibTableColumn
olEnetStatsPortRunts = _OlEnetStatsPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 11),
    _OlEnetStatsPortRunts_Type()
)
olEnetStatsPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortRunts.setStatus("mandatory")
_OlEnetStatsPortSrcAddrChanges_Type = Counter32
_OlEnetStatsPortSrcAddrChanges_Object = MibTableColumn
olEnetStatsPortSrcAddrChanges = _OlEnetStatsPortSrcAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 12),
    _OlEnetStatsPortSrcAddrChanges_Type()
)
olEnetStatsPortSrcAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortSrcAddrChanges.setStatus("mandatory")


class _OlEnetStatsPortLastSrcAddr_Type(OctetString):
    """Custom type olEnetStatsPortLastSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlEnetStatsPortLastSrcAddr_Type.__name__ = "OctetString"
_OlEnetStatsPortLastSrcAddr_Object = MibTableColumn
olEnetStatsPortLastSrcAddr = _OlEnetStatsPortLastSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 13),
    _OlEnetStatsPortLastSrcAddr_Type()
)
olEnetStatsPortLastSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortLastSrcAddr.setStatus("mandatory")


class _OlEnetStatsPortLastErrAddr_Type(OctetString):
    """Custom type olEnetStatsPortLastErrAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlEnetStatsPortLastErrAddr_Type.__name__ = "OctetString"
_OlEnetStatsPortLastErrAddr_Object = MibTableColumn
olEnetStatsPortLastErrAddr = _OlEnetStatsPortLastErrAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 14),
    _OlEnetStatsPortLastErrAddr_Type()
)
olEnetStatsPortLastErrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortLastErrAddr.setStatus("mandatory")
_OlEnetMapTable_Object = MibTable
olEnetMapTable = _OlEnetMapTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    olEnetMapTable.setStatus("mandatory")
_OlEnetMapEntry_Object = MibTableRow
olEnetMapEntry = _OlEnetMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1)
)
olEnetMapEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olEnetMapNetID"),
    (0, "CHIPCOMMIB", "olEnetMapAddress"),
)
if mibBuilder.loadTexts:
    olEnetMapEntry.setStatus("mandatory")


class _OlEnetMapNetID_Type(Integer32):
    """Custom type olEnetMapNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36))
    )


_OlEnetMapNetID_Type.__name__ = "Integer32"
_OlEnetMapNetID_Object = MibTableColumn
olEnetMapNetID = _OlEnetMapNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 1),
    _OlEnetMapNetID_Type()
)
olEnetMapNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapNetID.setStatus("mandatory")


class _OlEnetMapAddress_Type(OctetString):
    """Custom type olEnetMapAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlEnetMapAddress_Type.__name__ = "OctetString"
_OlEnetMapAddress_Object = MibTableColumn
olEnetMapAddress = _OlEnetMapAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 2),
    _OlEnetMapAddress_Type()
)
olEnetMapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapAddress.setStatus("mandatory")
_OlEnetMapSlotIndex_Type = Integer32
_OlEnetMapSlotIndex_Object = MibTableColumn
olEnetMapSlotIndex = _OlEnetMapSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 3),
    _OlEnetMapSlotIndex_Type()
)
olEnetMapSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapSlotIndex.setStatus("mandatory")
_OlEnetMapPortIndex_Type = Integer32
_OlEnetMapPortIndex_Object = MibTableColumn
olEnetMapPortIndex = _OlEnetMapPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 4),
    _OlEnetMapPortIndex_Type()
)
olEnetMapPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapPortIndex.setStatus("mandatory")
_OlEnetMapFrames_Type = Counter32
_OlEnetMapFrames_Object = MibTableColumn
olEnetMapFrames = _OlEnetMapFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 5),
    _OlEnetMapFrames_Type()
)
olEnetMapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapFrames.setStatus("mandatory")
_OlEnetMapOctets_Type = Counter32
_OlEnetMapOctets_Object = MibTableColumn
olEnetMapOctets = _OlEnetMapOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 6),
    _OlEnetMapOctets_Type()
)
olEnetMapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapOctets.setStatus("mandatory")
_OlEnetMapTime_Type = TimeTicks
_OlEnetMapTime_Object = MibTableColumn
olEnetMapTime = _OlEnetMapTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 7),
    _OlEnetMapTime_Type()
)
olEnetMapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapTime.setStatus("mandatory")
_ChipSnmpDot3RptrMgt_ObjectIdentity = ObjectIdentity
chipSnmpDot3RptrMgt = _ChipSnmpDot3RptrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5)
)
_ChipRptrBasicPackage_ObjectIdentity = ObjectIdentity
chipRptrBasicPackage = _ChipRptrBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1)
)
_ChipRptrRptrInfo_ObjectIdentity = ObjectIdentity
chipRptrRptrInfo = _ChipRptrRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1)
)
_ChipRptrRptrInfoTable_Object = MibTable
chipRptrRptrInfoTable = _ChipRptrRptrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    chipRptrRptrInfoTable.setStatus("mandatory")
_ChipRptrRptrInfoEntry_Object = MibTableRow
chipRptrRptrInfoEntry = _ChipRptrRptrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1, 1, 1)
)
chipRptrRptrInfoEntry.setIndexNames(
    (0, "CHIPCOMMIB", "chipRptrRptrInfoSlotIndex"),
    (0, "CHIPCOMMIB", "chipRptrRptrInfoNetID"),
)
if mibBuilder.loadTexts:
    chipRptrRptrInfoEntry.setStatus("mandatory")


class _ChipRptrRptrInfoSlotIndex_Type(Integer32):
    """Custom type chipRptrRptrInfoSlotIndex based on Integer32"""
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
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_ChipRptrRptrInfoSlotIndex_Type.__name__ = "Integer32"
_ChipRptrRptrInfoSlotIndex_Object = MibTableColumn
chipRptrRptrInfoSlotIndex = _ChipRptrRptrInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1, 1, 1, 1),
    _ChipRptrRptrInfoSlotIndex_Type()
)
chipRptrRptrInfoSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrRptrInfoSlotIndex.setStatus("mandatory")


class _ChipRptrRptrInfoNetID_Type(Integer32):
    """Custom type chipRptrRptrInfoNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36))
    )


_ChipRptrRptrInfoNetID_Type.__name__ = "Integer32"
_ChipRptrRptrInfoNetID_Object = MibTableColumn
chipRptrRptrInfoNetID = _ChipRptrRptrInfoNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1, 1, 1, 2),
    _ChipRptrRptrInfoNetID_Type()
)
chipRptrRptrInfoNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrRptrInfoNetID.setStatus("mandatory")


class _ChipRptrGroupCapacity_Type(Integer32):
    """Custom type chipRptrGroupCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChipRptrGroupCapacity_Type.__name__ = "Integer32"
_ChipRptrGroupCapacity_Object = MibTableColumn
chipRptrGroupCapacity = _ChipRptrGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1, 1, 1, 3),
    _ChipRptrGroupCapacity_Type()
)
chipRptrGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrGroupCapacity.setStatus("mandatory")


class _ChipRptrOperStatus_Type(Integer32):
    """Custom type chipRptrOperStatus based on Integer32"""
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
        *(("generalFailure", 6),
          ("groupFailure", 4),
          ("ok", 2),
          ("other", 1),
          ("portFailure", 5),
          ("rptrFailure", 3))
    )


_ChipRptrOperStatus_Type.__name__ = "Integer32"
_ChipRptrOperStatus_Object = MibTableColumn
chipRptrOperStatus = _ChipRptrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1, 1, 1, 4),
    _ChipRptrOperStatus_Type()
)
chipRptrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrOperStatus.setStatus("mandatory")


class _ChipRptrHealthText_Type(DisplayString):
    """Custom type chipRptrHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChipRptrHealthText_Type.__name__ = "DisplayString"
_ChipRptrHealthText_Object = MibTableColumn
chipRptrHealthText = _ChipRptrHealthText_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1, 1, 1, 5),
    _ChipRptrHealthText_Type()
)
chipRptrHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrHealthText.setStatus("mandatory")


class _ChipRptrReset_Type(Integer32):
    """Custom type chipRptrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_ChipRptrReset_Type.__name__ = "Integer32"
_ChipRptrReset_Object = MibTableColumn
chipRptrReset = _ChipRptrReset_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1, 1, 1, 6),
    _ChipRptrReset_Type()
)
chipRptrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipRptrReset.setStatus("mandatory")


class _ChipRptrNonDisruptTest_Type(Integer32):
    """Custom type chipRptrNonDisruptTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest", 1),
          ("selfTest", 2))
    )


_ChipRptrNonDisruptTest_Type.__name__ = "Integer32"
_ChipRptrNonDisruptTest_Object = MibTableColumn
chipRptrNonDisruptTest = _ChipRptrNonDisruptTest_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1, 1, 1, 7),
    _ChipRptrNonDisruptTest_Type()
)
chipRptrNonDisruptTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipRptrNonDisruptTest.setStatus("mandatory")
_ChipRptrTotalPartitionedPorts_Type = Gauge32
_ChipRptrTotalPartitionedPorts_Object = MibTableColumn
chipRptrTotalPartitionedPorts = _ChipRptrTotalPartitionedPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 1, 1, 1, 8),
    _ChipRptrTotalPartitionedPorts_Type()
)
chipRptrTotalPartitionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrTotalPartitionedPorts.setStatus("mandatory")
_ChipRptrGroupInfo_ObjectIdentity = ObjectIdentity
chipRptrGroupInfo = _ChipRptrGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2)
)
_ChipRptrGroupTable_Object = MibTable
chipRptrGroupTable = _ChipRptrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chipRptrGroupTable.setStatus("mandatory")
_ChipRptrGroupEntry_Object = MibTableRow
chipRptrGroupEntry = _ChipRptrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2, 1, 1)
)
chipRptrGroupEntry.setIndexNames(
    (0, "CHIPCOMMIB", "chipRptrGroupSlotIndex"),
    (0, "CHIPCOMMIB", "chipRptrGroupNetID"),
    (0, "CHIPCOMMIB", "chipRptrGroupIndex"),
)
if mibBuilder.loadTexts:
    chipRptrGroupEntry.setStatus("mandatory")


class _ChipRptrGroupSlotIndex_Type(Integer32):
    """Custom type chipRptrGroupSlotIndex based on Integer32"""
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
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_ChipRptrGroupSlotIndex_Type.__name__ = "Integer32"
_ChipRptrGroupSlotIndex_Object = MibTableColumn
chipRptrGroupSlotIndex = _ChipRptrGroupSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2, 1, 1, 1),
    _ChipRptrGroupSlotIndex_Type()
)
chipRptrGroupSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrGroupSlotIndex.setStatus("mandatory")


class _ChipRptrGroupNetID_Type(Integer32):
    """Custom type chipRptrGroupNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36))
    )


_ChipRptrGroupNetID_Type.__name__ = "Integer32"
_ChipRptrGroupNetID_Object = MibTableColumn
chipRptrGroupNetID = _ChipRptrGroupNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2, 1, 1, 2),
    _ChipRptrGroupNetID_Type()
)
chipRptrGroupNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrGroupNetID.setStatus("mandatory")


class _ChipRptrGroupIndex_Type(Integer32):
    """Custom type chipRptrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChipRptrGroupIndex_Type.__name__ = "Integer32"
_ChipRptrGroupIndex_Object = MibTableColumn
chipRptrGroupIndex = _ChipRptrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2, 1, 1, 3),
    _ChipRptrGroupIndex_Type()
)
chipRptrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrGroupIndex.setStatus("mandatory")


class _ChipRptrGroupDescr_Type(DisplayString):
    """Custom type chipRptrGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChipRptrGroupDescr_Type.__name__ = "DisplayString"
_ChipRptrGroupDescr_Object = MibTableColumn
chipRptrGroupDescr = _ChipRptrGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2, 1, 1, 4),
    _ChipRptrGroupDescr_Type()
)
chipRptrGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrGroupDescr.setStatus("mandatory")
_ChipRptrGroupObjectID_Type = ObjectIdentifier
_ChipRptrGroupObjectID_Object = MibTableColumn
chipRptrGroupObjectID = _ChipRptrGroupObjectID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2, 1, 1, 5),
    _ChipRptrGroupObjectID_Type()
)
chipRptrGroupObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrGroupObjectID.setStatus("mandatory")


class _ChipRptrGroupOperStatus_Type(Integer32):
    """Custom type chipRptrGroupOperStatus based on Integer32"""
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
        *(("malfunctioning", 3),
          ("notPresent", 4),
          ("operational", 2),
          ("other", 1),
          ("resetInProgress", 6),
          ("underTest", 5))
    )


_ChipRptrGroupOperStatus_Type.__name__ = "Integer32"
_ChipRptrGroupOperStatus_Object = MibTableColumn
chipRptrGroupOperStatus = _ChipRptrGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2, 1, 1, 6),
    _ChipRptrGroupOperStatus_Type()
)
chipRptrGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrGroupOperStatus.setStatus("mandatory")
_ChipRptrGroupLastOperStatusChange_Type = TimeTicks
_ChipRptrGroupLastOperStatusChange_Object = MibTableColumn
chipRptrGroupLastOperStatusChange = _ChipRptrGroupLastOperStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2, 1, 1, 7),
    _ChipRptrGroupLastOperStatusChange_Type()
)
chipRptrGroupLastOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrGroupLastOperStatusChange.setStatus("mandatory")


class _ChipRptrGroupPortCapacity_Type(Integer32):
    """Custom type chipRptrGroupPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChipRptrGroupPortCapacity_Type.__name__ = "Integer32"
_ChipRptrGroupPortCapacity_Object = MibTableColumn
chipRptrGroupPortCapacity = _ChipRptrGroupPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 2, 1, 1, 8),
    _ChipRptrGroupPortCapacity_Type()
)
chipRptrGroupPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrGroupPortCapacity.setStatus("mandatory")
_ChipRptrPortInfo_ObjectIdentity = ObjectIdentity
chipRptrPortInfo = _ChipRptrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 3)
)
_ChipRptrPortTable_Object = MibTable
chipRptrPortTable = _ChipRptrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    chipRptrPortTable.setStatus("mandatory")
_ChipRptrPortEntry_Object = MibTableRow
chipRptrPortEntry = _ChipRptrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 3, 1, 1)
)
chipRptrPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "chipRptrPortSlotIndex"),
    (0, "CHIPCOMMIB", "chipRptrPortNetID"),
    (0, "CHIPCOMMIB", "chipRptrPortGroupIndex"),
    (0, "CHIPCOMMIB", "chipRptrPortIndex"),
)
if mibBuilder.loadTexts:
    chipRptrPortEntry.setStatus("mandatory")


class _ChipRptrPortSlotIndex_Type(Integer32):
    """Custom type chipRptrPortSlotIndex based on Integer32"""
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
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_ChipRptrPortSlotIndex_Type.__name__ = "Integer32"
_ChipRptrPortSlotIndex_Object = MibTableColumn
chipRptrPortSlotIndex = _ChipRptrPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 3, 1, 1, 1),
    _ChipRptrPortSlotIndex_Type()
)
chipRptrPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrPortSlotIndex.setStatus("mandatory")


class _ChipRptrPortNetID_Type(Integer32):
    """Custom type chipRptrPortNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36))
    )


_ChipRptrPortNetID_Type.__name__ = "Integer32"
_ChipRptrPortNetID_Object = MibTableColumn
chipRptrPortNetID = _ChipRptrPortNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 3, 1, 1, 2),
    _ChipRptrPortNetID_Type()
)
chipRptrPortNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrPortNetID.setStatus("mandatory")


class _ChipRptrPortGroupIndex_Type(Integer32):
    """Custom type chipRptrPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChipRptrPortGroupIndex_Type.__name__ = "Integer32"
_ChipRptrPortGroupIndex_Object = MibTableColumn
chipRptrPortGroupIndex = _ChipRptrPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 3, 1, 1, 3),
    _ChipRptrPortGroupIndex_Type()
)
chipRptrPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrPortGroupIndex.setStatus("mandatory")


class _ChipRptrPortIndex_Type(Integer32):
    """Custom type chipRptrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChipRptrPortIndex_Type.__name__ = "Integer32"
_ChipRptrPortIndex_Object = MibTableColumn
chipRptrPortIndex = _ChipRptrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 3, 1, 1, 4),
    _ChipRptrPortIndex_Type()
)
chipRptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrPortIndex.setStatus("mandatory")


class _ChipRptrPortAdminStatus_Type(Integer32):
    """Custom type chipRptrPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ChipRptrPortAdminStatus_Type.__name__ = "Integer32"
_ChipRptrPortAdminStatus_Object = MibTableColumn
chipRptrPortAdminStatus = _ChipRptrPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 3, 1, 1, 5),
    _ChipRptrPortAdminStatus_Type()
)
chipRptrPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipRptrPortAdminStatus.setStatus("mandatory")


class _ChipRptrPortAutoPartitionState_Type(Integer32):
    """Custom type chipRptrPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 2),
          ("notAutoPartitioned", 1))
    )


_ChipRptrPortAutoPartitionState_Type.__name__ = "Integer32"
_ChipRptrPortAutoPartitionState_Object = MibTableColumn
chipRptrPortAutoPartitionState = _ChipRptrPortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 3, 1, 1, 6),
    _ChipRptrPortAutoPartitionState_Type()
)
chipRptrPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrPortAutoPartitionState.setStatus("mandatory")


class _ChipRptrPortOperStatus_Type(Integer32):
    """Custom type chipRptrPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notPresent", 3),
          ("operational", 1))
    )


_ChipRptrPortOperStatus_Type.__name__ = "Integer32"
_ChipRptrPortOperStatus_Object = MibTableColumn
chipRptrPortOperStatus = _ChipRptrPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 1, 3, 1, 1, 7),
    _ChipRptrPortOperStatus_Type()
)
chipRptrPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrPortOperStatus.setStatus("mandatory")
_ChipRptrMonitorPackage_ObjectIdentity = ObjectIdentity
chipRptrMonitorPackage = _ChipRptrMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2)
)
_ChipRptrMonitorRptrInfo_ObjectIdentity = ObjectIdentity
chipRptrMonitorRptrInfo = _ChipRptrMonitorRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 1)
)
_ChipRptrMonitorRptrTable_Object = MibTable
chipRptrMonitorRptrTable = _ChipRptrMonitorRptrTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    chipRptrMonitorRptrTable.setStatus("mandatory")
_ChipRptrMonitorRptrEntry_Object = MibTableRow
chipRptrMonitorRptrEntry = _ChipRptrMonitorRptrEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 1, 1, 1)
)
chipRptrMonitorRptrEntry.setIndexNames(
    (0, "CHIPCOMMIB", "chipRptrMonitorSlotIndex"),
    (0, "CHIPCOMMIB", "chipRptrMonitorNetID"),
)
if mibBuilder.loadTexts:
    chipRptrMonitorRptrEntry.setStatus("mandatory")


class _ChipRptrMonitorSlotIndex_Type(Integer32):
    """Custom type chipRptrMonitorSlotIndex based on Integer32"""
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
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_ChipRptrMonitorSlotIndex_Type.__name__ = "Integer32"
_ChipRptrMonitorSlotIndex_Object = MibTableColumn
chipRptrMonitorSlotIndex = _ChipRptrMonitorSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 1, 1, 1, 1),
    _ChipRptrMonitorSlotIndex_Type()
)
chipRptrMonitorSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorSlotIndex.setStatus("mandatory")


class _ChipRptrMonitorNetID_Type(Integer32):
    """Custom type chipRptrMonitorNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36))
    )


_ChipRptrMonitorNetID_Type.__name__ = "Integer32"
_ChipRptrMonitorNetID_Object = MibTableColumn
chipRptrMonitorNetID = _ChipRptrMonitorNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 1, 1, 1, 2),
    _ChipRptrMonitorNetID_Type()
)
chipRptrMonitorNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorNetID.setStatus("mandatory")
_ChipRptrMonitorTransmitCollisions_Type = Counter32
_ChipRptrMonitorTransmitCollisions_Object = MibTableColumn
chipRptrMonitorTransmitCollisions = _ChipRptrMonitorTransmitCollisions_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 1, 1, 1, 3),
    _ChipRptrMonitorTransmitCollisions_Type()
)
chipRptrMonitorTransmitCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorTransmitCollisions.setStatus("mandatory")
_ChipRptrMonitorGroupInfo_ObjectIdentity = ObjectIdentity
chipRptrMonitorGroupInfo = _ChipRptrMonitorGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 2)
)
_ChipRptrMonitorGroupTable_Object = MibTable
chipRptrMonitorGroupTable = _ChipRptrMonitorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    chipRptrMonitorGroupTable.setStatus("mandatory")
_ChipRptrMonitorGroupEntry_Object = MibTableRow
chipRptrMonitorGroupEntry = _ChipRptrMonitorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 2, 1, 1)
)
chipRptrMonitorGroupEntry.setIndexNames(
    (0, "CHIPCOMMIB", "chipRptrMonitorGroupSlotIndex"),
    (0, "CHIPCOMMIB", "chipRptrMonitorGroupNetID"),
    (0, "CHIPCOMMIB", "chipRptrMonitorGroupIndex"),
)
if mibBuilder.loadTexts:
    chipRptrMonitorGroupEntry.setStatus("mandatory")


class _ChipRptrMonitorGroupSlotIndex_Type(Integer32):
    """Custom type chipRptrMonitorGroupSlotIndex based on Integer32"""
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
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_ChipRptrMonitorGroupSlotIndex_Type.__name__ = "Integer32"
_ChipRptrMonitorGroupSlotIndex_Object = MibTableColumn
chipRptrMonitorGroupSlotIndex = _ChipRptrMonitorGroupSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 2, 1, 1, 1),
    _ChipRptrMonitorGroupSlotIndex_Type()
)
chipRptrMonitorGroupSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorGroupSlotIndex.setStatus("mandatory")


class _ChipRptrMonitorGroupNetID_Type(Integer32):
    """Custom type chipRptrMonitorGroupNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36))
    )


_ChipRptrMonitorGroupNetID_Type.__name__ = "Integer32"
_ChipRptrMonitorGroupNetID_Object = MibTableColumn
chipRptrMonitorGroupNetID = _ChipRptrMonitorGroupNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 2, 1, 1, 2),
    _ChipRptrMonitorGroupNetID_Type()
)
chipRptrMonitorGroupNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorGroupNetID.setStatus("mandatory")


class _ChipRptrMonitorGroupIndex_Type(Integer32):
    """Custom type chipRptrMonitorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChipRptrMonitorGroupIndex_Type.__name__ = "Integer32"
_ChipRptrMonitorGroupIndex_Object = MibTableColumn
chipRptrMonitorGroupIndex = _ChipRptrMonitorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 2, 1, 1, 3),
    _ChipRptrMonitorGroupIndex_Type()
)
chipRptrMonitorGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorGroupIndex.setStatus("mandatory")
_ChipRptrMonitorGroupTotalFrames_Type = Counter32
_ChipRptrMonitorGroupTotalFrames_Object = MibTableColumn
chipRptrMonitorGroupTotalFrames = _ChipRptrMonitorGroupTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 2, 1, 1, 4),
    _ChipRptrMonitorGroupTotalFrames_Type()
)
chipRptrMonitorGroupTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorGroupTotalFrames.setStatus("mandatory")
_ChipRptrMonitorGroupTotalOctets_Type = Counter32
_ChipRptrMonitorGroupTotalOctets_Object = MibTableColumn
chipRptrMonitorGroupTotalOctets = _ChipRptrMonitorGroupTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 2, 1, 1, 5),
    _ChipRptrMonitorGroupTotalOctets_Type()
)
chipRptrMonitorGroupTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorGroupTotalOctets.setStatus("mandatory")
_ChipRptrMonitorGroupTotalErrors_Type = Counter32
_ChipRptrMonitorGroupTotalErrors_Object = MibTableColumn
chipRptrMonitorGroupTotalErrors = _ChipRptrMonitorGroupTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 2, 1, 1, 6),
    _ChipRptrMonitorGroupTotalErrors_Type()
)
chipRptrMonitorGroupTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorGroupTotalErrors.setStatus("mandatory")
_ChipRptrMonitorPortInfo_ObjectIdentity = ObjectIdentity
chipRptrMonitorPortInfo = _ChipRptrMonitorPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3)
)
_ChipRptrMonitorPortTable_Object = MibTable
chipRptrMonitorPortTable = _ChipRptrMonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    chipRptrMonitorPortTable.setStatus("mandatory")
_ChipRptrMonitorPortEntry_Object = MibTableRow
chipRptrMonitorPortEntry = _ChipRptrMonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1)
)
chipRptrMonitorPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "chipRptrMonitorPortSlotIndex"),
    (0, "CHIPCOMMIB", "chipRptrMonitorPortNetID"),
    (0, "CHIPCOMMIB", "chipRptrMonitorPortGroupIndex"),
    (0, "CHIPCOMMIB", "chipRptrMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    chipRptrMonitorPortEntry.setStatus("mandatory")


class _ChipRptrMonitorPortSlotIndex_Type(Integer32):
    """Custom type chipRptrMonitorPortSlotIndex based on Integer32"""
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
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_ChipRptrMonitorPortSlotIndex_Type.__name__ = "Integer32"
_ChipRptrMonitorPortSlotIndex_Object = MibTableColumn
chipRptrMonitorPortSlotIndex = _ChipRptrMonitorPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 1),
    _ChipRptrMonitorPortSlotIndex_Type()
)
chipRptrMonitorPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortSlotIndex.setStatus("mandatory")


class _ChipRptrMonitorPortNetID_Type(Integer32):
    """Custom type chipRptrMonitorPortNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36))
    )


_ChipRptrMonitorPortNetID_Type.__name__ = "Integer32"
_ChipRptrMonitorPortNetID_Object = MibTableColumn
chipRptrMonitorPortNetID = _ChipRptrMonitorPortNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 2),
    _ChipRptrMonitorPortNetID_Type()
)
chipRptrMonitorPortNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortNetID.setStatus("mandatory")


class _ChipRptrMonitorPortGroupIndex_Type(Integer32):
    """Custom type chipRptrMonitorPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChipRptrMonitorPortGroupIndex_Type.__name__ = "Integer32"
_ChipRptrMonitorPortGroupIndex_Object = MibTableColumn
chipRptrMonitorPortGroupIndex = _ChipRptrMonitorPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 3),
    _ChipRptrMonitorPortGroupIndex_Type()
)
chipRptrMonitorPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortGroupIndex.setStatus("mandatory")


class _ChipRptrMonitorPortIndex_Type(Integer32):
    """Custom type chipRptrMonitorPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChipRptrMonitorPortIndex_Type.__name__ = "Integer32"
_ChipRptrMonitorPortIndex_Object = MibTableColumn
chipRptrMonitorPortIndex = _ChipRptrMonitorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 4),
    _ChipRptrMonitorPortIndex_Type()
)
chipRptrMonitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortIndex.setStatus("mandatory")
_ChipRptrMonitorPortReadableFrames_Type = Counter32
_ChipRptrMonitorPortReadableFrames_Object = MibTableColumn
chipRptrMonitorPortReadableFrames = _ChipRptrMonitorPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 5),
    _ChipRptrMonitorPortReadableFrames_Type()
)
chipRptrMonitorPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortReadableFrames.setStatus("mandatory")
_ChipRptrMonitorPortReadableOctets_Type = Counter32
_ChipRptrMonitorPortReadableOctets_Object = MibTableColumn
chipRptrMonitorPortReadableOctets = _ChipRptrMonitorPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 6),
    _ChipRptrMonitorPortReadableOctets_Type()
)
chipRptrMonitorPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortReadableOctets.setStatus("mandatory")
_ChipRptrMonitorPortFCSErrors_Type = Counter32
_ChipRptrMonitorPortFCSErrors_Object = MibTableColumn
chipRptrMonitorPortFCSErrors = _ChipRptrMonitorPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 7),
    _ChipRptrMonitorPortFCSErrors_Type()
)
chipRptrMonitorPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortFCSErrors.setStatus("mandatory")
_ChipRptrMonitorPortAlignmentErrors_Type = Counter32
_ChipRptrMonitorPortAlignmentErrors_Object = MibTableColumn
chipRptrMonitorPortAlignmentErrors = _ChipRptrMonitorPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 8),
    _ChipRptrMonitorPortAlignmentErrors_Type()
)
chipRptrMonitorPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortAlignmentErrors.setStatus("mandatory")
_ChipRptrMonitorPortFrameTooLongs_Type = Counter32
_ChipRptrMonitorPortFrameTooLongs_Object = MibTableColumn
chipRptrMonitorPortFrameTooLongs = _ChipRptrMonitorPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 9),
    _ChipRptrMonitorPortFrameTooLongs_Type()
)
chipRptrMonitorPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortFrameTooLongs.setStatus("mandatory")
_ChipRptrMonitorPortShortEvents_Type = Counter32
_ChipRptrMonitorPortShortEvents_Object = MibTableColumn
chipRptrMonitorPortShortEvents = _ChipRptrMonitorPortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 10),
    _ChipRptrMonitorPortShortEvents_Type()
)
chipRptrMonitorPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortShortEvents.setStatus("mandatory")
_ChipRptrMonitorPortRunts_Type = Counter32
_ChipRptrMonitorPortRunts_Object = MibTableColumn
chipRptrMonitorPortRunts = _ChipRptrMonitorPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 11),
    _ChipRptrMonitorPortRunts_Type()
)
chipRptrMonitorPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortRunts.setStatus("mandatory")
_ChipRptrMonitorPortCollisions_Type = Counter32
_ChipRptrMonitorPortCollisions_Object = MibTableColumn
chipRptrMonitorPortCollisions = _ChipRptrMonitorPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 12),
    _ChipRptrMonitorPortCollisions_Type()
)
chipRptrMonitorPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortCollisions.setStatus("mandatory")
_ChipRptrMonitorPortLateEvents_Type = Counter32
_ChipRptrMonitorPortLateEvents_Object = MibTableColumn
chipRptrMonitorPortLateEvents = _ChipRptrMonitorPortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 13),
    _ChipRptrMonitorPortLateEvents_Type()
)
chipRptrMonitorPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortLateEvents.setStatus("mandatory")
_ChipRptrMonitorPortVeryLongEvents_Type = Counter32
_ChipRptrMonitorPortVeryLongEvents_Object = MibTableColumn
chipRptrMonitorPortVeryLongEvents = _ChipRptrMonitorPortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 14),
    _ChipRptrMonitorPortVeryLongEvents_Type()
)
chipRptrMonitorPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortVeryLongEvents.setStatus("mandatory")
_ChipRptrMonitorPortDataRateMismatches_Type = Counter32
_ChipRptrMonitorPortDataRateMismatches_Object = MibTableColumn
chipRptrMonitorPortDataRateMismatches = _ChipRptrMonitorPortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 15),
    _ChipRptrMonitorPortDataRateMismatches_Type()
)
chipRptrMonitorPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortDataRateMismatches.setStatus("mandatory")
_ChipRptrMonitorPortAutoPartitions_Type = Counter32
_ChipRptrMonitorPortAutoPartitions_Object = MibTableColumn
chipRptrMonitorPortAutoPartitions = _ChipRptrMonitorPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 16),
    _ChipRptrMonitorPortAutoPartitions_Type()
)
chipRptrMonitorPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortAutoPartitions.setStatus("mandatory")
_ChipRptrMonitorPortTotalErrors_Type = Counter32
_ChipRptrMonitorPortTotalErrors_Object = MibTableColumn
chipRptrMonitorPortTotalErrors = _ChipRptrMonitorPortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 2, 3, 1, 1, 17),
    _ChipRptrMonitorPortTotalErrors_Type()
)
chipRptrMonitorPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrMonitorPortTotalErrors.setStatus("mandatory")
_ChipRptrAddrTrackPackage_ObjectIdentity = ObjectIdentity
chipRptrAddrTrackPackage = _ChipRptrAddrTrackPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3)
)
_ChipRptrAddrTrackRptrInfo_ObjectIdentity = ObjectIdentity
chipRptrAddrTrackRptrInfo = _ChipRptrAddrTrackRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 1)
)
_ChipRptrAddrTrackGroupInfo_ObjectIdentity = ObjectIdentity
chipRptrAddrTrackGroupInfo = _ChipRptrAddrTrackGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 2)
)
_ChipRptrAddrTrackPortInfo_ObjectIdentity = ObjectIdentity
chipRptrAddrTrackPortInfo = _ChipRptrAddrTrackPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 3)
)
_ChipRptrAddrTrackTable_Object = MibTable
chipRptrAddrTrackTable = _ChipRptrAddrTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 3, 1)
)
if mibBuilder.loadTexts:
    chipRptrAddrTrackTable.setStatus("mandatory")
_ChipRptrAddrTrackEntry_Object = MibTableRow
chipRptrAddrTrackEntry = _ChipRptrAddrTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 3, 1, 1)
)
chipRptrAddrTrackEntry.setIndexNames(
    (0, "CHIPCOMMIB", "chipRptrAddrTrackSlotIndex"),
    (0, "CHIPCOMMIB", "chipRptrAddrTrackGroupNetID"),
    (0, "CHIPCOMMIB", "chipRptrAddrTrackGroupIndex"),
    (0, "CHIPCOMMIB", "chipRptrAddrTrackPortIndex"),
)
if mibBuilder.loadTexts:
    chipRptrAddrTrackEntry.setStatus("mandatory")


class _ChipRptrAddrTrackSlotIndex_Type(Integer32):
    """Custom type chipRptrAddrTrackSlotIndex based on Integer32"""
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
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_ChipRptrAddrTrackSlotIndex_Type.__name__ = "Integer32"
_ChipRptrAddrTrackSlotIndex_Object = MibTableColumn
chipRptrAddrTrackSlotIndex = _ChipRptrAddrTrackSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 3, 1, 1, 1),
    _ChipRptrAddrTrackSlotIndex_Type()
)
chipRptrAddrTrackSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrAddrTrackSlotIndex.setStatus("mandatory")


class _ChipRptrAddrTrackGroupNetID_Type(Integer32):
    """Custom type chipRptrAddrTrackGroupNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("ethernet-4", 32),
          ("ethernet-5", 33),
          ("ethernet-6", 34),
          ("ethernet-7", 35),
          ("ethernet-8", 36))
    )


_ChipRptrAddrTrackGroupNetID_Type.__name__ = "Integer32"
_ChipRptrAddrTrackGroupNetID_Object = MibTableColumn
chipRptrAddrTrackGroupNetID = _ChipRptrAddrTrackGroupNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 3, 1, 1, 2),
    _ChipRptrAddrTrackGroupNetID_Type()
)
chipRptrAddrTrackGroupNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrAddrTrackGroupNetID.setStatus("mandatory")


class _ChipRptrAddrTrackGroupIndex_Type(Integer32):
    """Custom type chipRptrAddrTrackGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChipRptrAddrTrackGroupIndex_Type.__name__ = "Integer32"
_ChipRptrAddrTrackGroupIndex_Object = MibTableColumn
chipRptrAddrTrackGroupIndex = _ChipRptrAddrTrackGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 3, 1, 1, 3),
    _ChipRptrAddrTrackGroupIndex_Type()
)
chipRptrAddrTrackGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrAddrTrackGroupIndex.setStatus("mandatory")


class _ChipRptrAddrTrackPortIndex_Type(Integer32):
    """Custom type chipRptrAddrTrackPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChipRptrAddrTrackPortIndex_Type.__name__ = "Integer32"
_ChipRptrAddrTrackPortIndex_Object = MibTableColumn
chipRptrAddrTrackPortIndex = _ChipRptrAddrTrackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 3, 1, 1, 4),
    _ChipRptrAddrTrackPortIndex_Type()
)
chipRptrAddrTrackPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrAddrTrackPortIndex.setStatus("mandatory")
_ChipRptrAddrTrackLastSourceAddress_Type = MacAddress
_ChipRptrAddrTrackLastSourceAddress_Object = MibTableColumn
chipRptrAddrTrackLastSourceAddress = _ChipRptrAddrTrackLastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 3, 1, 1, 5),
    _ChipRptrAddrTrackLastSourceAddress_Type()
)
chipRptrAddrTrackLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrAddrTrackLastSourceAddress.setStatus("mandatory")
_ChipRptrAddrTrackSourceAddrChanges_Type = Counter32
_ChipRptrAddrTrackSourceAddrChanges_Object = MibTableColumn
chipRptrAddrTrackSourceAddrChanges = _ChipRptrAddrTrackSourceAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 3, 1, 1, 6),
    _ChipRptrAddrTrackSourceAddrChanges_Type()
)
chipRptrAddrTrackSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrAddrTrackSourceAddrChanges.setStatus("mandatory")


class _ChipRptrAddrTrackNewLastSrcAddress_Type(OctetString):
    """Custom type chipRptrAddrTrackNewLastSrcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_ChipRptrAddrTrackNewLastSrcAddress_Type.__name__ = "OctetString"
_ChipRptrAddrTrackNewLastSrcAddress_Object = MibTableColumn
chipRptrAddrTrackNewLastSrcAddress = _ChipRptrAddrTrackNewLastSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 5, 3, 3, 1, 1, 7),
    _ChipRptrAddrTrackNewLastSrcAddress_Type()
)
chipRptrAddrTrackNewLastSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRptrAddrTrackNewLastSrcAddress.setStatus("mandatory")
_OlTRnet_ObjectIdentity = ObjectIdentity
olTRnet = _OlTRnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3)
)


class _OlTRnetMapState_Type(Integer32):
    """Custom type olTRnetMapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changing", 1),
          ("notChanging", 2))
    )


_OlTRnetMapState_Type.__name__ = "Integer32"
_OlTRnetMapState_Object = MibScalar
olTRnetMapState = _OlTRnetMapState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 1),
    _OlTRnetMapState_Type()
)
olTRnetMapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetMapState.setStatus("mandatory")
_OlTRnetStatsTable_Object = MibTable
olTRnetStatsTable = _OlTRnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    olTRnetStatsTable.setStatus("mandatory")
_OlTRnetStatsEntry_Object = MibTableRow
olTRnetStatsEntry = _OlTRnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1)
)
olTRnetStatsEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTRnetStatsNetID"),
)
if mibBuilder.loadTexts:
    olTRnetStatsEntry.setStatus("mandatory")


class _OlTRnetStatsNetID_Type(Integer32):
    """Custom type olTRnetStatsNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRnetStatsNetID_Type.__name__ = "Integer32"
_OlTRnetStatsNetID_Object = MibTableColumn
olTRnetStatsNetID = _OlTRnetStatsNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 1),
    _OlTRnetStatsNetID_Type()
)
olTRnetStatsNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsNetID.setStatus("mandatory")
_OlTRnetStatsLineErrors_Type = Counter32
_OlTRnetStatsLineErrors_Object = MibTableColumn
olTRnetStatsLineErrors = _OlTRnetStatsLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 2),
    _OlTRnetStatsLineErrors_Type()
)
olTRnetStatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLineErrors.setStatus("mandatory")
_OlTRnetStatsBurstErrors_Type = Counter32
_OlTRnetStatsBurstErrors_Object = MibTableColumn
olTRnetStatsBurstErrors = _OlTRnetStatsBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 3),
    _OlTRnetStatsBurstErrors_Type()
)
olTRnetStatsBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsBurstErrors.setStatus("mandatory")
_OlTRnetStatsACErrors_Type = Counter32
_OlTRnetStatsACErrors_Object = MibTableColumn
olTRnetStatsACErrors = _OlTRnetStatsACErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 4),
    _OlTRnetStatsACErrors_Type()
)
olTRnetStatsACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsACErrors.setStatus("mandatory")
_OlTRnetStatsLostFrameErrors_Type = Counter32
_OlTRnetStatsLostFrameErrors_Object = MibTableColumn
olTRnetStatsLostFrameErrors = _OlTRnetStatsLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 5),
    _OlTRnetStatsLostFrameErrors_Type()
)
olTRnetStatsLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLostFrameErrors.setStatus("mandatory")
_OlTRnetStatsCongestionErrors_Type = Counter32
_OlTRnetStatsCongestionErrors_Object = MibTableColumn
olTRnetStatsCongestionErrors = _OlTRnetStatsCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 6),
    _OlTRnetStatsCongestionErrors_Type()
)
olTRnetStatsCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsCongestionErrors.setStatus("mandatory")
_OlTRnetStatsFrameCopiedErrors_Type = Counter32
_OlTRnetStatsFrameCopiedErrors_Object = MibTableColumn
olTRnetStatsFrameCopiedErrors = _OlTRnetStatsFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 7),
    _OlTRnetStatsFrameCopiedErrors_Type()
)
olTRnetStatsFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsFrameCopiedErrors.setStatus("mandatory")
_OlTRnetStatsTokenErrors_Type = Counter32
_OlTRnetStatsTokenErrors_Object = MibTableColumn
olTRnetStatsTokenErrors = _OlTRnetStatsTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 8),
    _OlTRnetStatsTokenErrors_Type()
)
olTRnetStatsTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsTokenErrors.setStatus("mandatory")
_OlTRnetStatsDuplicateAddresses_Type = Counter32
_OlTRnetStatsDuplicateAddresses_Object = MibTableColumn
olTRnetStatsDuplicateAddresses = _OlTRnetStatsDuplicateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 9),
    _OlTRnetStatsDuplicateAddresses_Type()
)
olTRnetStatsDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsDuplicateAddresses.setStatus("mandatory")
_OlTRnetStatsBeaconEvents_Type = Counter32
_OlTRnetStatsBeaconEvents_Object = MibTableColumn
olTRnetStatsBeaconEvents = _OlTRnetStatsBeaconEvents_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 10),
    _OlTRnetStatsBeaconEvents_Type()
)
olTRnetStatsBeaconEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsBeaconEvents.setStatus("mandatory")


class _OlTRnetStatsLastBeaconSender_Type(OctetString):
    """Custom type olTRnetStatsLastBeaconSender based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlTRnetStatsLastBeaconSender_Type.__name__ = "OctetString"
_OlTRnetStatsLastBeaconSender_Object = MibTableColumn
olTRnetStatsLastBeaconSender = _OlTRnetStatsLastBeaconSender_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 11),
    _OlTRnetStatsLastBeaconSender_Type()
)
olTRnetStatsLastBeaconSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLastBeaconSender.setStatus("mandatory")


class _OlTRnetStatsLastBeaconNAUN_Type(OctetString):
    """Custom type olTRnetStatsLastBeaconNAUN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlTRnetStatsLastBeaconNAUN_Type.__name__ = "OctetString"
_OlTRnetStatsLastBeaconNAUN_Object = MibTableColumn
olTRnetStatsLastBeaconNAUN = _OlTRnetStatsLastBeaconNAUN_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 12),
    _OlTRnetStatsLastBeaconNAUN_Type()
)
olTRnetStatsLastBeaconNAUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLastBeaconNAUN.setStatus("mandatory")
_OlTRnetStatsLastBeaconTime_Type = TimeTicks
_OlTRnetStatsLastBeaconTime_Object = MibTableColumn
olTRnetStatsLastBeaconTime = _OlTRnetStatsLastBeaconTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 13),
    _OlTRnetStatsLastBeaconTime_Type()
)
olTRnetStatsLastBeaconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLastBeaconTime.setStatus("mandatory")


class _OlTRnetStatsLastBeaconAction_Type(Integer32):
    """Custom type olTRnetStatsLastBeaconAction based on Integer32"""
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
        *(("moduleIsolate", 4),
          ("noAction", 1),
          ("portDisable", 2),
          ("trunkDisable", 3))
    )


_OlTRnetStatsLastBeaconAction_Type.__name__ = "Integer32"
_OlTRnetStatsLastBeaconAction_Object = MibTableColumn
olTRnetStatsLastBeaconAction = _OlTRnetStatsLastBeaconAction_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 14),
    _OlTRnetStatsLastBeaconAction_Type()
)
olTRnetStatsLastBeaconAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLastBeaconAction.setStatus("mandatory")


class _OlTRnetStatsTotalStations_Type(Integer32):
    """Custom type olTRnetStatsTotalStations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OlTRnetStatsTotalStations_Type.__name__ = "Integer32"
_OlTRnetStatsTotalStations_Object = MibTableColumn
olTRnetStatsTotalStations = _OlTRnetStatsTotalStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 15),
    _OlTRnetStatsTotalStations_Type()
)
olTRnetStatsTotalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsTotalStations.setStatus("mandatory")


class _OlTRnetStatsConcStations_Type(Integer32):
    """Custom type olTRnetStatsConcStations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OlTRnetStatsConcStations_Type.__name__ = "Integer32"
_OlTRnetStatsConcStations_Object = MibTableColumn
olTRnetStatsConcStations = _OlTRnetStatsConcStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 16),
    _OlTRnetStatsConcStations_Type()
)
olTRnetStatsConcStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsConcStations.setStatus("mandatory")
_OlTRnetStatsTotalPorts_Type = Integer32
_OlTRnetStatsTotalPorts_Object = MibTableColumn
olTRnetStatsTotalPorts = _OlTRnetStatsTotalPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 17),
    _OlTRnetStatsTotalPorts_Type()
)
olTRnetStatsTotalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsTotalPorts.setStatus("mandatory")
_OlTRnetStatsEnabledPorts_Type = Integer32
_OlTRnetStatsEnabledPorts_Object = MibTableColumn
olTRnetStatsEnabledPorts = _OlTRnetStatsEnabledPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 18),
    _OlTRnetStatsEnabledPorts_Type()
)
olTRnetStatsEnabledPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsEnabledPorts.setStatus("mandatory")
_OlTRnetStatsActivePorts_Type = Integer32
_OlTRnetStatsActivePorts_Object = MibTableColumn
olTRnetStatsActivePorts = _OlTRnetStatsActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 19),
    _OlTRnetStatsActivePorts_Type()
)
olTRnetStatsActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsActivePorts.setStatus("mandatory")
_OlTRnetStatsStationTable_Object = MibTable
olTRnetStatsStationTable = _OlTRnetStatsStationTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    olTRnetStatsStationTable.setStatus("mandatory")
_OlTRnetStatsStationEntry_Object = MibTableRow
olTRnetStatsStationEntry = _OlTRnetStatsStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1)
)
olTRnetStatsStationEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTRnetStatsStationNetID"),
    (0, "CHIPCOMMIB", "olTRnetStatsStationAddr"),
)
if mibBuilder.loadTexts:
    olTRnetStatsStationEntry.setStatus("mandatory")


class _OlTRnetStatsStationNetID_Type(Integer32):
    """Custom type olTRnetStatsStationNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRnetStatsStationNetID_Type.__name__ = "Integer32"
_OlTRnetStatsStationNetID_Object = MibTableColumn
olTRnetStatsStationNetID = _OlTRnetStatsStationNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 1),
    _OlTRnetStatsStationNetID_Type()
)
olTRnetStatsStationNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationNetID.setStatus("mandatory")


class _OlTRnetStatsStationAddr_Type(OctetString):
    """Custom type olTRnetStatsStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlTRnetStatsStationAddr_Type.__name__ = "OctetString"
_OlTRnetStatsStationAddr_Object = MibTableColumn
olTRnetStatsStationAddr = _OlTRnetStatsStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 2),
    _OlTRnetStatsStationAddr_Type()
)
olTRnetStatsStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationAddr.setStatus("mandatory")


class _OlTRnetStatsStationSlotIndex_Type(Integer32):
    """Custom type olTRnetStatsStationSlotIndex based on Integer32"""
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
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("external", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_OlTRnetStatsStationSlotIndex_Type.__name__ = "Integer32"
_OlTRnetStatsStationSlotIndex_Object = MibTableColumn
olTRnetStatsStationSlotIndex = _OlTRnetStatsStationSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 3),
    _OlTRnetStatsStationSlotIndex_Type()
)
olTRnetStatsStationSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationSlotIndex.setStatus("mandatory")
_OlTRnetStatsStationPortIndex_Type = Integer32
_OlTRnetStatsStationPortIndex_Object = MibTableColumn
olTRnetStatsStationPortIndex = _OlTRnetStatsStationPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 4),
    _OlTRnetStatsStationPortIndex_Type()
)
olTRnetStatsStationPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationPortIndex.setStatus("mandatory")


class _OlTRnetStatsStationNAUNAddress_Type(OctetString):
    """Custom type olTRnetStatsStationNAUNAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlTRnetStatsStationNAUNAddress_Type.__name__ = "OctetString"
_OlTRnetStatsStationNAUNAddress_Object = MibTableColumn
olTRnetStatsStationNAUNAddress = _OlTRnetStatsStationNAUNAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 5),
    _OlTRnetStatsStationNAUNAddress_Type()
)
olTRnetStatsStationNAUNAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationNAUNAddress.setStatus("mandatory")
_OlTRnetStatsStationLineErrors_Type = Counter32
_OlTRnetStatsStationLineErrors_Object = MibTableColumn
olTRnetStatsStationLineErrors = _OlTRnetStatsStationLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 6),
    _OlTRnetStatsStationLineErrors_Type()
)
olTRnetStatsStationLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationLineErrors.setStatus("mandatory")
_OlTRnetStatsStationBurstErrors_Type = Counter32
_OlTRnetStatsStationBurstErrors_Object = MibTableColumn
olTRnetStatsStationBurstErrors = _OlTRnetStatsStationBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 7),
    _OlTRnetStatsStationBurstErrors_Type()
)
olTRnetStatsStationBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationBurstErrors.setStatus("mandatory")
_OlTRnetStatsStationACErrors_Type = Counter32
_OlTRnetStatsStationACErrors_Object = MibTableColumn
olTRnetStatsStationACErrors = _OlTRnetStatsStationACErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 8),
    _OlTRnetStatsStationACErrors_Type()
)
olTRnetStatsStationACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationACErrors.setStatus("mandatory")
_OlTRnetStatsStationLostFrameErrors_Type = Counter32
_OlTRnetStatsStationLostFrameErrors_Object = MibTableColumn
olTRnetStatsStationLostFrameErrors = _OlTRnetStatsStationLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 9),
    _OlTRnetStatsStationLostFrameErrors_Type()
)
olTRnetStatsStationLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationLostFrameErrors.setStatus("mandatory")
_OlTRnetStatsStationCongestionErrors_Type = Counter32
_OlTRnetStatsStationCongestionErrors_Object = MibTableColumn
olTRnetStatsStationCongestionErrors = _OlTRnetStatsStationCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 10),
    _OlTRnetStatsStationCongestionErrors_Type()
)
olTRnetStatsStationCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationCongestionErrors.setStatus("mandatory")
_OlTRnetStatsStationFrameCopiedErrors_Type = Counter32
_OlTRnetStatsStationFrameCopiedErrors_Object = MibTableColumn
olTRnetStatsStationFrameCopiedErrors = _OlTRnetStatsStationFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 11),
    _OlTRnetStatsStationFrameCopiedErrors_Type()
)
olTRnetStatsStationFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationFrameCopiedErrors.setStatus("mandatory")
_OlTRnetStatsStationTokenErrors_Type = Counter32
_OlTRnetStatsStationTokenErrors_Object = MibTableColumn
olTRnetStatsStationTokenErrors = _OlTRnetStatsStationTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 12),
    _OlTRnetStatsStationTokenErrors_Type()
)
olTRnetStatsStationTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationTokenErrors.setStatus("mandatory")
_OlTRnetStatsStationDuplicateAddresses_Type = Counter32
_OlTRnetStatsStationDuplicateAddresses_Object = MibTableColumn
olTRnetStatsStationDuplicateAddresses = _OlTRnetStatsStationDuplicateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 13),
    _OlTRnetStatsStationDuplicateAddresses_Type()
)
olTRnetStatsStationDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationDuplicateAddresses.setStatus("mandatory")
_OlTRnetStatsPortTable_Object = MibTable
olTRnetStatsPortTable = _OlTRnetStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    olTRnetStatsPortTable.setStatus("mandatory")
_OlTRnetStatsPortEntry_Object = MibTableRow
olTRnetStatsPortEntry = _OlTRnetStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1)
)
olTRnetStatsPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTRnetStatsPortSlotIndex"),
    (0, "CHIPCOMMIB", "olTRnetStatsPortIndex"),
)
if mibBuilder.loadTexts:
    olTRnetStatsPortEntry.setStatus("mandatory")
_OlTRnetStatsPortSlotIndex_Type = Integer32
_OlTRnetStatsPortSlotIndex_Object = MibTableColumn
olTRnetStatsPortSlotIndex = _OlTRnetStatsPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 1),
    _OlTRnetStatsPortSlotIndex_Type()
)
olTRnetStatsPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortSlotIndex.setStatus("mandatory")
_OlTRnetStatsPortIndex_Type = Integer32
_OlTRnetStatsPortIndex_Object = MibTableColumn
olTRnetStatsPortIndex = _OlTRnetStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 2),
    _OlTRnetStatsPortIndex_Type()
)
olTRnetStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortIndex.setStatus("mandatory")


class _OlTRnetStatsPortNetID_Type(Integer32):
    """Custom type olTRnetStatsPortNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRnetStatsPortNetID_Type.__name__ = "Integer32"
_OlTRnetStatsPortNetID_Object = MibTableColumn
olTRnetStatsPortNetID = _OlTRnetStatsPortNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 3),
    _OlTRnetStatsPortNetID_Type()
)
olTRnetStatsPortNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortNetID.setStatus("mandatory")
_OlTRnetStatsPortTotalStations_Type = Integer32
_OlTRnetStatsPortTotalStations_Object = MibTableColumn
olTRnetStatsPortTotalStations = _OlTRnetStatsPortTotalStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 4),
    _OlTRnetStatsPortTotalStations_Type()
)
olTRnetStatsPortTotalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortTotalStations.setStatus("mandatory")


class _OlTRnetStatsPortAddress_Type(OctetString):
    """Custom type olTRnetStatsPortAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlTRnetStatsPortAddress_Type.__name__ = "OctetString"
_OlTRnetStatsPortAddress_Object = MibTableColumn
olTRnetStatsPortAddress = _OlTRnetStatsPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 5),
    _OlTRnetStatsPortAddress_Type()
)
olTRnetStatsPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortAddress.setStatus("mandatory")
_OlTRnetStatsPortLineErrors_Type = Counter32
_OlTRnetStatsPortLineErrors_Object = MibTableColumn
olTRnetStatsPortLineErrors = _OlTRnetStatsPortLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 6),
    _OlTRnetStatsPortLineErrors_Type()
)
olTRnetStatsPortLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortLineErrors.setStatus("mandatory")
_OlTRnetStatsPortBurstErrors_Type = Counter32
_OlTRnetStatsPortBurstErrors_Object = MibTableColumn
olTRnetStatsPortBurstErrors = _OlTRnetStatsPortBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 7),
    _OlTRnetStatsPortBurstErrors_Type()
)
olTRnetStatsPortBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortBurstErrors.setStatus("mandatory")
_OlTRnetStatsPortACErrors_Type = Counter32
_OlTRnetStatsPortACErrors_Object = MibTableColumn
olTRnetStatsPortACErrors = _OlTRnetStatsPortACErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 8),
    _OlTRnetStatsPortACErrors_Type()
)
olTRnetStatsPortACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortACErrors.setStatus("mandatory")
_OlTRnetStatsPortLostFrameErrors_Type = Counter32
_OlTRnetStatsPortLostFrameErrors_Object = MibTableColumn
olTRnetStatsPortLostFrameErrors = _OlTRnetStatsPortLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 9),
    _OlTRnetStatsPortLostFrameErrors_Type()
)
olTRnetStatsPortLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortLostFrameErrors.setStatus("mandatory")
_OlTRnetStatsPortCongestionErrors_Type = Counter32
_OlTRnetStatsPortCongestionErrors_Object = MibTableColumn
olTRnetStatsPortCongestionErrors = _OlTRnetStatsPortCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 10),
    _OlTRnetStatsPortCongestionErrors_Type()
)
olTRnetStatsPortCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortCongestionErrors.setStatus("mandatory")
_OlTRnetStatsPortFrameCopiedErrors_Type = Counter32
_OlTRnetStatsPortFrameCopiedErrors_Object = MibTableColumn
olTRnetStatsPortFrameCopiedErrors = _OlTRnetStatsPortFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 11),
    _OlTRnetStatsPortFrameCopiedErrors_Type()
)
olTRnetStatsPortFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortFrameCopiedErrors.setStatus("mandatory")
_OlTRnetStatsPortTokenErrors_Type = Counter32
_OlTRnetStatsPortTokenErrors_Object = MibTableColumn
olTRnetStatsPortTokenErrors = _OlTRnetStatsPortTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 12),
    _OlTRnetStatsPortTokenErrors_Type()
)
olTRnetStatsPortTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortTokenErrors.setStatus("mandatory")
_OlTRnetStatsPortDuplicateAddresses_Type = Counter32
_OlTRnetStatsPortDuplicateAddresses_Object = MibTableColumn
olTRnetStatsPortDuplicateAddresses = _OlTRnetStatsPortDuplicateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 13),
    _OlTRnetStatsPortDuplicateAddresses_Type()
)
olTRnetStatsPortDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortDuplicateAddresses.setStatus("mandatory")
_OlTRnetMapSummary_ObjectIdentity = ObjectIdentity
olTRnetMapSummary = _OlTRnetMapSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5)
)


class _OlTRnetMapSummaryLogicalState_Type(Integer32):
    """Custom type olTRnetMapSummaryLogicalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changing", 1),
          ("notChanging", 2))
    )


_OlTRnetMapSummaryLogicalState_Type.__name__ = "Integer32"
_OlTRnetMapSummaryLogicalState_Object = MibScalar
olTRnetMapSummaryLogicalState = _OlTRnetMapSummaryLogicalState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 1),
    _OlTRnetMapSummaryLogicalState_Type()
)
olTRnetMapSummaryLogicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetMapSummaryLogicalState.setStatus("mandatory")


class _OlTRnetMapSummaryLogicalLock_Type(Integer32):
    """Custom type olTRnetMapSummaryLogicalLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_OlTRnetMapSummaryLogicalLock_Type.__name__ = "Integer32"
_OlTRnetMapSummaryLogicalLock_Object = MibScalar
olTRnetMapSummaryLogicalLock = _OlTRnetMapSummaryLogicalLock_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 2),
    _OlTRnetMapSummaryLogicalLock_Type()
)
olTRnetMapSummaryLogicalLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRnetMapSummaryLogicalLock.setStatus("mandatory")
_OlTRnetMapSummaryTable_Object = MibTable
olTRnetMapSummaryTable = _OlTRnetMapSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 3)
)
if mibBuilder.loadTexts:
    olTRnetMapSummaryTable.setStatus("mandatory")
_OlTRnetMapSummaryEntry_Object = MibTableRow
olTRnetMapSummaryEntry = _OlTRnetMapSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 3, 1)
)
olTRnetMapSummaryEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTRnetMapSummaryNetID"),
    (0, "CHIPCOMMIB", "olTRnetMapSummaryIndex"),
)
if mibBuilder.loadTexts:
    olTRnetMapSummaryEntry.setStatus("mandatory")


class _OlTRnetMapSummaryNetID_Type(Integer32):
    """Custom type olTRnetMapSummaryNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRnetMapSummaryNetID_Type.__name__ = "Integer32"
_OlTRnetMapSummaryNetID_Object = MibTableColumn
olTRnetMapSummaryNetID = _OlTRnetMapSummaryNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 3, 1, 1),
    _OlTRnetMapSummaryNetID_Type()
)
olTRnetMapSummaryNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetMapSummaryNetID.setStatus("mandatory")
_OlTRnetMapSummaryIndex_Type = Integer32
_OlTRnetMapSummaryIndex_Object = MibTableColumn
olTRnetMapSummaryIndex = _OlTRnetMapSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 3, 1, 2),
    _OlTRnetMapSummaryIndex_Type()
)
olTRnetMapSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetMapSummaryIndex.setStatus("mandatory")


class _OlTRnetMapSummary32Stations_Type(OctetString):
    """Custom type olTRnetMapSummary32Stations based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 256),
    )


_OlTRnetMapSummary32Stations_Type.__name__ = "OctetString"
_OlTRnetMapSummary32Stations_Object = MibTableColumn
olTRnetMapSummary32Stations = _OlTRnetMapSummary32Stations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 3, 1, 3),
    _OlTRnetMapSummary32Stations_Type()
)
olTRnetMapSummary32Stations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetMapSummary32Stations.setStatus("mandatory")
_OlTRTrafTable_Object = MibTable
olTRTrafTable = _OlTRTrafTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    olTRTrafTable.setStatus("mandatory")
_OlTRTrafEntry_Object = MibTableRow
olTRTrafEntry = _OlTRTrafEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1)
)
olTRTrafEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTRTrafNetID"),
)
if mibBuilder.loadTexts:
    olTRTrafEntry.setStatus("mandatory")


class _OlTRTrafNetID_Type(Integer32):
    """Custom type olTRTrafNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafNetID_Type.__name__ = "Integer32"
_OlTRTrafNetID_Object = MibTableColumn
olTRTrafNetID = _OlTRTrafNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 1),
    _OlTRTrafNetID_Type()
)
olTRTrafNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafNetID.setStatus("mandatory")
_OlTRTrafTokenRotationTime_Type = Integer32
_OlTRTrafTokenRotationTime_Object = MibTableColumn
olTRTrafTokenRotationTime = _OlTRTrafTokenRotationTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 2),
    _OlTRTrafTokenRotationTime_Type()
)
olTRTrafTokenRotationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTokenRotationTime.setStatus("mandatory")
_OlTRTrafDropEvents_Type = Counter32
_OlTRTrafDropEvents_Object = MibTableColumn
olTRTrafDropEvents = _OlTRTrafDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 3),
    _OlTRTrafDropEvents_Type()
)
olTRTrafDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafDropEvents.setStatus("mandatory")
_OlTRTrafOctets_Type = Counter32
_OlTRTrafOctets_Object = MibTableColumn
olTRTrafOctets = _OlTRTrafOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 4),
    _OlTRTrafOctets_Type()
)
olTRTrafOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafOctets.setStatus("mandatory")
_OlTRTrafFrames_Type = Counter32
_OlTRTrafFrames_Object = MibTableColumn
olTRTrafFrames = _OlTRTrafFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 5),
    _OlTRTrafFrames_Type()
)
olTRTrafFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames.setStatus("mandatory")
_OlTRTrafMacOctets_Type = Counter32
_OlTRTrafMacOctets_Object = MibTableColumn
olTRTrafMacOctets = _OlTRTrafMacOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 6),
    _OlTRTrafMacOctets_Type()
)
olTRTrafMacOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafMacOctets.setStatus("mandatory")
_OlTRTrafMacFrames_Type = Counter32
_OlTRTrafMacFrames_Object = MibTableColumn
olTRTrafMacFrames = _OlTRTrafMacFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 7),
    _OlTRTrafMacFrames_Type()
)
olTRTrafMacFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafMacFrames.setStatus("mandatory")
_OlTRTrafBroadcastFrames_Type = Counter32
_OlTRTrafBroadcastFrames_Object = MibTableColumn
olTRTrafBroadcastFrames = _OlTRTrafBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 8),
    _OlTRTrafBroadcastFrames_Type()
)
olTRTrafBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafBroadcastFrames.setStatus("mandatory")
_OlTRTrafMulticastFrames_Type = Counter32
_OlTRTrafMulticastFrames_Object = MibTableColumn
olTRTrafMulticastFrames = _OlTRTrafMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 9),
    _OlTRTrafMulticastFrames_Type()
)
olTRTrafMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafMulticastFrames.setStatus("mandatory")
_OlTRTrafFrames18to63Octets_Type = Counter32
_OlTRTrafFrames18to63Octets_Object = MibTableColumn
olTRTrafFrames18to63Octets = _OlTRTrafFrames18to63Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 10),
    _OlTRTrafFrames18to63Octets_Type()
)
olTRTrafFrames18to63Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames18to63Octets.setStatus("mandatory")
_OlTRTrafFrames64to127Octets_Type = Counter32
_OlTRTrafFrames64to127Octets_Object = MibTableColumn
olTRTrafFrames64to127Octets = _OlTRTrafFrames64to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 11),
    _OlTRTrafFrames64to127Octets_Type()
)
olTRTrafFrames64to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames64to127Octets.setStatus("mandatory")
_OlTRTrafFrames128to255Octets_Type = Counter32
_OlTRTrafFrames128to255Octets_Object = MibTableColumn
olTRTrafFrames128to255Octets = _OlTRTrafFrames128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 12),
    _OlTRTrafFrames128to255Octets_Type()
)
olTRTrafFrames128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames128to255Octets.setStatus("mandatory")
_OlTRTrafFrames256to511Octets_Type = Counter32
_OlTRTrafFrames256to511Octets_Object = MibTableColumn
olTRTrafFrames256to511Octets = _OlTRTrafFrames256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 13),
    _OlTRTrafFrames256to511Octets_Type()
)
olTRTrafFrames256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames256to511Octets.setStatus("mandatory")
_OlTRTrafFrames512to1023Octets_Type = Counter32
_OlTRTrafFrames512to1023Octets_Object = MibTableColumn
olTRTrafFrames512to1023Octets = _OlTRTrafFrames512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 14),
    _OlTRTrafFrames512to1023Octets_Type()
)
olTRTrafFrames512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames512to1023Octets.setStatus("mandatory")
_OlTRTrafFrames1024to2047Octets_Type = Counter32
_OlTRTrafFrames1024to2047Octets_Object = MibTableColumn
olTRTrafFrames1024to2047Octets = _OlTRTrafFrames1024to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 15),
    _OlTRTrafFrames1024to2047Octets_Type()
)
olTRTrafFrames1024to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames1024to2047Octets.setStatus("mandatory")
_OlTRTrafFrames2048to4095Octets_Type = Counter32
_OlTRTrafFrames2048to4095Octets_Object = MibTableColumn
olTRTrafFrames2048to4095Octets = _OlTRTrafFrames2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 16),
    _OlTRTrafFrames2048to4095Octets_Type()
)
olTRTrafFrames2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames2048to4095Octets.setStatus("mandatory")
_OlTRTrafFrames4096to8191Octets_Type = Counter32
_OlTRTrafFrames4096to8191Octets_Object = MibTableColumn
olTRTrafFrames4096to8191Octets = _OlTRTrafFrames4096to8191Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 17),
    _OlTRTrafFrames4096to8191Octets_Type()
)
olTRTrafFrames4096to8191Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames4096to8191Octets.setStatus("mandatory")
_OlTRTrafFrames8192to18000Octets_Type = Counter32
_OlTRTrafFrames8192to18000Octets_Object = MibTableColumn
olTRTrafFrames8192to18000Octets = _OlTRTrafFrames8192to18000Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 18),
    _OlTRTrafFrames8192to18000Octets_Type()
)
olTRTrafFrames8192to18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames8192to18000Octets.setStatus("mandatory")
_OlTRTrafFramesGreaterThan18000Octets_Type = Counter32
_OlTRTrafFramesGreaterThan18000Octets_Object = MibTableColumn
olTRTrafFramesGreaterThan18000Octets = _OlTRTrafFramesGreaterThan18000Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 19),
    _OlTRTrafFramesGreaterThan18000Octets_Type()
)
olTRTrafFramesGreaterThan18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFramesGreaterThan18000Octets.setStatus("mandatory")
_OlTRTrafControlTable_Object = MibTable
olTRTrafControlTable = _OlTRTrafControlTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    olTRTrafControlTable.setStatus("mandatory")
_OlTRTrafControlEntry_Object = MibTableRow
olTRTrafControlEntry = _OlTRTrafControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1)
)
olTRTrafControlEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTRTrafControlNetID"),
)
if mibBuilder.loadTexts:
    olTRTrafControlEntry.setStatus("mandatory")


class _OlTRTrafControlNetID_Type(Integer32):
    """Custom type olTRTrafControlNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafControlNetID_Type.__name__ = "Integer32"
_OlTRTrafControlNetID_Object = MibTableColumn
olTRTrafControlNetID = _OlTRTrafControlNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 1),
    _OlTRTrafControlNetID_Type()
)
olTRTrafControlNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlNetID.setStatus("mandatory")


class _OlTRTrafControlLogicalState_Type(Integer32):
    """Custom type olTRTrafControlLogicalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changing", 1),
          ("notChanging", 2))
    )


_OlTRTrafControlLogicalState_Type.__name__ = "Integer32"
_OlTRTrafControlLogicalState_Object = MibTableColumn
olTRTrafControlLogicalState = _OlTRTrafControlLogicalState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 2),
    _OlTRTrafControlLogicalState_Type()
)
olTRTrafControlLogicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlLogicalState.setStatus("mandatory")


class _OlTRTrafControlLogicalLock_Type(Integer32):
    """Custom type olTRTrafControlLogicalLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_OlTRTrafControlLogicalLock_Type.__name__ = "Integer32"
_OlTRTrafControlLogicalLock_Object = MibTableColumn
olTRTrafControlLogicalLock = _OlTRTrafControlLogicalLock_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 3),
    _OlTRTrafControlLogicalLock_Type()
)
olTRTrafControlLogicalLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRTrafControlLogicalLock.setStatus("mandatory")


class _OlTRTrafControlClear_Type(Integer32):
    """Custom type olTRTrafControlClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("normal", 1))
    )


_OlTRTrafControlClear_Type.__name__ = "Integer32"
_OlTRTrafControlClear_Object = MibTableColumn
olTRTrafControlClear = _OlTRTrafControlClear_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 4),
    _OlTRTrafControlClear_Type()
)
olTRTrafControlClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRTrafControlClear.setStatus("mandatory")
_OlTRTrafControlLastClearTime_Type = TimeTicks
_OlTRTrafControlLastClearTime_Object = MibTableColumn
olTRTrafControlLastClearTime = _OlTRTrafControlLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 5),
    _OlTRTrafControlLastClearTime_Type()
)
olTRTrafControlLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlLastClearTime.setStatus("mandatory")
_OlTRTrafControlTotalStations_Type = Integer32
_OlTRTrafControlTotalStations_Object = MibTableColumn
olTRTrafControlTotalStations = _OlTRTrafControlTotalStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 6),
    _OlTRTrafControlTotalStations_Type()
)
olTRTrafControlTotalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlTotalStations.setStatus("mandatory")
_OlTRTrafControlStationLastChangeTime_Type = TimeTicks
_OlTRTrafControlStationLastChangeTime_Object = MibTableColumn
olTRTrafControlStationLastChangeTime = _OlTRTrafControlStationLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 7),
    _OlTRTrafControlStationLastChangeTime_Type()
)
olTRTrafControlStationLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlStationLastChangeTime.setStatus("mandatory")
_OlTRTrafControlPortTotalStations_Type = Integer32
_OlTRTrafControlPortTotalStations_Object = MibTableColumn
olTRTrafControlPortTotalStations = _OlTRTrafControlPortTotalStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 8),
    _OlTRTrafControlPortTotalStations_Type()
)
olTRTrafControlPortTotalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlPortTotalStations.setStatus("mandatory")
_OlTRTrafControlPortLastChangeTime_Type = TimeTicks
_OlTRTrafControlPortLastChangeTime_Object = MibTableColumn
olTRTrafControlPortLastChangeTime = _OlTRTrafControlPortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 9),
    _OlTRTrafControlPortLastChangeTime_Type()
)
olTRTrafControlPortLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlPortLastChangeTime.setStatus("mandatory")
_OlTRTrafControlTopNMaxStations_Type = Integer32
_OlTRTrafControlTopNMaxStations_Object = MibTableColumn
olTRTrafControlTopNMaxStations = _OlTRTrafControlTopNMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 10),
    _OlTRTrafControlTopNMaxStations_Type()
)
olTRTrafControlTopNMaxStations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRTrafControlTopNMaxStations.setStatus("mandatory")
_OlTRTrafControlTopNTotalStations_Type = Integer32
_OlTRTrafControlTopNTotalStations_Object = MibTableColumn
olTRTrafControlTopNTotalStations = _OlTRTrafControlTopNTotalStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 11),
    _OlTRTrafControlTopNTotalStations_Type()
)
olTRTrafControlTopNTotalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlTopNTotalStations.setStatus("mandatory")
_OlTRTrafControlTopNLastChangeTime_Type = TimeTicks
_OlTRTrafControlTopNLastChangeTime_Object = MibTableColumn
olTRTrafControlTopNLastChangeTime = _OlTRTrafControlTopNLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 12),
    _OlTRTrafControlTopNLastChangeTime_Type()
)
olTRTrafControlTopNLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlTopNLastChangeTime.setStatus("mandatory")
_OlTRTrafControlTopNInterval_Type = Integer32
_OlTRTrafControlTopNInterval_Object = MibTableColumn
olTRTrafControlTopNInterval = _OlTRTrafControlTopNInterval_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 13),
    _OlTRTrafControlTopNInterval_Type()
)
olTRTrafControlTopNInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRTrafControlTopNInterval.setStatus("mandatory")
_OlTRTrafStationTable_Object = MibTable
olTRTrafStationTable = _OlTRTrafStationTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    olTRTrafStationTable.setStatus("mandatory")
_OlTRTrafStationEntry_Object = MibTableRow
olTRTrafStationEntry = _OlTRTrafStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1)
)
olTRTrafStationEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTRTrafStationNetID"),
    (0, "CHIPCOMMIB", "olTRTrafStationAddress"),
)
if mibBuilder.loadTexts:
    olTRTrafStationEntry.setStatus("mandatory")


class _OlTRTrafStationNetID_Type(Integer32):
    """Custom type olTRTrafStationNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafStationNetID_Type.__name__ = "Integer32"
_OlTRTrafStationNetID_Object = MibTableColumn
olTRTrafStationNetID = _OlTRTrafStationNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 1),
    _OlTRTrafStationNetID_Type()
)
olTRTrafStationNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationNetID.setStatus("mandatory")
_OlTRTrafStationAddress_Type = MacAddress
_OlTRTrafStationAddress_Object = MibTableColumn
olTRTrafStationAddress = _OlTRTrafStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 2),
    _OlTRTrafStationAddress_Type()
)
olTRTrafStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationAddress.setStatus("mandatory")


class _OlTRTrafStationSlotIndex_Type(Integer32):
    """Custom type olTRTrafStationSlotIndex based on Integer32"""
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
              15,
              16,
              17,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("external", 255),
          ("remote-ring", 254),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_OlTRTrafStationSlotIndex_Type.__name__ = "Integer32"
_OlTRTrafStationSlotIndex_Object = MibTableColumn
olTRTrafStationSlotIndex = _OlTRTrafStationSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 3),
    _OlTRTrafStationSlotIndex_Type()
)
olTRTrafStationSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationSlotIndex.setStatus("mandatory")
_OlTRTrafStationPortIndex_Type = Integer32
_OlTRTrafStationPortIndex_Object = MibTableColumn
olTRTrafStationPortIndex = _OlTRTrafStationPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 4),
    _OlTRTrafStationPortIndex_Type()
)
olTRTrafStationPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationPortIndex.setStatus("mandatory")
_OlTRTrafStationInFrames_Type = Counter32
_OlTRTrafStationInFrames_Object = MibTableColumn
olTRTrafStationInFrames = _OlTRTrafStationInFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 5),
    _OlTRTrafStationInFrames_Type()
)
olTRTrafStationInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationInFrames.setStatus("mandatory")
_OlTRTrafStationOutFrames_Type = Counter32
_OlTRTrafStationOutFrames_Object = MibTableColumn
olTRTrafStationOutFrames = _OlTRTrafStationOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 6),
    _OlTRTrafStationOutFrames_Type()
)
olTRTrafStationOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationOutFrames.setStatus("mandatory")
_OlTRTrafStationInOctets_Type = Counter32
_OlTRTrafStationInOctets_Object = MibTableColumn
olTRTrafStationInOctets = _OlTRTrafStationInOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 7),
    _OlTRTrafStationInOctets_Type()
)
olTRTrafStationInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationInOctets.setStatus("mandatory")
_OlTRTrafStationOutOctets_Type = Counter32
_OlTRTrafStationOutOctets_Object = MibTableColumn
olTRTrafStationOutOctets = _OlTRTrafStationOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 8),
    _OlTRTrafStationOutOctets_Type()
)
olTRTrafStationOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationOutOctets.setStatus("mandatory")
_OlTRTrafStationOutErrors_Type = Counter32
_OlTRTrafStationOutErrors_Object = MibTableColumn
olTRTrafStationOutErrors = _OlTRTrafStationOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 9),
    _OlTRTrafStationOutErrors_Type()
)
olTRTrafStationOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationOutErrors.setStatus("mandatory")
_OlTRTrafStationOutBroadcastFrames_Type = Counter32
_OlTRTrafStationOutBroadcastFrames_Object = MibTableColumn
olTRTrafStationOutBroadcastFrames = _OlTRTrafStationOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 10),
    _OlTRTrafStationOutBroadcastFrames_Type()
)
olTRTrafStationOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationOutBroadcastFrames.setStatus("mandatory")
_OlTRTrafStationOutMulticastFrames_Type = Counter32
_OlTRTrafStationOutMulticastFrames_Object = MibTableColumn
olTRTrafStationOutMulticastFrames = _OlTRTrafStationOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 11),
    _OlTRTrafStationOutMulticastFrames_Type()
)
olTRTrafStationOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationOutMulticastFrames.setStatus("mandatory")
_OlTRTrafPortTable_Object = MibTable
olTRTrafPortTable = _OlTRTrafPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9)
)
if mibBuilder.loadTexts:
    olTRTrafPortTable.setStatus("mandatory")
_OlTRTrafPortEntry_Object = MibTableRow
olTRTrafPortEntry = _OlTRTrafPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1)
)
olTRTrafPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTRTrafPortSlotIndex"),
    (0, "CHIPCOMMIB", "olTRTrafPortPortIndex"),
)
if mibBuilder.loadTexts:
    olTRTrafPortEntry.setStatus("mandatory")
_OlTRTrafPortSlotIndex_Type = Integer32
_OlTRTrafPortSlotIndex_Object = MibTableColumn
olTRTrafPortSlotIndex = _OlTRTrafPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 1),
    _OlTRTrafPortSlotIndex_Type()
)
olTRTrafPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortSlotIndex.setStatus("mandatory")
_OlTRTrafPortPortIndex_Type = Integer32
_OlTRTrafPortPortIndex_Object = MibTableColumn
olTRTrafPortPortIndex = _OlTRTrafPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 2),
    _OlTRTrafPortPortIndex_Type()
)
olTRTrafPortPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortPortIndex.setStatus("mandatory")


class _OlTRTrafPortNetID_Type(Integer32):
    """Custom type olTRTrafPortNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafPortNetID_Type.__name__ = "Integer32"
_OlTRTrafPortNetID_Object = MibTableColumn
olTRTrafPortNetID = _OlTRTrafPortNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 3),
    _OlTRTrafPortNetID_Type()
)
olTRTrafPortNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortNetID.setStatus("mandatory")
_OlTRTrafPortAddress_Type = MacAddress
_OlTRTrafPortAddress_Object = MibTableColumn
olTRTrafPortAddress = _OlTRTrafPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 4),
    _OlTRTrafPortAddress_Type()
)
olTRTrafPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortAddress.setStatus("mandatory")
_OlTRTrafPortInFrames_Type = Counter32
_OlTRTrafPortInFrames_Object = MibTableColumn
olTRTrafPortInFrames = _OlTRTrafPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 5),
    _OlTRTrafPortInFrames_Type()
)
olTRTrafPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortInFrames.setStatus("mandatory")
_OlTRTrafPortOutFrames_Type = Counter32
_OlTRTrafPortOutFrames_Object = MibTableColumn
olTRTrafPortOutFrames = _OlTRTrafPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 6),
    _OlTRTrafPortOutFrames_Type()
)
olTRTrafPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortOutFrames.setStatus("mandatory")
_OlTRTrafPortInOctets_Type = Counter32
_OlTRTrafPortInOctets_Object = MibTableColumn
olTRTrafPortInOctets = _OlTRTrafPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 7),
    _OlTRTrafPortInOctets_Type()
)
olTRTrafPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortInOctets.setStatus("mandatory")
_OlTRTrafPortOutOctets_Type = Counter32
_OlTRTrafPortOutOctets_Object = MibTableColumn
olTRTrafPortOutOctets = _OlTRTrafPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 8),
    _OlTRTrafPortOutOctets_Type()
)
olTRTrafPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortOutOctets.setStatus("mandatory")
_OlTRTrafPortOutErrors_Type = Counter32
_OlTRTrafPortOutErrors_Object = MibTableColumn
olTRTrafPortOutErrors = _OlTRTrafPortOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 9),
    _OlTRTrafPortOutErrors_Type()
)
olTRTrafPortOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortOutErrors.setStatus("mandatory")
_OlTRTrafPortOutBroadcastFrames_Type = Counter32
_OlTRTrafPortOutBroadcastFrames_Object = MibTableColumn
olTRTrafPortOutBroadcastFrames = _OlTRTrafPortOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 10),
    _OlTRTrafPortOutBroadcastFrames_Type()
)
olTRTrafPortOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortOutBroadcastFrames.setStatus("mandatory")
_OlTRTrafPortOutMulticastFrames_Type = Counter32
_OlTRTrafPortOutMulticastFrames_Object = MibTableColumn
olTRTrafPortOutMulticastFrames = _OlTRTrafPortOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 11),
    _OlTRTrafPortOutMulticastFrames_Type()
)
olTRTrafPortOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortOutMulticastFrames.setStatus("mandatory")
_OlTRTrafTopNTable_Object = MibTable
olTRTrafTopNTable = _OlTRTrafTopNTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10)
)
if mibBuilder.loadTexts:
    olTRTrafTopNTable.setStatus("mandatory")
_OlTRTrafTopNEntry_Object = MibTableRow
olTRTrafTopNEntry = _OlTRTrafTopNEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1)
)
olTRTrafTopNEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTRTrafTopNNetID"),
    (0, "CHIPCOMMIB", "olTRTrafTopNStatistic"),
    (0, "CHIPCOMMIB", "olTRTrafTopNIndex"),
)
if mibBuilder.loadTexts:
    olTRTrafTopNEntry.setStatus("mandatory")


class _OlTRTrafTopNNetID_Type(Integer32):
    """Custom type olTRTrafTopNNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafTopNNetID_Type.__name__ = "Integer32"
_OlTRTrafTopNNetID_Object = MibTableColumn
olTRTrafTopNNetID = _OlTRTrafTopNNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 1),
    _OlTRTrafTopNNetID_Type()
)
olTRTrafTopNNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNNetID.setStatus("mandatory")


class _OlTRTrafTopNStatistic_Type(Integer32):
    """Custom type olTRTrafTopNStatistic based on Integer32"""
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
        *(("olTRTrafTopNInFrames", 1),
          ("olTRTrafTopNInOctets", 3),
          ("olTRTrafTopNOutBroadcastFrames", 6),
          ("olTRTrafTopNOutErrors", 5),
          ("olTRTrafTopNOutFrames", 2),
          ("olTRTrafTopNOutMulticastFrames", 7),
          ("olTRTrafTopNOutOctets", 4))
    )


_OlTRTrafTopNStatistic_Type.__name__ = "Integer32"
_OlTRTrafTopNStatistic_Object = MibTableColumn
olTRTrafTopNStatistic = _OlTRTrafTopNStatistic_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 2),
    _OlTRTrafTopNStatistic_Type()
)
olTRTrafTopNStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNStatistic.setStatus("mandatory")
_OlTRTrafTopNIndex_Type = Integer32
_OlTRTrafTopNIndex_Object = MibTableColumn
olTRTrafTopNIndex = _OlTRTrafTopNIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 3),
    _OlTRTrafTopNIndex_Type()
)
olTRTrafTopNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNIndex.setStatus("mandatory")
_OlTRTrafTopNAddress_Type = MacAddress
_OlTRTrafTopNAddress_Object = MibTableColumn
olTRTrafTopNAddress = _OlTRTrafTopNAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 4),
    _OlTRTrafTopNAddress_Type()
)
olTRTrafTopNAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNAddress.setStatus("mandatory")


class _OlTRTrafTopNSlotIndex_Type(Integer32):
    """Custom type olTRTrafTopNSlotIndex based on Integer32"""
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
              15,
              16,
              17,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("external", 255),
          ("remote-ring", 254),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_OlTRTrafTopNSlotIndex_Type.__name__ = "Integer32"
_OlTRTrafTopNSlotIndex_Object = MibTableColumn
olTRTrafTopNSlotIndex = _OlTRTrafTopNSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 5),
    _OlTRTrafTopNSlotIndex_Type()
)
olTRTrafTopNSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNSlotIndex.setStatus("mandatory")
_OlTRTrafTopNPortIndex_Type = Integer32
_OlTRTrafTopNPortIndex_Object = MibTableColumn
olTRTrafTopNPortIndex = _OlTRTrafTopNPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 6),
    _OlTRTrafTopNPortIndex_Type()
)
olTRTrafTopNPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNPortIndex.setStatus("mandatory")
_OlTRTrafTopNInFrames_Type = Counter32
_OlTRTrafTopNInFrames_Object = MibTableColumn
olTRTrafTopNInFrames = _OlTRTrafTopNInFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 7),
    _OlTRTrafTopNInFrames_Type()
)
olTRTrafTopNInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNInFrames.setStatus("mandatory")
_OlTRTrafTopNOutFrames_Type = Counter32
_OlTRTrafTopNOutFrames_Object = MibTableColumn
olTRTrafTopNOutFrames = _OlTRTrafTopNOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 8),
    _OlTRTrafTopNOutFrames_Type()
)
olTRTrafTopNOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNOutFrames.setStatus("mandatory")
_OlTRTrafTopNInOctets_Type = Counter32
_OlTRTrafTopNInOctets_Object = MibTableColumn
olTRTrafTopNInOctets = _OlTRTrafTopNInOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 9),
    _OlTRTrafTopNInOctets_Type()
)
olTRTrafTopNInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNInOctets.setStatus("mandatory")
_OlTRTrafTopNOutOctets_Type = Counter32
_OlTRTrafTopNOutOctets_Object = MibTableColumn
olTRTrafTopNOutOctets = _OlTRTrafTopNOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 10),
    _OlTRTrafTopNOutOctets_Type()
)
olTRTrafTopNOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNOutOctets.setStatus("mandatory")
_OlTRTrafTopNOutErrors_Type = Counter32
_OlTRTrafTopNOutErrors_Object = MibTableColumn
olTRTrafTopNOutErrors = _OlTRTrafTopNOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 11),
    _OlTRTrafTopNOutErrors_Type()
)
olTRTrafTopNOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNOutErrors.setStatus("mandatory")
_OlTRTrafTopNOutBroadcastFrames_Type = Counter32
_OlTRTrafTopNOutBroadcastFrames_Object = MibTableColumn
olTRTrafTopNOutBroadcastFrames = _OlTRTrafTopNOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 12),
    _OlTRTrafTopNOutBroadcastFrames_Type()
)
olTRTrafTopNOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNOutBroadcastFrames.setStatus("mandatory")
_OlTRTrafTopNOutMulticastFrames_Type = Counter32
_OlTRTrafTopNOutMulticastFrames_Object = MibTableColumn
olTRTrafTopNOutMulticastFrames = _OlTRTrafTopNOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 13),
    _OlTRTrafTopNOutMulticastFrames_Type()
)
olTRTrafTopNOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNOutMulticastFrames.setStatus("mandatory")
_OlTRTrafTopNSummaryTable_Object = MibTable
olTRTrafTopNSummaryTable = _OlTRTrafTopNSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11)
)
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryTable.setStatus("mandatory")
_OlTRTrafTopNSummaryEntry_Object = MibTableRow
olTRTrafTopNSummaryEntry = _OlTRTrafTopNSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11, 1)
)
olTRTrafTopNSummaryEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olTRTrafTopNSummaryNetID"),
    (0, "CHIPCOMMIB", "olTRTrafTopNSummaryStatistic"),
    (0, "CHIPCOMMIB", "olTRTrafTopNSummaryIndex"),
)
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryEntry.setStatus("mandatory")


class _OlTRTrafTopNSummaryNetID_Type(Integer32):
    """Custom type olTRTrafTopNSummaryNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafTopNSummaryNetID_Type.__name__ = "Integer32"
_OlTRTrafTopNSummaryNetID_Object = MibTableColumn
olTRTrafTopNSummaryNetID = _OlTRTrafTopNSummaryNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11, 1, 1),
    _OlTRTrafTopNSummaryNetID_Type()
)
olTRTrafTopNSummaryNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryNetID.setStatus("mandatory")


class _OlTRTrafTopNSummaryStatistic_Type(Integer32):
    """Custom type olTRTrafTopNSummaryStatistic based on Integer32"""
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
        *(("olTRTrafTopNSummaryInFrames", 1),
          ("olTRTrafTopNSummaryInOctets", 3),
          ("olTRTrafTopNSummaryOutBroadcastFrames", 6),
          ("olTRTrafTopNSummaryOutErrors", 5),
          ("olTRTrafTopNSummaryOutFrames", 2),
          ("olTRTrafTopNSummaryOutMulticastFrames", 7),
          ("olTRTrafTopNSummaryOutOctets", 4))
    )


_OlTRTrafTopNSummaryStatistic_Type.__name__ = "Integer32"
_OlTRTrafTopNSummaryStatistic_Object = MibTableColumn
olTRTrafTopNSummaryStatistic = _OlTRTrafTopNSummaryStatistic_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11, 1, 2),
    _OlTRTrafTopNSummaryStatistic_Type()
)
olTRTrafTopNSummaryStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryStatistic.setStatus("mandatory")
_OlTRTrafTopNSummaryIndex_Type = Integer32
_OlTRTrafTopNSummaryIndex_Object = MibTableColumn
olTRTrafTopNSummaryIndex = _OlTRTrafTopNSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11, 1, 3),
    _OlTRTrafTopNSummaryIndex_Type()
)
olTRTrafTopNSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryIndex.setStatus("mandatory")
_OlTRTrafTopNSummaryStations_Type = OctetString
_OlTRTrafTopNSummaryStations_Object = MibTableColumn
olTRTrafTopNSummaryStations = _OlTRTrafTopNSummaryStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11, 1, 4),
    _OlTRTrafTopNSummaryStations_Type()
)
olTRTrafTopNSummaryStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryStations.setStatus("mandatory")
_OlFDDInet_ObjectIdentity = ObjectIdentity
olFDDInet = _OlFDDInet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4)
)
_OlFDDIStatsModTable_Object = MibTable
olFDDIStatsModTable = _OlFDDIStatsModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    olFDDIStatsModTable.setStatus("mandatory")
_OlFDDIStatsModEntry_Object = MibTableRow
olFDDIStatsModEntry = _OlFDDIStatsModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1)
)
olFDDIStatsModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olFDDIStatsModSlotIndex"),
)
if mibBuilder.loadTexts:
    olFDDIStatsModEntry.setStatus("mandatory")
_OlFDDIStatsModSlotIndex_Type = Integer32
_OlFDDIStatsModSlotIndex_Object = MibTableColumn
olFDDIStatsModSlotIndex = _OlFDDIStatsModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1, 1),
    _OlFDDIStatsModSlotIndex_Type()
)
olFDDIStatsModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsModSlotIndex.setStatus("mandatory")
_OlFDDIStatsModMgtRcvErrs_Type = Counter32
_OlFDDIStatsModMgtRcvErrs_Object = MibTableColumn
olFDDIStatsModMgtRcvErrs = _OlFDDIStatsModMgtRcvErrs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1, 2),
    _OlFDDIStatsModMgtRcvErrs_Type()
)
olFDDIStatsModMgtRcvErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsModMgtRcvErrs.setStatus("mandatory")
_OlFDDIStatsModMgtXmitErrs_Type = Counter32
_OlFDDIStatsModMgtXmitErrs_Object = MibTableColumn
olFDDIStatsModMgtXmitErrs = _OlFDDIStatsModMgtXmitErrs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1, 3),
    _OlFDDIStatsModMgtXmitErrs_Type()
)
olFDDIStatsModMgtXmitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsModMgtXmitErrs.setStatus("mandatory")
_OlFDDIStatsModBackplaneErrs_Type = Counter32
_OlFDDIStatsModBackplaneErrs_Object = MibTableColumn
olFDDIStatsModBackplaneErrs = _OlFDDIStatsModBackplaneErrs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1, 4),
    _OlFDDIStatsModBackplaneErrs_Type()
)
olFDDIStatsModBackplaneErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsModBackplaneErrs.setStatus("mandatory")
_OlFDDIStatsModPllUnlockErrs_Type = Counter32
_OlFDDIStatsModPllUnlockErrs_Object = MibTableColumn
olFDDIStatsModPllUnlockErrs = _OlFDDIStatsModPllUnlockErrs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1, 5),
    _OlFDDIStatsModPllUnlockErrs_Type()
)
olFDDIStatsModPllUnlockErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsModPllUnlockErrs.setStatus("mandatory")
_OlFDDIStatsPortTable_Object = MibTable
olFDDIStatsPortTable = _OlFDDIStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3)
)
if mibBuilder.loadTexts:
    olFDDIStatsPortTable.setStatus("mandatory")
_OlFDDIStatsPortEntry_Object = MibTableRow
olFDDIStatsPortEntry = _OlFDDIStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1)
)
olFDDIStatsPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olFDDIStatsPortSlotIndex"),
    (0, "CHIPCOMMIB", "olFDDIStatsPortIndex"),
)
if mibBuilder.loadTexts:
    olFDDIStatsPortEntry.setStatus("mandatory")
_OlFDDIStatsPortSlotIndex_Type = Integer32
_OlFDDIStatsPortSlotIndex_Object = MibTableColumn
olFDDIStatsPortSlotIndex = _OlFDDIStatsPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 1),
    _OlFDDIStatsPortSlotIndex_Type()
)
olFDDIStatsPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortSlotIndex.setStatus("mandatory")
_OlFDDIStatsPortIndex_Type = Integer32
_OlFDDIStatsPortIndex_Object = MibTableColumn
olFDDIStatsPortIndex = _OlFDDIStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 2),
    _OlFDDIStatsPortIndex_Type()
)
olFDDIStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortIndex.setStatus("mandatory")
_OlFDDIStatsPortLCTFailCts_Type = Counter32
_OlFDDIStatsPortLCTFailCts_Object = MibTableColumn
olFDDIStatsPortLCTFailCts = _OlFDDIStatsPortLCTFailCts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 3),
    _OlFDDIStatsPortLCTFailCts_Type()
)
olFDDIStatsPortLCTFailCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortLCTFailCts.setStatus("mandatory")
_OlFDDIStatsPortLerEstimate_Type = Integer32
_OlFDDIStatsPortLerEstimate_Object = MibTableColumn
olFDDIStatsPortLerEstimate = _OlFDDIStatsPortLerEstimate_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 4),
    _OlFDDIStatsPortLerEstimate_Type()
)
olFDDIStatsPortLerEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortLerEstimate.setStatus("mandatory")
_OlFDDIStatsPortLemRejectCts_Type = Counter32
_OlFDDIStatsPortLemRejectCts_Object = MibTableColumn
olFDDIStatsPortLemRejectCts = _OlFDDIStatsPortLemRejectCts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 5),
    _OlFDDIStatsPortLemRejectCts_Type()
)
olFDDIStatsPortLemRejectCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortLemRejectCts.setStatus("mandatory")
_OlFDDIStatsPortLemCts_Type = Counter32
_OlFDDIStatsPortLemCts_Object = MibTableColumn
olFDDIStatsPortLemCts = _OlFDDIStatsPortLemCts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 6),
    _OlFDDIStatsPortLemCts_Type()
)
olFDDIStatsPortLemCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortLemCts.setStatus("mandatory")
_OlFDDInetStatsTable_Object = MibTable
olFDDInetStatsTable = _OlFDDInetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4)
)
if mibBuilder.loadTexts:
    olFDDInetStatsTable.setStatus("mandatory")
_OlFDDInetStatsEntry_Object = MibTableRow
olFDDInetStatsEntry = _OlFDDInetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1)
)
olFDDInetStatsEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olFDDInetStatsNetID"),
)
if mibBuilder.loadTexts:
    olFDDInetStatsEntry.setStatus("mandatory")


class _OlFDDInetStatsNetID_Type(Integer32):
    """Custom type olFDDInetStatsNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("fddi-1", 16),
          ("fddi-2", 17),
          ("fddi-3", 18),
          ("fddi-4", 19),
          ("isolated", 2))
    )


_OlFDDInetStatsNetID_Type.__name__ = "Integer32"
_OlFDDInetStatsNetID_Object = MibTableColumn
olFDDInetStatsNetID = _OlFDDInetStatsNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 1),
    _OlFDDInetStatsNetID_Type()
)
olFDDInetStatsNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsNetID.setStatus("mandatory")
_OlFDDInetStatsRingOpCounts_Type = Counter32
_OlFDDInetStatsRingOpCounts_Object = MibTableColumn
olFDDInetStatsRingOpCounts = _OlFDDInetStatsRingOpCounts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 2),
    _OlFDDInetStatsRingOpCounts_Type()
)
olFDDInetStatsRingOpCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsRingOpCounts.setStatus("mandatory")
_OlFDDInetStatsFrameCounts_Type = Counter32
_OlFDDInetStatsFrameCounts_Object = MibTableColumn
olFDDInetStatsFrameCounts = _OlFDDInetStatsFrameCounts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 3),
    _OlFDDInetStatsFrameCounts_Type()
)
olFDDInetStatsFrameCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsFrameCounts.setStatus("mandatory")
_OlFDDInetStatsErrorCounts_Type = Counter32
_OlFDDInetStatsErrorCounts_Object = MibTableColumn
olFDDInetStatsErrorCounts = _OlFDDInetStatsErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 4),
    _OlFDDInetStatsErrorCounts_Type()
)
olFDDInetStatsErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsErrorCounts.setStatus("mandatory")
_OlFDDInetStatsLostCounts_Type = Counter32
_OlFDDInetStatsLostCounts_Object = MibTableColumn
olFDDInetStatsLostCounts = _OlFDDInetStatsLostCounts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 5),
    _OlFDDInetStatsLostCounts_Type()
)
olFDDInetStatsLostCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsLostCounts.setStatus("mandatory")


class _OlFDDInetStatsFrameErrorRatio_Type(Integer32):
    """Custom type olFDDInetStatsFrameErrorRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OlFDDInetStatsFrameErrorRatio_Type.__name__ = "Integer32"
_OlFDDInetStatsFrameErrorRatio_Object = MibTableColumn
olFDDInetStatsFrameErrorRatio = _OlFDDInetStatsFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 6),
    _OlFDDInetStatsFrameErrorRatio_Type()
)
olFDDInetStatsFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsFrameErrorRatio.setStatus("mandatory")
_OlGroups_ObjectIdentity = ObjectIdentity
olGroups = _OlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6)
)
_OlGroupPortTable_Object = MibTable
olGroupPortTable = _OlGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    olGroupPortTable.setStatus("mandatory")
_OlGroupPortEntry_Object = MibTableRow
olGroupPortEntry = _OlGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 1, 1)
)
olGroupPortEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olGroupPortSlotIndex"),
    (0, "CHIPCOMMIB", "olGroupPortIndex"),
)
if mibBuilder.loadTexts:
    olGroupPortEntry.setStatus("mandatory")
_OlGroupPortSlotIndex_Type = Integer32
_OlGroupPortSlotIndex_Object = MibTableColumn
olGroupPortSlotIndex = _OlGroupPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 1, 1, 1),
    _OlGroupPortSlotIndex_Type()
)
olGroupPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupPortSlotIndex.setStatus("mandatory")
_OlGroupPortIndex_Type = Integer32
_OlGroupPortIndex_Object = MibTableColumn
olGroupPortIndex = _OlGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 1, 1, 2),
    _OlGroupPortIndex_Type()
)
olGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupPortIndex.setStatus("mandatory")


class _OlGroupPortGroupID_Type(OctetString):
    """Custom type olGroupPortGroupID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OlGroupPortGroupID_Type.__name__ = "OctetString"
_OlGroupPortGroupID_Object = MibTableColumn
olGroupPortGroupID = _OlGroupPortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 1, 1, 3),
    _OlGroupPortGroupID_Type()
)
olGroupPortGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupPortGroupID.setStatus("mandatory")
_OlGroupSummaryTable_Object = MibTable
olGroupSummaryTable = _OlGroupSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    olGroupSummaryTable.setStatus("mandatory")
_OlGroupSummaryEntry_Object = MibTableRow
olGroupSummaryEntry = _OlGroupSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 2, 1)
)
olGroupSummaryEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olGroupSummaryGroupID"),
    (0, "CHIPCOMMIB", "olGroupSummaryIndex"),
)
if mibBuilder.loadTexts:
    olGroupSummaryEntry.setStatus("mandatory")


class _OlGroupSummaryGroupID_Type(Integer32):
    """Custom type olGroupSummaryGroupID based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("group-1", 1),
          ("group-2", 2),
          ("group-3", 3),
          ("group-4", 4),
          ("group-5", 5),
          ("group-6", 6),
          ("group-7", 7),
          ("group-8", 8))
    )


_OlGroupSummaryGroupID_Type.__name__ = "Integer32"
_OlGroupSummaryGroupID_Object = MibTableColumn
olGroupSummaryGroupID = _OlGroupSummaryGroupID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 2, 1, 1),
    _OlGroupSummaryGroupID_Type()
)
olGroupSummaryGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupSummaryGroupID.setStatus("mandatory")
_OlGroupSummaryIndex_Type = Integer32
_OlGroupSummaryIndex_Object = MibTableColumn
olGroupSummaryIndex = _OlGroupSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 2, 1, 2),
    _OlGroupSummaryIndex_Type()
)
olGroupSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupSummaryIndex.setStatus("mandatory")


class _OlGroupSummaryPorts_Type(OctetString):
    """Custom type olGroupSummaryPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_OlGroupSummaryPorts_Type.__name__ = "OctetString"
_OlGroupSummaryPorts_Object = MibTableColumn
olGroupSummaryPorts = _OlGroupSummaryPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 2, 1, 3),
    _OlGroupSummaryPorts_Type()
)
olGroupSummaryPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupSummaryPorts.setStatus("mandatory")
_OlGroupSet_ObjectIdentity = ObjectIdentity
olGroupSet = _OlGroupSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3)
)


class _OlGroupSetAction_Type(Integer32):
    """Custom type olGroupSetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add-ports", 1),
          ("clear-ports", 2),
          ("set-admin-state", 3))
    )


_OlGroupSetAction_Type.__name__ = "Integer32"
_OlGroupSetAction_Object = MibScalar
olGroupSetAction = _OlGroupSetAction_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3, 1),
    _OlGroupSetAction_Type()
)
olGroupSetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupSetAction.setStatus("mandatory")


class _OlGroupSetGroupID_Type(Integer32):
    """Custom type olGroupSetGroupID based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("all-groups", 255),
          ("group-1", 1),
          ("group-2", 2),
          ("group-3", 3),
          ("group-4", 4),
          ("group-5", 5),
          ("group-6", 6),
          ("group-7", 7),
          ("group-8", 8))
    )


_OlGroupSetGroupID_Type.__name__ = "Integer32"
_OlGroupSetGroupID_Object = MibScalar
olGroupSetGroupID = _OlGroupSetGroupID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3, 2),
    _OlGroupSetGroupID_Type()
)
olGroupSetGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupSetGroupID.setStatus("mandatory")
_OlGroupSetSlotIndex_Type = Integer32
_OlGroupSetSlotIndex_Object = MibScalar
olGroupSetSlotIndex = _OlGroupSetSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3, 3),
    _OlGroupSetSlotIndex_Type()
)
olGroupSetSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupSetSlotIndex.setStatus("mandatory")
_OlGroupSetPortIndex_Type = Integer32
_OlGroupSetPortIndex_Object = MibScalar
olGroupSetPortIndex = _OlGroupSetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3, 4),
    _OlGroupSetPortIndex_Type()
)
olGroupSetPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupSetPortIndex.setStatus("mandatory")


class _OlGroupSetAdminState_Type(Integer32):
    """Custom type olGroupSetAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OlGroupSetAdminState_Type.__name__ = "Integer32"
_OlGroupSetAdminState_Object = MibScalar
olGroupSetAdminState = _OlGroupSetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3, 5),
    _OlGroupSetAdminState_Type()
)
olGroupSetAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupSetAdminState.setStatus("mandatory")
_OlAlarm_ObjectIdentity = ObjectIdentity
olAlarm = _OlAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7)
)
_OlThresh_ObjectIdentity = ObjectIdentity
olThresh = _OlThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1)
)
_OlThreshControl_ObjectIdentity = ObjectIdentity
olThreshControl = _OlThreshControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1)
)
_OlThreshTotalEntries_Type = Integer32
_OlThreshTotalEntries_Object = MibScalar
olThreshTotalEntries = _OlThreshTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1, 1),
    _OlThreshTotalEntries_Type()
)
olThreshTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshTotalEntries.setStatus("mandatory")
_OlThreshMaxEntries_Type = Integer32
_OlThreshMaxEntries_Object = MibScalar
olThreshMaxEntries = _OlThreshMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1, 2),
    _OlThreshMaxEntries_Type()
)
olThreshMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshMaxEntries.setStatus("mandatory")
_OlThreshLastCreatedIndex_Type = Integer32
_OlThreshLastCreatedIndex_Object = MibScalar
olThreshLastCreatedIndex = _OlThreshLastCreatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1, 3),
    _OlThreshLastCreatedIndex_Type()
)
olThreshLastCreatedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshLastCreatedIndex.setStatus("mandatory")


class _OlThreshAllMode_Type(Integer32):
    """Custom type olThreshAllMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OlThreshAllMode_Type.__name__ = "Integer32"
_OlThreshAllMode_Object = MibScalar
olThreshAllMode = _OlThreshAllMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1, 4),
    _OlThreshAllMode_Type()
)
olThreshAllMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshAllMode.setStatus("mandatory")
_OlThreshTable_Object = MibTable
olThreshTable = _OlThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    olThreshTable.setStatus("mandatory")
_OlThreshEntry_Object = MibTableRow
olThreshEntry = _OlThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1)
)
olThreshEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olThreshIndex"),
)
if mibBuilder.loadTexts:
    olThreshEntry.setStatus("mandatory")
_OlThreshIndex_Type = Integer32
_OlThreshIndex_Object = MibTableColumn
olThreshIndex = _OlThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 1),
    _OlThreshIndex_Type()
)
olThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshIndex.setStatus("mandatory")


class _OlThreshMode_Type(Integer32):
    """Custom type olThreshMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OlThreshMode_Type.__name__ = "Integer32"
_OlThreshMode_Object = MibTableColumn
olThreshMode = _OlThreshMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 2),
    _OlThreshMode_Type()
)
olThreshMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshMode.setStatus("mandatory")


class _OlThreshDescription_Type(DisplayString):
    """Custom type olThreshDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_OlThreshDescription_Type.__name__ = "DisplayString"
_OlThreshDescription_Object = MibTableColumn
olThreshDescription = _OlThreshDescription_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 3),
    _OlThreshDescription_Type()
)
olThreshDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshDescription.setStatus("mandatory")
_OlThreshObjectIdentifier_Type = ObjectIdentifier
_OlThreshObjectIdentifier_Object = MibTableColumn
olThreshObjectIdentifier = _OlThreshObjectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 4),
    _OlThreshObjectIdentifier_Type()
)
olThreshObjectIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshObjectIdentifier.setStatus("mandatory")


class _OlThreshStatCategory_Type(Integer32):
    """Custom type olThreshStatCategory based on Integer32"""
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
        *(("network", 2),
          ("other", 1),
          ("port", 3),
          ("station", 4))
    )


_OlThreshStatCategory_Type.__name__ = "Integer32"
_OlThreshStatCategory_Object = MibTableColumn
olThreshStatCategory = _OlThreshStatCategory_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 5),
    _OlThreshStatCategory_Type()
)
olThreshStatCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatCategory.setStatus("mandatory")


class _OlThreshStatType_Type(Integer32):
    """Custom type olThreshStatType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("broadcast-frames", 4),
          ("error-frames", 6),
          ("frames", 2),
          ("multicast-frames", 5),
          ("octets", 3),
          ("other", 1),
          ("tr-net-hard-errors", 8),
          ("tr-net-soft-errors", 7))
    )


_OlThreshStatType_Type.__name__ = "Integer32"
_OlThreshStatType_Object = MibTableColumn
olThreshStatType = _OlThreshStatType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 6),
    _OlThreshStatType_Type()
)
olThreshStatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatType.setStatus("mandatory")


class _OlThreshStatNetID_Type(Integer32):
    """Custom type olThreshStatNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              255)
        )
    )
    namedValues = NamedValues(
        *(("agent-network", 255),
          ("isolated", 2),
          ("other", 1),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlThreshStatNetID_Type.__name__ = "Integer32"
_OlThreshStatNetID_Object = MibTableColumn
olThreshStatNetID = _OlThreshStatNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 7),
    _OlThreshStatNetID_Type()
)
olThreshStatNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatNetID.setStatus("mandatory")
_OlThreshStatSlotIndex_Type = Integer32
_OlThreshStatSlotIndex_Object = MibTableColumn
olThreshStatSlotIndex = _OlThreshStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 8),
    _OlThreshStatSlotIndex_Type()
)
olThreshStatSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatSlotIndex.setStatus("mandatory")
_OlThreshStatPortIndex_Type = Integer32
_OlThreshStatPortIndex_Object = MibTableColumn
olThreshStatPortIndex = _OlThreshStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 9),
    _OlThreshStatPortIndex_Type()
)
olThreshStatPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatPortIndex.setStatus("mandatory")
_OlThreshStatStationAddr_Type = MacAddress
_OlThreshStatStationAddr_Object = MibTableColumn
olThreshStatStationAddr = _OlThreshStatStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 10),
    _OlThreshStatStationAddr_Type()
)
olThreshStatStationAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatStationAddr.setStatus("mandatory")
_OlThreshInterval_Type = Integer32
_OlThreshInterval_Object = MibTableColumn
olThreshInterval = _OlThreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 11),
    _OlThreshInterval_Type()
)
olThreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshInterval.setStatus("mandatory")


class _OlThreshCondition_Type(Integer32):
    """Custom type olThreshCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delta-above", 1)
    )


_OlThreshCondition_Type.__name__ = "Integer32"
_OlThreshCondition_Object = MibTableColumn
olThreshCondition = _OlThreshCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 12),
    _OlThreshCondition_Type()
)
olThreshCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshCondition.setStatus("mandatory")
_OlThreshValue_Type = Integer32
_OlThreshValue_Object = MibTableColumn
olThreshValue = _OlThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 13),
    _OlThreshValue_Type()
)
olThreshValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshValue.setStatus("mandatory")
_OlThreshCurrentValue_Type = Integer32
_OlThreshCurrentValue_Object = MibTableColumn
olThreshCurrentValue = _OlThreshCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 14),
    _OlThreshCurrentValue_Type()
)
olThreshCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshCurrentValue.setStatus("mandatory")


class _OlThreshStatus_Type(Integer32):
    """Custom type olThreshStatus based on Integer32"""
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
        *(("no-statistic-specified", 1),
          ("not-yet-available", 3),
          ("statistic-not-accessible", 2),
          ("valid", 4))
    )


_OlThreshStatus_Type.__name__ = "Integer32"
_OlThreshStatus_Object = MibTableColumn
olThreshStatus = _OlThreshStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 15),
    _OlThreshStatus_Type()
)
olThreshStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshStatus.setStatus("mandatory")
_OlThreshTimeSinceLastTriggered_Type = TimeTicks
_OlThreshTimeSinceLastTriggered_Object = MibTableColumn
olThreshTimeSinceLastTriggered = _OlThreshTimeSinceLastTriggered_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 16),
    _OlThreshTimeSinceLastTriggered_Type()
)
olThreshTimeSinceLastTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshTimeSinceLastTriggered.setStatus("mandatory")


class _OlThreshActionType_Type(Integer32):
    """Custom type olThreshActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("run-script-only", 2),
          ("trap-only", 1),
          ("trap-run-script", 3))
    )


_OlThreshActionType_Type.__name__ = "Integer32"
_OlThreshActionType_Object = MibTableColumn
olThreshActionType = _OlThreshActionType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 17),
    _OlThreshActionType_Type()
)
olThreshActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshActionType.setStatus("mandatory")
_OlThreshActionData_Type = Integer32
_OlThreshActionData_Object = MibTableColumn
olThreshActionData = _OlThreshActionData_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 18),
    _OlThreshActionData_Type()
)
olThreshActionData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshActionData.setStatus("mandatory")


class _OlThreshActionPriority_Type(Integer32):
    """Custom type olThreshActionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_OlThreshActionPriority_Type.__name__ = "Integer32"
_OlThreshActionPriority_Object = MibTableColumn
olThreshActionPriority = _OlThreshActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 19),
    _OlThreshActionPriority_Type()
)
olThreshActionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshActionPriority.setStatus("mandatory")
_OcPower_ObjectIdentity = ObjectIdentity
ocPower = _OcPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8)
)
_OcPowerControl_ObjectIdentity = ObjectIdentity
ocPowerControl = _OcPowerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 1)
)


class _OcPowerModeAdminStatus_Type(Integer32):
    """Custom type ocPowerModeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault-tolerant", 1),
          ("not-fault-tolerant", 2))
    )


_OcPowerModeAdminStatus_Type.__name__ = "Integer32"
_OcPowerModeAdminStatus_Object = MibScalar
ocPowerModeAdminStatus = _OcPowerModeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 1, 1),
    _OcPowerModeAdminStatus_Type()
)
ocPowerModeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocPowerModeAdminStatus.setStatus("mandatory")


class _OcPowerModeOperStatus_Type(Integer32):
    """Custom type ocPowerModeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault-tolerant", 1),
          ("not-fault-tolerant", 2))
    )


_OcPowerModeOperStatus_Type.__name__ = "Integer32"
_OcPowerModeOperStatus_Object = MibScalar
ocPowerModeOperStatus = _OcPowerModeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 1, 2),
    _OcPowerModeOperStatus_Type()
)
ocPowerModeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocPowerModeOperStatus.setStatus("mandatory")


class _OcPowerOverheatPowerDownMode_Type(Integer32):
    """Custom type ocPowerOverheatPowerDownMode based on Integer32"""
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


_OcPowerOverheatPowerDownMode_Type.__name__ = "Integer32"
_OcPowerOverheatPowerDownMode_Object = MibScalar
ocPowerOverheatPowerDownMode = _OcPowerOverheatPowerDownMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 1, 3),
    _OcPowerOverheatPowerDownMode_Type()
)
ocPowerOverheatPowerDownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocPowerOverheatPowerDownMode.setStatus("mandatory")
_OcPowerOutputTable_Object = MibTable
ocPowerOutputTable = _OcPowerOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ocPowerOutputTable.setStatus("mandatory")
_OcPowerOutputEntry_Object = MibTableRow
ocPowerOutputEntry = _OcPowerOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 2, 1)
)
ocPowerOutputEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ocPowerOutputType"),
)
if mibBuilder.loadTexts:
    ocPowerOutputEntry.setStatus("mandatory")


class _OcPowerOutputType_Type(Integer32):
    """Custom type ocPowerOutputType based on Integer32"""
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
        *(("minusFiveVolt", 2),
          ("minusTwelveVolt", 4),
          ("plusFiveVolt", 1),
          ("plusTwelveVolt", 3),
          ("plusTwoVolt", 5))
    )


_OcPowerOutputType_Type.__name__ = "Integer32"
_OcPowerOutputType_Object = MibTableColumn
ocPowerOutputType = _OcPowerOutputType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 2, 1, 1),
    _OcPowerOutputType_Type()
)
ocPowerOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocPowerOutputType.setStatus("mandatory")
_OcPowerOutputVoltageLevel_Type = Gauge32
_OcPowerOutputVoltageLevel_Object = MibTableColumn
ocPowerOutputVoltageLevel = _OcPowerOutputVoltageLevel_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 2, 1, 2),
    _OcPowerOutputVoltageLevel_Type()
)
ocPowerOutputVoltageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocPowerOutputVoltageLevel.setStatus("mandatory")
_OcPowerOutputWattageCapacity_Type = Gauge32
_OcPowerOutputWattageCapacity_Object = MibTableColumn
ocPowerOutputWattageCapacity = _OcPowerOutputWattageCapacity_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 2, 1, 3),
    _OcPowerOutputWattageCapacity_Type()
)
ocPowerOutputWattageCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocPowerOutputWattageCapacity.setStatus("mandatory")
_OcPowerOutputWattageConsumed_Type = Gauge32
_OcPowerOutputWattageConsumed_Object = MibTableColumn
ocPowerOutputWattageConsumed = _OcPowerOutputWattageConsumed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 2, 1, 4),
    _OcPowerOutputWattageConsumed_Type()
)
ocPowerOutputWattageConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocPowerOutputWattageConsumed.setStatus("mandatory")
_OcPowerOutputWattageAvailable_Type = Gauge32
_OcPowerOutputWattageAvailable_Object = MibTableColumn
ocPowerOutputWattageAvailable = _OcPowerOutputWattageAvailable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 2, 1, 5),
    _OcPowerOutputWattageAvailable_Type()
)
ocPowerOutputWattageAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocPowerOutputWattageAvailable.setStatus("mandatory")
_OcPowerOutputUnmanagedWattageAlloc_Type = Gauge32
_OcPowerOutputUnmanagedWattageAlloc_Object = MibTableColumn
ocPowerOutputUnmanagedWattageAlloc = _OcPowerOutputUnmanagedWattageAlloc_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 2, 1, 6),
    _OcPowerOutputUnmanagedWattageAlloc_Type()
)
ocPowerOutputUnmanagedWattageAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocPowerOutputUnmanagedWattageAlloc.setStatus("mandatory")
_OcPowerSlotTable_Object = MibTable
ocPowerSlotTable = _OcPowerSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 3)
)
if mibBuilder.loadTexts:
    ocPowerSlotTable.setStatus("mandatory")
_OcPowerSlotEntry_Object = MibTableRow
ocPowerSlotEntry = _OcPowerSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 3, 1)
)
ocPowerSlotEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ocPowerSlotIndex"),
)
if mibBuilder.loadTexts:
    ocPowerSlotEntry.setStatus("mandatory")
_OcPowerSlotIndex_Type = Integer32
_OcPowerSlotIndex_Object = MibTableColumn
ocPowerSlotIndex = _OcPowerSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 3, 1, 1),
    _OcPowerSlotIndex_Type()
)
ocPowerSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocPowerSlotIndex.setStatus("mandatory")


class _OcPowerSlotClass_Type(Integer32):
    """Custom type ocPowerSlotClass based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("nine", 9),
          ("not-applicable", 11),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("ten", 10),
          ("three", 3),
          ("two", 2))
    )


_OcPowerSlotClass_Type.__name__ = "Integer32"
_OcPowerSlotClass_Object = MibTableColumn
ocPowerSlotClass = _OcPowerSlotClass_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 3, 1, 2),
    _OcPowerSlotClass_Type()
)
ocPowerSlotClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocPowerSlotClass.setStatus("mandatory")


class _OcPowerSlotAdminStatus_Type(Integer32):
    """Custom type ocPowerSlotAdminStatus based on Integer32"""
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


_OcPowerSlotAdminStatus_Type.__name__ = "Integer32"
_OcPowerSlotAdminStatus_Object = MibTableColumn
ocPowerSlotAdminStatus = _OcPowerSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 3, 1, 3),
    _OcPowerSlotAdminStatus_Type()
)
ocPowerSlotAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocPowerSlotAdminStatus.setStatus("mandatory")


class _OcPowerSlotOperStatus_Type(Integer32):
    """Custom type ocPowerSlotOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("enabled-always", 4),
          ("insufficient-power", 3))
    )


_OcPowerSlotOperStatus_Type.__name__ = "Integer32"
_OcPowerSlotOperStatus_Object = MibTableColumn
ocPowerSlotOperStatus = _OcPowerSlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 8, 3, 1, 4),
    _OcPowerSlotOperStatus_Type()
)
ocPowerSlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocPowerSlotOperStatus.setStatus("mandatory")
_OcInventory_ObjectIdentity = ObjectIdentity
ocInventory = _OcInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9)
)
_OcInvHub_ObjectIdentity = ObjectIdentity
ocInvHub = _OcInvHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 1)
)


class _OcInvHubType_Type(DisplayString):
    """Custom type ocInvHubType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcInvHubType_Type.__name__ = "DisplayString"
_OcInvHubType_Object = MibScalar
ocInvHubType = _OcInvHubType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 1, 1),
    _OcInvHubType_Type()
)
ocInvHubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvHubType.setStatus("mandatory")


class _OcInvHubSerialNo_Type(DisplayString):
    """Custom type ocInvHubSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcInvHubSerialNo_Type.__name__ = "DisplayString"
_OcInvHubSerialNo_Object = MibScalar
ocInvHubSerialNo = _OcInvHubSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 1, 2),
    _OcInvHubSerialNo_Type()
)
ocInvHubSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvHubSerialNo.setStatus("mandatory")


class _OcInvHubHWVer_Type(DisplayString):
    """Custom type ocInvHubHWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcInvHubHWVer_Type.__name__ = "DisplayString"
_OcInvHubHWVer_Object = MibScalar
ocInvHubHWVer = _OcInvHubHWVer_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 1, 3),
    _OcInvHubHWVer_Type()
)
ocInvHubHWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvHubHWVer.setStatus("mandatory")


class _OcInvHubMfr_Type(DisplayString):
    """Custom type ocInvHubMfr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcInvHubMfr_Type.__name__ = "DisplayString"
_OcInvHubMfr_Object = MibScalar
ocInvHubMfr = _OcInvHubMfr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 1, 4),
    _OcInvHubMfr_Type()
)
ocInvHubMfr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvHubMfr.setStatus("mandatory")


class _OcInvHubMfrDate_Type(DisplayString):
    """Custom type ocInvHubMfrDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OcInvHubMfrDate_Type.__name__ = "DisplayString"
_OcInvHubMfrDate_Object = MibScalar
ocInvHubMfrDate = _OcInvHubMfrDate_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 1, 5),
    _OcInvHubMfrDate_Type()
)
ocInvHubMfrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvHubMfrDate.setStatus("mandatory")
_OcInvMods_ObjectIdentity = ObjectIdentity
ocInvMods = _OcInvMods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2)
)
_OcInvModTable_Object = MibTable
ocInvModTable = _OcInvModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    ocInvModTable.setStatus("mandatory")
_OcInvModEntry_Object = MibTableRow
ocInvModEntry = _OcInvModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1, 1)
)
ocInvModEntry.setIndexNames(
    (0, "CHIPCOMMIB", "ocInvModSlotIndex"),
    (0, "CHIPCOMMIB", "ocInvModSubSlotIndex"),
)
if mibBuilder.loadTexts:
    ocInvModEntry.setStatus("mandatory")
_OcInvModSlotIndex_Type = Integer32
_OcInvModSlotIndex_Object = MibTableColumn
ocInvModSlotIndex = _OcInvModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1, 1, 1),
    _OcInvModSlotIndex_Type()
)
ocInvModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvModSlotIndex.setStatus("mandatory")
_OcInvModSubSlotIndex_Type = Integer32
_OcInvModSubSlotIndex_Object = MibTableColumn
ocInvModSubSlotIndex = _OcInvModSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1, 1, 2),
    _OcInvModSubSlotIndex_Type()
)
ocInvModSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvModSubSlotIndex.setStatus("mandatory")


class _OcInvModModel_Type(DisplayString):
    """Custom type ocInvModModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcInvModModel_Type.__name__ = "DisplayString"
_OcInvModModel_Object = MibTableColumn
ocInvModModel = _OcInvModModel_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1, 1, 3),
    _OcInvModModel_Type()
)
ocInvModModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvModModel.setStatus("mandatory")


class _OcInvModSerialNo_Type(DisplayString):
    """Custom type ocInvModSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcInvModSerialNo_Type.__name__ = "DisplayString"
_OcInvModSerialNo_Object = MibTableColumn
ocInvModSerialNo = _OcInvModSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1, 1, 4),
    _OcInvModSerialNo_Type()
)
ocInvModSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvModSerialNo.setStatus("mandatory")


class _OcInvModHWVer_Type(DisplayString):
    """Custom type ocInvModHWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcInvModHWVer_Type.__name__ = "DisplayString"
_OcInvModHWVer_Object = MibTableColumn
ocInvModHWVer = _OcInvModHWVer_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1, 1, 5),
    _OcInvModHWVer_Type()
)
ocInvModHWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvModHWVer.setStatus("mandatory")


class _OcInvModSWVer_Type(DisplayString):
    """Custom type ocInvModSWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcInvModSWVer_Type.__name__ = "DisplayString"
_OcInvModSWVer_Object = MibTableColumn
ocInvModSWVer = _OcInvModSWVer_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1, 1, 6),
    _OcInvModSWVer_Type()
)
ocInvModSWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvModSWVer.setStatus("mandatory")


class _OcInvModSWBootVer_Type(DisplayString):
    """Custom type ocInvModSWBootVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcInvModSWBootVer_Type.__name__ = "DisplayString"
_OcInvModSWBootVer_Object = MibTableColumn
ocInvModSWBootVer = _OcInvModSWBootVer_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1, 1, 7),
    _OcInvModSWBootVer_Type()
)
ocInvModSWBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvModSWBootVer.setStatus("mandatory")


class _OcInvModMfr_Type(DisplayString):
    """Custom type ocInvModMfr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OcInvModMfr_Type.__name__ = "DisplayString"
_OcInvModMfr_Object = MibTableColumn
ocInvModMfr = _OcInvModMfr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1, 1, 8),
    _OcInvModMfr_Type()
)
ocInvModMfr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvModMfr.setStatus("mandatory")


class _OcInvModMfrDate_Type(DisplayString):
    """Custom type ocInvModMfrDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OcInvModMfrDate_Type.__name__ = "DisplayString"
_OcInvModMfrDate_Object = MibTableColumn
ocInvModMfrDate = _OcInvModMfrDate_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 9, 2, 1, 1, 9),
    _OcInvModMfrDate_Type()
)
ocInvModMfrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocInvModMfrDate.setStatus("mandatory")
_OlPS2_ObjectIdentity = ObjectIdentity
olPS2 = _OlPS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11)
)
_OlPS2Info_ObjectIdentity = ObjectIdentity
olPS2Info = _OlPS2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 1)
)


class _OlPS2OperatingSystem_Type(DisplayString):
    """Custom type olPS2OperatingSystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlPS2OperatingSystem_Type.__name__ = "DisplayString"
_OlPS2OperatingSystem_Object = MibScalar
olPS2OperatingSystem = _OlPS2OperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 1, 1),
    _OlPS2OperatingSystem_Type()
)
olPS2OperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPS2OperatingSystem.setStatus("mandatory")


class _OlPS2FixedDiskSize_Type(DisplayString):
    """Custom type olPS2FixedDiskSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlPS2FixedDiskSize_Type.__name__ = "DisplayString"
_OlPS2FixedDiskSize_Object = MibScalar
olPS2FixedDiskSize = _OlPS2FixedDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 1, 2),
    _OlPS2FixedDiskSize_Type()
)
olPS2FixedDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPS2FixedDiskSize.setStatus("mandatory")


class _OlPS2RamSize_Type(DisplayString):
    """Custom type olPS2RamSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlPS2RamSize_Type.__name__ = "DisplayString"
_OlPS2RamSize_Object = MibScalar
olPS2RamSize = _OlPS2RamSize_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 1, 3),
    _OlPS2RamSize_Type()
)
olPS2RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPS2RamSize.setStatus("mandatory")
_OlPS2McaTable_Object = MibTable
olPS2McaTable = _OlPS2McaTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 2)
)
if mibBuilder.loadTexts:
    olPS2McaTable.setStatus("mandatory")
_OlPS2McaEntry_Object = MibTableRow
olPS2McaEntry = _OlPS2McaEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 2, 1)
)
olPS2McaEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olPS2McaIndex"),
)
if mibBuilder.loadTexts:
    olPS2McaEntry.setStatus("mandatory")
_OlPS2McaIndex_Type = Integer32
_OlPS2McaIndex_Object = MibTableColumn
olPS2McaIndex = _OlPS2McaIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 2, 1, 1),
    _OlPS2McaIndex_Type()
)
olPS2McaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPS2McaIndex.setStatus("mandatory")


class _OlPS2McaDescription_Type(DisplayString):
    """Custom type olPS2McaDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlPS2McaDescription_Type.__name__ = "DisplayString"
_OlPS2McaDescription_Object = MibTableColumn
olPS2McaDescription = _OlPS2McaDescription_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 2, 1, 2),
    _OlPS2McaDescription_Type()
)
olPS2McaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPS2McaDescription.setStatus("mandatory")
_OlPS2McaSlotConnectPoint_Type = Integer32
_OlPS2McaSlotConnectPoint_Object = MibTableColumn
olPS2McaSlotConnectPoint = _OlPS2McaSlotConnectPoint_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 2, 1, 3),
    _OlPS2McaSlotConnectPoint_Type()
)
olPS2McaSlotConnectPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPS2McaSlotConnectPoint.setStatus("mandatory")
_OlPS2McaPortConnectPoint_Type = Integer32
_OlPS2McaPortConnectPoint_Object = MibTableColumn
olPS2McaPortConnectPoint = _OlPS2McaPortConnectPoint_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 2, 1, 4),
    _OlPS2McaPortConnectPoint_Type()
)
olPS2McaPortConnectPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPS2McaPortConnectPoint.setStatus("mandatory")


class _OlPS2McaMacAddress_Type(OctetString):
    """Custom type olPS2McaMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlPS2McaMacAddress_Type.__name__ = "OctetString"
_OlPS2McaMacAddress_Object = MibTableColumn
olPS2McaMacAddress = _OlPS2McaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 2, 1, 5),
    _OlPS2McaMacAddress_Type()
)
olPS2McaMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPS2McaMacAddress.setStatus("mandatory")
_OlPS2ApplTable_Object = MibTable
olPS2ApplTable = _OlPS2ApplTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 3)
)
if mibBuilder.loadTexts:
    olPS2ApplTable.setStatus("mandatory")
_OlPS2ApplEntry_Object = MibTableRow
olPS2ApplEntry = _OlPS2ApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 3, 1)
)
olPS2ApplEntry.setIndexNames(
    (0, "CHIPCOMMIB", "olPS2ApplIndex"),
)
if mibBuilder.loadTexts:
    olPS2ApplEntry.setStatus("mandatory")
_OlPS2ApplIndex_Type = Integer32
_OlPS2ApplIndex_Object = MibTableColumn
olPS2ApplIndex = _OlPS2ApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 3, 1, 1),
    _OlPS2ApplIndex_Type()
)
olPS2ApplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPS2ApplIndex.setStatus("mandatory")


class _OlPS2ApplDescription_Type(DisplayString):
    """Custom type olPS2ApplDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlPS2ApplDescription_Type.__name__ = "DisplayString"
_OlPS2ApplDescription_Object = MibTableColumn
olPS2ApplDescription = _OlPS2ApplDescription_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 11, 3, 1, 2),
    _OlPS2ApplDescription_Type()
)
olPS2ApplDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPS2ApplDescription.setStatus("mandatory")
_Oebm_ObjectIdentity = ObjectIdentity
oebm = _Oebm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 2)
)
_Midnight_ObjectIdentity = ObjectIdentity
midnight = _Midnight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 3)
)
_WorkGroupHub_ObjectIdentity = ObjectIdentity
workGroupHub = _WorkGroupHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4)
)
_HubSysGroup_ObjectIdentity = ObjectIdentity
hubSysGroup = _HubSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 1)
)
_HardwareGroup_ObjectIdentity = ObjectIdentity
hardwareGroup = _HardwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 2)
)
_SoftwareGroup_ObjectIdentity = ObjectIdentity
softwareGroup = _SoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 3)
)
_HubGroup_ObjectIdentity = ObjectIdentity
hubGroup = _HubGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 4)
)
_BoardGroup_ObjectIdentity = ObjectIdentity
boardGroup = _BoardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 5)
)
_PortGroup_ObjectIdentity = ObjectIdentity
portGroup = _PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 6)
)
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 7)
)
_Emm_ObjectIdentity = ObjectIdentity
emm = _Emm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 5)
)
_ChipBridge_ObjectIdentity = ObjectIdentity
chipBridge = _ChipBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 6)
)
_Trmm_ObjectIdentity = ObjectIdentity
trmm = _Trmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 7)
)
_Fmm_ObjectIdentity = ObjectIdentity
fmm = _Fmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 8)
)
_Focus1_ObjectIdentity = ObjectIdentity
focus1 = _Focus1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 9)
)
_Oeim_ObjectIdentity = ObjectIdentity
oeim = _Oeim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 10)
)
_Oncore_ObjectIdentity = ObjectIdentity
oncore = _Oncore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 11)
)
_Dmm_ObjectIdentity = ObjectIdentity
dmm = _Dmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 12)
)
_OnsembleEthernet_ObjectIdentity = ObjectIdentity
onsembleEthernet = _OnsembleEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 13)
)
_ChipExperiment_ObjectIdentity = ObjectIdentity
chipExperiment = _ChipExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4)
)
_ChipExpTokenRing_ObjectIdentity = ObjectIdentity
chipExpTokenRing = _ChipExpTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1)
)
_ExpDot5_ObjectIdentity = ObjectIdentity
expDot5 = _ExpDot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1)
)
_ExpDot5Table_Object = MibTable
expDot5Table = _ExpDot5Table_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    expDot5Table.setStatus("obsolete")
_ExpDot5Entry_Object = MibTableRow
expDot5Entry = _ExpDot5Entry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1)
)
expDot5Entry.setIndexNames(
    (0, "CHIPCOMMIB", "expDot5IfIndex"),
)
if mibBuilder.loadTexts:
    expDot5Entry.setStatus("obsolete")
_ExpDot5IfIndex_Type = Integer32
_ExpDot5IfIndex_Object = MibTableColumn
expDot5IfIndex = _ExpDot5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 1),
    _ExpDot5IfIndex_Type()
)
expDot5IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5IfIndex.setStatus("obsolete")


class _ExpDot5Commands_Type(Integer32):
    """Custom type expDot5Commands based on Integer32"""
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
        *(("close", 4),
          ("no-op", 1),
          ("open", 2),
          ("reset", 3))
    )


_ExpDot5Commands_Type.__name__ = "Integer32"
_ExpDot5Commands_Object = MibTableColumn
expDot5Commands = _ExpDot5Commands_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 2),
    _ExpDot5Commands_Type()
)
expDot5Commands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expDot5Commands.setStatus("obsolete")
_ExpDot5RingStatus_Type = Integer32
_ExpDot5RingStatus_Object = MibTableColumn
expDot5RingStatus = _ExpDot5RingStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 3),
    _ExpDot5RingStatus_Type()
)
expDot5RingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5RingStatus.setStatus("obsolete")


class _ExpDot5RingState_Type(Integer32):
    """Custom type expDot5RingState based on Integer32"""
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
        *(("closed", 2),
          ("closing", 4),
          ("openFailure", 5),
          ("opened", 1),
          ("opening", 3),
          ("ringFailure", 6))
    )


_ExpDot5RingState_Type.__name__ = "Integer32"
_ExpDot5RingState_Object = MibTableColumn
expDot5RingState = _ExpDot5RingState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 4),
    _ExpDot5RingState_Type()
)
expDot5RingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5RingState.setStatus("obsolete")


class _ExpDot5RingOpenStatus_Type(Integer32):
    """Custom type expDot5RingOpenStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("badParam", 2),
          ("beaconing", 7),
          ("duplicateMAC", 8),
          ("insertionTimeout", 5),
          ("lobeFailed", 3),
          ("noOpen", 1),
          ("open", 11),
          ("removeReceived", 10),
          ("requestFailed", 9),
          ("ringFailed", 6),
          ("signalLoss", 4))
    )


_ExpDot5RingOpenStatus_Type.__name__ = "Integer32"
_ExpDot5RingOpenStatus_Object = MibTableColumn
expDot5RingOpenStatus = _ExpDot5RingOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 5),
    _ExpDot5RingOpenStatus_Type()
)
expDot5RingOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5RingOpenStatus.setStatus("obsolete")


class _ExpDot5RingSpeed_Type(Integer32):
    """Custom type expDot5RingSpeed based on Integer32"""
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
        *(("fourMegabit", 3),
          ("oneMegabit", 2),
          ("sixteenMegabit", 4),
          ("unknown", 1))
    )


_ExpDot5RingSpeed_Type.__name__ = "Integer32"
_ExpDot5RingSpeed_Object = MibTableColumn
expDot5RingSpeed = _ExpDot5RingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 6),
    _ExpDot5RingSpeed_Type()
)
expDot5RingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expDot5RingSpeed.setStatus("obsolete")
_ExpDot5UpStream_Type = MacAddress
_ExpDot5UpStream_Object = MibTableColumn
expDot5UpStream = _ExpDot5UpStream_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 7),
    _ExpDot5UpStream_Type()
)
expDot5UpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5UpStream.setStatus("obsolete")


class _ExpDot5ActMonParticipate_Type(Integer32):
    """Custom type expDot5ActMonParticipate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ExpDot5ActMonParticipate_Type.__name__ = "Integer32"
_ExpDot5ActMonParticipate_Object = MibTableColumn
expDot5ActMonParticipate = _ExpDot5ActMonParticipate_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 8),
    _ExpDot5ActMonParticipate_Type()
)
expDot5ActMonParticipate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expDot5ActMonParticipate.setStatus("obsolete")
_ExpDot5Functional_Type = MacAddress
_ExpDot5Functional_Object = MibTableColumn
expDot5Functional = _ExpDot5Functional_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 9),
    _ExpDot5Functional_Type()
)
expDot5Functional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expDot5Functional.setStatus("obsolete")
_ExpDot5StatsTable_Object = MibTable
expDot5StatsTable = _ExpDot5StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    expDot5StatsTable.setStatus("obsolete")
_ExpDot5StatsEntry_Object = MibTableRow
expDot5StatsEntry = _ExpDot5StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1)
)
expDot5StatsEntry.setIndexNames(
    (0, "CHIPCOMMIB", "expDot5StatsIfIndex"),
)
if mibBuilder.loadTexts:
    expDot5StatsEntry.setStatus("obsolete")
_ExpDot5StatsIfIndex_Type = Integer32
_ExpDot5StatsIfIndex_Object = MibTableColumn
expDot5StatsIfIndex = _ExpDot5StatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 1),
    _ExpDot5StatsIfIndex_Type()
)
expDot5StatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsIfIndex.setStatus("obsolete")
_ExpDot5StatsLineErrors_Type = Counter32
_ExpDot5StatsLineErrors_Object = MibTableColumn
expDot5StatsLineErrors = _ExpDot5StatsLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 2),
    _ExpDot5StatsLineErrors_Type()
)
expDot5StatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsLineErrors.setStatus("obsolete")
_ExpDot5StatsBurstErrors_Type = Counter32
_ExpDot5StatsBurstErrors_Object = MibTableColumn
expDot5StatsBurstErrors = _ExpDot5StatsBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 3),
    _ExpDot5StatsBurstErrors_Type()
)
expDot5StatsBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsBurstErrors.setStatus("obsolete")
_ExpDot5StatsACErrors_Type = Counter32
_ExpDot5StatsACErrors_Object = MibTableColumn
expDot5StatsACErrors = _ExpDot5StatsACErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 4),
    _ExpDot5StatsACErrors_Type()
)
expDot5StatsACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsACErrors.setStatus("obsolete")
_ExpDot5StatsAbortTransErrors_Type = Counter32
_ExpDot5StatsAbortTransErrors_Object = MibTableColumn
expDot5StatsAbortTransErrors = _ExpDot5StatsAbortTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 5),
    _ExpDot5StatsAbortTransErrors_Type()
)
expDot5StatsAbortTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsAbortTransErrors.setStatus("obsolete")
_ExpDot5StatsInternalErrors_Type = Counter32
_ExpDot5StatsInternalErrors_Object = MibTableColumn
expDot5StatsInternalErrors = _ExpDot5StatsInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 6),
    _ExpDot5StatsInternalErrors_Type()
)
expDot5StatsInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsInternalErrors.setStatus("obsolete")
_ExpDot5StatsLostFrameErrors_Type = Counter32
_ExpDot5StatsLostFrameErrors_Object = MibTableColumn
expDot5StatsLostFrameErrors = _ExpDot5StatsLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 7),
    _ExpDot5StatsLostFrameErrors_Type()
)
expDot5StatsLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsLostFrameErrors.setStatus("obsolete")
_ExpDot5StatsReceiveCongestions_Type = Counter32
_ExpDot5StatsReceiveCongestions_Object = MibTableColumn
expDot5StatsReceiveCongestions = _ExpDot5StatsReceiveCongestions_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 8),
    _ExpDot5StatsReceiveCongestions_Type()
)
expDot5StatsReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsReceiveCongestions.setStatus("obsolete")
_ExpDot5StatsFrameCopiedErrors_Type = Counter32
_ExpDot5StatsFrameCopiedErrors_Object = MibTableColumn
expDot5StatsFrameCopiedErrors = _ExpDot5StatsFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 9),
    _ExpDot5StatsFrameCopiedErrors_Type()
)
expDot5StatsFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsFrameCopiedErrors.setStatus("obsolete")
_ExpDot5StatsTokenErrors_Type = Counter32
_ExpDot5StatsTokenErrors_Object = MibTableColumn
expDot5StatsTokenErrors = _ExpDot5StatsTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 10),
    _ExpDot5StatsTokenErrors_Type()
)
expDot5StatsTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsTokenErrors.setStatus("obsolete")
_ExpDot5StatsSoftErrors_Type = Counter32
_ExpDot5StatsSoftErrors_Object = MibTableColumn
expDot5StatsSoftErrors = _ExpDot5StatsSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 11),
    _ExpDot5StatsSoftErrors_Type()
)
expDot5StatsSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsSoftErrors.setStatus("obsolete")
_ExpDot5StatsHardErrors_Type = Counter32
_ExpDot5StatsHardErrors_Object = MibTableColumn
expDot5StatsHardErrors = _ExpDot5StatsHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 12),
    _ExpDot5StatsHardErrors_Type()
)
expDot5StatsHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsHardErrors.setStatus("obsolete")
_ExpDot5StatsSignalLoss_Type = Counter32
_ExpDot5StatsSignalLoss_Object = MibTableColumn
expDot5StatsSignalLoss = _ExpDot5StatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 13),
    _ExpDot5StatsSignalLoss_Type()
)
expDot5StatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsSignalLoss.setStatus("obsolete")
_ExpDot5StatsTransmitBeacons_Type = Counter32
_ExpDot5StatsTransmitBeacons_Object = MibTableColumn
expDot5StatsTransmitBeacons = _ExpDot5StatsTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 14),
    _ExpDot5StatsTransmitBeacons_Type()
)
expDot5StatsTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsTransmitBeacons.setStatus("obsolete")
_ExpDot5StatsRecoverys_Type = Counter32
_ExpDot5StatsRecoverys_Object = MibTableColumn
expDot5StatsRecoverys = _ExpDot5StatsRecoverys_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 15),
    _ExpDot5StatsRecoverys_Type()
)
expDot5StatsRecoverys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsRecoverys.setStatus("obsolete")
_ExpDot5StatsLobeWires_Type = Counter32
_ExpDot5StatsLobeWires_Object = MibTableColumn
expDot5StatsLobeWires = _ExpDot5StatsLobeWires_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 16),
    _ExpDot5StatsLobeWires_Type()
)
expDot5StatsLobeWires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsLobeWires.setStatus("obsolete")
_ExpDot5StatsRemoves_Type = Counter32
_ExpDot5StatsRemoves_Object = MibTableColumn
expDot5StatsRemoves = _ExpDot5StatsRemoves_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 17),
    _ExpDot5StatsRemoves_Type()
)
expDot5StatsRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsRemoves.setStatus("obsolete")
_ExpDot5StatsSingles_Type = Counter32
_ExpDot5StatsSingles_Object = MibTableColumn
expDot5StatsSingles = _ExpDot5StatsSingles_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 18),
    _ExpDot5StatsSingles_Type()
)
expDot5StatsSingles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsSingles.setStatus("obsolete")
_ExpDot5StatsFreqErrors_Type = Counter32
_ExpDot5StatsFreqErrors_Object = MibTableColumn
expDot5StatsFreqErrors = _ExpDot5StatsFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 19),
    _ExpDot5StatsFreqErrors_Type()
)
expDot5StatsFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5StatsFreqErrors.setStatus("obsolete")
_ExpDot5Tests_ObjectIdentity = ObjectIdentity
expDot5Tests = _ExpDot5Tests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 3)
)
_TestInsertFunc_ObjectIdentity = ObjectIdentity
testInsertFunc = _TestInsertFunc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 3, 1)
)
_ExpDot5ChipSets_ObjectIdentity = ObjectIdentity
expDot5ChipSets = _ExpDot5ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 4)
)
_ChipSetIBM16_ObjectIdentity = ObjectIdentity
chipSetIBM16 = _ChipSetIBM16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 4, 1)
)
_ChipSetTItms380_ObjectIdentity = ObjectIdentity
chipSetTItms380 = _ChipSetTItms380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 4, 2)
)
_ChipSetTItms380c16_ObjectIdentity = ObjectIdentity
chipSetTItms380c16 = _ChipSetTItms380c16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 4, 3)
)
_ExpDot5TimerTable_Object = MibTable
expDot5TimerTable = _ExpDot5TimerTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    expDot5TimerTable.setStatus("obsolete")
_ExpDot5TimerEntry_Object = MibTableRow
expDot5TimerEntry = _ExpDot5TimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1)
)
expDot5TimerEntry.setIndexNames(
    (0, "CHIPCOMMIB", "expDot5TimerIfIndex"),
)
if mibBuilder.loadTexts:
    expDot5TimerEntry.setStatus("obsolete")
_ExpDot5TimerIfIndex_Type = Integer32
_ExpDot5TimerIfIndex_Object = MibTableColumn
expDot5TimerIfIndex = _ExpDot5TimerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 1),
    _ExpDot5TimerIfIndex_Type()
)
expDot5TimerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerIfIndex.setStatus("obsolete")
_ExpDot5TimerReturnRepeat_Type = Integer32
_ExpDot5TimerReturnRepeat_Object = MibTableColumn
expDot5TimerReturnRepeat = _ExpDot5TimerReturnRepeat_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 2),
    _ExpDot5TimerReturnRepeat_Type()
)
expDot5TimerReturnRepeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerReturnRepeat.setStatus("obsolete")
_ExpDot5TimerHolding_Type = Integer32
_ExpDot5TimerHolding_Object = MibTableColumn
expDot5TimerHolding = _ExpDot5TimerHolding_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 3),
    _ExpDot5TimerHolding_Type()
)
expDot5TimerHolding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerHolding.setStatus("obsolete")
_ExpDot5TimerQueuePDU_Type = Integer32
_ExpDot5TimerQueuePDU_Object = MibTableColumn
expDot5TimerQueuePDU = _ExpDot5TimerQueuePDU_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 4),
    _ExpDot5TimerQueuePDU_Type()
)
expDot5TimerQueuePDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerQueuePDU.setStatus("obsolete")
_ExpDot5TimerValidTransmit_Type = Integer32
_ExpDot5TimerValidTransmit_Object = MibTableColumn
expDot5TimerValidTransmit = _ExpDot5TimerValidTransmit_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 5),
    _ExpDot5TimerValidTransmit_Type()
)
expDot5TimerValidTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerValidTransmit.setStatus("obsolete")
_ExpDot5TimerNoToken_Type = Integer32
_ExpDot5TimerNoToken_Object = MibTableColumn
expDot5TimerNoToken = _ExpDot5TimerNoToken_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 6),
    _ExpDot5TimerNoToken_Type()
)
expDot5TimerNoToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerNoToken.setStatus("obsolete")
_ExpDot5TimerActiveMon_Type = Integer32
_ExpDot5TimerActiveMon_Object = MibTableColumn
expDot5TimerActiveMon = _ExpDot5TimerActiveMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 7),
    _ExpDot5TimerActiveMon_Type()
)
expDot5TimerActiveMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerActiveMon.setStatus("obsolete")
_ExpDot5TimerStandbyMon_Type = Integer32
_ExpDot5TimerStandbyMon_Object = MibTableColumn
expDot5TimerStandbyMon = _ExpDot5TimerStandbyMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 8),
    _ExpDot5TimerStandbyMon_Type()
)
expDot5TimerStandbyMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerStandbyMon.setStatus("obsolete")
_ExpDot5TimerErrorReport_Type = Integer32
_ExpDot5TimerErrorReport_Object = MibTableColumn
expDot5TimerErrorReport = _ExpDot5TimerErrorReport_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 9),
    _ExpDot5TimerErrorReport_Type()
)
expDot5TimerErrorReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerErrorReport.setStatus("obsolete")
_ExpDot5TimerBeaconTransmit_Type = Integer32
_ExpDot5TimerBeaconTransmit_Object = MibTableColumn
expDot5TimerBeaconTransmit = _ExpDot5TimerBeaconTransmit_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 10),
    _ExpDot5TimerBeaconTransmit_Type()
)
expDot5TimerBeaconTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerBeaconTransmit.setStatus("obsolete")
_ExpDot5TimerBeaconReceive_Type = Integer32
_ExpDot5TimerBeaconReceive_Object = MibTableColumn
expDot5TimerBeaconReceive = _ExpDot5TimerBeaconReceive_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 11),
    _ExpDot5TimerBeaconReceive_Type()
)
expDot5TimerBeaconReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDot5TimerBeaconReceive.setStatus("obsolete")
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14)
)
_ChipTTY_ObjectIdentity = ObjectIdentity
chipTTY = _ChipTTY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 5)
)
_ChipTTYNumber_Type = Integer32
_ChipTTYNumber_Object = MibScalar
chipTTYNumber = _ChipTTYNumber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 1),
    _ChipTTYNumber_Type()
)
chipTTYNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipTTYNumber.setStatus("mandatory")
_ChipTTYTable_Object = MibTable
chipTTYTable = _ChipTTYTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2)
)
if mibBuilder.loadTexts:
    chipTTYTable.setStatus("mandatory")
_ChipTTYEntry_Object = MibTableRow
chipTTYEntry = _ChipTTYEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1)
)
chipTTYEntry.setIndexNames(
    (0, "CHIPCOMMIB", "chipTTYIndex"),
)
if mibBuilder.loadTexts:
    chipTTYEntry.setStatus("mandatory")
_ChipTTYIndex_Type = Integer32
_ChipTTYIndex_Object = MibTableColumn
chipTTYIndex = _ChipTTYIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 1),
    _ChipTTYIndex_Type()
)
chipTTYIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipTTYIndex.setStatus("mandatory")


class _ChipTTYBaud_Type(Integer32):
    """Custom type chipTTYBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(110,
              300,
              1200,
              2400,
              4800,
              9600,
              19200,
              38400)
        )
    )
    namedValues = NamedValues(
        *(("forty-eight-hundred", 4800),
          ("nineteen-two-hundred", 19200),
          ("ninety-six-hundred", 9600),
          ("one-hundred-ten", 110),
          ("thirty-eight-thousand-four-hundred", 38400),
          ("three-hundred", 300),
          ("twelve-hundred", 1200),
          ("twenty-four-hundred", 2400))
    )


_ChipTTYBaud_Type.__name__ = "Integer32"
_ChipTTYBaud_Object = MibTableColumn
chipTTYBaud = _ChipTTYBaud_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 2),
    _ChipTTYBaud_Type()
)
chipTTYBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYBaud.setStatus("mandatory")


class _ChipTTYParity_Type(Integer32):
    """Custom type chipTTYParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 3),
          ("odd", 1))
    )


_ChipTTYParity_Type.__name__ = "Integer32"
_ChipTTYParity_Object = MibTableColumn
chipTTYParity = _ChipTTYParity_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 3),
    _ChipTTYParity_Type()
)
chipTTYParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYParity.setStatus("mandatory")


class _ChipTTYStop_Type(Integer32):
    """Custom type chipTTYStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_ChipTTYStop_Type.__name__ = "Integer32"
_ChipTTYStop_Object = MibTableColumn
chipTTYStop = _ChipTTYStop_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 4),
    _ChipTTYStop_Type()
)
chipTTYStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYStop.setStatus("mandatory")


class _ChipTTYData_Type(Integer32):
    """Custom type chipTTYData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("seven", 7))
    )


_ChipTTYData_Type.__name__ = "Integer32"
_ChipTTYData_Object = MibTableColumn
chipTTYData = _ChipTTYData_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 5),
    _ChipTTYData_Type()
)
chipTTYData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYData.setStatus("mandatory")
_ChipTTYTimeout_Type = Integer32
_ChipTTYTimeout_Object = MibTableColumn
chipTTYTimeout = _ChipTTYTimeout_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 6),
    _ChipTTYTimeout_Type()
)
chipTTYTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYTimeout.setStatus("mandatory")


class _ChipTTYPrompt_Type(DisplayString):
    """Custom type chipTTYPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChipTTYPrompt_Type.__name__ = "DisplayString"
_ChipTTYPrompt_Object = MibTableColumn
chipTTYPrompt = _ChipTTYPrompt_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 7),
    _ChipTTYPrompt_Type()
)
chipTTYPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYPrompt.setStatus("mandatory")


class _ChipTTYDTR_Type(Integer32):
    """Custom type chipTTYDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asserted", 1),
          ("deasserted", 2),
          ("notApplicable", 3))
    )


_ChipTTYDTR_Type.__name__ = "Integer32"
_ChipTTYDTR_Object = MibTableColumn
chipTTYDTR = _ChipTTYDTR_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 8),
    _ChipTTYDTR_Type()
)
chipTTYDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYDTR.setStatus("mandatory")


class _ChipTTYTerminalType_Type(DisplayString):
    """Custom type chipTTYTerminalType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ChipTTYTerminalType_Type.__name__ = "DisplayString"
_ChipTTYTerminalType_Object = MibTableColumn
chipTTYTerminalType = _ChipTTYTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 9),
    _ChipTTYTerminalType_Type()
)
chipTTYTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYTerminalType.setStatus("mandatory")
_ChipTFTP_ObjectIdentity = ObjectIdentity
chipTFTP = _ChipTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 6)
)


class _ChipTFTPStart_Type(Integer32):
    """Custom type chipTFTPStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftpGet", 2),
          ("tftpNoTransfer", 1),
          ("tftpPut", 3))
    )


_ChipTFTPStart_Type.__name__ = "Integer32"
_ChipTFTPStart_Object = MibScalar
chipTFTPStart = _ChipTFTPStart_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 1),
    _ChipTFTPStart_Type()
)
chipTFTPStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPStart.setStatus("mandatory")


class _ChipTFTPSlot_Type(Integer32):
    """Custom type chipTFTPSlot based on Integer32"""
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
              15,
              16,
              17,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("agent-slot", 255),
          ("all-fddi-port-slots", 254),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_ChipTFTPSlot_Type.__name__ = "Integer32"
_ChipTFTPSlot_Object = MibScalar
chipTFTPSlot = _ChipTFTPSlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 2),
    _ChipTFTPSlot_Type()
)
chipTFTPSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPSlot.setStatus("mandatory")
_ChipTFTPIpAddress_Type = IpAddress
_ChipTFTPIpAddress_Object = MibScalar
chipTFTPIpAddress = _ChipTFTPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 3),
    _ChipTFTPIpAddress_Type()
)
chipTFTPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPIpAddress.setStatus("mandatory")


class _ChipTFTPFileName_Type(DisplayString):
    """Custom type chipTFTPFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChipTFTPFileName_Type.__name__ = "DisplayString"
_ChipTFTPFileName_Object = MibScalar
chipTFTPFileName = _ChipTFTPFileName_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 4),
    _ChipTFTPFileName_Type()
)
chipTFTPFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPFileName.setStatus("mandatory")


class _ChipTFTPFileType_Type(Integer32):
    """Custom type chipTFTPFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 3),
          ("bootCode", 2),
          ("flashCode", 1))
    )


_ChipTFTPFileType_Type.__name__ = "Integer32"
_ChipTFTPFileType_Object = MibScalar
chipTFTPFileType = _ChipTFTPFileType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 5),
    _ChipTFTPFileType_Type()
)
chipTFTPFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPFileType.setStatus("mandatory")


class _ChipTFTPResult_Type(Integer32):
    """Custom type chipTFTPResult based on Integer32"""
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
              15,
              16,
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
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("accessError", 6),
          ("clear", 1),
          ("crcError", 22),
          ("decodeError", 17),
          ("diskFull", 7),
          ("dlInProgress", 18),
          ("downloadFailed", 21),
          ("fepromErase", 14),
          ("fepromProg", 15),
          ("fileForwardProblem", 33),
          ("fileGetProblem", 26),
          ("fileNotFound", 5),
          ("fileTooLarge", 25),
          ("fileTypeError", 32),
          ("gatewayUnreachable", 30),
          ("illegalTFTPOperation", 8),
          ("invalidDLType", 23),
          ("invalidDownloadKey", 11),
          ("invalidNetwork", 13),
          ("invalidSlot", 12),
          ("invalidTFTPTransactionID", 9),
          ("moduleTypeError", 31),
          ("noModsOfType", 20),
          ("noModuleInSlot", 36),
          ("noResponse", 10),
          ("notMaster", 27),
          ("notYetSupported", 19),
          ("notifyTargetError", 34),
          ("okay", 3),
          ("onlyOperational", 28),
          ("otherTFTPError", 4),
          ("rejectedByTarget", 29),
          ("serverTimeout", 35),
          ("targetTimeout", 37),
          ("unknownFEPROMType", 24),
          ("xferError", 16),
          ("xferInProgress", 2))
    )


_ChipTFTPResult_Type.__name__ = "Integer32"
_ChipTFTPResult_Object = MibScalar
chipTFTPResult = _ChipTFTPResult_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 6),
    _ChipTFTPResult_Type()
)
chipTFTPResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipTFTPResult.setStatus("mandatory")
_ChipTFTPSubSlot_Type = Integer32
_ChipTFTPSubSlot_Object = MibScalar
chipTFTPSubSlot = _ChipTFTPSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 7),
    _ChipTFTPSubSlot_Type()
)
chipTFTPSubSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPSubSlot.setStatus("mandatory")


class _ChipTFTPTargetLocation_Type(Integer32):
    """Custom type chipTFTPTargetLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("target-Device", 1),
          ("target-SlotSubSlot", 2))
    )


_ChipTFTPTargetLocation_Type.__name__ = "Integer32"
_ChipTFTPTargetLocation_Object = MibScalar
chipTFTPTargetLocation = _ChipTFTPTargetLocation_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 8),
    _ChipTFTPTargetLocation_Type()
)
chipTFTPTargetLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPTargetLocation.setStatus("mandatory")
_ChipDownload_ObjectIdentity = ObjectIdentity
chipDownload = _ChipDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 7)
)


class _ChipDownloadUDKSerial_Type(DisplayString):
    """Custom type chipDownloadUDKSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ChipDownloadUDKSerial_Type.__name__ = "DisplayString"
_ChipDownloadUDKSerial_Object = MibScalar
chipDownloadUDKSerial = _ChipDownloadUDKSerial_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 7, 1),
    _ChipDownloadUDKSerial_Type()
)
chipDownloadUDKSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipDownloadUDKSerial.setStatus("mandatory")


class _ChipDownloadKey_Type(DisplayString):
    """Custom type chipDownloadKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ChipDownloadKey_Type.__name__ = "DisplayString"
_ChipDownloadKey_Object = MibScalar
chipDownloadKey = _ChipDownloadKey_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 7, 2),
    _ChipDownloadKey_Type()
)
chipDownloadKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipDownloadKey.setStatus("mandatory")


class _ChipDownloadDateTime_Type(DisplayString):
    """Custom type chipDownloadDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ChipDownloadDateTime_Type.__name__ = "DisplayString"
_ChipDownloadDateTime_Object = MibScalar
chipDownloadDateTime = _ChipDownloadDateTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 7, 3),
    _ChipDownloadDateTime_Type()
)
chipDownloadDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipDownloadDateTime.setStatus("mandatory")
_ChipAlert_ObjectIdentity = ObjectIdentity
chipAlert = _ChipAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 8)
)
_ChipAlertTable_Object = MibTable
chipAlertTable = _ChipAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 8, 1)
)
if mibBuilder.loadTexts:
    chipAlertTable.setStatus("mandatory")
_ChipAlertEntry_Object = MibTableRow
chipAlertEntry = _ChipAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 8, 1, 1)
)
chipAlertEntry.setIndexNames(
    (0, "CHIPCOMMIB", "chipAlertIndex"),
)
if mibBuilder.loadTexts:
    chipAlertEntry.setStatus("mandatory")


class _ChipAlertIndex_Type(Integer32):
    """Custom type chipAlertIndex based on Integer32"""
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
        *(("change", 3),
          ("console-display", 4),
          ("hello", 2),
          ("port-up-down", 5),
          ("snmp-authentication", 1))
    )


_ChipAlertIndex_Type.__name__ = "Integer32"
_ChipAlertIndex_Object = MibTableColumn
chipAlertIndex = _ChipAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 8, 1, 1, 1),
    _ChipAlertIndex_Type()
)
chipAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipAlertIndex.setStatus("mandatory")


class _ChipAlertMode_Type(Integer32):
    """Custom type chipAlertMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("filter", 3))
    )


_ChipAlertMode_Type.__name__ = "Integer32"
_ChipAlertMode_Object = MibTableColumn
chipAlertMode = _ChipAlertMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 8, 1, 1, 2),
    _ChipAlertMode_Type()
)
chipAlertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipAlertMode.setStatus("mandatory")
_ChipBootP_ObjectIdentity = ObjectIdentity
chipBootP = _ChipBootP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 11)
)


class _ChipBootPStart_Type(Integer32):
    """Custom type chipBootPStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootpNoTransfer", 1),
          ("bootpRequest", 2))
    )


_ChipBootPStart_Type.__name__ = "Integer32"
_ChipBootPStart_Object = MibScalar
chipBootPStart = _ChipBootPStart_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 11, 1),
    _ChipBootPStart_Type()
)
chipBootPStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipBootPStart.setStatus("mandatory")


class _ChipBootPPowerUpMode_Type(Integer32):
    """Custom type chipBootPPowerUpMode based on Integer32"""
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


_ChipBootPPowerUpMode_Type.__name__ = "Integer32"
_ChipBootPPowerUpMode_Object = MibScalar
chipBootPPowerUpMode = _ChipBootPPowerUpMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 11, 2),
    _ChipBootPPowerUpMode_Type()
)
chipBootPPowerUpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipBootPPowerUpMode.setStatus("mandatory")
_ChipBootPIpAddress_Type = IpAddress
_ChipBootPIpAddress_Object = MibScalar
chipBootPIpAddress = _ChipBootPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 11, 3),
    _ChipBootPIpAddress_Type()
)
chipBootPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipBootPIpAddress.setStatus("mandatory")


class _ChipBootPResult_Type(Integer32):
    """Custom type chipBootPResult based on Integer32"""
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
        *(("clear", 1),
          ("noBootPResponse", 4),
          ("okay", 3),
          ("otherBootPError", 5),
          ("xferInProgress", 2))
    )


_ChipBootPResult_Type.__name__ = "Integer32"
_ChipBootPResult_Object = MibScalar
chipBootPResult = _ChipBootPResult_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 11, 4),
    _ChipBootPResult_Type()
)
chipBootPResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipBootPResult.setStatus("mandatory")

# Managed Objects groups


# Notification objects

chipHello = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 1)
)
if mibBuilder.loadTexts:
    chipHello.setStatus(
        ""
    )

chipSlotDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 2)
)
chipSlotDown.setObjects(
    ("CHIPCOMMIB", "olModSlotIndex")
)
if mibBuilder.loadTexts:
    chipSlotDown.setStatus(
        ""
    )

chipSlotUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 3)
)
chipSlotUp.setObjects(
    ("CHIPCOMMIB", "olModSlotIndex")
)
if mibBuilder.loadTexts:
    chipSlotUp.setStatus(
        ""
    )

chipEnvironment = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 4)
)
if mibBuilder.loadTexts:
    chipEnvironment.setStatus(
        ""
    )

chipHardware = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 5)
)
if mibBuilder.loadTexts:
    chipHardware.setStatus(
        ""
    )

chipSoftware = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 6)
)
if mibBuilder.loadTexts:
    chipSoftware.setStatus(
        ""
    )

chipChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 7)
)
if mibBuilder.loadTexts:
    chipChange.setStatus(
        ""
    )

chipFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 8)
)
if mibBuilder.loadTexts:
    chipFatal.setStatus(
        ""
    )

chipTrunkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 9)
)
chipTrunkDown.setObjects(
      *(("CHIPCOMMIB", "olTrunkSlotIndex"),
        ("CHIPCOMMIB", "olTrunkIndex"),
        ("CHIPCOMMIB", "olTrunkAdminState"),
        ("CHIPCOMMIB", "olTrunkStatus"))
)
if mibBuilder.loadTexts:
    chipTrunkDown.setStatus(
        ""
    )

chipTrunkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 10)
)
chipTrunkUp.setObjects(
      *(("CHIPCOMMIB", "olTrunkSlotIndex"),
        ("CHIPCOMMIB", "olTrunkIndex"),
        ("CHIPCOMMIB", "olTrunkAdminState"),
        ("CHIPCOMMIB", "olTrunkStatus"))
)
if mibBuilder.loadTexts:
    chipTrunkUp.setStatus(
        ""
    )

chipPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 11)
)
chipPortDown.setObjects(
      *(("CHIPCOMMIB", "olPortSlotIndex"),
        ("CHIPCOMMIB", "olPortIndex"),
        ("CHIPCOMMIB", "olPortAdminState"),
        ("CHIPCOMMIB", "olPortStatus"))
)
if mibBuilder.loadTexts:
    chipPortDown.setStatus(
        ""
    )

chipPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 12)
)
chipPortUp.setObjects(
      *(("CHIPCOMMIB", "olPortSlotIndex"),
        ("CHIPCOMMIB", "olPortIndex"),
        ("CHIPCOMMIB", "olPortAdminState"),
        ("CHIPCOMMIB", "olPortStatus"))
)
if mibBuilder.loadTexts:
    chipPortUp.setStatus(
        ""
    )

chipPing = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 13)
)
chipPing.setObjects(
      *(("CHIPCOMMIB", "chipEchoAddr"),
        ("CHIPCOMMIB", "chipEchoNumber"),
        ("CHIPCOMMIB", "chipEchoResponseCounts"))
)
if mibBuilder.loadTexts:
    chipPing.setStatus(
        ""
    )

chipAboveThreshd = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 14)
)
if mibBuilder.loadTexts:
    chipAboveThreshd.setStatus(
        ""
    )

chipBelowThreshd = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 15)
)
if mibBuilder.loadTexts:
    chipBelowThreshd.setStatus(
        ""
    )

chipModuleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 16)
)
chipModuleDown.setObjects(
      *(("CHIPCOMMIB", "ocModSlotIndex"),
        ("CHIPCOMMIB", "ocModSubSlotIndex"),
        ("CHIPCOMMIB", "ocModType"),
        ("CHIPCOMMIB", "ocModDescr"))
)
if mibBuilder.loadTexts:
    chipModuleDown.setStatus(
        ""
    )

chipModuleUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 17)
)
chipModuleUp.setObjects(
      *(("CHIPCOMMIB", "ocModSlotIndex"),
        ("CHIPCOMMIB", "ocModSubSlotIndex"),
        ("CHIPCOMMIB", "ocModType"),
        ("CHIPCOMMIB", "ocModDescr"))
)
if mibBuilder.loadTexts:
    chipModuleUp.setStatus(
        ""
    )

chipSecurity = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 0, 18)
)
chipSecurity.setObjects(
    ("CHIPCOMMIB", "olNetOlSecTrapReason")
)
if mibBuilder.loadTexts:
    chipSecurity.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHIPCOMMIB",
    **{"MacAddress": MacAddress,
       "chipcom": chipcom,
       "chipHello": chipHello,
       "chipSlotDown": chipSlotDown,
       "chipSlotUp": chipSlotUp,
       "chipEnvironment": chipEnvironment,
       "chipHardware": chipHardware,
       "chipSoftware": chipSoftware,
       "chipChange": chipChange,
       "chipFatal": chipFatal,
       "chipTrunkDown": chipTrunkDown,
       "chipTrunkUp": chipTrunkUp,
       "chipPortDown": chipPortDown,
       "chipPortUp": chipPortUp,
       "chipPing": chipPing,
       "chipAboveThreshd": chipAboveThreshd,
       "chipBelowThreshd": chipBelowThreshd,
       "chipModuleDown": chipModuleDown,
       "chipModuleUp": chipModuleUp,
       "chipSecurity": chipSecurity,
       "chipmib02": chipmib02,
       "chipGen": chipGen,
       "chipGenProduct": chipGenProduct,
       "chipGenServiceDate": chipGenServiceDate,
       "chipGenNetman": chipGenNetman,
       "chipGenDiagnostics": chipGenDiagnostics,
       "chipGenSerial": chipGenSerial,
       "chipGenID": chipGenID,
       "chipGenVers": chipGenVers,
       "chipGenAuthFailureAddr": chipGenAuthFailureAddr,
       "chipGenTimeLastChanged": chipGenTimeLastChanged,
       "chipEcho": chipEcho,
       "chipEchoStart": chipEchoStart,
       "chipEchoAddr": chipEchoAddr,
       "chipEchoPattern": chipEchoPattern,
       "chipEchoNumber": chipEchoNumber,
       "chipEchoSize": chipEchoSize,
       "chipEchoResponseCounts": chipEchoResponseCounts,
       "chipProducts": chipProducts,
       "online": online,
       "olAgents": olAgents,
       "olAgentsMySlot": olAgentsMySlot,
       "olAgentsMasterReset": olAgentsMasterReset,
       "olAgentsTable": olAgentsTable,
       "olAgentsEntry": olAgentsEntry,
       "olAgentsSlotIndex": olAgentsSlotIndex,
       "olAgentsStationAddr": olAgentsStationAddr,
       "olAgentsIpAddress": olAgentsIpAddress,
       "olAgentsMasterStatus": olAgentsMasterStatus,
       "olAgentsMasterPriority": olAgentsMasterPriority,
       "ocAgentsSubSlot": ocAgentsSubSlot,
       "olConc": olConc,
       "olConcType": olConcType,
       "olConcReset": olConcReset,
       "olConcNumSlots": olConcNumSlots,
       "olConcProfile": olConcProfile,
       "olEnv": olEnv,
       "olEnvTempStatus": olEnvTempStatus,
       "olEnvPSCapacity": olEnvPSCapacity,
       "olEnvPSTable": olEnvPSTable,
       "olEnvPSEntry": olEnvPSEntry,
       "olEnvPSIndex": olEnvPSIndex,
       "olEnvPSAdminState": olEnvPSAdminState,
       "olEnvPSOperStatus": olEnvPSOperStatus,
       "olEnvFanStatus": olEnvFanStatus,
       "olEnvTable": olEnvTable,
       "olEnvEntry": olEnvEntry,
       "olEnvType": olEnvType,
       "olEnvStatus": olEnvStatus,
       "olModules": olModules,
       "olModTable": olModTable,
       "olModEntry": olModEntry,
       "olModSlotIndex": olModSlotIndex,
       "olModType": olModType,
       "olModClass": olModClass,
       "olModDescr": olModDescr,
       "olModVersion": olModVersion,
       "olModVendor": olModVendor,
       "olModResetModule": olModResetModule,
       "olModConfigToDips": olModConfigToDips,
       "olModConfigured": olModConfigured,
       "olModNetwork": olModNetwork,
       "olModNetworkType": olModNetworkType,
       "olModStatus": olModStatus,
       "olModNumPorts": olModNumPorts,
       "olModNumTrunks": olModNumTrunks,
       "olPortTable": olPortTable,
       "olPortEntry": olPortEntry,
       "olPortSlotIndex": olPortSlotIndex,
       "olPortIndex": olPortIndex,
       "olPortType": olPortType,
       "olPortConnector": olPortConnector,
       "olPortStatus": olPortStatus,
       "olPortAdminState": olPortAdminState,
       "olPortNetwork": olPortNetwork,
       "olPortNetworkType": olPortNetworkType,
       "olPortAlertFilter": olPortAlertFilter,
       "olTrunkTable": olTrunkTable,
       "olTrunkEntry": olTrunkEntry,
       "olTrunkSlotIndex": olTrunkSlotIndex,
       "olTrunkIndex": olTrunkIndex,
       "olTrunkType": olTrunkType,
       "olTrunkConnector": olTrunkConnector,
       "olTrunkStatus": olTrunkStatus,
       "olTrunkAdminState": olTrunkAdminState,
       "olTrunkWrapState": olTrunkWrapState,
       "olTrunkNeighbor": olTrunkNeighbor,
       "olSpecMods": olSpecMods,
       "ol50nnMCTL": ol50nnMCTL,
       "ol50nnMCTLModTable": ol50nnMCTLModTable,
       "ol50nnMCTLModEntry": ol50nnMCTLModEntry,
       "ol50nnMCTLModSlotIndex": ol50nnMCTLModSlotIndex,
       "ol50nnMCTLModTempStatus": ol50nnMCTLModTempStatus,
       "ol51nnMMGT": ol51nnMMGT,
       "ol51nnMMGTModTable": ol51nnMMGTModTable,
       "ol51nnMMGTModEntry": ol51nnMMGTModEntry,
       "ol51nnMMGTModSlotIndex": ol51nnMMGTModSlotIndex,
       "ol51nnMMGTModMasterPriority": ol51nnMMGTModMasterPriority,
       "ol51nnMMGTModMasterStatus": ol51nnMMGTModMasterStatus,
       "ol51nnMMGTModStationAddr": ol51nnMMGTModStationAddr,
       "ol51nnMMGTPortTable": ol51nnMMGTPortTable,
       "ol51nnMMGTPortEntry": ol51nnMMGTPortEntry,
       "ol51nnMMGTPortSlotIndex": ol51nnMMGTPortSlotIndex,
       "ol51nnMMGTPortIndex": ol51nnMMGTPortIndex,
       "ol51nnMMGTIpAddress": ol51nnMMGTIpAddress,
       "ol51nnMFIB": ol51nnMFIB,
       "ol51nnMFIBModTable": ol51nnMFIBModTable,
       "ol51nnMFIBModEntry": ol51nnMFIBModEntry,
       "ol51nnMFIBModSlotIndex": ol51nnMFIBModSlotIndex,
       "ol51nnMFIBModDipNetwork": ol51nnMFIBModDipNetwork,
       "ol51nnMFIBModLLW": ol51nnMFIBModLLW,
       "ol51nnMFIBModDipLLW": ol51nnMFIBModDipLLW,
       "ol51nnMFIBPortTable": ol51nnMFIBPortTable,
       "ol51nnMFIBPortEntry": ol51nnMFIBPortEntry,
       "ol51nnMFIBPortSlotIndex": ol51nnMFIBPortSlotIndex,
       "ol51nnMFIBPortIndex": ol51nnMFIBPortIndex,
       "ol51nnMFIBPortAdminState": ol51nnMFIBPortAdminState,
       "ol51nnMFIBPortBuddySlot": ol51nnMFIBPortBuddySlot,
       "ol51nnMFIBPortBuddyPort": ol51nnMFIBPortBuddyPort,
       "ol51nnMFIBPortDipAdminState": ol51nnMFIBPortDipAdminState,
       "ol51nnMUTP": ol51nnMUTP,
       "ol51nnMUTPModTable": ol51nnMUTPModTable,
       "ol51nnMUTPModEntry": ol51nnMUTPModEntry,
       "ol51nnMUTPModSlotIndex": ol51nnMUTPModSlotIndex,
       "ol51nnMUTPModDipNetwork": ol51nnMUTPModDipNetwork,
       "ol51nnMUTPModCrossover": ol51nnMUTPModCrossover,
       "ol51nnMUTPModDipCrossover": ol51nnMUTPModDipCrossover,
       "ol51nnMUTPModFFL": ol51nnMUTPModFFL,
       "ol51nnMUTPModDipFFL": ol51nnMUTPModDipFFL,
       "ol51nnMUTPPortTable": ol51nnMUTPPortTable,
       "ol51nnMUTPPortEntry": ol51nnMUTPPortEntry,
       "ol51nnMUTPPortSlotIndex": ol51nnMUTPPortSlotIndex,
       "ol51nnMUTPPortIndex": ol51nnMUTPPortIndex,
       "ol51nnMUTPPortAdminState": ol51nnMUTPPortAdminState,
       "ol51nnMUTPPortBuddySlot": ol51nnMUTPPortBuddySlot,
       "ol51nnMUTPPortBuddyPort": ol51nnMUTPPortBuddyPort,
       "ol51nnMUTPPortDipAdminState": ol51nnMUTPPortDipAdminState,
       "ol51nnMUTPPortLinkInteg": ol51nnMUTPPortLinkInteg,
       "ol51nnMUTPPortDipLinkInteg": ol51nnMUTPPortDipLinkInteg,
       "ol51nnMUTPPortSquelch": ol51nnMUTPPortSquelch,
       "ol51nnMUTPPortDipSquelch": ol51nnMUTPPortDipSquelch,
       "ol51nnMTP": ol51nnMTP,
       "ol51nnMTPModTable": ol51nnMTPModTable,
       "ol51nnMTPModEntry": ol51nnMTPModEntry,
       "ol51nnMTPModSlotIndex": ol51nnMTPModSlotIndex,
       "ol51nnMTPModDipNetwork": ol51nnMTPModDipNetwork,
       "ol51nnMTPModCrossover": ol51nnMTPModCrossover,
       "ol51nnMTPModDipCrossover": ol51nnMTPModDipCrossover,
       "ol51nnMTPPortTable": ol51nnMTPPortTable,
       "ol51nnMTPPortEntry": ol51nnMTPPortEntry,
       "ol51nnMTPPortSlotIndex": ol51nnMTPPortSlotIndex,
       "ol51nnMTPPortIndex": ol51nnMTPPortIndex,
       "ol51nnMTPPortAdminState": ol51nnMTPPortAdminState,
       "ol51nnMTPPortBuddySlot": ol51nnMTPPortBuddySlot,
       "ol51nnMTPPortBuddyPort": ol51nnMTPPortBuddyPort,
       "ol51nnMTPPortDipAdminState": ol51nnMTPPortDipAdminState,
       "ol51nnMTPPortLinkInteg": ol51nnMTPPortLinkInteg,
       "ol51nnMTPPortDipLinkInteg": ol51nnMTPPortDipLinkInteg,
       "ol51nnMTPPortSquelch": ol51nnMTPPortSquelch,
       "ol51nnMTPPortDipSquelch": ol51nnMTPPortDipSquelch,
       "ol51nnMBNC": ol51nnMBNC,
       "ol51nnMBNCModTable": ol51nnMBNCModTable,
       "ol51nnMBNCModEntry": ol51nnMBNCModEntry,
       "ol51nnMBNCModSlotIndex": ol51nnMBNCModSlotIndex,
       "ol51nnMBNCModDipNetwork": ol51nnMBNCModDipNetwork,
       "ol51nnMBNCPortTable": ol51nnMBNCPortTable,
       "ol51nnMBNCPortEntry": ol51nnMBNCPortEntry,
       "ol51nnMBNCPortSlotIndex": ol51nnMBNCPortSlotIndex,
       "ol51nnMBNCPortIndex": ol51nnMBNCPortIndex,
       "ol51nnMBNCPortDipAdminState": ol51nnMBNCPortDipAdminState,
       "ol51nnMBNCPortDipTermination": ol51nnMBNCPortDipTermination,
       "ol51nnMBNCPortDipGround": ol51nnMBNCPortDipGround,
       "ol51nnBEE": ol51nnBEE,
       "ol51nnBEEModTable": ol51nnBEEModTable,
       "ol51nnBEEModEntry": ol51nnBEEModEntry,
       "ol51nnBEEModSlotIndex": ol51nnBEEModSlotIndex,
       "ol51nnBEEModStationAddr": ol51nnBEEModStationAddr,
       "ol51nnBEEModProtocols": ol51nnBEEModProtocols,
       "ol51nnBEEPortTable": ol51nnBEEPortTable,
       "ol51nnBEEPortEntry": ol51nnBEEPortEntry,
       "ol51nnBEEPortSlotIndex": ol51nnBEEPortSlotIndex,
       "ol51nnBEEPortIndex": ol51nnBEEPortIndex,
       "ol51nnBEEPortIpAddress": ol51nnBEEPortIpAddress,
       "ol51nnBEEPortDipNetwork": ol51nnBEEPortDipNetwork,
       "ol51nnBEEPortDefNetwork": ol51nnBEEPortDefNetwork,
       "ol51nnRES": ol51nnRES,
       "ol51nnRESModTable": ol51nnRESModTable,
       "ol51nnRESModEntry": ol51nnRESModEntry,
       "ol51nnRESModSlotIndex": ol51nnRESModSlotIndex,
       "ol51nnRESModStationAddr": ol51nnRESModStationAddr,
       "ol51nnRESModProtocols": ol51nnRESModProtocols,
       "ol51nnRESPortTable": ol51nnRESPortTable,
       "ol51nnRESPortEntry": ol51nnRESPortEntry,
       "ol51nnRESPortSlotIndex": ol51nnRESPortSlotIndex,
       "ol51nnRESPortIndex": ol51nnRESPortIndex,
       "ol51nnRESPortIpAddress": ol51nnRESPortIpAddress,
       "ol51nnRESPortDipNetwork": ol51nnRESPortDipNetwork,
       "ol51nnRESPortDefNetwork": ol51nnRESPortDefNetwork,
       "ol51nnREE": ol51nnREE,
       "ol51nnREEModTable": ol51nnREEModTable,
       "ol51nnREEModEntry": ol51nnREEModEntry,
       "ol51nnREEModSlotIndex": ol51nnREEModSlotIndex,
       "ol51nnREEModStationAddr": ol51nnREEModStationAddr,
       "ol51nnREEModProtocols": ol51nnREEModProtocols,
       "ol51nnREEPortTable": ol51nnREEPortTable,
       "ol51nnREEPortEntry": ol51nnREEPortEntry,
       "ol51nnREEPortSlotIndex": ol51nnREEPortSlotIndex,
       "ol51nnREEPortIndex": ol51nnREEPortIndex,
       "ol51nnREEPortIpAddress": ol51nnREEPortIpAddress,
       "ol51nnREEPortDipNetwork": ol51nnREEPortDipNetwork,
       "ol51nnREEPortDefNetwork": ol51nnREEPortDefNetwork,
       "ol51nnMAUIF": ol51nnMAUIF,
       "ol51nnMAUIFModTable": ol51nnMAUIFModTable,
       "ol51nnMAUIFModEntry": ol51nnMAUIFModEntry,
       "ol51nnMAUIFModSlotIndex": ol51nnMAUIFModSlotIndex,
       "ol51nnMAUIFPortTable": ol51nnMAUIFPortTable,
       "ol51nnMAUIFPortEntry": ol51nnMAUIFPortEntry,
       "ol51nnMAUIFPortSlotIndex": ol51nnMAUIFPortSlotIndex,
       "ol51nnMAUIFPortIndex": ol51nnMAUIFPortIndex,
       "ol51nnMAUIFPortAdminState": ol51nnMAUIFPortAdminState,
       "ol51nnMAUIFPortBuddySlot": ol51nnMAUIFPortBuddySlot,
       "ol51nnMAUIFPortBuddyPort": ol51nnMAUIFPortBuddyPort,
       "ol51nnMAUIFPortDipAdminState": ol51nnMAUIFPortDipAdminState,
       "ol51nnMAUIFPortDipNetwork": ol51nnMAUIFPortDipNetwork,
       "ol51nnMAUIM": ol51nnMAUIM,
       "ol51nnMAUIMModTable": ol51nnMAUIMModTable,
       "ol51nnMAUIMModEntry": ol51nnMAUIMModEntry,
       "ol51nnMAUIMModSlotIndex": ol51nnMAUIMModSlotIndex,
       "ol51nnMAUIMPortTable": ol51nnMAUIMPortTable,
       "ol51nnMAUIMPortEntry": ol51nnMAUIMPortEntry,
       "ol51nnMAUIMPortSlotIndex": ol51nnMAUIMPortSlotIndex,
       "ol51nnMAUIMPortIndex": ol51nnMAUIMPortIndex,
       "ol51nnMAUIMPortAdminState": ol51nnMAUIMPortAdminState,
       "ol51nnMAUIMPortBuddySlot": ol51nnMAUIMPortBuddySlot,
       "ol51nnMAUIMPortBuddyPort": ol51nnMAUIMPortBuddyPort,
       "ol51nnMAUIMPortDipAdminState": ol51nnMAUIMPortDipAdminState,
       "ol51nnMAUIMPortDipNetwork": ol51nnMAUIMPortDipNetwork,
       "ol51nnMAUIMPortSQETest": ol51nnMAUIMPortSQETest,
       "ol51nnMAUIMPortDipSQETest": ol51nnMAUIMPortDipSQETest,
       "ol51nnMAUIMPortCollision": ol51nnMAUIMPortCollision,
       "ol51nnMAUIMPortDipCollision": ol51nnMAUIMPortDipCollision,
       "ol51nnMAUIMPortHalfStep": ol51nnMAUIMPortHalfStep,
       "ol51nnMAUIMPortDipHalfStep": ol51nnMAUIMPortDipHalfStep,
       "ol5208MTP": ol5208MTP,
       "ol5208MTPModTable": ol5208MTPModTable,
       "ol5208MTPModEntry": ol5208MTPModEntry,
       "ol5208MTPModSlotIndex": ol5208MTPModSlotIndex,
       "ol5208MTPModBypsAdminState": ol5208MTPModBypsAdminState,
       "ol5208MTPModBypsOperState": ol5208MTPModBypsOperState,
       "ol5208MTPModDipCableImp": ol5208MTPModDipCableImp,
       "ol5208MTPPortTable": ol5208MTPPortTable,
       "ol5208MTPPortEntry": ol5208MTPPortEntry,
       "ol5208MTPPortSlotIndex": ol5208MTPPortSlotIndex,
       "ol5208MTPPortIndex": ol5208MTPPortIndex,
       "ol5208MTPPortDipAdminState": ol5208MTPPortDipAdminState,
       "ol5208MTPPortStationType": ol5208MTPPortStationType,
       "ol5208MTPTrunkTable": ol5208MTPTrunkTable,
       "ol5208MTPTrunkEntry": ol5208MTPTrunkEntry,
       "ol5208MTPTrunkSlotIndex": ol5208MTPTrunkSlotIndex,
       "ol5208MTPTrunkIndex": ol5208MTPTrunkIndex,
       "ol5208MTPTrunkDipAdminState": ol5208MTPTrunkDipAdminState,
       "ol5208MTPTrunkCableMon": ol5208MTPTrunkCableMon,
       "ol5208MTPTrunkDipCableMon": ol5208MTPTrunkDipCableMon,
       "ol5208MTPTrunkNetMapState": ol5208MTPTrunkNetMapState,
       "ol5208MTPTrunkExtBcnRecovery": ol5208MTPTrunkExtBcnRecovery,
       "ol51nnMFP": ol51nnMFP,
       "ol51nnMFPModTable": ol51nnMFPModTable,
       "ol51nnMFPModEntry": ol51nnMFPModEntry,
       "ol51nnMFPModSlotIndex": ol51nnMFPModSlotIndex,
       "ol51nnMFPPortTable": ol51nnMFPPortTable,
       "ol51nnMFPPortEntry": ol51nnMFPPortEntry,
       "ol51nnMFPPortSlotIndex": ol51nnMFPPortSlotIndex,
       "ol51nnMFPPortIndex": ol51nnMFPPortIndex,
       "ol51nnMFPPortAdminState": ol51nnMFPPortAdminState,
       "ol51nnMFPPortBuddySlot": ol51nnMFPPortBuddySlot,
       "ol51nnMFPPortBuddyPort": ol51nnMFPPortBuddyPort,
       "ol51nnMFPPortDipAdminState": ol51nnMFPPortDipAdminState,
       "ol51nnMFPPortDipNetwork": ol51nnMFPPortDipNetwork,
       "ol51nnMFPPortLLW": ol51nnMFPPortLLW,
       "ol51nnMFPPortDipLLW": ol51nnMFPPortDipLLW,
       "ol51nnMFPPortHipwr": ol51nnMFPPortHipwr,
       "ol51nnMFPPortDipHipwr": ol51nnMFPPortDipHipwr,
       "ol51nnMFBP": ol51nnMFBP,
       "ol51nnMFBPModTable": ol51nnMFBPModTable,
       "ol51nnMFBPModEntry": ol51nnMFBPModEntry,
       "ol51nnMFBPModSlotIndex": ol51nnMFBPModSlotIndex,
       "ol51nnMFBPPortTable": ol51nnMFBPPortTable,
       "ol51nnMFBPPortEntry": ol51nnMFBPPortEntry,
       "ol51nnMFBPPortSlotIndex": ol51nnMFBPPortSlotIndex,
       "ol51nnMFBPPortIndex": ol51nnMFBPPortIndex,
       "ol51nnMFBPPortAdminState": ol51nnMFBPPortAdminState,
       "ol51nnMFBPPortBuddySlot": ol51nnMFBPPortBuddySlot,
       "ol51nnMFBPPortBuddyPort": ol51nnMFBPPortBuddyPort,
       "ol51nnMFBPPortDipAdminState": ol51nnMFBPPortDipAdminState,
       "ol51nnMFBPPortDipNetwork": ol51nnMFBPPortDipNetwork,
       "ol51nnMFBPPortLLW": ol51nnMFBPPortLLW,
       "ol51nnMFBPPortDipLLW": ol51nnMFBPPortDipLLW,
       "ol51nnMFBPPortHipwr": ol51nnMFBPPortHipwr,
       "ol51nnMFBPPortDipHipwr": ol51nnMFBPPortDipHipwr,
       "ol51nnMTPL": ol51nnMTPL,
       "ol51nnMTPLModTable": ol51nnMTPLModTable,
       "ol51nnMTPLModEntry": ol51nnMTPLModEntry,
       "ol51nnMTPLModSlotIndex": ol51nnMTPLModSlotIndex,
       "ol51nnMTPLModDipNetwork": ol51nnMTPLModDipNetwork,
       "ol51nnMTPLPortTable": ol51nnMTPLPortTable,
       "ol51nnMTPLPortEntry": ol51nnMTPLPortEntry,
       "ol51nnMTPLPortSlotIndex": ol51nnMTPLPortSlotIndex,
       "ol51nnMTPLPortIndex": ol51nnMTPLPortIndex,
       "ol51nnMTPLPortAdminState": ol51nnMTPLPortAdminState,
       "ol51nnMTPLPortBuddySlot": ol51nnMTPLPortBuddySlot,
       "ol51nnMTPLPortBuddyPort": ol51nnMTPLPortBuddyPort,
       "ol51nnMTPLPortDipAdminState": ol51nnMTPLPortDipAdminState,
       "ol51nnMTPLPortLinkInteg": ol51nnMTPLPortLinkInteg,
       "ol51nnMTPLPortDipLinkInteg": ol51nnMTPLPortDipLinkInteg,
       "ol51nnMTPLPortSquelch": ol51nnMTPLPortSquelch,
       "ol51nnMTPLPortJabber": ol51nnMTPLPortJabber,
       "ol51nnMTPLPortDipJabber": ol51nnMTPLPortDipJabber,
       "ol51nnMTPPL": ol51nnMTPPL,
       "ol51nnMTPPLModTable": ol51nnMTPPLModTable,
       "ol51nnMTPPLModEntry": ol51nnMTPPLModEntry,
       "ol51nnMTPPLModSlotIndex": ol51nnMTPPLModSlotIndex,
       "ol51nnMTPPLPortTable": ol51nnMTPPLPortTable,
       "ol51nnMTPPLPortEntry": ol51nnMTPPLPortEntry,
       "ol51nnMTPPLPortSlotIndex": ol51nnMTPPLPortSlotIndex,
       "ol51nnMTPPLPortIndex": ol51nnMTPPLPortIndex,
       "ol51nnMTPPLPortAdminState": ol51nnMTPPLPortAdminState,
       "ol51nnMTPPLPortBuddySlot": ol51nnMTPPLPortBuddySlot,
       "ol51nnMTPPLPortBuddyPort": ol51nnMTPPLPortBuddyPort,
       "ol51nnMTPPLPortDipAdminState": ol51nnMTPPLPortDipAdminState,
       "ol51nnMTPPLPortDipNetwork": ol51nnMTPPLPortDipNetwork,
       "ol51nnMTPPLPortLinkInteg": ol51nnMTPPLPortLinkInteg,
       "ol51nnMTPPLPortDipLinkInteg": ol51nnMTPPLPortDipLinkInteg,
       "ol51nnMTPPLPortSquelch": ol51nnMTPPLPortSquelch,
       "ol51nnMTPPLPortJabber": ol51nnMTPPLPortJabber,
       "ol51nnMTPPLPortDipJabber": ol51nnMTPPLPortDipJabber,
       "ol52nnMTP": ol52nnMTP,
       "ol52nnMTPModTable": ol52nnMTPModTable,
       "ol52nnMTPModEntry": ol52nnMTPModEntry,
       "ol52nnMTPModSlotIndex": ol52nnMTPModSlotIndex,
       "ol52nnMTPModRingSpeed": ol52nnMTPModRingSpeed,
       "ol52nnMTPModDipRingSpeed": ol52nnMTPModDipRingSpeed,
       "ol52nnMTPModCableImp": ol52nnMTPModCableImp,
       "ol52nnMTPModDipCableImp": ol52nnMTPModDipCableImp,
       "ol52nnMTPPortTable": ol52nnMTPPortTable,
       "ol52nnMTPPortEntry": ol52nnMTPPortEntry,
       "ol52nnMTPPortSlotIndex": ol52nnMTPPortSlotIndex,
       "ol52nnMTPPortIndex": ol52nnMTPPortIndex,
       "ol52nnMTPPortDipAdminState": ol52nnMTPPortDipAdminState,
       "ol52nnMTPPortStationType": ol52nnMTPPortStationType,
       "ol52nnMTPTrunkTable": ol52nnMTPTrunkTable,
       "ol52nnMTPTrunkEntry": ol52nnMTPTrunkEntry,
       "ol52nnMTPTrunkSlotIndex": ol52nnMTPTrunkSlotIndex,
       "ol52nnMTPTrunkIndex": ol52nnMTPTrunkIndex,
       "ol52nnMTPTrunkDipAdminState": ol52nnMTPTrunkDipAdminState,
       "ol52nnMFR": ol52nnMFR,
       "ol52nnMFRModTable": ol52nnMFRModTable,
       "ol52nnMFRModEntry": ol52nnMFRModEntry,
       "ol52nnMFRModSlotIndex": ol52nnMFRModSlotIndex,
       "ol52nnMFRModRingSpeed": ol52nnMFRModRingSpeed,
       "ol52nnMFRModDipRingSpeed": ol52nnMFRModDipRingSpeed,
       "ol52nnMFRPortTable": ol52nnMFRPortTable,
       "ol52nnMFRPortEntry": ol52nnMFRPortEntry,
       "ol52nnMFRPortSlotIndex": ol52nnMFRPortSlotIndex,
       "ol52nnMFRPortIndex": ol52nnMFRPortIndex,
       "ol52nnMFRPortDipAdminState": ol52nnMFRPortDipAdminState,
       "ol52nnMFRPortCableImp": ol52nnMFRPortCableImp,
       "ol52nnMFRPortStationType": ol52nnMFRPortStationType,
       "ol52nnMFRTrunkTable": ol52nnMFRTrunkTable,
       "ol52nnMFRTrunkEntry": ol52nnMFRTrunkEntry,
       "ol52nnMFRTrunkSlotIndex": ol52nnMFRTrunkSlotIndex,
       "ol52nnMFRTrunkIndex": ol52nnMFRTrunkIndex,
       "ol52nnMFRTrunkDipAdminState": ol52nnMFRTrunkDipAdminState,
       "ol52nnMFRTrunkCableMon": ol52nnMFRTrunkCableMon,
       "ol52nnMFRTrunkDipCableMon": ol52nnMFRTrunkDipCableMon,
       "ol52nnMFRTrunkCompMode": ol52nnMFRTrunkCompMode,
       "ol52nnMFRTrunkDipCompMode": ol52nnMFRTrunkDipCompMode,
       "ol52nnMFRTrunkNetMapState": ol52nnMFRTrunkNetMapState,
       "ol52nnMFRTrunkExtBcnRecovery": ol52nnMFRTrunkExtBcnRecovery,
       "ol52nnMFRTrunkBuddySlot": ol52nnMFRTrunkBuddySlot,
       "ol52nnMFRTrunkAdminState": ol52nnMFRTrunkAdminState,
       "ol51nnMTS": ol51nnMTS,
       "ol51nnMTSModTable": ol51nnMTSModTable,
       "ol51nnMTSModEntry": ol51nnMTSModEntry,
       "ol51nnMTSModSlotIndex": ol51nnMTSModSlotIndex,
       "ol51nnMTSModProtocols": ol51nnMTSModProtocols,
       "ol51nnMTSModIpAddress": ol51nnMTSModIpAddress,
       "ol51nnMTSModTCPPort": ol51nnMTSModTCPPort,
       "ol51nnMTSModStationAddr": ol51nnMTSModStationAddr,
       "ol51nnMTSModDipNetwork": ol51nnMTSModDipNetwork,
       "ol51nnMTSModCPURev": ol51nnMTSModCPURev,
       "ol51nnMTSPortTable": ol51nnMTSPortTable,
       "ol51nnMTSPortEntry": ol51nnMTSPortEntry,
       "ol51nnMTSPortSlotIndex": ol51nnMTSPortSlotIndex,
       "ol51nnMTSPortIndex": ol51nnMTSPortIndex,
       "ol51nnMTSPortAdminState": ol51nnMTSPortAdminState,
       "ol51nnMTSPortOperState": ol51nnMTSPortOperState,
       "ol51nnMFL": ol51nnMFL,
       "ol51nnMFLModTable": ol51nnMFLModTable,
       "ol51nnMFLModEntry": ol51nnMFLModEntry,
       "ol51nnMFLModSlotIndex": ol51nnMFLModSlotIndex,
       "ol51nnMFLModDipNetwork": ol51nnMFLModDipNetwork,
       "ol51nnMFLPortTable": ol51nnMFLPortTable,
       "ol51nnMFLPortEntry": ol51nnMFLPortEntry,
       "ol51nnMFLPortSlotIndex": ol51nnMFLPortSlotIndex,
       "ol51nnMFLPortIndex": ol51nnMFLPortIndex,
       "ol51nnMFLPortAdminState": ol51nnMFLPortAdminState,
       "ol51nnMFLPortBuddySlot": ol51nnMFLPortBuddySlot,
       "ol51nnMFLPortBuddyPort": ol51nnMFLPortBuddyPort,
       "ol51nnMFLPortDipAdminState": ol51nnMFLPortDipAdminState,
       "ol50nnMRCTL": ol50nnMRCTL,
       "ol50nnMRCTLModTable": ol50nnMRCTLModTable,
       "ol50nnMRCTLModEntry": ol50nnMRCTLModEntry,
       "ol50nnMRCTLModSlotIndex": ol50nnMRCTLModSlotIndex,
       "ol50nnMRCTLModOperState": ol50nnMRCTLModOperState,
       "ol50nnMRCTLModClockStatus": ol50nnMRCTLModClockStatus,
       "ol50nnMRCTLModTempStatus": ol50nnMRCTLModTempStatus,
       "ol51nnMFB": ol51nnMFB,
       "ol51nnMFBModTable": ol51nnMFBModTable,
       "ol51nnMFBModEntry": ol51nnMFBModEntry,
       "ol51nnMFBModSlotIndex": ol51nnMFBModSlotIndex,
       "ol51nnMFBModDipNetwork": ol51nnMFBModDipNetwork,
       "ol51nnMFBModLLW": ol51nnMFBModLLW,
       "ol51nnMFBModDipLLW": ol51nnMFBModDipLLW,
       "ol51nnMFBPortTable": ol51nnMFBPortTable,
       "ol51nnMFBPortEntry": ol51nnMFBPortEntry,
       "ol51nnMFBPortSlotIndex": ol51nnMFBPortSlotIndex,
       "ol51nnMFBPortIndex": ol51nnMFBPortIndex,
       "ol51nnMFBPortAdminState": ol51nnMFBPortAdminState,
       "ol51nnMFBPortBuddySlot": ol51nnMFBPortBuddySlot,
       "ol51nnMFBPortBuddyPort": ol51nnMFBPortBuddyPort,
       "ol51nnMFBPortDipAdminState": ol51nnMFBPortDipAdminState,
       "ol53nnMMGT": ol53nnMMGT,
       "ol53nnMMGTModTable": ol53nnMMGTModTable,
       "ol53nnMMGTModEntry": ol53nnMMGTModEntry,
       "ol53nnMMGTModSlotIndex": ol53nnMMGTModSlotIndex,
       "ol53nnMMGTModMasterPriority": ol53nnMMGTModMasterPriority,
       "ol53nnMMGTModMasterStatus": ol53nnMMGTModMasterStatus,
       "ol53nnMMGTModStationAddr": ol53nnMMGTModStationAddr,
       "ol53nnMMGTModIpAddress": ol53nnMMGTModIpAddress,
       "ol53nnMMGTModDownStreamMAC": ol53nnMMGTModDownStreamMAC,
       "ol53nnMMGTModUpStreamMAC": ol53nnMMGTModUpStreamMAC,
       "ol53nnMMGTModfddiMACPath": ol53nnMMGTModfddiMACPath,
       "ol53nnMMGTModDownStreamModule": ol53nnMMGTModDownStreamModule,
       "ol53nnMMGTModUpStreamModule": ol53nnMMGTModUpStreamModule,
       "ol53nnMMGTModDownStreamOperPath": ol53nnMMGTModDownStreamOperPath,
       "ol53nnMMGTModUpStreamOperPath": ol53nnMMGTModUpStreamOperPath,
       "ol53nnMMGTModRingInfo": ol53nnMMGTModRingInfo,
       "ol53nnMMGTPortTable": ol53nnMMGTPortTable,
       "ol53nnMMGTPortEntry": ol53nnMMGTPortEntry,
       "ol53nnMMGTPortSlotIndex": ol53nnMMGTPortSlotIndex,
       "ol53nnMMGTPortIndex": ol53nnMMGTPortIndex,
       "ol53nnMMGTPortConfig": ol53nnMMGTPortConfig,
       "ol53nnMMGTPortPcmState": ol53nnMMGTPortPcmState,
       "ol53nnMMGTPortConnectState": ol53nnMMGTPortConnectState,
       "ol53nnMMGTPortNeighbor": ol53nnMMGTPortNeighbor,
       "ol53nnMMGTPortRemoteMACIndicated": ol53nnMMGTPortRemoteMACIndicated,
       "ol53nnMMGTPortBSFlag": ol53nnMMGTPortBSFlag,
       "ol53nnMMGTPortPCWithhold": ol53nnMMGTPortPCWithhold,
       "ol53nnMMGTPortLerCondition": ol53nnMMGTPortLerCondition,
       "ol53nnMMGTTrunkTable": ol53nnMMGTTrunkTable,
       "ol53nnMMGTTrunkEntry": ol53nnMMGTTrunkEntry,
       "ol53nnMMGTTrunkSlotIndex": ol53nnMMGTTrunkSlotIndex,
       "ol53nnMMGTTrunkIndex": ol53nnMMGTTrunkIndex,
       "ol53nnMFBMIC": ol53nnMFBMIC,
       "ol53nnMFBMICModTable": ol53nnMFBMICModTable,
       "ol53nnMFBMICModEntry": ol53nnMFBMICModEntry,
       "ol53nnMFBMICModSlotIndex": ol53nnMFBMICModSlotIndex,
       "ol53nnMFBMICModDownStreamModule": ol53nnMFBMICModDownStreamModule,
       "ol53nnMFBMICModUpStreamModule": ol53nnMFBMICModUpStreamModule,
       "ol53nnMFBMICModDownStreamOperPath": ol53nnMFBMICModDownStreamOperPath,
       "ol53nnMFBMICModUpStreamOperPath": ol53nnMFBMICModUpStreamOperPath,
       "ol53nnMFBMICModRingInfo": ol53nnMFBMICModRingInfo,
       "ol53nnMFBMICPortTable": ol53nnMFBMICPortTable,
       "ol53nnMFBMICPortEntry": ol53nnMFBMICPortEntry,
       "ol53nnMFBMICPortSlotIndex": ol53nnMFBMICPortSlotIndex,
       "ol53nnMFBMICPortIndex": ol53nnMFBMICPortIndex,
       "ol53nnMFBMICPortConfig": ol53nnMFBMICPortConfig,
       "ol53nnMFBMICPortPcmState": ol53nnMFBMICPortPcmState,
       "ol53nnMFBMICPortConnectState": ol53nnMFBMICPortConnectState,
       "ol53nnMFBMICPortNeighbor": ol53nnMFBMICPortNeighbor,
       "ol53nnMFBMICPortRemoteMACIndicated": ol53nnMFBMICPortRemoteMACIndicated,
       "ol53nnMFBMICPortBSFlag": ol53nnMFBMICPortBSFlag,
       "ol53nnMFBMICPortPCWithhold": ol53nnMFBMICPortPCWithhold,
       "ol53nnMFBMICPortLerCondition": ol53nnMFBMICPortLerCondition,
       "ol53nnMFBMICTrunkTable": ol53nnMFBMICTrunkTable,
       "ol53nnMFBMICTrunkEntry": ol53nnMFBMICTrunkEntry,
       "ol53nnMFBMICTrunkSlotIndex": ol53nnMFBMICTrunkSlotIndex,
       "ol53nnMFBMICTrunkIndex": ol53nnMFBMICTrunkIndex,
       "ol53nnMFIBST": ol53nnMFIBST,
       "ol53nnMFIBSTModTable": ol53nnMFIBSTModTable,
       "ol53nnMFIBSTModEntry": ol53nnMFIBSTModEntry,
       "ol53nnMFIBSTModSlotIndex": ol53nnMFIBSTModSlotIndex,
       "ol53nnMFIBSTModDownStreamModule": ol53nnMFIBSTModDownStreamModule,
       "ol53nnMFIBSTModUpStreamModule": ol53nnMFIBSTModUpStreamModule,
       "ol53nnMFIBSTModDownStreamOperPath": ol53nnMFIBSTModDownStreamOperPath,
       "ol53nnMFIBSTModUpStreamOperPath": ol53nnMFIBSTModUpStreamOperPath,
       "ol53nnMFIBSTModRingInfo": ol53nnMFIBSTModRingInfo,
       "ol53nnMFIBSTPortTable": ol53nnMFIBSTPortTable,
       "ol53nnMFIBSTPortEntry": ol53nnMFIBSTPortEntry,
       "ol53nnMFIBSTPortSlotIndex": ol53nnMFIBSTPortSlotIndex,
       "ol53nnMFIBSTPortIndex": ol53nnMFIBSTPortIndex,
       "ol53nnMFIBSTPortConfig": ol53nnMFIBSTPortConfig,
       "ol53nnMFIBSTPortPcmState": ol53nnMFIBSTPortPcmState,
       "ol53nnMFIBSTPortConnectState": ol53nnMFIBSTPortConnectState,
       "ol53nnMFIBSTPortNeighbor": ol53nnMFIBSTPortNeighbor,
       "ol53nnMFIBSTPortRemoteMACIndicated": ol53nnMFIBSTPortRemoteMACIndicated,
       "ol53nnMFIBSTPortBSFlag": ol53nnMFIBSTPortBSFlag,
       "ol53nnMFIBSTPortPCWithhold": ol53nnMFIBSTPortPCWithhold,
       "ol53nnMFIBSTPortLerCondition": ol53nnMFIBSTPortLerCondition,
       "ol53nnMFIBSTTrunkTable": ol53nnMFIBSTTrunkTable,
       "ol53nnMFIBSTTrunkEntry": ol53nnMFIBSTTrunkEntry,
       "ol53nnMFIBSTTrunkSlotIndex": ol53nnMFIBSTTrunkSlotIndex,
       "ol53nnMFIBSTTrunkIndex": ol53nnMFIBSTTrunkIndex,
       "ol53nnMSTP": ol53nnMSTP,
       "ol53nnMSTPModTable": ol53nnMSTPModTable,
       "ol53nnMSTPModEntry": ol53nnMSTPModEntry,
       "ol53nnMSTPModSlotIndex": ol53nnMSTPModSlotIndex,
       "ol53nnMSTPModDownStreamModule": ol53nnMSTPModDownStreamModule,
       "ol53nnMSTPModUpStreamModule": ol53nnMSTPModUpStreamModule,
       "ol53nnMSTPModDownStreamOperPath": ol53nnMSTPModDownStreamOperPath,
       "ol53nnMSTPModUpStreamOperPath": ol53nnMSTPModUpStreamOperPath,
       "ol53nnMSTPModRingInfo": ol53nnMSTPModRingInfo,
       "ol53nnMSTPPortTable": ol53nnMSTPPortTable,
       "ol53nnMSTPPortEntry": ol53nnMSTPPortEntry,
       "ol53nnMSTPPortSlotIndex": ol53nnMSTPPortSlotIndex,
       "ol53nnMSTPPortIndex": ol53nnMSTPPortIndex,
       "ol53nnMSTPPortConfig": ol53nnMSTPPortConfig,
       "ol53nnMSTPPortPcmState": ol53nnMSTPPortPcmState,
       "ol53nnMSTPPortConnectState": ol53nnMSTPPortConnectState,
       "ol53nnMSTPPortNeighbor": ol53nnMSTPPortNeighbor,
       "ol53nnMSTPPortRemoteMACIndicated": ol53nnMSTPPortRemoteMACIndicated,
       "ol53nnMSTPPortBSFlag": ol53nnMSTPPortBSFlag,
       "ol53nnMSTPPortPCWithhold": ol53nnMSTPPortPCWithhold,
       "ol53nnMSTPPortLerCondition": ol53nnMSTPPortLerCondition,
       "ol53nnMSTPPortPersonality": ol53nnMSTPPortPersonality,
       "ol53nnMSTPTrunkTable": ol53nnMSTPTrunkTable,
       "ol53nnMSTPTrunkEntry": ol53nnMSTPTrunkEntry,
       "ol53nnMSTPTrunkSlotIndex": ol53nnMSTPTrunkSlotIndex,
       "ol53nnMSTPTrunkIndex": ol53nnMSTPTrunkIndex,
       "ol51nnMTPCL": ol51nnMTPCL,
       "ol51nnMTPCLModTable": ol51nnMTPCLModTable,
       "ol51nnMTPCLModEntry": ol51nnMTPCLModEntry,
       "ol51nnMTPCLModSlotIndex": ol51nnMTPCLModSlotIndex,
       "ol51nnMTPCLModMonitorConn": ol51nnMTPCLModMonitorConn,
       "ol51nnMTPCLModConn1Network": ol51nnMTPCLModConn1Network,
       "ol51nnMTPCLModConn2Network": ol51nnMTPCLModConn2Network,
       "ol51nnMTPCLModConn1DipNetwork": ol51nnMTPCLModConn1DipNetwork,
       "ol51nnMTPCLModConn2DipNetwork": ol51nnMTPCLModConn2DipNetwork,
       "ol51nnMTPCLModAutoPartition": ol51nnMTPCLModAutoPartition,
       "ol51nnMTPCLPortTable": ol51nnMTPCLPortTable,
       "ol51nnMTPCLPortEntry": ol51nnMTPCLPortEntry,
       "ol51nnMTPCLPortSlotIndex": ol51nnMTPCLPortSlotIndex,
       "ol51nnMTPCLPortIndex": ol51nnMTPCLPortIndex,
       "ol51nnMTPCLPortAdminState": ol51nnMTPCLPortAdminState,
       "ol51nnMTPCLPortBuddySlot": ol51nnMTPCLPortBuddySlot,
       "ol51nnMTPCLPortBuddyPort": ol51nnMTPCLPortBuddyPort,
       "ol51nnMTPCLPortDipAdminState": ol51nnMTPCLPortDipAdminState,
       "ol51nnMTPCLPortLinkInteg": ol51nnMTPCLPortLinkInteg,
       "ol51nnMTPCLPortDipLinkInteg": ol51nnMTPCLPortDipLinkInteg,
       "ol52nnBTT": ol52nnBTT,
       "ol52nnBTTModTable": ol52nnBTTModTable,
       "ol52nnBTTModEntry": ol52nnBTTModEntry,
       "ol52nnBTTModSlotIndex": ol52nnBTTModSlotIndex,
       "ol52nnBTTModBridgeType": ol52nnBTTModBridgeType,
       "ol52nnBTTModSoftwareVersion": ol52nnBTTModSoftwareVersion,
       "ol52nnBTTModSRBridgeNo": ol52nnBTTModSRBridgeNo,
       "ol52nnBTTModNetworkStatus": ol52nnBTTModNetworkStatus,
       "ol52nnBTTPortTable": ol52nnBTTPortTable,
       "ol52nnBTTPortEntry": ol52nnBTTPortEntry,
       "ol52nnBTTPortSlotIndex": ol52nnBTTPortSlotIndex,
       "ol52nnBTTPortIndex": ol52nnBTTPortIndex,
       "ol52nnBTTPortConnector": ol52nnBTTPortConnector,
       "ol52nnBTTPortSTAPState": ol52nnBTTPortSTAPState,
       "ol52nnBTTPortIpAddress": ol52nnBTTPortIpAddress,
       "ol52nnBTTPortMACAddress": ol52nnBTTPortMACAddress,
       "ol52nnBTTPortThroughput": ol52nnBTTPortThroughput,
       "ol52nnBTTPortForwarding": ol52nnBTTPortForwarding,
       "ol52nnBTTPortSRRingNo": ol52nnBTTPortSRRingNo,
       "ol52nnBTTPortRingSpeed": ol52nnBTTPortRingSpeed,
       "ol52nnBTTTrunkTable": ol52nnBTTTrunkTable,
       "ol52nnBTTTrunkEntry": ol52nnBTTTrunkEntry,
       "ol52nnBTTTrunkSlotIndex": ol52nnBTTTrunkSlotIndex,
       "ol52nnBTTTrunkIndex": ol52nnBTTTrunkIndex,
       "ol51nnIx": ol51nnIx,
       "ol51nnIxModTable": ol51nnIxModTable,
       "ol51nnIxModEntry": ol51nnIxModEntry,
       "ol51nnIxModSlotIndex": ol51nnIxModSlotIndex,
       "ol51nnIxModSwType": ol51nnIxModSwType,
       "ol51nnIxModStationAddr": ol51nnIxModStationAddr,
       "ol51nnIxModDipPromDefaults": ol51nnIxModDipPromDefaults,
       "ol51nnIxModProtocols": ol51nnIxModProtocols,
       "ol51nnIxPortTable": ol51nnIxPortTable,
       "ol51nnIxPortEntry": ol51nnIxPortEntry,
       "ol51nnIxPortSlotIndex": ol51nnIxPortSlotIndex,
       "ol51nnIxPortIndex": ol51nnIxPortIndex,
       "ol51nnIxPortDipAdminState": ol51nnIxPortDipAdminState,
       "ol51nnIxPortSTAPState": ol51nnIxPortSTAPState,
       "ol51nnIxPortIpAddress": ol51nnIxPortIpAddress,
       "ol51nnIxPortDipNetwork": ol51nnIxPortDipNetwork,
       "ol51nnIxPortDefNetwork": ol51nnIxPortDefNetwork,
       "ol52nnMMGT": ol52nnMMGT,
       "ol52nnMMGTModTable": ol52nnMMGTModTable,
       "ol52nnMMGTModEntry": ol52nnMMGTModEntry,
       "ol52nnMMGTModSlotIndex": ol52nnMMGTModSlotIndex,
       "ol52nnMMGTModMasterPriority": ol52nnMMGTModMasterPriority,
       "ol52nnMMGTModMasterStatus": ol52nnMMGTModMasterStatus,
       "ol52nnMMGTModStationAddr": ol52nnMMGTModStationAddr,
       "ol52nnMMGTModRingSpeed": ol52nnMMGTModRingSpeed,
       "ol52nnMMGTModNetworkStatus": ol52nnMMGTModNetworkStatus,
       "ol52nnMMGTModMasterNetwork": ol52nnMMGTModMasterNetwork,
       "ol52nnMMGTModLocalMACAddress": ol52nnMMGTModLocalMACAddress,
       "ol52nnMMGTModMACAddressType": ol52nnMMGTModMACAddressType,
       "ol52nnMMGTModActiveMACAddress": ol52nnMMGTModActiveMACAddress,
       "ol52nnMMGTPortTable": ol52nnMMGTPortTable,
       "ol52nnMMGTPortEntry": ol52nnMMGTPortEntry,
       "ol52nnMMGTPortSlotIndex": ol52nnMMGTPortSlotIndex,
       "ol52nnMMGTPortIndex": ol52nnMMGTPortIndex,
       "ol52nnMMGTPortIpAddress": ol52nnMMGTPortIpAddress,
       "ol52nnMMGTTrunkTable": ol52nnMMGTTrunkTable,
       "ol52nnMMGTTrunkEntry": ol52nnMMGTTrunkEntry,
       "ol52nnMMGTTrunkSlotIndex": ol52nnMMGTTrunkSlotIndex,
       "ol52nnMMGTTrunkIndex": ol52nnMMGTTrunkIndex,
       "ol52nnMMGTTrunkCableMon": ol52nnMMGTTrunkCableMon,
       "ol52nnMMGTTrunkNetMapState": ol52nnMMGTTrunkNetMapState,
       "ol52nnMMGTTrunkExtBcnRecovery": ol52nnMMGTTrunkExtBcnRecovery,
       "ol50nnMHCTL": ol50nnMHCTL,
       "ol50nnMHCTLModTable": ol50nnMHCTLModTable,
       "ol50nnMHCTLModEntry": ol50nnMHCTLModEntry,
       "ol50nnMHCTLModSlotIndex": ol50nnMHCTLModSlotIndex,
       "ol50nnMHCTLModOperState": ol50nnMHCTLModOperState,
       "ol50nnMHCTLModClockStatus": ol50nnMHCTLModClockStatus,
       "ol50nnMHCTLModTempStatus": ol50nnMHCTLModTempStatus,
       "ol50nnMHCTLModPDBStatus": ol50nnMHCTLModPDBStatus,
       "ol50nnMHCTLModDipCh1ActCol": ol50nnMHCTLModDipCh1ActCol,
       "ol50nnMHCTLModDipCh2ActCol": ol50nnMHCTLModDipCh2ActCol,
       "ol50nnMHCTLModDipCh3ActCol": ol50nnMHCTLModDipCh3ActCol,
       "oc61nnMCAR": oc61nnMCAR,
       "oc61nnMCARModTable": oc61nnMCARModTable,
       "oc61nnMCARModEntry": oc61nnMCARModEntry,
       "oc61nnMCARModSlotIndex": oc61nnMCARModSlotIndex,
       "oc61nnMCARModSubSlotIndex": oc61nnMCARModSubSlotIndex,
       "oc61nnMCARModBootVersion": oc61nnMCARModBootVersion,
       "oc60nnMMGT": oc60nnMMGT,
       "oc60nnMMGTModTable": oc60nnMMGTModTable,
       "oc60nnMMGTModEntry": oc60nnMMGTModEntry,
       "oc60nnMMGTModSlotIndex": oc60nnMMGTModSlotIndex,
       "oc60nnMMGTModSubSlotIndex": oc60nnMMGTModSubSlotIndex,
       "oc60nnMMGTModBootVersion": oc60nnMMGTModBootVersion,
       "oc60nnMMGTModMasterPriority": oc60nnMMGTModMasterPriority,
       "oc60nnMMGTModMasterStatus": oc60nnMMGTModMasterStatus,
       "oc60nnMMGTModHubSerial": oc60nnMMGTModHubSerial,
       "oc61nnDMGT": oc61nnDMGT,
       "oc61nnDMGTModTable": oc61nnDMGTModTable,
       "oc61nnDMGTModEntry": oc61nnDMGTModEntry,
       "oc61nnDMGTModSlotIndex": oc61nnDMGTModSlotIndex,
       "oc61nnDMGTModSubSlotIndex": oc61nnDMGTModSubSlotIndex,
       "oc61nnDMGTModBootVersion": oc61nnDMGTModBootVersion,
       "oc61nnDMGTModIpAddress": oc61nnDMGTModIpAddress,
       "oc61nnDMGTModSubnetMask": oc61nnDMGTModSubnetMask,
       "oc61nnDMGTModDefaultGateway": oc61nnDMGTModDefaultGateway,
       "oc61nnDMGTModStationAddr": oc61nnDMGTModStationAddr,
       "oc61nnDMGTModInterfaceMode": oc61nnDMGTModInterfaceMode,
       "oc61nnDMGTModRMONHostStatsMode": oc61nnDMGTModRMONHostStatsMode,
       "oc61nnMFBP": oc61nnMFBP,
       "oc61nnMFBPPortTable": oc61nnMFBPPortTable,
       "oc61nnMFBPPortEntry": oc61nnMFBPPortEntry,
       "oc61nnMFBPPortSlotIndex": oc61nnMFBPPortSlotIndex,
       "oc61nnMFBPPortIndex": oc61nnMFBPPortIndex,
       "oc61nnMFBPPortAdminState": oc61nnMFBPPortAdminState,
       "oc61nnMFBPPortBuddySlot": oc61nnMFBPPortBuddySlot,
       "oc61nnMFBPPortBuddyPort": oc61nnMFBPPortBuddyPort,
       "oc61nnMFBPPortDipNetwork": oc61nnMFBPPortDipNetwork,
       "oc61nnMFBPPortHipwr": oc61nnMFBPPortHipwr,
       "oc61nnMFBPModTable": oc61nnMFBPModTable,
       "oc61nnMFBPModEntry": oc61nnMFBPModEntry,
       "oc61nnMFBPModSlotIndex": oc61nnMFBPModSlotIndex,
       "oc61nnMFBPModSubSlotIndex": oc61nnMFBPModSubSlotIndex,
       "oc61nnMFBPModBootVersion": oc61nnMFBPModBootVersion,
       "oc61nnMFBPModDipNVRam": oc61nnMFBPModDipNVRam,
       "oc61nnMTPL": oc61nnMTPL,
       "oc61nnMTPLPortTable": oc61nnMTPLPortTable,
       "oc61nnMTPLPortEntry": oc61nnMTPLPortEntry,
       "oc61nnMTPLPortSlotIndex": oc61nnMTPLPortSlotIndex,
       "oc61nnMTPLPortIndex": oc61nnMTPLPortIndex,
       "oc61nnMTPLPortAdminState": oc61nnMTPLPortAdminState,
       "oc61nnMTPLPortBuddySlot": oc61nnMTPLPortBuddySlot,
       "oc61nnMTPLPortBuddyPort": oc61nnMTPLPortBuddyPort,
       "oc61nnMTPLPortDipNetwork": oc61nnMTPLPortDipNetwork,
       "oc61nnMTPLPortLinkInteg": oc61nnMTPLPortLinkInteg,
       "oc61nnMTPLPortAutoPolarity": oc61nnMTPLPortAutoPolarity,
       "oc61nnMTPLModTable": oc61nnMTPLModTable,
       "oc61nnMTPLModEntry": oc61nnMTPLModEntry,
       "oc61nnMTPLModSlotIndex": oc61nnMTPLModSlotIndex,
       "oc61nnMTPLModSubSlotIndex": oc61nnMTPLModSubSlotIndex,
       "oc61nnMTPLModBootVersion": oc61nnMTPLModBootVersion,
       "oc61nnMTPLModDipNVRam": oc61nnMTPLModDipNVRam,
       "ol51nnMTPLS": ol51nnMTPLS,
       "ol51nnMTPLSModTable": ol51nnMTPLSModTable,
       "ol51nnMTPLSModEntry": ol51nnMTPLSModEntry,
       "ol51nnMTPLSModSlotIndex": ol51nnMTPLSModSlotIndex,
       "ol51nnMTPLSModDipNetwork": ol51nnMTPLSModDipNetwork,
       "ol51nnMTPLSModAutoPartition": ol51nnMTPLSModAutoPartition,
       "ol51nnMTPLSPortTable": ol51nnMTPLSPortTable,
       "ol51nnMTPLSPortEntry": ol51nnMTPLSPortEntry,
       "ol51nnMTPLSPortSlotIndex": ol51nnMTPLSPortSlotIndex,
       "ol51nnMTPLSPortIndex": ol51nnMTPLSPortIndex,
       "ol51nnMTPLSPortAdminState": ol51nnMTPLSPortAdminState,
       "ol51nnMTPLSPortDipAdminState": ol51nnMTPLSPortDipAdminState,
       "ol51nnMTPLSPortDipSecurity": ol51nnMTPLSPortDipSecurity,
       "ol51nnMTPLSPortBuddySlot": ol51nnMTPLSPortBuddySlot,
       "ol51nnMTPLSPortBuddyPort": ol51nnMTPLSPortBuddyPort,
       "ol51nnMTPLSPortLinkInteg": ol51nnMTPLSPortLinkInteg,
       "ol51nnMTPLSPortDipLinkInteg": ol51nnMTPLSPortDipLinkInteg,
       "oc60nnMRCTL": oc60nnMRCTL,
       "ol60nnMRCTLModTable": ol60nnMRCTLModTable,
       "ol60nnMRCTLModEntry": ol60nnMRCTLModEntry,
       "ol60nnMRCTLModSlotIndex": ol60nnMRCTLModSlotIndex,
       "ol60nnMRCTLModOperState": ol60nnMRCTLModOperState,
       "ol60nnMRCTLModClockStatus": ol60nnMRCTLModClockStatus,
       "ol60nnMRCTLModTempStatus": ol60nnMRCTLModTempStatus,
       "oc60nnMRCTLModTable": oc60nnMRCTLModTable,
       "oc60nnMRCTLModEntry": oc60nnMRCTLModEntry,
       "oc60nnMRCTLModSlotIndex": oc60nnMRCTLModSlotIndex,
       "oc60nnMRCTLModSubSlotIndex": oc60nnMRCTLModSubSlotIndex,
       "oc60nnMRCTLModBootVersion": oc60nnMRCTLModBootVersion,
       "oc60nnMRCTLModOperState": oc60nnMRCTLModOperState,
       "oc60nnMRCTLModClockStatus": oc60nnMRCTLModClockStatus,
       "oc60nnMRCTLModTempStatus": oc60nnMRCTLModTempStatus,
       "oc60nnMRCTLModAtoDConverterStatus": oc60nnMRCTLModAtoDConverterStatus,
       "oc60nnMRCTLModPS1Status": oc60nnMRCTLModPS1Status,
       "oc60nnMRCTLModPS2Status": oc60nnMRCTLModPS2Status,
       "oc60nnMRCTLModPS3Status": oc60nnMRCTLModPS3Status,
       "oc60nnMRCTLModPS4Status": oc60nnMRCTLModPS4Status,
       "ol50nnMRCLS": ol50nnMRCLS,
       "ol50nnMRCLSModTable": ol50nnMRCLSModTable,
       "ol50nnMRCLSModEntry": ol50nnMRCLSModEntry,
       "ol50nnMRCLSModSlotIndex": ol50nnMRCLSModSlotIndex,
       "ol50nnMRCLSModOperState": ol50nnMRCLSModOperState,
       "ol50nnMRCLSModClockStatus": ol50nnMRCLSModClockStatus,
       "ol50nnMRCLSModTempStatus": ol50nnMRCLSModTempStatus,
       "ol41nnHMTP": ol41nnHMTP,
       "ol41nnHMTPModTable": ol41nnHMTPModTable,
       "ol41nnHMTPModEntry": ol41nnHMTPModEntry,
       "ol41nnHMTPModSlotIndex": ol41nnHMTPModSlotIndex,
       "ol41nnHMTPModSerialNo": ol41nnHMTPModSerialNo,
       "ol41nnHMTPModProtocols": ol41nnHMTPModProtocols,
       "ol41nnHMTPModIpAddress": ol41nnHMTPModIpAddress,
       "ol41nnHMTPPortTable": ol41nnHMTPPortTable,
       "ol41nnHMTPPortEntry": ol41nnHMTPPortEntry,
       "ol41nnHMTPPortSlotIndex": ol41nnHMTPPortSlotIndex,
       "ol41nnHMTPPortIndex": ol41nnHMTPPortIndex,
       "ol41nnHMTPPortReset": ol41nnHMTPPortReset,
       "ol41nnHMTPPortLinkInteg": ol41nnHMTPPortLinkInteg,
       "ol41nnHETP": ol41nnHETP,
       "ol41nnHETPModTable": ol41nnHETPModTable,
       "ol41nnHETPModEntry": ol41nnHETPModEntry,
       "ol41nnHETPModSlotIndex": ol41nnHETPModSlotIndex,
       "ol41nnHETPModSerialNo": ol41nnHETPModSerialNo,
       "ol41nnHETPPortTable": ol41nnHETPPortTable,
       "ol41nnHETPPortEntry": ol41nnHETPPortEntry,
       "ol41nnHETPPortSlotIndex": ol41nnHETPPortSlotIndex,
       "ol41nnHETPPortIndex": ol41nnHETPPortIndex,
       "ol41nnHETPPortReset": ol41nnHETPPortReset,
       "ol41nnHETPPortLinkInteg": ol41nnHETPPortLinkInteg,
       "ol52nnMEC": ol52nnMEC,
       "ol52nnMECModTable": ol52nnMECModTable,
       "ol52nnMECModEntry": ol52nnMECModEntry,
       "ol52nnMECModSlotIndex": ol52nnMECModSlotIndex,
       "ol52nnMECModSoftwareVersion": ol52nnMECModSoftwareVersion,
       "ol52nnMECModSystemStatusCode": ol52nnMECModSystemStatusCode,
       "ol52nnMECModRingSpeed": ol52nnMECModRingSpeed,
       "ol52nnMECModNetworkStatus": ol52nnMECModNetworkStatus,
       "ol52nnMECModIpAddress": ol52nnMECModIpAddress,
       "ol52nnMECModMACStationAddr": ol52nnMECModMACStationAddr,
       "ol52nnMECPortTable": ol52nnMECPortTable,
       "ol52nnMECPortEntry": ol52nnMECPortEntry,
       "ol52nnMECPortSlotIndex": ol52nnMECPortSlotIndex,
       "ol52nnMECPortIndex": ol52nnMECPortIndex,
       "ol52nnMECTrunkTable": ol52nnMECTrunkTable,
       "ol52nnMECTrunkEntry": ol52nnMECTrunkEntry,
       "ol52nnMECTrunkSlotIndex": ol52nnMECTrunkSlotIndex,
       "ol52nnMECTrunkIndex": ol52nnMECTrunkIndex,
       "ol53nnMTDDI": ol53nnMTDDI,
       "ol53nnMTDDIModTable": ol53nnMTDDIModTable,
       "ol53nnMTDDIModEntry": ol53nnMTDDIModEntry,
       "ol53nnMTDDIModSlotIndex": ol53nnMTDDIModSlotIndex,
       "ol53nnMTDDIModDownStreamModule": ol53nnMTDDIModDownStreamModule,
       "ol53nnMTDDIModUpStreamModule": ol53nnMTDDIModUpStreamModule,
       "ol53nnMTDDIModDownStreamOperPath": ol53nnMTDDIModDownStreamOperPath,
       "ol53nnMTDDIModUpStreamOperPath": ol53nnMTDDIModUpStreamOperPath,
       "ol53nnMTDDIModRingInfo": ol53nnMTDDIModRingInfo,
       "ol53nnMTDDIPortTable": ol53nnMTDDIPortTable,
       "ol53nnMTDDIPortEntry": ol53nnMTDDIPortEntry,
       "ol53nnMTDDIPortSlotIndex": ol53nnMTDDIPortSlotIndex,
       "ol53nnMTDDIPortIndex": ol53nnMTDDIPortIndex,
       "ol53nnMTDDIPortConfig": ol53nnMTDDIPortConfig,
       "ol53nnMTDDIPortPcmState": ol53nnMTDDIPortPcmState,
       "ol53nnMTDDIPortConnectState": ol53nnMTDDIPortConnectState,
       "ol53nnMTDDIPortNeighbor": ol53nnMTDDIPortNeighbor,
       "ol53nnMTDDIPortRemoteMACIndicated": ol53nnMTDDIPortRemoteMACIndicated,
       "ol53nnMTDDIPortBSFlag": ol53nnMTDDIPortBSFlag,
       "ol53nnMTDDIPortPCWithhold": ol53nnMTDDIPortPCWithhold,
       "ol53nnMTDDIPortLerCondition": ol53nnMTDDIPortLerCondition,
       "ol53nnMTDDITrunkTable": ol53nnMTDDITrunkTable,
       "ol53nnMTDDITrunkEntry": ol53nnMTDDITrunkEntry,
       "ol53nnMTDDITrunkSlotIndex": ol53nnMTDDITrunkSlotIndex,
       "ol53nnMTDDITrunkIndex": ol53nnMTDDITrunkIndex,
       "olModSummaryTable": olModSummaryTable,
       "olModSummaryEntry": olModSummaryEntry,
       "olModSummarySlotIndex": olModSummarySlotIndex,
       "olModSummaryInfo": olModSummaryInfo,
       "ocModTable": ocModTable,
       "ocModEntry": ocModEntry,
       "ocModSlotIndex": ocModSlotIndex,
       "ocModSubSlotIndex": ocModSubSlotIndex,
       "ocModType": ocModType,
       "ocModClass": ocModClass,
       "ocModDescr": ocModDescr,
       "ocModVersion": ocModVersion,
       "ocModVendor": ocModVendor,
       "ocModResetModule": ocModResetModule,
       "ocModConfigToDips": ocModConfigToDips,
       "ocModConfigured": ocModConfigured,
       "ocModNetwork": ocModNetwork,
       "ocModNetworkType": ocModNetworkType,
       "ocModStatus": ocModStatus,
       "ocModNumPorts": ocModNumPorts,
       "ocModNumTrunks": ocModNumTrunks,
       "ocModNumSubSlots": ocModNumSubSlots,
       "olNets": olNets,
       "olNet": olNet,
       "olNetDPTable": olNetDPTable,
       "olNetDPEntry": olNetDPEntry,
       "olNetDPDataPath": olNetDPDataPath,
       "olNetDPNetID": olNetDPNetID,
       "olNetSecurityMACTable": olNetSecurityMACTable,
       "olNetSecurityMACEntry": olNetSecurityMACEntry,
       "olNetSecurityMACSlotIndex": olNetSecurityMACSlotIndex,
       "olNetSecurityMACPortIndex": olNetSecurityMACPortIndex,
       "olNetSecurityMACAddress": olNetSecurityMACAddress,
       "olNetSecurityMACMode": olNetSecurityMACMode,
       "olNetSecurityMACStatus": olNetSecurityMACStatus,
       "olNetOlSec": olNetOlSec,
       "olNetOlSecAddrTable": olNetOlSecAddrTable,
       "olNetOlSecAddrEntry": olNetOlSecAddrEntry,
       "olNetOlSecAddrSlotIndex": olNetOlSecAddrSlotIndex,
       "olNetOlSecAddrPortIndex": olNetOlSecAddrPortIndex,
       "olNetOlSecAddrAddress": olNetOlSecAddrAddress,
       "olNetOlSecAddrStatus": olNetOlSecAddrStatus,
       "olNetOlSecControlTable": olNetOlSecControlTable,
       "olNetOlSecControlEntry": olNetOlSecControlEntry,
       "olNetOlSecControlSlotIndex": olNetOlSecControlSlotIndex,
       "olNetOlSecControlPortIndex": olNetOlSecControlPortIndex,
       "olNetOlSecControlMode": olNetOlSecControlMode,
       "olNetOlSecControlSecType": olNetOlSecControlSecType,
       "olNetOlSecControlActOnIntr": olNetOlSecControlActOnIntr,
       "olNetOlSecControlClearAddrs": olNetOlSecControlClearAddrs,
       "olNetOlSecControlAutolearnMask": olNetOlSecControlAutolearnMask,
       "olNetOlSecAutolearn": olNetOlSecAutolearn,
       "olNetOlSecAutolearnTrigger": olNetOlSecAutolearnTrigger,
       "olNetOlSecAutolearnDownload": olNetOlSecAutolearnDownload,
       "olNetOlSecLearnTable": olNetOlSecLearnTable,
       "olNetOlSecLearnEntry": olNetOlSecLearnEntry,
       "olNetOlSecLearnSlotIndex": olNetOlSecLearnSlotIndex,
       "olNetOlSecLearnPortIndex": olNetOlSecLearnPortIndex,
       "olNetOlSecLearnAddress": olNetOlSecLearnAddress,
       "olNetOlSecLearnStatus": olNetOlSecLearnStatus,
       "olNetOlSecIntruderTable": olNetOlSecIntruderTable,
       "olNetOlSecIntruderEntry": olNetOlSecIntruderEntry,
       "olNetOlSecIntruderChronIndex": olNetOlSecIntruderChronIndex,
       "olNetOlSecIntruderSlot": olNetOlSecIntruderSlot,
       "olNetOlSecIntruderPort": olNetOlSecIntruderPort,
       "olNetOlSecIntruderAddress": olNetOlSecIntruderAddress,
       "olNetOlSecIntruderTimeSince": olNetOlSecIntruderTimeSince,
       "olNetOlSecIntruderDisabled": olNetOlSecIntruderDisabled,
       "olNetOlSecPortIntrTable": olNetOlSecPortIntrTable,
       "olNetOlSecPortIntrEntry": olNetOlSecPortIntrEntry,
       "olNetOlSecPortIntrSlotIndex": olNetOlSecPortIntrSlotIndex,
       "olNetOlSecPortIntrPortIndex": olNetOlSecPortIntrPortIndex,
       "olNetOlSecPortIntrChronIndex": olNetOlSecPortIntrChronIndex,
       "olNetOlSecPortIntrAddress": olNetOlSecPortIntrAddress,
       "olNetOlSecPortIntrTimeSince": olNetOlSecPortIntrTimeSince,
       "olNetOlSecPortIntrDisabled": olNetOlSecPortIntrDisabled,
       "olNetOlSecTrap": olNetOlSecTrap,
       "olNetOlSecTrapReason": olNetOlSecTrapReason,
       "olEnet": olEnet,
       "olEnetStatsTable": olEnetStatsTable,
       "olEnetStatsEntry": olEnetStatsEntry,
       "olEnetStatsNetID": olEnetStatsNetID,
       "olEnetStatsFramesRcvdOks": olEnetStatsFramesRcvdOks,
       "olEnetStatsOctetsRcvdOks": olEnetStatsOctetsRcvdOks,
       "olEnetStatsMcastRcvdOks": olEnetStatsMcastRcvdOks,
       "olEnetStatsBcastRcvdOks": olEnetStatsBcastRcvdOks,
       "olEnetStatsFrameTooLongs": olEnetStatsFrameTooLongs,
       "olEnetStatsAlignmentErrors": olEnetStatsAlignmentErrors,
       "olEnetStatsFCSErrors": olEnetStatsFCSErrors,
       "olEnetStatsRunts": olEnetStatsRunts,
       "olEnetStatsLocalColls": olEnetStatsLocalColls,
       "olEnetStatsDropEvents": olEnetStatsDropEvents,
       "olEnetStatsModTable": olEnetStatsModTable,
       "olEnetStatsModEntry": olEnetStatsModEntry,
       "olEnetStatsModNetID": olEnetStatsModNetID,
       "olEnetStatsModSlotIndex": olEnetStatsModSlotIndex,
       "olEnetStatsModFramesRcvdOks": olEnetStatsModFramesRcvdOks,
       "olEnetStatsModOctetsRcvdOks": olEnetStatsModOctetsRcvdOks,
       "olEnetStatsModMcastRcvdOks": olEnetStatsModMcastRcvdOks,
       "olEnetStatsModBcastRcvdOks": olEnetStatsModBcastRcvdOks,
       "olEnetStatsModFrameTooLongs": olEnetStatsModFrameTooLongs,
       "olEnetStatsModAlignmentErrors": olEnetStatsModAlignmentErrors,
       "olEnetStatsModFCSErrors": olEnetStatsModFCSErrors,
       "olEnetStatsModRunts": olEnetStatsModRunts,
       "olEnetStatsPortTable": olEnetStatsPortTable,
       "olEnetStatsPortEntry": olEnetStatsPortEntry,
       "olEnetStatsPortNetID": olEnetStatsPortNetID,
       "olEnetStatsPortSlotIndex": olEnetStatsPortSlotIndex,
       "olEnetStatsPortIndex": olEnetStatsPortIndex,
       "olEnetStatsPortFramesRcvdOks": olEnetStatsPortFramesRcvdOks,
       "olEnetStatsPortOctetsRcvdOks": olEnetStatsPortOctetsRcvdOks,
       "olEnetStatsPortMcastRcvdOks": olEnetStatsPortMcastRcvdOks,
       "olEnetStatsPortBcastRcvdOks": olEnetStatsPortBcastRcvdOks,
       "olEnetStatsPortFrameTooLongs": olEnetStatsPortFrameTooLongs,
       "olEnetStatsPortAlignmentErrors": olEnetStatsPortAlignmentErrors,
       "olEnetStatsPortFCSErrors": olEnetStatsPortFCSErrors,
       "olEnetStatsPortRunts": olEnetStatsPortRunts,
       "olEnetStatsPortSrcAddrChanges": olEnetStatsPortSrcAddrChanges,
       "olEnetStatsPortLastSrcAddr": olEnetStatsPortLastSrcAddr,
       "olEnetStatsPortLastErrAddr": olEnetStatsPortLastErrAddr,
       "olEnetMapTable": olEnetMapTable,
       "olEnetMapEntry": olEnetMapEntry,
       "olEnetMapNetID": olEnetMapNetID,
       "olEnetMapAddress": olEnetMapAddress,
       "olEnetMapSlotIndex": olEnetMapSlotIndex,
       "olEnetMapPortIndex": olEnetMapPortIndex,
       "olEnetMapFrames": olEnetMapFrames,
       "olEnetMapOctets": olEnetMapOctets,
       "olEnetMapTime": olEnetMapTime,
       "chipSnmpDot3RptrMgt": chipSnmpDot3RptrMgt,
       "chipRptrBasicPackage": chipRptrBasicPackage,
       "chipRptrRptrInfo": chipRptrRptrInfo,
       "chipRptrRptrInfoTable": chipRptrRptrInfoTable,
       "chipRptrRptrInfoEntry": chipRptrRptrInfoEntry,
       "chipRptrRptrInfoSlotIndex": chipRptrRptrInfoSlotIndex,
       "chipRptrRptrInfoNetID": chipRptrRptrInfoNetID,
       "chipRptrGroupCapacity": chipRptrGroupCapacity,
       "chipRptrOperStatus": chipRptrOperStatus,
       "chipRptrHealthText": chipRptrHealthText,
       "chipRptrReset": chipRptrReset,
       "chipRptrNonDisruptTest": chipRptrNonDisruptTest,
       "chipRptrTotalPartitionedPorts": chipRptrTotalPartitionedPorts,
       "chipRptrGroupInfo": chipRptrGroupInfo,
       "chipRptrGroupTable": chipRptrGroupTable,
       "chipRptrGroupEntry": chipRptrGroupEntry,
       "chipRptrGroupSlotIndex": chipRptrGroupSlotIndex,
       "chipRptrGroupNetID": chipRptrGroupNetID,
       "chipRptrGroupIndex": chipRptrGroupIndex,
       "chipRptrGroupDescr": chipRptrGroupDescr,
       "chipRptrGroupObjectID": chipRptrGroupObjectID,
       "chipRptrGroupOperStatus": chipRptrGroupOperStatus,
       "chipRptrGroupLastOperStatusChange": chipRptrGroupLastOperStatusChange,
       "chipRptrGroupPortCapacity": chipRptrGroupPortCapacity,
       "chipRptrPortInfo": chipRptrPortInfo,
       "chipRptrPortTable": chipRptrPortTable,
       "chipRptrPortEntry": chipRptrPortEntry,
       "chipRptrPortSlotIndex": chipRptrPortSlotIndex,
       "chipRptrPortNetID": chipRptrPortNetID,
       "chipRptrPortGroupIndex": chipRptrPortGroupIndex,
       "chipRptrPortIndex": chipRptrPortIndex,
       "chipRptrPortAdminStatus": chipRptrPortAdminStatus,
       "chipRptrPortAutoPartitionState": chipRptrPortAutoPartitionState,
       "chipRptrPortOperStatus": chipRptrPortOperStatus,
       "chipRptrMonitorPackage": chipRptrMonitorPackage,
       "chipRptrMonitorRptrInfo": chipRptrMonitorRptrInfo,
       "chipRptrMonitorRptrTable": chipRptrMonitorRptrTable,
       "chipRptrMonitorRptrEntry": chipRptrMonitorRptrEntry,
       "chipRptrMonitorSlotIndex": chipRptrMonitorSlotIndex,
       "chipRptrMonitorNetID": chipRptrMonitorNetID,
       "chipRptrMonitorTransmitCollisions": chipRptrMonitorTransmitCollisions,
       "chipRptrMonitorGroupInfo": chipRptrMonitorGroupInfo,
       "chipRptrMonitorGroupTable": chipRptrMonitorGroupTable,
       "chipRptrMonitorGroupEntry": chipRptrMonitorGroupEntry,
       "chipRptrMonitorGroupSlotIndex": chipRptrMonitorGroupSlotIndex,
       "chipRptrMonitorGroupNetID": chipRptrMonitorGroupNetID,
       "chipRptrMonitorGroupIndex": chipRptrMonitorGroupIndex,
       "chipRptrMonitorGroupTotalFrames": chipRptrMonitorGroupTotalFrames,
       "chipRptrMonitorGroupTotalOctets": chipRptrMonitorGroupTotalOctets,
       "chipRptrMonitorGroupTotalErrors": chipRptrMonitorGroupTotalErrors,
       "chipRptrMonitorPortInfo": chipRptrMonitorPortInfo,
       "chipRptrMonitorPortTable": chipRptrMonitorPortTable,
       "chipRptrMonitorPortEntry": chipRptrMonitorPortEntry,
       "chipRptrMonitorPortSlotIndex": chipRptrMonitorPortSlotIndex,
       "chipRptrMonitorPortNetID": chipRptrMonitorPortNetID,
       "chipRptrMonitorPortGroupIndex": chipRptrMonitorPortGroupIndex,
       "chipRptrMonitorPortIndex": chipRptrMonitorPortIndex,
       "chipRptrMonitorPortReadableFrames": chipRptrMonitorPortReadableFrames,
       "chipRptrMonitorPortReadableOctets": chipRptrMonitorPortReadableOctets,
       "chipRptrMonitorPortFCSErrors": chipRptrMonitorPortFCSErrors,
       "chipRptrMonitorPortAlignmentErrors": chipRptrMonitorPortAlignmentErrors,
       "chipRptrMonitorPortFrameTooLongs": chipRptrMonitorPortFrameTooLongs,
       "chipRptrMonitorPortShortEvents": chipRptrMonitorPortShortEvents,
       "chipRptrMonitorPortRunts": chipRptrMonitorPortRunts,
       "chipRptrMonitorPortCollisions": chipRptrMonitorPortCollisions,
       "chipRptrMonitorPortLateEvents": chipRptrMonitorPortLateEvents,
       "chipRptrMonitorPortVeryLongEvents": chipRptrMonitorPortVeryLongEvents,
       "chipRptrMonitorPortDataRateMismatches": chipRptrMonitorPortDataRateMismatches,
       "chipRptrMonitorPortAutoPartitions": chipRptrMonitorPortAutoPartitions,
       "chipRptrMonitorPortTotalErrors": chipRptrMonitorPortTotalErrors,
       "chipRptrAddrTrackPackage": chipRptrAddrTrackPackage,
       "chipRptrAddrTrackRptrInfo": chipRptrAddrTrackRptrInfo,
       "chipRptrAddrTrackGroupInfo": chipRptrAddrTrackGroupInfo,
       "chipRptrAddrTrackPortInfo": chipRptrAddrTrackPortInfo,
       "chipRptrAddrTrackTable": chipRptrAddrTrackTable,
       "chipRptrAddrTrackEntry": chipRptrAddrTrackEntry,
       "chipRptrAddrTrackSlotIndex": chipRptrAddrTrackSlotIndex,
       "chipRptrAddrTrackGroupNetID": chipRptrAddrTrackGroupNetID,
       "chipRptrAddrTrackGroupIndex": chipRptrAddrTrackGroupIndex,
       "chipRptrAddrTrackPortIndex": chipRptrAddrTrackPortIndex,
       "chipRptrAddrTrackLastSourceAddress": chipRptrAddrTrackLastSourceAddress,
       "chipRptrAddrTrackSourceAddrChanges": chipRptrAddrTrackSourceAddrChanges,
       "chipRptrAddrTrackNewLastSrcAddress": chipRptrAddrTrackNewLastSrcAddress,
       "olTRnet": olTRnet,
       "olTRnetMapState": olTRnetMapState,
       "olTRnetStatsTable": olTRnetStatsTable,
       "olTRnetStatsEntry": olTRnetStatsEntry,
       "olTRnetStatsNetID": olTRnetStatsNetID,
       "olTRnetStatsLineErrors": olTRnetStatsLineErrors,
       "olTRnetStatsBurstErrors": olTRnetStatsBurstErrors,
       "olTRnetStatsACErrors": olTRnetStatsACErrors,
       "olTRnetStatsLostFrameErrors": olTRnetStatsLostFrameErrors,
       "olTRnetStatsCongestionErrors": olTRnetStatsCongestionErrors,
       "olTRnetStatsFrameCopiedErrors": olTRnetStatsFrameCopiedErrors,
       "olTRnetStatsTokenErrors": olTRnetStatsTokenErrors,
       "olTRnetStatsDuplicateAddresses": olTRnetStatsDuplicateAddresses,
       "olTRnetStatsBeaconEvents": olTRnetStatsBeaconEvents,
       "olTRnetStatsLastBeaconSender": olTRnetStatsLastBeaconSender,
       "olTRnetStatsLastBeaconNAUN": olTRnetStatsLastBeaconNAUN,
       "olTRnetStatsLastBeaconTime": olTRnetStatsLastBeaconTime,
       "olTRnetStatsLastBeaconAction": olTRnetStatsLastBeaconAction,
       "olTRnetStatsTotalStations": olTRnetStatsTotalStations,
       "olTRnetStatsConcStations": olTRnetStatsConcStations,
       "olTRnetStatsTotalPorts": olTRnetStatsTotalPorts,
       "olTRnetStatsEnabledPorts": olTRnetStatsEnabledPorts,
       "olTRnetStatsActivePorts": olTRnetStatsActivePorts,
       "olTRnetStatsStationTable": olTRnetStatsStationTable,
       "olTRnetStatsStationEntry": olTRnetStatsStationEntry,
       "olTRnetStatsStationNetID": olTRnetStatsStationNetID,
       "olTRnetStatsStationAddr": olTRnetStatsStationAddr,
       "olTRnetStatsStationSlotIndex": olTRnetStatsStationSlotIndex,
       "olTRnetStatsStationPortIndex": olTRnetStatsStationPortIndex,
       "olTRnetStatsStationNAUNAddress": olTRnetStatsStationNAUNAddress,
       "olTRnetStatsStationLineErrors": olTRnetStatsStationLineErrors,
       "olTRnetStatsStationBurstErrors": olTRnetStatsStationBurstErrors,
       "olTRnetStatsStationACErrors": olTRnetStatsStationACErrors,
       "olTRnetStatsStationLostFrameErrors": olTRnetStatsStationLostFrameErrors,
       "olTRnetStatsStationCongestionErrors": olTRnetStatsStationCongestionErrors,
       "olTRnetStatsStationFrameCopiedErrors": olTRnetStatsStationFrameCopiedErrors,
       "olTRnetStatsStationTokenErrors": olTRnetStatsStationTokenErrors,
       "olTRnetStatsStationDuplicateAddresses": olTRnetStatsStationDuplicateAddresses,
       "olTRnetStatsPortTable": olTRnetStatsPortTable,
       "olTRnetStatsPortEntry": olTRnetStatsPortEntry,
       "olTRnetStatsPortSlotIndex": olTRnetStatsPortSlotIndex,
       "olTRnetStatsPortIndex": olTRnetStatsPortIndex,
       "olTRnetStatsPortNetID": olTRnetStatsPortNetID,
       "olTRnetStatsPortTotalStations": olTRnetStatsPortTotalStations,
       "olTRnetStatsPortAddress": olTRnetStatsPortAddress,
       "olTRnetStatsPortLineErrors": olTRnetStatsPortLineErrors,
       "olTRnetStatsPortBurstErrors": olTRnetStatsPortBurstErrors,
       "olTRnetStatsPortACErrors": olTRnetStatsPortACErrors,
       "olTRnetStatsPortLostFrameErrors": olTRnetStatsPortLostFrameErrors,
       "olTRnetStatsPortCongestionErrors": olTRnetStatsPortCongestionErrors,
       "olTRnetStatsPortFrameCopiedErrors": olTRnetStatsPortFrameCopiedErrors,
       "olTRnetStatsPortTokenErrors": olTRnetStatsPortTokenErrors,
       "olTRnetStatsPortDuplicateAddresses": olTRnetStatsPortDuplicateAddresses,
       "olTRnetMapSummary": olTRnetMapSummary,
       "olTRnetMapSummaryLogicalState": olTRnetMapSummaryLogicalState,
       "olTRnetMapSummaryLogicalLock": olTRnetMapSummaryLogicalLock,
       "olTRnetMapSummaryTable": olTRnetMapSummaryTable,
       "olTRnetMapSummaryEntry": olTRnetMapSummaryEntry,
       "olTRnetMapSummaryNetID": olTRnetMapSummaryNetID,
       "olTRnetMapSummaryIndex": olTRnetMapSummaryIndex,
       "olTRnetMapSummary32Stations": olTRnetMapSummary32Stations,
       "olTRTrafTable": olTRTrafTable,
       "olTRTrafEntry": olTRTrafEntry,
       "olTRTrafNetID": olTRTrafNetID,
       "olTRTrafTokenRotationTime": olTRTrafTokenRotationTime,
       "olTRTrafDropEvents": olTRTrafDropEvents,
       "olTRTrafOctets": olTRTrafOctets,
       "olTRTrafFrames": olTRTrafFrames,
       "olTRTrafMacOctets": olTRTrafMacOctets,
       "olTRTrafMacFrames": olTRTrafMacFrames,
       "olTRTrafBroadcastFrames": olTRTrafBroadcastFrames,
       "olTRTrafMulticastFrames": olTRTrafMulticastFrames,
       "olTRTrafFrames18to63Octets": olTRTrafFrames18to63Octets,
       "olTRTrafFrames64to127Octets": olTRTrafFrames64to127Octets,
       "olTRTrafFrames128to255Octets": olTRTrafFrames128to255Octets,
       "olTRTrafFrames256to511Octets": olTRTrafFrames256to511Octets,
       "olTRTrafFrames512to1023Octets": olTRTrafFrames512to1023Octets,
       "olTRTrafFrames1024to2047Octets": olTRTrafFrames1024to2047Octets,
       "olTRTrafFrames2048to4095Octets": olTRTrafFrames2048to4095Octets,
       "olTRTrafFrames4096to8191Octets": olTRTrafFrames4096to8191Octets,
       "olTRTrafFrames8192to18000Octets": olTRTrafFrames8192to18000Octets,
       "olTRTrafFramesGreaterThan18000Octets": olTRTrafFramesGreaterThan18000Octets,
       "olTRTrafControlTable": olTRTrafControlTable,
       "olTRTrafControlEntry": olTRTrafControlEntry,
       "olTRTrafControlNetID": olTRTrafControlNetID,
       "olTRTrafControlLogicalState": olTRTrafControlLogicalState,
       "olTRTrafControlLogicalLock": olTRTrafControlLogicalLock,
       "olTRTrafControlClear": olTRTrafControlClear,
       "olTRTrafControlLastClearTime": olTRTrafControlLastClearTime,
       "olTRTrafControlTotalStations": olTRTrafControlTotalStations,
       "olTRTrafControlStationLastChangeTime": olTRTrafControlStationLastChangeTime,
       "olTRTrafControlPortTotalStations": olTRTrafControlPortTotalStations,
       "olTRTrafControlPortLastChangeTime": olTRTrafControlPortLastChangeTime,
       "olTRTrafControlTopNMaxStations": olTRTrafControlTopNMaxStations,
       "olTRTrafControlTopNTotalStations": olTRTrafControlTopNTotalStations,
       "olTRTrafControlTopNLastChangeTime": olTRTrafControlTopNLastChangeTime,
       "olTRTrafControlTopNInterval": olTRTrafControlTopNInterval,
       "olTRTrafStationTable": olTRTrafStationTable,
       "olTRTrafStationEntry": olTRTrafStationEntry,
       "olTRTrafStationNetID": olTRTrafStationNetID,
       "olTRTrafStationAddress": olTRTrafStationAddress,
       "olTRTrafStationSlotIndex": olTRTrafStationSlotIndex,
       "olTRTrafStationPortIndex": olTRTrafStationPortIndex,
       "olTRTrafStationInFrames": olTRTrafStationInFrames,
       "olTRTrafStationOutFrames": olTRTrafStationOutFrames,
       "olTRTrafStationInOctets": olTRTrafStationInOctets,
       "olTRTrafStationOutOctets": olTRTrafStationOutOctets,
       "olTRTrafStationOutErrors": olTRTrafStationOutErrors,
       "olTRTrafStationOutBroadcastFrames": olTRTrafStationOutBroadcastFrames,
       "olTRTrafStationOutMulticastFrames": olTRTrafStationOutMulticastFrames,
       "olTRTrafPortTable": olTRTrafPortTable,
       "olTRTrafPortEntry": olTRTrafPortEntry,
       "olTRTrafPortSlotIndex": olTRTrafPortSlotIndex,
       "olTRTrafPortPortIndex": olTRTrafPortPortIndex,
       "olTRTrafPortNetID": olTRTrafPortNetID,
       "olTRTrafPortAddress": olTRTrafPortAddress,
       "olTRTrafPortInFrames": olTRTrafPortInFrames,
       "olTRTrafPortOutFrames": olTRTrafPortOutFrames,
       "olTRTrafPortInOctets": olTRTrafPortInOctets,
       "olTRTrafPortOutOctets": olTRTrafPortOutOctets,
       "olTRTrafPortOutErrors": olTRTrafPortOutErrors,
       "olTRTrafPortOutBroadcastFrames": olTRTrafPortOutBroadcastFrames,
       "olTRTrafPortOutMulticastFrames": olTRTrafPortOutMulticastFrames,
       "olTRTrafTopNTable": olTRTrafTopNTable,
       "olTRTrafTopNEntry": olTRTrafTopNEntry,
       "olTRTrafTopNNetID": olTRTrafTopNNetID,
       "olTRTrafTopNStatistic": olTRTrafTopNStatistic,
       "olTRTrafTopNIndex": olTRTrafTopNIndex,
       "olTRTrafTopNAddress": olTRTrafTopNAddress,
       "olTRTrafTopNSlotIndex": olTRTrafTopNSlotIndex,
       "olTRTrafTopNPortIndex": olTRTrafTopNPortIndex,
       "olTRTrafTopNInFrames": olTRTrafTopNInFrames,
       "olTRTrafTopNOutFrames": olTRTrafTopNOutFrames,
       "olTRTrafTopNInOctets": olTRTrafTopNInOctets,
       "olTRTrafTopNOutOctets": olTRTrafTopNOutOctets,
       "olTRTrafTopNOutErrors": olTRTrafTopNOutErrors,
       "olTRTrafTopNOutBroadcastFrames": olTRTrafTopNOutBroadcastFrames,
       "olTRTrafTopNOutMulticastFrames": olTRTrafTopNOutMulticastFrames,
       "olTRTrafTopNSummaryTable": olTRTrafTopNSummaryTable,
       "olTRTrafTopNSummaryEntry": olTRTrafTopNSummaryEntry,
       "olTRTrafTopNSummaryNetID": olTRTrafTopNSummaryNetID,
       "olTRTrafTopNSummaryStatistic": olTRTrafTopNSummaryStatistic,
       "olTRTrafTopNSummaryIndex": olTRTrafTopNSummaryIndex,
       "olTRTrafTopNSummaryStations": olTRTrafTopNSummaryStations,
       "olFDDInet": olFDDInet,
       "olFDDIStatsModTable": olFDDIStatsModTable,
       "olFDDIStatsModEntry": olFDDIStatsModEntry,
       "olFDDIStatsModSlotIndex": olFDDIStatsModSlotIndex,
       "olFDDIStatsModMgtRcvErrs": olFDDIStatsModMgtRcvErrs,
       "olFDDIStatsModMgtXmitErrs": olFDDIStatsModMgtXmitErrs,
       "olFDDIStatsModBackplaneErrs": olFDDIStatsModBackplaneErrs,
       "olFDDIStatsModPllUnlockErrs": olFDDIStatsModPllUnlockErrs,
       "olFDDIStatsPortTable": olFDDIStatsPortTable,
       "olFDDIStatsPortEntry": olFDDIStatsPortEntry,
       "olFDDIStatsPortSlotIndex": olFDDIStatsPortSlotIndex,
       "olFDDIStatsPortIndex": olFDDIStatsPortIndex,
       "olFDDIStatsPortLCTFailCts": olFDDIStatsPortLCTFailCts,
       "olFDDIStatsPortLerEstimate": olFDDIStatsPortLerEstimate,
       "olFDDIStatsPortLemRejectCts": olFDDIStatsPortLemRejectCts,
       "olFDDIStatsPortLemCts": olFDDIStatsPortLemCts,
       "olFDDInetStatsTable": olFDDInetStatsTable,
       "olFDDInetStatsEntry": olFDDInetStatsEntry,
       "olFDDInetStatsNetID": olFDDInetStatsNetID,
       "olFDDInetStatsRingOpCounts": olFDDInetStatsRingOpCounts,
       "olFDDInetStatsFrameCounts": olFDDInetStatsFrameCounts,
       "olFDDInetStatsErrorCounts": olFDDInetStatsErrorCounts,
       "olFDDInetStatsLostCounts": olFDDInetStatsLostCounts,
       "olFDDInetStatsFrameErrorRatio": olFDDInetStatsFrameErrorRatio,
       "olGroups": olGroups,
       "olGroupPortTable": olGroupPortTable,
       "olGroupPortEntry": olGroupPortEntry,
       "olGroupPortSlotIndex": olGroupPortSlotIndex,
       "olGroupPortIndex": olGroupPortIndex,
       "olGroupPortGroupID": olGroupPortGroupID,
       "olGroupSummaryTable": olGroupSummaryTable,
       "olGroupSummaryEntry": olGroupSummaryEntry,
       "olGroupSummaryGroupID": olGroupSummaryGroupID,
       "olGroupSummaryIndex": olGroupSummaryIndex,
       "olGroupSummaryPorts": olGroupSummaryPorts,
       "olGroupSet": olGroupSet,
       "olGroupSetAction": olGroupSetAction,
       "olGroupSetGroupID": olGroupSetGroupID,
       "olGroupSetSlotIndex": olGroupSetSlotIndex,
       "olGroupSetPortIndex": olGroupSetPortIndex,
       "olGroupSetAdminState": olGroupSetAdminState,
       "olAlarm": olAlarm,
       "olThresh": olThresh,
       "olThreshControl": olThreshControl,
       "olThreshTotalEntries": olThreshTotalEntries,
       "olThreshMaxEntries": olThreshMaxEntries,
       "olThreshLastCreatedIndex": olThreshLastCreatedIndex,
       "olThreshAllMode": olThreshAllMode,
       "olThreshTable": olThreshTable,
       "olThreshEntry": olThreshEntry,
       "olThreshIndex": olThreshIndex,
       "olThreshMode": olThreshMode,
       "olThreshDescription": olThreshDescription,
       "olThreshObjectIdentifier": olThreshObjectIdentifier,
       "olThreshStatCategory": olThreshStatCategory,
       "olThreshStatType": olThreshStatType,
       "olThreshStatNetID": olThreshStatNetID,
       "olThreshStatSlotIndex": olThreshStatSlotIndex,
       "olThreshStatPortIndex": olThreshStatPortIndex,
       "olThreshStatStationAddr": olThreshStatStationAddr,
       "olThreshInterval": olThreshInterval,
       "olThreshCondition": olThreshCondition,
       "olThreshValue": olThreshValue,
       "olThreshCurrentValue": olThreshCurrentValue,
       "olThreshStatus": olThreshStatus,
       "olThreshTimeSinceLastTriggered": olThreshTimeSinceLastTriggered,
       "olThreshActionType": olThreshActionType,
       "olThreshActionData": olThreshActionData,
       "olThreshActionPriority": olThreshActionPriority,
       "ocPower": ocPower,
       "ocPowerControl": ocPowerControl,
       "ocPowerModeAdminStatus": ocPowerModeAdminStatus,
       "ocPowerModeOperStatus": ocPowerModeOperStatus,
       "ocPowerOverheatPowerDownMode": ocPowerOverheatPowerDownMode,
       "ocPowerOutputTable": ocPowerOutputTable,
       "ocPowerOutputEntry": ocPowerOutputEntry,
       "ocPowerOutputType": ocPowerOutputType,
       "ocPowerOutputVoltageLevel": ocPowerOutputVoltageLevel,
       "ocPowerOutputWattageCapacity": ocPowerOutputWattageCapacity,
       "ocPowerOutputWattageConsumed": ocPowerOutputWattageConsumed,
       "ocPowerOutputWattageAvailable": ocPowerOutputWattageAvailable,
       "ocPowerOutputUnmanagedWattageAlloc": ocPowerOutputUnmanagedWattageAlloc,
       "ocPowerSlotTable": ocPowerSlotTable,
       "ocPowerSlotEntry": ocPowerSlotEntry,
       "ocPowerSlotIndex": ocPowerSlotIndex,
       "ocPowerSlotClass": ocPowerSlotClass,
       "ocPowerSlotAdminStatus": ocPowerSlotAdminStatus,
       "ocPowerSlotOperStatus": ocPowerSlotOperStatus,
       "ocInventory": ocInventory,
       "ocInvHub": ocInvHub,
       "ocInvHubType": ocInvHubType,
       "ocInvHubSerialNo": ocInvHubSerialNo,
       "ocInvHubHWVer": ocInvHubHWVer,
       "ocInvHubMfr": ocInvHubMfr,
       "ocInvHubMfrDate": ocInvHubMfrDate,
       "ocInvMods": ocInvMods,
       "ocInvModTable": ocInvModTable,
       "ocInvModEntry": ocInvModEntry,
       "ocInvModSlotIndex": ocInvModSlotIndex,
       "ocInvModSubSlotIndex": ocInvModSubSlotIndex,
       "ocInvModModel": ocInvModModel,
       "ocInvModSerialNo": ocInvModSerialNo,
       "ocInvModHWVer": ocInvModHWVer,
       "ocInvModSWVer": ocInvModSWVer,
       "ocInvModSWBootVer": ocInvModSWBootVer,
       "ocInvModMfr": ocInvModMfr,
       "ocInvModMfrDate": ocInvModMfrDate,
       "olPS2": olPS2,
       "olPS2Info": olPS2Info,
       "olPS2OperatingSystem": olPS2OperatingSystem,
       "olPS2FixedDiskSize": olPS2FixedDiskSize,
       "olPS2RamSize": olPS2RamSize,
       "olPS2McaTable": olPS2McaTable,
       "olPS2McaEntry": olPS2McaEntry,
       "olPS2McaIndex": olPS2McaIndex,
       "olPS2McaDescription": olPS2McaDescription,
       "olPS2McaSlotConnectPoint": olPS2McaSlotConnectPoint,
       "olPS2McaPortConnectPoint": olPS2McaPortConnectPoint,
       "olPS2McaMacAddress": olPS2McaMacAddress,
       "olPS2ApplTable": olPS2ApplTable,
       "olPS2ApplEntry": olPS2ApplEntry,
       "olPS2ApplIndex": olPS2ApplIndex,
       "olPS2ApplDescription": olPS2ApplDescription,
       "oebm": oebm,
       "midnight": midnight,
       "workGroupHub": workGroupHub,
       "hubSysGroup": hubSysGroup,
       "hardwareGroup": hardwareGroup,
       "softwareGroup": softwareGroup,
       "hubGroup": hubGroup,
       "boardGroup": boardGroup,
       "portGroup": portGroup,
       "alarmGroup": alarmGroup,
       "emm": emm,
       "chipBridge": chipBridge,
       "trmm": trmm,
       "fmm": fmm,
       "focus1": focus1,
       "oeim": oeim,
       "oncore": oncore,
       "dmm": dmm,
       "onsembleEthernet": onsembleEthernet,
       "chipExperiment": chipExperiment,
       "chipExpTokenRing": chipExpTokenRing,
       "expDot5": expDot5,
       "expDot5Table": expDot5Table,
       "expDot5Entry": expDot5Entry,
       "expDot5IfIndex": expDot5IfIndex,
       "expDot5Commands": expDot5Commands,
       "expDot5RingStatus": expDot5RingStatus,
       "expDot5RingState": expDot5RingState,
       "expDot5RingOpenStatus": expDot5RingOpenStatus,
       "expDot5RingSpeed": expDot5RingSpeed,
       "expDot5UpStream": expDot5UpStream,
       "expDot5ActMonParticipate": expDot5ActMonParticipate,
       "expDot5Functional": expDot5Functional,
       "expDot5StatsTable": expDot5StatsTable,
       "expDot5StatsEntry": expDot5StatsEntry,
       "expDot5StatsIfIndex": expDot5StatsIfIndex,
       "expDot5StatsLineErrors": expDot5StatsLineErrors,
       "expDot5StatsBurstErrors": expDot5StatsBurstErrors,
       "expDot5StatsACErrors": expDot5StatsACErrors,
       "expDot5StatsAbortTransErrors": expDot5StatsAbortTransErrors,
       "expDot5StatsInternalErrors": expDot5StatsInternalErrors,
       "expDot5StatsLostFrameErrors": expDot5StatsLostFrameErrors,
       "expDot5StatsReceiveCongestions": expDot5StatsReceiveCongestions,
       "expDot5StatsFrameCopiedErrors": expDot5StatsFrameCopiedErrors,
       "expDot5StatsTokenErrors": expDot5StatsTokenErrors,
       "expDot5StatsSoftErrors": expDot5StatsSoftErrors,
       "expDot5StatsHardErrors": expDot5StatsHardErrors,
       "expDot5StatsSignalLoss": expDot5StatsSignalLoss,
       "expDot5StatsTransmitBeacons": expDot5StatsTransmitBeacons,
       "expDot5StatsRecoverys": expDot5StatsRecoverys,
       "expDot5StatsLobeWires": expDot5StatsLobeWires,
       "expDot5StatsRemoves": expDot5StatsRemoves,
       "expDot5StatsSingles": expDot5StatsSingles,
       "expDot5StatsFreqErrors": expDot5StatsFreqErrors,
       "expDot5Tests": expDot5Tests,
       "testInsertFunc": testInsertFunc,
       "expDot5ChipSets": expDot5ChipSets,
       "chipSetIBM16": chipSetIBM16,
       "chipSetTItms380": chipSetTItms380,
       "chipSetTItms380c16": chipSetTItms380c16,
       "expDot5TimerTable": expDot5TimerTable,
       "expDot5TimerEntry": expDot5TimerEntry,
       "expDot5TimerIfIndex": expDot5TimerIfIndex,
       "expDot5TimerReturnRepeat": expDot5TimerReturnRepeat,
       "expDot5TimerHolding": expDot5TimerHolding,
       "expDot5TimerQueuePDU": expDot5TimerQueuePDU,
       "expDot5TimerValidTransmit": expDot5TimerValidTransmit,
       "expDot5TimerNoToken": expDot5TimerNoToken,
       "expDot5TimerActiveMon": expDot5TimerActiveMon,
       "expDot5TimerStandbyMon": expDot5TimerStandbyMon,
       "expDot5TimerErrorReport": expDot5TimerErrorReport,
       "expDot5TimerBeaconTransmit": expDot5TimerBeaconTransmit,
       "expDot5TimerBeaconReceive": expDot5TimerBeaconReceive,
       "dot1dBridge": dot1dBridge,
       "chipTTY": chipTTY,
       "chipTTYNumber": chipTTYNumber,
       "chipTTYTable": chipTTYTable,
       "chipTTYEntry": chipTTYEntry,
       "chipTTYIndex": chipTTYIndex,
       "chipTTYBaud": chipTTYBaud,
       "chipTTYParity": chipTTYParity,
       "chipTTYStop": chipTTYStop,
       "chipTTYData": chipTTYData,
       "chipTTYTimeout": chipTTYTimeout,
       "chipTTYPrompt": chipTTYPrompt,
       "chipTTYDTR": chipTTYDTR,
       "chipTTYTerminalType": chipTTYTerminalType,
       "chipTFTP": chipTFTP,
       "chipTFTPStart": chipTFTPStart,
       "chipTFTPSlot": chipTFTPSlot,
       "chipTFTPIpAddress": chipTFTPIpAddress,
       "chipTFTPFileName": chipTFTPFileName,
       "chipTFTPFileType": chipTFTPFileType,
       "chipTFTPResult": chipTFTPResult,
       "chipTFTPSubSlot": chipTFTPSubSlot,
       "chipTFTPTargetLocation": chipTFTPTargetLocation,
       "chipDownload": chipDownload,
       "chipDownloadUDKSerial": chipDownloadUDKSerial,
       "chipDownloadKey": chipDownloadKey,
       "chipDownloadDateTime": chipDownloadDateTime,
       "chipAlert": chipAlert,
       "chipAlertTable": chipAlertTable,
       "chipAlertEntry": chipAlertEntry,
       "chipAlertIndex": chipAlertIndex,
       "chipAlertMode": chipAlertMode,
       "chipBootP": chipBootP,
       "chipBootPStart": chipBootPStart,
       "chipBootPPowerUpMode": chipBootPPowerUpMode,
       "chipBootPIpAddress": chipBootPIpAddress,
       "chipBootPResult": chipBootPResult}
)
