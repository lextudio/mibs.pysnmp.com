# SNMP MIB module (XYPLEX-LAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYPLEX-LAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:52 2024
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

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "RFC1212-CONCISE-MIB",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xyplex_ObjectIdentity = ObjectIdentity
xyplex = _Xyplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33)
)
_Lat_ObjectIdentity = ObjectIdentity
lat = _Lat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 3)
)


class _LatAnnounceServices_Type(Integer32):
    """Custom type latAnnounceServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatAnnounceServices_Type.__name__ = "Integer32"
_LatAnnounceServices_Object = MibScalar
latAnnounceServices = _LatAnnounceServices_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 1),
    _LatAnnounceServices_Type()
)
latAnnounceServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latAnnounceServices.setStatus("mandatory")


class _LatCircuitTimer_Type(Integer32):
    """Custom type latCircuitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 200),
    )


_LatCircuitTimer_Type.__name__ = "Integer32"
_LatCircuitTimer_Object = MibScalar
latCircuitTimer = _LatCircuitTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 2),
    _LatCircuitTimer_Type()
)
latCircuitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latCircuitTimer.setStatus("mandatory")


class _LatIdentificationLengthLimit_Type(Integer32):
    """Custom type latIdentificationLengthLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_LatIdentificationLengthLimit_Type.__name__ = "Integer32"
_LatIdentificationLengthLimit_Object = MibScalar
latIdentificationLengthLimit = _LatIdentificationLengthLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 3),
    _LatIdentificationLengthLimit_Type()
)
latIdentificationLengthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latIdentificationLengthLimit.setStatus("mandatory")


class _LatKeepaliveTimer_Type(Integer32):
    """Custom type latKeepaliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_LatKeepaliveTimer_Type.__name__ = "Integer32"
_LatKeepaliveTimer_Object = MibScalar
latKeepaliveTimer = _LatKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 4),
    _LatKeepaliveTimer_Type()
)
latKeepaliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latKeepaliveTimer.setStatus("mandatory")


class _LatMulticastTimer_Type(Integer32):
    """Custom type latMulticastTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_LatMulticastTimer_Type.__name__ = "Integer32"
_LatMulticastTimer_Object = MibScalar
latMulticastTimer = _LatMulticastTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 5),
    _LatMulticastTimer_Type()
)
latMulticastTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latMulticastTimer.setStatus("mandatory")


class _LatNodeLimit_Type(Integer32):
    """Custom type latNodeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_LatNodeLimit_Type.__name__ = "Integer32"
_LatNodeLimit_Object = MibScalar
latNodeLimit = _LatNodeLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 6),
    _LatNodeLimit_Type()
)
latNodeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latNodeLimit.setStatus("mandatory")


class _LatNumber_Type(Integer32):
    """Custom type latNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LatNumber_Type.__name__ = "Integer32"
_LatNumber_Object = MibScalar
latNumber = _LatNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 7),
    _LatNumber_Type()
)
latNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latNumber.setStatus("mandatory")


class _LatRetransmitLimit_Type(Integer32):
    """Custom type latRetransmitLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 120),
    )


_LatRetransmitLimit_Type.__name__ = "Integer32"
_LatRetransmitLimit_Object = MibScalar
latRetransmitLimit = _LatRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 8),
    _LatRetransmitLimit_Type()
)
latRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latRetransmitLimit.setStatus("mandatory")


class _LatLocalServiceGroups_Type(OctetString):
    """Custom type latLocalServiceGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LatLocalServiceGroups_Type.__name__ = "OctetString"
_LatLocalServiceGroups_Object = MibScalar
latLocalServiceGroups = _LatLocalServiceGroups_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 9),
    _LatLocalServiceGroups_Type()
)
latLocalServiceGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latLocalServiceGroups.setStatus("mandatory")


class _LatGroupPurge_Type(Integer32):
    """Custom type latGroupPurge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatGroupPurge_Type.__name__ = "Integer32"
_LatGroupPurge_Object = MibScalar
latGroupPurge = _LatGroupPurge_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 10),
    _LatGroupPurge_Type()
)
latGroupPurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latGroupPurge.setStatus("mandatory")


class _LatNodePurge_Type(Integer32):
    """Custom type latNodePurge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatNodePurge_Type.__name__ = "Integer32"
_LatNodePurge_Object = MibScalar
latNodePurge = _LatNodePurge_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 11),
    _LatNodePurge_Type()
)
latNodePurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latNodePurge.setStatus("mandatory")
_LatNodesRejected_Type = Counter32
_LatNodesRejected_Object = MibScalar
latNodesRejected = _LatNodesRejected_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 12),
    _LatNodesRejected_Type()
)
latNodesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodesRejected.setStatus("mandatory")
_LatInMessages_Type = Counter32
_LatInMessages_Object = MibScalar
latInMessages = _LatInMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 13),
    _LatInMessages_Type()
)
latInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInMessages.setStatus("mandatory")
_LatOutMessages_Type = Counter32
_LatOutMessages_Object = MibScalar
latOutMessages = _LatOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 14),
    _LatOutMessages_Type()
)
latOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latOutMessages.setStatus("mandatory")
_LatInSessionsAccepted_Type = Counter32
_LatInSessionsAccepted_Object = MibScalar
latInSessionsAccepted = _LatInSessionsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 15),
    _LatInSessionsAccepted_Type()
)
latInSessionsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInSessionsAccepted.setStatus("mandatory")
_LatInSessionsRejected_Type = Counter32
_LatInSessionsRejected_Object = MibScalar
latInSessionsRejected = _LatInSessionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 16),
    _LatInSessionsRejected_Type()
)
latInSessionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInSessionsRejected.setStatus("mandatory")
_LatAddressChange_Type = Counter32
_LatAddressChange_Object = MibScalar
latAddressChange = _LatAddressChange_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 17),
    _LatAddressChange_Type()
)
latAddressChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latAddressChange.setStatus("mandatory")
_LatInDuplicates_Type = Counter32
_LatInDuplicates_Object = MibScalar
latInDuplicates = _LatInDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 18),
    _LatInDuplicates_Type()
)
latInDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInDuplicates.setStatus("mandatory")
_LatOutRetransmits_Type = Counter32
_LatOutRetransmits_Object = MibScalar
latOutRetransmits = _LatOutRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 19),
    _LatOutRetransmits_Type()
)
latOutRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latOutRetransmits.setStatus("mandatory")
_LatInBadMessages_Type = Counter32
_LatInBadMessages_Object = MibScalar
latInBadMessages = _LatInBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 20),
    _LatInBadMessages_Type()
)
latInBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInBadMessages.setStatus("mandatory")
_LatInBadSlots_Type = Counter32
_LatInBadSlots_Object = MibScalar
latInBadSlots = _LatInBadSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 21),
    _LatInBadSlots_Type()
)
latInBadSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInBadSlots.setStatus("mandatory")
_LatInBadMulticasts_Type = Counter32
_LatInBadMulticasts_Object = MibScalar
latInBadMulticasts = _LatInBadMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 22),
    _LatInBadMulticasts_Type()
)
latInBadMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInBadMulticasts.setStatus("mandatory")
_LatPortTable_Object = MibTable
latPortTable = _LatPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23)
)
if mibBuilder.loadTexts:
    latPortTable.setStatus("mandatory")
_LatPortEntry_Object = MibTableRow
latPortEntry = _LatPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1)
)
latPortEntry.setIndexNames(
    (0, "XYPLEX-LAT-MIB", "latPortIndex"),
)
if mibBuilder.loadTexts:
    latPortEntry.setStatus("mandatory")
_LatPortIndex_Type = Integer32
_LatPortIndex_Object = MibTableColumn
latPortIndex = _LatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 1),
    _LatPortIndex_Type()
)
latPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latPortIndex.setStatus("mandatory")


class _LatPortAuthorizedGroups_Type(OctetString):
    """Custom type latPortAuthorizedGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LatPortAuthorizedGroups_Type.__name__ = "OctetString"
_LatPortAuthorizedGroups_Object = MibTableColumn
latPortAuthorizedGroups = _LatPortAuthorizedGroups_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 2),
    _LatPortAuthorizedGroups_Type()
)
latPortAuthorizedGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latPortAuthorizedGroups.setStatus("mandatory")


class _LatPortAutoPrompt_Type(Integer32):
    """Custom type latPortAutoPrompt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatPortAutoPrompt_Type.__name__ = "Integer32"
_LatPortAutoPrompt_Object = MibTableColumn
latPortAutoPrompt = _LatPortAutoPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 3),
    _LatPortAutoPrompt_Type()
)
latPortAutoPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latPortAutoPrompt.setStatus("mandatory")


class _LatPortCurrentGroups_Type(OctetString):
    """Custom type latPortCurrentGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LatPortCurrentGroups_Type.__name__ = "OctetString"
_LatPortCurrentGroups_Object = MibTableColumn
latPortCurrentGroups = _LatPortCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 4),
    _LatPortCurrentGroups_Type()
)
latPortCurrentGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latPortCurrentGroups.setStatus("mandatory")


class _LatPortRemoteModification_Type(Integer32):
    """Custom type latPortRemoteModification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatPortRemoteModification_Type.__name__ = "Integer32"
_LatPortRemoteModification_Object = MibTableColumn
latPortRemoteModification = _LatPortRemoteModification_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 5),
    _LatPortRemoteModification_Type()
)
latPortRemoteModification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latPortRemoteModification.setStatus("mandatory")
_LatOfferedServiceTable_Object = MibTable
latOfferedServiceTable = _LatOfferedServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24)
)
if mibBuilder.loadTexts:
    latOfferedServiceTable.setStatus("mandatory")
_LatOfferedServiceEntry_Object = MibTableRow
latOfferedServiceEntry = _LatOfferedServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1)
)
latOfferedServiceEntry.setIndexNames(
    (0, "XYPLEX-LAT-MIB", "latOfferedServiceName"),
)
if mibBuilder.loadTexts:
    latOfferedServiceEntry.setStatus("mandatory")


class _LatOfferedServiceName_Type(DisplayString):
    """Custom type latOfferedServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LatOfferedServiceName_Type.__name__ = "DisplayString"
_LatOfferedServiceName_Object = MibTableColumn
latOfferedServiceName = _LatOfferedServiceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 1),
    _LatOfferedServiceName_Type()
)
latOfferedServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServiceName.setStatus("mandatory")


class _LatOfferedServiceStatus_Type(Integer32):
    """Custom type latOfferedServiceStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_LatOfferedServiceStatus_Type.__name__ = "Integer32"
_LatOfferedServiceStatus_Object = MibTableColumn
latOfferedServiceStatus = _LatOfferedServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 2),
    _LatOfferedServiceStatus_Type()
)
latOfferedServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServiceStatus.setStatus("mandatory")


class _LatOfferedServiceAllowConnections_Type(Integer32):
    """Custom type latOfferedServiceAllowConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatOfferedServiceAllowConnections_Type.__name__ = "Integer32"
_LatOfferedServiceAllowConnections_Object = MibTableColumn
latOfferedServiceAllowConnections = _LatOfferedServiceAllowConnections_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 3),
    _LatOfferedServiceAllowConnections_Type()
)
latOfferedServiceAllowConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServiceAllowConnections.setStatus("mandatory")


class _LatOfferedServiceIdentification_Type(DisplayString):
    """Custom type latOfferedServiceIdentification based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LatOfferedServiceIdentification_Type.__name__ = "DisplayString"
_LatOfferedServiceIdentification_Object = MibTableColumn
latOfferedServiceIdentification = _LatOfferedServiceIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 4),
    _LatOfferedServiceIdentification_Type()
)
latOfferedServiceIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServiceIdentification.setStatus("mandatory")


class _LatOfferedServicePassword_Type(DisplayString):
    """Custom type latOfferedServicePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LatOfferedServicePassword_Type.__name__ = "DisplayString"
_LatOfferedServicePassword_Object = MibTableColumn
latOfferedServicePassword = _LatOfferedServicePassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 5),
    _LatOfferedServicePassword_Type()
)
latOfferedServicePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServicePassword.setStatus("mandatory")
_LatOfferedServicePortMap_Type = OctetString
_LatOfferedServicePortMap_Object = MibTableColumn
latOfferedServicePortMap = _LatOfferedServicePortMap_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 6),
    _LatOfferedServicePortMap_Type()
)
latOfferedServicePortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServicePortMap.setStatus("mandatory")


class _LatOfferedServiceQueuing_Type(Integer32):
    """Custom type latOfferedServiceQueuing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatOfferedServiceQueuing_Type.__name__ = "Integer32"
_LatOfferedServiceQueuing_Object = MibTableColumn
latOfferedServiceQueuing = _LatOfferedServiceQueuing_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 7),
    _LatOfferedServiceQueuing_Type()
)
latOfferedServiceQueuing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServiceQueuing.setStatus("mandatory")
_LatVisibleServiceTable_Object = MibTable
latVisibleServiceTable = _LatVisibleServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25)
)
if mibBuilder.loadTexts:
    latVisibleServiceTable.setStatus("mandatory")
_LatVisibleServiceEntry_Object = MibTableRow
latVisibleServiceEntry = _LatVisibleServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1)
)
latVisibleServiceEntry.setIndexNames(
    (0, "XYPLEX-LAT-MIB", "latVisibleServiceName"),
)
if mibBuilder.loadTexts:
    latVisibleServiceEntry.setStatus("mandatory")


class _LatVisibleServiceName_Type(DisplayString):
    """Custom type latVisibleServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LatVisibleServiceName_Type.__name__ = "DisplayString"
_LatVisibleServiceName_Object = MibTableColumn
latVisibleServiceName = _LatVisibleServiceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 1),
    _LatVisibleServiceName_Type()
)
latVisibleServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceName.setStatus("mandatory")


class _LatVisibleServiceStatus_Type(Integer32):
    """Custom type latVisibleServiceStatus based on Integer32"""
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
        *(("available", 1),
          ("connected", 6),
          ("reachable", 5),
          ("unavailable", 2),
          ("unknown", 3),
          ("unreachable", 4))
    )


_LatVisibleServiceStatus_Type.__name__ = "Integer32"
_LatVisibleServiceStatus_Object = MibTableColumn
latVisibleServiceStatus = _LatVisibleServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 2),
    _LatVisibleServiceStatus_Type()
)
latVisibleServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceStatus.setStatus("mandatory")


class _LatVisibleServiceNode_Type(DisplayString):
    """Custom type latVisibleServiceNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LatVisibleServiceNode_Type.__name__ = "DisplayString"
_LatVisibleServiceNode_Object = MibTableColumn
latVisibleServiceNode = _LatVisibleServiceNode_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 3),
    _LatVisibleServiceNode_Type()
)
latVisibleServiceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceNode.setStatus("mandatory")
_LatVisibleServiceConnectedSessions_Type = Gauge32
_LatVisibleServiceConnectedSessions_Object = MibTableColumn
latVisibleServiceConnectedSessions = _LatVisibleServiceConnectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 4),
    _LatVisibleServiceConnectedSessions_Type()
)
latVisibleServiceConnectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceConnectedSessions.setStatus("mandatory")


class _LatVisibleServiceIdentification_Type(DisplayString):
    """Custom type latVisibleServiceIdentification based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LatVisibleServiceIdentification_Type.__name__ = "DisplayString"
_LatVisibleServiceIdentification_Object = MibTableColumn
latVisibleServiceIdentification = _LatVisibleServiceIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 5),
    _LatVisibleServiceIdentification_Type()
)
latVisibleServiceIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceIdentification.setStatus("mandatory")
_LatVisibleServiceRating_Type = Gauge32
_LatVisibleServiceRating_Object = MibTableColumn
latVisibleServiceRating = _LatVisibleServiceRating_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 6),
    _LatVisibleServiceRating_Type()
)
latVisibleServiceRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceRating.setStatus("mandatory")
_LatNodeTable_Object = MibTable
latNodeTable = _LatNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26)
)
if mibBuilder.loadTexts:
    latNodeTable.setStatus("mandatory")
_LatNodeEntry_Object = MibTableRow
latNodeEntry = _LatNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1)
)
latNodeEntry.setIndexNames(
    (0, "XYPLEX-LAT-MIB", "latNodeName"),
)
if mibBuilder.loadTexts:
    latNodeEntry.setStatus("mandatory")


class _LatNodeName_Type(DisplayString):
    """Custom type latNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LatNodeName_Type.__name__ = "DisplayString"
_LatNodeName_Object = MibTableColumn
latNodeName = _LatNodeName_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 1),
    _LatNodeName_Type()
)
latNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeName.setStatus("mandatory")


class _LatNodeStatus_Type(Integer32):
    """Custom type latNodeStatus based on Integer32"""
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
        *(("available", 1),
          ("connected", 6),
          ("reachable", 5),
          ("unavailable", 2),
          ("unknown", 3),
          ("unreachable", 4))
    )


_LatNodeStatus_Type.__name__ = "Integer32"
_LatNodeStatus_Object = MibTableColumn
latNodeStatus = _LatNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 2),
    _LatNodeStatus_Type()
)
latNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeStatus.setStatus("mandatory")
_LatNodeConnectedSessions_Type = Gauge32
_LatNodeConnectedSessions_Object = MibTableColumn
latNodeConnectedSessions = _LatNodeConnectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 3),
    _LatNodeConnectedSessions_Type()
)
latNodeConnectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeConnectedSessions.setStatus("mandatory")


class _LatNodeAddress_Type(OctetString):
    """Custom type latNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LatNodeAddress_Type.__name__ = "OctetString"
_LatNodeAddress_Object = MibTableColumn
latNodeAddress = _LatNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 4),
    _LatNodeAddress_Type()
)
latNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeAddress.setStatus("mandatory")
_LatNodeDataLinkFrame_Type = Integer32
_LatNodeDataLinkFrame_Object = MibTableColumn
latNodeDataLinkFrame = _LatNodeDataLinkFrame_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 5),
    _LatNodeDataLinkFrame_Type()
)
latNodeDataLinkFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeDataLinkFrame.setStatus("mandatory")


class _LatNodeIdentification_Type(DisplayString):
    """Custom type latNodeIdentification based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LatNodeIdentification_Type.__name__ = "DisplayString"
_LatNodeIdentification_Object = MibTableColumn
latNodeIdentification = _LatNodeIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 6),
    _LatNodeIdentification_Type()
)
latNodeIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeIdentification.setStatus("mandatory")


class _LatNodeGroups_Type(OctetString):
    """Custom type latNodeGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LatNodeGroups_Type.__name__ = "OctetString"
_LatNodeGroups_Object = MibTableColumn
latNodeGroups = _LatNodeGroups_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 7),
    _LatNodeGroups_Type()
)
latNodeGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latNodeGroups.setStatus("mandatory")
_LatNodeServiceNumber_Type = Gauge32
_LatNodeServiceNumber_Object = MibTableColumn
latNodeServiceNumber = _LatNodeServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 8),
    _LatNodeServiceNumber_Type()
)
latNodeServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeServiceNumber.setStatus("mandatory")


class _LatNodeZero_Type(Integer32):
    """Custom type latNodeZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_LatNodeZero_Type.__name__ = "Integer32"
_LatNodeZero_Object = MibTableColumn
latNodeZero = _LatNodeZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 9),
    _LatNodeZero_Type()
)
latNodeZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latNodeZero.setStatus("mandatory")
_LatNodeZeroTime_Type = TimeTicks
_LatNodeZeroTime_Object = MibTableColumn
latNodeZeroTime = _LatNodeZeroTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 10),
    _LatNodeZeroTime_Type()
)
latNodeZeroTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeZeroTime.setStatus("mandatory")
_LatNodeInMessages_Type = Counter32
_LatNodeInMessages_Object = MibTableColumn
latNodeInMessages = _LatNodeInMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 11),
    _LatNodeInMessages_Type()
)
latNodeInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInMessages.setStatus("mandatory")
_LatNodeOutMessages_Type = Counter32
_LatNodeOutMessages_Object = MibTableColumn
latNodeOutMessages = _LatNodeOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 12),
    _LatNodeOutMessages_Type()
)
latNodeOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeOutMessages.setStatus("mandatory")
_LatNodeInSlots_Type = Counter32
_LatNodeInSlots_Object = MibTableColumn
latNodeInSlots = _LatNodeInSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 13),
    _LatNodeInSlots_Type()
)
latNodeInSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInSlots.setStatus("mandatory")
_LatNodeOutSlots_Type = Counter32
_LatNodeOutSlots_Object = MibTableColumn
latNodeOutSlots = _LatNodeOutSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 14),
    _LatNodeOutSlots_Type()
)
latNodeOutSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeOutSlots.setStatus("mandatory")
_LatNodeInBytes_Type = Counter32
_LatNodeInBytes_Object = MibTableColumn
latNodeInBytes = _LatNodeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 15),
    _LatNodeInBytes_Type()
)
latNodeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInBytes.setStatus("mandatory")
_LatNodeOutBytes_Type = Counter32
_LatNodeOutBytes_Object = MibTableColumn
latNodeOutBytes = _LatNodeOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 16),
    _LatNodeOutBytes_Type()
)
latNodeOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeOutBytes.setStatus("mandatory")
_LatNodeAddressChange_Type = Counter32
_LatNodeAddressChange_Object = MibTableColumn
latNodeAddressChange = _LatNodeAddressChange_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 17),
    _LatNodeAddressChange_Type()
)
latNodeAddressChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeAddressChange.setStatus("mandatory")
_LatNodeInDuplicates_Type = Counter32
_LatNodeInDuplicates_Object = MibTableColumn
latNodeInDuplicates = _LatNodeInDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 18),
    _LatNodeInDuplicates_Type()
)
latNodeInDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInDuplicates.setStatus("mandatory")
_LatNodeOutRetransmits_Type = Counter32
_LatNodeOutRetransmits_Object = MibTableColumn
latNodeOutRetransmits = _LatNodeOutRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 19),
    _LatNodeOutRetransmits_Type()
)
latNodeOutRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeOutRetransmits.setStatus("mandatory")
_LatNodeInBadMessages_Type = Counter32
_LatNodeInBadMessages_Object = MibTableColumn
latNodeInBadMessages = _LatNodeInBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 20),
    _LatNodeInBadMessages_Type()
)
latNodeInBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInBadMessages.setStatus("mandatory")
_LatNodeInBadSlots_Type = Counter32
_LatNodeInBadSlots_Object = MibTableColumn
latNodeInBadSlots = _LatNodeInBadSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 21),
    _LatNodeInBadSlots_Type()
)
latNodeInBadSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInBadSlots.setStatus("mandatory")
_LatNodeInSessionsAccepted_Type = Counter32
_LatNodeInSessionsAccepted_Object = MibTableColumn
latNodeInSessionsAccepted = _LatNodeInSessionsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 22),
    _LatNodeInSessionsAccepted_Type()
)
latNodeInSessionsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInSessionsAccepted.setStatus("mandatory")
_LatNodeInSessionsRejected_Type = Counter32
_LatNodeInSessionsRejected_Object = MibTableColumn
latNodeInSessionsRejected = _LatNodeInSessionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 23),
    _LatNodeInSessionsRejected_Type()
)
latNodeInSessionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInSessionsRejected.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYPLEX-LAT-MIB",
    **{"xyplex": xyplex,
       "lat": lat,
       "latAnnounceServices": latAnnounceServices,
       "latCircuitTimer": latCircuitTimer,
       "latIdentificationLengthLimit": latIdentificationLengthLimit,
       "latKeepaliveTimer": latKeepaliveTimer,
       "latMulticastTimer": latMulticastTimer,
       "latNodeLimit": latNodeLimit,
       "latNumber": latNumber,
       "latRetransmitLimit": latRetransmitLimit,
       "latLocalServiceGroups": latLocalServiceGroups,
       "latGroupPurge": latGroupPurge,
       "latNodePurge": latNodePurge,
       "latNodesRejected": latNodesRejected,
       "latInMessages": latInMessages,
       "latOutMessages": latOutMessages,
       "latInSessionsAccepted": latInSessionsAccepted,
       "latInSessionsRejected": latInSessionsRejected,
       "latAddressChange": latAddressChange,
       "latInDuplicates": latInDuplicates,
       "latOutRetransmits": latOutRetransmits,
       "latInBadMessages": latInBadMessages,
       "latInBadSlots": latInBadSlots,
       "latInBadMulticasts": latInBadMulticasts,
       "latPortTable": latPortTable,
       "latPortEntry": latPortEntry,
       "latPortIndex": latPortIndex,
       "latPortAuthorizedGroups": latPortAuthorizedGroups,
       "latPortAutoPrompt": latPortAutoPrompt,
       "latPortCurrentGroups": latPortCurrentGroups,
       "latPortRemoteModification": latPortRemoteModification,
       "latOfferedServiceTable": latOfferedServiceTable,
       "latOfferedServiceEntry": latOfferedServiceEntry,
       "latOfferedServiceName": latOfferedServiceName,
       "latOfferedServiceStatus": latOfferedServiceStatus,
       "latOfferedServiceAllowConnections": latOfferedServiceAllowConnections,
       "latOfferedServiceIdentification": latOfferedServiceIdentification,
       "latOfferedServicePassword": latOfferedServicePassword,
       "latOfferedServicePortMap": latOfferedServicePortMap,
       "latOfferedServiceQueuing": latOfferedServiceQueuing,
       "latVisibleServiceTable": latVisibleServiceTable,
       "latVisibleServiceEntry": latVisibleServiceEntry,
       "latVisibleServiceName": latVisibleServiceName,
       "latVisibleServiceStatus": latVisibleServiceStatus,
       "latVisibleServiceNode": latVisibleServiceNode,
       "latVisibleServiceConnectedSessions": latVisibleServiceConnectedSessions,
       "latVisibleServiceIdentification": latVisibleServiceIdentification,
       "latVisibleServiceRating": latVisibleServiceRating,
       "latNodeTable": latNodeTable,
       "latNodeEntry": latNodeEntry,
       "latNodeName": latNodeName,
       "latNodeStatus": latNodeStatus,
       "latNodeConnectedSessions": latNodeConnectedSessions,
       "latNodeAddress": latNodeAddress,
       "latNodeDataLinkFrame": latNodeDataLinkFrame,
       "latNodeIdentification": latNodeIdentification,
       "latNodeGroups": latNodeGroups,
       "latNodeServiceNumber": latNodeServiceNumber,
       "latNodeZero": latNodeZero,
       "latNodeZeroTime": latNodeZeroTime,
       "latNodeInMessages": latNodeInMessages,
       "latNodeOutMessages": latNodeOutMessages,
       "latNodeInSlots": latNodeInSlots,
       "latNodeOutSlots": latNodeOutSlots,
       "latNodeInBytes": latNodeInBytes,
       "latNodeOutBytes": latNodeOutBytes,
       "latNodeAddressChange": latNodeAddressChange,
       "latNodeInDuplicates": latNodeInDuplicates,
       "latNodeOutRetransmits": latNodeOutRetransmits,
       "latNodeInBadMessages": latNodeInBadMessages,
       "latNodeInBadSlots": latNodeInBadSlots,
       "latNodeInSessionsAccepted": latNodeInSessionsAccepted,
       "latNodeInSessionsRejected": latNodeInSessionsRejected}
)
