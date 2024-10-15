# SNMP MIB module (IEEE8021X-PAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021X-PAE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:48 2024
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

(SecySCI,) = mibBuilder.importSymbols(
    "IEEE8021-SECY-MIB",
    "SecySCI")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ieee8021XPaeMIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15)
)
ieee8021XPaeMIB.setRevisions(
        ("2017-10-28 14:57",
         "2014-04-10 16:19",
         "2009-10-01 16:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Ieee8021XPaeCKN(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class Ieee8021XPaeCKNOrNull(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class Ieee8021XPaeKMD(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )



class Ieee8021XPaeNID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )



class Ieee8021XPaeNIDOrNull(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )



class Ieee8021XMkaKeyServerPriority(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class Ieee8021XMkaMI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )



class Ieee8021XMkaMN(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )



class Ieee8021XMkaKN(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )



class Ieee8021XPaeNIDCapabilites(Bits, TextualConvention):
    status = "current"


class Ieee8021XPaeNIDAccessStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expectedAccess", 3),
          ("noAccess", 0),
          ("remedialAccess", 1),
          ("restrictedAccess", 2))
    )



class Ieee8021XPaeNIDUnauthenticatedStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallbackAccess", 1),
          ("limitedAccess", 2),
          ("noAccess", 0),
          ("openAccess", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Ieee8021XPaeMIBNotifications_ObjectIdentity = ObjectIdentity
ieee8021XPaeMIBNotifications = _Ieee8021XPaeMIBNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 0)
)
_Ieee8021XPaeMIBObjects_ObjectIdentity = ObjectIdentity
ieee8021XPaeMIBObjects = _Ieee8021XPaeMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 1)
)
_Ieee8021XPaeSystem_ObjectIdentity = ObjectIdentity
ieee8021XPaeSystem = _Ieee8021XPaeSystem_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1)
)
_Ieee8021XPaeSysAccessControl_Type = TruthValue
_Ieee8021XPaeSysAccessControl_Object = MibScalar
ieee8021XPaeSysAccessControl = _Ieee8021XPaeSysAccessControl_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 1),
    _Ieee8021XPaeSysAccessControl_Type()
)
ieee8021XPaeSysAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XPaeSysAccessControl.setStatus("current")
_Ieee8021XPaeSysAnnouncements_Type = TruthValue
_Ieee8021XPaeSysAnnouncements_Object = MibScalar
ieee8021XPaeSysAnnouncements = _Ieee8021XPaeSysAnnouncements_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 2),
    _Ieee8021XPaeSysAnnouncements_Type()
)
ieee8021XPaeSysAnnouncements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XPaeSysAnnouncements.setStatus("current")
_Ieee8021XPaeSysEapolVersion_Type = Unsigned32
_Ieee8021XPaeSysEapolVersion_Object = MibScalar
ieee8021XPaeSysEapolVersion = _Ieee8021XPaeSysEapolVersion_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 3),
    _Ieee8021XPaeSysEapolVersion_Type()
)
ieee8021XPaeSysEapolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaeSysEapolVersion.setStatus("current")
_Ieee8021XPaeSysMkaVersion_Type = Unsigned32
_Ieee8021XPaeSysMkaVersion_Object = MibScalar
ieee8021XPaeSysMkaVersion = _Ieee8021XPaeSysMkaVersion_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 4),
    _Ieee8021XPaeSysMkaVersion_Type()
)
ieee8021XPaeSysMkaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaeSysMkaVersion.setStatus("current")
_Ieee8021XPaePortTable_Object = MibTable
ieee8021XPaePortTable = _Ieee8021XPaePortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021XPaePortTable.setStatus("current")
_Ieee8021XPaePortEntry_Object = MibTableRow
ieee8021XPaePortEntry = _Ieee8021XPaePortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1)
)
ieee8021XPaePortEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021XPaePortEntry.setStatus("current")
_Ieee8021XPaePortNumber_Type = InterfaceIndex
_Ieee8021XPaePortNumber_Object = MibTableColumn
ieee8021XPaePortNumber = _Ieee8021XPaePortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 1),
    _Ieee8021XPaePortNumber_Type()
)
ieee8021XPaePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021XPaePortNumber.setStatus("current")


class _Ieee8021XPaePortType_Type(Integer32):
    """Custom type ieee8021XPaePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("realPort", 1),
          ("virtualPort", 2))
    )


_Ieee8021XPaePortType_Type.__name__ = "Integer32"
_Ieee8021XPaePortType_Object = MibTableColumn
ieee8021XPaePortType = _Ieee8021XPaePortType_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 2),
    _Ieee8021XPaePortType_Type()
)
ieee8021XPaePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortType.setStatus("current")
_Ieee8021XPaeControlledPortNumber_Type = InterfaceIndex
_Ieee8021XPaeControlledPortNumber_Object = MibTableColumn
ieee8021XPaeControlledPortNumber = _Ieee8021XPaeControlledPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 3),
    _Ieee8021XPaeControlledPortNumber_Type()
)
ieee8021XPaeControlledPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaeControlledPortNumber.setStatus("current")
_Ieee8021XPaeUncontrolledPortNumber_Type = InterfaceIndex
_Ieee8021XPaeUncontrolledPortNumber_Object = MibTableColumn
ieee8021XPaeUncontrolledPortNumber = _Ieee8021XPaeUncontrolledPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 4),
    _Ieee8021XPaeUncontrolledPortNumber_Type()
)
ieee8021XPaeUncontrolledPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaeUncontrolledPortNumber.setStatus("current")
_Ieee8021XPaeCommonPortNumber_Type = InterfaceIndex
_Ieee8021XPaeCommonPortNumber_Object = MibTableColumn
ieee8021XPaeCommonPortNumber = _Ieee8021XPaeCommonPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 5),
    _Ieee8021XPaeCommonPortNumber_Type()
)
ieee8021XPaeCommonPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaeCommonPortNumber.setStatus("current")
_Ieee8021XPaePortInitialize_Type = TruthValue
_Ieee8021XPaePortInitialize_Object = MibTableColumn
ieee8021XPaePortInitialize = _Ieee8021XPaePortInitialize_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 6),
    _Ieee8021XPaePortInitialize_Type()
)
ieee8021XPaePortInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XPaePortInitialize.setStatus("current")


class _Ieee8021XPaePortCapabilities_Type(Bits):
    """Custom type ieee8021XPaePortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("announcementsImplemented", 4),
          ("authImplemented", 1),
          ("listenerImplemented", 5),
          ("macsecImplemented", 3),
          ("mkaImplemented", 2),
          ("suppImplemented", 0),
          ("virtualPortsImplemented", 6))
    )

_Ieee8021XPaePortCapabilities_Type.__name__ = "Bits"
_Ieee8021XPaePortCapabilities_Object = MibTableColumn
ieee8021XPaePortCapabilities = _Ieee8021XPaePortCapabilities_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 7),
    _Ieee8021XPaePortCapabilities_Type()
)
ieee8021XPaePortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortCapabilities.setStatus("current")
_Ieee8021XPaePortVirtualPortsEnable_Type = TruthValue
_Ieee8021XPaePortVirtualPortsEnable_Object = MibTableColumn
ieee8021XPaePortVirtualPortsEnable = _Ieee8021XPaePortVirtualPortsEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 8),
    _Ieee8021XPaePortVirtualPortsEnable_Type()
)
ieee8021XPaePortVirtualPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XPaePortVirtualPortsEnable.setStatus("current")
_Ieee8021XPaePortMaxVirtualPorts_Type = Unsigned32
_Ieee8021XPaePortMaxVirtualPorts_Object = MibTableColumn
ieee8021XPaePortMaxVirtualPorts = _Ieee8021XPaePortMaxVirtualPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 9),
    _Ieee8021XPaePortMaxVirtualPorts_Type()
)
ieee8021XPaePortMaxVirtualPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortMaxVirtualPorts.setStatus("current")
_Ieee8021XPaePortCurrentVirtualPorts_Type = Gauge32
_Ieee8021XPaePortCurrentVirtualPorts_Object = MibTableColumn
ieee8021XPaePortCurrentVirtualPorts = _Ieee8021XPaePortCurrentVirtualPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 10),
    _Ieee8021XPaePortCurrentVirtualPorts_Type()
)
ieee8021XPaePortCurrentVirtualPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortCurrentVirtualPorts.setStatus("current")
_Ieee8021XPaePortVirtualPortStart_Type = TruthValue
_Ieee8021XPaePortVirtualPortStart_Object = MibTableColumn
ieee8021XPaePortVirtualPortStart = _Ieee8021XPaePortVirtualPortStart_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 11),
    _Ieee8021XPaePortVirtualPortStart_Type()
)
ieee8021XPaePortVirtualPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortVirtualPortStart.setStatus("current")
_Ieee8021XPaePortVirtualPortPeerMAC_Type = MacAddress
_Ieee8021XPaePortVirtualPortPeerMAC_Object = MibTableColumn
ieee8021XPaePortVirtualPortPeerMAC = _Ieee8021XPaePortVirtualPortPeerMAC_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 12),
    _Ieee8021XPaePortVirtualPortPeerMAC_Type()
)
ieee8021XPaePortVirtualPortPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortVirtualPortPeerMAC.setStatus("current")
_Ieee8021XPaePortLogonEnable_Type = TruthValue
_Ieee8021XPaePortLogonEnable_Object = MibTableColumn
ieee8021XPaePortLogonEnable = _Ieee8021XPaePortLogonEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 13),
    _Ieee8021XPaePortLogonEnable_Type()
)
ieee8021XPaePortLogonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XPaePortLogonEnable.setStatus("current")
_Ieee8021XPaePortAuthenticatorEnable_Type = TruthValue
_Ieee8021XPaePortAuthenticatorEnable_Object = MibTableColumn
ieee8021XPaePortAuthenticatorEnable = _Ieee8021XPaePortAuthenticatorEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 14),
    _Ieee8021XPaePortAuthenticatorEnable_Type()
)
ieee8021XPaePortAuthenticatorEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortAuthenticatorEnable.setStatus("current")
_Ieee8021XPaePortSupplicantEnable_Type = TruthValue
_Ieee8021XPaePortSupplicantEnable_Object = MibTableColumn
ieee8021XPaePortSupplicantEnable = _Ieee8021XPaePortSupplicantEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 15),
    _Ieee8021XPaePortSupplicantEnable_Type()
)
ieee8021XPaePortSupplicantEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortSupplicantEnable.setStatus("current")
_Ieee8021XPaePortKayMkaEnable_Type = TruthValue
_Ieee8021XPaePortKayMkaEnable_Object = MibTableColumn
ieee8021XPaePortKayMkaEnable = _Ieee8021XPaePortKayMkaEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 16),
    _Ieee8021XPaePortKayMkaEnable_Type()
)
ieee8021XPaePortKayMkaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XPaePortKayMkaEnable.setStatus("current")
_Ieee8021XPaePortAnnouncerEnable_Type = TruthValue
_Ieee8021XPaePortAnnouncerEnable_Object = MibTableColumn
ieee8021XPaePortAnnouncerEnable = _Ieee8021XPaePortAnnouncerEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 17),
    _Ieee8021XPaePortAnnouncerEnable_Type()
)
ieee8021XPaePortAnnouncerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XPaePortAnnouncerEnable.setStatus("current")
_Ieee8021XPaePortListenerEnable_Type = TruthValue
_Ieee8021XPaePortListenerEnable_Object = MibTableColumn
ieee8021XPaePortListenerEnable = _Ieee8021XPaePortListenerEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 18),
    _Ieee8021XPaePortListenerEnable_Type()
)
ieee8021XPaePortListenerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XPaePortListenerEnable.setStatus("current")
_Ieee8021XPaeEapolGroupMAC_Type = MacAddress
_Ieee8021XPaeEapolGroupMAC_Object = MibTableColumn
ieee8021XPaeEapolGroupMAC = _Ieee8021XPaeEapolGroupMAC_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 5, 1, 19),
    _Ieee8021XPaeEapolGroupMAC_Type()
)
ieee8021XPaeEapolGroupMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaeEapolGroupMAC.setStatus("current")
_Ieee8021XPacPortTable_Object = MibTable
ieee8021XPacPortTable = _Ieee8021XPacPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021XPacPortTable.setStatus("current")
_Ieee8021XPacPortEntry_Object = MibTableRow
ieee8021XPacPortEntry = _Ieee8021XPacPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 6, 1)
)
ieee8021XPacPortEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPacPortControlledPortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021XPacPortEntry.setStatus("current")
_Ieee8021XPacPortControlledPortNumber_Type = InterfaceIndex
_Ieee8021XPacPortControlledPortNumber_Object = MibTableColumn
ieee8021XPacPortControlledPortNumber = _Ieee8021XPacPortControlledPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 6, 1, 1),
    _Ieee8021XPacPortControlledPortNumber_Type()
)
ieee8021XPacPortControlledPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021XPacPortControlledPortNumber.setStatus("current")


class _Ieee8021XPacPortAdminPt2PtMAC_Type(Integer32):
    """Custom type ieee8021XPacPortAdminPt2PtMAC based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("forceFalse", 2),
          ("forceTrue", 1))
    )


_Ieee8021XPacPortAdminPt2PtMAC_Type.__name__ = "Integer32"
_Ieee8021XPacPortAdminPt2PtMAC_Object = MibTableColumn
ieee8021XPacPortAdminPt2PtMAC = _Ieee8021XPacPortAdminPt2PtMAC_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 6, 1, 2),
    _Ieee8021XPacPortAdminPt2PtMAC_Type()
)
ieee8021XPacPortAdminPt2PtMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XPacPortAdminPt2PtMAC.setStatus("current")
_Ieee8021XPacPortOperPt2PtMAC_Type = TruthValue
_Ieee8021XPacPortOperPt2PtMAC_Object = MibTableColumn
ieee8021XPacPortOperPt2PtMAC = _Ieee8021XPacPortOperPt2PtMAC_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 1, 6, 1, 3),
    _Ieee8021XPacPortOperPt2PtMAC_Type()
)
ieee8021XPacPortOperPt2PtMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPacPortOperPt2PtMAC.setStatus("current")
_Ieee8021XPaeLogon_ObjectIdentity = ObjectIdentity
ieee8021XPaeLogon = _Ieee8021XPaeLogon_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2)
)
_Ieee8021XPaePortLogonTable_Object = MibTable
ieee8021XPaePortLogonTable = _Ieee8021XPaePortLogonTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021XPaePortLogonTable.setStatus("current")
_Ieee8021XPaePortLogonEntry_Object = MibTableRow
ieee8021XPaePortLogonEntry = _Ieee8021XPaePortLogonEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 1, 1)
)
ieee8021XPaePortLogonEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021XPaePortLogonEntry.setStatus("current")


class _Ieee8021XPaePortLogonConnectStatus_Type(Integer32):
    """Custom type ieee8021XPaePortLogonConnectStatus based on Integer32"""
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
        *(("authenticated", 3),
          ("pending", 1),
          ("secure", 4),
          ("unauthenticated", 2))
    )


_Ieee8021XPaePortLogonConnectStatus_Type.__name__ = "Integer32"
_Ieee8021XPaePortLogonConnectStatus_Object = MibTableColumn
ieee8021XPaePortLogonConnectStatus = _Ieee8021XPaePortLogonConnectStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 1, 1, 1),
    _Ieee8021XPaePortLogonConnectStatus_Type()
)
ieee8021XPaePortLogonConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortLogonConnectStatus.setStatus("current")
_Ieee8021XPaePortPortValid_Type = TruthValue
_Ieee8021XPaePortPortValid_Object = MibTableColumn
ieee8021XPaePortPortValid = _Ieee8021XPaePortPortValid_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 1, 1, 2),
    _Ieee8021XPaePortPortValid_Type()
)
ieee8021XPaePortPortValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortPortValid.setStatus("current")
_Ieee8021XPaePortSessionTable_Object = MibTable
ieee8021XPaePortSessionTable = _Ieee8021XPaePortSessionTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionTable.setStatus("current")
_Ieee8021XPaePortSessionEntry_Object = MibTableRow
ieee8021XPaePortSessionEntry = _Ieee8021XPaePortSessionEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1)
)
ieee8021XPaePortSessionEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaeSessionControlledPortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionEntry.setStatus("current")
_Ieee8021XPaeSessionControlledPortNumber_Type = InterfaceIndex
_Ieee8021XPaeSessionControlledPortNumber_Object = MibTableColumn
ieee8021XPaeSessionControlledPortNumber = _Ieee8021XPaeSessionControlledPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1, 1),
    _Ieee8021XPaeSessionControlledPortNumber_Type()
)
ieee8021XPaeSessionControlledPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021XPaeSessionControlledPortNumber.setStatus("current")
_Ieee8021XPaePortSessionOctetsRx_Type = Counter64
_Ieee8021XPaePortSessionOctetsRx_Object = MibTableColumn
ieee8021XPaePortSessionOctetsRx = _Ieee8021XPaePortSessionOctetsRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1, 2),
    _Ieee8021XPaePortSessionOctetsRx_Type()
)
ieee8021XPaePortSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionOctetsRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionOctetsRx.setUnits("Octets")
_Ieee8021XPaePortSessionOctetsTx_Type = Counter64
_Ieee8021XPaePortSessionOctetsTx_Object = MibTableColumn
ieee8021XPaePortSessionOctetsTx = _Ieee8021XPaePortSessionOctetsTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1, 3),
    _Ieee8021XPaePortSessionOctetsTx_Type()
)
ieee8021XPaePortSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionOctetsTx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionOctetsTx.setUnits("Octets")
_Ieee8021XPaePortSessionPktsRx_Type = Counter64
_Ieee8021XPaePortSessionPktsRx_Object = MibTableColumn
ieee8021XPaePortSessionPktsRx = _Ieee8021XPaePortSessionPktsRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1, 4),
    _Ieee8021XPaePortSessionPktsRx_Type()
)
ieee8021XPaePortSessionPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionPktsRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionPktsRx.setUnits("Packets")
_Ieee8021XPaePortSessionPktsTx_Type = Counter64
_Ieee8021XPaePortSessionPktsTx_Object = MibTableColumn
ieee8021XPaePortSessionPktsTx = _Ieee8021XPaePortSessionPktsTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1, 5),
    _Ieee8021XPaePortSessionPktsTx_Type()
)
ieee8021XPaePortSessionPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionPktsTx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionPktsTx.setUnits("Packets")


class _Ieee8021XPaePortSessionId_Type(SnmpAdminString):
    """Custom type ieee8021XPaePortSessionId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 253),
    )


_Ieee8021XPaePortSessionId_Type.__name__ = "SnmpAdminString"
_Ieee8021XPaePortSessionId_Object = MibTableColumn
ieee8021XPaePortSessionId = _Ieee8021XPaePortSessionId_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1, 6),
    _Ieee8021XPaePortSessionId_Type()
)
ieee8021XPaePortSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionId.setStatus("current")
_Ieee8021XPaePortSessionStartTime_Type = TimeStamp
_Ieee8021XPaePortSessionStartTime_Object = MibTableColumn
ieee8021XPaePortSessionStartTime = _Ieee8021XPaePortSessionStartTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1, 7),
    _Ieee8021XPaePortSessionStartTime_Type()
)
ieee8021XPaePortSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionStartTime.setStatus("current")
_Ieee8021XPaePortSessionIntervalTime_Type = TimeInterval
_Ieee8021XPaePortSessionIntervalTime_Object = MibTableColumn
ieee8021XPaePortSessionIntervalTime = _Ieee8021XPaePortSessionIntervalTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1, 8),
    _Ieee8021XPaePortSessionIntervalTime_Type()
)
ieee8021XPaePortSessionIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionIntervalTime.setStatus("current")


class _Ieee8021XPaePortSessionTerminate_Type(Integer32):
    """Custom type ieee8021XPaePortSessionTerminate based on Integer32"""
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
        *(("eapReauthFailure", 4),
          ("macOperFailed", 1),
          ("mkaFailure", 5),
          ("newSessionBegin", 6),
          ("notTerminateYet", 7),
          ("receiveEapolLogOff", 3),
          ("sysAccessDisableOrPortInit", 2))
    )


_Ieee8021XPaePortSessionTerminate_Type.__name__ = "Integer32"
_Ieee8021XPaePortSessionTerminate_Object = MibTableColumn
ieee8021XPaePortSessionTerminate = _Ieee8021XPaePortSessionTerminate_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1, 9),
    _Ieee8021XPaePortSessionTerminate_Type()
)
ieee8021XPaePortSessionTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionTerminate.setStatus("current")


class _Ieee8021XPaePortSessionUserName_Type(SnmpAdminString):
    """Custom type ieee8021XPaePortSessionUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_Ieee8021XPaePortSessionUserName_Type.__name__ = "SnmpAdminString"
_Ieee8021XPaePortSessionUserName_Object = MibTableColumn
ieee8021XPaePortSessionUserName = _Ieee8021XPaePortSessionUserName_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 2, 1, 10),
    _Ieee8021XPaePortSessionUserName_Type()
)
ieee8021XPaePortSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XPaePortSessionUserName.setStatus("current")
_Ieee8021XLogonNIDTable_Object = MibTable
ieee8021XLogonNIDTable = _Ieee8021XLogonNIDTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ieee8021XLogonNIDTable.setStatus("current")
_Ieee8021XLogonNIDEntry_Object = MibTableRow
ieee8021XLogonNIDEntry = _Ieee8021XLogonNIDEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 3, 1)
)
ieee8021XLogonNIDEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021XLogonNIDEntry.setStatus("current")
_Ieee8021XLogonNIDConnectedNID_Type = Ieee8021XPaeNID
_Ieee8021XLogonNIDConnectedNID_Object = MibTableColumn
ieee8021XLogonNIDConnectedNID = _Ieee8021XLogonNIDConnectedNID_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 3, 1, 1),
    _Ieee8021XLogonNIDConnectedNID_Type()
)
ieee8021XLogonNIDConnectedNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XLogonNIDConnectedNID.setStatus("current")
_Ieee8021XLogonNIDRequestedNID_Type = Ieee8021XPaeNIDOrNull
_Ieee8021XLogonNIDRequestedNID_Object = MibTableColumn
ieee8021XLogonNIDRequestedNID = _Ieee8021XLogonNIDRequestedNID_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 3, 1, 2),
    _Ieee8021XLogonNIDRequestedNID_Type()
)
ieee8021XLogonNIDRequestedNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XLogonNIDRequestedNID.setStatus("current")
_Ieee8021XLogonNIDSelectedNID_Type = Ieee8021XPaeNIDOrNull
_Ieee8021XLogonNIDSelectedNID_Object = MibTableColumn
ieee8021XLogonNIDSelectedNID = _Ieee8021XLogonNIDSelectedNID_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 2, 3, 1, 3),
    _Ieee8021XLogonNIDSelectedNID_Type()
)
ieee8021XLogonNIDSelectedNID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XLogonNIDSelectedNID.setStatus("current")
_Ieee8021XPaeAuthenticator_ObjectIdentity = ObjectIdentity
ieee8021XPaeAuthenticator = _Ieee8021XPaeAuthenticator_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3)
)
_Ieee8021XAuthenticatorTable_Object = MibTable
ieee8021XAuthenticatorTable = _Ieee8021XAuthenticatorTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021XAuthenticatorTable.setStatus("current")
_Ieee8021XAuthenticatorEntry_Object = MibTableRow
ieee8021XAuthenticatorEntry = _Ieee8021XAuthenticatorEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3, 1, 1)
)
ieee8021XAuthenticatorEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021XAuthenticatorEntry.setStatus("current")
_Ieee8021XAuthPaeAuthenticate_Type = TruthValue
_Ieee8021XAuthPaeAuthenticate_Object = MibTableColumn
ieee8021XAuthPaeAuthenticate = _Ieee8021XAuthPaeAuthenticate_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3, 1, 1, 1),
    _Ieee8021XAuthPaeAuthenticate_Type()
)
ieee8021XAuthPaeAuthenticate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeAuthenticate.setStatus("current")
_Ieee8021XAuthPaeAuthenticated_Type = TruthValue
_Ieee8021XAuthPaeAuthenticated_Object = MibTableColumn
ieee8021XAuthPaeAuthenticated = _Ieee8021XAuthPaeAuthenticated_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3, 1, 1, 2),
    _Ieee8021XAuthPaeAuthenticated_Type()
)
ieee8021XAuthPaeAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeAuthenticated.setStatus("current")
_Ieee8021XAuthPaeFailed_Type = TruthValue
_Ieee8021XAuthPaeFailed_Object = MibTableColumn
ieee8021XAuthPaeFailed = _Ieee8021XAuthPaeFailed_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3, 1, 1, 3),
    _Ieee8021XAuthPaeFailed_Type()
)
ieee8021XAuthPaeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeFailed.setStatus("current")
_Ieee8021XAuthPaeReAuthEnabled_Type = TruthValue
_Ieee8021XAuthPaeReAuthEnabled_Object = MibTableColumn
ieee8021XAuthPaeReAuthEnabled = _Ieee8021XAuthPaeReAuthEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3, 1, 1, 4),
    _Ieee8021XAuthPaeReAuthEnabled_Type()
)
ieee8021XAuthPaeReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeReAuthEnabled.setStatus("current")


class _Ieee8021XAuthPaeQuietPeriod_Type(Unsigned32):
    """Custom type ieee8021XAuthPaeQuietPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021XAuthPaeQuietPeriod_Type.__name__ = "Unsigned32"
_Ieee8021XAuthPaeQuietPeriod_Object = MibTableColumn
ieee8021XAuthPaeQuietPeriod = _Ieee8021XAuthPaeQuietPeriod_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3, 1, 1, 5),
    _Ieee8021XAuthPaeQuietPeriod_Type()
)
ieee8021XAuthPaeQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeQuietPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeQuietPeriod.setUnits("seconds")


class _Ieee8021XAuthPaeReauthPeriod_Type(Unsigned32):
    """Custom type ieee8021XAuthPaeReauthPeriod based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021XAuthPaeReauthPeriod_Type.__name__ = "Unsigned32"
_Ieee8021XAuthPaeReauthPeriod_Object = MibTableColumn
ieee8021XAuthPaeReauthPeriod = _Ieee8021XAuthPaeReauthPeriod_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3, 1, 1, 6),
    _Ieee8021XAuthPaeReauthPeriod_Type()
)
ieee8021XAuthPaeReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeReauthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeReauthPeriod.setUnits("seconds")


class _Ieee8021XAuthPaeRetryMax_Type(Unsigned32):
    """Custom type ieee8021XAuthPaeRetryMax based on Unsigned32"""
    defaultValue = 2


_Ieee8021XAuthPaeRetryMax_Object = MibTableColumn
ieee8021XAuthPaeRetryMax = _Ieee8021XAuthPaeRetryMax_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3, 1, 1, 7),
    _Ieee8021XAuthPaeRetryMax_Type()
)
ieee8021XAuthPaeRetryMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeRetryMax.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeRetryMax.setUnits("times")
_Ieee8021XAuthPaeRetryCount_Type = Gauge32
_Ieee8021XAuthPaeRetryCount_Object = MibTableColumn
ieee8021XAuthPaeRetryCount = _Ieee8021XAuthPaeRetryCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 3, 1, 1, 8),
    _Ieee8021XAuthPaeRetryCount_Type()
)
ieee8021XAuthPaeRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeRetryCount.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XAuthPaeRetryCount.setUnits("times")
_Ieee8021XPaeSupplicant_ObjectIdentity = ObjectIdentity
ieee8021XPaeSupplicant = _Ieee8021XPaeSupplicant_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 4)
)
_Ieee8021XSupplicantTable_Object = MibTable
ieee8021XSupplicantTable = _Ieee8021XSupplicantTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ieee8021XSupplicantTable.setStatus("current")
_Ieee8021XSupplicantEntry_Object = MibTableRow
ieee8021XSupplicantEntry = _Ieee8021XSupplicantEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 4, 1, 1)
)
ieee8021XSupplicantEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021XSupplicantEntry.setStatus("current")
_Ieee8021XSuppPaeAuthenticate_Type = TruthValue
_Ieee8021XSuppPaeAuthenticate_Object = MibTableColumn
ieee8021XSuppPaeAuthenticate = _Ieee8021XSuppPaeAuthenticate_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 4, 1, 1, 1),
    _Ieee8021XSuppPaeAuthenticate_Type()
)
ieee8021XSuppPaeAuthenticate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XSuppPaeAuthenticate.setStatus("current")
_Ieee8021XSuppPaeAuthenticated_Type = TruthValue
_Ieee8021XSuppPaeAuthenticated_Object = MibTableColumn
ieee8021XSuppPaeAuthenticated = _Ieee8021XSuppPaeAuthenticated_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 4, 1, 1, 2),
    _Ieee8021XSuppPaeAuthenticated_Type()
)
ieee8021XSuppPaeAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XSuppPaeAuthenticated.setStatus("current")
_Ieee8021XSuppPaeFailed_Type = TruthValue
_Ieee8021XSuppPaeFailed_Object = MibTableColumn
ieee8021XSuppPaeFailed = _Ieee8021XSuppPaeFailed_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 4, 1, 1, 3),
    _Ieee8021XSuppPaeFailed_Type()
)
ieee8021XSuppPaeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XSuppPaeFailed.setStatus("current")


class _Ieee8021XSuppPaeHelloPeriod_Type(Unsigned32):
    """Custom type ieee8021XSuppPaeHelloPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021XSuppPaeHelloPeriod_Type.__name__ = "Unsigned32"
_Ieee8021XSuppPaeHelloPeriod_Object = MibTableColumn
ieee8021XSuppPaeHelloPeriod = _Ieee8021XSuppPaeHelloPeriod_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 4, 1, 1, 4),
    _Ieee8021XSuppPaeHelloPeriod_Type()
)
ieee8021XSuppPaeHelloPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XSuppPaeHelloPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XSuppPaeHelloPeriod.setUnits("seconds")


class _Ieee8021XSuppPaeRetryMax_Type(Unsigned32):
    """Custom type ieee8021XSuppPaeRetryMax based on Unsigned32"""
    defaultValue = 2


_Ieee8021XSuppPaeRetryMax_Object = MibTableColumn
ieee8021XSuppPaeRetryMax = _Ieee8021XSuppPaeRetryMax_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 4, 1, 1, 5),
    _Ieee8021XSuppPaeRetryMax_Type()
)
ieee8021XSuppPaeRetryMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XSuppPaeRetryMax.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XSuppPaeRetryMax.setUnits("times")
_Ieee8021XSuppPaeRetryCount_Type = Gauge32
_Ieee8021XSuppPaeRetryCount_Object = MibTableColumn
ieee8021XSuppPaeRetryCount = _Ieee8021XSuppPaeRetryCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 4, 1, 1, 6),
    _Ieee8021XSuppPaeRetryCount_Type()
)
ieee8021XSuppPaeRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XSuppPaeRetryCount.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XSuppPaeRetryCount.setUnits("times")
_Ieee8021XPaeEapol_ObjectIdentity = ObjectIdentity
ieee8021XPaeEapol = _Ieee8021XPaeEapol_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5)
)
_Ieee8021XEapolStatsTable_Object = MibTable
ieee8021XEapolStatsTable = _Ieee8021XEapolStatsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ieee8021XEapolStatsTable.setStatus("current")
_Ieee8021XEapolStatsEntry_Object = MibTableRow
ieee8021XEapolStatsEntry = _Ieee8021XEapolStatsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1)
)
ieee8021XEapolStatsEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021XEapolStatsEntry.setStatus("current")
_Ieee8021XEapolInvalidFramesRx_Type = Counter32
_Ieee8021XEapolInvalidFramesRx_Object = MibTableColumn
ieee8021XEapolInvalidFramesRx = _Ieee8021XEapolInvalidFramesRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 1),
    _Ieee8021XEapolInvalidFramesRx_Type()
)
ieee8021XEapolInvalidFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolInvalidFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolInvalidFramesRx.setUnits("Packets")
_Ieee8021XEapolEapLengthErrorFramesRx_Type = Counter32
_Ieee8021XEapolEapLengthErrorFramesRx_Object = MibTableColumn
ieee8021XEapolEapLengthErrorFramesRx = _Ieee8021XEapolEapLengthErrorFramesRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 2),
    _Ieee8021XEapolEapLengthErrorFramesRx_Type()
)
ieee8021XEapolEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolEapLengthErrorFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolEapLengthErrorFramesRx.setUnits("Packets")
_Ieee8021XEapolAnnouncementFramesRx_Type = Counter32
_Ieee8021XEapolAnnouncementFramesRx_Object = MibTableColumn
ieee8021XEapolAnnouncementFramesRx = _Ieee8021XEapolAnnouncementFramesRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 3),
    _Ieee8021XEapolAnnouncementFramesRx_Type()
)
ieee8021XEapolAnnouncementFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolAnnouncementFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolAnnouncementFramesRx.setUnits("Packets")
_Ieee8021XEapolAnnouncementReqFramesRx_Type = Counter32
_Ieee8021XEapolAnnouncementReqFramesRx_Object = MibTableColumn
ieee8021XEapolAnnouncementReqFramesRx = _Ieee8021XEapolAnnouncementReqFramesRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 4),
    _Ieee8021XEapolAnnouncementReqFramesRx_Type()
)
ieee8021XEapolAnnouncementReqFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolAnnouncementReqFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolAnnouncementReqFramesRx.setUnits("Packets")
_Ieee8021XEapolPortUnavailableFramesRx_Type = Counter32
_Ieee8021XEapolPortUnavailableFramesRx_Object = MibTableColumn
ieee8021XEapolPortUnavailableFramesRx = _Ieee8021XEapolPortUnavailableFramesRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 5),
    _Ieee8021XEapolPortUnavailableFramesRx_Type()
)
ieee8021XEapolPortUnavailableFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolPortUnavailableFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolPortUnavailableFramesRx.setUnits("Packets")
_Ieee8021XEapolStartFramesRx_Type = Counter32
_Ieee8021XEapolStartFramesRx_Object = MibTableColumn
ieee8021XEapolStartFramesRx = _Ieee8021XEapolStartFramesRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 6),
    _Ieee8021XEapolStartFramesRx_Type()
)
ieee8021XEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolStartFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolStartFramesRx.setUnits("Packets")
_Ieee8021XEapolEapFramesRx_Type = Counter32
_Ieee8021XEapolEapFramesRx_Object = MibTableColumn
ieee8021XEapolEapFramesRx = _Ieee8021XEapolEapFramesRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 7),
    _Ieee8021XEapolEapFramesRx_Type()
)
ieee8021XEapolEapFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolEapFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolEapFramesRx.setUnits("Packets")
_Ieee8021XEapolLogoffFramesRx_Type = Counter32
_Ieee8021XEapolLogoffFramesRx_Object = MibTableColumn
ieee8021XEapolLogoffFramesRx = _Ieee8021XEapolLogoffFramesRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 8),
    _Ieee8021XEapolLogoffFramesRx_Type()
)
ieee8021XEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolLogoffFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolLogoffFramesRx.setUnits("Packets")
_Ieee8021XEapolMkNoCknFramesRx_Type = Counter32
_Ieee8021XEapolMkNoCknFramesRx_Object = MibTableColumn
ieee8021XEapolMkNoCknFramesRx = _Ieee8021XEapolMkNoCknFramesRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 9),
    _Ieee8021XEapolMkNoCknFramesRx_Type()
)
ieee8021XEapolMkNoCknFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolMkNoCknFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolMkNoCknFramesRx.setUnits("Packets")
_Ieee8021XEapolMkInvalidFramesRx_Type = Counter32
_Ieee8021XEapolMkInvalidFramesRx_Object = MibTableColumn
ieee8021XEapolMkInvalidFramesRx = _Ieee8021XEapolMkInvalidFramesRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 10),
    _Ieee8021XEapolMkInvalidFramesRx_Type()
)
ieee8021XEapolMkInvalidFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolMkInvalidFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolMkInvalidFramesRx.setUnits("Packets")
_Ieee8021XEapolLastRxFrameVersion_Type = Unsigned32
_Ieee8021XEapolLastRxFrameVersion_Object = MibTableColumn
ieee8021XEapolLastRxFrameVersion = _Ieee8021XEapolLastRxFrameVersion_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 11),
    _Ieee8021XEapolLastRxFrameVersion_Type()
)
ieee8021XEapolLastRxFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolLastRxFrameVersion.setStatus("current")
_Ieee8021XEapolLastRxFrameSource_Type = MacAddress
_Ieee8021XEapolLastRxFrameSource_Object = MibTableColumn
ieee8021XEapolLastRxFrameSource = _Ieee8021XEapolLastRxFrameSource_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 12),
    _Ieee8021XEapolLastRxFrameSource_Type()
)
ieee8021XEapolLastRxFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolLastRxFrameSource.setStatus("current")
_Ieee8021XEapolSuppEapFramesTx_Type = Counter32
_Ieee8021XEapolSuppEapFramesTx_Object = MibTableColumn
ieee8021XEapolSuppEapFramesTx = _Ieee8021XEapolSuppEapFramesTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 13),
    _Ieee8021XEapolSuppEapFramesTx_Type()
)
ieee8021XEapolSuppEapFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolSuppEapFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolSuppEapFramesTx.setUnits("Packets")
_Ieee8021XEapolLogoffFramesTx_Type = Counter32
_Ieee8021XEapolLogoffFramesTx_Object = MibTableColumn
ieee8021XEapolLogoffFramesTx = _Ieee8021XEapolLogoffFramesTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 14),
    _Ieee8021XEapolLogoffFramesTx_Type()
)
ieee8021XEapolLogoffFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolLogoffFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolLogoffFramesTx.setUnits("Packets")
_Ieee8021XEapolAnnouncementFramesTx_Type = Counter32
_Ieee8021XEapolAnnouncementFramesTx_Object = MibTableColumn
ieee8021XEapolAnnouncementFramesTx = _Ieee8021XEapolAnnouncementFramesTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 15),
    _Ieee8021XEapolAnnouncementFramesTx_Type()
)
ieee8021XEapolAnnouncementFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolAnnouncementFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolAnnouncementFramesTx.setUnits("Packets")
_Ieee8021XEapolAnnouncementReqFramesTx_Type = Counter32
_Ieee8021XEapolAnnouncementReqFramesTx_Object = MibTableColumn
ieee8021XEapolAnnouncementReqFramesTx = _Ieee8021XEapolAnnouncementReqFramesTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 16),
    _Ieee8021XEapolAnnouncementReqFramesTx_Type()
)
ieee8021XEapolAnnouncementReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolAnnouncementReqFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolAnnouncementReqFramesTx.setUnits("Packets")
_Ieee8021XEapolStartFramesTx_Type = Counter32
_Ieee8021XEapolStartFramesTx_Object = MibTableColumn
ieee8021XEapolStartFramesTx = _Ieee8021XEapolStartFramesTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 17),
    _Ieee8021XEapolStartFramesTx_Type()
)
ieee8021XEapolStartFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolStartFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolStartFramesTx.setUnits("Packets")
_Ieee8021XEapolAuthEapFramesTx_Type = Counter32
_Ieee8021XEapolAuthEapFramesTx_Object = MibTableColumn
ieee8021XEapolAuthEapFramesTx = _Ieee8021XEapolAuthEapFramesTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 18),
    _Ieee8021XEapolAuthEapFramesTx_Type()
)
ieee8021XEapolAuthEapFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolAuthEapFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolAuthEapFramesTx.setUnits("Packets")
_Ieee8021XEapolMkaFramesTx_Type = Counter32
_Ieee8021XEapolMkaFramesTx_Object = MibTableColumn
ieee8021XEapolMkaFramesTx = _Ieee8021XEapolMkaFramesTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 5, 1, 1, 19),
    _Ieee8021XEapolMkaFramesTx_Type()
)
ieee8021XEapolMkaFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XEapolMkaFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XEapolMkaFramesTx.setUnits("Packets")
_Ieee8021XPaeKaY_ObjectIdentity = ObjectIdentity
ieee8021XPaeKaY = _Ieee8021XPaeKaY_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6)
)
_Ieee8021XKayMkaTable_Object = MibTable
ieee8021XKayMkaTable = _Ieee8021XKayMkaTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ieee8021XKayMkaTable.setStatus("current")
_Ieee8021XKayMkaEntry_Object = MibTableRow
ieee8021XKayMkaEntry = _Ieee8021XKayMkaEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1)
)
ieee8021XKayMkaEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021XKayMkaEntry.setStatus("current")
_Ieee8021XKayMkaActive_Type = TruthValue
_Ieee8021XKayMkaActive_Object = MibTableColumn
ieee8021XKayMkaActive = _Ieee8021XKayMkaActive_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 1),
    _Ieee8021XKayMkaActive_Type()
)
ieee8021XKayMkaActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaActive.setStatus("current")
_Ieee8021XKayMkaAuthenticated_Type = TruthValue
_Ieee8021XKayMkaAuthenticated_Object = MibTableColumn
ieee8021XKayMkaAuthenticated = _Ieee8021XKayMkaAuthenticated_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 2),
    _Ieee8021XKayMkaAuthenticated_Type()
)
ieee8021XKayMkaAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaAuthenticated.setStatus("current")
_Ieee8021XKayMkaSecured_Type = TruthValue
_Ieee8021XKayMkaSecured_Object = MibTableColumn
ieee8021XKayMkaSecured = _Ieee8021XKayMkaSecured_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 3),
    _Ieee8021XKayMkaSecured_Type()
)
ieee8021XKayMkaSecured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaSecured.setStatus("current")
_Ieee8021XKayMkaFailed_Type = TruthValue
_Ieee8021XKayMkaFailed_Object = MibTableColumn
ieee8021XKayMkaFailed = _Ieee8021XKayMkaFailed_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 4),
    _Ieee8021XKayMkaFailed_Type()
)
ieee8021XKayMkaFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaFailed.setStatus("current")
_Ieee8021XKayMkaActorSCI_Type = SecySCI
_Ieee8021XKayMkaActorSCI_Object = MibTableColumn
ieee8021XKayMkaActorSCI = _Ieee8021XKayMkaActorSCI_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 5),
    _Ieee8021XKayMkaActorSCI_Type()
)
ieee8021XKayMkaActorSCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaActorSCI.setStatus("current")
_Ieee8021XKayMkaActorsPriority_Type = Ieee8021XMkaKeyServerPriority
_Ieee8021XKayMkaActorsPriority_Object = MibTableColumn
ieee8021XKayMkaActorsPriority = _Ieee8021XKayMkaActorsPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 6),
    _Ieee8021XKayMkaActorsPriority_Type()
)
ieee8021XKayMkaActorsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XKayMkaActorsPriority.setStatus("current")
_Ieee8021XKayMkaKeyServerPriority_Type = Ieee8021XMkaKeyServerPriority
_Ieee8021XKayMkaKeyServerPriority_Object = MibTableColumn
ieee8021XKayMkaKeyServerPriority = _Ieee8021XKayMkaKeyServerPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 7),
    _Ieee8021XKayMkaKeyServerPriority_Type()
)
ieee8021XKayMkaKeyServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaKeyServerPriority.setStatus("current")
_Ieee8021XKayMkaKeyServerSCI_Type = SecySCI
_Ieee8021XKayMkaKeyServerSCI_Object = MibTableColumn
ieee8021XKayMkaKeyServerSCI = _Ieee8021XKayMkaKeyServerSCI_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 8),
    _Ieee8021XKayMkaKeyServerSCI_Type()
)
ieee8021XKayMkaKeyServerSCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaKeyServerSCI.setStatus("current")
_Ieee8021XKayAllowedJoinGroup_Type = TruthValue
_Ieee8021XKayAllowedJoinGroup_Object = MibTableColumn
ieee8021XKayAllowedJoinGroup = _Ieee8021XKayAllowedJoinGroup_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 9),
    _Ieee8021XKayAllowedJoinGroup_Type()
)
ieee8021XKayAllowedJoinGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayAllowedJoinGroup.setStatus("current")
_Ieee8021XKayAllowedFormGroup_Type = TruthValue
_Ieee8021XKayAllowedFormGroup_Object = MibTableColumn
ieee8021XKayAllowedFormGroup = _Ieee8021XKayAllowedFormGroup_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 10),
    _Ieee8021XKayAllowedFormGroup_Type()
)
ieee8021XKayAllowedFormGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayAllowedFormGroup.setStatus("current")
_Ieee8021XKayCreateNewGroup_Type = TruthValue
_Ieee8021XKayCreateNewGroup_Object = MibTableColumn
ieee8021XKayCreateNewGroup = _Ieee8021XKayCreateNewGroup_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 11),
    _Ieee8021XKayCreateNewGroup_Type()
)
ieee8021XKayCreateNewGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XKayCreateNewGroup.setStatus("current")


class _Ieee8021XKayMacSecCapability_Type(Integer32):
    """Custom type ieee8021XKayMacSecCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macSecCapability1", 1),
          ("macSecCapability2", 2),
          ("macSecCapability3", 3),
          ("noMACsec", 0))
    )


_Ieee8021XKayMacSecCapability_Type.__name__ = "Integer32"
_Ieee8021XKayMacSecCapability_Object = MibTableColumn
ieee8021XKayMacSecCapability = _Ieee8021XKayMacSecCapability_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 12),
    _Ieee8021XKayMacSecCapability_Type()
)
ieee8021XKayMacSecCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMacSecCapability.setStatus("current")
_Ieee8021XKayMacSecDesired_Type = TruthValue
_Ieee8021XKayMacSecDesired_Object = MibTableColumn
ieee8021XKayMacSecDesired = _Ieee8021XKayMacSecDesired_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 13),
    _Ieee8021XKayMacSecDesired_Type()
)
ieee8021XKayMacSecDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XKayMacSecDesired.setStatus("current")
_Ieee8021XKayMacSecProtect_Type = TruthValue
_Ieee8021XKayMacSecProtect_Object = MibTableColumn
ieee8021XKayMacSecProtect = _Ieee8021XKayMacSecProtect_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 14),
    _Ieee8021XKayMacSecProtect_Type()
)
ieee8021XKayMacSecProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMacSecProtect.setStatus("current")
_Ieee8021XKayMacSecReplayProtect_Type = TruthValue
_Ieee8021XKayMacSecReplayProtect_Object = MibTableColumn
ieee8021XKayMacSecReplayProtect = _Ieee8021XKayMacSecReplayProtect_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 15),
    _Ieee8021XKayMacSecReplayProtect_Type()
)
ieee8021XKayMacSecReplayProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMacSecReplayProtect.setStatus("current")
_Ieee8021XKayMacSecValidate_Type = TruthValue
_Ieee8021XKayMacSecValidate_Object = MibTableColumn
ieee8021XKayMacSecValidate = _Ieee8021XKayMacSecValidate_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 16),
    _Ieee8021XKayMacSecValidate_Type()
)
ieee8021XKayMacSecValidate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMacSecValidate.setStatus("current")


class _Ieee8021XKayMacSecConfidentialityOffset_Type(Integer32):
    """Custom type ieee8021XKayMacSecConfidentialityOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(50, 50),
    )


_Ieee8021XKayMacSecConfidentialityOffset_Type.__name__ = "Integer32"
_Ieee8021XKayMacSecConfidentialityOffset_Object = MibTableColumn
ieee8021XKayMacSecConfidentialityOffset = _Ieee8021XKayMacSecConfidentialityOffset_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 17),
    _Ieee8021XKayMacSecConfidentialityOffset_Type()
)
ieee8021XKayMacSecConfidentialityOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XKayMacSecConfidentialityOffset.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021XKayMacSecConfidentialityOffset.setUnits("bytes")
_Ieee8021XKayMkaTxKN_Type = Ieee8021XMkaKN
_Ieee8021XKayMkaTxKN_Object = MibTableColumn
ieee8021XKayMkaTxKN = _Ieee8021XKayMkaTxKN_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 18),
    _Ieee8021XKayMkaTxKN_Type()
)
ieee8021XKayMkaTxKN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaTxKN.setStatus("current")
_Ieee8021XKayMkaTxAN_Type = RowPointer
_Ieee8021XKayMkaTxAN_Object = MibTableColumn
ieee8021XKayMkaTxAN = _Ieee8021XKayMkaTxAN_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 19),
    _Ieee8021XKayMkaTxAN_Type()
)
ieee8021XKayMkaTxAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaTxAN.setStatus("current")
_Ieee8021XKayMkaRxKN_Type = Ieee8021XMkaKN
_Ieee8021XKayMkaRxKN_Object = MibTableColumn
ieee8021XKayMkaRxKN = _Ieee8021XKayMkaRxKN_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 20),
    _Ieee8021XKayMkaRxKN_Type()
)
ieee8021XKayMkaRxKN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaRxKN.setStatus("current")
_Ieee8021XKayMkaRxAN_Type = RowPointer
_Ieee8021XKayMkaRxAN_Object = MibTableColumn
ieee8021XKayMkaRxAN = _Ieee8021XKayMkaRxAN_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 21),
    _Ieee8021XKayMkaRxAN_Type()
)
ieee8021XKayMkaRxAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaRxAN.setStatus("current")


class _Ieee8021XKayMkaSuspendFor_Type(Integer32):
    """Custom type ieee8021XKayMkaSuspendFor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Ieee8021XKayMkaSuspendFor_Type.__name__ = "Integer32"
_Ieee8021XKayMkaSuspendFor_Object = MibTableColumn
ieee8021XKayMkaSuspendFor = _Ieee8021XKayMkaSuspendFor_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 22),
    _Ieee8021XKayMkaSuspendFor_Type()
)
ieee8021XKayMkaSuspendFor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XKayMkaSuspendFor.setStatus("current")
_Ieee8021XKayMkaSuspendOnRequest_Type = TruthValue
_Ieee8021XKayMkaSuspendOnRequest_Object = MibTableColumn
ieee8021XKayMkaSuspendOnRequest = _Ieee8021XKayMkaSuspendOnRequest_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 23),
    _Ieee8021XKayMkaSuspendOnRequest_Type()
)
ieee8021XKayMkaSuspendOnRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XKayMkaSuspendOnRequest.setStatus("current")


class _Ieee8021XKayMkaSuspendedWhile_Type(Integer32):
    """Custom type ieee8021XKayMkaSuspendedWhile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_Ieee8021XKayMkaSuspendedWhile_Type.__name__ = "Integer32"
_Ieee8021XKayMkaSuspendedWhile_Object = MibTableColumn
ieee8021XKayMkaSuspendedWhile = _Ieee8021XKayMkaSuspendedWhile_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 1, 1, 24),
    _Ieee8021XKayMkaSuspendedWhile_Type()
)
ieee8021XKayMkaSuspendedWhile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XKayMkaSuspendedWhile.setStatus("current")
_Ieee8021XKayMkaParticipantTable_Object = MibTable
ieee8021XKayMkaParticipantTable = _Ieee8021XKayMkaParticipantTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ieee8021XKayMkaParticipantTable.setStatus("current")
_Ieee8021XKayMkaParticipantEntry_Object = MibTableRow
ieee8021XKayMkaParticipantEntry = _Ieee8021XKayMkaParticipantEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1)
)
ieee8021XKayMkaParticipantEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
    (0, "IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartCKN"),
)
if mibBuilder.loadTexts:
    ieee8021XKayMkaParticipantEntry.setStatus("current")
_Ieee8021XKayMkaPartCKN_Type = Ieee8021XPaeCKN
_Ieee8021XKayMkaPartCKN_Object = MibTableColumn
ieee8021XKayMkaPartCKN = _Ieee8021XKayMkaPartCKN_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1, 1),
    _Ieee8021XKayMkaPartCKN_Type()
)
ieee8021XKayMkaPartCKN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPartCKN.setStatus("current")
_Ieee8021XKayMkaPartKMD_Type = Ieee8021XPaeKMD
_Ieee8021XKayMkaPartKMD_Object = MibTableColumn
ieee8021XKayMkaPartKMD = _Ieee8021XKayMkaPartKMD_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1, 2),
    _Ieee8021XKayMkaPartKMD_Type()
)
ieee8021XKayMkaPartKMD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPartKMD.setStatus("current")
_Ieee8021XKayMkaPartNID_Type = Ieee8021XPaeNID
_Ieee8021XKayMkaPartNID_Object = MibTableColumn
ieee8021XKayMkaPartNID = _Ieee8021XKayMkaPartNID_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1, 3),
    _Ieee8021XKayMkaPartNID_Type()
)
ieee8021XKayMkaPartNID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPartNID.setStatus("current")
_Ieee8021XKayMkaPartCached_Type = TruthValue
_Ieee8021XKayMkaPartCached_Object = MibTableColumn
ieee8021XKayMkaPartCached = _Ieee8021XKayMkaPartCached_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1, 4),
    _Ieee8021XKayMkaPartCached_Type()
)
ieee8021XKayMkaPartCached.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPartCached.setStatus("current")


class _Ieee8021XKayMkaPartActive_Type(TruthValue):
    """Custom type ieee8021XKayMkaPartActive based on TruthValue"""


_Ieee8021XKayMkaPartActive_Object = MibTableColumn
ieee8021XKayMkaPartActive = _Ieee8021XKayMkaPartActive_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1, 5),
    _Ieee8021XKayMkaPartActive_Type()
)
ieee8021XKayMkaPartActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPartActive.setStatus("current")
_Ieee8021XKayMkaPartRetain_Type = TruthValue
_Ieee8021XKayMkaPartRetain_Object = MibTableColumn
ieee8021XKayMkaPartRetain = _Ieee8021XKayMkaPartRetain_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1, 6),
    _Ieee8021XKayMkaPartRetain_Type()
)
ieee8021XKayMkaPartRetain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPartRetain.setStatus("current")


class _Ieee8021XKayMkaPartActivateControl_Type(Integer32):
    """Custom type ieee8021XKayMkaPartActivateControl based on Integer32"""
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
        *(("always", 4),
          ("default", 1),
          ("disabled", 2),
          ("onOperUp", 3))
    )


_Ieee8021XKayMkaPartActivateControl_Type.__name__ = "Integer32"
_Ieee8021XKayMkaPartActivateControl_Object = MibTableColumn
ieee8021XKayMkaPartActivateControl = _Ieee8021XKayMkaPartActivateControl_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1, 7),
    _Ieee8021XKayMkaPartActivateControl_Type()
)
ieee8021XKayMkaPartActivateControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPartActivateControl.setStatus("current")


class _Ieee8021XKayMkaPartPrincipal_Type(TruthValue):
    """Custom type ieee8021XKayMkaPartPrincipal based on TruthValue"""


_Ieee8021XKayMkaPartPrincipal_Object = MibTableColumn
ieee8021XKayMkaPartPrincipal = _Ieee8021XKayMkaPartPrincipal_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1, 8),
    _Ieee8021XKayMkaPartPrincipal_Type()
)
ieee8021XKayMkaPartPrincipal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPartPrincipal.setStatus("current")
_Ieee8021XKayMkaPartDistCKN_Type = Ieee8021XPaeCKNOrNull
_Ieee8021XKayMkaPartDistCKN_Object = MibTableColumn
ieee8021XKayMkaPartDistCKN = _Ieee8021XKayMkaPartDistCKN_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1, 9),
    _Ieee8021XKayMkaPartDistCKN_Type()
)
ieee8021XKayMkaPartDistCKN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPartDistCKN.setStatus("current")
_Ieee8021XKayMkaPartRowStatus_Type = RowStatus
_Ieee8021XKayMkaPartRowStatus_Object = MibTableColumn
ieee8021XKayMkaPartRowStatus = _Ieee8021XKayMkaPartRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 2, 1, 10),
    _Ieee8021XKayMkaPartRowStatus_Type()
)
ieee8021XKayMkaPartRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPartRowStatus.setStatus("current")
_Ieee8021XKayMkaPeerListTable_Object = MibTable
ieee8021XKayMkaPeerListTable = _Ieee8021XKayMkaPeerListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 3)
)
if mibBuilder.loadTexts:
    ieee8021XKayMkaPeerListTable.setStatus("current")
_Ieee8021XKayMkaPeerListEntry_Object = MibTableRow
ieee8021XKayMkaPeerListEntry = _Ieee8021XKayMkaPeerListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 3, 1)
)
ieee8021XKayMkaPeerListEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
    (0, "IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartCKN"),
    (0, "IEEE8021X-PAE-MIB", "ieee8021XKayMkaPeerListMI"),
)
if mibBuilder.loadTexts:
    ieee8021XKayMkaPeerListEntry.setStatus("current")
_Ieee8021XKayMkaPeerListMI_Type = Ieee8021XMkaMI
_Ieee8021XKayMkaPeerListMI_Object = MibTableColumn
ieee8021XKayMkaPeerListMI = _Ieee8021XKayMkaPeerListMI_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 3, 1, 1),
    _Ieee8021XKayMkaPeerListMI_Type()
)
ieee8021XKayMkaPeerListMI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPeerListMI.setStatus("current")
_Ieee8021XKayMkaPeerListMN_Type = Ieee8021XMkaMN
_Ieee8021XKayMkaPeerListMN_Object = MibTableColumn
ieee8021XKayMkaPeerListMN = _Ieee8021XKayMkaPeerListMN_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 3, 1, 2),
    _Ieee8021XKayMkaPeerListMN_Type()
)
ieee8021XKayMkaPeerListMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPeerListMN.setStatus("current")


class _Ieee8021XKayMkaPeerListType_Type(Integer32):
    """Custom type ieee8021XKayMkaPeerListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("livePeerList", 1),
          ("potentialPeerList", 2))
    )


_Ieee8021XKayMkaPeerListType_Type.__name__ = "Integer32"
_Ieee8021XKayMkaPeerListType_Object = MibTableColumn
ieee8021XKayMkaPeerListType = _Ieee8021XKayMkaPeerListType_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 3, 1, 3),
    _Ieee8021XKayMkaPeerListType_Type()
)
ieee8021XKayMkaPeerListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPeerListType.setStatus("current")
_Ieee8021XKayMkaPeerListSCI_Type = SecySCI
_Ieee8021XKayMkaPeerListSCI_Object = MibTableColumn
ieee8021XKayMkaPeerListSCI = _Ieee8021XKayMkaPeerListSCI_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 6, 3, 1, 4),
    _Ieee8021XKayMkaPeerListSCI_Type()
)
ieee8021XKayMkaPeerListSCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XKayMkaPeerListSCI.setStatus("current")
_Ieee8021XPaeNetworkIdentifier_ObjectIdentity = ObjectIdentity
ieee8021XPaeNetworkIdentifier = _Ieee8021XPaeNetworkIdentifier_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7)
)
_Ieee8021XNidConfigTable_Object = MibTable
ieee8021XNidConfigTable = _Ieee8021XNidConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ieee8021XNidConfigTable.setStatus("current")
_Ieee8021XNidConfigEntry_Object = MibTableRow
ieee8021XNidConfigEntry = _Ieee8021XNidConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 1, 1)
)
ieee8021XNidConfigEntry.setIndexNames(
    (1, "IEEE8021X-PAE-MIB", "ieee8021XNidNID"),
)
if mibBuilder.loadTexts:
    ieee8021XNidConfigEntry.setStatus("current")
_Ieee8021XNidNID_Type = Ieee8021XPaeNID
_Ieee8021XNidNID_Object = MibTableColumn
ieee8021XNidNID = _Ieee8021XNidNID_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 1, 1, 1),
    _Ieee8021XNidNID_Type()
)
ieee8021XNidNID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021XNidNID.setStatus("current")


class _Ieee8021XNidUseEap_Type(Integer32):
    """Custom type ieee8021XNidUseEap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 2),
          ("mkaFail", 3),
          ("never", 1))
    )


_Ieee8021XNidUseEap_Type.__name__ = "Integer32"
_Ieee8021XNidUseEap_Object = MibTableColumn
ieee8021XNidUseEap = _Ieee8021XNidUseEap_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 1, 1, 2),
    _Ieee8021XNidUseEap_Type()
)
ieee8021XNidUseEap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XNidUseEap.setStatus("current")


class _Ieee8021XNidUnauthAllowed_Type(Integer32):
    """Custom type ieee8021XNidUnauthAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authFail", 3),
          ("immediate", 2),
          ("never", 1))
    )


_Ieee8021XNidUnauthAllowed_Type.__name__ = "Integer32"
_Ieee8021XNidUnauthAllowed_Object = MibTableColumn
ieee8021XNidUnauthAllowed = _Ieee8021XNidUnauthAllowed_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 1, 1, 3),
    _Ieee8021XNidUnauthAllowed_Type()
)
ieee8021XNidUnauthAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XNidUnauthAllowed.setStatus("current")


class _Ieee8021XNidUnsecuredAllowed_Type(Integer32):
    """Custom type ieee8021XNidUnsecuredAllowed based on Integer32"""
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
        *(("immediate", 2),
          ("mkaFail", 3),
          ("mkaServer", 4),
          ("never", 1))
    )


_Ieee8021XNidUnsecuredAllowed_Type.__name__ = "Integer32"
_Ieee8021XNidUnsecuredAllowed_Object = MibTableColumn
ieee8021XNidUnsecuredAllowed = _Ieee8021XNidUnsecuredAllowed_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 1, 1, 4),
    _Ieee8021XNidUnsecuredAllowed_Type()
)
ieee8021XNidUnsecuredAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XNidUnsecuredAllowed.setStatus("current")
_Ieee8021XNidUnauthenticatedAccess_Type = Ieee8021XPaeNIDUnauthenticatedStatus
_Ieee8021XNidUnauthenticatedAccess_Object = MibTableColumn
ieee8021XNidUnauthenticatedAccess = _Ieee8021XNidUnauthenticatedAccess_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 1, 1, 5),
    _Ieee8021XNidUnauthenticatedAccess_Type()
)
ieee8021XNidUnauthenticatedAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XNidUnauthenticatedAccess.setStatus("current")
_Ieee8021XNidAccessCapabilities_Type = Ieee8021XPaeNIDCapabilites
_Ieee8021XNidAccessCapabilities_Object = MibTableColumn
ieee8021XNidAccessCapabilities = _Ieee8021XNidAccessCapabilities_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 1, 1, 6),
    _Ieee8021XNidAccessCapabilities_Type()
)
ieee8021XNidAccessCapabilities.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XNidAccessCapabilities.setStatus("current")
_Ieee8021XNidKMD_Type = Ieee8021XPaeKMD
_Ieee8021XNidKMD_Object = MibTableColumn
ieee8021XNidKMD = _Ieee8021XNidKMD_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 1, 1, 7),
    _Ieee8021XNidKMD_Type()
)
ieee8021XNidKMD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XNidKMD.setStatus("current")
_Ieee8021XNidRowStatus_Type = RowStatus
_Ieee8021XNidRowStatus_Object = MibTableColumn
ieee8021XNidRowStatus = _Ieee8021XNidRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 1, 1, 8),
    _Ieee8021XNidRowStatus_Type()
)
ieee8021XNidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021XNidRowStatus.setStatus("current")
_Ieee8021XAnnounceTable_Object = MibTable
ieee8021XAnnounceTable = _Ieee8021XAnnounceTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ieee8021XAnnounceTable.setStatus("current")
_Ieee8021XAnnounceEntry_Object = MibTableRow
ieee8021XAnnounceEntry = _Ieee8021XAnnounceEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 2, 1)
)
ieee8021XAnnounceEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
    (1, "IEEE8021X-PAE-MIB", "ieee8021XAnnounceNID"),
)
if mibBuilder.loadTexts:
    ieee8021XAnnounceEntry.setStatus("current")
_Ieee8021XAnnounceNID_Type = Ieee8021XPaeNID
_Ieee8021XAnnounceNID_Object = MibTableColumn
ieee8021XAnnounceNID = _Ieee8021XAnnounceNID_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 2, 1, 1),
    _Ieee8021XAnnounceNID_Type()
)
ieee8021XAnnounceNID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021XAnnounceNID.setStatus("current")
_Ieee8021XAnnounceAccessStatus_Type = Ieee8021XPaeNIDAccessStatus
_Ieee8021XAnnounceAccessStatus_Object = MibTableColumn
ieee8021XAnnounceAccessStatus = _Ieee8021XAnnounceAccessStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 2, 1, 2),
    _Ieee8021XAnnounceAccessStatus_Type()
)
ieee8021XAnnounceAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAnnounceAccessStatus.setStatus("current")
_Ieee8021XAnnouncementTable_Object = MibTable
ieee8021XAnnouncementTable = _Ieee8021XAnnouncementTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 3)
)
if mibBuilder.loadTexts:
    ieee8021XAnnouncementTable.setStatus("current")
_Ieee8021XAnnouncementEntry_Object = MibTableRow
ieee8021XAnnouncementEntry = _Ieee8021XAnnouncementEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 3, 1)
)
ieee8021XAnnouncementEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
    (1, "IEEE8021X-PAE-MIB", "ieee8021XAnnouncementNID"),
)
if mibBuilder.loadTexts:
    ieee8021XAnnouncementEntry.setStatus("current")
_Ieee8021XAnnouncementNID_Type = Ieee8021XPaeNID
_Ieee8021XAnnouncementNID_Object = MibTableColumn
ieee8021XAnnouncementNID = _Ieee8021XAnnouncementNID_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 3, 1, 1),
    _Ieee8021XAnnouncementNID_Type()
)
ieee8021XAnnouncementNID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021XAnnouncementNID.setStatus("current")
_Ieee8021XAnnouncementKMD_Type = Ieee8021XPaeKMD
_Ieee8021XAnnouncementKMD_Object = MibTableColumn
ieee8021XAnnouncementKMD = _Ieee8021XAnnouncementKMD_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 3, 1, 2),
    _Ieee8021XAnnouncementKMD_Type()
)
ieee8021XAnnouncementKMD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAnnouncementKMD.setStatus("current")
_Ieee8021XAnnouncementSpecific_Type = TruthValue
_Ieee8021XAnnouncementSpecific_Object = MibTableColumn
ieee8021XAnnouncementSpecific = _Ieee8021XAnnouncementSpecific_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 3, 1, 3),
    _Ieee8021XAnnouncementSpecific_Type()
)
ieee8021XAnnouncementSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAnnouncementSpecific.setStatus("current")
_Ieee8021XAnnouncementAccessStatus_Type = Ieee8021XPaeNIDAccessStatus
_Ieee8021XAnnouncementAccessStatus_Object = MibTableColumn
ieee8021XAnnouncementAccessStatus = _Ieee8021XAnnouncementAccessStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 3, 1, 4),
    _Ieee8021XAnnouncementAccessStatus_Type()
)
ieee8021XAnnouncementAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAnnouncementAccessStatus.setStatus("current")
_Ieee8021XAnnouncementAccessRequested_Type = TruthValue
_Ieee8021XAnnouncementAccessRequested_Object = MibTableColumn
ieee8021XAnnouncementAccessRequested = _Ieee8021XAnnouncementAccessRequested_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 3, 1, 5),
    _Ieee8021XAnnouncementAccessRequested_Type()
)
ieee8021XAnnouncementAccessRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAnnouncementAccessRequested.setStatus("current")
_Ieee8021XAnnouncementUnauthAccess_Type = Ieee8021XPaeNIDUnauthenticatedStatus
_Ieee8021XAnnouncementUnauthAccess_Object = MibTableColumn
ieee8021XAnnouncementUnauthAccess = _Ieee8021XAnnouncementUnauthAccess_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 3, 1, 6),
    _Ieee8021XAnnouncementUnauthAccess_Type()
)
ieee8021XAnnouncementUnauthAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAnnouncementUnauthAccess.setStatus("current")
_Ieee8021XAnnouncementCapabilities_Type = Ieee8021XPaeNIDCapabilites
_Ieee8021XAnnouncementCapabilities_Object = MibTableColumn
ieee8021XAnnouncementCapabilities = _Ieee8021XAnnouncementCapabilities_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 3, 1, 7),
    _Ieee8021XAnnouncementCapabilities_Type()
)
ieee8021XAnnouncementCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAnnouncementCapabilities.setStatus("current")
_Ieee8021XAnnouncementCipherSuitesTable_Object = MibTable
ieee8021XAnnouncementCipherSuitesTable = _Ieee8021XAnnouncementCipherSuitesTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 4)
)
if mibBuilder.loadTexts:
    ieee8021XAnnouncementCipherSuitesTable.setStatus("current")
_Ieee8021XAnnouncementCipherSuitesEntry_Object = MibTableRow
ieee8021XAnnouncementCipherSuitesEntry = _Ieee8021XAnnouncementCipherSuitesEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 4, 1)
)
ieee8021XAnnouncementCipherSuitesEntry.setIndexNames(
    (0, "IEEE8021X-PAE-MIB", "ieee8021XPaePortNumber"),
    (0, "IEEE8021X-PAE-MIB", "ieee8021XAnnouncementNID"),
    (0, "IEEE8021X-PAE-MIB", "ieee8021XAnnouncementCipherSuite"),
)
if mibBuilder.loadTexts:
    ieee8021XAnnouncementCipherSuitesEntry.setStatus("current")


class _Ieee8021XAnnouncementCipherSuite_Type(OctetString):
    """Custom type ieee8021XAnnouncementCipherSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ieee8021XAnnouncementCipherSuite_Type.__name__ = "OctetString"
_Ieee8021XAnnouncementCipherSuite_Object = MibTableColumn
ieee8021XAnnouncementCipherSuite = _Ieee8021XAnnouncementCipherSuite_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 4, 1, 1),
    _Ieee8021XAnnouncementCipherSuite_Type()
)
ieee8021XAnnouncementCipherSuite.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021XAnnouncementCipherSuite.setStatus("current")


class _Ieee8021XAnnouncementCipherCapability_Type(Unsigned32):
    """Custom type ieee8021XAnnouncementCipherCapability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021XAnnouncementCipherCapability_Type.__name__ = "Unsigned32"
_Ieee8021XAnnouncementCipherCapability_Object = MibTableColumn
ieee8021XAnnouncementCipherCapability = _Ieee8021XAnnouncementCipherCapability_Object(
    (1, 3, 111, 2, 802, 1, 1, 15, 1, 7, 4, 1, 2),
    _Ieee8021XAnnouncementCipherCapability_Type()
)
ieee8021XAnnouncementCipherCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021XAnnouncementCipherCapability.setStatus("current")
_Ieee8021XPaeMIBConformance_ObjectIdentity = ObjectIdentity
ieee8021XPaeMIBConformance = _Ieee8021XPaeMIBConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 2)
)
_Ieee8021XPaeCompliances_ObjectIdentity = ObjectIdentity
ieee8021XPaeCompliances = _Ieee8021XPaeCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 1)
)
_Ieee8021XPaeGroups_ObjectIdentity = ObjectIdentity
ieee8021XPaeGroups = _Ieee8021XPaeGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2)
)

# Managed Objects groups

ieee8021XPaeSystemGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 1)
)
ieee8021XPaeSystemGroup.setObjects(
      *(("IEEE8021X-PAE-MIB", "ieee8021XPaeSysAccessControl"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaeSysAnnouncements"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaeSysEapolVersion"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaeSysMkaVersion"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortType"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaeControlledPortNumber"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaeUncontrolledPortNumber"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaeCommonPortNumber"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortInitialize"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortCapabilities"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortVirtualPortsEnable"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortMaxVirtualPorts"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortCurrentVirtualPorts"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortVirtualPortStart"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortVirtualPortPeerMAC"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortLogonEnable"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortAuthenticatorEnable"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortSupplicantEnable"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortKayMkaEnable"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortAnnouncerEnable"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortListenerEnable"))
)
if mibBuilder.loadTexts:
    ieee8021XPaeSystemGroup.setStatus("current")

ieee8021XPacGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 2)
)
ieee8021XPacGroup.setObjects(
      *(("IEEE8021X-PAE-MIB", "ieee8021XPacPortAdminPt2PtMAC"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPacPortOperPt2PtMAC"))
)
if mibBuilder.loadTexts:
    ieee8021XPacGroup.setStatus("current")

ieee8021XPaeLogonGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 3)
)
ieee8021XPaeLogonGroup.setObjects(
      *(("IEEE8021X-PAE-MIB", "ieee8021XPaePortLogonConnectStatus"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortPortValid"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortSessionOctetsRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortSessionOctetsTx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortSessionPktsRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortSessionPktsTx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortSessionId"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortSessionStartTime"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortSessionIntervalTime"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortSessionTerminate"),
        ("IEEE8021X-PAE-MIB", "ieee8021XPaePortSessionUserName"))
)
if mibBuilder.loadTexts:
    ieee8021XPaeLogonGroup.setStatus("current")

ieee8021XPaeAuthConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 4)
)
ieee8021XPaeAuthConfigGroup.setObjects(
      *(("IEEE8021X-PAE-MIB", "ieee8021XAuthPaeAuthenticate"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAuthPaeAuthenticated"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAuthPaeFailed"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAuthPaeReAuthEnabled"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAuthPaeQuietPeriod"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAuthPaeReauthPeriod"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAuthPaeRetryMax"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAuthPaeRetryCount"))
)
if mibBuilder.loadTexts:
    ieee8021XPaeAuthConfigGroup.setStatus("current")

ieee8021XPaeSuppConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 5)
)
ieee8021XPaeSuppConfigGroup.setObjects(
      *(("IEEE8021X-PAE-MIB", "ieee8021XSuppPaeAuthenticate"),
        ("IEEE8021X-PAE-MIB", "ieee8021XSuppPaeAuthenticated"),
        ("IEEE8021X-PAE-MIB", "ieee8021XSuppPaeFailed"),
        ("IEEE8021X-PAE-MIB", "ieee8021XSuppPaeHelloPeriod"),
        ("IEEE8021X-PAE-MIB", "ieee8021XSuppPaeRetryMax"),
        ("IEEE8021X-PAE-MIB", "ieee8021XSuppPaeRetryCount"))
)
if mibBuilder.loadTexts:
    ieee8021XPaeSuppConfigGroup.setStatus("current")

ieee8021XPaeEapolStatsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 6)
)
ieee8021XPaeEapolStatsGroup.setObjects(
      *(("IEEE8021X-PAE-MIB", "ieee8021XEapolInvalidFramesRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolEapLengthErrorFramesRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolAnnouncementFramesRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolAnnouncementReqFramesRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolPortUnavailableFramesRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolStartFramesRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolEapFramesRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolLogoffFramesRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolMkNoCknFramesRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolMkInvalidFramesRx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolLastRxFrameVersion"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolLastRxFrameSource"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolSuppEapFramesTx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolLogoffFramesTx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolAnnouncementFramesTx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolAnnouncementReqFramesTx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolStartFramesTx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolAuthEapFramesTx"),
        ("IEEE8021X-PAE-MIB", "ieee8021XEapolMkaFramesTx"))
)
if mibBuilder.loadTexts:
    ieee8021XPaeEapolStatsGroup.setStatus("current")

ieee8021XPaeKaYMkaGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 7)
)
ieee8021XPaeKaYMkaGroup.setObjects(
      *(("IEEE8021X-PAE-MIB", "ieee8021XKayMkaActive"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaAuthenticated"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaSecured"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaFailed"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaActorSCI"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaActorsPriority"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaKeyServerPriority"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaKeyServerSCI"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayAllowedJoinGroup"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayAllowedFormGroup"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayCreateNewGroup"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMacSecCapability"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMacSecDesired"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMacSecProtect"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMacSecReplayProtect"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMacSecValidate"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMacSecConfidentialityOffset"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaTxKN"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaTxAN"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaRxKN"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaRxAN"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartKMD"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartNID"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartCached"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartActive"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartRetain"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartActivateControl"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartPrincipal"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartDistCKN"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPartRowStatus"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPeerListMN"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPeerListType"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaPeerListSCI"))
)
if mibBuilder.loadTexts:
    ieee8021XPaeKaYMkaGroup.setStatus("current")

ieee8021XPaeNetworkIdentifierGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 8)
)
ieee8021XPaeNetworkIdentifierGroup.setObjects(
      *(("IEEE8021X-PAE-MIB", "ieee8021XLogonNIDConnectedNID"),
        ("IEEE8021X-PAE-MIB", "ieee8021XLogonNIDRequestedNID"),
        ("IEEE8021X-PAE-MIB", "ieee8021XLogonNIDSelectedNID"),
        ("IEEE8021X-PAE-MIB", "ieee8021XNidUseEap"),
        ("IEEE8021X-PAE-MIB", "ieee8021XNidUnauthAllowed"),
        ("IEEE8021X-PAE-MIB", "ieee8021XNidUnsecuredAllowed"),
        ("IEEE8021X-PAE-MIB", "ieee8021XNidUnauthenticatedAccess"),
        ("IEEE8021X-PAE-MIB", "ieee8021XNidAccessCapabilities"),
        ("IEEE8021X-PAE-MIB", "ieee8021XNidKMD"),
        ("IEEE8021X-PAE-MIB", "ieee8021XNidRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021XPaeNetworkIdentifierGroup.setStatus("current")

ieee8021XPaeAnnouncerGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 9)
)
ieee8021XPaeAnnouncerGroup.setObjects(
    ("IEEE8021X-PAE-MIB", "ieee8021XAnnounceAccessStatus")
)
if mibBuilder.loadTexts:
    ieee8021XPaeAnnouncerGroup.setStatus("current")

ieee8021XPaeListenerGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 10)
)
ieee8021XPaeListenerGroup.setObjects(
      *(("IEEE8021X-PAE-MIB", "ieee8021XAnnouncementKMD"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAnnouncementSpecific"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAnnouncementAccessStatus"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAnnouncementAccessRequested"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAnnouncementUnauthAccess"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAnnouncementCapabilities"),
        ("IEEE8021X-PAE-MIB", "ieee8021XAnnouncementCipherCapability"))
)
if mibBuilder.loadTexts:
    ieee8021XPaeListenerGroup.setStatus("current")

ieee8021XPaeKaYIsupgradeGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 11)
)
ieee8021XPaeKaYIsupgradeGroup.setObjects(
      *(("IEEE8021X-PAE-MIB", "ieee8021XKayMkaSuspendFor"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaSuspendOnRequest"),
        ("IEEE8021X-PAE-MIB", "ieee8021XKayMkaSuspendedWhile"))
)
if mibBuilder.loadTexts:
    ieee8021XPaeKaYIsupgradeGroup.setStatus("current")

ieee8021XPaeSystemAddGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 2, 12)
)
ieee8021XPaeSystemAddGroup.setObjects(
    ("IEEE8021X-PAE-MIB", "ieee8021XPaeEapolGroupMAC")
)
if mibBuilder.loadTexts:
    ieee8021XPaeSystemAddGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021XPaeCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021XPaeCompliance.setStatus(
        "current"
    )

ieee8021XPaeV2Compliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 15, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021XPaeV2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021X-PAE-MIB",
    **{"Ieee8021XPaeCKN": Ieee8021XPaeCKN,
       "Ieee8021XPaeCKNOrNull": Ieee8021XPaeCKNOrNull,
       "Ieee8021XPaeKMD": Ieee8021XPaeKMD,
       "Ieee8021XPaeNID": Ieee8021XPaeNID,
       "Ieee8021XPaeNIDOrNull": Ieee8021XPaeNIDOrNull,
       "Ieee8021XMkaKeyServerPriority": Ieee8021XMkaKeyServerPriority,
       "Ieee8021XMkaMI": Ieee8021XMkaMI,
       "Ieee8021XMkaMN": Ieee8021XMkaMN,
       "Ieee8021XMkaKN": Ieee8021XMkaKN,
       "Ieee8021XPaeNIDCapabilites": Ieee8021XPaeNIDCapabilites,
       "Ieee8021XPaeNIDAccessStatus": Ieee8021XPaeNIDAccessStatus,
       "Ieee8021XPaeNIDUnauthenticatedStatus": Ieee8021XPaeNIDUnauthenticatedStatus,
       "ieee8021XPaeMIB": ieee8021XPaeMIB,
       "ieee8021XPaeMIBNotifications": ieee8021XPaeMIBNotifications,
       "ieee8021XPaeMIBObjects": ieee8021XPaeMIBObjects,
       "ieee8021XPaeSystem": ieee8021XPaeSystem,
       "ieee8021XPaeSysAccessControl": ieee8021XPaeSysAccessControl,
       "ieee8021XPaeSysAnnouncements": ieee8021XPaeSysAnnouncements,
       "ieee8021XPaeSysEapolVersion": ieee8021XPaeSysEapolVersion,
       "ieee8021XPaeSysMkaVersion": ieee8021XPaeSysMkaVersion,
       "ieee8021XPaePortTable": ieee8021XPaePortTable,
       "ieee8021XPaePortEntry": ieee8021XPaePortEntry,
       "ieee8021XPaePortNumber": ieee8021XPaePortNumber,
       "ieee8021XPaePortType": ieee8021XPaePortType,
       "ieee8021XPaeControlledPortNumber": ieee8021XPaeControlledPortNumber,
       "ieee8021XPaeUncontrolledPortNumber": ieee8021XPaeUncontrolledPortNumber,
       "ieee8021XPaeCommonPortNumber": ieee8021XPaeCommonPortNumber,
       "ieee8021XPaePortInitialize": ieee8021XPaePortInitialize,
       "ieee8021XPaePortCapabilities": ieee8021XPaePortCapabilities,
       "ieee8021XPaePortVirtualPortsEnable": ieee8021XPaePortVirtualPortsEnable,
       "ieee8021XPaePortMaxVirtualPorts": ieee8021XPaePortMaxVirtualPorts,
       "ieee8021XPaePortCurrentVirtualPorts": ieee8021XPaePortCurrentVirtualPorts,
       "ieee8021XPaePortVirtualPortStart": ieee8021XPaePortVirtualPortStart,
       "ieee8021XPaePortVirtualPortPeerMAC": ieee8021XPaePortVirtualPortPeerMAC,
       "ieee8021XPaePortLogonEnable": ieee8021XPaePortLogonEnable,
       "ieee8021XPaePortAuthenticatorEnable": ieee8021XPaePortAuthenticatorEnable,
       "ieee8021XPaePortSupplicantEnable": ieee8021XPaePortSupplicantEnable,
       "ieee8021XPaePortKayMkaEnable": ieee8021XPaePortKayMkaEnable,
       "ieee8021XPaePortAnnouncerEnable": ieee8021XPaePortAnnouncerEnable,
       "ieee8021XPaePortListenerEnable": ieee8021XPaePortListenerEnable,
       "ieee8021XPaeEapolGroupMAC": ieee8021XPaeEapolGroupMAC,
       "ieee8021XPacPortTable": ieee8021XPacPortTable,
       "ieee8021XPacPortEntry": ieee8021XPacPortEntry,
       "ieee8021XPacPortControlledPortNumber": ieee8021XPacPortControlledPortNumber,
       "ieee8021XPacPortAdminPt2PtMAC": ieee8021XPacPortAdminPt2PtMAC,
       "ieee8021XPacPortOperPt2PtMAC": ieee8021XPacPortOperPt2PtMAC,
       "ieee8021XPaeLogon": ieee8021XPaeLogon,
       "ieee8021XPaePortLogonTable": ieee8021XPaePortLogonTable,
       "ieee8021XPaePortLogonEntry": ieee8021XPaePortLogonEntry,
       "ieee8021XPaePortLogonConnectStatus": ieee8021XPaePortLogonConnectStatus,
       "ieee8021XPaePortPortValid": ieee8021XPaePortPortValid,
       "ieee8021XPaePortSessionTable": ieee8021XPaePortSessionTable,
       "ieee8021XPaePortSessionEntry": ieee8021XPaePortSessionEntry,
       "ieee8021XPaeSessionControlledPortNumber": ieee8021XPaeSessionControlledPortNumber,
       "ieee8021XPaePortSessionOctetsRx": ieee8021XPaePortSessionOctetsRx,
       "ieee8021XPaePortSessionOctetsTx": ieee8021XPaePortSessionOctetsTx,
       "ieee8021XPaePortSessionPktsRx": ieee8021XPaePortSessionPktsRx,
       "ieee8021XPaePortSessionPktsTx": ieee8021XPaePortSessionPktsTx,
       "ieee8021XPaePortSessionId": ieee8021XPaePortSessionId,
       "ieee8021XPaePortSessionStartTime": ieee8021XPaePortSessionStartTime,
       "ieee8021XPaePortSessionIntervalTime": ieee8021XPaePortSessionIntervalTime,
       "ieee8021XPaePortSessionTerminate": ieee8021XPaePortSessionTerminate,
       "ieee8021XPaePortSessionUserName": ieee8021XPaePortSessionUserName,
       "ieee8021XLogonNIDTable": ieee8021XLogonNIDTable,
       "ieee8021XLogonNIDEntry": ieee8021XLogonNIDEntry,
       "ieee8021XLogonNIDConnectedNID": ieee8021XLogonNIDConnectedNID,
       "ieee8021XLogonNIDRequestedNID": ieee8021XLogonNIDRequestedNID,
       "ieee8021XLogonNIDSelectedNID": ieee8021XLogonNIDSelectedNID,
       "ieee8021XPaeAuthenticator": ieee8021XPaeAuthenticator,
       "ieee8021XAuthenticatorTable": ieee8021XAuthenticatorTable,
       "ieee8021XAuthenticatorEntry": ieee8021XAuthenticatorEntry,
       "ieee8021XAuthPaeAuthenticate": ieee8021XAuthPaeAuthenticate,
       "ieee8021XAuthPaeAuthenticated": ieee8021XAuthPaeAuthenticated,
       "ieee8021XAuthPaeFailed": ieee8021XAuthPaeFailed,
       "ieee8021XAuthPaeReAuthEnabled": ieee8021XAuthPaeReAuthEnabled,
       "ieee8021XAuthPaeQuietPeriod": ieee8021XAuthPaeQuietPeriod,
       "ieee8021XAuthPaeReauthPeriod": ieee8021XAuthPaeReauthPeriod,
       "ieee8021XAuthPaeRetryMax": ieee8021XAuthPaeRetryMax,
       "ieee8021XAuthPaeRetryCount": ieee8021XAuthPaeRetryCount,
       "ieee8021XPaeSupplicant": ieee8021XPaeSupplicant,
       "ieee8021XSupplicantTable": ieee8021XSupplicantTable,
       "ieee8021XSupplicantEntry": ieee8021XSupplicantEntry,
       "ieee8021XSuppPaeAuthenticate": ieee8021XSuppPaeAuthenticate,
       "ieee8021XSuppPaeAuthenticated": ieee8021XSuppPaeAuthenticated,
       "ieee8021XSuppPaeFailed": ieee8021XSuppPaeFailed,
       "ieee8021XSuppPaeHelloPeriod": ieee8021XSuppPaeHelloPeriod,
       "ieee8021XSuppPaeRetryMax": ieee8021XSuppPaeRetryMax,
       "ieee8021XSuppPaeRetryCount": ieee8021XSuppPaeRetryCount,
       "ieee8021XPaeEapol": ieee8021XPaeEapol,
       "ieee8021XEapolStatsTable": ieee8021XEapolStatsTable,
       "ieee8021XEapolStatsEntry": ieee8021XEapolStatsEntry,
       "ieee8021XEapolInvalidFramesRx": ieee8021XEapolInvalidFramesRx,
       "ieee8021XEapolEapLengthErrorFramesRx": ieee8021XEapolEapLengthErrorFramesRx,
       "ieee8021XEapolAnnouncementFramesRx": ieee8021XEapolAnnouncementFramesRx,
       "ieee8021XEapolAnnouncementReqFramesRx": ieee8021XEapolAnnouncementReqFramesRx,
       "ieee8021XEapolPortUnavailableFramesRx": ieee8021XEapolPortUnavailableFramesRx,
       "ieee8021XEapolStartFramesRx": ieee8021XEapolStartFramesRx,
       "ieee8021XEapolEapFramesRx": ieee8021XEapolEapFramesRx,
       "ieee8021XEapolLogoffFramesRx": ieee8021XEapolLogoffFramesRx,
       "ieee8021XEapolMkNoCknFramesRx": ieee8021XEapolMkNoCknFramesRx,
       "ieee8021XEapolMkInvalidFramesRx": ieee8021XEapolMkInvalidFramesRx,
       "ieee8021XEapolLastRxFrameVersion": ieee8021XEapolLastRxFrameVersion,
       "ieee8021XEapolLastRxFrameSource": ieee8021XEapolLastRxFrameSource,
       "ieee8021XEapolSuppEapFramesTx": ieee8021XEapolSuppEapFramesTx,
       "ieee8021XEapolLogoffFramesTx": ieee8021XEapolLogoffFramesTx,
       "ieee8021XEapolAnnouncementFramesTx": ieee8021XEapolAnnouncementFramesTx,
       "ieee8021XEapolAnnouncementReqFramesTx": ieee8021XEapolAnnouncementReqFramesTx,
       "ieee8021XEapolStartFramesTx": ieee8021XEapolStartFramesTx,
       "ieee8021XEapolAuthEapFramesTx": ieee8021XEapolAuthEapFramesTx,
       "ieee8021XEapolMkaFramesTx": ieee8021XEapolMkaFramesTx,
       "ieee8021XPaeKaY": ieee8021XPaeKaY,
       "ieee8021XKayMkaTable": ieee8021XKayMkaTable,
       "ieee8021XKayMkaEntry": ieee8021XKayMkaEntry,
       "ieee8021XKayMkaActive": ieee8021XKayMkaActive,
       "ieee8021XKayMkaAuthenticated": ieee8021XKayMkaAuthenticated,
       "ieee8021XKayMkaSecured": ieee8021XKayMkaSecured,
       "ieee8021XKayMkaFailed": ieee8021XKayMkaFailed,
       "ieee8021XKayMkaActorSCI": ieee8021XKayMkaActorSCI,
       "ieee8021XKayMkaActorsPriority": ieee8021XKayMkaActorsPriority,
       "ieee8021XKayMkaKeyServerPriority": ieee8021XKayMkaKeyServerPriority,
       "ieee8021XKayMkaKeyServerSCI": ieee8021XKayMkaKeyServerSCI,
       "ieee8021XKayAllowedJoinGroup": ieee8021XKayAllowedJoinGroup,
       "ieee8021XKayAllowedFormGroup": ieee8021XKayAllowedFormGroup,
       "ieee8021XKayCreateNewGroup": ieee8021XKayCreateNewGroup,
       "ieee8021XKayMacSecCapability": ieee8021XKayMacSecCapability,
       "ieee8021XKayMacSecDesired": ieee8021XKayMacSecDesired,
       "ieee8021XKayMacSecProtect": ieee8021XKayMacSecProtect,
       "ieee8021XKayMacSecReplayProtect": ieee8021XKayMacSecReplayProtect,
       "ieee8021XKayMacSecValidate": ieee8021XKayMacSecValidate,
       "ieee8021XKayMacSecConfidentialityOffset": ieee8021XKayMacSecConfidentialityOffset,
       "ieee8021XKayMkaTxKN": ieee8021XKayMkaTxKN,
       "ieee8021XKayMkaTxAN": ieee8021XKayMkaTxAN,
       "ieee8021XKayMkaRxKN": ieee8021XKayMkaRxKN,
       "ieee8021XKayMkaRxAN": ieee8021XKayMkaRxAN,
       "ieee8021XKayMkaSuspendFor": ieee8021XKayMkaSuspendFor,
       "ieee8021XKayMkaSuspendOnRequest": ieee8021XKayMkaSuspendOnRequest,
       "ieee8021XKayMkaSuspendedWhile": ieee8021XKayMkaSuspendedWhile,
       "ieee8021XKayMkaParticipantTable": ieee8021XKayMkaParticipantTable,
       "ieee8021XKayMkaParticipantEntry": ieee8021XKayMkaParticipantEntry,
       "ieee8021XKayMkaPartCKN": ieee8021XKayMkaPartCKN,
       "ieee8021XKayMkaPartKMD": ieee8021XKayMkaPartKMD,
       "ieee8021XKayMkaPartNID": ieee8021XKayMkaPartNID,
       "ieee8021XKayMkaPartCached": ieee8021XKayMkaPartCached,
       "ieee8021XKayMkaPartActive": ieee8021XKayMkaPartActive,
       "ieee8021XKayMkaPartRetain": ieee8021XKayMkaPartRetain,
       "ieee8021XKayMkaPartActivateControl": ieee8021XKayMkaPartActivateControl,
       "ieee8021XKayMkaPartPrincipal": ieee8021XKayMkaPartPrincipal,
       "ieee8021XKayMkaPartDistCKN": ieee8021XKayMkaPartDistCKN,
       "ieee8021XKayMkaPartRowStatus": ieee8021XKayMkaPartRowStatus,
       "ieee8021XKayMkaPeerListTable": ieee8021XKayMkaPeerListTable,
       "ieee8021XKayMkaPeerListEntry": ieee8021XKayMkaPeerListEntry,
       "ieee8021XKayMkaPeerListMI": ieee8021XKayMkaPeerListMI,
       "ieee8021XKayMkaPeerListMN": ieee8021XKayMkaPeerListMN,
       "ieee8021XKayMkaPeerListType": ieee8021XKayMkaPeerListType,
       "ieee8021XKayMkaPeerListSCI": ieee8021XKayMkaPeerListSCI,
       "ieee8021XPaeNetworkIdentifier": ieee8021XPaeNetworkIdentifier,
       "ieee8021XNidConfigTable": ieee8021XNidConfigTable,
       "ieee8021XNidConfigEntry": ieee8021XNidConfigEntry,
       "ieee8021XNidNID": ieee8021XNidNID,
       "ieee8021XNidUseEap": ieee8021XNidUseEap,
       "ieee8021XNidUnauthAllowed": ieee8021XNidUnauthAllowed,
       "ieee8021XNidUnsecuredAllowed": ieee8021XNidUnsecuredAllowed,
       "ieee8021XNidUnauthenticatedAccess": ieee8021XNidUnauthenticatedAccess,
       "ieee8021XNidAccessCapabilities": ieee8021XNidAccessCapabilities,
       "ieee8021XNidKMD": ieee8021XNidKMD,
       "ieee8021XNidRowStatus": ieee8021XNidRowStatus,
       "ieee8021XAnnounceTable": ieee8021XAnnounceTable,
       "ieee8021XAnnounceEntry": ieee8021XAnnounceEntry,
       "ieee8021XAnnounceNID": ieee8021XAnnounceNID,
       "ieee8021XAnnounceAccessStatus": ieee8021XAnnounceAccessStatus,
       "ieee8021XAnnouncementTable": ieee8021XAnnouncementTable,
       "ieee8021XAnnouncementEntry": ieee8021XAnnouncementEntry,
       "ieee8021XAnnouncementNID": ieee8021XAnnouncementNID,
       "ieee8021XAnnouncementKMD": ieee8021XAnnouncementKMD,
       "ieee8021XAnnouncementSpecific": ieee8021XAnnouncementSpecific,
       "ieee8021XAnnouncementAccessStatus": ieee8021XAnnouncementAccessStatus,
       "ieee8021XAnnouncementAccessRequested": ieee8021XAnnouncementAccessRequested,
       "ieee8021XAnnouncementUnauthAccess": ieee8021XAnnouncementUnauthAccess,
       "ieee8021XAnnouncementCapabilities": ieee8021XAnnouncementCapabilities,
       "ieee8021XAnnouncementCipherSuitesTable": ieee8021XAnnouncementCipherSuitesTable,
       "ieee8021XAnnouncementCipherSuitesEntry": ieee8021XAnnouncementCipherSuitesEntry,
       "ieee8021XAnnouncementCipherSuite": ieee8021XAnnouncementCipherSuite,
       "ieee8021XAnnouncementCipherCapability": ieee8021XAnnouncementCipherCapability,
       "ieee8021XPaeMIBConformance": ieee8021XPaeMIBConformance,
       "ieee8021XPaeCompliances": ieee8021XPaeCompliances,
       "ieee8021XPaeCompliance": ieee8021XPaeCompliance,
       "ieee8021XPaeV2Compliance": ieee8021XPaeV2Compliance,
       "ieee8021XPaeGroups": ieee8021XPaeGroups,
       "ieee8021XPaeSystemGroup": ieee8021XPaeSystemGroup,
       "ieee8021XPacGroup": ieee8021XPacGroup,
       "ieee8021XPaeLogonGroup": ieee8021XPaeLogonGroup,
       "ieee8021XPaeAuthConfigGroup": ieee8021XPaeAuthConfigGroup,
       "ieee8021XPaeSuppConfigGroup": ieee8021XPaeSuppConfigGroup,
       "ieee8021XPaeEapolStatsGroup": ieee8021XPaeEapolStatsGroup,
       "ieee8021XPaeKaYMkaGroup": ieee8021XPaeKaYMkaGroup,
       "ieee8021XPaeNetworkIdentifierGroup": ieee8021XPaeNetworkIdentifierGroup,
       "ieee8021XPaeAnnouncerGroup": ieee8021XPaeAnnouncerGroup,
       "ieee8021XPaeListenerGroup": ieee8021XPaeListenerGroup,
       "ieee8021XPaeKaYIsupgradeGroup": ieee8021XPaeKaYIsupgradeGroup,
       "ieee8021XPaeSystemAddGroup": ieee8021XPaeSystemAddGroup}
)
