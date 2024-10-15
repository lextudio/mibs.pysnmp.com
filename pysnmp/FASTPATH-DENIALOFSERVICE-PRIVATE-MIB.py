# SNMP MIB module (FASTPATH-DENIALOFSERVICE-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTPATH-DENIALOFSERVICE-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:45 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "BROADCOM-REF-MIB",
    "fastPath")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathDenialOfService = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31)
)
fastPathDenialOfService.setRevisions(
        ("2007-05-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentSwitchDenialOfServiceGroup_ObjectIdentity = ObjectIdentity
agentSwitchDenialOfServiceGroup = _AgentSwitchDenialOfServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1)
)


class _AgentSwitchDenialOfServiceSIPDIPMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceSIPDIPMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceSIPDIPMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceSIPDIPMode_Object = MibScalar
agentSwitchDenialOfServiceSIPDIPMode = _AgentSwitchDenialOfServiceSIPDIPMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 1),
    _AgentSwitchDenialOfServiceSIPDIPMode_Type()
)
agentSwitchDenialOfServiceSIPDIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceSIPDIPMode.setStatus("current")


class _AgentSwitchDenialOfServiceFirstFragMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceFirstFragMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceFirstFragMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceFirstFragMode_Object = MibScalar
agentSwitchDenialOfServiceFirstFragMode = _AgentSwitchDenialOfServiceFirstFragMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 2),
    _AgentSwitchDenialOfServiceFirstFragMode_Type()
)
agentSwitchDenialOfServiceFirstFragMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceFirstFragMode.setStatus("current")


class _AgentSwitchDenialOfServiceTCPHdrSize_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPHdrSize based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentSwitchDenialOfServiceTCPHdrSize_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPHdrSize_Object = MibScalar
agentSwitchDenialOfServiceTCPHdrSize = _AgentSwitchDenialOfServiceTCPHdrSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 3),
    _AgentSwitchDenialOfServiceTCPHdrSize_Type()
)
agentSwitchDenialOfServiceTCPHdrSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPHdrSize.setStatus("current")


class _AgentSwitchDenialOfServiceTCPFragMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPFragMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceTCPFragMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPFragMode_Object = MibScalar
agentSwitchDenialOfServiceTCPFragMode = _AgentSwitchDenialOfServiceTCPFragMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 4),
    _AgentSwitchDenialOfServiceTCPFragMode_Type()
)
agentSwitchDenialOfServiceTCPFragMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPFragMode.setStatus("current")


class _AgentSwitchDenialOfServiceTCPFlagMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPFlagMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceTCPFlagMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPFlagMode_Object = MibScalar
agentSwitchDenialOfServiceTCPFlagMode = _AgentSwitchDenialOfServiceTCPFlagMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 5),
    _AgentSwitchDenialOfServiceTCPFlagMode_Type()
)
agentSwitchDenialOfServiceTCPFlagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPFlagMode.setStatus("current")


class _AgentSwitchDenialOfServiceL4PortMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceL4PortMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceL4PortMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceL4PortMode_Object = MibScalar
agentSwitchDenialOfServiceL4PortMode = _AgentSwitchDenialOfServiceL4PortMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 6),
    _AgentSwitchDenialOfServiceL4PortMode_Type()
)
agentSwitchDenialOfServiceL4PortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceL4PortMode.setStatus("current")


class _AgentSwitchDenialOfServiceICMPMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceICMPMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceICMPMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceICMPMode_Object = MibScalar
agentSwitchDenialOfServiceICMPMode = _AgentSwitchDenialOfServiceICMPMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 7),
    _AgentSwitchDenialOfServiceICMPMode_Type()
)
agentSwitchDenialOfServiceICMPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceICMPMode.setStatus("current")


class _AgentSwitchDenialOfServiceICMPSize_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceICMPSize based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16376),
    )


_AgentSwitchDenialOfServiceICMPSize_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceICMPSize_Object = MibScalar
agentSwitchDenialOfServiceICMPSize = _AgentSwitchDenialOfServiceICMPSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 8),
    _AgentSwitchDenialOfServiceICMPSize_Type()
)
agentSwitchDenialOfServiceICMPSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceICMPSize.setStatus("current")


class _AgentSwitchDenialOfServiceSMACDMACMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceSMACDMACMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceSMACDMACMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceSMACDMACMode_Object = MibScalar
agentSwitchDenialOfServiceSMACDMACMode = _AgentSwitchDenialOfServiceSMACDMACMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 9),
    _AgentSwitchDenialOfServiceSMACDMACMode_Type()
)
agentSwitchDenialOfServiceSMACDMACMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceSMACDMACMode.setStatus("current")


class _AgentSwitchDenialOfServiceTCPOffsetMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPOffsetMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceTCPOffsetMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPOffsetMode_Object = MibScalar
agentSwitchDenialOfServiceTCPOffsetMode = _AgentSwitchDenialOfServiceTCPOffsetMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 10),
    _AgentSwitchDenialOfServiceTCPOffsetMode_Type()
)
agentSwitchDenialOfServiceTCPOffsetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPOffsetMode.setStatus("current")


class _AgentSwitchDenialOfServiceTCPFlagSeqMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPFlagSeqMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceTCPFlagSeqMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPFlagSeqMode_Object = MibScalar
agentSwitchDenialOfServiceTCPFlagSeqMode = _AgentSwitchDenialOfServiceTCPFlagSeqMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 11),
    _AgentSwitchDenialOfServiceTCPFlagSeqMode_Type()
)
agentSwitchDenialOfServiceTCPFlagSeqMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPFlagSeqMode.setStatus("current")


class _AgentSwitchDenialOfServiceTCPPortMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPPortMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceTCPPortMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPPortMode_Object = MibScalar
agentSwitchDenialOfServiceTCPPortMode = _AgentSwitchDenialOfServiceTCPPortMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 12),
    _AgentSwitchDenialOfServiceTCPPortMode_Type()
)
agentSwitchDenialOfServiceTCPPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPPortMode.setStatus("current")


class _AgentSwitchDenialOfServiceUDPPortMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceUDPPortMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceUDPPortMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceUDPPortMode_Object = MibScalar
agentSwitchDenialOfServiceUDPPortMode = _AgentSwitchDenialOfServiceUDPPortMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 13),
    _AgentSwitchDenialOfServiceUDPPortMode_Type()
)
agentSwitchDenialOfServiceUDPPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceUDPPortMode.setStatus("current")


class _AgentSwitchDenialOfServiceTCPSynMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPSynMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceTCPSynMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPSynMode_Object = MibScalar
agentSwitchDenialOfServiceTCPSynMode = _AgentSwitchDenialOfServiceTCPSynMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 14),
    _AgentSwitchDenialOfServiceTCPSynMode_Type()
)
agentSwitchDenialOfServiceTCPSynMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPSynMode.setStatus("current")


class _AgentSwitchDenialOfServiceTCPSynFinMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPSynFinMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceTCPSynFinMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPSynFinMode_Object = MibScalar
agentSwitchDenialOfServiceTCPSynFinMode = _AgentSwitchDenialOfServiceTCPSynFinMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 15),
    _AgentSwitchDenialOfServiceTCPSynFinMode_Type()
)
agentSwitchDenialOfServiceTCPSynFinMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPSynFinMode.setStatus("current")


class _AgentSwitchDenialOfServiceTCPFinUrgPshMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPFinUrgPshMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceTCPFinUrgPshMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPFinUrgPshMode_Object = MibScalar
agentSwitchDenialOfServiceTCPFinUrgPshMode = _AgentSwitchDenialOfServiceTCPFinUrgPshMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 16),
    _AgentSwitchDenialOfServiceTCPFinUrgPshMode_Type()
)
agentSwitchDenialOfServiceTCPFinUrgPshMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPFinUrgPshMode.setStatus("current")


class _AgentSwitchDenialOfServiceICMPv6Size_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceICMPv6Size based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AgentSwitchDenialOfServiceICMPv6Size_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceICMPv6Size_Object = MibScalar
agentSwitchDenialOfServiceICMPv6Size = _AgentSwitchDenialOfServiceICMPv6Size_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 18),
    _AgentSwitchDenialOfServiceICMPv6Size_Type()
)
agentSwitchDenialOfServiceICMPv6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceICMPv6Size.setStatus("current")


class _AgentSwitchDenialOfServiceICMPFragMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceICMPFragMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceICMPFragMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceICMPFragMode_Object = MibScalar
agentSwitchDenialOfServiceICMPFragMode = _AgentSwitchDenialOfServiceICMPFragMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 31, 1, 19),
    _AgentSwitchDenialOfServiceICMPFragMode_Type()
)
agentSwitchDenialOfServiceICMPFragMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceICMPFragMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-DENIALOFSERVICE-PRIVATE-MIB",
    **{"fastPathDenialOfService": fastPathDenialOfService,
       "agentSwitchDenialOfServiceGroup": agentSwitchDenialOfServiceGroup,
       "agentSwitchDenialOfServiceSIPDIPMode": agentSwitchDenialOfServiceSIPDIPMode,
       "agentSwitchDenialOfServiceFirstFragMode": agentSwitchDenialOfServiceFirstFragMode,
       "agentSwitchDenialOfServiceTCPHdrSize": agentSwitchDenialOfServiceTCPHdrSize,
       "agentSwitchDenialOfServiceTCPFragMode": agentSwitchDenialOfServiceTCPFragMode,
       "agentSwitchDenialOfServiceTCPFlagMode": agentSwitchDenialOfServiceTCPFlagMode,
       "agentSwitchDenialOfServiceL4PortMode": agentSwitchDenialOfServiceL4PortMode,
       "agentSwitchDenialOfServiceICMPMode": agentSwitchDenialOfServiceICMPMode,
       "agentSwitchDenialOfServiceICMPSize": agentSwitchDenialOfServiceICMPSize,
       "agentSwitchDenialOfServiceSMACDMACMode": agentSwitchDenialOfServiceSMACDMACMode,
       "agentSwitchDenialOfServiceTCPOffsetMode": agentSwitchDenialOfServiceTCPOffsetMode,
       "agentSwitchDenialOfServiceTCPFlagSeqMode": agentSwitchDenialOfServiceTCPFlagSeqMode,
       "agentSwitchDenialOfServiceTCPPortMode": agentSwitchDenialOfServiceTCPPortMode,
       "agentSwitchDenialOfServiceUDPPortMode": agentSwitchDenialOfServiceUDPPortMode,
       "agentSwitchDenialOfServiceTCPSynMode": agentSwitchDenialOfServiceTCPSynMode,
       "agentSwitchDenialOfServiceTCPSynFinMode": agentSwitchDenialOfServiceTCPSynFinMode,
       "agentSwitchDenialOfServiceTCPFinUrgPshMode": agentSwitchDenialOfServiceTCPFinUrgPshMode,
       "agentSwitchDenialOfServiceICMPv6Size": agentSwitchDenialOfServiceICMPv6Size,
       "agentSwitchDenialOfServiceICMPFragMode": agentSwitchDenialOfServiceICMPFragMode}
)
