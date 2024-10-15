# SNMP MIB module (RUCKUS-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:41 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ruckusCommonL2TPModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonL2TPModule")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusL2TPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusL2TPObjects_ObjectIdentity = ObjectIdentity
ruckusL2TPObjects = _RuckusL2TPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1)
)
_RuckusL2TPInfo_ObjectIdentity = ObjectIdentity
ruckusL2TPInfo = _RuckusL2TPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1, 1)
)


class _RuckusL2TPServiceStatus_Type(Integer32):
    """Custom type ruckusL2TPServiceStatus based on Integer32"""

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


_RuckusL2TPServiceStatus_Type.__name__ = "Integer32"
_RuckusL2TPServiceStatus_Object = MibScalar
ruckusL2TPServiceStatus = _RuckusL2TPServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1, 1, 1),
    _RuckusL2TPServiceStatus_Type()
)
ruckusL2TPServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusL2TPServiceStatus.setStatus("current")


class _RuckusL2TPConnectionStatus_Type(Integer32):
    """Custom type ruckusL2TPConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disabled", 3),
          ("disconnected", 2))
    )


_RuckusL2TPConnectionStatus_Type.__name__ = "Integer32"
_RuckusL2TPConnectionStatus_Object = MibScalar
ruckusL2TPConnectionStatus = _RuckusL2TPConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1, 1, 2),
    _RuckusL2TPConnectionStatus_Type()
)
ruckusL2TPConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusL2TPConnectionStatus.setStatus("current")
_RuckusL2TPServerIP_Type = IpAddress
_RuckusL2TPServerIP_Object = MibScalar
ruckusL2TPServerIP = _RuckusL2TPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1, 1, 3),
    _RuckusL2TPServerIP_Type()
)
ruckusL2TPServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusL2TPServerIP.setStatus("current")
_RuckusL2TPSharedSecret_Type = DisplayString
_RuckusL2TPSharedSecret_Object = MibScalar
ruckusL2TPSharedSecret = _RuckusL2TPSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1, 1, 4),
    _RuckusL2TPSharedSecret_Type()
)
ruckusL2TPSharedSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusL2TPSharedSecret.setStatus("current")
_RuckusL2TPUserName_Type = DisplayString
_RuckusL2TPUserName_Object = MibScalar
ruckusL2TPUserName = _RuckusL2TPUserName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1, 1, 5),
    _RuckusL2TPUserName_Type()
)
ruckusL2TPUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusL2TPUserName.setStatus("current")
_RuckusL2TPPassword_Type = DisplayString
_RuckusL2TPPassword_Object = MibScalar
ruckusL2TPPassword = _RuckusL2TPPassword_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1, 1, 6),
    _RuckusL2TPPassword_Type()
)
ruckusL2TPPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusL2TPPassword.setStatus("current")
_RuckusL2TPIfIPAddr_Type = IpAddress
_RuckusL2TPIfIPAddr_Object = MibScalar
ruckusL2TPIfIPAddr = _RuckusL2TPIfIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1, 1, 7),
    _RuckusL2TPIfIPAddr_Type()
)
ruckusL2TPIfIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusL2TPIfIPAddr.setStatus("current")
_RuckusL2TPIfNetMask_Type = IpAddress
_RuckusL2TPIfNetMask_Object = MibScalar
ruckusL2TPIfNetMask = _RuckusL2TPIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1, 1, 8),
    _RuckusL2TPIfNetMask_Type()
)
ruckusL2TPIfNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusL2TPIfNetMask.setStatus("current")
_RuckusL2TPIfGateway_Type = IpAddress
_RuckusL2TPIfGateway_Object = MibScalar
ruckusL2TPIfGateway = _RuckusL2TPIfGateway_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 1, 1, 9),
    _RuckusL2TPIfGateway_Type()
)
ruckusL2TPIfGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusL2TPIfGateway.setStatus("current")
_RuckusL2TPEvents_ObjectIdentity = ObjectIdentity
ruckusL2TPEvents = _RuckusL2TPEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-L2TP-MIB",
    **{"ruckusL2TPMIB": ruckusL2TPMIB,
       "ruckusL2TPObjects": ruckusL2TPObjects,
       "ruckusL2TPInfo": ruckusL2TPInfo,
       "ruckusL2TPServiceStatus": ruckusL2TPServiceStatus,
       "ruckusL2TPConnectionStatus": ruckusL2TPConnectionStatus,
       "ruckusL2TPServerIP": ruckusL2TPServerIP,
       "ruckusL2TPSharedSecret": ruckusL2TPSharedSecret,
       "ruckusL2TPUserName": ruckusL2TPUserName,
       "ruckusL2TPPassword": ruckusL2TPPassword,
       "ruckusL2TPIfIPAddr": ruckusL2TPIfIPAddr,
       "ruckusL2TPIfNetMask": ruckusL2TPIfNetMask,
       "ruckusL2TPIfGateway": ruckusL2TPIfGateway,
       "ruckusL2TPEvents": ruckusL2TPEvents}
)
