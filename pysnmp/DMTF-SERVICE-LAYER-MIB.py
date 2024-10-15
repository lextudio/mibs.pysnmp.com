# SNMP MIB module (DMTF-SERVICE-LAYER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DMTF-SERVICE-LAYER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:43 2024
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

(DmiDate,
 DmiString,
 dmiCompId,
 dmiEventAssociatedGroup,
 dmiEventDateTime,
 dmiEventSeverity,
 dmiEventStateKey,
 dmiEventSubSystem,
 dmiEventSystem) = mibBuilder.importSymbols(
    "DMTF-DMI-MIB",
    "DmiDate",
    "DmiString",
    "dmiCompId",
    "dmiEventAssociatedGroup",
    "dmiEventDateTime",
    "dmiEventSeverity",
    "dmiEventStateKey",
    "dmiEventSubSystem",
    "dmiEventSystem")

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

dmtfServiceLayerMIF = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2, 1)
)


# Types definitions



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiCounter64(Counter64):
    """Custom type DmiCounter64 based on Counter64"""




class DmiGauge(Gauge32):
    """Custom type DmiGauge based on Gauge32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiCompId(Integer32):
    """Custom type DmiCompId based on Integer32"""




class DmiGroupId(Integer32):
    """Custom type DmiGroupId based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dmtf_ObjectIdentity = ObjectIdentity
dmtf = _Dmtf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412)
)
_DmtfStdMifs_ObjectIdentity = ObjectIdentity
dmtfStdMifs = _DmtfStdMifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2)
)
_DmtfComponentIDTable_Object = MibTable
dmtfComponentIDTable = _DmtfComponentIDTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dmtfComponentIDTable.setStatus("current")
_DmtfComponentIDEntry_Object = MibTableRow
dmtfComponentIDEntry = _DmtfComponentIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1)
)
dmtfComponentIDEntry.setIndexNames(
    (0, "DMTF-SERVICE-LAYER-MIB", "DmiCompId"),
    (0, "DMTF-SERVICE-LAYER-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dmtfComponentIDEntry.setStatus("current")
_Manufacturer_Type = DmiString
_Manufacturer_Object = MibTableColumn
manufacturer = _Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 1),
    _Manufacturer_Type()
)
manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturer.setStatus("current")
_Product_Type = DmiString
_Product_Object = MibTableColumn
product = _Product_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 2),
    _Product_Type()
)
product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product.setStatus("current")
_Version_Type = DmiString
_Version_Object = MibTableColumn
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 3),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_SerialNumber_Type = DmiString
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 4),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_Installation_Type = DmiDate
_Installation_Object = MibTableColumn
installation = _Installation_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 5),
    _Installation_Type()
)
installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installation.setStatus("current")


class _Verify_Type(Integer32):
    """Custom type verify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("anErrorOccurredCheckStatusCode", 0),
          ("reserved", 3),
          ("thisComponentDoesNotExist", 1),
          ("thisComponentExistsAndIsFunctioningCorrectly", 7),
          ("thisComponentExistsAndIsNotFunctioningCorrectly", 6),
          ("thisComponentExistsButTheFunctionalityIsUnknown", 5),
          ("thisComponentExistsButTheFunctionalityIsUntested", 4),
          ("verificationIsNotSupported", 2))
    )


_Verify_Type.__name__ = "Integer32"
_Verify_Object = MibTableColumn
verify = _Verify_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 6),
    _Verify_Type()
)
verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verify.setStatus("current")
_DmtfSPIndicationSubscriptionTable_Object = MibTable
dmtfSPIndicationSubscriptionTable = _DmtfSPIndicationSubscriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 3)
)
if mibBuilder.loadTexts:
    dmtfSPIndicationSubscriptionTable.setStatus("current")
_DmtfSPIndicationSubscriptionEntry_Object = MibTableRow
dmtfSPIndicationSubscriptionEntry = _DmtfSPIndicationSubscriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1)
)
dmtfSPIndicationSubscriptionEntry.setIndexNames(
    (0, "DMTF-SERVICE-LAYER-MIB", "DmiCompId"),
    (0, "DMTF-SERVICE-LAYER-MIB", "DmiGroupId"),
    (0, "DMTF-SERVICE-LAYER-MIB", "subscriberRPCType"),
    (0, "DMTF-SERVICE-LAYER-MIB", "subscriberTransportType"),
    (0, "DMTF-SERVICE-LAYER-MIB", "subscriberAddressing"),
    (0, "DMTF-SERVICE-LAYER-MIB", "subscriberID"),
)
if mibBuilder.loadTexts:
    dmtfSPIndicationSubscriptionEntry.setStatus("current")


class _DmtfSPIndicationSubscriptionState_Type(Integer32):
    """Custom type dmtfSPIndicationSubscriptionState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfSPIndicationSubscriptionState_Type.__name__ = "Integer32"
_DmtfSPIndicationSubscriptionState_Object = MibTableColumn
dmtfSPIndicationSubscriptionState = _DmtfSPIndicationSubscriptionState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 0),
    _DmtfSPIndicationSubscriptionState_Type()
)
dmtfSPIndicationSubscriptionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfSPIndicationSubscriptionState.setStatus("current")
_SubscriberRPCType_Type = DmiString
_SubscriberRPCType_Object = MibTableColumn
subscriberRPCType = _SubscriberRPCType_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 1),
    _SubscriberRPCType_Type()
)
subscriberRPCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberRPCType.setStatus("current")
_SubscriberTransportType_Type = DmiString
_SubscriberTransportType_Object = MibTableColumn
subscriberTransportType = _SubscriberTransportType_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 2),
    _SubscriberTransportType_Type()
)
subscriberTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberTransportType.setStatus("current")
_SubscriberAddressing_Type = DmiString
_SubscriberAddressing_Object = MibTableColumn
subscriberAddressing = _SubscriberAddressing_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 3),
    _SubscriberAddressing_Type()
)
subscriberAddressing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberAddressing.setStatus("current")
_SubscriberID_Type = DmiInteger
_SubscriberID_Object = MibTableColumn
subscriberID = _SubscriberID_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 4),
    _SubscriberID_Type()
)
subscriberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberID.setStatus("current")
_SubscriptionExpirationWarningDateStamp_Type = DmiDate
_SubscriptionExpirationWarningDateStamp_Object = MibTableColumn
subscriptionExpirationWarningDateStamp = _SubscriptionExpirationWarningDateStamp_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 5),
    _SubscriptionExpirationWarningDateStamp_Type()
)
subscriptionExpirationWarningDateStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriptionExpirationWarningDateStamp.setStatus("current")
_SubscriptionExpirationDateStamp_Type = DmiDate
_SubscriptionExpirationDateStamp_Object = MibTableColumn
subscriptionExpirationDateStamp = _SubscriptionExpirationDateStamp_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 6),
    _SubscriptionExpirationDateStamp_Type()
)
subscriptionExpirationDateStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriptionExpirationDateStamp.setStatus("current")
_IndicationFailureThreshold_Type = DmiInteger
_IndicationFailureThreshold_Object = MibTableColumn
indicationFailureThreshold = _IndicationFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 3, 1, 7),
    _IndicationFailureThreshold_Type()
)
indicationFailureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indicationFailureThreshold.setStatus("current")
_DmtfSPFilterInformationTable_Object = MibTable
dmtfSPFilterInformationTable = _DmtfSPFilterInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 4)
)
if mibBuilder.loadTexts:
    dmtfSPFilterInformationTable.setStatus("current")
_DmtfSPFilterInformationEntry_Object = MibTableRow
dmtfSPFilterInformationEntry = _DmtfSPFilterInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1)
)
dmtfSPFilterInformationEntry.setIndexNames(
    (0, "DMTF-SERVICE-LAYER-MIB", "DmiCompId"),
    (0, "DMTF-SERVICE-LAYER-MIB", "DmiGroupId"),
    (0, "DMTF-SERVICE-LAYER-MIB", "subscriberRPCType"),
    (0, "DMTF-SERVICE-LAYER-MIB", "subscriberTransportType"),
    (0, "DMTF-SERVICE-LAYER-MIB", "subscriberAddressing"),
    (0, "DMTF-SERVICE-LAYER-MIB", "subscriberID"),
    (0, "DMTF-SERVICE-LAYER-MIB", "componentID"),
    (0, "DMTF-SERVICE-LAYER-MIB", "groupClassString"),
)
if mibBuilder.loadTexts:
    dmtfSPFilterInformationEntry.setStatus("current")


class _DmtfSPFilterInformationState_Type(Integer32):
    """Custom type dmtfSPFilterInformationState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfSPFilterInformationState_Type.__name__ = "Integer32"
_DmtfSPFilterInformationState_Object = MibTableColumn
dmtfSPFilterInformationState = _DmtfSPFilterInformationState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 0),
    _DmtfSPFilterInformationState_Type()
)
dmtfSPFilterInformationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfSPFilterInformationState.setStatus("current")
_SubscriberRPCType2_Type = DmiString
_SubscriberRPCType2_Object = MibScalar
subscriberRPCType2 = _SubscriberRPCType2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 1),
    _SubscriberRPCType2_Type()
)
subscriberRPCType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberRPCType2.setStatus("current")
_SubscriberTransportType2_Type = DmiString
_SubscriberTransportType2_Object = MibScalar
subscriberTransportType2 = _SubscriberTransportType2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 2),
    _SubscriberTransportType2_Type()
)
subscriberTransportType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberTransportType2.setStatus("current")
_SubscriberAddressing2_Type = DmiString
_SubscriberAddressing2_Object = MibScalar
subscriberAddressing2 = _SubscriberAddressing2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 3),
    _SubscriberAddressing2_Type()
)
subscriberAddressing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberAddressing2.setStatus("current")
_SubscriberID2_Type = DmiInteger
_SubscriberID2_Object = MibScalar
subscriberID2 = _SubscriberID2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 4),
    _SubscriberID2_Type()
)
subscriberID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberID2.setStatus("current")
_ComponentID_Type = DmiInteger
_ComponentID_Object = MibScalar
componentID = _ComponentID_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 5),
    _ComponentID_Type()
)
componentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentID.setStatus("current")
_GroupClassString_Type = DmiString
_GroupClassString_Object = MibTableColumn
groupClassString = _GroupClassString_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 6),
    _GroupClassString_Type()
)
groupClassString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupClassString.setStatus("current")


class _EventSeverity_Type(Integer32):
    """Custom type eventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("critical", 16),
          ("information", 2),
          ("monitor", 1),
          ("nonCritical-1", 8),
          ("nonRecoverable", 32),
          ("oK", 4))
    )


_EventSeverity_Type.__name__ = "Integer32"
_EventSeverity_Object = MibTableColumn
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 4, 1, 7),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_DmtfDynOids_ObjectIdentity = ObjectIdentity
dmtfDynOids = _DmtfDynOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMTF-SERVICE-LAYER-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiCounter64": DmiCounter64,
       "DmiGauge": DmiGauge,
       "DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiCompId": DmiCompId,
       "DmiGroupId": DmiGroupId,
       "dmtf": dmtf,
       "dmtfStdMifs": dmtfStdMifs,
       "dmtfServiceLayerMIF": dmtfServiceLayerMIF,
       "dmtfComponentIDTable": dmtfComponentIDTable,
       "dmtfComponentIDEntry": dmtfComponentIDEntry,
       "manufacturer": manufacturer,
       "product": product,
       "version": version,
       "serialNumber": serialNumber,
       "installation": installation,
       "verify": verify,
       "dmtfSPIndicationSubscriptionTable": dmtfSPIndicationSubscriptionTable,
       "dmtfSPIndicationSubscriptionEntry": dmtfSPIndicationSubscriptionEntry,
       "dmtfSPIndicationSubscriptionState": dmtfSPIndicationSubscriptionState,
       "subscriberRPCType": subscriberRPCType,
       "subscriberTransportType": subscriberTransportType,
       "subscriberAddressing": subscriberAddressing,
       "subscriberID": subscriberID,
       "subscriptionExpirationWarningDateStamp": subscriptionExpirationWarningDateStamp,
       "subscriptionExpirationDateStamp": subscriptionExpirationDateStamp,
       "indicationFailureThreshold": indicationFailureThreshold,
       "dmtfSPFilterInformationTable": dmtfSPFilterInformationTable,
       "dmtfSPFilterInformationEntry": dmtfSPFilterInformationEntry,
       "dmtfSPFilterInformationState": dmtfSPFilterInformationState,
       "subscriberRPCType2": subscriberRPCType2,
       "subscriberTransportType2": subscriberTransportType2,
       "subscriberAddressing2": subscriberAddressing2,
       "subscriberID2": subscriberID2,
       "componentID": componentID,
       "groupClassString": groupClassString,
       "eventSeverity": eventSeverity,
       "dmtfDynOids": dmtfDynOids}
)
