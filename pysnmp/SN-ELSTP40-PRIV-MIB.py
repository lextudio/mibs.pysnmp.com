# SNMP MIB module (SN-ELSTP40-PRIV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SN-ELSTP40-PRIV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:42 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 enterprises,
 internet,
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
    "internet",
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

_Ad_ObjectIdentity = ObjectIdentity
ad = _Ad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196)
)
_AdProductMibs_ObjectIdentity = ObjectIdentity
adProductMibs = _AdProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1)
)
_SimaticNet_ObjectIdentity = ObjectIdentity
simaticNet = _SimaticNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1)
)
_IHub_ObjectIdentity = ObjectIdentity
iHub = _IHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 1)
)
_ISwitch_ObjectIdentity = ObjectIdentity
iSwitch = _ISwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2)
)
_ILeanSwitch_ObjectIdentity = ObjectIdentity
iLeanSwitch = _ILeanSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3)
)
_ElsTP40M_ObjectIdentity = ObjectIdentity
elsTP40M = _ElsTP40M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1)
)
_ElsInfo_ObjectIdentity = ObjectIdentity
elsInfo = _ElsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 1)
)


class _Version_Type(DisplayString):
    """Custom type version based on DisplayString"""
    defaultValue = OctetString("V1.0.0.0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_Version_Type.__name__ = "DisplayString"
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 1, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("mandatory")


class _Hardware_Type(DisplayString):
    """Custom type hardware based on DisplayString"""
    defaultValue = OctetString("01")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_Hardware_Type.__name__ = "DisplayString"
_Hardware_Object = MibScalar
hardware = _Hardware_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 1, 2),
    _Hardware_Type()
)
hardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware.setStatus("mandatory")
_ElsStatus_ObjectIdentity = ObjectIdentity
elsStatus = _ElsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2)
)


class _ReceiveError1_Type(Integer32):
    """Custom type receiveError1 based on Integer32"""
    defaultValue = 0


_ReceiveError1_Object = MibScalar
receiveError1 = _ReceiveError1_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 1),
    _ReceiveError1_Type()
)
receiveError1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveError1.setStatus("mandatory")


class _ReceiveError2_Type(Integer32):
    """Custom type receiveError2 based on Integer32"""
    defaultValue = 0


_ReceiveError2_Object = MibScalar
receiveError2 = _ReceiveError2_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 2),
    _ReceiveError2_Type()
)
receiveError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveError2.setStatus("mandatory")


class _ReceiveError3_Type(Integer32):
    """Custom type receiveError3 based on Integer32"""
    defaultValue = 0


_ReceiveError3_Object = MibScalar
receiveError3 = _ReceiveError3_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 3),
    _ReceiveError3_Type()
)
receiveError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveError3.setStatus("mandatory")


class _ReceiveError4_Type(Integer32):
    """Custom type receiveError4 based on Integer32"""
    defaultValue = 0


_ReceiveError4_Object = MibScalar
receiveError4 = _ReceiveError4_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 4),
    _ReceiveError4_Type()
)
receiveError4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveError4.setStatus("mandatory")


class _CollisionCount1_Type(Integer32):
    """Custom type collisionCount1 based on Integer32"""
    defaultValue = 0


_CollisionCount1_Object = MibScalar
collisionCount1 = _CollisionCount1_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 5),
    _CollisionCount1_Type()
)
collisionCount1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collisionCount1.setStatus("mandatory")


class _CollisionCount2_Type(Integer32):
    """Custom type collisionCount2 based on Integer32"""
    defaultValue = 0


_CollisionCount2_Object = MibScalar
collisionCount2 = _CollisionCount2_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 6),
    _CollisionCount2_Type()
)
collisionCount2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collisionCount2.setStatus("mandatory")


class _CollisionCount3_Type(Integer32):
    """Custom type collisionCount3 based on Integer32"""
    defaultValue = 0


_CollisionCount3_Object = MibScalar
collisionCount3 = _CollisionCount3_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 7),
    _CollisionCount3_Type()
)
collisionCount3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collisionCount3.setStatus("mandatory")


class _CollisionCount4_Type(Integer32):
    """Custom type collisionCount4 based on Integer32"""
    defaultValue = 0


_CollisionCount4_Object = MibScalar
collisionCount4 = _CollisionCount4_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 8),
    _CollisionCount4_Type()
)
collisionCount4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collisionCount4.setStatus("mandatory")


class _LedStatus_Type(Integer32):
    """Custom type ledStatus based on Integer32"""
    defaultValue = 0


_LedStatus_Object = MibScalar
ledStatus = _LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 9),
    _LedStatus_Type()
)
ledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledStatus.setStatus("mandatory")


class _StartBank_Type(Integer32):
    """Custom type startBank based on Integer32"""
    defaultValue = 0


_StartBank_Object = MibScalar
startBank = _StartBank_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 10),
    _StartBank_Type()
)
startBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startBank.setStatus("mandatory")
_ElsMail_ObjectIdentity = ObjectIdentity
elsMail = _ElsMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 3)
)


class _EmailFrom_Type(DisplayString):
    """Custom type emailFrom based on DisplayString"""
    defaultValue = OctetString("owner@anywhere.com")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_EmailFrom_Type.__name__ = "DisplayString"
_EmailFrom_Object = MibScalar
emailFrom = _EmailFrom_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 3, 1),
    _EmailFrom_Type()
)
emailFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailFrom.setStatus("mandatory")


class _EmailTo_Type(DisplayString):
    """Custom type emailTo based on DisplayString"""
    defaultValue = OctetString("test@els.com")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_EmailTo_Type.__name__ = "DisplayString"
_EmailTo_Object = MibScalar
emailTo = _EmailTo_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 3, 2),
    _EmailTo_Type()
)
emailTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailTo.setStatus("mandatory")


class _EmailSubject_Type(DisplayString):
    """Custom type emailSubject based on DisplayString"""
    defaultValue = OctetString("test@els.com")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_EmailSubject_Type.__name__ = "DisplayString"
_EmailSubject_Object = MibScalar
emailSubject = _EmailSubject_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 3, 3),
    _EmailSubject_Type()
)
emailSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emailSubject.setStatus("mandatory")


class _SmtpdIP_Type(IpAddress):
    """Custom type smtpdIP based on IpAddress"""
    defaultValue = 0


_SmtpdIP_Object = MibScalar
smtpdIP = _SmtpdIP_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 3, 4),
    _SmtpdIP_Type()
)
smtpdIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpdIP.setStatus("mandatory")
_ElsTrap_ObjectIdentity = ObjectIdentity
elsTrap = _ElsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 4)
)


class _TrapIP1_Type(IpAddress):
    """Custom type trapIP1 based on IpAddress"""
    defaultValue = 0


_TrapIP1_Object = MibScalar
trapIP1 = _TrapIP1_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 4, 1),
    _TrapIP1_Type()
)
trapIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP1.setStatus("mandatory")


class _TrapIP2_Type(IpAddress):
    """Custom type trapIP2 based on IpAddress"""
    defaultValue = 0


_TrapIP2_Object = MibScalar
trapIP2 = _TrapIP2_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 4, 2),
    _TrapIP2_Type()
)
trapIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP2.setStatus("mandatory")
_ElsEvents_ObjectIdentity = ObjectIdentity
elsEvents = _ElsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 5)
)


class _EmailMask_Type(Integer32):
    """Custom type emailMask based on Integer32"""
    defaultValue = 0


_EmailMask_Object = MibScalar
emailMask = _EmailMask_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 5, 1),
    _EmailMask_Type()
)
emailMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailMask.setStatus("mandatory")


class _TrapMask_Type(Integer32):
    """Custom type trapMask based on Integer32"""
    defaultValue = 0


_TrapMask_Object = MibScalar
trapMask = _TrapMask_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 5, 2),
    _TrapMask_Type()
)
trapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapMask.setStatus("mandatory")


class _OtherMask_Type(Integer32):
    """Custom type otherMask based on Integer32"""
    defaultValue = 0


_OtherMask_Object = MibScalar
otherMask = _OtherMask_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 5, 3),
    _OtherMask_Type()
)
otherMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otherMask.setStatus("mandatory")
_ElsIPInfo_ObjectIdentity = ObjectIdentity
elsIPInfo = _ElsIPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 6)
)


class _OwnIP_Type(IpAddress):
    """Custom type ownIP based on IpAddress"""
    defaultValue = 0


_OwnIP_Object = MibScalar
ownIP = _OwnIP_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 6, 1),
    _OwnIP_Type()
)
ownIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ownIP.setStatus("mandatory")


class _NetMask_Type(IpAddress):
    """Custom type netMask based on IpAddress"""
    defaultValue = 0


_NetMask_Object = MibScalar
netMask = _NetMask_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 6, 2),
    _NetMask_Type()
)
netMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMask.setStatus("mandatory")


class _Gateway_Type(IpAddress):
    """Custom type gateway based on IpAddress"""
    defaultValue = 0


_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 6, 3),
    _Gateway_Type()
)
gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway.setStatus("mandatory")


class _FromDHCP_Type(Integer32):
    """Custom type fromDHCP based on Integer32"""
    defaultValue = 0


_FromDHCP_Object = MibScalar
fromDHCP = _FromDHCP_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 6, 4),
    _FromDHCP_Type()
)
fromDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fromDHCP.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SN-ELSTP40-PRIV-MIB",
    **{"ad": ad,
       "adProductMibs": adProductMibs,
       "simaticNet": simaticNet,
       "iHub": iHub,
       "iSwitch": iSwitch,
       "iLeanSwitch": iLeanSwitch,
       "elsTP40M": elsTP40M,
       "elsInfo": elsInfo,
       "version": version,
       "hardware": hardware,
       "elsStatus": elsStatus,
       "receiveError1": receiveError1,
       "receiveError2": receiveError2,
       "receiveError3": receiveError3,
       "receiveError4": receiveError4,
       "collisionCount1": collisionCount1,
       "collisionCount2": collisionCount2,
       "collisionCount3": collisionCount3,
       "collisionCount4": collisionCount4,
       "ledStatus": ledStatus,
       "startBank": startBank,
       "elsMail": elsMail,
       "emailFrom": emailFrom,
       "emailTo": emailTo,
       "emailSubject": emailSubject,
       "smtpdIP": smtpdIP,
       "elsTrap": elsTrap,
       "trapIP1": trapIP1,
       "trapIP2": trapIP2,
       "elsEvents": elsEvents,
       "emailMask": emailMask,
       "trapMask": trapMask,
       "otherMask": otherMask,
       "elsIPInfo": elsIPInfo,
       "ownIP": ownIP,
       "netMask": netMask,
       "gateway": gateway,
       "fromDHCP": fromDHCP}
)
